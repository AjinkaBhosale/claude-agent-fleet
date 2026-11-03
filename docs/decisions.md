# Decisions and trade-offs

| Decision | Why | Cost / what I'd change |
|---|---|---|
| Many focused sub-agents instead of one big prompt | Smaller prompts, clear ownership, easier to test and replace | Overlap crept in; needed a consolidation pass and an auditor |
| Shared skills for config and conventions | One place to fix a wrong field ID or severity label | Agents silently break if a skill is renamed; solved with `tools/lint_fleet.py` |
| Preview, confirm, then write | Jira and Confluence are shared systems; mistakes are visible to others | Slower for bulk work; added `autoCreate` and dry-run modes for trusted runs |
| Blocking quality gate | Stops weak epics before they generate weak stories and tests | Can frustrate on early drafts; severity levels let Nice-to-have pass |
| Verify IDs against live metadata | Models invent plausible custom-field IDs | Extra API calls per run; cached per session |
| Triage separates infra from product bugs | Fixing flaky tests and filing bugs need different actions | Needs reproduction evidence; "green with skips" is checked, not trusted |
| Superseded agents kept with a pointer | Safe migration, no broken references | Clutter; archive after a release |

## What went wrong (and the fix)
- **Wrapper agents referenced agents that did not exist.** They looked fine and never ran. Fix: reference checks in the auditor and the linter.
- **Hallucinated field and account IDs.** Fix: look up from live metadata, never from memory.
- **Markdown mentions in Jira comments did not notify anyone.** Fix: use structured mention nodes (ADF).
- **Prompts accumulated one-off patches.** Fix: periodic fleet evaluation and merge.

## Evals
`demo/` and `tests/` show the idea: golden fixtures with an expected verdict. The next step is the same approach against the real agents, using recorded transcripts and expected gap lists.
