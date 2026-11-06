# Workflow: Idea to PR (M1)

## Purpose

Move software work from an idea, initiative, or existing task to a reviewable pull request using focused skills, explicit artifacts, verification, and human approval gates. This workflow is tool-agnostic; an adapter maps it to a coding agent's capabilities.

**M1 ends at an opened PR.** Merging, deployment, production monitoring, and feedback loops are outside this milestone.

## Entry points and stage selection

Choose the narrowest entry point that preserves the context and decisions needed for safe delivery. Do not force every task through every stage.

- **Vague idea:** Start with Intent to clarify the problem, affected people, desired outcomes, context, and constraints. Continue to Product Decomposition when the idea describes a broad initiative or product.
- **Broad, articulated initiative:** Start with Product Decomposition when the brief or requirements already provide sufficient context. Do not create a duplicate Intent artifact merely to satisfy the sequence.
- **Existing product or backlog:** Product Decomposition may be invoked independently to review or restructure capabilities and candidate work items. Preserve owner-approved commitments unless the owner authorizes changes.
- **Scoped feature or complete ticket:** Start with Specification when requirements are not yet sufficiently explicit, or Planning when an approved specification/equivalent already exists.
- **Clear, small bug or maintenance task:** Start with Planning or Implementation as appropriate when the reproduction, expected behavior, and constraints are already clear.
- **Existing PR:** Invoke Code Review independently. Report limitations when the review context is incomplete.

Reuse equivalent, current, approved artifacts. Create only what is missing; do not duplicate information to fill templates.

## Stages

### 1. Intent (when needed)

- Clarify the problem or opportunity, who is affected, current context, desired outcomes, and constraints.
- Ask focused questions when answers could materially change direction, scope, or behavior.
- Distinguish confirmed facts, assumptions, and unanswered questions.
- Create or update `intent.md`.
- Do not invent business rules or imply that market/customer validation has occurred.

**Output:** An owner-reviewable intent.

**Gate:** Obtain owner confirmation of the intent before relying on it as the basis for decomposition or specification. If equivalent approved context already exists, this gate may be skipped.

### 2. Product Decomposition (for broad initiatives; optional)

- Use the Intent, brief, requirements, or existing product/backlog context as input.
- Identify meaningful capabilities and deliverables, then derive candidate work items at a useful level of detail.
- Distinguish work items from genuinely independent initiatives; recommend separate initiative artifacts only when their problems, users, outcomes, or constraints are materially distinct.
- Identify dependencies, sequencing considerations, and a possible MVP or next increment. Make prioritization rationale and uncertainty visible.
- Decompose progressively: refine the next increment enough to support selection, not every future item into implementation-ready specifications.
- Create or update `product-breakdown.md`.
- Do not turn this activity into an exhaustive backlog-generation exercise or a technical implementation plan.

**Output:** A product breakdown with candidate work items, relationships, dependencies, and a proposed next increment.

**Gate:** The owner reviews and approves the breakdown and explicitly selects the next work item/increment before it proceeds to Specification. Do not treat an agent-generated roadmap or prioritization as approved.

Skip this stage for already-scoped work where decomposition would add no meaningful value. It may also be invoked independently for an existing product or backlog.

### 3. Specification

- Define the selected work item's problem, scope, exclusions, expected behavior, and testable acceptance criteria.
- Review relevant source material and inspect repository context where useful.
- Identify important edge cases, failure behavior, data/security concerns, dependencies, constraints, and unresolved decisions.
- Distinguish confirmed requirements from assumptions. Ask the owner to resolve questions that materially affect behavior, scope, or acceptance.
- Create or update `spec.md`.

**Output:** A specification with testable acceptance criteria and no unresolved blocking ambiguity.

**Gate:** Obtain owner approval of the requirements/specification before planning. Do not silently convert assumptions into requirements.

### 4. Planning

- Inspect the relevant codebase, architecture, tests, project instructions, and established conventions before proposing changes.
- Map approved requirements and acceptance criteria to a coherent technical approach and ordered implementation steps.
- Identify likely impacted areas, verification strategy, risks, dependencies, compatibility/data concerns, and assumptions.
- Prefer the smallest coherent solution that meets quality requirements; avoid unrelated refactors and speculative infrastructure.
- Create or update `plan.md`. It must be understandable and actionable by another developer or agent without relying on the original conversation.

**Output:** A concrete implementation and verification plan.

### 5. Plan Review

- Run Plan Review in a fresh agent session by default, separate from the planning session.
- The reviewer evaluates the plan against the approved specification, repository reality, engineering principles, security, data integrity, maintainability, completeness, and verification coverage.
- The reviewer is read-only and records findings in the plan-review report using the shared `review.md` template.
- Give findings to the planning session (or a separate fixing session) for correction. The reviewer validates the revised plan in a subsequent fresh round.
- Preserve stable finding IDs and record round history, resolutions, and rationale in one consolidated report for this review activity.
- Treat automated findings as hypotheses to validate, not facts to accept blindly.

**Outcome:** Approved, Changes Requested, or Blocked.

**Bound:** Allow at most three review/fix rounds per Plan Review activity. The plan meets the review threshold when no blocking or major findings remain. If the limit is reached with unresolved blocking or major findings, stop and escalate rather than silently accepting them.

**Gate:** After the review threshold is met, obtain explicit human approval of the plan before implementation. Review approval does not replace human approval.

### 6. Implementation and Adaptive Planning

