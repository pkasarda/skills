---
name: production-ui
description: Build or assess data-backed UI for complete, reachable results and truthful asynchronous behavior. Use for lists, filters, database-backed pickers, forms and workflows that must work beyond demo data. Keep static copy or visual-only changes local; this is not a replacement for visual design.
---

# Production UI

Make the user's actual task work with the data and states the product accepts. Assess the affected surface, not an imagined whole-product readiness label.

## Trace the data contract

Start at a real entrypoint and follow the loader/query, serialized view, controls, mutation and refreshed result. Identify the current actor/context, applied filters, sort, selection and relevant limits. Compare source to the intended task; a mock screen or green happy-path test is not evidence of complete data access.

For each affected collection, establish what the rows and count mean and how an authorized record beyond the first page is reached. A limit can bound work; silent truncation that masquerades as the complete population is a defect. Rows, count, search and drill-through must share the same authorized population. A bounded or approximate count may be honest if its meaning is explicit and the task remains possible.

Classify option sets before changing loading: static enums, already available small/bounded data, and growing or expensive query-backed choices have different needs. Load data when the interaction needs it, using existing components and readers. Choose a page/search contract appropriate to measured data and latency, rather than replacing one arbitrary cap with another or creating infrastructure for hypothetical scale.

For picker, filter or async request work, read [Data interaction checks](references/data-interactions.md). Keep authorization and eligibility in their existing server/store owners; a UI flag or client filter cannot supply that proof.

## Exercise real states and content

Choose realistic accepted data at the actual boundary: zero, one, beyond-page results, long/missing labels, fractional/zero/unknown values, existing inactive selections and relevant role differences. Preserve meaning: missing, measured zero, withheld and incomplete are distinct states. Use supported formatting and business/time authorities rather than a second client derivation.

Trace initial loading, empty search, transport failure, partial/stale data, pending mutation and refresh after success or refusal. Name the user's next action in each state. Preserve valid drafts on failure, distinguish uncertain completion from a definite refusal and avoid automatic repeats of non-idempotent work. Late responses must be checked before every applicable cache/state publication, including after the same scope is reopened.

Use the actual target layouts, keyboard/focus behavior and relevant device constraints. Check accessible names, errors attached to the real control, scroll/overflow discoverability and reachable actions with real content. Reuse the project's design system. Visual-design or content-stress skills can help when available; they do not establish query completeness or successful persistence.

## Prove the task

Select a thin end-to-end scenario: find an authorized record outside the first page, select or modify it, save, reopen and confirm the actual result. Include a meaningful refusal or interrupted/stale path and a wrong-scope decoy where applicable. Test query/count/serialization at the real data seam; use actual UI interaction for a claim about usability. Screenshot appearance alone does not prove the task completed.

Create isolated test data only within the user's authorized environment, record owned IDs and clean them through supported lifecycles. Preserve shared personas and unrelated data. Measure affected payload/query/interaction cost before claiming performance improvement. A source risk is not a measured bottleneck.

Report the concrete task and states reached, evidence, unreachable states and smallest fixes. A central unreached state remains unverified in the verdict. Design, source review, component tests and mounted acceptance establish different things. Respect the requested scope; findings do not themselves authorize backend rewrites, deployments or live-data changes.
