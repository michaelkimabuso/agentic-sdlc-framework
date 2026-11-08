# Agentic SDLC Framework — M1 Blueprint

**Document status:** Approved architectural direction; implementation is in progress  
**Milestone:** M1 — Guided Idea-to-PR  
**Framework version:** Initial development; no release version assigned  
**Last updated:** 2026-11-04

> This document is the architectural and implementation reference for M1. It records the agreed design, intended behavior, boundaries, and completion criteria. It is not a runtime instruction file and does not replace the detailed workflow, skill instructions, or templates.

## 1. Purpose and vision

The Agentic SDLC Framework is a reusable, tool-agnostic framework for helping AI coding agents carry software work through a disciplined development lifecycle.

It aims to make agent-assisted software delivery more consistent, understandable, verifiable, and reusable across projects and coding-agent tools. It combines explicit work artifacts, focused skills, repeatable workflows, technical validation, and human approval at consequential decision points.

The framework should support both:
- **AI-Native development:** AI agents are integrated into ordinary engineering work, with humans retaining direction and accountability.
- **Agentic workflows:** Agents can perform multi-step work and coordinate skill handoffs within clearly defined boundaries and approval requirements.

The framework should not equate agentic behavior with unrestricted autonomy. M1 is guided and approval-driven.

## 2. Milestones and scope

### 2.1 Roadmap

| Milestone | Intended outcome | Status |
|---|---|---|
| M1 | Guided Idea-to-PR workflow, reusable skills, artifacts, Codex adapter, installer, and validation | Current milestone |
| M2 | Extend the lifecycle from PR through integration and deployment | Deferred |
| M3 | Incorporate post-deployment feedback into the development lifecycle | Deferred |
| M4 | Introduce controlled autonomous operation with explicit safeguards and an off switch | Deferred |
| M5 | Validate reuse across additional projects and coding-agent adapters | Future validation and expansion |

These milestones are directional. They do not imply that later capabilities are part of M1.

### 2.2 M1 goals

M1 must provide:
- A tool-agnostic framework core.
- Seven independently invokable skills, including optional product-level decomposition for broad initiatives.
- A guided Idea-to-PR workflow that composes those skills.
- Reusable templates for initiative-level and work-item artifacts and review reports.
- Human approval gates for requirements, implementation planning, and PR creation.
- Adaptive Planning for justified technical changes during implementation.
- A first coding-agent adapter for OpenAI Codex.
- A repeatable, safe installation and update process.
- Framework tests and an end-to-end Codex validation against a sample application.

### 2.3 M1 non-goals

M1 does not include:
- Automatic PR merging.
- Automatic deployment or production changes.
- Production monitoring or feedback loops.
- Unattended, unrestricted end-to-end autonomy.
- A custom orchestration engine.
- Multiple coding-agent adapters. Codex is the first adapter; other adapters can follow.
- Mandatory use of every workflow stage for every task.
- A complex evaluation platform for agent behavior.

M1 ends when a human-authorized, reviewable PR has been opened. Merging remains a separate human-authorized action.

## 3. Architecture

The framework has three layers.

### 3.1 Framework core

The core is tool-agnostic and contains:
- Engineering principles.
- Workflow definitions.
- Standalone skill definitions.
- Artifact templates.

The core describes what the process and skills must do. It should avoid depending on a particular coding agent's proprietary commands, configuration, or orchestration features.

### 3.2 Project integration

Project integration makes the framework usable in a specific application repository. It includes:
- Project-level agent instructions, such as AGENTS.md.
- Installed framework resources.
- The project's existing conventions and documentation.
- Work-item artifacts created while using the framework.

The framework must coexist with existing project instructions and conventions. It must not assume that every project has the same stack, directory layout, or documentation practices.

### 3.3 Coding-agent adapter

An adapter maps the framework core to a coding agent's native capabilities. The first adapter is Codex.

The adapter is responsible for:
- Installing skills where the coding agent can discover them.
- Integrating the framework with the project's agent instructions.
- Explaining how the agent should locate and invoke framework workflows and resources.
- Keeping product-specific syntax and requirements out of the tool-agnostic core.

Use native agent capabilities where practical. Do not build custom orchestration infrastructure in M1.

### 3.4 Separation of responsibilities

| Component | Responsibility |
|---|---|
| Principles | Shared engineering decision guidance |
| Workflow | Coordinates stages, transitions, and approval gates |
| Skill | Defines the detailed behavior of one focused activity |
| Template | Defines the structure of a generated artifact |
| Adapter | Maps core resources to a coding agent |
| Installer | Copies and integrates resources into a project |
| Tests | Validate framework software and agent behavior |

A workflow coordinates skills; it should not duplicate all of their detailed instructions. Skills define behavior; templates define document structure.

## 4. Engineering principles

The canonical shared principles live in .agentic-sdlc/principles/engineering-principles.md in the source repository and are installed at that same project-root-relative path.

All skills and workflows must follow these principles. They should reference the shared file rather than maintain conflicting copies of the same guidance.

### 4.1 Lean by default, without compromising quality

Prefer the simplest solution that reliably satisfies the requirements. Avoid unnecessary complexity, abstractions, dependencies, infrastructure, and unrelated refactoring.

Simplicity must not compromise correctness, security, data integrity, maintainability, reliability, or scalability where those qualities are required.

### 4.2 Established engineering practices

