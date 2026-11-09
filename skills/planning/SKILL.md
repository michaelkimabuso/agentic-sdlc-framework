---
name: planning
description: Turn an approved specification into a codebase-grounded implementation and verification plan before application code changes begin.
---

# Planning

## Purpose

Produce a practical, ordered plan for implementing one approved work item. The plan describes intended work; it does not implement or verify it.

## When to use

Use after the owner has approved a specification. A current ticket or requirements document may serve as an equivalent source only when it is explicitly owner-approved and contains enough scope and acceptance detail to plan safely. Do not plan from an unapproved draft.

## Inputs

- The approved `spec.md` or equivalent explicitly approved requirements, including acceptance criteria and constraints.
- Relevant intent, product breakdown, project instructions, architecture documentation, existing decisions, code, tests, and project conventions.
- The work-item artifact directory and any existing `plan.md`.
- Shared principles: `.agentic-sdlc/principles/engineering-principles.md`.

## Outputs

Create or update `<work-item-artifact-directory>/plan.md` using `templates/plan.md`. The default path is `docs/tickets/<work-item-id>/plan.md`; respect established project conventions and explicit artifact paths instead. Reuse existing artifacts and do not create duplicate directories.

Set the plan approval status to **Draft** when creating or materially updating it. Change the status to **Approved** only after Plan Review meets its threshold and the owner explicitly approves the plan. Review passing alone is not approval.

The plan should be independently understandable and include:
- The approved source and acceptance criteria being planned.
- Relevant code areas and findings from project inspection.
- A concise technical approach and rationale.
- Ordered tasks, expected outcomes, relevant dependencies, and impacted areas.
- Risks, assumptions, open questions, and decisions requiring owner input.
- A verification strategy mapped to acceptance criteria, including tests and checks that should be run. Describe these as planned checks; do not imply they have been implemented or run.
- Explicit exclusions where useful to prevent scope expansion.

## Procedure

1. Confirm that the source is explicitly approved. If approval is absent or unclear, stop and request approval; do not create a plan as though the gate were met.
2. Read the source requirements and relevant linked artifacts. Preserve approved behavior, scope, acceptance criteria, and constraints.
3. Inspect relevant project instructions, architecture, source areas, dependencies, tests, and established conventions before proposing implementation. Verify assumptions against repository reality; note conflicts rather than silently resolving consequential ones.
4. Map each acceptance criterion to the work and verification needed. Identify impacted areas, task order, dependencies, risks, assumptions, and unresolved decisions.
5. Choose the smallest coherent technical approach that satisfies the approved requirements and shared engineering principles. Escalate decisions needing owner input, especially those that could change requirements, behavior, scope, or important constraints.
6. Draft or update `plan.md` using the shared template and set its approval status to Draft. Keep it actionable and avoid restating the specification or adding application code.
7. Hand the plan to Plan Review. Planning does not approve the plan or authorize implementation.

## Boundaries

- Do not write application code, implement tests, or execute the proposed verification.
- Do not silently change approved requirements, acceptance criteria, scope, or business behavior.
- Do not duplicate the specification; reference its criteria and explain how planned work addresses them.
- Do not present assumptions as confirmed facts or unresolved decisions as settled.
- Follow `.agentic-sdlc/principles/engineering-principles.md`.

## Escalation

Pause and ask the owner when approval is missing, requirements or technical constraints are unresolved in a way that affects safe planning, instructions or architecture conflict materially, or a proposed approach would change approved behavior, scope, acceptance criteria, or important constraints. Record the question and its impact; do not choose for the owner.
