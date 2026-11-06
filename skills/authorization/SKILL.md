---
name: authorization
description: Design, implement or review access policy for protected resources and operations. Use for new protected entrypoints, roles, ownership or tenant scope, field visibility, sharing links, delegated jobs and permission changes. Authentication alone does not settle access; visual-only edits need no authorization review.
---

# Authorization

Make each affected access decision explicit, enforce it at the real boundary and prove both allowed and refused behavior. Work within the requested flow; loading this skill does not start a whole-application audit. Use existing identity, policy and domain owners before introducing a new framework.

## Define the policy

Read accepted product decisions and actual callers. Record a small policy matrix for the changed flow: principal, operation, resource, applicable relationship/scope/state, allowed input/output fields and outcome. Use roles, attributes, ownership or capabilities according to the actual need; a role alone may not establish access to a particular record. Preserve intentionally different read, write, export, share and administrative permissions.

Separate identity authentication from the permission to act. Obtain identity and grants from trusted session, token or service context. Request IDs, tenant selectors, role fields and UI state select or describe a request; they do not confer authority. Anonymous/public access can be explicitly permitted or capability-scoped. Missing identity or scope must not silently become a global/system grant. Keep privileged operators and impersonation explicit and attributable.

Default unmatched access to refusal and use the least authority that satisfies the accepted policy. An undecided business permission is a product question, not an invitation to invent a permissive default. Continue independent work while that choice is unresolved. Keep a deliberately local, non-shared demo distinct from a service exposing real protected data.

## Find every affected access path

Follow the affected resource through its actual entrypoints and owners. Include relevant web/mobile APIs, server-rendered loaders, actions, imports, batch operations, jobs and integrations. Inspect search/count/export, files, caches and subscriptions when they expose the same protected facts. Read [Access surfaces](references/access-surfaces.md) for those paths or for capabilities, delegation and revocation; select the applicable sections.

Name the policy owner and enforcement points. Centralize the meaning of the rule while enforcing it wherever data or effects cross trust boundaries. A middleware login check, UI guard, UUID or earlier successful read is insufficient by itself. A framework policy, database policy or scoped owner can work; verify its actual configuration and runtime credentials instead of assuming it covers bypass routes.

## Enforce the decision

For reads, restrict the authorized resource population before results leave the trusted boundary and restrict returned fields. Apply equivalent policy to related objects and alternate representations. Use the product's disclosure policy for missing versus forbidden resources; errors, counts and serialized props can reveal protected facts too.

For mutations, validate the action, target and resulting relationships, including user-supplied foreign keys and protected fields. Use allowed input fields rather than binding an entire request into a durable entity. Where a reachable interleaving can invalidate authority, enforce scope, membership or state at the effect using the store's appropriate atomic guard or serialization. Coupled children and side effects follow the same admission. Keep an existing complete owner; do not add another business writer merely to insert authorization checks.

Define when grants are evaluated and when a change takes effect. Current access, immutable historical attribution and a previously accepted durable obligation are different contracts. Replays, delayed delivery and delegated jobs need an explicit authority/lifetime; neither stale user claims nor a generic system identity answers that question. Apply revocation and recovery according to that contract without silently cancelling valid obligations or widening their audience.

## Prove the boundary

Derive a small discriminating test set from the policy matrix. Through the real owner and relevant mounted boundary, show a valid actor completing the operation and meaningful refusals: another owner in the same tenant, another tenant, a weaker role, anonymous/malformed capability or changed grant where applicable. Use actual target records and explicit decoys; assert protected fields, unchanged durable effects and unrelated records. Select relevant cases rather than rehearsing every theoretical combination.

A mocked policy returning true or false proves neither its decision nor the query/write restriction. Test actual predicates or store policies with realistic runtime authority. For UI access claims, verify a direct request independently of button visibility. Do not probe other people's identities or shared/live data; use isolated authorized fixtures. Separate static findings, proposed checks, executed tests and deployment-policy gaps.

Deliver the policy, authoritative sources, affected paths, enforcement and proof, plus unresolved product choices or external configuration. A passing check is bounded to those paths; the procedure does not certify the application's overall security.
