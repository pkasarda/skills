---
name: evidence-based-verification
description: Verify a change or claim with discriminating evidence at the actual affected boundary. Use when planning validation, reviewing weak tests, diagnosing false-green results, or deciding whether behavior is verified. Keep checks proportional; trivial edits do not require a full test programme.
---

# Evidence Based Verification

Begin with a falsifiable claim: which actor, action, input/state, observable result and revision/environment are being tested? Choose the narrowest check that can disprove that claim. A verdict is no broader than the evidence that actually executed.

## Choose the right seam

Map the changed contract and its real consumers. Pure logic can use a focused unit check. Query, mutation, file and protocol claims need the relevant real engine or public boundary; fake query rows or a mocked domain command cannot prove their predicates and effects. For UI behavior, reach the named state through the mounted interaction and inspect the outcome, including reopening or stored state when relevant.

Use realistic accepted data and explicit controls. Seed success deliberately and assert setup. Foreign scope, different IDs, null versus zero, stale state and valid unchanged rows should differ where the rule says they differ. A negative assertion about an unrelated decoy does not prove the intended target was protected. A useful test fails when the actual guard, join, ordering or owning operation is removed.

When the claim concerns protected reads/writes or permission changes, derive allow/refusal cases using [authorization](../authorization/SKILL.md) if installed. Its policy matrix selects the cases; this skill determines the evidence needed to prove them.

## Make failures discriminating

Select relevant failure points and controlled interleavings rather than sleeps or repetition as the diagnosis. Control the clock at the authority that uses it before deriving dependent fixtures; browser timezone does not determine a Node or server expectation. Keep wall/calendar time and elapsed deadlines distinct, and restore local controls afterward.

Measure the real bottleneck before changing timeout, setup or concurrency policy. Preserve safety assertions and meaningful scope/ID diversity while improving fixtures. A justified test-local budget differs from a blanket timeout waiver. Repeated failure needs a new hypothesis, not merely another retry.

## Trust the run, then the result

Record the process exit, suite/hook/collection health, executed assertions, skips and retries. Zero failed assertions with unexecuted tests is not green. Missing/malformed output or failure before discovery is no valid proof. Keep complete failure artifacts; do not invent counts or report old gates against a newer head.

For deployed behavior, establish which build/environment actually served the request. A checkout SHA, URL nickname or successful build alone does not prove deployed behavior. Separate source review, local tests, runtime, external provider, native/device and deployment results.

## Own test data

Operate only in the authorized test environment and scope. Prefer new isolated rows/resources over changing shared fixtures. Record exact owned identities as soon as creation succeeds, clean them after success and failure through supported lifecycles, and verify cleanup. Preserve shared QA accounts/grants and unrelated history. One-time historical cleanup needs its own inventory and authority.

## Report what happened

State the claim, revision/target, checks and observations; then central states not reached and why; then the bounded verdict. If the named central state was not reached, say unverified in the verdict. A screenshot, source analogy or green retry does not fill that gap.

Broaden checking when a new change, failure or unresolved risk gives a reason. Existing design, UI-stress and test-writing tools may support a specific check; their presence or a high score is not itself evidence of the user's task succeeding. Keep assumptions and proposed experiments explicitly separate from results.
