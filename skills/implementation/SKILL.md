---
name: implementation
description: Implement an explicitly approved specification and human-approved plan, adapting technical details within approved boundaries.
---

# Implementation

## Purpose

Implement one approved work item against its current project state, preserving approved behavior, scope, acceptance criteria, and constraints.

## When to use

Use only after both the specification (or equivalent requirements source) is explicitly approved and the plan has passed Plan Review and is explicitly human-approved. A review result alone does not approve either artifact.

## Inputs

- The approved specification or equivalent owner-approved requirements, including acceptance criteria and constraints.
- The plan with explicit human approval and its Plan Review outcome.
- Relevant project instructions, architecture and decision records, source, tests, dependencies, and conventions.
- Existing work-item artifacts and applicable review reports.
- Shared principles: `.agentic-sdlc/principles/engineering-principles.md`.

## Outputs

- Focused implementation and appropriate automated tests.
- Updated plan and, when appropriate, specification documenting authorized clarifications or material technical adaptations.
- An implementation summary covering changed files, deviations, actual verification results, and outstanding concerns.

## Procedure

1. Locate both baseline artifacts and verify their approval status and provenance. If either is missing, draft, or unclear, stop implementation and request the required approval. Do not approve the plan yourself.
2. Read the approved requirements, acceptance criteria, constraints, and plan. Inspect the current repository state, relevant source and tests, project instructions, architecture, dependencies, and conventions before relying on planned assumptions. Check whether assumptions remain true and whether local changes or recent project changes affect the work.
3. Reconcile the plan with reality. Flag stale, unsafe, contradictory, or materially incomplete assumptions. Preserve approved requirements and constraints; ask the owner when a safe technical path depends on their decision.
4. Implement the smallest coherent change that meets the baseline. Add or update appropriate automated tests. Follow project conventions and avoid unrelated refactoring, new abstractions, or scope expansion.
5. Adapt technical details when discoveries make the planned approach unsuitable and approved requirements, acceptance criteria, scope, and constraints remain intact. Minor implementation choices need no new approval. For a material technical deviation, record in the plan: discovery; original approach; adjusted approach; justification; and impacts on files, tests, risks, and verification. Pause affected work and request explicit owner approval before proceeding if the proposal affects business behavior, scope, acceptance criteria, important product requirements, user-visible behavior, privacy, security or data-integrity guarantees, or significant architectural or operational constraints. Do not treat technical adaptation itself as a new approval gate when those approved boundaries remain intact.
6. After approval of a material change, update the relevant specification and/or plan before continuing. Revisit Plan Review when significance or changed risk makes the previous review no longer adequate; obtain human plan approval again if the approved baseline materially changes. A rejected proposal is not implemented: retain the existing approved behavior, revert/avoid the affected change, and report the decision and any safe work that remains possible.
7. Run appropriate available verification, including relevant automated tests and project-defined checks. Fix in-scope failures and rerun affected checks. Record command/check and actual outcome. Clearly separate executed checks from checks merely planned or recommended; report failures, skips, and checks that could not run. Never claim an unexecuted or unsuccessful check passed.
8. Inspect the final diff for scope, accidental changes, generated artifacts, and secrets. Do not self-review as a substitute for independent Code Review.

## Boundaries

- Do not approve the specification or plan, or silently reinterpret or weaken approved requirements.
- Do not perform Code Review of your own work as a substitute for independent review.
- Do not authorize or create a PR, merge a branch or PR, or deploy to production.
- Follow `.agentic-sdlc/principles/engineering-principles.md` and applicable project instructions.

## Escalation

Pause affected work and ask the owner when approval is absent, a material deviation crosses an approval boundary, a requirement or constraint conflicts with repository reality, a proposed change could weaken security or data integrity, or a safe fix/verification path is unclear. Report the decision and any work that can safely continue independently.
