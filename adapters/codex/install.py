#!/usr/bin/env python3
"""Install or update the Agentic SDLC Framework Codex adapter."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from pathlib import PurePosixPath
import re
import stat
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = Path(".agentic-sdlc/manifest.json")
START = "<!-- BEGIN AGENTIC-SDLC MANAGED SECTION -->"
END = "<!-- END AGENTIC-SDLC MANAGED SECTION -->"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_files() -> dict[str, Path]:
    files: dict[str, Path] = {}
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if skill_dir.is_dir():
            files[f".agents/skills/{skill_dir.name}/SKILL.md"] = skill_dir / "SKILL.md"
    files[".agentic-sdlc/principles/engineering-principles.md"] = (
        ROOT / ".agentic-sdlc/principles/engineering-principles.md"
    )
    files[".agentic-sdlc/workflows/idea-to-pr.md"] = ROOT / "workflows/idea-to-pr.md"
    for path in sorted((ROOT / "templates").glob("*.md")):
        files[f".agentic-sdlc/templates/{path.name}"] = path
    files[".agentic-sdlc/VERSION"] = ROOT / "VERSION"
    return files


def managed_section(template: bytes) -> bytes:
    content = template.decode("utf-8").rstrip()
    return f"{START}\n{content}\n{END}".encode("utf-8")


def valid_managed_path(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    path = PurePosixPath(value)
    parts = value.split("/")
    if path.is_absolute() or str(path) != value or any(part in ("", ".", "..") for part in parts):
        return False
    if value in {
        "AGENTS.md",
        ".agentic-sdlc/VERSION",
    }:
        return True
    if len(parts) == 4 and parts[:2] == [".agents", "skills"]:
        return bool(re.fullmatch(r"[a-z0-9][a-z0-9-]*", parts[2])) and parts[3] == "SKILL.md"
    if len(parts) == 3 and parts[:1] == [".agentic-sdlc"]:
        return parts[1] in {"principles", "workflows", "templates"} and bool(
            re.fullmatch(r"[a-z0-9][a-z0-9-]*\.md", parts[2])
        )
    return False


def valid_hash(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def read_manifest(path: Path) -> dict:
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("manifest root must be an object")
        if set(manifest) - {"schema", "version", "files", "resolved"}:
            raise ValueError("manifest contains unknown fields")
        if (
            type(manifest.get("schema")) is not int
            or manifest.get("schema") != 1
            or not isinstance(manifest.get("version"), str)
            or not manifest["version"].strip()
            or manifest["version"] != manifest["version"].strip()
            or not isinstance(manifest.get("files"), dict)
            or not isinstance(manifest.get("resolved", {}), dict)
        ):
            raise ValueError("unsupported or malformed manifest")
        for relative, file_hash in manifest["files"].items():
            if not valid_managed_path(relative):
                raise ValueError(f"invalid managed file path: {relative!r}")
            if not valid_hash(file_hash):
                raise ValueError(f"invalid SHA-256 for managed file: {relative}")
        for relative, file_hash in manifest.get("resolved", {}).items():
            if relative not in manifest["files"]:
                raise ValueError(f"resolved entry has no managed file: {relative!r}")
            if not valid_hash(file_hash):
                raise ValueError(f"invalid SHA-256 for resolved file: {relative}")
        return manifest
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError(f"cannot trust installer manifest {path}: {exc}") from exc


def safe_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
        os.chmod(temporary_name, mode)
        os.replace(temporary_name, path)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)


def reject_symlink_path(target: Path, relative: str) -> None:
    current = target
    for part in Path(relative).parts:
        current = current / part
        if current.is_symlink():
            raise RuntimeError(f"refusing to follow symlink in managed path: {current}")


def incoming_copy(target: Path, relative: str, data: bytes) -> Path:
    base = target / ".agentic-sdlc/conflicts" / (relative.replace("/", "__") + ".incoming")
    reject_symlink_path(target, str(base.relative_to(target)))
    candidate = base
    if candidate.exists() and candidate.read_bytes() != data:
        candidate = base.with_name(base.name + "." + digest(data)[:12])
        reject_symlink_path(target, str(candidate.relative_to(target)))
    if not candidate.exists():
        safe_write(candidate, data)
    return candidate


def managed_section_from(data: bytes) -> bytes | None:
    start_marker, end_marker = START.encode(), END.encode()
    if data.count(start_marker) != 1 or data.count(end_marker) != 1:
        return None
    begin = data.index(start_marker)
    finish = data.index(end_marker)
    if finish < begin:
        return None
    return data[begin : finish + len(end_marker)]


def install(
    target: Path, update: bool = False, accept_resolved: list[str] | None = None
) -> list[str]:
    target = target.expanduser().resolve(strict=True)
    if not target.is_dir():
        raise RuntimeError(f"target is not a directory: {target}")
    if target == ROOT or ROOT in target.parents:
        raise RuntimeError("target must not be the framework repository or one of its parents")

    state_path = target / MANIFEST
    reject_symlink_path(target, str(MANIFEST))
    old = read_manifest(state_path) if state_path.exists() else None
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if old and old.get("version") != version and not update:
        raise RuntimeError("framework version differs from the installed version; rerun with --update")

    sources = source_files()
    current_paths = set(sources) | {"AGENTS.md"}
    previous = old["files"] if old else {}
    previous_resolved = old.get("resolved", {}) if old else {}
    resolved = dict(previous_resolved)
    accepted = accept_resolved or []
    if len(accepted) != len(set(accepted)):
        raise RuntimeError("--accept-resolved paths must not be repeated")
    valid_paths = set(sources) | {"AGENTS.md"}
    for relative in accepted:
        if relative not in valid_paths:
            raise RuntimeError(f"--accept-resolved is not a managed path: {relative}")
        if relative not in previous:
            raise RuntimeError(f"cannot accept {relative}: it is not tracked by the installation manifest")
        destination = target / relative
        reject_symlink_path(target, relative)
        if not destination.is_file():
            raise RuntimeError(f"cannot accept {relative}: target file is missing")
        content = destination.read_bytes()
        if relative == "AGENTS.md":
            content = managed_section_from(content) or b""
            if not content:
                raise RuntimeError("cannot accept AGENTS.md: its managed section is missing or malformed")
        content_hash = digest(content)
        if content_hash == previous[relative]:
            raise RuntimeError(f"cannot accept {relative}: it does not differ from the recorded baseline")

    reports: list[str] = []
    new_hashes: dict[str, str] = {}

    for relative, source in sources.items():
        reject_symlink_path(target, relative)
        destination = target / relative
        data = source.read_bytes()
        new_hash = digest(data)
        prior_hash = previous.get(relative)
        if relative in accepted:
            existing_hash = digest(destination.read_bytes()) if destination.is_file() else None
            if existing_hash == new_hash:
                resolved.pop(relative, None)
                new_hashes[relative] = new_hash
                reports.append(f"accepted {relative} at the incoming version")
            else:
                resolved[relative] = existing_hash
                new_hashes[relative] = new_hash
                reports.append(f"accepted manually resolved content for {relative}")
            continue
        if destination.exists():
            existing = destination.read_bytes()
            existing_hash = digest(existing)
            accepted_hash = resolved.get(relative)
            if accepted_hash and existing_hash == accepted_hash:
                if new_hash != prior_hash:
                    incoming = incoming_copy(target, relative, data)
                    reports.append(
                        f"CONFLICT preserved accepted local resolution for {relative}; "
                        f"incoming: {incoming.relative_to(target)}"
                    )
                new_hashes[relative] = new_hash
                continue
            if accepted_hash:
                resolved.pop(relative, None)
            if prior_hash is None:
                if existing != data:
                    incoming = incoming_copy(target, relative, data)
                    reports.append(f"CONFLICT preserved untracked file {relative}; incoming: {incoming.relative_to(target)}")
                    continue
            elif digest(existing) != prior_hash:
                if digest(existing) != new_hash:
                    incoming = incoming_copy(target, relative, data)
                    reports.append(f"CONFLICT preserved modified file {relative}; incoming: {incoming.relative_to(target)}")
                    new_hashes[relative] = prior_hash
                    continue
            if existing != data:
                safe_write(destination, data)
                reports.append(f"updated {relative}")
        else:
            resolved.pop(relative, None)
            safe_write(destination, data)
            reports.append(f"installed {relative}")
        new_hashes[relative] = new_hash

    agents_path = target / "AGENTS.md"
    reject_symlink_path(target, "AGENTS.md")
    template_section = managed_section((ROOT / "adapters/codex/AGENTS.md.template").read_bytes())
    template_hash = digest(template_section)
    if agents_path.exists():
        agents = agents_path.read_bytes()
    else:
        agents = b""
    start_count, end_count = agents.count(START.encode()), agents.count(END.encode())
    current_section = managed_section_from(agents)
    section_was_accepted = (
        current_section is not None
        and previous_resolved.get("AGENTS.md")
        and digest(current_section) == previous_resolved["AGENTS.md"]
    )
    if "AGENTS.md" in accepted:
        if current_section is None:
            raise RuntimeError("cannot accept AGENTS.md: its managed section is missing or malformed")
        if digest(current_section) == template_hash:
            resolved.pop("AGENTS.md", None)
            reports.append("accepted AGENTS.md section at the incoming version")
        else:
            resolved["AGENTS.md"] = digest(current_section)
            reports.append("accepted manually resolved AGENTS.md managed section")
        new_hashes["AGENTS.md"] = template_hash
    elif section_was_accepted:
        prior_hash = previous.get("AGENTS.md")
        if template_hash != prior_hash:
            incoming = incoming_copy(target, "AGENTS.md", template_section)
            reports.append(
                f"CONFLICT preserved accepted AGENTS.md resolution; "
                f"incoming: {incoming.relative_to(target)}"
            )
        new_hashes["AGENTS.md"] = template_hash
    else:
        if resolved.get("AGENTS.md"):
            resolved.pop("AGENTS.md", None)
    if "AGENTS.md" not in accepted and not section_was_accepted and current_section is None and (start_count or end_count):
        incoming = incoming_copy(target, "AGENTS.md", template_section)
        reports.append(
            f"CONFLICT AGENTS.md has malformed or duplicate framework markers; "
            f"no changes made; incoming: {incoming.relative_to(target)}"
        )
        if "AGENTS.md" in previous:
            new_hashes["AGENTS.md"] = previous["AGENTS.md"]
    elif "AGENTS.md" not in accepted and not section_was_accepted and current_section is not None:
        begin = agents.index(START.encode())
        finish = agents.index(END.encode()) + len(END)
        old_section = agents[begin:finish]
        prior_hash = previous.get("AGENTS.md")
        if prior_hash is None or digest(old_section) != prior_hash:
            if old_section != template_section:
                incoming = incoming_copy(target, "AGENTS.md", template_section)
                reports.append(f"CONFLICT preserved untracked or modified AGENTS.md section; incoming: {incoming.relative_to(target)}")
                if prior_hash:
                    new_hashes["AGENTS.md"] = prior_hash
            else:
                new_hashes["AGENTS.md"] = template_hash
        else:
            updated = agents[:begin] + template_section + agents[finish:]
            if updated != agents:
                safe_write(agents_path, updated)
                reports.append("updated managed section in AGENTS.md")
            new_hashes["AGENTS.md"] = template_hash
    elif "AGENTS.md" not in accepted and not section_was_accepted and current_section is None and not (start_count or end_count):
        if agents_path.exists() and "AGENTS.md" in previous:
            incoming = incoming_copy(target, "AGENTS.md", template_section)
            reports.append(f"CONFLICT AGENTS.md managed markers were removed; preserved file; incoming: {incoming.relative_to(target)}")
            new_hashes["AGENTS.md"] = previous["AGENTS.md"]
        else:
            separator = b"" if not agents or agents.endswith(b"\n") else b"\n"
            updated = agents + separator + (b"\n" if agents else b"") + template_section + b"\n"
            safe_write(agents_path, updated)
            reports.append("added managed section to AGENTS.md" if agents else "installed AGENTS.md")
            new_hashes["AGENTS.md"] = template_hash

    if old:
        removed = sorted(set(previous) - current_paths)
        for relative in removed:
            reports.append(f"NOTICE previously managed file no longer in source; preserved {relative}")
            new_hashes[relative] = previous[relative]

    manifest = {"schema": 1, "version": version, "files": new_hashes}
    if resolved:
        manifest["resolved"] = resolved
    safe_write(state_path, (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode())
    reports.insert(0, f"Installed framework version {version} into {target}")
    if not any(item.startswith(("installed ", "updated ", "added managed")) for item in reports):
        reports.append("installation is up to date")
    return reports


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path, help="existing project directory")
    parser.add_argument("--adapter", choices=["codex"], default="codex")
    parser.add_argument("--update", action="store_true", help="allow an intentional framework version update")
    parser.add_argument(
        "--accept-resolved",
        action="append",
        default=[],
        metavar="PROJECT_PATH",
        help="accept a manually merged, previously tracked file as a local baseline",
    )
    args = parser.parse_args(argv)
    try:
        for message in install(args.target, args.update, args.accept_resolved):
            print(message)
    except (OSError, RuntimeError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