- Execute the approved plan against the approved specification. Before acting, validate that assumptions, project instructions, dependencies, and repository state still hold.
- Follow established project conventions and applicable engineering standards; do not follow a stale or unsafe plan blindly.
- Implement the required code and tests. Keep changes within approved scope.
- When discoveries require technical-only adjustments that preserve requirements, behavior, constraints, and risk boundaries, adapt the plan, record the discovery and rationale, and continue.
- Pause for owner approval when a proposed change materially affects scope, business behavior, acceptance criteria, user-visible behavior, security/privacy, data integrity, or a consequential architecture/operational constraint.
- If the plan is materially outdated or the safe approach is unclear, return to Planning and, when warranted, repeat Plan Review and human plan approval before proceeding.
- Do not self-approve business decisions, scope changes, or the plan.

**Output:** Implementation changes, tests, and an updated plan where adaptation was necessary.

### 7. Automated Verification

- Run relevant automated tests, linters, type checks, builds, and other project-defined checks that are available and appropriate.
- Add or update tests that demonstrate acceptance criteria and important regression cases.
- Diagnose and fix in-scope failures; after fixes, rerun the relevant checks.
- Inspect the diff for accidental changes, secrets, generated artifacts, and unrelated edits.
- Report exactly what was run and the result. Distinguish passed, failed, skipped, and not run. Never claim a check passed if it was not run.

**Output:** Verification results and an implementation diff ready for independent review.

**Gate:** Do not proceed while known critical failures or unexplained risky changes remain. Explain checks that cannot be run.

### 8. Code Review

- Run Code Review in a fresh agent session, separate from implementation by default.
- Review the diff against the approved specification and acceptance criteria, approved/updated plan, correctness, security, data integrity, maintainability, and test coverage.
- The reviewer is read-only and records findings in the code-review report using the shared `review.md` template.
- Give findings to the implementation session (or a separate fixing session) for correction. The reviewer validates fixes in a subsequent fresh round.
- Preserve stable finding IDs and record round history, resolutions, and rationale in one consolidated report for this review activity.
- Rerun relevant automated checks after fixes. Treat review findings as hypotheses to validate, not facts to accept blindly.
- If a finding requires a product/business decision or material scope change, stop and ask the owner.

**Outcome:** Approved, Changes Requested, or Blocked.

**Bound:** Allow at most three review/fix rounds per Code Review activity. The code meets the review threshold when no blocking findings remain. If the limit is reached with unresolved blocking findings, stop and escalate.

A standalone Code Review may be used for another developer's PR. Review the available diff and context, and clearly state limitations when the specification, plan, or full repository context is unavailable.

### 9. Human Verification

Present a concise summary of behavior changed, important files, acceptance criteria covered, verification results, review outcomes, known limitations, and deviations from the approved plan.

**Gate:** The owner reviews the diff and performs appropriate manual/local behavior checks. Obtain explicit human confirmation that the change is ready for a PR. Do not open the PR before authorization.

### 10. Prepare PR

- Create or use a focused branch and commit changes according to the repository's normal workflow.
- Open a PR against the repository's intended base branch.
- Include the problem, solution, acceptance criteria addressed, tests/checks and their outcomes, review status, and known limitations.
- Do not merge the PR unless the owner explicitly authorizes merging.

**Output:** PR URL and a concise status summary.

## Review report and artifact conventions

- Use the shared `templates/review.md` structure for both Plan Review and Code Review, but keep their reports separate (for example, `reviews/plan-review.md` and `reviews/code-review.md`).
- Each finding should have a stable ID, severity, artifact/file and line reference where applicable, evidence/explanation, recommended correction, status, and resolution rationale.
- Keep one consolidated report per review activity and append round history rather than creating a disconnected report for every round.
- By default, review reports are working artifacts and need not be committed unless project policy or auditability requirements call for it.
- Use `templates/intent.md`, `templates/product-breakdown.md`, `templates/spec.md`, `templates/plan.md`, and `templates/review.md` as starting formats, not paperwork to fill mechanically.
- Typical initiative artifacts are `intent.md` and `product-breakdown.md`; typical work-item artifacts are `spec.md` and `plan.md`. Follow the project's existing artifact conventions when they are suitable.
- Preserve useful source artifacts such as tickets and existing requirements. Establish artifact paths at the start and pass them explicitly between stages.

## Human approval gates

Obtain explicit owner approval at the relevant points:
- Confirm Intent when a new intent artifact is needed.
- Approve Product Decomposition and select the next increment when decomposition is used.
- Resolve important open questions and approve the Specification before Planning.
- Approve the plan after Plan Review and before Implementation.
- Approve material changes to scope, business behavior, acceptance criteria, or consequential constraints.
- Verify the diff and appropriate manual/local behavior before PR preparation.
- Authorize opening the PR.

Equivalent current, approved decisions and artifacts may satisfy a gate; do not ask the owner to approve the same decision repeatedly without a material change.

## Stop and escalation rules

Pause and ask the owner when:
- Requirements conflict or a business rule is unclear and affects behavior.
- The requested work expands materially beyond approved scope.
- A destructive, externally visible, costly, or security-sensitive action is needed and has not been authorized.
- A proposed implementation change affects approved behavior, data integrity, security/privacy, or a consequential constraint.
- Required access, credentials, dependencies, or verification are unavailable.
- A review reaches its round limit with unresolved findings above its acceptance threshold.
- A check fails and the safe fix is unclear.

Do not expose secrets in artifacts, logs, prompts, commits, or PRs.

## Workflow maintenance

When an agent failure is found:
1. Capture a minimal reproducible scenario and expected behavior.
2. Diagnose whether the cause is a missing/ambiguous instruction, workflow gap, project context, or tool limitation.
3. Fix the smallest appropriate source; do not automatically append another rule.
4. Add or update a regression scenario under `tests/regression/`.
5. Re-run the new scenario and relevant existing scenarios.
6. Refactor redundant instructions only when regression checks can validate the change.
