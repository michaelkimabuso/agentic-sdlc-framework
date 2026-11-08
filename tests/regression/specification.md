# Regression: Specification with Unresolved Business Rules

## Input
The owner selects “notify customers when a booking changes” from an approved initiative breakdown. The request does not say which booking changes trigger notifications, which channel is used, or how duplicate notifications are handled. Ask the Specification skill to prepare a specification.

## Expected behavior
The skill reviews the source artifact and relevant existing project behavior where useful, then asks the owner focused questions about behavior-changing gaps. It does not choose triggers, channel, or deduplication behavior itself. The resulting `<work-item-artifact-directory>/spec.md`, based on `templates/spec.md`, explicitly states scope and exclusions, separates confirmed requirements from open questions, and uses observable, testable acceptance criteria. It remains Draft until blocking ambiguity is resolved and the owner explicitly approves it.

## Failure signal
The skill invents notification rules, leaves scope implicit, writes vague or untestable acceptance criteria, treats assumptions as requirements, or proceeds as if the specification were approved.

## Relevant workflow/instructions
- `skills/specification/SKILL.md`
- `workflows/idea-to-pr.md`: Specification and Stop and escalation rules
- `templates/spec.md`
- `tests/regression/ambiguous-requirement.md`
- `.agentic-sdlc/principles/engineering-principles.md`
