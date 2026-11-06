# Additional skills: validation scope

Date: 2026-11-06.

Applies to `production-ui`, `safe-state-changes`, `reliable-effects`, `evidence-based-verification` and `issue-readiness`.

## Completed checks

- All five passed the skill creator's `quick_validate.py`; local reference targets and UI metadata were checked.
- One fresh, read-only review requested `gpt-6-luna` with high reasoning. It read all five skills and the production UI reference, found no blocker and recommended making mutation verification cases conditional on actual risk. That recommendation was applied before installation.
- The review reasoned through three contrast groups: visual-only copy versus a scoped growing picker with late responses; committed writes with failed refresh versus unknown external acceptance; and accepted human decisions versus stale automated summaries during a paused programme.
- Installation/export verification compares actual file bytes. Existing `robust-architecture` evaluation inputs and skill content are preserved.

## What this establishes

These checks establish valid structure and a reviewed, proportionate procedure with useful scope boundaries. The scenario review was a written reasoning check; no application was built or executed for it. There is no paired benchmark, quantified efficacy score or claim that these five skills prevent every defect. Runtime behavior and suitability for a particular project require that project's own evidence.

The existing `robust-architecture` evaluation record is separate. Private-project source, raw model traces and customer data are not published here. Model IDs above are the requested identifiers; local CLI metadata warnings do not independently certify a backend model version.
