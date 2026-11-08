---
name: intent
description: Clarify an early or incomplete idea with its owner and capture the problem, context, affected people, outcomes, and constraints before product shaping or specification.
---

# Intent

## Purpose

Help an owner make a vague, incomplete, or poorly defined idea clear enough to decide what should happen next. This is guided discovery, not solution design or market validation.

## When to use

Use when the problem, opportunity, affected people, context, outcomes, or constraints are unclear. Skip when a current, approved intent or equivalent source already provides the needed context.

## Inputs

- The owner's initial idea and any available notes, evidence, or project context.
- The artifact directory selected for this initiative; use its existing `intent.md` if present.
- Shared principles: `.agentic-sdlc/principles/engineering-principles.md`.

## Outputs

Create or update `<initiative-artifact-directory>/intent.md` using `templates/intent.md` as the starting structure. Use the explicit project-root-relative artifact path agreed at workflow start; the default is `docs/initiatives/<initiative-id>/intent.md`. Keep useful existing content and do not create a duplicate artifact directory.

The artifact records the problem or opportunity, affected people, current situation and evidence, desired outcomes, scope, constraints, assumptions, open questions, and owner confirmation. Label facts, assumptions, hypotheses, and unanswered questions distinctly.

## Procedure

1. Review the idea and relevant existing artifacts. Do not ask for information already available.
2. Discover adaptively through focused conversation. Follow answers and ask questions whose answers could materially change the understanding or direction. Explore the problem/opportunity, affected people, current situation, impact, desired outcomes, constraints, and priorities as relevant; do not administer a fixed questionnaire.
3. Keep the discussion problem- and outcome-oriented. Do not prematurely prescribe software or technical solutions.
4. Separate owner-confirmed facts and evidence from assumptions, hypotheses, and unanswered questions. Record what evidence supports claims and what remains unverified.
5. Draft or update `intent.md` with the template, preserving the distinction between known and uncertain information. A conclusion that further research is needed, the opportunity is unclear, or software may not be appropriate is valid.
6. Show the owner the resulting intent and ask for confirmation or changes. Mark it confirmed only after explicit owner confirmation; silence is not approval.

## Boundaries

- Do not claim market demand, willingness to pay, customer validation, or product viability without evidence. Intent discovery alone establishes none of these.
- Do not turn assumptions into requirements or make business decisions for the owner.
- Do not duplicate suitable current artifacts or perform product breakdown, detailed specification, or implementation planning.
- Follow `.agentic-sdlc/principles/engineering-principles.md`.

## Escalation

Pause and ask the owner when a material business decision is unclear, evidence conflicts, priorities or constraints conflict, or the owner cannot confirm the intent. Record unresolved questions and any research needed; do not represent a draft as approved.
