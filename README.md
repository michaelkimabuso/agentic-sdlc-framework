# Agentic SDLC Framework

A reusable, tool-agnostic framework for guiding AI coding agents through software delivery with focused skills, explicit artifacts, verification, and human approval gates.

## Project status

**Current milestone:** M1 — Guided Idea-to-PR  
**Implementation status:** Architecture and workflow are documented; framework skills, templates, installer, and Codex integration are still being implemented and validated. This repository is not yet a ready-to-install release.

M1 is designed to guide work from an idea or existing task to an authorized, reviewable pull request. It does not include automatic merging, deployment, or unrestricted autonomous operation.

## Start here

- [M1 Blueprint](M1-BLUEPRINT.md) — architecture, scope, principles, skill definitions, implementation plan, and completion criteria.
- [Idea-to-PR Workflow](workflows/idea-to-pr.md) — workflow stages, entry points, artifacts, review loops, approval gates, and escalation rules.
- [Provenance](PROVENANCE.md) — material external influences and identifiable third-party material incorporated into the project.
- [License](LICENSE) — Apache License 2.0.

## How the framework is organized

The framework separates the tool-agnostic process from its project integration and coding-agent adapters.

- **Workflow:** Coordinates stages, handoffs, and human approval gates.
- **Skills:** Define focused activities such as Intent, Product Breakdown, Specification, Planning, Plan Review, Implementation, and Code Review. Intent, Product Breakdown, and Specification are implemented; the other four remain planned, and agent behavior still requires validation.
- **Templates:** Define reusable initiative, work-item, and review artifacts. The planned templates cover intent, product breakdown, specification, plan, and review reports.
- **Adapters:** Map the framework to a coding agent's native conventions. Codex is the first planned adapter; additional adapters are deferred.
- **Installer and validation:** Planned M1 work includes safe installation/update behavior and validation in a sample application. No installer or successful end-to-end agent validation is claimed yet.

## Installation and use

There is no supported installation process or released package yet. The [M1 Blueprint](M1-BLUEPRINT.md) documents the intended installer design and Codex integration validation. Until those are implemented and tested, use the workflow and blueprint as design documentation rather than treating the repository as a functioning drop-in framework.

## Contributing

The framework is under active design and implementation. Before proposing changes:

1. Read the [M1 Blueprint](M1-BLUEPRINT.md) and [Idea-to-PR Workflow](workflows/idea-to-pr.md).
2. Keep the core tool-agnostic; place coding-agent-specific conventions in the relevant adapter.
3. Preserve explicit human approval, verification, security, and data-integrity requirements.
4. Prefer focused changes and update relevant regression scenarios when correcting workflow behavior.
5. Identify material external influences or incorporated third-party material in [PROVENANCE.md](PROVENANCE.md), including applicable license and notice requirements.

Issues and pull requests should explain the problem, proposed change, relevant workflow or architecture impact, and how the change was verified.

## Project attribution

**Project creator and maintainer:** Michael Kim Abuso

This project was developed with AI assistance. The project direction, requirements, architectural decisions, and final review are maintained by the project maintainer.

## License

This project is distributed under the [Apache License, Version 2.0](LICENSE) (Apache-2.0). The license applies to material the project maintainer is authorized to license. Third-party material remains subject to its applicable rights and license terms. See [PROVENANCE.md](PROVENANCE.md) for material external influences and identifiable third-party material incorporated into the project.
