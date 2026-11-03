---
name: playwright-qa-architect
description: "Single source of truth for Playwright rules: locator strategy, waits, assertions, page-object and test structure, API checklist, code-review checklist. Invoke when writing, reviewing or debugging Playwright tests. Used by the playwright-qa-architect and playwright-pr-reviewer agents. Repo-specific conventions for acme-insights-playwright are at the end and win over generic rules."
---

# Playwright Rules

## Locators (priority order)

1. `data-selector` / `data-testid` — explicit test hooks, most stable
2. `getByRole()` — standard HTML / SSO forms
3. `getByLabel()` — form controls with visible labels
4. `getByText()` — only when text is stable and unique
5. Scoped CSS (component + class) for web components that expose no roles
6. Avoid XPath, bare tags, generated class names, and `nth()` unless order is guaranteed

Web components (UI-lib `ui-*`, Angular Material) often lack ARIA roles / native `disabled`: use `data-selector`, assert disabled via `ng-reflect-disabled="true"` (or `aria-disabled` for Material tabs).

## Waits

| Situation | Use |
|---|---|
| Element will appear | `expect(locator).toBeVisible()` or `waitFor({state:'visible'})` |
| Spinner finishing | `waitFor({state:'hidden'})` |
| Element may be absent | `isVisible()` (returns immediately; never `waitFor` on DOM-absent elements) |
| URL change | `waitForURL('**/glob/**')` — glob strings, never callbacks |
| API-driven UI change | `waitForResponse(...)` paired with the action |

`page.waitForTimeout()` is banned in new code. Only exception: a short pause (animation/debounce) with no observable DOM or network signal — add a one-line comment saying why. Never use it as a substitute for an element wait, and do not use `networkidle`, `force: true` or catch-and-ignore to mask a timing problem.

## Assertions

Specific web-first matchers (`toHaveText`, `toBeVisible`, `toHaveAttribute`, `toHaveCount`, `toHaveURL`…). No `toBeTruthy()`, no assertions swallowed by try/catch, no vacuous tests (action with no assertion). Assert data correctness, not just visibility.

## Structure

- Independent tests by default; use `test.describe.serial` only for genuinely stateful flows (upload → verify → delete), with a `beforeAll` cleanup so state starts empty.
- Page objects: one class per page/component, locators/actions only. Keep assertions in specs (or clearly named `assert*` helpers only if the repo already does so).
- Never commit `.only`; no new `.skip` without a ticket and reason.
- Type returns (`Promise<void>`), `const` over `let`, interfaces for test-data shapes.

## API tests

Validate status codes (success AND error), required fields and types, schema for complex bodies, edge cases (empty/null), error format. Always add negatives: invalid auth, malformed request, missing required fields, wrong types.

## Review checklist (flag these)

- [ ] `waitForTimeout`, `networkidle`, `force: true` without a reason
- [ ] Brittle selectors (`nth`, dynamic IDs, class chains)
- [ ] Missing/weak assertions after actions
- [ ] Hardcoded credentials or env values; login code inside specs
- [ ] Shared mutable state between tests that are not serial by design
- [ ] `.only`, undocumented `.skip`, commented-out tests

## acme-insights-playwright conventions (override the above)

- Auth: global setup only (`authfiles/storageState.json`). Specs use `quickSetup(browser)` in `beforeAll` and `quickCleanup(page)` in `afterAll`. Never log in inside a spec. Shared `beforeAll` state is the repo pattern here.
- Page objects (`src/pages/Insights/`): constructor takes `(page, testRunInfo)`, private readonly fields, **locators only — no assertions, no actions** (actions live in `src/utilities/`). Selectors that vary by env come from `src/test-data/` JSON.
- Titles: `"PROJ-XXXXX: @smoke Description"` (see the test-categorizer skill).
- Navigate with `TabSwitch`, not direct URLs. Multi-locale: `LocaleTestHelper`, reuse existing `storageState-<locale>.json`. Conversational flows: `ConversationPanel` (+ optional `APIResponseHelper`).
- The repo still contains many legacy `waitForTimeout` calls: do not add new ones, and do not mass-rewrite old ones in unrelated PRs.

## acme-webapp-mfe (Angular MFE) conventions

- Login once via `loginAndNavigate(page)` in `beforeAll`; settings tests use `test.describe.serial` with a shared `page` and cleanup loop.
- POMs in `e2e/pageobjects/`; `readonly` Locator fields initialised in the constructor are the pattern there.
- `ui-grid` empty state removes the grid from the DOM → use `isVisible()`. `ui-modal` by `id`. Material tabs: wait for `aria-disabled` to clear before clicking.
- SPA navigation after login: set `window.location.hash`, never `page.goto()` (reload drops the session).
