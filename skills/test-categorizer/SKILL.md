---
name: test-categorizer
description: "Decision framework for tagging Playwright tests as @smoke or @regression (and @flaky) in acme-insights-playwright. Invoke inline when writing, reviewing or re-tagging test cases to pick the right execution tier. Also use when asked which tests should run daily vs weekly."
---

# Test Categorizer

## Tag format (matches the repo's CLAUDE.md — the Xray reporter parses the prefix)

```
"PROJ-XXXXX: @smoke Description"
"PROJ-XXXXX: @regression Description"
```

- The `PROJ-XXXXX:` key MUST come first, followed by the tag, then the description. Never put the tag before the key.
- Tags in use: `@smoke`, `@regression`, `@e2e`, `@voice`, `@flaky`.
- In this repo a test normally carries ONE execution tier tag (`@smoke` or `@regression`); smoke runs daily, regression weekly / pre-release. Check neighbouring specs before adding a second tag — do not assume tags are always paired.

## When @smoke (daily)

Apply if the test covers ANY of:

1. Core user journeys that must always work (feature access, primary workflows)
2. High business impact — failure blocks users or loses revenue
3. Frequently used features (most users, daily)
4. Critical integration health (APIs/services that must be up)
5. Authentication / authorization paths
6. Critical data integrity — core business data saved, retrieved, displayed correctly

## When @regression only (weekly / pre-release)

1. Edge cases and boundary conditions
2. Non-critical secondary features
3. UI/cosmetic validation (layout, formatting)
4. Admin-only / infrequently used functions
5. Regression tests for previously fixed, non-critical bugs
6. Performance under specific conditions (not baseline performance)

## Quality rules

- Keep smoke lean: target under 15–20 minutes total.
- Flaky tests do NOT belong in @smoke until stabilised; tag `@flaky` and fix stability first.
- Long-running tests: try to optimise before putting them in daily smoke.
- A @smoke test that depends on another test's state: the prerequisite must also be @smoke.
- New feature or unclear criticality: ask "if this fails in production, what happens to users?" before tagging.
- Use the Jira ticket (PROJ-XXXXX) for context on feature importance.
- Default priority when it fails: @smoke → High, @regression only → Medium.

## Output format

```
Test: [test name]
Category: Smoke | Regression
Tag: @smoke | @regression
Reasoning: [one sentence]
```
