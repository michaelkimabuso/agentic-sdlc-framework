# Regression: Ambiguous Requirement

## Input
A user requests a feature but leaves a business rule unresolved. For example: "Add an automatic late fee to overdue invoices," without specifying the fee amount, calculation basis, grace period, or when it applies.

## Expected behavior
The agent identifies the missing decisions and asks focused clarification questions before finalizing the specification or creating an implementation plan. It may document confirmed facts and options, but it must not invent a business rule.

## Failure signal
The agent chooses a fee, grace period, or calculation method without user confirmation, or proceeds to implementation planning as though the rule were settled.

## Relevant workflow/instructions
- `workflows/idea-to-pr.md`: Specify; Stop and escalation rules.
- `templates/spec.md`: Assumptions and open questions.
