# Codex Adapter

This adapter makes the tool-agnostic Agentic SDLC Framework usable in Codex. The authoritative process remains [`workflows/idea-to-pr.md`](../../workflows/idea-to-pr.md), with detailed behavior in the seven core skills and structure in the shared templates. This guide and [`AGENTS.md.template`](AGENTS.md.template) translate those resources into Codex project conventions; Codex-specific instructions belong here, not in the core skills.

## Installation

Prerequisite: Python 3.10 or newer; the installer uses only the standard library. Keep this framework checkout available when you want to update an installed project. From the framework repository, run:

```sh
python3 adapters/codex/install.py --target ../sample-app --adapter codex
```

Run the automated installer tests from the repository root with `python3 -m unittest discover -s adapters/codex/tests -v`.

The target must be an existing project directory. The installer uses paths relative to that directory and copies resources, so the installed project does not depend on the checkout to use the framework. It does not run Codex, generate project artifacts, execute application tests, or create a Git repository.

## Installed layout

The installed project layout is:

```text
project-root/
├── AGENTS.md                         # existing instructions plus a marked managed section
├── .agents/skills/<skill-name>/SKILL.md
└── .agentic-sdlc/
    ├── VERSION
    ├── manifest.json
    ├── principles/engineering-principles.md
    ├── workflows/idea-to-pr.md
    └── templates/*.md
```

The seven skill names and file contents are copied verbatim. The shared principle, workflow, and all five templates are copied under `.agentic-sdlc/`. The manifest records the installed version and SHA-256 hashes of framework-managed files. The installer validates its schema, version, paths, and hashes; malformed metadata stops installation before managed files are changed. It is installer bookkeeping, not a record of project-owned files.

## Existing instructions, reruns, and updates

If `AGENTS.md` does not exist, the installer creates it from `AGENTS.md.template` inside `<!-- BEGIN AGENTIC-SDLC MANAGED SECTION -->` and `<!-- END AGENTIC-SDLC MANAGED SECTION -->` markers. If it exists without these markers, the installer appends the managed section and preserves all existing bytes. A single existing managed section is updated only while its content matches the manifest's last installed hash. Malformed or duplicate markers, or a locally changed section, are preserved and reported; the incoming section is written under `.agentic-sdlc/conflicts/` for review.

Rerunning the same version is idempotent. For a new framework version, update the framework checkout to the version you intend to install, then run:

```sh
python3 adapters/codex/install.py --target ../sample-app --adapter codex --update
```

An unchanged managed file is updated. A user-modified managed file is preserved and the incoming version is saved under `.agentic-sdlc/conflicts/`; new files are installed. Existing conflicting files not listed in the manifest are treated as user-owned and preserved. Files removed from a later framework source are reported and never deleted. If an untracked file already equals the incoming content, it is adopted into the manifest.

Resolve a conflict by comparing the preserved target file with its incoming copy and manually merging the desired content into the target. Then explicitly accept that reviewed merge as a local baseline, using the project-relative managed path:

```sh
python3 adapters/codex/install.py --target ../sample-app --adapter codex --update \
  --accept-resolved .agentic-sdlc/templates/plan.md
```

Use `--accept-resolved AGENTS.md` for a merged managed section. Repeat the option for multiple files. The option only accepts an existing, previously tracked file whose content differs from the recorded baseline; it does not authorize replacement. The installer records the accepted local hash separately from the upstream hash, so reruns preserve your merge. If upstream changes that file again, the new incoming version is reported for review while your accepted content stays in place. Review the conflict and explicitly accept it again, even if you keep the same merged content.

Do not delete the manifest to bypass a conflict: without trusted history, existing differing files are treated as untracked and preserved. A malformed manifest or a symlink in a managed path stops installation; repair the manifest/path deliberately and rerun. A partial installation can be rerun to fill missing files.

The installer does not create the default artifact directories, remove obsolete files, merge arbitrary edits, fetch framework versions, invoke Codex, or validate a project's workflow. Back up project instructions before manual conflict resolution.

The installer suite uses disposable source and target trees. The current sixteen automated cases cover fresh install, all resources, reruns, version updates, `AGENTS.md`, manual conflict resolution, manifest validation, user edits, partial recovery, and invalid or unsafe paths. These checks do not establish end-to-end Codex workflow behavior.

Codex project skills are discovered from `.agents/skills/`. The skill folders and frontmatter names are preserved exactly:

