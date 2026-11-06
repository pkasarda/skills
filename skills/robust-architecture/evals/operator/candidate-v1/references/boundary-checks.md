# Boundary checks

Read the branch matching a real requirement. These are questions to resolve, not infrastructure to add to every project.

## Durable effects and external systems

- Name the local commit and the external acknowledgement. Enumerate the windows between them. After an ambiguous timeout, the effect may already exist.
- An atomic acceptance record, stable request identity and provider/consumer idempotency can compose a recoverable protocol. State which component deduplicates which effect and for how long. A request hash alone does not identify an intention.
- When delivery must survive a crash, persist intent with the state it describes using the existing owner. A queue/outbox is one implementation, not a universal prerequisite. Define retry budget/backoff, duplicate/reorder handling, reconciliation and the operator/user result when automatic progress stops.
- Record data needed at the occurrence before later mutations erase it. A consumer should not silently reinterpret old work using today's owner, recipients or price.
- A network partition can make a globally coordinated definitive answer unavailable. State the exact consistency and progress guarantees, time bounds and permissible degradation. Surface incompatible requirements instead of promising all of them.
- Compensation is a new action with its own guard and possible failure, not transaction rollback. Preserve evidence and responsibility when reversal cannot be completed.

## Files, streams and resource lifetime

- Assign responsibility for opening, borrowing, transferring, cancelling and closing each resource. Define early exit as well as normal exhaustion; garbage collection or abandoning a generator may not close it promptly.
- Propagate cancellation/deadlines to owned work, await termination when required, and bound buffering/backpressure. Test a slow or abandoned consumer while references remain alive.
- Define what a completed file means. A completed temporary file and appropriate same-filesystem replacement can protect the previous output from partial publication; platform replacement semantics and persistence after power loss are separate guarantees.
- Persist only the progress necessary for resume. Reconcile an output committed just before a crash with progress not yet recorded, and bind resume to the actual source/settings/target identity. Resolve overwrite and stale-input semantics explicitly.

## Real-time and bounded resources

- Put deadlines and memory/queue limits in the contract. Separate hard-deadline work from blocking I/O, allocation, locks and unbounded callbacks where the execution environment requires it.
- Choose bounded handoff, ownership and overload behavior: reject, coalesce, drop, degrade or wait, according to the product's semantics. Specify a valid state when fresh control data is absent.
- Measure the relevant worst case on the target environment. Desktop averages, static inspection and a passing functional test do not establish a real-time guarantee.

## State, history and authority

- Decide whether the feature needs a current association, an occurrence snapshot, a versioned value or a relationship interval. Choose the smallest representation that answers the actual historical question.
- Missing legacy history stays unknown unless reliable evidence can recover it. Avoid silently backfilling yesterday's fact from today's association. Audit strings do not become an implicit relationship database.
- Separate permission to create a new fact, attribution of an old fact and permission to read it. A historical association is not by itself a current access grant.
- Distinguish instants, civil date/clock inputs, effective intervals and elapsed durations. The relevant authority resolves calendar rules; clients or local processes may be that authority when the product is local/offline. Use an appropriate monotonic clock for elapsed deadlines.
- Validate the complete resulting state, including sparse/clear/no-change semantics. Keep a stored historical reference distinct from eligibility for a new selection.
