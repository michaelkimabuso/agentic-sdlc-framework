from contextlib import redirect_stdout
import io
import importlib.util
from pathlib import Path
import json
import shutil
import tempfile
import unittest


INSTALLER_PATH = Path(__file__).resolve().parents[1] / "install.py"
SPEC = importlib.util.spec_from_file_location("codex_install", INSTALLER_PATH)
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "framework"
        self.target = self.base / "project"
        self.source.mkdir()
        self.target.mkdir()
        self.copy_source()
        self.original_root = installer.ROOT
        installer.ROOT = self.source
        self.addCleanup(setattr, installer, "ROOT", self.original_root)

    def copy_source(self):
        repository = INSTALLER_PATH.parents[2]
        for name in ("skills", "templates", "workflows", ".agentic-sdlc", "adapters/codex"):
            shutil.copytree(repository / name, self.source / name,
                            ignore=shutil.ignore_patterns("tests", "__pycache__"))
        shutil.copy(repository / "VERSION", self.source / "VERSION")

    def install(self, update=False, accept_resolved=None):
        return installer.install(self.target, update=update, accept_resolved=accept_resolved)

    def test_fresh_install_has_all_seven_skills_and_shared_resources(self):
        self.install()
        expected_skills = {
            "intent", "product-breakdown", "specification", "planning",
            "plan-review", "implementation", "code-review",
        }
        installed = {p.parent.name for p in (self.target / ".agents/skills").glob("*/SKILL.md")}
        self.assertEqual(installed, expected_skills)
        for skill in expected_skills:
            self.assertEqual(
                (self.target / f".agents/skills/{skill}/SKILL.md").read_bytes(),
                (self.source / f"skills/{skill}/SKILL.md").read_bytes(),
            )
        self.assertEqual(
            (self.target / ".agentic-sdlc/principles/engineering-principles.md").read_bytes(),
            (self.source / ".agentic-sdlc/principles/engineering-principles.md").read_bytes(),
        )
        self.assertEqual(
            (self.target / ".agentic-sdlc/workflows/idea-to-pr.md").read_bytes(),
            (self.source / "workflows/idea-to-pr.md").read_bytes(),
        )
        for template in (self.source / "templates").glob("*.md"):
            self.assertEqual(
                (self.target / ".agentic-sdlc/templates" / template.name).read_bytes(),
                template.read_bytes(),
            )
        agents = (self.target / "AGENTS.md").read_text()
        self.assertIn(installer.START, agents)
        self.assertIn("Agentic SDLC Framework (Codex)", agents)
        manifest = json.loads((self.target / installer.MANIFEST).read_text())
        self.assertEqual(manifest["version"], (self.source / "VERSION").read_text().strip())

    def test_reinstallation_is_byte_for_byte_idempotent(self):
        self.install()
        before = self.snapshot()
        self.install()
        self.assertEqual(before, self.snapshot())
        agents = (self.target / "AGENTS.md").read_text()
        self.assertEqual(agents.count(installer.START), 1)

    def test_existing_user_agents_is_preserved_and_integrated_once(self):
        original = "# Project instructions\n\nKeep this guidance.\n"
        (self.target / "AGENTS.md").write_text(original)
        self.install()
        agents = (self.target / "AGENTS.md").read_text()
        self.assertTrue(agents.startswith(original))
        self.install()
        self.assertEqual(agents, (self.target / "AGENTS.md").read_text())

    def test_update_changes_unmodified_files_and_preserves_customized_files(self):
        self.install()
        managed = self.target / ".agents/skills/intent/SKILL.md"
        customized = self.target / ".agentic-sdlc/templates/plan.md"
        customized.write_text(customized.read_text() + "\nlocal note\n")
        agents_path = self.target / "AGENTS.md"
        agents_path.write_text("# User preface\n\n" + agents_path.read_text())
        (self.source / "VERSION").write_text("0.2.0-dev\n")
        upstream_skill = self.source / "skills/intent/SKILL.md"
        upstream_skill.write_text(upstream_skill.read_text() + "\nupstream change\n")
        upstream_plan = self.source / "templates/plan.md"
        upstream_plan.write_text(upstream_plan.read_text() + "\nnew upstream text\n")
        upstream_agents = self.source / "adapters/codex/AGENTS.md.template"
        upstream_agents.write_text(upstream_agents.read_text() + "\nUpdated framework instructions.\n")
        with self.assertRaisesRegex(RuntimeError, "--update"):
            self.install()
        reports = self.install(update=True)
        self.assertEqual(managed.read_bytes(), upstream_skill.read_bytes())
        self.assertIn("local note", customized.read_text())
        self.assertTrue(agents_path.read_text().startswith("# User preface\n\n"))
        self.assertIn("Updated framework instructions.", agents_path.read_text())
        conflict = self.target / ".agentic-sdlc/conflicts/.agentic-sdlc__templates__plan.md.incoming"
        self.assertEqual(conflict.read_bytes(), upstream_plan.read_bytes())
        self.assertTrue(any("CONFLICT preserved modified file" in item for item in reports))

    def test_manual_file_merge_can_be_accepted_and_survives_later_updates(self):
        self.install()
        relative = ".agentic-sdlc/templates/plan.md"
        path = self.target / relative
        path.write_text(path.read_text() + "\nlocal planning note\n")
        (self.source / "VERSION").write_text("0.2.0-dev\n")
        upstream = self.source / "templates/plan.md"
        upstream.write_text(upstream.read_text() + "\nupstream planning guidance\n")
        reports = self.install(update=True)
        self.assertTrue(any("CONFLICT preserved modified file" in item for item in reports))

        path.write_text(path.read_text() + "\nmerged upstream planning guidance\n")
        output = io.StringIO()
        with redirect_stdout(output):
            result = installer.main([
                "--target", str(self.target), "--adapter", "codex",
                "--accept-resolved", relative,
            ])
        self.assertEqual(result, 0)
        reports = output.getvalue().splitlines()
        self.assertIn("merged upstream planning guidance", path.read_text())
        self.assertTrue(any("accepted manually resolved content" in item for item in reports))
        reports = self.install()
        self.assertIn("merged upstream planning guidance", path.read_text())
        self.assertFalse(any("CONFLICT" in item for item in reports))

        (self.source / "VERSION").write_text("0.3.0-dev\n")
        upstream.write_text(upstream.read_text() + "\nnew upstream revision\n")
        reports = self.install(update=True)
        self.assertIn("merged upstream planning guidance", path.read_text())
        self.assertTrue(any("CONFLICT preserved accepted local resolution" in item for item in reports))
        reports = self.install(accept_resolved=[relative])
        self.assertTrue(any("accepted manually resolved content" in item for item in reports))
        reports = self.install()
        self.assertFalse(any("CONFLICT" in item for item in reports))

    def test_manual_agents_section_merge_can_be_accepted_and_updated(self):
        original = "# Project instructions\n\nKeep these rules.\n"
        (self.target / "AGENTS.md").write_text(original)
        self.install()
        agents_path = self.target / "AGENTS.md"
        agents_path.write_text(agents_path.read_text().replace("Inspect the repository", "Inspect project and local notes"))
        (self.source / "VERSION").write_text("0.2.0-dev\n")
        template = self.source / "adapters/codex/AGENTS.md.template"
        template.write_text(template.read_text() + "\nUpstream addition.\n")
        reports = self.install(update=True)
        self.assertTrue(any("AGENTS.md section" in item and "CONFLICT" in item for item in reports))

        agents_path.write_text(
            agents_path.read_text()
            .replace("Inspect the repository", "Inspect the repository and generated code")
            .replace(installer.END, "Upstream addition.\n" + installer.END)
        )
        reports = self.install(accept_resolved=["AGENTS.md"])
        self.assertTrue(agents_path.read_text().startswith(original))
        self.assertIn("Upstream addition.", agents_path.read_text())
        self.assertTrue(any("accepted manually resolved AGENTS.md" in item for item in reports))
        reports = self.install()
        self.assertFalse(any("CONFLICT" in item for item in reports))

        (self.source / "VERSION").write_text("0.3.0-dev\n")
        template.write_text(template.read_text() + "\nLater upstream addition.\n")
        reports = self.install(update=True)
        self.assertTrue(agents_path.read_text().startswith(original))
        self.assertTrue(any("accepted AGENTS.md resolution" in item for item in reports))
        reports = self.install(accept_resolved=["AGENTS.md"])
        self.assertTrue(any("accepted manually resolved AGENTS.md" in item for item in reports))
        self.assertFalse(any("CONFLICT" in item for item in self.install()))

    def test_accept_resolved_rejects_untracked_or_unmodified_paths(self):
        self.install()
        with self.assertRaisesRegex(RuntimeError, "not a managed path"):
            self.install(accept_resolved=["README.md"])
        with self.assertRaisesRegex(RuntimeError, "does not differ"):
            self.install(accept_resolved=[".agentic-sdlc/templates/plan.md"])

    def test_modified_managed_agents_section_is_preserved_with_incoming_copy(self):
        self.install()
        agents_path = self.target / "AGENTS.md"
        agents = agents_path.read_text().replace("Inspect the repository", "CUSTOMIZED guidance")
        agents_path.write_text(agents)
        (self.source / "VERSION").write_text("0.2.0-dev\n")
        reports = self.install(update=True)
        self.assertEqual(agents_path.read_text(), agents)
        incoming = self.target / ".agentic-sdlc/conflicts/AGENTS.md.incoming"
        self.assertIn("Inspect the repository", incoming.read_text())
        self.assertTrue(any("modified AGENTS.md section" in item for item in reports))

    def test_removed_agents_markers_are_a_conflict_not_a_second_append(self):
        self.install()
        agents_path = self.target / "AGENTS.md"
        agents_path.write_text("# User replaced the instructions\n")
        reports = self.install()
        self.assertEqual(agents_path.read_text(), "# User replaced the instructions\n")
        self.assertTrue(any("managed markers were removed" in item for item in reports))
        self.assertTrue((self.target / ".agentic-sdlc/conflicts/AGENTS.md.incoming").exists())

    def test_malformed_agents_markers_are_preserved_with_incoming_copy(self):
        malformed = "# Keep this file\n" + installer.START + "\nunfinished\n"
        agents_path = self.target / "AGENTS.md"
        agents_path.write_text(malformed)
        reports = self.install()
        self.assertEqual(agents_path.read_text(), malformed)
        self.assertTrue(any("malformed or duplicate" in item for item in reports))
        self.assertTrue((self.target / ".agentic-sdlc/conflicts/AGENTS.md.incoming").exists())

    def test_partial_installation_recovers_missing_managed_file(self):
        self.install()
        path = self.target / ".agentic-sdlc/templates/review.md"
        path.unlink()
        self.install()
        self.assertEqual(path.read_bytes(), (self.source / "templates/review.md").read_bytes())

    def test_new_upstream_files_install_and_removed_files_are_preserved_and_reported(self):
        self.install()
        added = self.source / "templates/new-template.md"
        added.write_text("new template\n")
        removed = self.source / "templates/intent.md"
        old_target = self.target / ".agentic-sdlc/templates/intent.md"
        removed.unlink()
        reports = self.install()
        self.assertEqual((self.target / ".agentic-sdlc/templates/new-template.md").read_text(), "new template\n")
        self.assertTrue(old_target.exists())
        self.assertTrue(any("no longer in source; preserved" in item for item in reports))
        self.assertTrue(any("no longer in source; preserved" in item for item in self.install()))

    def test_existing_untracked_conflicting_file_is_never_overwritten(self):
        path = self.target / ".agents/skills/intent/SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("user owned\n")
        reports = self.install()
        self.assertEqual(path.read_text(), "user owned\n")
        self.assertTrue(any("untracked file" in item for item in reports))
        self.assertTrue((self.target / ".agentic-sdlc/conflicts/.agents__skills__intent__SKILL.md.incoming").exists())

    def test_invalid_targets_manifest_and_symlinks_fail_safely(self):
        with self.assertRaises((FileNotFoundError, RuntimeError)):
            installer.install(self.base / "missing")
        with self.assertRaisesRegex(RuntimeError, "not a directory"):
            installer.install(self.source / "VERSION")
        with self.assertRaisesRegex(RuntimeError, "must not be the framework"):
            installer.install(self.source)
        (self.target / ".agentic-sdlc").mkdir()
        (self.target / ".agentic-sdlc/manifest.json").write_text("not json")
        with self.assertRaisesRegex(RuntimeError, "cannot trust installer manifest"):
            self.install()
        (self.target / ".agentic-sdlc/manifest.json").unlink()
        external = self.base / "external"
        external.mkdir()
        (self.target / ".agents").symlink_to(external, target_is_directory=True)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            self.install()

    def test_manifest_rejects_invalid_version_paths_hashes_and_entries(self):
        self.install()
        path = self.target / installer.MANIFEST
        valid = json.loads(path.read_text())
        good_hash = next(iter(valid["files"].values()))
        invalid_manifests = [
            {**valid, "version": 1},
            {**valid, "version": " 0.1.0 "},
            {**valid, "schema": True},
            {**valid, "unexpected": "field"},
            {**valid, "files": {"../AGENTS.md": good_hash}},
            {**valid, "files": {".agentic-sdlc\\templates\\plan.md": good_hash}},
            {**valid, "files": {".agentic-sdlc/templates/plan.md": "a" * 63}},
            {**valid, "files": {".agentic-sdlc/templates/plan.md": "g" * 64}},
            {**valid, "files": {".agentic-sdlc/templates/plan.md": {"sha256": good_hash}}},
            {**valid, "resolved": {".agentic-sdlc/templates/plan.md": "bad-hash"}},
            {**valid, "resolved": {".agentic-sdlc/templates/missing.md": good_hash}},
        ]
        for invalid in invalid_manifests:
            with self.subTest(manifest=invalid):
                path.write_text(json.dumps(invalid))
                with self.assertRaisesRegex(RuntimeError, "cannot trust installer manifest"):
                    self.install()
        path.write_text(json.dumps(valid))

    def test_modified_existing_file_is_preserved_even_without_version_change(self):
        self.install()
        path = self.target / ".agentic-sdlc/workflows/idea-to-pr.md"
        path.write_text(path.read_text() + "\nuser edit\n")
        reports = self.install()
        self.assertIn("user edit", path.read_text())
        self.assertTrue(any("CONFLICT preserved modified file" in item for item in reports))

    def snapshot(self):
        return {p.relative_to(self.target).as_posix(): p.read_bytes()
                for p in self.target.rglob("*") if p.is_file()}


if __name__ == "__main__":
    unittest.main()
