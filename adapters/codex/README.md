# Codex Adapter

This directory documents how the tool-agnostic workflow is mapped to OpenAI Codex. The workflow definition in `workflows/idea-to-pr.md` remains the source of truth for stages, artifacts, approval gates, and stop conditions.

## Adapter responsibilities

- Tell Codex where to find and follow the workflow and artifact templates.
- Make the current stage, approved artifacts, and next expected output explicit.
- Preserve the workflow's conditional approval gates, including owner approval of a product breakdown and increment selection when Product Decomposition is used, specification approval, plan approval after Plan Review, approval of material scope/behavior changes, and authorization before PR creation.
- Invoke Plan Review and Code Review as separate activities in fresh sessions by default; preserve their bounded review/fix loops and human approval gates.
- Use Codex's native repository and coding capabilities rather than introducing a custom orchestration engine.
- Report tool limitations and verification results honestly.

## Initial scope

M1 is guided, not autonomous. Do not enable unattended implementation, automatic merging, deployment, or other out-of-scope actions. The exact Codex instruction/configuration mechanism should be chosen and validated in a small real run before adding more adapter files.

## Portability

Keep product-specific syntax, commands, and configuration here. Do not put Codex-only instructions into the tool-agnostic workflow unless they are genuinely workflow requirements.