Prefer mature, widely adopted, well-supported standards and practices when they fit the requirements and project context.

Evaluate alternatives based on suitability, ecosystem maturity, security, maintainability, and long-term support. Do not equate industry standard with newest, most popular, or personally preferred. Emerging practices may be appropriate when their trade-offs are understood and justified.

This principle applies throughout the lifecycle, including requirements, architecture, APIs, data design, implementation, testing, dependencies, and operations.

### 4.3 Discover before documenting

Before requesting or creating additional project context, inspect relevant existing instructions, documentation, configuration, manifests, source code, tests, and CI configuration.

Create new documentation only when it captures information that cannot be reliably inferred from existing sources and has ongoing value. Avoid duplicating information that will drift.

### 4.4 Validate assumptions and constraints against reality

Project instructions, conventions, technical assumptions, dependencies, and architectural decisions must be evaluated against actual project state, approved requirements, security considerations, and established engineering practices.

Identify outdated, contradictory, unsafe, or unjustified instructions rather than blindly following them. Verify important technical assumptions against the current codebase and environment.

An unusual convention is not automatically wrong. Understand its purpose before recommending a change.

### 4.5 Preserve approved requirements and constraints

Approved business requirements, expected behavior, acceptance criteria, and scope cannot be silently changed by an agent.

Business decisions require the appropriate human owner. Security, regulatory, and data-integrity constraints must not be relaxed without appropriate authorization.

### 4.6 Adaptive Planning

An approved plan is a baseline, not immutable. During implementation, an agent may revise technical decisions when discoveries justify doing so, provided approved requirements, constraints, and scope are preserved.

Material deviations must be recorded with the discovery, original approach, adjustment, rationale, and impact. Changes that affect business behavior, acceptance criteria, scope, or important constraints require human approval.

### 4.7 Appropriate verification and honest reporting

Define and perform verification appropriate to the change. Report what was run, what passed or failed, what was skipped, and what could not be run. Never claim a test or check passed if it was not executed successfully.

### 4.8 Security, data integrity, and human accountability

Do not expose secrets in prompts, artifacts, logs, commits, or PRs. Do not perform destructive, externally visible, costly, or security-sensitive actions without the required authorization.

Agents may perform delegated technical work within approved boundaries. Humans retain accountability for business decisions, approval gates, and consequential actions.

### 4.9 Conflict handling

Framework principles guide engineering decisions; they do not automatically override valid project-specific requirements, conventions, or architectural decisions. Project instructions are important context, but they are not unquestionable truth.

When instructions conflict:
1. Preserve approved requirements and acceptance criteria.
2. Preserve security, regulatory, and data-integrity constraints.
3. Inspect actual project state and verify technical facts.
4. Understand the rationale for project conventions and architectural decisions.
5. Apply framework principles as decision guidance.
6. Flag unsafe, contradictory, outdated, or unjustified instructions.
7. Escalate when resolving the conflict requires a business decision, authorization, or material change.

Do not resolve a conflict by silently discarding either source.

### 4.10 Originality, provenance, and quality

Create project-specific documentation, skill instructions, templates, examples, and implementation in original wording and structure wherever practical. Do not copy or closely imitate third-party expressive material without permission or a license that allows the intended use.

Originality is not a requirement to reinvent established engineering practice. Use appropriate standards, common terminology, proven design patterns, and mature techniques when they best serve correctness, security, maintainability, reliability, and the user's requirements. Do not choose an inferior or unfamiliar approach merely to make the work appear unique.

Apply these rules proportionately:
- **Original expression:** Write framework-specific material for this project. Independent expression and implementation are preferred; unnecessary novelty is not.
- **Established ideas and practices:** General concepts, methods, standards, and common engineering practices may be used and adapted. Explain meaningful project-specific decisions in our own words.
- **Third-party material:** Before incorporating identifiable third-party text, code, templates, assets, or other protected material, verify that the source and license or permission allow the intended use. Preserve required notices and attribution.
- **External influence:** When a specific external work materially informs a design or a substantial project decision, record the source and describe the influence in the root PROVENANCE.md. Routine use of generic engineering knowledge does not need an entry.
- **No close imitation:** Do not reproduce distinctive wording, organization, examples, or other expressive choices from a source merely by changing a few words. When in doubt, summarize the underlying idea independently and cite the source where relevant.
- **Honest claims:** Do not claim that all project material is wholly original, exclusively human-authored, or guaranteed copyrightable. Disclose material AI assistance and respect the limits of applicable law and third-party rights.
- **Quality first:** These requirements must not weaken the solution. Prefer the best suitable, well-supported engineering approach while ensuring that incorporated material has a clear and lawful provenance.

Before a public release or material third-party incorporation, review provenance, license compatibility, required notices, and any unresolved ownership or permission questions. PROVENANCE.md is a practical record, not a guarantee of legal clearance.

## 5. Standalone skills

M1 contains seven standalone skills. Each skill must have clearly defined inputs, outputs, responsibilities, and boundaries. It must be independently invokable and must adapt to the context and artifacts available.

Every generated artifact must contain enough context for another qualified human or agent to understand and use it without relying on the original conversation or workflow session.

### 5.1 Intent

**Purpose:** Help an idea owner move from an initial idea—even a vague or incomplete business idea—to a clear articulation of the problem or opportunity, context, affected users, and desired outcomes before solution design begins.

