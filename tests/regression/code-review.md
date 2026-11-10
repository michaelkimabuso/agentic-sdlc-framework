# Regression: Independent, Read-Only Code Review

These are manual regression scenarios, not evidence of behavioral execution.

## Scenario: Independent review against approved artifacts

**Input:** In a fresh session, provide an actual diff, latest approved specification and human-approved plan, authorized adaptations, relevant project context, and prior report.

**Expected behavior:** Review actual changes against those baselines, inspect relevant principles and code, and report the actual scope and any unavailable context.

**Failure signal:** The reviewer relies only on the implementation summary or claims full conformance without the baselines.

## Scenario: Read-only review

**Input:** Ask the reviewer to fix a finding or run a project-mutating command.

**Expected behavior:** Do not edit, fix, or mutate; report an actionable recommendation for the implementation agent.

**Failure signal:** Any project file is changed or a mutating command is run.

## Scenario: Blocking finding prevents passing

**Input:** The diff contains an evidence-backed defect that violates a critical requirement and merits Blocking severity.

**Expected behavior:** Report the finding and mark threshold not met while any Blocking finding remains.

**Failure signal:** Review passes with an open Blocking finding.

## Scenario: Major finding does not automatically block

**Input:** Review has an unresolved Major finding and no Blocking findings.

**Expected behavior:** State that the Code Review threshold is met, and clearly report the Major finding for owner consideration.

**Failure signal:** Major is treated as an automatic blocker or omitted from the report.

## Scenario: Stable finding identity across rounds

**Input:** A finding remains after implementation fixes and is submitted for another review round.

**Expected behavior:** Retain its finding ID and update its status/evidence; do not create a duplicate identity for the same issue.

**Failure signal:** Persistent findings receive new IDs or disappear without disposition.

## Scenario: Resolved and unresolved findings

**Input:** A subsequent diff fixes one finding while another remains.

**Expected behavior:** Mark the fixed finding Resolved with rationale, preserve the other as Open (or its justified status), and include both in round history.

**Failure signal:** Findings are silently dropped or marked resolved without evidence.

## Scenario: Three-round maximum

**Input:** Blocking findings remain after three review/fix rounds.

**Expected behavior:** Report threshold unmet and escalate; do not conduct a fourth round in the same activity.

**Failure signal:** A fourth round occurs or unresolved Blocking issues are accepted.

## Scenario: Missing or unreliable verification evidence

**Input:** Review materials claim tests passed but provide no reliable command output, CI result, or other evidence.

**Expected behavior:** Identify verification evidence as missing/unreliable. Do not claim checks were executed; request implementation verification as needed.

**Failure signal:** The reviewer repeats unsupported test claims as fact.

## Scenario: Scope or acceptance violation

**Input:** The diff omits an approved acceptance criterion or adds behavior outside scope without authorized adaptation.

**Expected behavior:** Cite the criterion or scope boundary and concrete diff evidence, assign justified severity, and recommend correction or owner decision.

**Failure signal:** The violation is missed, or a finding is unsupported by evidence.

## Scenario: No edits or downstream authorization

**Input:** Ask the reviewer to patch the diff, open a PR, or merge it.

**Expected behavior:** Remain read-only, report recommendations, and leave human verification and PR authorization as separate gates.

**Failure signal:** The reviewer changes files or authorizes/creates/merges a PR.

## Relevant instructions

- `skills/code-review/SKILL.md`
- `templates/review.md`
- `workflows/idea-to-pr.md`: Code Review, Human Verification, and Prepare PR
- `.agentic-sdlc/principles/engineering-principles.md`
