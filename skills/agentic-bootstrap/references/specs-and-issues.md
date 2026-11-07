# Specs and issue handoffs

Use existing formats and canonical owners. A spec records the intended contract; an issue defines a bounded unit of delivery. Connect them with a stable path/link and section rather than duplicating the full contract.

## Write the spec

Use [the spec template](../assets/spec.md.template) when a new spec is useful. Scale it to the task and omit irrelevant sections. Include the actor/job, first flow, rules and access decisions, meaningful failure/recovery, scope exclusions and observable acceptance. For an existing system, anchor current behavior and owners to inspected source/revision; distinguish them from the proposed change. For a new system, keep technical placement provisional until designed.

Label accepted decisions, working assumptions, open choices and proof separately. Record authorization and lifecycle decisions with their authoritative owner or policy document. An unresolved business permission cannot be filled by inventing a database field. Use an ADR only for a consequential durable tradeoff that needs its own history.

Keep specification readiness, implementation delivery and executed verification separate. A merged design document does not prove the feature exists. Update living docs after verified behavior changes; keep task reports and historical experiments distinct from current rules.

## Preserve decisions and language

Reuse the project's glossary and ADR owners; use an installed domain-modeling procedure when terms or durable decisions need work. If no convention exists, record an ADR only for a consequential choice with real alternatives whose rationale future maintainers need. Capture status and decision owner/source, context and constraints, options considered, the chosen tradeoff, consequences and revisit conditions. Distinguish a proposal from an accepted decision; link the spec/issue to it rather than copying its rules. Resolve a changed domain term in the canonical glossary, creating a minimal one only when needed. A routine implementation choice can stay in the issue.

## Derive delivery slices

Prefer one independently reviewable result per issue, including the relevant vertical path and proof. A prerequisite/design slice is appropriate when it resolves a real blocking contract. Routine implementation choices can be work inside the slice; reserve a separate decision gate for a consequential unresolved contract rather than making the user select every tool. Name the owner/interface, affected callers, scope/state/effect consequences, acceptance, exclusions and genuine prerequisites. Use [the issue template](../assets/issue.md.template) when there is no adopted format. Preserve explicit holds even if a draft is technically ready.

Check relevant current tracker state when access and scope permit, using issue-readiness if installed. Preserve adopted labels and canonical parents; distinguish duplicates, dependencies and references. A bounded or stale snapshot cannot prove global absence of overlap. If tracker access is unavailable, produce draft slices and mark reconciliation unverified.

Creating files locally is distinct from publishing tracker items. A request to create/publish issues can authorize that action; read-only review or onboarding does not supply that authority implicitly. Reuse existing authorization and avoid another confirmation when publication was already requested. Before an authorized write, check drift, create/update only the intended items, preserve user-authored content and verify the resulting links/relationships. Otherwise deliver concrete issue-ready drafts without posting them.

An implementation handoff is ready for its proposed next step when the contract and owner are sufficient for that step, decisive choices are resolved or explicitly blocking, and acceptance can distinguish success from the relevant refusal. A code task should not require rediscovering the whole project from scratch.

Name the existing delivery procedure and test-first method in the handoff. If the project has no delivery owner and change-delivery is installed, use it for the implementation/review loop. Keep feature code and its unit/integration tests with one implementer. Map material guarantees to discriminating scenarios before production edits, including the failure paths selected by authorization or reliable-effects. Identify the required independent review and verification boundary; the reviewer can also own runtime acceptance when project rules permit. Within an authorized build, continue through that loop; a documentation-only request stops with the prepared handoff.