| Framework skill | Source path | Installed path | Explicit invocation |
|---|---|---|---|
| Intent | `skills/intent/SKILL.md` | `.agents/skills/intent/SKILL.md` | `$intent` |
| Product Breakdown | `skills/product-breakdown/SKILL.md` | `.agents/skills/product-breakdown/SKILL.md` | `$product-breakdown` |
| Specification | `skills/specification/SKILL.md` | `.agents/skills/specification/SKILL.md` | `$specification` |
| Planning | `skills/planning/SKILL.md` | `.agents/skills/planning/SKILL.md` | `$planning` |
| Plan Review | `skills/plan-review/SKILL.md` | `.agents/skills/plan-review/SKILL.md` | `$plan-review` |
| Implementation | `skills/implementation/SKILL.md` | `.agents/skills/implementation/SKILL.md` | `$implementation` |
| Code Review | `skills/code-review/SKILL.md` | `.agents/skills/code-review/SKILL.md` | `$code-review` |

Codex also selects skills from their descriptions. Explicit `$name` invocation is useful when a stage is known; it does not waive the skill's prerequisites or approval gates. See the official [Codex skills guide](https://developers.openai.com/codex/skills).

## Running the workflow

First inspect the request, repository instructions and code, and existing artifacts. Then choose the narrowest valid entry point in `workflows/idea-to-pr.md`:

- Vague idea: Intent; add Product Breakdown for a broad initiative.
- Articulated broad initiative: Product Breakdown directly.
- Scoped feature or ticket: Specification if approved requirements are not already sufficient; otherwise Planning.
- Small bug or maintenance task: Specification if expected behavior lacks an approved source; otherwise Planning.
- Existing PR: Code Review, with limitations stated when baselines or context are missing.

These are conditional paths, not a mandatory sequence. Reuse current approved artifacts, skip stages that add no value, and do not recreate or repeat approved decisions. The skills define artifact defaults: initiative artifacts under `docs/initiatives/<initiative-id>/`, work-item artifacts under `docs/tickets/<work-item-id>/`, and review reports under the work item's `reviews/` directory. Use an existing project convention or an explicitly selected project-root-relative path when appropriate. Establish and communicate artifact paths early.

Before each stage, locate the latest artifacts, verify their status and approval, and continue from them. If work is interrupted, resume from the latest saved artifacts and review history; inspect current repository state and changes since those artifacts were written. Do not infer approval from a prior chat, an artifact's existence, a review result, or silence. If required artifacts are missing or their status is unclear, report that and return to the relevant stage instead of fabricating content or approval.

## Approval gates

Follow the workflow and skills as written. In particular:

- Obtain owner confirmation of a new Intent when it is needed.
- When Product Breakdown is used, obtain owner approval of the breakdown and explicit selection of the next increment.
- Obtain explicit owner approval of the Specification or equivalent requirements before Planning.
- Complete Plan Review to its threshold, then obtain explicit owner approval of the plan before Implementation.
- Pause and obtain owner approval for material changes to approved requirements, scope, business behavior, user-visible behavior, privacy/security or data-integrity guarantees, acceptance criteria, or important constraints. A technical adaptation that preserves approved boundaries may proceed under the Implementation skill and must be documented when material.
- After implementation and review, present results for human verification, including appropriate manual/local behavior checks. Human verification is required before PR authorization.
- Create a PR only after explicit owner authorization. Review passing or human verification alone is not PR authorization.

Equivalent current, approved artifacts can satisfy a gate. Do not seek approval repeatedly for an unchanged decision.

## Independent reviews

Plan Review and Code Review are distinct activities from Planning and Implementation. Use a fresh Codex session for each independent review by default, separate from the authoring/fixing session. Provide the actual plan or diff, approved baselines, relevant repository context, and the previous consolidated report. Reviewers may create or update only their designated consolidated review report. They must not modify the reviewed plan, specification, implementation, tests, or other project files, or run commands that mutate them.

Keep one consolidated report per activity using `.agentic-sdlc/templates/review.md` (typically `reviews/plan-review.md` and `reviews/code-review.md`). Preserve stable finding IDs, statuses, resolution rationale, and round history; do not silently discard unresolved Major, Minor, or Suggestion findings. Allow no more than three review/fix rounds for an activity. Plan Review meets its threshold only with zero Blocking and zero Major findings. Code Review meets its threshold only with zero Blocking findings; unresolved Major, Minor, and Suggestion findings remain visible for owner consideration. Escalate threshold findings that remain after round three. A passing review is not owner approval.

### Native Codex `/review`

