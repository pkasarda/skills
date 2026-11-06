---
name: safe-state-changes
description: Implement or review a bounded state-changing operation with authoritative scope, lifecycle, consistency and truthful results. Use for database or durable-state mutations, transitions and coupled writes. Architecture discovery and ordinary local presentation edits are separate tasks.
---

# Safe State Changes

Make one intended operation safe through its existing owner and every relevant entrypoint. Establish the contract before editing: actor or trusted-job context, target, expected state, allowed effect and refusal, companion writes and explicit exclusions. Use project rules and current code; missing product behavior stays a named decision.

## Trace the operation

Inventory mounted producers of this same operation, including API/UI adapters, imports and background jobs where applicable. Find the authoritative owner and its public interface. If the necessary fact or complete operation has no coherent authority, resolve that model gap before table-by-table patches. An existing owner with an incomplete guard usually needs a bounded repair.

Separate entry trust and parsing from domain admission. Anonymous/token workflows establish their explicit purpose and scope; authenticated workflows resolve the actual actor. Caller-provided IDs, hidden controls and an earlier authorized read are not proof at a later effect.

When designing, implementing or reviewing a protected mutation or its producers, apply [authorization](../authorization/SKILL.md) if installed to cover the access policy and meaningful actor/resource combinations. Keep the existing owner and the write guards below.

## Guard the real effect

Use the store's appropriate atomicity or serialization mechanism when a reachable interleaving can invalidate scope, state, availability, revision or locks. Guard all coupled effects under the same winning operation, not merely the final parent row. Expected-state failure must not leave unrelated child, audit, quantity or derived-state changes. Preserve legitimate correction, historical attribution and sparse/clear/no-change meanings.

Validate the effective resulting state at its owner. Use the actual inserted/generated identity for dependent work. Keep one lifecycle rule and stable refusal contract across callers; do not create a second status writer or reconstruct ownership from today's projection. Respect intentionally separate operations and documented partial outcomes rather than forcing every batch into a new all-or-nothing framework.

Classify companions: which audit, financial, inventory or durable-intent records are part of the invariant, and which post-commit effects are supplemental? Compose required work at the owning boundary. An external call cannot be made atomic merely by placing it beside a transaction. Use the project's reliable-effect protocol, or define the smallest missing contract before implementing it.

## Preserve truthful outcomes

Return whether the intended operation committed, refused, was a no-op, or remains uncertain/partially complete. Keep meaningful typed codes and safe details; log unexpected failures without exposing raw diagnostics. A failed refresh or optional side effect must not masquerade as an uncommitted mutation. Retry or compensation needs an explicit identity and admission policy; do not automatically repeat a non-idempotent write.

## Verify a vertical slice

Test through the public owner and affected mounted adapters, using the actual compiled schema/store or equivalent real seam. Seed meaningful scope, ID and state decoys where the operation uses those distinctions. Assert setup and exact changed and unchanged records. Exercise a valid operation and a relevant refusal. Add no-op/repeat, controlled stale-state or failure-point checks when those are part of the contract or a reachable risk. For coupled effects, prove they follow the same winner and a rollback leaves the promised state.

Run the project's appropriate SQL/query-plan, type/export and targeted behavior checks when their surfaces change. Preserve complete failure output and distinguish blocked-before-execution from failing assertions. Verify the mounted result when claiming user behavior works.

Deliver the owner/interface, affected callers, implemented invariant, result semantics, checks and limits. A small scope does not waive its relevant gates. This procedure grants no authority to apply remote migrations, deploy, merge or alter unrelated data.
