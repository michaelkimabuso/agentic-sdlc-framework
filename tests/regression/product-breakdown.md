# Regression: Progressive Product Breakdown

## Input
An owner provides an articulated initiative brief and a small existing backlog for a scheduling product. The brief already describes users and desired outcomes, but several candidate capabilities and dependencies are unclear. Ask for a product breakdown and next increment.

## Expected behavior
The skill uses the brief and backlog directly without requiring Intent or repeating discovery. It progressively identifies useful capabilities, candidate deliverables/work items, dependencies, plausible increments, uncertainties, and a proposed next increment in `<initiative-artifact-directory>/product-breakdown.md` based on `templates/product-breakdown.md`. It refines only the likely next increment enough for specification, leaving future work at a useful level. It distinguishes knowns and assumptions and explains prioritization as rationale, not validated market research. It obtains explicit owner approval of the breakdown and explicit selection and scope of the next increment.

## Failure signal
The skill requires an unnecessary Intent artifact, generates an exhaustive backlog or implementation plan, hides assumptions/dependencies, implies validated demand, or proceeds without owner approval and explicit next-increment selection.

## Relevant workflow/instructions
- `skills/product-breakdown/SKILL.md`
- `workflows/idea-to-pr.md`: Product Breakdown and human approval gates
- `templates/product-breakdown.md`
- `.agentic-sdlc/principles/engineering-principles.md`
