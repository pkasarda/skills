---
name: change-delivery
description: Deliver a scoped feature or bug fix from its accepted contract through test-first implementation, independent review and verified handoff. Use when asked to implement or finish a change and no project-specific delivery workflow already owns it. Read-only advice, discovery-only work and trivial copy edits do not need this workflow.
---

# Change Delivery

Own one change through its requested endpoint. Follow an existing project delivery procedure when it covers this work; use this procedure to fill a missing delivery loop, not to run a second one. A repository's authority and required gates remain in force.

## Establish the contract

Inspect the working path, revision, instructions, relevant source and work in progress. Preserve unrelated changes. Read the originating request/spec and accepted decisions; check current issue discussion when an issue supplies the contract. Use issue-readiness if installed when overlap or stale scope needs reconciliation.

State the observable outcome, authoritative owner/interface, relevant callers, acceptance and exclusions. Ask only unresolved choices that change correctness; continue independent work while waiting. Use product-discovery for an unresolved product promise or robust-architecture for a missing ownership/failure contract, if available. A prepared task can proceed directly; a clear implementation request needs no new blanket sign-off.

Preserve the requested endpoint: local implementation, reviewable branch/PR, or an explicitly authorized release. Keep separate what is implemented, verified, published and deployed. A held programme stays held unless its activation is authorized.

## Select one delivery and test path

Reuse the user's chosen execution method and project roles. Select skills by the affected contract: authorization for access, production-ui for data-backed interaction, safe-state-changes for durable mutations, and reliable-effects for delivery/retry uncertainty. Load an available sibling only when needed; use the existing project owner when it already supplies the same rules. Missing siblings do not prevent this skill from working.

For behavior changes, choose the installed test-first procedure that belongs to this execution path: for example Matt Pocock's `tdd` or Superpowers' `test-driven-development`. Follow one, with project/user instructions taking precedence. Do not invoke both or start another planning workflow merely to use its TDD skill. Without either, use the loop below directly.

For a substantive slice, name the implementer and independent reviewer. Delegate only when the harness and request permit; compatible tasks can stay with one implementer. Keep a compact done/running/next checkpoint for long work.

## Turn risks into failing tests

Before production edits, map each affected acceptance rule and material failure guarantee to a test at the real public/data seam. Name the wrong change the test should catch. Derive cases from the operation's contract, not only its happy path. Retry keys and coupled effects require the concrete proof selected by their owning procedure; a general instruction to test edge cases is insufficient.

When no specialized procedure is available, a request-key contract still needs replay after downstream progress (including unchanged-field acceptance), changed-intent refusal without effects, and controlled overlap if duplicate attempts can race. Preserve valid recovery of the accepted operation and permitted new intentions with fresh keys. For conflicting coupled writes, test all effects against the admission that actually won; independent compatible commands may both commit under their contract.

Run one discriminating test and observe it fail for the intended missing behavior. A setup/import failure does not establish RED. Make the smallest complete vertical change, observe GREEN, and repeat for the next rule. Keep cleanup/refactoring behavior-preserving and tests green. If the regression test was added after a fix, safely demonstrate sensitivity by removing the relevant guard in an isolated copy or another controlled mutation; restore the source and run green again. Record any unexecuted proof honestly.

Exercise relevant callers and actual storage/query/protocol behavior. A mocked owner cannot prove its guards. For a trivial prose/configuration edit with no meaningful behavioral test, use the direct artifact/config check instead; throwaway spikes follow their explicitly agreed verification scope.

## Review and resolve

Run the project's affected checks and required gates. For a substantive change, request a fresh independent review with the accepted contract, exact revision/diff, relevant instructions and raw evidence. Ask it to find missing behavior, incorrect failure/access outcomes, regressions and unnecessary scope. Supply evidence without prescribing its findings. A user-selected reviewer or tool takes precedence over adding another review system.

If independent review is unavailable, label the review as self-review and leave any required independent gate unmet. A passing suite or implementer's own reread does not satisfy it.

Verify findings against source, fix material defects or record a concrete justification, then rerun affected tests/checks on the changed revision. Obtain renewed independent review when a fix changes the substantive contract or leaves a material finding unresolved; follow a project's existing stopping rule. Do not repeat an unchanged green gate without new evidence requiring it.

## Close the requested loop

Use evidence-based-verification if available to match each claim to executed evidence at the affected boundary. For user-visible behavior, reach the changed state through the actual interaction; report missing runtime/device/environment access as unverified rather than substituting a screenshot or source analogy.

Update durable rules/specs when behavior establishes new facts, preserving one canonical owner. For a lasting tradeoff or changed domain term, follow the project's ADR/glossary convention; bootstrap's [spec and decision guidance](../agentic-bootstrap/references/specs-and-issues.md) is an optional fallback if installed. Do not create a new ADR for a routine local choice.

Commit, publish, update issues, merge or deploy only within the request's authority; execute already-authorized steps without asking again. Check current tracker/branch state before external writes and read back the result. Recheck the served revision before claiming deployed behavior. A blocked release does not erase a completed local result.

Deliver the outcome, revision/artifacts, tests and observed results, review disposition, unverified guarantees and remaining authorized next step. The requested endpoint and applicable gates determine completion; missing proof remains visible.
