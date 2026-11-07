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

## Authorization and set integration: 1.2.0

- Added a self-contained authorization procedure and conditional pointers from the other seven skills. All eight passed the skill validator and repository-relative link checks. Claude Code strict manifest/catalog validation and native Codex discovery exposed eight skills at version 1.2.0.
- One fresh read-only reviewer requested `gpt-6-luna` with max reasoning followed the set on three scenarios: proposed reservation routes with an accepted access policy; accepted invoice delivery and public-link rules after a manager loses their role; and a copy-only UI edit.
- It identified source-level owner/scope/field/bulk/file issues, preserved valid committed delivery separately from current portal access, and kept the copy edit local. This was a static response simulation on synthetic artifacts; no application or attack was executed.
- The review found that mutation and delivery pointers were too narrowly worded around new/changed code. Those were widened for reviews/plans; the architecture and issue-readiness pointers were aligned as well. Root checked the corrected conditions without a further model round.
- Original skill content is preserved outside the seven small routing paragraphs. Historical evaluation inputs/results remain byte-identical; their scores do not evaluate the new authorization routing. Optional sibling pointers require the sibling only when it is installed, preserving standalone use.

These instructions guide a model. They do not enforce application permissions or establish that a project is secure. No efficacy benchmark or real-project security audit was performed for this release.

## Agentic Engineering Kit / agentic-bootstrap: 1.3.0

- Added the project-entry workflow, conditional new/existing/instruction/spec guides and optional artifact templates. The display name is now Agentic Engineering Kit; repository and plugin identifiers remain unchanged. Existing eight skill trees and historical evaluation artifacts are byte-identical to 1.2.0.
- All nine skills passed structural validation. Internal guide/template links resolve. Claude strict manifest/catalog validation and both native plugin inventories discovered nine skills at 1.3.0, including the new display metadata.
- Two independent evaluators were requested: gpt-6-luna/max for new-project documentation plus two response-only boundary probes, and gpt-6.1-terra/high for scoped existing-project documentation and a tracker-draft probe. Actual artifacts were written only in two synthetic repositories; original input bytes were preserved, written links resolved and emitted template tokens were absent.
- The initial new-project pilot failed proportionality: it created a mandatory maintainer gate for routine runtime/storage choices. The responsible entry/spec guidance was clarified and only that pilot reran on a fresh equivalent fixture. The final artifact kept routine technical selection inside implementation and contained edge assumptions explicitly. Initial failed artifacts were retained locally.
- Five final routing outcomes passed root inspection: new-project artifacts; an ordinary copy edit that skips bootstrap; unresolved medical-note permissions; scoped onboarding preserving current owners/root rules; and draft-only tracker reconciliation preserving delivered work and a programme hold.

These are bounded artifact/routing checks, not an A/B efficacy benchmark. Fixture application code, live products, live tracker state and actual project-instruction loading inside Codex/Claude sessions were not executed. Native plugin discovery proves package loading, not generated-project runtime behavior or complete instruction compliance.

## Change delivery and request-identity proof: 1.4.0

Date: 2026-11-07.

- Added `change-delivery`, bootstrap routing/handoff integration, decision-record guidance and a conditional request-identity proof reference. Strengthened the mutation verification handoff without changing historical architecture evaluation artifacts.
- All ten skills passed structural validation. Local links and shared manifest metadata were checked. Native Claude and Codex plugin loaders discovered ten skills at 1.4.0; Claude strict manifest/catalog validation passed. Its optional directory listing still warns about the missing icon. A real local-source skills CLI install of change-delivery into a fresh temporary project matched both agents' source bytes.
- An independent read-only review requested gpt-6.1-terra/high found two material problems in the first draft: standalone delivery delegated identity proof without a fallback, and a coupled-write race instruction imposed one winner on independent compatible commands. Both were corrected and the reviewer checked those corrections. A response-only standalone probe covered request replay/conflict/overlap, two independent additive commands and an unavailable independent-review gate; it did not execute an application.
- One fresh implementer requested gpt-6-luna/max used the explicitly selected skill on a synthetic Python/SQLite resend workflow. Three behavioral regressions failed before the fix; all four fixture tests passed afterward and on the author's rerun. Disabling the acceptance guard in a temporary copy reproduced the three failures. Tests covered prepared overlapping executions after queue/send/failure progress, unchanged recipients, conflicting intent and a valid fresh-key confirmation. Two short response-only probes kept a static copy edit local and respected a repository's existing workflow/reviewer.
- That implementation pilot used the frozen first candidate, before the two narrow review corrections; the final corrections received the separate reread/standalone probe above. The fixture used deterministic public prepare/commit phases on one SQLite connection and simulated downstream delivery, not a live provider or multi-process database race. Its three new regression tests were prepared together, so this was not a strict one-test-per-cycle TDD demonstration. As instructed by the fixture's available capabilities, the implementer reported its independent-review gate unmet rather than claiming review occurred.

These checks do not establish comparative efficacy, automatic selection from the full skill catalog or production defect reduction. External TDD libraries are optional and were not bundled or re-evaluated. Project-specific delivery instructions and release authority remain authoritative.
