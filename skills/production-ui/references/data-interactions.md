# Data interaction checks

Read only the sections relevant to the affected interaction. These checks describe contracts; they do not mandate a framework, page size or new fetching library.

## Pickers and lists

- A query-backed choice has explicit scope, eligibility, search, deterministic ordering, bounded rows and completeness metadata. Filter and rank before limiting. Validate the form's selected context at the query boundary rather than loading unrelated options and hiding them in the browser.
- Separate the whole option set from current search matches. A query returning three matches does not prove the client holds the entire original set. Switch to client-only search only when completeness of the relevant unfiltered set is established.
- Keep a selected value's authorized label when it falls outside the current page. Resolve it narrowly; avoid fetching every option to display one chip. A stored inactive value can remain readable while being ineligible for a new selection.
- First open, typing before the first response, rapid search, close/reopen and changing form context all need coherent state. Invalidate old context and ignore obsolete successes and failures before they alter caches or views. Preserve input and make load failure distinct from no matches.
- A truthful footer may use total, has-more or a documented bounded count. Provide the navigation/search needed to reach the rest. Totals and page rows must use equivalent scope/filter predicates; zero rows on an out-of-range page is not proof that the population is empty.
- Reserve or intentionally transition loading space where it affects interaction. Retain stable item identity and meaningful ordering through refresh; do not select a different record because its list index changed.

## Filters and navigation

- Resolve route parameters once into the effective authorized filter state. Controls, chips, rows, counts, exports and drill-through reflect that state, including invalid/foreign values and reset/back navigation.
- A full list, filtered result, tab badge and all-time metric may intentionally describe different populations. Give them honest labels instead of forcing equal numbers.
- Search covers the accepted identifiers and locale rules of the task. Verify escaping, sorting ties, null values and empty results. Exact expensive counts, virtualization and new indexes need a reason and the project's relevant proof.

## Forms and results

- Centre/project/account-dependent options follow the form's effective context. Changing it invalidates incompatible choices. The final mutation independently enforces applicable scope and state.
- Show field errors beside the actual control with the project's supported accessibility contract. Preserve IDs/descriptions, focus and drafts; avoid duplicate announcements or an unrelated generic toast as the only result.
- Prevent unintended native submission behavior before hydration where progressive enhancement applies. Verify method and data exposure, not merely a JavaScript event handler.
- Distinguish a committed operation from failed refresh, optional telemetry or delivery. The UI must not invite a duplicate write because a post-commit step failed. Unknown network completion needs reconciliation or the operation's retry contract.
- Verify success after refreshed rendering as well as rejection: changed buttons need a live focus target, saved selections must survive reopening, and the next legitimate action must remain possible.