- Optional in the Idea-to-PR workflow when equivalent context already exists.
- Accept both an early, loosely expressed idea and a more developed concept that needs refinement. Do not require a separate idea-formation exercise before invoking this skill.
- When the starting point is vague, facilitate guided discovery through adaptive, focused questions. Explore the motivation, potential audience, current situation or problem, impact, desired outcomes, constraints, priorities, assumptions, and important unknowns as relevant.
- Do not use a fixed questionnaire or ask for information already provided. Follow the most useful unanswered thread rather than mechanically covering every topic.
- Remain primarily business- and problem-oriented; avoid premature technical solutioning or assuming that software is necessarily the right answer.
- Distinguish owner-confirmed facts from assumptions, hypotheses, and unanswered questions.
- Discovery conversations do not establish market demand or validate a business opportunity. Where evidence is needed, identify appropriate follow-up validation such as customer interviews, market or competitor research, prototype testing, or willingness-to-pay research.
- It is acceptable for discovery to conclude that more research is needed, the opportunity is not yet clear, or a non-software solution may be more appropriate.
- Create or update intent.md. A draft may capture incomplete information, but critical unresolved business decisions must be acknowledged by the owner before the intent is treated as confirmed.

**Output:** intent.md.

### 5.2 Product Breakdown

**Purpose:** Turn a broad initiative or product intent into a useful, owner-reviewed structure of capabilities and candidate work items, so implementation can proceed in manageable increments.

Inputs may include intent.md, an existing product brief, requirements, an existing application, or a backlog that needs restructuring. Intent is useful context but is not mandatory when equivalent information exists.

Responsibilities:
- Understand the initiative's desired outcomes, users, constraints, known assumptions, and evidence gaps.
- Identify meaningful product capabilities or areas of value, then candidate epics or deliverables and work items where useful.
- Describe the purpose and expected outcome of each proposed item at an appropriate level; avoid prematurely writing detailed acceptance criteria for every item.
- Identify dependencies, sequencing constraints, opportunities for independently valuable increments, and a reasonable initial MVP or next increment when the available context supports it.
- Recommend prioritization with transparent rationale, while leaving final scope and priority decisions to the owner.
- Decompose progressively: provide a useful high-level structure first, then refine the selected capability or next increment into actionable work items. Do not generate an exhaustive speculative backlog by default.
- Distinguish confirmed information from assumptions, hypotheses, and unanswered questions. Flag where customer, market, regulatory, or operational validation is needed; decomposition itself does not validate demand or business viability.
- Adapt the structure to the initiative. Not every project needs every hierarchy level, and small, already-scoped tasks should bypass this skill.
- Review the proposed breakdown with the owner and record decisions, deferred items, dependencies, and unresolved questions.

Boundaries:
- Does not replace business discovery or market validation.
- Does not independently approve product scope, priorities, or roadmap commitments.
- Does not produce full specifications or technical implementation plans for every candidate item.
- Does not require an entire product backlog to be defined before the first increment can begin.

**Output:** product-breakdown.md, an initiative-level, revisable structure of capabilities and candidate work items.

### 5.3 Specification

**Purpose:** Define what the system should do for one selected deliverable, using an intent, product breakdown item, ticket, existing requirements, or other source material.

- Identify expected behavior, functional and non-functional requirements, scope, exclusions, and testable acceptance criteria.
- Identify edge cases, failure behavior, security and data considerations, dependencies, constraints, assumptions, and open questions.
- Inspect relevant existing project context.
- Avoid duplicating equivalent information from existing tickets or documents.
- Self-check for completeness, ambiguity, contradictions, and testability.
- Ask the owner to resolve important business ambiguity.
- Do not silently invent behavior-changing rules.

**Output:** spec.md.

M1 does not include a separate Specification Review skill. Important unresolved business questions are resolved by the human owner, and the specification performs its own completeness checks.

### 5.4 Planning

**Purpose:** Transform an approved specification into a technically sound, executable implementation plan before application code changes begin.

Required input: approved spec.md or equivalent approved ticket/requirements. Optional inputs include intent.md, project instructions, architecture documentation, existing decisions, and relevant code.

Responsibilities:
1. Understand requirements, expected behavior, acceptance criteria, constraints, dependencies, and ambiguities.
2. Inspect relevant project architecture, modules, files, dependencies, conventions, and reusable functionality. Avoid unrelated exploration.
3. Determine a technical approach and its rationale.
4. Identify expected files and components to create, modify, or remove.
5. Break work into ordered tasks with dependencies and expected outcomes.
6. Define verification strategy, including appropriate test levels, scenarios, edge cases, and regression checks.
7. Identify risks, assumptions, dependencies, and decisions requiring human input.

Boundaries:
- Does not write application code.
- Does not implement tests or execute verification.
- Does not claim implementation is complete or tests pass.
- Does not change approved requirements or scope.

**Output:** plan.md, describing intended work rather than claiming work has already occurred.

### 5.5 Plan Review

**Purpose:** Independently evaluate a proposed plan before implementation.

Inputs: intent when applicable, approved specification, and plan.

- Review requirement coverage, technical soundness, codebase grounding, task order, risks, assumptions, dependencies, and verification strategy.
- Identify findings with severity, location or reference, explanation, evidence where possible, and recommended correction.
- Distinguish confirmed defects or gaps from optional suggestions.
- Operate read-only; report findings rather than modifying the plan.
- Reuse stable finding IDs across review rounds.

