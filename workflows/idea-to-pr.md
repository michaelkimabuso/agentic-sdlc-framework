# Workflow: Idea to PR (M1)

## Purpose

Move a change from an idea or an existing task to a reviewable pull request using explicit artifacts, verification, and human approval gates. This workflow is tool-agnostic; an adapter maps these steps to a coding agent's capabilities.

**M1 ends at an opened PR.** Merging, deployment, production monitoring, and feedback loops are future milestones.

## Entry points

- **Idea-driven:** Start with a problem or idea. Create `intent.md` and clarify the desired outcome before writing a specification.
- **Task-driven:** Start from an existing ticket, issue, or acceptance criteria. Reuse relevant source material and create only missing artifacts; do not duplicate information just to fill a template.

Both paths converge at Specification.

## Stages

### 1. Understand intent (idea-driven only)

- Identify the problem, who experiences it, and the outcome sought.
- Ask focused questions when answers could materially change scope or behavior.
- Separate confirmed facts, assumptions, and open questions.
- Create or update `intent.md`.
- Do not invent business rules to make the idea appear complete.

**Output:** An intent that the user can confirm.

**Gate:** Ask the user to confirm the intent before moving on.

### 2. Specify

- Review the intent or existing task and inspect relevant repository context.
- Define scope, exclusions, expected behavior, and testable acceptance criteria.
- Identify important edge cases, data/security concerns, dependencies, and unresolved questions.
- Mark assumptions explicitly. Ask the user when an unresolved decision materially affects implementation or acceptance.
- Create or update `spec.md`.

**Output:** A specification with testable acceptance criteria and no blocking ambiguity.

**Gate:** Ask the user to approve the specification before planning.

### 3. Plan

- Inspect the relevant code and existing conventions before proposing changes.
- Map acceptance criteria to implementation steps and verification.
- Prefer the smallest coherent change; avoid unrelated refactors and speculative infrastructure.
- Identify files or areas likely to change, risks, tests, and any migration or compatibility concerns.
- Create or update `plan.md`.

**Output:** A concrete, ordered implementation and verification plan.

**Gate:** Present the plan and wait for explicit user approval. Do not implement before approval.

### 4. Implement

- Follow the approved plan and existing project conventions.
- Keep changes scoped to the approved specification.
- If implementation reveals a material ambiguity, scope change, or risk, stop and ask rather than silently deciding.
- Update the plan only when needed, explaining material deviations and requesting approval when scope or behavior changes.

**Output:** Implementation changes and any necessary tests.

### 5. Verify

- Run relevant automated tests, linters, type checks, builds, and other project-defined checks that are available and appropriate.
- Add or update tests that demonstrate the acceptance criteria and important regression cases.
- Inspect the diff for accidental changes, secrets, generated artifacts, and unrelated edits.
- Report exactly what was run and the result. Distinguish passed, failed, skipped, and not run. Never claim a check passed if it was not run.
- If checks fail, diagnose and fix in-scope issues; ask for help when blocked or when a fix requires a material decision.

**Output:** Verification results and a reviewed diff.

**Gate:** Do not proceed while known critical failures or unexplained risky changes remain. Explain any checks that cannot be run.

### 6. Review

- Review the diff against the specification, acceptance criteria, approved plan, security, correctness, maintainability, and test coverage.
- Treat automated review findings as hypotheses to validate, not facts to accept blindly.
- Fix substantiated in-scope issues and re-run relevant checks.
- If a finding requires a scope or product decision, ask the user.

**Output:** Review findings, resolutions, and remaining limitations.

### 7. Human verification

Present a concise summary of behavior changed, important files, acceptance criteria covered, verification results, known limitations, and any deviations from the approved plan.

**Gate:** Ask the user to confirm the change is ready for a PR. Do not open the PR until confirmed.

### 8. Prepare PR

- Create a focused branch and commit changes according to the repository's normal workflow.
- Open a PR against the repository's intended base branch.
- Include the problem, solution, acceptance criteria addressed, tests/checks and their outcomes, and known limitations.
- Do not merge the PR unless the user explicitly authorizes merging.

**Output:** PR URL and a short status summary.

## Stop and escalation rules

Pause and ask the user when:
- Requirements conflict or a business rule is unclear and affects behavior.
- The requested work expands materially beyond the approved scope.
- A destructive, externally visible, costly, or security-sensitive action is needed and has not been authorized.
- Required access, credentials, dependencies, or verification are unavailable.
- A check fails and the safe fix is unclear.

Do not expose secrets in artifacts, logs, prompts, commits, or PRs.

## Artifact expectations

Use `templates/intent.md`, `templates/spec.md`, and `templates/plan.md` as starting formats, not paperwork to fill mechanically. Omit irrelevant sections and preserve useful source artifacts such as existing tickets. Store working artifacts with the project/change they describe unless the user chooses another location.

## Workflow maintenance

When an agent failure is found:
1. Capture a minimal reproducible scenario and the expected behavior.
2. Diagnose whether the cause is missing/ambiguous instruction, a workflow gap, project context, or tool limitation.
3. Fix the smallest appropriate source; do not automatically append another rule.
4. Add or update a regression scenario under `tests/regression/`.
5. Re-run the new scenario and relevant existing scenarios.
6. Refactor redundant instructions only when regression checks can validate the change.
