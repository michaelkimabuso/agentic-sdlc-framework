---
name: product-breakdown
description: Progressively shape a broad initiative or existing product/backlog into capabilities, candidate deliverables, and a prioritized next increment approved by its owner.
---

# Product Breakdown

## Purpose

Help an owner turn a broad initiative into a useful, revisable decomposition and select a manageable next increment. Keep the result at product/initiative level.

## When to use

Use for a broad product or initiative, including an existing product or backlog that needs review or restructuring. Skip for already-scoped work when decomposition adds no value. Intent is optional when an existing brief, approved requirements, product context, or backlog provides sufficient information.

## Inputs

- An approved `intent.md`, an articulated initiative, existing product/requirements, or an existing backlog.
- The project context and existing owner-approved commitments.
- The initiative artifact directory and any existing `product-breakdown.md`.
- Shared principles: `.agentic-sdlc/principles/engineering-principles.md`.

## Outputs

Create or update `<initiative-artifact-directory>/product-breakdown.md` using `templates/product-breakdown.md`. Use the explicit project-root-relative path agreed at workflow start; the default is `docs/initiatives/<initiative-id>/product-breakdown.md`. Reuse the artifact directory and preserve current approved decisions.

Include useful capabilities, candidate deliverables/work items, dependencies and sequencing, possible increments, uncertainty, and a proposed next increment. Record the owner's approval and explicit selected increment and scope in the template's decision section.

## Procedure

1. Inspect the supplied source material and existing breakdown. Reuse sufficient context; do not require the Intent skill or repeat discovery unnecessarily.
2. Establish desired outcomes, users, constraints, confirmed information, assumptions, dependencies, and open questions. Preserve owner-approved commitments; distinguish proposed restructuring from approved changes.
3. Identify the capabilities or areas of value, then candidate deliverables and work items at only the levels useful to this initiative.
4. Identify dependencies, sequencing, and a small number of plausible increments. Explain prioritization rationale and uncertainty without presenting it as validated market research.
5. Refine the likely next increment enough to hand off for Specification. Do not write detailed specifications or technical implementation plans for all candidates.
6. Draft or update `product-breakdown.md` using the template. Avoid exhaustive backlog generation; leave future items at a useful high level.
7. Review the proposed breakdown with the owner. Obtain explicit approval of the breakdown and explicit selection and scope of the next increment before handing it to Specification. Record decisions, deferrals, and unresolved questions.

## Boundaries

- This is a product/initiative decomposition, not an exhaustive task backlog, business validation, detailed specification, or technical implementation plan.
- Do not independently approve scope, priorities, or roadmap commitments, and do not alter approved commitments without owner authorization.
- Do not present prioritization rationale as evidence of customer demand or viability.
- Follow `.agentic-sdlc/principles/engineering-principles.md`.

## Escalation

Pause and ask the owner when desired outcomes conflict, material dependencies or assumptions are unresolved, proposed changes affect approved commitments, or the owner has not approved the breakdown and selected the next increment. Acknowledge research needs rather than filling evidence gaps with guesses.