**Output:** plan-review report generated from the shared review template.

### 5.6 Implementation

**Purpose:** Execute the approved specification and plan while maintaining engineering quality and adapting responsibly to discoveries.

Inputs: approved specification and human-approved plan. Optional inputs include intent, project instructions, documentation, source code, and test suites.

Responsibilities:
1. Understand approved requirements, plan, and project instructions.
2. Inspect the current project state before making changes. Confirm planned files, components, dependencies, architecture, and technical assumptions.
3. Identify outdated instructions, changed constraints, or differences between the plan and current reality.
4. Implement application code and create, update, or remove appropriate automated tests.
5. Follow established project practices and keep changes focused.
6. Apply Adaptive Planning when technical discoveries justify a change within approved boundaries.
7. Update plan.md when material technical changes occur. Update spec.md only when justified to clarify technical details or constraints without silently changing expected behavior.
8. Record significant discoveries, deviations, rationale, and impact.
9. Run relevant tests and checks, investigate failures, and verify acceptance criteria.
10. Report changed files, behavior, deviations, verification results, unresolved issues, and review-relevant context.

Boundaries:
- No independent business requirement or acceptance-criteria changes.
- No silent scope changes or discarding of business, security, regulatory, or data-integrity constraints.
- No self-approval, PR authorization, or merging.
- No false claims about tests or completion.

**Output:** application changes, tests, justified artifact updates, and an implementation summary.

### 5.7 Code Review

**Purpose:** Independently assess actual code changes for correctness, security, maintainability, regressions, and alignment with available requirements and plans.

Inputs: actual diff or PR; intent, specification, and plan when available.

- Review the actual implementation, not intended changes described in a plan.
- Use the specification as the source of expected behavior.
- Compare against the approved plan when available.
- A standalone review with only a diff can assess code-level concerns; without requirements it must not claim full requirement coverage.
- Identify findings with severity, file/line location, explanation, evidence or reproduction where possible, and recommended correction.
- Distinguish confirmed defects from suggestions.
- Operate read-only; report findings rather than changing code.
- Reuse stable finding IDs across rounds.

**Output:** code-review report generated from the shared review template.

## 6. Artifacts and templates

### 6.1 Canonical templates

M1 provides five templates: (product-breakdown is initiative-level; the others are work-item or review templates).

| Template | Purpose |
|---|---|
| templates/intent.md | Problem, affected users, desired outcome, context, constraints, assumptions, open questions, owner confirmation |
| templates/product-breakdown.md | Initiative outcomes, capabilities, candidate epics/work items, dependencies, proposed increments, prioritization rationale, assumptions, owner decisions |
| templates/spec.md | Scope, requirements, acceptance criteria, edge cases, security/data considerations, dependencies, assumptions, approval |
| templates/plan.md | Objective, requirements references, codebase findings, technical approach, expected changes, ordered tasks, verification, risks, decisions |
| templates/review.md | Review rounds, findings, severity, evidence, recommendations, statuses, outcomes, and resolution history |

Templates are starting structures, not mandatory paperwork. Omit irrelevant sections and adapt them to the project while retaining essential information.

### 6.2 Artifact location

Default work-item artifact location:

    docs/initiatives/<initiative-id>/
    ├── intent.md
    └── product-breakdown.md

Selected work items use the project's work-item convention, defaulting to:

    docs/tickets/<work-item-id>/

Example:

    docs/tickets/feature-123/
    ├── spec.md
    ├── plan.md
    └── reviews/
        ├── plan-review.md
        └── code-review.md

An existing project convention takes precedence. The framework must not force docs/tickets/ when the project already has an equivalent, established location.

If no ticket or work-item identifier exists, use a stable descriptive slug.

At the beginning of a workflow, determine the artifact directory and pass its explicit path to each skill. Standalone skills must accept an existing artifact path and must not create duplicate directories.

### 6.3 Commit policy

- Commit initiative-level intent.md and product-breakdown.md when applicable, and work-item spec.md and plan.md by default.
- Review reports are local-only by default. Commit them when auditability, team policy, or the project requires it.
- Retain work-item artifacts after PR merge as engineering history.
- Do not commit secrets, temporary files, or unrelated generated artifacts.

## 7. Workflow applicability and orchestration

### 7.1 Full Idea-to-PR workflow

The default flow for a new idea or feature is:

1. Intent — optional when equivalent context already exists; for a vague idea, use it to clarify the problem, context, and desired outcomes.
2. Product Breakdown — use when the input represents a broad initiative or product rather than one implementable deliverable. It may be skipped for already-scoped work.
3. Owner review and approval of the proposed product breakdown and selection of the next work item or increment.
4. Specification — define and self-validate expected behavior for the selected work item.
5. Human resolution and approval of important requirements.
6. Planning.
7. Fresh-session Plan Review.
8. Bounded automated plan review/fix loop.
9. Human plan approval.
10. Implementation.
11. Adaptive Planning as needed during implementation.
12. Automated verification.
13. Fresh-session Code Review.
14. Bounded automated code review/fix loop, with relevant checks rerun after fixes.
15. Human verification of the diff and manual/local behavior where appropriate.
16. Human authorization to prepare and open the PR.

The workflow coordinates skills and gates. It should not duplicate their detailed instructions.

### 7.2 Flexible entry points

