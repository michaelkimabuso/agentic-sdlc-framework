---
name: specification
description: Turn an approved initiative item, intent, or sufficiently clear ticket into an explicit, testable specification for owner review before planning.
---

# Specification

## Purpose

Define expected behavior and boundaries for one selected work item so it can be planned without relying on unstated decisions.

## When to use

Use for a selected product-breakdown item, approved intent, ticket, or other request when requirements need clarification or consolidation. If an approved specification or equivalent current requirements already suffice, reuse them rather than duplicating them.

## Inputs

- The selected work item and its source: approved intent, product breakdown, ticket, or requirements.
- Relevant existing artifacts and project context; inspect the project where useful to understand current behavior and conventions.
- The work-item artifact directory and any existing `spec.md`.
- Shared principles: `.agentic-sdlc/principles/engineering-principles.md`.

## Outputs

Create or update `<work-item-artifact-directory>/spec.md` using `templates/spec.md`. Use the explicit project-root-relative path agreed at workflow start; the default is `docs/tickets/<work-item-id>/spec.md` (or the project's established equivalent). Reuse existing artifacts and avoid duplicate directories.

The specification states source, problem/outcome, in-scope and excluded behavior, requirements, testable acceptance criteria, relevant edge/failure behavior, data/security/privacy considerations, dependencies, constraints, assumptions, open questions, and approval status.

## Procedure

1. Review the source request and linked approved decisions. Inspect relevant project files or existing behavior when that helps clarify context. Do not infer business behavior solely from implementation details.
2. Define the work item's scope, exclusions, expected behavior, and observable functional and non-functional requirements. Preserve approved requirements; do not add scope or technical decisions without authorization.
3. Identify relevant edge cases, failure scenarios, security, privacy, data integrity, dependencies, and constraints. Mark non-applicable concerns with a brief reason where useful.
4. Separate confirmed requirements from assumptions and open questions. Check for ambiguity, contradiction, completeness, and testability. Ask the owner focused questions about decisions that materially affect behavior, scope, or acceptance.
5. Draft or update `spec.md` using `templates/spec.md`. Write acceptance criteria that can be observed and verified, without embedding unapproved solutions.
6. Resolve blocking ambiguity with the owner, update the artifact, and request explicit owner approval. Keep the status Draft until approval is explicit; approval of an earlier artifact does not approve this specification.

## Boundaries

- Do not invent business rules, silently convert assumptions into requirements, or treat unanswered behavior-changing questions as settled.
- Do not expand selected scope or choose consequential technical approaches on the owner's behalf.
- Do not create a separate Specification Review activity or proceed to planning as though an unapproved or materially ambiguous specification were approved.
- Follow `.agentic-sdlc/principles/engineering-principles.md`.

## Escalation

Pause and ask the owner when requirements conflict, a business decision affects behavior or acceptance, scope or constraints are unclear, or safe interpretation is uncertain. Record the question and alternatives without selecting one. Do not mark the specification approved while a blocking question remains or without explicit owner approval.
