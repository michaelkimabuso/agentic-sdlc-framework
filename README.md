# Agentic SDLC Framework

A reusable, tool-agnostic framework for guiding AI coding agents through software delivery with focused skills, explicit artifacts, verification, and human approval gates.

## Project status

**Current milestone:** M1 — Guided Idea-to-PR  
**Implementation status:** The tool-agnostic core and Codex adapter are implemented, including a standard-library installer and automated installer tests. Codex compatibility evidence remains limited to the CLI 0.167.0 Linux/WSL2 environment described in [the adapter guide](adapters/codex/README.md). End-to-end sample-application workflow validation remains incomplete; this is an unreleased development version.

M1 is designed to guide work from an idea or existing task to an authorized, reviewable pull request. It does not include automatic merging, deployment, or unrestricted autonomous operation.

## Start here

- [M1 Blueprint](M1-BLUEPRINT.md) — architecture, scope, principles, skill definitions, implementation plan, and completion criteria.
- [Idea-to-PR Workflow](workflows/idea-to-pr.md) — workflow stages, entry points, artifacts, review loops, approval gates, and escalation rules.
- [Provenance](PROVENANCE.md) — material external influences and identifiable third-party material incorporated into the project.
- [License](LICENSE) — Apache License 2.0.

## How the framework is organized

The framework separates the tool-agnostic process from its project integration and coding-agent adapters.

- **Workflow:** Coordinates stages, handoffs, and human approval gates.
- **Skills:** Define focused activities: Intent, Product Breakdown, Specification, Planning, Plan Review, Implementation, and Code Review. All seven core skill instructions are implemented; agent behavior still requires validation.
- **Templates:** Define reusable initiative, work-item, and review artifacts. The templates cover intent, product breakdown, specification, plan, and review reports.
- **Adapters:** Map the framework to a coding agent's native conventions. The Codex adapter includes its installer; additional adapters are deferred.
- **Installer and validation:** The Codex installer copies framework resources and protects modified managed files during updates. Automated installer tests cover these behaviors; end-to-end validation in a sample application remains incomplete.

## Installation and use

The Codex adapter can be installed from a framework checkout using Python 3.10 or newer:

```sh
python3 adapters/codex/install.py --target ../your-project --adapter codex
```

See [the Codex adapter guide](adapters/codex/README.md) for update behavior, conflicts, and limitations. This is an unreleased development installer; it does not run Codex or validate an application's workflow.

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
