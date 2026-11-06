---
name: agentic-bootstrap
description: Set up a new repository or onboard an existing project for agent-assisted work, connecting project context, specs, issue handoffs and progressively disclosed instructions. Use for project bootstrap or instruction/workflow onboarding. A bounded feature, bug or copy edit should use its normal delivery procedure without repeating bootstrap.
---

# Agentic Bootstrap

Establish just enough truthful project context and routing for the next useful task. Connect the relevant engineering procedures; keep their detailed rules with their owners. This is a project-entry workflow, not a requirement to run the whole library for every change.

## Establish scope and choose the entry

Resolve the target repository, working path, current instructions, existing artifacts and requested outcome. Check revision/dirty state when source claims or edits depend on it. Preserve unrelated changes. Distinguish read-only advice, local documentation setup, implementation and external publication; carry forward authority already given instead of inserting another approval step.

Read the matching entry guide:

- For a project without a functioning implementation, read [New project](references/new-project.md).
- For existing code, workflows or instructions, read [Existing project](references/existing-project.md), even when the user is new to that repository. A new module inside an established project keeps its inherited constraints.

Use an explicit user-selected mode when appropriate. If the task is actually a local change, follow the current owner and relevant delivery procedure rather than generating a project dossier. Ask only consequential questions that existing evidence cannot answer; continue independent work while they are pending.

## Build the minimum useful context

Separate accepted intent, observed implementation, assumptions and unexecuted proof. Name the first user flow, its essential rules and applicable authority. Record consequential ownership and failure decisions at the level the evidence supports. A new project can have provisional technical seams; an existing one needs source-grounded owners and callers.

Choose available skills by the work that remains:

| Need | Procedure, if installed |
| --- | --- |
| Unclear actor, job, product promise or first scope | product-discovery |
| Ownership, state/history or complete failure contract | robust-architecture |
| Protected reads/writes, fields, sharing or delegated authority | authorization |
| Data-backed screens and realistic asynchronous interaction | production-ui |
| Durable mutations and coupled effects | safe-state-changes |
| Delivery, retries and uncertain external outcomes | reliable-effects |
| Current issue decisions, overlap and effective readiness | issue-readiness |
| Evidence needed for a concrete claim | evidence-based-verification |

Load only the relevant procedure and its conditional references. If a sibling skill is absent, use the entry/spec guides to state the product flow, owner, access/effect boundaries and acceptance evidence directly. Record unresolved choices rather than implying the missing review happened. This skill must remain usable on its own.

## Produce project artifacts when requested

Reuse the project's actual document and tracker conventions. When writing or restructuring project instructions, read [Instructions and disclosure](references/instructions.md). When preparing a spec or issue handoff, read [Specs and issues](references/specs-and-issues.md). Reach the templates from those guides only when producing that artifact. Keep one maintained home for each rule, with specific pointers from its consumers.

Create or update only artifacts needed by this request. Preserve adopted labels, canonical issue relationships, accepted product decisions and explicit programme holds. A useful ready brief can remain held; bootstrap is not permission to restart delivery. Keep stable knowledge separate from temporary task requirements and review snapshots.

A setup request does not itself authorize application rewrites, dependency installation, live-data changes, issue publication, merge, deployment or migration. Within authorized local scope, finish the files and relevant validation. If an external action is already requested, prepare the concrete artifact, check current state and execute within that authority; otherwise return the ready-to-use draft.

## Verify the handoff

Check written facts against their source, links against actual targets, examples against applicable policy, and commands against project configuration. Remove unresolved template tokens and empty scaffolding. Verify how the active tool loads root/scoped instructions; keep untested loader behavior explicitly unverified.

Try a few representative task shapes against the routing: a trivial edit stays local, a normal feature reaches its owner, and a protected or cross-cutting change reaches the needed deeper rules. Test relevant authority or paused-work boundaries when they changed. Judge the selected context and action, not recited document names.

Deliver the selected mode, created/updated artifacts, decision and evidence gaps, proposed delivery slices, checks actually performed and next action. Readiness is for that next action, not the whole future roadmap. Continue an authorized build when its required choices are clear; a documentation-only onboarding finishes with a coherent handoff.