Do not force the full workflow when equivalent information or artifacts already exist.

Examples:
- Vague or early-stage business/product idea: use Intent to clarify the problem or opportunity, then Product Breakdown to shape a broad initiative into candidate increments; select one and proceed to Specification.
- Broad, already-articulated product initiative: Product Breakdown can start from the existing brief or requirements without creating a duplicate Intent.
- Existing backlog or product: invoke Product Breakdown independently to review or restructure it; preserve owner-approved commitments and distinguish proposed changes.
- More developed idea without a ticket: use Intent to refine the context if needed, then Specification, Planning, and subsequent stages.
- Existing complete ticket: start at Specification or Planning as appropriate.
- Clear, small bug with reproduction: start at Planning or Implementation depending on complexity.
- Another developer's PR: invoke Code Review independently.
- Technical investigation: invoke a standalone investigation activity and proceed to Planning only if implementation is needed.
- Small maintenance task: use only the relevant standalone skills.

At the start, determine available artifacts, project context, and current stage. Reuse existing information and avoid duplicate artifacts.

### 7.3 Human approval gates

M1 requires explicit human approval at consequential decision points:
- Confirm intent when the optional Intent stage is used.
- Review and approve the product breakdown and select the next increment when Product Breakdown is used.
- Approve requirements/specification before planning proceeds.
- Approve the implementation plan before implementation begins.
- Resolve business decisions or changes to scope, expected behavior, or acceptance criteria.
- Verify the implemented diff and relevant manual behavior before PR preparation.
- Authorize PR creation.

An agent must not infer approval from silence or from approval of an earlier stage. No automatic merge is allowed.

## 8. Review process and bounded loops

Plan Review and Code Review are separate skills but use the same templates/review-report structure.

### 8.1 Review independence

- Start each review round in a fresh agent session by default.
- The same agent/model may be used initially; a different model is not required for M1.
- Reviewers are read-only and report findings.
- The planning or implementation session addresses accepted findings.
- Reviewers validate corrections in a subsequent round.

### 8.2 Findings and report history

Each finding should include:
- Stable ID.
- Severity.
- File/line or artifact reference.
- Explanation and evidence.
- Recommended correction.
- Status and resolution rationale.

Maintain one consolidated report per review activity. Record round history and retain finding IDs; do not create a new report file for every round.

Possible outcomes:
- Approved.
- Changes Requested.
- Blocked.

### 8.3 Review thresholds and limits

Initial default maximum: three rounds per review activity. This is a safety cap, not a target.

- Plan Review approval threshold: no blocking or major findings.
- Code Review approval threshold: no blocking findings.
- Minor findings and suggestions remain visible for human judgment.
- If the maximum is reached with unresolved blocking or major findings, stop and escalate to a human.
- Do not mark a review approved while its applicable blocking threshold is unmet.

Human approval remains separate from an agent's review outcome.

### 8.4 Review execution strategy

The framework owns the Code Review process, criteria, finding lifecycle, review-round limits, and approval thresholds. The coding-agent adapter selects the review execution mechanism.

Use this preference order:
1. **Native review capability:** Prefer a suitable native review feature provided by the coding agent (for example, Codex `/review` or a Claude Code review capability), when it can satisfy the framework's review requirements.
2. **Dedicated reviewer agent:** If no suitable native capability is available, use a dedicated reviewer agent or subagent with read-only access where the platform supports it.
3. **Framework-defined procedure:** If neither option is available, use the framework's structured review procedure. Prefer a fresh review context. If the platform cannot provide meaningful separation from the implementation context, disclose that limitation rather than claiming independent review.

Native review features are execution mechanisms, not replacements for the framework's Code Review skill or its rules. Review findings must still be evaluated, validated where practical, normalized into the shared report format, and processed through the framework's bounded review lifecycle. A native or separate reviewer is not automatically correct; do not accept findings without assessment.

## 9. Adaptive Planning and escalation

An approved plan is a baseline, not immutable. During implementation, technical decisions may be revised when actual project discoveries justify an adjustment, provided approved requirements, constraints, and scope are preserved.

### 9.1 Agent may adapt autonomously

Examples include:
- A planned file or component differs from the current codebase.
- A technical assumption is disproved.
- A library or framework does not support the assumed capability.
- A more suitable established technical approach is needed without changing expected behavior.

The agent must record the discovery, original approach, adjustment, rationale, and impact in plan.md and continue when the adjustment is within approved boundaries.

### 9.2 Human approval or escalation required

Stop and ask when a proposed change affects:
- Business behavior or decisions.
- Requirements or acceptance criteria.
- Scope or user-visible outcomes.
- Important business or operational constraints.
- Security, regulatory, or data-integrity boundaries.
- Significant architectural decisions that require human ownership or authorization.

Technical clarification that does not change expected behavior may be documented and handled by the agent. Do not use a technical clarification to silently change product behavior.

A targeted plan review may be appropriate for a significant technical adjustment. A full plan review is not automatically required for every minor technical adaptation.

The latest approved specification and the plan with documented, authorized adaptations are the baseline for final Code Review.

## 10. Codex adapter

### 10.1 Adapter principles

Codex is the first supported coding-agent adapter. Its exact skill-discovery and instruction requirements must be verified against the current Codex environment and documentation before the adapter is considered validated.

