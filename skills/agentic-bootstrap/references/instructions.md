# Instructions and progressive disclosure

Use this guide when creating or restructuring project instructions. Inventory effective files first. Preserve useful existing conventions and authority; fill templates only for missing artifacts.

## Place each meaning once

- Root instructions: stable context, non-obvious working rules, authority boundaries and critical invariants relevant across that root's scope.
- Scoped instructions: rules that apply only inside a real package/directory scope.
- Referenced document: domain knowledge, access policy or architectural decisions consulted for a topic.
- Skill: a reusable task-shaped procedure, selected when its trigger applies.
- Spec/issue: the current feature's behavior, acceptance and temporary implementation scope.
- Configuration/source: readily discoverable commands and implementation facts. Cache them in prose only when the maintained pointer materially helps.

Root instructions are a small interface. State a pointer as a condition and action, such as “When changing customer-visible fields, read the access policy at …”. Use real, repository-relative targets that resolve from the written file. Keep generated guidance portable across checkouts; do not bake in the author's machine paths or the installed copy of this skill. A link in Markdown makes material reachable; it does not automatically load it. Keep conditional docs out of unconditional imports. Preserve the critical rule in effective instructions if missing it would create a real safety or authorization gap.

Split by scope or conditional use, rather than by arbitrary line count. Create detailed documents when they have maintained content; leave no empty directory tree for hypothetical features. Use [the root template](../assets/AGENTS.md.template) only when writing a new root, substituting the project's verified facts and boundaries. Remove optional empty sections and every unresolved token before handing off.

## Share guidance across tools

Use one canonical body when the target tools support it. `AGENTS.md` is a practical shared root. Inspect the installed clients and active settings before relying on their discovery behavior:

- Codex discovers instructions along the project-root-to-working-directory chain. Confirm the effective working scope and applicable nested files.
- Current Claude Code can use `AGENTS.md` directly in supported configurations. Where a Claude adapter is needed, use [the adapter template](../assets/CLAUDE.md.template), importing the adjacent canonical file. Keep Claude-specific additions narrow.
- A root import does not recursively activate every nested instruction file. If a parent Claude file prevents nested `AGENTS.md` discovery, use a matching scoped adapter or the tool's supported scoped-rule mechanism, and verify it. Keep shared nested content in one owner.

Avoid copying whole skills into root instructions. Installed skill availability and project instructions are separate: a plugin may supply a procedure while the repository supplies its concrete owner and policy. Do not change a user's global settings merely to make a proposed layout work.

Check root and scoped loading with the target client's supported context/diagnostic facilities. A filesystem/link check proves structure only. If client execution is outside scope, report the loading gap and a specific verification step instead of claiming it worked.

Primary platform references, checked when authoring this guide:

- [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- [Claude Code instruction loading and imports](https://code.claude.com/docs/en/memory).
