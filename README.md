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

## Validation

See [validation scope and limits](VALIDATION.md) for the five additional skills. They received structural checks and one bounded independent review, not separate efficacy benchmarks.

`robust-architecture` is v2. Its [evaluation record](skills/robust-architecture/evals/RESULTS.md) distinguishes the historical precise-task comparison, miniature repository discovery tests, the critical issue discovered there, and the targeted v2 regression/transfer checks. The v2 targeted set passed 10/12 criteria, including all 8 critical criteria; a complete paired v2 benchmark and production validation were not performed.

Evaluation fixture code intentionally contains defects. It is test input, not an implementation to copy or silently repair. Raw proposals, rubrics and failed runs are retained for inspection. Additional private-project checks are not included in this shared library.