Use Codex's native skill, repository-instruction, and review mechanisms where suitable. In particular, prefer Codex's native code-review capability (such as `/review`) for review execution when it is available and compatible with the framework's review requirements. Keep Codex-specific commands, syntax, and conventions in adapters/codex/ and avoid leaking them into the framework core.

The framework's Code Review skill remains responsible for the review process, inputs, criteria, finding format and lifecycle, review rounds, and outcome rules. The adapter selects the strongest suitable execution mechanism supported by the coding agent.

### 10.2 Installed skill layout

The intended Codex installation location is:

    .agents/
    └── skills/
        ├── intent/
        │   └── SKILL.md
        ├── product-breakdown/
        │   └── SKILL.md
        ├── specification/
        │   └── SKILL.md
        ├── planning/
        │   └── SKILL.md
        ├── plan-review/
        │   └── SKILL.md
        ├── implementation/
        │   └── SKILL.md
        └── code-review/
            └── SKILL.md

The canonical source skill definitions live under skills/ in the framework repository. The adapter may copy or transform them as required by verified Codex conventions. Do not assume compatibility details without testing.

### 10.3 Installed shared resources

The intended shared resource layout is:

    .agentic-sdlc/
    ├── VERSION
    ├── manifest.json
    ├── principles/
    │   └── engineering-principles.md
    ├── workflows/
    │   └── idea-to-pr.md
    └── templates/
        ├── intent.md
        ├── product-breakdown.md
        ├── spec.md
        ├── plan.md
        └── review.md

### 10.4 AGENTS.md integration

The adapter provides adapters/codex/AGENTS.md.template. The installer adds its content as a clearly marked, framework-managed section in the target project's AGENTS.md.

The section should:
- Identify the framework and installed resource locations.
- Tell Codex how to determine the appropriate workflow stage or standalone skill.
- Point to workflow, templates, principles, and skills without duplicating their detailed instructions.
- Reinforce approval gates and boundaries.
- Explain the default artifact location and that existing project conventions take precedence.

Use explicit markers:

    <!-- BEGIN AGENTIC-SDLC MANAGED SECTION -->
    ...
    <!-- END AGENTIC-SDLC MANAGED SECTION -->

Never replace the entire project AGENTS.md. Preserve all content outside the managed section. If the managed section has been locally modified, detect and report the conflict rather than silently overwriting it.

AGENTS.md is a project instruction source, not unquestionable truth. Apply the conflict-handling policy in Section 4.9.

A future Claude Code adapter may use CLAUDE.md and its native skill conventions, but it is outside M1.

## 11. Source repository structure

The intended source repository structure is:

    agentic-sdlc-framework/
    ├── README.md
    ├── M1-BLUEPRINT.md
    ├── VERSION
    ├── LICENSE
    ├── PROVENANCE.md
    ├── .agentic-sdlc/
    │   └── principles/
    │       └── engineering-principles.md
    ├── workflows/
    │   └── idea-to-pr.md
    ├── skills/
    │   ├── intent/
    │   │   └── SKILL.md
    │   ├── product-breakdown/
    │   │   └── SKILL.md
    │   ├── specification/
    │   │   └── SKILL.md
    │   ├── planning/
    │   │   └── SKILL.md
    │   ├── plan-review/
    │   │   └── SKILL.md
    │   ├── implementation/
    │   │   └── SKILL.md
    │   └── code-review/
    │       └── SKILL.md
    ├── templates/
    │   ├── intent.md
    │   ├── product-breakdown.md
    │   ├── spec.md
    │   ├── plan.md
    │   └── review.md
    ├── adapters/
    │   └── codex/
    │       ├── README.md
    │       └── AGENTS.md.template
    ├── scripts/
    │   └── install.py
    └── tests/
        ├── installer/
        │   ├── fixtures/
        │   └── test_*.py
        ├── regression/
        │   ├── README.md
        │   └── *.md
        └── integration/
            ├── README.md
            └── codex-validation.md

This is the intended M1 structure, not a claim that every listed file already exists.

### 11.1 Root README

The root README introduces the framework to users and contributors. It should explain the problem, goals, M1 scope, high-level architecture, skills, workflow, installation, supported adapters, limitations, and contribution approach.

It should remain an entry point rather than duplicating the full blueprint or every skill instruction.

### 11.2 License and attribution

The repository is intended to be distributed under the **Apache License, Version 2.0**, subject to confirming that the project maintainer has the necessary rights to license the material included in the repository.

- The root `LICENSE` file contains the complete Apache License 2.0 text without a project-specific blanket copyright notice.
- The root README identifies Apache-2.0 as the intended project license and links to the root LICENSE file.
- The README identifies the project creator and maintainer and transparently discloses AI assistance.
- Do not make a blanket claim that every part of the repository is exclusively human-authored or copyrightable by the project maintainer.
- Preserve applicable third-party copyright and license notices. Do not include employer-owned, confidential, or otherwise unlicensed material in the repository.
- Contributions from other people remain subject to the project's contribution terms and the applicable license.

Project attribution describes the maintainer's role; it is not a legal determination of copyright ownership over every element. Confirm licensing rights before distributing or relying on the license commercially.

The root `PROVENANCE.md` records material external influences and identifiable third-party material incorporated into the repository. Keep it concise and update it when such material or influence is added. It is not necessary to cite generic engineering knowledge or every routine reference consulted during development.

### 11.2 Codex adapter README

