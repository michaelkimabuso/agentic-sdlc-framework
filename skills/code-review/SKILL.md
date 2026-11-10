---
name: code-review
description: Independently review implementation changes against approved requirements and plan, reporting evidence-based findings without modifying the project.
---

# Code Review

## Purpose

Independently assess actual changes for correctness, regressions, maintainability, security, data integrity, test coverage, and scope compliance.

## When to use

After implementation verification, or independently for an existing PR when the available context permits. Prefer a fresh session separate from implementation. Use the adapter's native review mechanism when available, while keeping this skill tool-agnostic.

## Inputs

- The actual diff or PR and relevant repository context.
- The latest approved specification or equivalent approved requirements and human-approved plan.
- Documented adaptations and their owner authorization where required.
- Relevant project instructions, code, tests, architecture, and `.agentic-sdlc/principles/engineering-principles.md`.
- The consolidated Code Review report from prior rounds, if any.
- Verification evidence from the implementation session or CI, when available.

## Outputs

Create or update one consolidated report using `templates/review.md` (normally `<work-item-artifact-directory>/reviews/code-review.md`). Record actual review scope, baseline artifacts, limitations, round history, findings, threshold, and disposition.

## Procedure

1. Establish the review baseline: latest approved requirements and plan, authorized adaptations, actual diff, and prior report. Inspect relevant project context and engineering principles. If an artifact is unavailable, state the limitation and do not claim full conformance review.
2. Review the actual changes, not just their description. Check requirement and acceptance-criteria coverage, correctness, regression risk, maintainability, security, data integrity, test coverage, and scope. Treat unapproved changes crossing approved boundaries as findings. Ground each finding in concrete diff, artifact, or repository evidence; avoid speculation and immaterial style preferences.
3. Remain strictly read-only. Do not edit files, apply fixes, or run commands that modify the project. Recommend corrections for the implementation session.
4. Maintain stable finding IDs in the consolidated report. For each finding record severity, precise file/location when possible, evidence and explanation, recommended correction, status, and resolution rationale. Preserve identity for a persisting issue; mark a finding Resolved only when evidence supports resolution. Keep unresolved findings visible across rounds; do not silently discard them. Rejected or deferred findings retain their status and rationale.
5. Record each round in review history. Allow at most three review/fix rounds for this activity. After fixes, the implementation agent must rerun appropriate automated checks before another review; inspect reliable evidence, but do not claim to have executed those checks yourself. At round three, unresolved Blocking findings mean the threshold is unmet and must be escalated; do not start a fourth round under the same activity.
6. Apply the established threshold: Code Review passes only with zero Blocking findings. Major findings do not automatically block; report all unresolved Major, Minor, and Suggestion findings clearly for owner consideration. Human verification and PR authorization remain separate workflow gates.
7. Report limitations, missing or unreliable verification evidence, and the exact reviewed scope. Do not invent test results. Distinguish review observations from checks demonstrably run by another reliable source.

## Boundaries

- Do not modify code or other project files, fix findings, or run project-mutating commands.
- Do not approve product/business changes or the implementation plan.
- Do not authorize PR creation or merging. A passing review does not replace human verification or PR authorization.
- Follow `.agentic-sdlc/principles/engineering-principles.md`.

## Escalation

Report a missing baseline or unreliable evidence as a limitation. Escalate unresolved Blocking findings after round three, and ask the owner when resolving a finding requires a product decision or material change to approved behavior, scope, or constraints.
