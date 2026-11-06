---
name: issue-readiness
description: Assess whether an issue, epic or proposed slice is current, owned and ready for action. Use before planning implementation from a backlog or reconciling stale specifications and overlapping work. Assessment is read-only unless the user separately authorizes tracker changes.
---

# Issue Readiness

Turn the current request into an actionable decision, preserving the distinction between intended behavior, implemented code and executed proof. Use the project's tracker conventions and existing statuses; this skill does not create a new workflow taxonomy.

## Establish the actual request

Pin the source revision being assessed. Read the whole issue and discussion, relevant accepted decisions, actual parent/child relations and linked work. Paginate real tracker data where necessary. Checklists and text counts may lag the tracker; a closed child can mean superseded or rejected, not implemented. A number mentioned in prose is not automatically a dependency or even the same resource type.

Weigh authority and specificity as well as recency. A direct accepted product decision is not erased by a later automated summary claiming it is unanswered. Separate a later scope correction from an implementation restart. When authoritative statements conflict, name the consequence and missing decision rather than silently selecting a product contract.

## Check source and ownership

Trace mounted producers and consumers of the requested behavior, the authoritative owner, stored facts and relevant checks. Verify concrete source references. Test redundancy by domain concept rather than title wording. Existing behavior can make a missing-feature request obsolete while leaving a narrower independent guard or UX defect real.

Classify the remaining work: missing fact/ownership/contract, bypass of an adequate owner, unresolved product behavior, or local presentation. A cluster around one missing model needs one design decision, not parallel patches per reader. Give each remaining invariant and implementation slice one canonical home; references outside a parent relation need not be moved under it.

Check active work and exact PR state/head. Fixes, mentions, deferred work and shared prerequisites are different relationships. An open PR is not current-main delivery. An implemented path, merged proposal document and passing historical gate establish different things; none proves current live migration or acceptance status.

## Decide effective readiness

A useful handoff names the current/desired outcome, owner/interface, affected callers, scope/state/effect consequences, acceptance proof, exclusions and concrete unknowns. Keep implementation details provisional where the model itself is unresolved. Ask only the missing choice; preserve already settled decisions.

Technical specification readiness is distinct from permission and activation. Honour programme stops, customer triggers, prerequisite designs and active overlapping writers. Retain a prepared brief when work is held, but do not present it as available for an unattended agent. One explicitly authorised standalone task may override a programme gate; do not infer that override from a product answer or an audit request.

## Report and maintain scope

Give a source-grounded disposition per requested item, actual relation counts when relevant, overlaps and one next action or specific question. State what was not checked. Recommend bounded delivery groups and unresolved model work; avoid re-creating completed or superseded slices.

When tracker writes are explicitly authorized, preserve existing label mappings, priorities, canonical relationships and author content unless the request includes changing them. Check discussion/source drift before writing and verify the resulting state. Prefer updating the known current handoff over duplicate comments. New issues, closure, reparenting, publication, merge, deployment and migrations each retain their own applicable authority; this skill grants none implicitly.