adapters/codex/README.md explains Codex-specific integration: native skill discovery, project instruction integration, adapter-specific compatibility requirements, installed files, installation/update behavior, limitations, and validation.

### 11.3 Blueprint maintenance

This blueprint is a living architectural reference. Update it when meaningful architectural decisions, scope, intended behavior, or implementation status changes. Do not update it for every routine code change.

Clearly distinguish approved design from implemented and validated behavior. When implementation intentionally diverges, record the reason and update the blueprint when the intended architecture changes.

## 12. Installer and installation model

### 12.1 Installation model

Clone the framework repository alongside the application repository. Run the installer from the framework clone, targeting the application repository.

Example workspace:

    workspace/
    ├── agentic-sdlc-framework/
    └── sample-app/

Example command:

    cd agentic-sdlc-framework
    python scripts/install.py --target ../sample-app --adapter codex

Installation is copy-based. The application receives a self-contained copy of required runtime resources and does not depend on the framework clone after installation.

Keep the framework clone as the development and distribution workspace for maintaining the framework, running its tests, creating releases, and updating installations. It can technically be deleted after installation, but must be cloned again to develop or update the framework.

### 12.2 Installer responsibilities

The installer:
- Validates the target and selected adapter.
- Copies the seven skills into .agents/skills/.
- Copies principles, workflow, and templates (including product-breakdown.md) into .agentic-sdlc/.
- Writes installed version information.
- Generates and maintains a manifest of framework-managed files and integrity information.
- Safely adds or updates the managed section in AGENTS.md.
- Creates the default artifact directory only when needed and when the project has no established equivalent.
- Reports actions, conflicts, and errors clearly.

The installer must use Python's standard library only for M1. It should be dependency-free and designed for supported development environments.

### 12.3 Installer non-responsibilities

The installer does not:
- Run Codex or another AI agent.
- Execute a workflow or invoke skills.
- Generate project specifications, plans, or application code.
- Run application tests or perform code reviews.
- Make business or architectural decisions.
- Approve work, open PRs, merge, or deploy.
- Create a nested Git repository in the application.

### 12.4 Idempotency and preservation

Repeated installation must not duplicate files or managed instruction sections.

Preserve project-owned files and all AGENTS.md content outside the managed section.

For framework-managed files:
- Unmodified installed files may be updated automatically.
- Locally modified managed files must be preserved and reported as conflicts.
- New upstream files may be installed.
- Removed upstream files must be reported, not automatically deleted.
- Do not silently overwrite local customizations.
- Provide incoming upstream versions for comparison when conflicts occur.
- M1 does not require an automatic three-way merge engine; a human resolves conflicts.

If the managed AGENTS.md section has been locally modified, preserve it and report the conflict. Do not overwrite it silently.

### 12.5 Update command

Update the framework clone to the intended version, then run the installer in update mode:

    python scripts/install.py --target ../sample-app --adapter codex --update

The installer uses the checked-out framework version. It must not silently fetch or install the latest version. Updates are intentional and controlled.

### 12.6 Manifest and integrity

The manifest records the installed framework version and the framework-managed file inventory with sufficient integrity metadata to distinguish unmodified files from local modifications.

Exact manifest schema and checksum mechanics are implementation details to finalize during installer design. They must support safe update/conflict behavior and must not claim ownership of project files outside the managed integration section.

## 13. Versioning and releases

Use versioned Git tags for framework releases, for example v0.1.0, v0.2.0, and v0.3.0.

The source VERSION file identifies the framework version being developed or released. The installed .agentic-sdlc/VERSION records the version copied into an application.

An application may remain on an earlier framework version while another application uses a newer one. Do not automatically update installed applications when a new framework release is published.

A release should be created only after the relevant framework tests and Codex integration validation have been completed and results recorded. Exact release automation is outside M1 unless needed for the basic process.

## 14. Testing and validation

Framework tests and application tests are separate.

- Framework tests validate the framework repository and its installer, resources, and agent behavior.
- Application tests validate the target application's code during normal implementation.

The framework's development tests stay in the framework repository. They are not copied into installed applications.

### 14.1 Installer tests

Automated tests for scripts/install.py should use Python's standard unittest library and test at least:
- Fresh installation.
- Installation into a project with an existing AGENTS.md.
- Installation when AGENTS.md does not exist.
- Repeated installation and idempotency.
- Preservation of project instructions outside the managed block.
- Detection and preservation of a locally modified managed AGENTS.md section.
- Update of unmodified managed files.
- Detection and preservation of modified managed files.
- Installation of new upstream files.
- Reporting of removed upstream files without automatic deletion.
- Existing project documentation conventions.
- Invalid or unsafe target handling.

Use fixtures representing empty projects, projects with existing instructions, locally customized instructions, and existing documentation conventions.

### 14.2 Regression scenarios

Regression scenarios are documented agent-behavior tests. They initially remain manual rather than requiring a complex automated evaluation platform.

Scenarios should include:
- Ambiguous business requirements.
- Outdated or contradictory project instructions.
- A technical assumption disproved during implementation.
- A proposed scope or business behavior change.
- A review finding that is not a real defect.
- Unresolved blocking findings after the maximum review rounds.
- Existing artifacts that make one or more workflow stages unnecessary.
- Standalone skill invocation with incomplete optional context.
- Vague initiative clarified into intent, then progressively decomposed into candidate capabilities and a selected first increment.
- Product Breakdown invoked from an existing brief or backlog without requiring a new intent artifact.
- Small, already-scoped work item bypasses Product Breakdown.
- Owner rejects or reprioritizes proposed work, and the agent preserves the decision without silently generating an approved backlog.

