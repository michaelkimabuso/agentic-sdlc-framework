# Regression Scenarios

Keep small, reusable scenarios for agent failures and workflow behavior. These are initially manual test cases, not a claim of automated test coverage.

Each scenario should state:
- **Input:** The minimum prompt/context needed to reproduce the situation.
- **Expected behavior:** What the agent should do.
- **Failure signal:** Observable behavior that means the scenario failed.
- **Relevant workflow/instructions:** Where a correction would likely belong.

When a failure occurs, add a scenario before or alongside changing instructions. Run it after the fix and run relevant existing scenarios to catch regressions. Avoid adding a new rule for every failure without first diagnosing the root cause.
