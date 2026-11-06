# Foundations

These primary works motivate parts of the skill. Their principles need the assumptions of the actual project; citing them is not proof that a design is correct.

- D. L. Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* (1972): boundaries should hide design decisions that callers need not know. [Original publication](https://doi.org/10.1145/361598.361623), [paper reprint](https://ckrybus.com/static/papers/decomposing_systems_into_modules_1972.pdf).
- J. H. Saltzer, D. P. Reed and D. D. Clark, *End-to-End Arguments in System Design* (1984): completion and correctness depend on the application-level requirement, even when lower layers supply useful mechanisms. [Authors' MIT copy](https://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf).
- S. Gilbert and N. A. Lynch, *Perspectives on the CAP Theorem* (2012): coordinated shared-state semantics have consistency/progress tradeoffs under unreliable communication. This is not a blanket two-out-of-three rule for every application. [Authors' MIT copy](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf).

Reviewed 2026-11-06. The publisher landing page for Parnas returned403; its original paper was checked through a reprint. Recheck versioned platform APIs separately when choosing mechanisms.