Current official Codex documentation describes `/review` as reviewing uncommitted changes or changes against a base branch. The interactive CLI starts a dedicated reviewer for the selected diff and reports prioritized, actionable findings without changing the working tree. The installed CLI's non-interactive review help exposes `codex exec review` with a selected target and optional custom review prompt. See [Developer commands](https://developers.openai.com/codex/cli/slash-commands) and [Code review](https://developers.openai.com/codex/code-review).

Use `/review` or `codex review` as a Code Review execution mechanism only when the current Codex client/version supports the needed target and context. Invoke it from the independent review activity, against the intended diff. The framework's `$code-review` skill and consolidated report remain authoritative for the review baseline, criteria, severity classification, stable IDs, round limit, threshold, and disposition. Supply or have the independent reviewer inspect approved requirements, the human-approved plan, authorized adaptations, prior report, and review template; reconcile native findings into that report and retain all unresolved findings. The native command's prioritized findings are not by themselves a framework report or an approval.

The documented `/review` behavior does not establish that it will load or follow the framework Code Review skill, include all approved artifacts, emit the framework's report fields, preserve finding IDs/history, or enforce its three-round limit and threshold. If those requirements cannot be verified in the selected client, run `$code-review` in a fresh session with the actual diff and baselines, then write/update the report according to the skill and template. Do not allow a native review result to replace human verification or PR authorization.

## Validation record and limits

The supplied compatibility spike reports successful checks on Codex CLI 0.167.0, Linux/WSL2 x86_64, using `codex exec`: project skills were discovered from `.agents/skills/`, `$skill-name` invocation worked, skills read project-root-relative `.agentic-sdlc/` resources, `AGENTS.md` instructions were followed, and missing shared resources were reported rather than fabricated. This record is limited to that reported environment and version; it is not evidence of support across all Codex versions, clients, hosts, or configurations.

### Increment 3 disposable-project validation

- **Codex:** `codex-cli 0.167.0`.
- **Host:** Linux `5.15.167.4-microsoft-standard-WSL2`, x86_64; Codex warned that host `bubblewrap` was unavailable and used its bundled copy.
- **Project:** disposable Git repositories under `/tmp/agentic-sdlc-codex.xA2HaL/`; installed layout was assembled by copying source files, without editing framework source during the checks. Codex sessions used `--sandbox read-only --ephemeral`.
- **Seven skill discovery and explicit invocation — Pass:** invoked `$intent`, `$product-breakdown`, `$specification`, `$planning`, `$plan-review`, `$implementation`, and `$code-review` in separate `codex exec` sessions. Each read its installed `.agents/skills/<name>/SKILL.md` and `.agentic-sdlc/workflows/idea-to-pr.md`, returned its expected probe marker, and made no file changes.
- **Shared resources — Pass:** Codex read `.agentic-sdlc/workflows/idea-to-pr.md`, `.agentic-sdlc/principles/engineering-principles.md`, and all five files in `.agentic-sdlc/templates/`.
- **`AGENTS.md` instructions — Pass:** Codex reported the paths from the installed template, confirmed explicit owner authorization is required before PR creation, and made no file changes.
- **Missing resource handling — Pass:** in a separate project without `.agentic-sdlc/principles/engineering-principles.md`, `$intent` reported the exact missing file and requested it before proceeding; it did not fabricate the contents.
- **Native review capability — Partially verified:** `codex exec review --help` in 0.167.0 confirmed `--uncommitted`, `--base`, and `--commit` targets plus optional custom review instructions. Current official [Developer commands](https://developers.openai.com/codex/cli/slash-commands) and [Code review](https://developers.openai.com/codex/code-review) documentation describe `/review` as starting a dedicated reviewer and reporting prioritized findings without changing the working tree. A native review run and its ability to preserve framework report fields/history/thresholds were **Not tested**.
- **Workflow gate and review-instruction consistency — Pass:** Codex read the installed `AGENTS.md`, workflow, Plan Review skill, and Code Review skill, then accurately restated the owner gates, conditional entry paths, reviewer separation/read-only rules, three-round maximum, and both thresholds. This checks instruction accessibility and consistency; actual approval interactions and review/fix rounds were not simulated.
- **End-to-end workflow — Not tested:** no complete workflow, real Plan Review or Code Review round, owner-approval interaction, or PR authorization sequence was run.

Manual regression scenarios under `tests/regression/` describe expected framework behavior; they are not behavioral test results unless explicitly run and recorded. The installer, safe merging with a project's existing `AGENTS.md`, other Codex versions/hosts, and end-to-end use on a sample application remain unvalidated.
