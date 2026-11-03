---
name: epic-readiness-gate-conventions
description: Shared severity vocabulary, risk-level mapping, and blocking-gate enforcement contract used by every epic-readiness/quality gate in this fleet (epic-quality-gate, sprint-readiness-evaluator, jira-test-plan-and-case-generator's Epic GateKeeper, Requirements-Intelligence-Agent's Quality Gate hook). Reference this instead of restating severity labels or gate-enforcement behavior in each gate's own file.
---

# Epic Readiness Gate — Shared Conventions

This fleet has multiple readiness/quality gates that fire at different points in the epic lifecycle (pre-JIRA-creation, pre-sprint-planning, pre-test-generation, pre-story-creation). **Their scoring dimensions are intentionally NOT unified here** — a pre-JIRA quality check (AC measurability, KPI definitions, analytical formulas) and a pre-sprint Definition-of-Ready check (business value, story sizing, unresolved questions) measure genuinely different things and should keep their own local rubrics. What this skill centralizes is the vocabulary and enforcement behavior every gate should share, so a user moving between gates doesn't hit inconsistent labels or inconsistent "what happens on FAIL" behavior.

**Consumers of this skill:** `epic-quality-gate`, `sprint-readiness-evaluator`, `jira-test-plan-and-case-generator`'s Epic GateKeeper, `Requirements-Intelligence-Agent`'s Quality Gate hook and Epic Readiness Scorer. Each keeps its own dimensions/weights — only the pieces below are shared.

---

## Severity Vocabulary (use these exact labels/emoji everywhere)

| Label | Meaning |
|-------|---------|
| 🔴 Critical | Blocks progress outright — the gate must stop the caller from proceeding |
| 🟠 High | Materially reduces quality/confidence but is not automatically blocking on its own |
| 🟡 Medium | Worth fixing, does not block |
| 🟢 Low | Minor, cosmetic, or nice-to-have |

Every gate's individual findings should be tagged with one of these four, even if the gate's own overall PASS/FAIL band uses different terms (e.g. "NEEDS_WORK", "CONDITIONAL PASS").

## Risk-Level-from-Factor-Count Mapping

When a gate counts discrete risk factors (rather than, or in addition to, a single weighted score) to characterize overall risk:

| Risk Level | Factor Count | Score Correlation (if the gate also produces one) |
|------------|--------------|----------------------------------------------------|
| 🟢 LOW | 0-1 factors | typically ≥85/100 |
| 🟡 MEDIUM | 2 factors | typically 70-84/100 |
| 🟠 HIGH | 3-4 factors | typically 60-69/100 |
| 🔴 CRITICAL | 5+ factors, OR score <60, OR any auto-fail/blocking condition triggered | — |

A gate is free to define its own risk factors (dependency risk, quality risk, scope risk, testability risk, contingency risk, sprint-specific risks, etc.) — only the level names, emoji, and the "5+ or any auto-fail = CRITICAL" override are shared.

## Blocking-Gate Enforcement Contract

**Any gate that can produce a 🔴 Critical / auto-fail / BLOCKED result MUST specify this behavior for its caller, not leave it as an unenforced recommendation:**

1. **Hard stop** — the calling agent does not proceed to the next pipeline step (JIRA creation, sprint planning, test generation, story creation) while a 🔴 Critical/auto-fail condition is open. "Loops back to [prior skill]" is not sufficient on its own — it must also halt forward progress until re-validated.
2. **Notify, don't just log** — post a structured comment on the relevant JIRA issue (epic or story) listing the specific blocking condition(s), tagging the owner. **This comment must use `contentFormat: "adf"` with a real ADF `mention` node** — see `adf-formatter`'s ADF Mentions (CRITICAL) section. A gate result that only appears in chat, or that tags someone with plain `@Name` text or markdown `[~owner]`, has not actually notified anyone.
3. **Re-validation, not silent override** — the only way past a 🔴 Critical/auto-fail result is either (a) fixing the underlying gap and re-running the gate, or (b) an explicit, logged human override — never a quiet "proceed anyway" with no trace.
4. **State the reason in the caller's own output**, not just inside this skill's report — a user reading the calling agent's final summary should see *why* it stopped without having to open a separate report.

## Standard Output Skeleton

Gates are free to design their own detailed report (see each skill's own Output Format), but the top-level summary block should always surface these fields so results are scannable across gates:

```
Score:        [X]/100 (if the gate scores numerically)
Status:       [gate-specific band, e.g. PASS / CONDITIONAL PASS / FAIL / READY / NEEDS_WORK / BLOCKED]
Risk Level:   🟢 LOW / 🟡 MEDIUM / 🟠 HIGH / 🔴 CRITICAL
Blocking:     YES / NO — [if YES, one-line reason]
```

---

## Logging

Gates using this skill should write their run log via the **run-logger** skill's standard location and format (`~/.claude/agents/logs/<gate-name>/YYYY-MM-DD-<epic-key>.md`) rather than a bespoke path — this keeps all gate history discoverable in one place instead of scattered across per-skill custom log directories.
