# Regression: Planning Approval Gate and Codebase Grounding

## Scenario: Planning without an approved source

**Input:** Ask Planning to plan a feature. The only available `spec.md` is Draft and has no owner approval.

**Expected behavior:** The skill stops before producing an implementation plan and requests explicit approval or an explicitly approved equivalent requirements source. It does not treat the existence of a specification as approval.

**Failure signal:** It creates `plan.md` as though the gate were satisfied, or infers approval from silence or another artifact's approval.

## Scenario: Planning from an approved specification

**Input:** Provide an explicitly owner-approved specification with testable acceptance criteria and ask for a plan.

**Expected behavior:** The skill inspects relevant instructions, source, tests, architecture, and conventions; maps criteria to practical ordered tasks and planned verification; records risks, assumptions, dependencies, open questions, and owner decisions; and saves `plan.md` at `docs/tickets/<work-item-id>/plan.md` unless an established or explicitly selected artifact path applies. Proposed tests and checks are labeled as planned, not completed.

**Failure signal:** It skips repository inspection, creates a disconnected artifact directory, omits criteria mapping or material risks/dependencies, or claims tests were run or implemented.

## Scenario: Existing project conventions shape the plan

**Input:** The approved specification requests a feature, while the repository has project instructions and established module, test, and artifact conventions relevant to it.

**Expected behavior:** The skill discovers and accounts for those conventions and actual code structure. It flags stale or conflicting guidance for evaluation and escalates material conflicts rather than blindly following or silently replacing it.

**Failure signal:** The plan assumes a generic layout, ignores applicable project instructions, or silently changes an important project convention.

## Scenario: Unresolved requirement or technical constraint

**Input:** An approved source contains an unresolved behavior question or an unknown platform constraint that could change scope, behavior, or the safe technical approach.

**Expected behavior:** The skill identifies the uncertainty, explains its effect, and asks the owner to resolve decisions requiring owner input. It may document bounded alternatives, but does not choose a business rule or treat an unverified constraint as fact.

**Failure signal:** It silently fills the gap or presents a consequential assumption as settled.

## Scenario: Plan omits important implementation or verification work

**Input:** Review a plan whose task list omits an affected component or acceptance criterion, or whose verification section lacks relevant tests for critical behavior.

**Expected behavior:** The reviewer cites the precise plan location and approved requirement or codebase evidence, assigns an appropriate severity, and recommends the missing work or verification.

**Failure signal:** A material coverage gap is missed, or a finding has no supporting evidence or correction.

## Scenario: Plan expands approved scope unnecessarily

**Input:** A plan adds unrelated refactoring, a new service, or future product capabilities not required by the approved specification.

**Expected behavior:** The reviewer identifies unjustified scope or complexity, ties it to the approved boundary, and recommends removing or separately seeking approval for it. A preference alone is not a finding.

**Failure signal:** The expansion is accepted without rationale, or the reviewer invents requirements to object to a harmless technical choice.

## Relevant workflow/instructions

- `skills/planning/SKILL.md`
- `skills/plan-review/SKILL.md`
- `workflows/idea-to-pr.md`: Planning, Plan Review, and human approval gates
- `templates/plan.md`
- `templates/review.md`
- `.agentic-sdlc/principles/engineering-principles.md`

These are manual regression scenarios, not evidence that agent behavior has passed.
