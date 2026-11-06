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

## Plugin packaging

The 1.0.0 package uses one shared `skills/` tree, a portable root manifest for Codex, a Claude Code manifest and a marketplace catalog for each host.

- Claude Code strict manifest and marketplace validation passed without manifest warnings. Its local `--plugin-dir` component inventory discovered all six skills.
- Codex native app-server `plugin/list` and `plugin/read` discovered the marketplace, parsed the portable manifest and exposed all six namespaced skills, with no marketplace load errors. These were read-only packaging checks; no model task or plugin installation was performed.
- `npx skills add <local-repository> --list` discovered exactly six skills. A subsequent real install from the public `pkasarda/skills` repository into a fresh temporary project succeeded for both `claude-code` and `codex`; all six installed skill bodies and supporting reference/UI metadata matched the source bytes. Anonymous GitHub API access confirmed public visibility.
- Shared manifest identity/version, local marketplace paths and unchanged skill-file hashes were checked.
- A pattern scan of all 149 historical Git blobs found no credential-pattern, personal-home-path or private-project-reference matches before the public visibility change. This is a bounded check, not a complete security audit.

Public-directory submission was not performed. The initial 1.0.0 directory-submission checks flagged a missing license and icon, separately from successful plugin validation. At the author's request, 1.0.1 adds the MIT license and declares it in both manifests; no icon or directory submission was added.

## Product discovery: 1.1.0

- The new skill passed `quick_validate.py`. Both native plugin loaders discovered all seven skills at package version 1.1.0; Claude's strict manifest and marketplace validation also passed.
- One fresh reviewer requested `gpt-6-luna` with max reasoning applied the skill to three independent scenario descriptions: an unspecified reservation-system idea; a sufficiently specified local prototype with an explicit build request; and a proposed portal in a synthetic CRM that already had order tracking.
- Its simulated next responses asked consequential questions for the unclear idea, proceeded toward the specified prototype with explicit working assumptions, and inspected existing capabilities before suggesting further portal work. The reviewer reported no material skill defect. These were response simulations, not implemented applications, user interviews or live product experiments; there was no A/B benchmark.
- Existing six-skill content was preserved byte for byte. The new skill is self-contained and does not require the other skills to be installed.
