# Access surfaces

Use the sections that the affected policy reaches. Extend the inventory when a concrete caller or alternate representation is found, not into an unrelated security audit.

## Queries, fields and files

- Scope list, search, autocomplete, totals, exports and individual reads to their intended audience. A deliberately broader aggregate needs an explicit disclosure rule. Filtering after pagination or after serialization can leak or omit data.
- Resolve child IDs through an authorized parent/relationship or prove the child's scope directly. Validate every referenced resource in bulk writes and link/unlink operations; a valid first item does not authorize the rest. Preserve the operation's documented partial or all-or-nothing result.
- Treat editable and visible fields separately. An allowed update must not smuggle ownership, tenant, role or approval changes; an allowed read need not expose internal notes, credentials or full nested entities.
- Files and generated artifacts retain their policy at download, preview, derivative and storage/CDN paths. An authorized page does not protect a public object URL. A bearer URL intentionally grants a capability; document its audience, lifetime and sharing semantics rather than claiming ordinary account checks still apply.

## Caches and long-lived delivery

- Key or partition protected caches by every policy dimension that changes the result. Authorize before serving a cached result and check applicable identity/lifetime before late work publishes to shared state. A permission change needs the promised invalidation or revalidation behavior; merely changing the visible screen cannot retract leaked data.
- For streams and subscriptions, establish admission, message audience and the effect of expiry or grant changes during the connection. Match checking frequency to the promised semantics. A successful handshake alone does not establish indefinite authority.
- Data already delivered or a bearer artifact already issued may not be retractable. Define that limitation and the actual revocation mechanism before promising immediate withdrawal.

## Capabilities, jobs and delegation

- A public token/link has an issuer, purpose, resource/action scope, integrity/verification mechanism, expiry and any revocation or usage limit the product promises. Refuse a token for another resource or action. Apply appropriate credential handling; avoid placing bearer secrets in logs or diagnostics.
- Distinguish an actor-triggered asynchronous request from a trusted scheduled obligation. Name which authority is delegated, how it is bounded, which facts are frozen and which must be current. Delivery of a valid committed document can survive the initiating user's role change; newly accessing its content can still require current permission. Follow the accepted policy rather than a universal recheck-or-cancel rule.
- A replay key correlates an intention; it is not automatically a read credential. Scope any returned prior result under its applicable access policy. Distinguish receiving the same outcome from initiating another privileged effect.
- Derive job/integration scope from validated configuration, delegation or signed input. A supplied organization ID or a generic service account does not justify arbitrary cross-tenant access. Use narrowly defined system authority where the product actually needs it.

## Primary background

The workflow is independently authored. These references support baseline access-control and object-reference concepts, not the security of any particular implementation:

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).
- [OWASP IDOR Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html).
