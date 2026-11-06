# skills

Reusable agent skills with source-grounded decisions and reproducible evaluation artifacts.

| Skill | Purpose | Evaluation record |
| --- | --- | --- |
| [robust-architecture](skills/robust-architecture/SKILL.md) | Design or challenge architecture through concrete flows, invariants, ownership and failure evidence. | [Methods, results and limitations](skills/robust-architecture/evals/RESULTS.md) |

Each skill lives under `skills/<name>/`. Start with its `SKILL.md`; supporting references are loaded when relevant.

## robust-architecture

The current skill is v2. It covers data and operation ownership, trust and history, complete failure outcomes, resource limits, proportional structure and discriminating verification. It guides decisions; it does not guarantee correct architecture on every project.

The evaluation record distinguishes the historical precise-task comparison, miniature repository discovery tests, the critical issue discovered there, and the targeted v2 regression/transfer checks. The v2 targeted set passed 10/12 criteria, including all 8 critical criteria; a complete paired v2 benchmark and production validation were not performed.

Evaluation fixture code intentionally contains defects. It is test input, not an implementation to copy or silently repair. Raw proposals, rubrics and failed runs are retained for inspection.
