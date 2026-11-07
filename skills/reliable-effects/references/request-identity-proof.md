# Request identity: required proof

Use this branch when an operation promises deduplication by request key. The promise applies to every accepting path, including one whose submitted business fields are unchanged. Record key scope, canonical intent, admission/completion point, replay authority, retention and the result of a repeat. Equal payloads can represent different intentions.

Before implementation, map the following guarantees to executable tests. A missing test leaves the corresponding guarantee unverified. Where a case is structurally impossible, name the actual serialization or protocol boundary that excludes it; a small operating volume is not that proof.

| Guarantee | Discriminating scenario and observation |
| --- | --- |
| A key represents one accepted operation | Accept the request, advance its downstream state, then repeat the same key/intent. Assert the defined replay result, preserved newer state and no second operation or newly admitted effect. Cover accepting branches that change no business fields. |
| A key binds to its intent | Reuse it with materially different intent. Assert the defined conflict/refusal and unchanged authoritative state and delivery intent. Compare canonical business meaning, not incidental JSON ordering or equivalent address formatting. |
| Overlapping executions share one winner | If retries can overlap, pause one execution after its preliminary read and before its authoritative write. Let another accept and advance downstream state, then resume the paused execution. Assert every coupled write belongs to the winning acceptance; an older acceptance record merely existing is insufficient. |

For the overlapping case, choose downstream progress that could make the stale action appear eligible again. An e-mail example is accepted resend → actual worker send → matching bounce → delayed duplicate resumes. Drive the real owner/store and worker boundary, isolating the external provider; assert stored delivery identity/status and permitted external effects, not just the command's return code. Control interleaving explicitly rather than using sleeps.

The repeated caller may retrieve the prior result or continue the already accepted obligation according to its protocol; deduplication does not forbid valid recovery. Exercise a new deliberate request with a fresh key when the product permits it, so a payload-based blanket block cannot satisfy the tests. A pending provider outcome must not silently become a fresh send.

Show that the test catches the relevant broken mechanism: omitted acceptance identity in an unchanged branch, removed intent comparison, or a coupled-write guard that admits a previous winner. Safely mutate the real guard in an isolated copy or equivalent controlled check and restore it. Keep the RED/GREEN evidence with the implementation; fixture setup failure does not count.

Report each promised guarantee with its test/result and material untested boundary. These cases establish admission/replay behavior, not provider-wide exactly-once delivery, unlimited retention or complete crash recovery; select other protocol checks from the actual contract.
