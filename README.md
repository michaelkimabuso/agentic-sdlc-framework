# Agentic SDLC Framework

A reusable, tool-agnostic framework for guiding AI coding agents through software delivery with focused skills, explicit artifacts, verification, and human approval gates.

## Project status

**Current milestone:** M1 — Guided Idea-to-PR  
**Implementation and validation status:** M1 implementation and Increment 5 end-to-end validation in a disposable sample application are complete. The validation used Codex CLI 0.167.2 on Linux WSL2 x86_64; compatibility evidence is limited to that tested setup and the separate Increment 3 compatibility spike documented in [the adapter guide](adapters/codex/README.md). This remains an unreleased development version (`0.1.0-dev`) pending a release decision. Known limitations and unvalidated cases remain documented.

M1 is designed to guide work from an idea or existing task to an authorized, reviewable pull request. It does not include automatic merging, deployment, or unrestricted autonomous operation.

## Start here

- [M1 Blueprint](M1-BLUEPRINT.md) — architecture, scope, principles, skill definitions, implementation plan, and completion criteria.
- [Idea-to-PR Workflow](workflows/idea-to-pr.md) — workflow stages, entry points, artifacts, review loops, approval gates, and escalation rules.
- [Provenance](PROVENANCE.md) — material external influences and identifiable third-party material incorporated into the project.
- [License](LICENSE) — Apache License 2.0.

## How the framework is organized

The framework separates the tool-agnostic process from its project integration and coding-agent adapters.

- **Workflow:** Coordinates stages, handoffs, and human approval gates.
- **Skills:** Define focused activities: Intent, Product Breakdown, Specification, Planning, Plan Review, Implementation, and Code Review. All seven core skills were discovered and used during Increment 5 validation.
- **Templates:** Define reusable initiative, work-item, and review artifacts. The templates cover intent, product breakdown, specification, plan, and review reports.
- **Adapters:** Map the framework to a coding agent's native conventions. The Codex adapter includes its installer; additional adapters are deferred.
- **Installer and validation:** The Codex installer copies framework resources and protects modified managed files during updates. Its 16-case automated suite passed, and a disposable standard-library Python CLI application completed the Increment 5 end-to-end workflow validation. This evidence does not establish compatibility beyond the documented environments or versions.

## Installation and use

The Codex adapter can be installed from a framework checkout using Python 3.10 or newer:

```sh
python3 adapters/codex/install.py --target ../your-project --adapter codex
```

See [the Codex adapter guide](adapters/codex/README.md) for update behavior, conflicts, validation evidence, and limitations. The installer itself does not run Codex or validate an application's workflow; those behaviors were evaluated separately during Increment 5.

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
