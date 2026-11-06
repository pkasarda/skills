---
name: reliable-effects
description: Design, implement or debug recoverable asynchronous work and external side effects. Use for delivery, queues, retries, uncertain provider outcomes and compensation. It does not require a queue or outbox for every function or replace the domain owner of the underlying operation.
---

# Reliable Effects

Specify what the application promises before choosing delivery machinery. Trace the originating intention, local commit, dispatch, external acknowledgement and user-visible result. Keep existing domain and delivery owners; inspect all relevant producers and consumers.

## Identity and completion

Name one logical operation and the identity used across incoming retries, durable acceptance and downstream provider/consumer calls. Equal payloads can be different intentions. Define key scope, mismatched reuse, replay authorization and retention. A stable provider key alone does not correlate a newly accepted client retry unless the application binds it to that same operation.

Separate business commit, durable delivery intent, attempted send and acknowledged completion. A timeout can leave the external outcome unknown. Preserve pending/uncertain state and reconcile through a supported lookup or idempotent protocol; do not promise immediate certainty or end-to-end exactly-once behavior beyond the components that enforce it.

If intent must survive a crash, persist it with the state it describes under the existing atomic authority. Reuse a suitable existing protocol; a dedicated outbox is one option, not an automatic requirement. Freeze occurrence facts that later state changes could reinterpret, such as target, audience, version or amount.

## Execution and recovery

State who claims work, how a claim/lease is proved on completion, which failures retry, and how abandoned work progresses. Bound concurrency, buffering, time and retries according to the actual operating envelope. Handle duplicate and reordered input at the authoritative effect. Keep malformed, unsupported, deliberately skipped and successfully completed work distinguishable with safe diagnostics.

Trace every publication, not only the final callback. Before changing caches, current projections, notifications or externally visible objects, enforce the result's applicable identity/version/lifetime. An old but valid historical fact may still need recording while a current-state update is refused. Cancellation may race completion and does not undo an already committed business effect.

A compensation is a separate guarded action that can fail. Preserve evidence and responsibility if only part of a reversal succeeds; do not bury a surviving valid occurrence because one local component rolled back. Define user/operator recovery and the point at which automatic work stops.

## Policy and retention

Derive recipient eligibility, authorization and preferences from their actual owners. Distinguish required documents or security delivery from optional notifications according to the product contract, without widening recipient scope. Avoid sensitive data in logs, push previews or retry artifacts.

Before cleaning work records, determine whether they are also deduplication, replay, ownership or audit evidence. Retention must preserve the guarantees still promised to delayed clients and consumers. Deleting DONE rows is not automatically harmless; keeping all records forever is not automatically the right policy either.

## Prove the protocol

Use controlled crashes/failures around commit, claim, send, acknowledgement and completion. Include accepted-send/lost-response ambiguity, duplicate/reordered input, stale claim, failed compensation and eventual valid progress where applicable. Verify actual state and external-effect identities using a faithful external seam; a mock send count alone proves little.

Report exact guarantees and boundaries, recovery path, relevant operating limits and executed versus proposed proof. Provider, broker and storage semantics must be checked for the chosen platform. Live sends, infrastructure changes, data cleanup and deployment require the user's applicable authority.
