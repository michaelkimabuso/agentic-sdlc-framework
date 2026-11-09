---
name: plan-review
description: Independently review an implementation plan against its approved specification and project context before human plan approval.
---

# Plan Review

## Purpose

Evaluate whether a proposed plan is complete, feasible, grounded in the project, and faithful to approved requirements before implementation.

## When to use

Use after Planning has produced a plan and before the owner is asked to approve it. Start in a fresh session by default, independently of the planning session, with the relevant artifacts and repository context supplied.

## Inputs

- The approved specification or equivalent explicitly approved source.
- The proposed `plan.md` and relevant intent or product-breakdown context, when applicable.
- Project instructions, relevant code, architecture, dependencies, tests, and conventions needed to assess the plan.
- The existing review report for this activity, if a prior round exists.
- Shared principles: `.agentic-sdlc/principles/engineering-principles.md`.

## Outputs

Create or update the plan-review report using `templates/review.md` (normally `<work-item-artifact-directory>/reviews/plan-review.md`, unless project conventions or an explicit path say otherwise). Maintain one consolidated report for the activity and append review-round history.

For each finding, record a stable ID, severity (Blocking, Major, Minor, or Suggestion), precise location, evidence, recommended correction, status, and resolution rationale. Keep IDs stable across rounds; update prior findings rather than duplicating them. Record the round, date, outcome, changed findings, and remaining threshold findings in review history.

## Procedure

1. Review the approved requirements and plan independently. Inspect relevant project context to verify claims about code, conventions, dependencies, and feasibility.
2. Check requirement and acceptance-criteria coverage; technical feasibility and task order; relevant code areas; dependencies; risks and assumptions; unresolved owner decisions; and verification coverage. Look for missing implementation or verification work and unnecessary scope or complexity.
3. Ground findings in approved requirements, project evidence, or a clear feasibility/quality concern. Distinguish real gaps from preferences. Do not invent requirements or prescribe optional choices as defects.
4. Remain read-only. Report evidence and recommended corrections; do not edit the plan, code, or tests.
5. Use the shared review template and preserve finding IDs and round history. The planning or fixing session addresses findings; conduct each subsequent review round in a fresh session by default.
6. Allow no more than three review/fix rounds for the activity. After round three, unresolved Blocking or Major findings mean the plan cannot proceed and must be escalated.
7. Report the review outcome and threshold clearly. A review meets its threshold only when zero Blocking and zero Major findings remain.

## Boundaries

- This review is read-only; do not modify the plan or implementation.
- A passing review is not human plan approval. The owner must explicitly approve the plan before implementation begins.
- Minor findings and suggestions may remain visible for owner judgment; they do not satisfy or violate the Blocking/Major threshold by themselves.
- Follow `.agentic-sdlc/principles/engineering-principles.md`.

## Escalation

Escalate unresolved Blocking or Major findings after the third round, missing or unclear approval of the source requirements, or a material ambiguity requiring an owner decision. Never mark the plan ready for implementation without the applicable review threshold and explicit owner approval.
