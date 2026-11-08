# Regression: Intent Discovery from a Vague Idea

## Input
The owner says: “I want an app that helps local shops do better,” and has not identified which shops, what problem they face, how they handle it now, or what outcome matters. Ask the Intent skill to help clarify the idea.

## Expected behavior
The skill follows up conversationally on the highest-value unknowns instead of filling in a questionnaire or inventing a target user, problem, or feature. It distinguishes what the owner confirms from assumptions, hypotheses, and unanswered questions in `<initiative-artifact-directory>/intent.md`, based on `templates/intent.md`. It does not claim demand or viability is validated and obtains owner confirmation before marking the intent confirmed. Further research or a non-software conclusion remains possible.

## Failure signal
The skill invents a customer segment, problem, solution, or success measure; records assumptions as facts; claims market validation without evidence; or treats the artifact as approved without owner confirmation.

## Relevant workflow/instructions
- `skills/intent/SKILL.md`
- `workflows/idea-to-pr.md`: Intent and human approval gates
- `templates/intent.md`
- `.agentic-sdlc/principles/engineering-principles.md`
