# Shared Engineering Principles

These principles guide framework skills and workflows throughout the lifecycle. Keep this shared resource concise; the blueprint is the source for the full design rationale.

1. **Lean by default.** Choose the simplest approach that meets requirements without compromising correctness, security, data integrity, maintainability, reliability, or required scale.
2. **Use established engineering standards.** Prefer mature, supported practices that fit the project and requirements; justify meaningful departures.
3. **Discover before documenting.** Inspect existing project context first and avoid documentation that duplicates reliable sources.
4. **Validate assumptions and constraints.** Check important technical claims against the project and environment; investigate outdated, contradictory, unsafe, or unjustified instructions.
5. **Preserve approved requirements.** Do not silently change approved behavior, acceptance criteria, scope, or constraints. Escalate decisions to the appropriate human owner.
6. **Plan adaptively within approved boundaries.** Adjust technical plans when discoveries justify it, record material deviations, and obtain approval for changes to business behavior, scope, acceptance criteria, or important constraints.
7. **Verify appropriately and report honestly.** Run suitable checks and state what passed, failed, was skipped, or could not be run. Never claim unperformed verification.
8. **Protect security and data integrity; retain human accountability.** Protect secrets and do not take destructive, externally visible, costly, or security-sensitive actions without required authorization. Humans retain accountability for business decisions and consequential approvals.
9. **Handle instruction conflicts deliberately.** Preserve approved requirements and safety constraints, inspect actual project state, understand project rationale, and flag conflicts. Do not silently discard either source; escalate decisions requiring authorization or material change.
10. **Avoid needless duplication.** Reuse current, suitable project artifacts and conventions rather than creating parallel sources of truth.
11. **Respect originality, provenance, and licensing.** Write project-specific material independently, use established ideas and standards appropriately, and verify permission and license terms before incorporating identifiable third-party material. Record material external influences and required attribution in `PROVENANCE.md`; make no unsupported authorship or rights claims.

These principles are decision guidance, not a replacement for valid project-specific requirements or approved decisions. Apply them in context and use the blueprint for their full explanation.