Each scenario defines minimum input/context, expected behavior, failure signals, and relevant workflow or skill.

When an agent failure occurs, capture a minimal reproducible scenario, diagnose the root cause, update the smallest appropriate instruction or workflow source, and rerun the new and relevant existing scenarios.

### 14.3 Codex integration validation

Validate the installed framework in a real sample application using Codex.

At minimum:
1. Install the framework into a sample application.
2. Confirm Codex discovers all seven installed skills using verified native conventions.
3. Invoke each skill independently.
4. Exercise the Idea-to-PR workflow with a representative task, including a broad initiative that requires decomposition and a scoped task that skips it.
5. Verify artifact paths and template references.
6. Verify human approval gates, including owner approval of product breakdown decisions.
7. Exercise plan review and code review loops, including bounded stopping behavior.
8. Exercise Adaptive Planning and escalation behavior.
9. Verify that project instructions and framework principles are interpreted according to the conflict policy.
10. Test installer update and local customization conflict handling.
11. Record actual commands, outcomes, limitations, and any deviations.

A syntactically valid skill or successful file copy is not proof that Codex can use the framework correctly.

### 14.4 When tests run

| Event | Validation |
|---|---|
| Installer development/change | Run relevant automated installer tests |
| Skill change | Run relevant regression scenarios |
| Workflow change | Run relevant workflow regression scenarios |
| Codex adapter change | Run Codex integration validation |
| Release candidate | Run the full automated installer suite, relevant regression scenarios, and end-to-end Codex validation |
| Application installation | Run installation smoke checks |
| Application update | Run update smoke checks and resolve/report conflicts |
| Normal application implementation | Run the application's own relevant tests and checks |

Framework development tests are not limited to installation or update events. They run throughout framework development and before releases.

## 15. M1 completion criteria

M1 is complete only when all of the following are satisfied:

### Framework core
- [ ] Shared engineering principles are documented and referenced consistently.
- [ ] All seven standalone skills have defined inputs, outputs, boundaries, and behavior.
- [ ] Five canonical templates exist: intent, product-breakdown, spec, plan, and review.
- [ ] Product Breakdown supports progressive decomposition of broad initiatives and can be skipped for already-scoped work.
- [ ] Idea-to-PR workflow supports idea-driven and task-driven entry points.
- [ ] Workflow can skip stages when equivalent approved information exists.
- [ ] Human approval gates and stop/escalation rules are explicit.
- [ ] Plan Review and Code Review use bounded loops and stable finding IDs.
- [ ] Adaptive Planning rules are explicit and traceable.

### Codex adapter and installation
- [ ] Current Codex skill-discovery and instruction conventions have been verified.
- [ ] Codex adapter instructions and AGENTS.md template exist.
- [ ] Installer supports fresh installation and safe updates.
- [ ] Installer preserves project-owned instructions and local modifications.
- [ ] Manifest and version tracking support conflict detection.
- [ ] Installer is idempotent and uses only the Python standard library.

### Validation
- [ ] Automated installer tests pass.
- [ ] Relevant regression scenarios have been exercised.
- [ ] End-to-end Codex validation has been completed in a sample application.
- [ ] Validation results and limitations are documented.
- [ ] No unresolved critical issue prevents the intended M1 workflow from operating safely.

Do not mark a criterion complete based only on planned behavior. Record evidence from actual implementation and validation.

## 16. Deferred decisions and future work

The following remain outside M1 or require later evidence:
- A dedicated product-discovery and business-validation capability beyond the initial guided discovery supported by the Intent skill. Product Breakdown may identify evidence gaps but does not perform market validation.
- Advanced product portfolio management, roadmap governance, quantitative prioritization frameworks, and automated backlog synchronization with external project-management tools.
- Claude Code adapter and CLAUDE.md integration.
- Additional coding-agent adapters.
- Automated evaluation infrastructure for regression scenarios.
- Automated release pipelines.
- Advanced manifest migration or automatic three-way merge.
- PR-to-deployment workflow, production feedback, and controlled autonomous operation.
- Broader multi-project validation.

Implementation details that depend on current Codex behavior must be verified during adapter development rather than assumed from this blueprint.

---

## Change history

| Date | Change |
|---|---|
| 2026-11-01 | Initial consolidated M1 architecture and implementation blueprint based on agreed design decisions. |
| 2026-11-02 | Clarified native review execution strategy, specified Apache-2.0 licensing, and generalized sample application references. |
| 2026-11-02 | Expanded Intent to support guided discovery from vague ideas, distinguished discovery from market validation, and deferred product backlog decomposition beyond M1. |
| 2026-11-03 | Added Product Decomposition to M1 as an optional, standalone, progressive initiative-level capability; defined product-breakdown artifact, workflow handoff, approval, installation, and validation implications. |
| 2026-11-04 | Added project-wide originality, provenance, and quality principles; introduced a concise provenance record for material external influences and third-party material. |
| 2026-11-06 | Clarified the M1 workflow's conditional Product Decomposition, separate bounded review activities, approval gates, and flexible entry points; corrected the Codex skill-discovery checklist. |
