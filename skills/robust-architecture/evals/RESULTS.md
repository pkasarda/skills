# Evaluation record — 2026-11-06

Installed candidate: **v2**. No universal correctness guarantee is claimed.

## What was tested

Responders: `gpt-6-luna`, high reasoning. Semantic judge: `gpt-6.1-terra`, high reasoning. Proposals were at most250 words for structured cases and350 for discovery. Source/candidate hashes, raw proposals, criteria, blinded labels and judgments are retained here. Condition labels were withheld from the judge; this was procedural blinding, not an access-controlled security boundary.

The first ten tasks were precise: they supplied the important constraints and often named the reported symptom. These test decision quality given context. They do not establish that an agent can discover the right context in a large unfamiliar project.

## Measured runs

| Run | Without skill | With skill | Critical criteria | Interpretation |
|---|---:|---:|---|---|
| Structured v1,10 cases,20 fresh contexts |37/40|40/40|18/18 both|Small improvement in completeness on this fixed sample; not proof of general superiority.|
| Discovery v1,2 miniature repos |6/8|7/8|4/4 without;3/4 with|The skill-assisted proposal had a critical stale-cache publication gap despite a higher total. V1 was not accepted on the structured score alone.|
| V2 targeted regression/transfer,3 tasks |No new paired baseline|10/12|8/8|The observed critical gap was corrected in the proposal. This is not a complete rerun of the paired v1 suite.|

Structured differences were retention/replay lifetime, resource-close error contract, and explicit incomplete-export recovery. The judge additionally flagged an unsupported deterministic-export assumption in a baseline proposal; the numeric result was not retroactively changed after unblinding.

Discovery D01 used fresh contexts. D02 used short, previously completed same-condition contexts after the harness reached its thread cap. Both began with the same vague request to inspect the project. The repositories scattered relevant facts across entrypoints, source, accepted contracts, stale notes and happy-path tests. Responders ran local tests/probes and found reachable defects rather than receiving a named bug. These are still small synthetic repositories, not production samples.

The decisive v1 failure was D02: the proposed generation check ran in the panel callback, after the refresh code had already written the cache. Account-scoped keys did not protect a new lifetime under the same account. V2 now requires tracing every observable publication and checking applicability at each relevant boundary, while preserving legitimate committed business effects.

V2 retested D02, preserved external-payment reasoning in C08, and used a newly independently designed non-UI D03 repository. D03 requires preserving valid historical scan results while guarding current clearance and release notices. Targeted runs used resumed same-condition contexts and hidden version labels. V2 passed all8 critical checks. Two noncritical omissions remain: an explicit valid-current-feed control in D02, and concurrent-order/scanner-cancellation-limit verification in D03. They remain visible in `revision2/results/aggregate.json`; v2 is not described as12/12.

## Retained experimental failures

An earlier batched exploratory run mixed case identities in several baseline answers. Its scores were excluded from the primary comparison. `answers/A-main.json`, `answers/B-main.json` and `results/exploratory-grades.json` preserve it. The confirmatory structured run gave every case/condition a separate fresh context.

The judge flagged two over-specific rubric items (C01.4 and C04.3). They were clarified before isolated predictions; original criteria and the change note remain in `operator/`. Critical criteria and the v1 skill instructions were unchanged during that comparison.

## Proof boundaries

- Root ran five standard-library probes showing actual faulty fixture behavior: stale authorization, mutable historical attribution, identical-intent collapse, abandoned-stream reads and partial file publication.
- Model outputs are architecture proposals. The proposed fixes were not implemented or subjected to production/runtime acceptance.
- Grade aggregation checks exact evidence quotes, unique coverage and critical gating. Its self-check rejects fabricated passing evidence and verifies that a critical failure cannot be hidden by a high total.
- A separate Luna document review found no material issue before discovery; discovery still exposed a real instruction/application weakness. Document review is not end-to-end proof.
- Hardware timing, real provider behavior, migrations, large-repository discovery and deployment were not validated.

Use the skill to make assumptions, ownership and verification obligations explicit. Actual project correctness still depends on the requirements, implementation, environment and evidence from that project.
