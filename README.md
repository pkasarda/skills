# skills

Reusable agent skills for source-grounded decisions, complete user flows and honest verification.

| Skill | Use it for |
| --- | --- |
| [robust-architecture](skills/robust-architecture/SKILL.md) | Designing or challenging ownership, boundaries, invariants and failure contracts. |
| [production-ui](skills/production-ui/SKILL.md) | Complete lists and pickers, coherent filters, realistic content and truthful asynchronous UI. |
| [safe-state-changes](skills/safe-state-changes/SKILL.md) | Implementing bounded mutations through the existing owner with scope, state and coupled-effect guards. |
| [reliable-effects](skills/reliable-effects/SKILL.md) | Recovering asynchronous delivery, retries, unknown provider outcomes and compensation. |
| [evidence-based-verification](skills/evidence-based-verification/SKILL.md) | Choosing discriminating checks and reporting what the evidence actually proves. |
| [issue-readiness](skills/issue-readiness/SKILL.md) | Reconciling issue decisions, current source, ownership, prerequisites and effective readiness. |

Each skill lives under `skills/<name>/`. Start with its `SKILL.md`; supporting references are loaded when relevant. Each can be used independently. Combine only those needed by the affected contract: a scoped picker can need `production-ui`, a changed save operation can also need `safe-state-changes`, and a claim about the result needs appropriate verification. An ordinary local edit does not need all six.

These are technology-neutral workflows. They use the project's actual framework, store, design system and authority rules; they do not replace platform documentation or grant permission to publish, merge, migrate or deploy. They guide decisions and checks, without guaranteeing correct architecture or production readiness on every project. Visual design remains a separate concern from data completeness and successful persistence.

## Install with `npx skills`

Requires Node.js 22.20 or later. Run from the project where you want the skills:

```sh
npx skills add pkasarda/skills
```

The interactive installer lets you choose skills and agents. To install all six for both Claude Code and Codex in the current project:

```sh
npx skills add pkasarda/skills --skill '*' --agent claude-code codex
```

To install only one skill:

```sh
npx skills add pkasarda/skills --skill production-ui --agent claude-code codex
```

Add `--global` for use across projects. Preview the available skills without installing:

```sh
npx skills add pkasarda/skills --list
```

This installs standalone skills rather than the plugin package. Start a new agent session and invoke a skill, for example `$production-ui` in Codex or `/production-ui` in Claude Code. Choose this method or plugin installation for a given host to avoid duplicate skill entries. See the [skills CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

## Install as a plugin

The repository is one skills-only plugin, `pkasarda-skills`, in the `pkasarda` marketplace. Both hosts use the same six folders under `skills/`. It has no hooks, MCP servers or runtime dependencies. The public repository can be fetched without GitHub authentication.

### Codex

```sh
codex plugin marketplace add pkasarda/skills
codex plugin add pkasarda-skills@pkasarda
```

Start a new chat after installation. For example, ask to use `production-ui` to inspect a data-backed picker, or `robust-architecture` to assess an operation's ownership and failure contract.

To refresh the repository catalog:

```sh
codex plugin marketplace upgrade pkasarda
```

The catalog refresh and the installed plugin version are separate. After refreshing, use the Plugins page to apply an available plugin update. For the current CLI commands, see [Codex developer commands](https://learn.chatgpt.com/docs/developer-commands).

### Claude Code

Run these commands in your terminal:

```sh
claude plugin marketplace add pkasarda/skills
claude plugin install pkasarda-skills@pkasarda
```

Start a new session, then invoke a skill such as `/pkasarda-skills:production-ui` or `/pkasarda-skills:robust-architecture`.

To refresh the catalog and update the installed plugin:

```sh
claude plugin marketplace update pkasarda
claude plugin update pkasarda-skills@pkasarda
```

See [Claude Code marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) for installation and [the manifest reference](https://code.claude.com/docs/en/plugins-reference) for packaging.

### Local development

With a local clone, pass its root to `codex plugin marketplace add /absolute/path/to/skills`. Claude Code can load it for one session with `claude --plugin-dir /absolute/path/to/skills`. These use the same source folders; no generated copy is needed.

The root `plugin.json` uses the portable Agent Plugins format supported by Codex. `.claude-plugin/plugin.json` provides Claude Code metadata. The two marketplace manifests point to the repository root. See [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins) for the portable format.

Keep `name`, `version` and shared metadata aligned between plugin manifests, and bump both versions when publishing a plugin update. The plugin's package version is separate from the architecture skill's v2 evaluation history.

Use one installation method per host. Standalone copies already present in a user skills directory can appear alongside the plugin; installing this package does not remove those copies.

## Validation

See [validation scope and limits](VALIDATION.md) for the five additional skills. They received structural checks and one bounded independent review, not separate efficacy benchmarks.

`robust-architecture` is v2. Its [evaluation record](skills/robust-architecture/evals/RESULTS.md) distinguishes the historical precise-task comparison, miniature repository discovery tests, the critical issue discovered there, and the targeted v2 regression/transfer checks. The v2 targeted set passed 10/12 criteria, including all 8 critical criteria; a complete paired v2 benchmark and production validation were not performed.

Evaluation fixture code intentionally contains defects. It is test input, not an implementation to copy or silently repair. Raw proposals, rubrics and failed runs are retained for inspection. Additional private-project checks are not included in this shared library.

## License

[MIT](LICENSE) © 2026 Peter Kasarda.
