# Codex Adapter

This directory documents how the tool-agnostic workflow is mapped to OpenAI Codex. The workflow definition in `workflows/idea-to-pr.md` remains the source of truth for stages, artifacts, approval gates, and stop conditions.

## Adapter responsibilities

- Tell Codex where to find and follow the workflow and artifact templates.
- Make the current stage, approved artifacts, and next expected output explicit.
- Preserve approval gates: do not move from intent to specification, specification to planning, plan to implementation, or human verification to PR creation without the approvals defined by the workflow.
- Use Codex's native repository and coding capabilities rather than introducing a custom orchestration engine.
- Report tool limitations and verification results honestly.

## Initial scope

M1 is guided, not autonomous. Do not enable unattended implementation, automatic merging, deployment, or other out-of-scope actions. The exact Codex instruction/configuration mechanism should be chosen and validated in a small real run before adding more adapter files.

## Portability

Keep product-specific syntax, commands, and configuration here. Do not put Codex-only instructions into the tool-agnostic workflow unless they are genuinely workflow requirements.
