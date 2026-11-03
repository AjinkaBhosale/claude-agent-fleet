---
name: epic-quality-gate
description: "Use when validating epic readiness before JIRA creation - enforces measurability, completeness, and traceability standards."
---

# Epic Quality Gate Skill

## Purpose
Validate epic readiness before JIRA creation by enforcing measurability, completeness, and traceability standards.

See **Skill: epic-readiness-gate-conventions** for the shared severity vocabulary (🔴/🟠/🟡/🟢), the risk-level-from-factor-count mapping, and — critically — the mandatory blocking-gate enforcement contract this skill's calling agent must follow on FAIL/auto-fail. This skill defines its own 7 scoring dimensions below; only the surrounding vocabulary/enforcement behavior is shared.

## Execution Logging

See **Hook: Run Logger** at the end of this file for the single, canonical logging location and format — do not maintain a second execution log elsewhere.

---

## Core Validation Categories

### 1. Acceptance Criteria (AC) Measurability
**Requirement:** All AC must have quantifiable success thresholds.

**Validates:**
- ✅ Zero vague terms without quantification (no "fast", "intuitive", "robust" alone)
- ✅ Every AC has Given/When/Then structure
- ✅ Every AC includes verification method (how to test)
- ✅ Every AC has success threshold (specific number, percentage, or observable outcome)
- ✅ All AC are testable (can write pass/fail test case)

**Scoring:**
- 20 points: ALL AC measurable with clear thresholds
- 15 points: 90%+ AC measurable, minor issues
- 10 points: 75-90% AC measurable, some vague terms
- 5 points: 50-75% AC measurable, significant vague language
- 0 points: <50% AC measurable, many vague terms

**Auto-Fail Criteria:**
- More than 20% of AC are vague or unmeasurable

---

### 2. KPI Definition & Measurement
**Requirement:** All success metrics defined with baselines, targets, and measurement methods.

**Validates:**
- ✅ 5-10 KPIs defined (not too few, not too many)
- ✅ All 7 columns filled: Metric Name, Target, Baseline, Measurement Method, Frequency, Owner, Success Threshold
- ✅ Targets are specific numbers/percentages (not "improve" or "increase")
- ✅ Measurement methods are specific (tool name, API, survey, etc.)
- ✅ Owners are named individuals (not teams)
- ✅ Mix of leading (early signals) and lagging (final outcomes) indicators

**Scoring:**
- 15 points: All KPIs complete with all 7 columns, clear measurement methods
- 12 points: KPIs mostly complete, minor gaps (e.g., missing owner on 1-2)
- 8 points: KPIs defined but incomplete (missing baseline or method on multiple)
- 4 points: KPIs vague or missing critical columns (target, measurement)
- 0 points: No KPIs or entirely vague ("improve customer satisfaction")

**Auto-Fail Criteria:**
- Zero KPIs defined, or all KPIs lack measurement methods

---

### 3. Analytical Formulas (Insights Specific)
**Requirement:** For Insights epics, all calculated metrics must have documented formulas.

**Validates:**
- ✅ All dashboard metrics have calculation formulas documented
- ✅ Data sources identified for each metric (table, API, aggregation)
- ✅ Aggregation methods specified (SUM, AVG, COUNT, P95, etc.)
- ✅ Time windows defined (daily, weekly, rolling 30-day, etc.)
- ✅ Filters/conditions documented (e.g., "WHERE status='completed'")
- ✅ Example calculations provided with sample data

**Scoring:**
- 15 points: All metrics have complete formulas with data sources and examples
- 12 points: Most formulas complete, minor gaps (missing data source on 1-2 metrics)
- 8 points: Formulas defined but incomplete (missing aggregation method or filters)
- 4 points: Formulas vague or missing critical details (data source unknown)
- 0 points: No formulas documented, or entirely generic

**Auto-Fail Criteria:**
- Core dashboard metrics lack formulas AND data sources

**Skip Criteria:**
- If epic is NOT Insights-related (non-analytics epic), skip this validation and redistribute 15 points to other categories

---

### 4. Dependencies Documentation
**Requirement:** All critical path and important dependencies identified with mitigation plans.

**Validates:**
- ✅ Critical blockers identified and flagged (RED status)
- ✅ All dependencies have: Dependency description, From (team/person), Status, ETA, Impact if blocked, Mitigation plan
- ✅ Dependency owners are named individuals (not just "Data Platform Team")
- ✅ Mitigation plans are realistic and actionable (not "TBD" or "escalate")
- ✅ Tracking/review frequency defined for critical dependencies
- ✅ External vendor dependencies documented separately

**Scoring:**
- 15 points: All dependencies complete with owners, ETAs, mitigation plans
- 12 points: Dependencies mostly complete, minor gaps (missing ETA on 1-2 non-critical)
- 8 points: Dependencies listed but incomplete (missing mitigation or owner on multiple)
- 4 points: Dependencies vague or incomplete (no owners, no mitigations)
- 0 points: Zero dependencies documented, or all say "TBD"

**Auto-Fail Criteria:**
- Critical blocker dependencies have no mitigation plan

---

### 5. Risks Documentation
**Requirement:** Critical and high risks identified with impact, probability, and contingency plans.

**Validates:**
- ✅ At least 3-5 risks identified (realistic, not exhaustive)
- ✅ All critical/high risks have: Impact level (Critical/High/Medium/Low), Probability (%), Mitigation strategy, Contingency plan (what WILL we do if it happens)
- ✅ Risk owners assigned (person, not team)
- ✅ Review frequency defined for critical/high risks (weekly, bi-weekly)
- ✅ Contingency plans are specific and actionable (not "replan" or "escalate")
- ✅ Risks linked to dependencies where appropriate

**Scoring:**
- 15 points: All critical/high risks have complete mitigation + contingency plans
- 12 points: Risks mostly complete, minor gaps (missing probability % on 1-2 medium risks)
- 8 points: Risks listed but incomplete (missing contingency on critical/high risks)
- 4 points: Risks vague or incomplete (no mitigation or contingency)
- 0 points: Zero risks documented, or all say "TBD"

**Auto-Fail Criteria:**
- Critical risks have no contingency plan (what to do if risk occurs)

---

### 6. Success Criteria Testability
**Requirement:** All success criteria can be objectively verified with pass/fail tests.

**Validates:**
- ✅ Every success criterion links back to a KPI or AC
- ✅ Test scenarios can be written for each criterion (automated or manual)
- ✅ Success thresholds are binary (pass or fail, no ambiguity)
- ✅ Verification methods specified (load test, user study, APM monitoring, etc.)
- ✅ Test data requirements identified (sample size, test duration, environment)
- ✅ Definition of Done includes verification steps

**Scoring:**
- 10 points: All success criteria testable with clear verification methods
- 8 points: Most criteria testable, minor gaps (missing test data requirement)
- 5 points: Criteria defined but verification methods vague or incomplete
- 2 points: Criteria mostly subjective or not testable
- 0 points: No testability consideration, all criteria subjective

**Auto-Fail Criteria:**
- More than 30% of success criteria cannot be objectively tested

---

### 7. Scope Drift Check (Transcript Traceability)
**Requirement:** Epic scope aligns with original discovery meeting transcript (no major additions or omissions).

**Validates:**
- ✅ All features/capabilities discussed in transcript are in "In Scope" or explicitly in "Out of Scope" with rationale
- ✅ No major features added that were NOT discussed in transcript (unless explicitly marked as "Post-Discovery Addition")
- ✅ User personas match roles discussed in meeting
- ✅ KPIs align with success metrics mentioned in transcript
- ✅ Risks in epic match concerns raised in meeting
- ✅ Dependencies in epic align with blockers discussed in meeting

**Scoring:**
- 10 points: Perfect alignment, all transcript items covered, no unexplained additions
- 8 points: Minor alignment issues (1-2 features moved to Out of Scope without clear rationale)
- 5 points: Moderate drift (multiple transcript features missing OR multiple new features added without explanation)
- 2 points: Significant drift (major features missing OR scope expanded significantly)
- 0 points: Epic bears little resemblance to transcript discussion

**Auto-Fail Criteria:**
- Critical capabilities discussed in transcript are missing from epic AND not in Out of Scope
- Major scope expansion (>30% of capabilities were NOT discussed in transcript)

**Skip Criteria:**
- If no transcript available (epic created from other sources), skip this validation and redistribute 10 points

---

## Scoring System

### Total Score Calculation
- **Maximum Score:** 100 points
- **Distribution:**
  - AC Measurability: 20 points
  - KPI Definition: 15 points
  - Analytical Formulas (Insights only): 15 points (or redistributed if N/A)
  - Dependencies: 15 points
  - Risks: 15 points
  - Success Criteria Testability: 10 points
  - Scope Drift Check: 10 points (or redistributed if no transcript)

### PASS/FAIL Thresholds

| Score Range | Result | Meaning | Action |
|-------------|--------|---------|--------|
| **90-100** | ✅ **PASS (Excellent)** | Epic ready for JIRA creation immediately | Proceed to JIRA creation |
| **80-89** | ✅ **PASS (Good)** | Epic ready with minor refinements recommended | Address recommendations, then proceed |
| **70-79** | ⚠️ **CONDITIONAL PASS** | Epic has gaps but may proceed with documented risks | Fix critical issues, document acceptable risks, proceed with caution |
| **60-69** | ❌ **FAIL (Needs Work)** | Significant gaps, epic not ready | Address all critical feedback before JIRA creation |
| **<60** | ❌ **FAIL (Major Issues)** | Epic incomplete or low quality | Major rework required, do not proceed to JIRA |

### Auto-Fail Overrides (Regardless of Score)
Even if score is >70, epic automatically **FAILS** if ANY of these are true:
- ❌ >20% of AC are vague/unmeasurable
- ❌ Zero KPIs defined OR all KPIs lack measurement methods
- ❌ Critical dependencies have no mitigation plan
- ❌ Critical risks have no contingency plan
- ❌ >30% of success criteria cannot be objectively tested
- ❌ Critical transcript capabilities missing from epic (scope drift)

---

## Risk Level Calculation

### Risk Factors
1. **Dependency Risk:** Critical dependencies with ETA >2 weeks in future OR status = "At Risk"
2. **Quality Risk:** >20% of AC vague OR >20% of KPIs incomplete
3. **Scope Risk:** Significant scope drift (score <5/10 on Scope Drift Check)
4. **Testability Risk:** >20% of success criteria not testable
5. **Contingency Risk:** Critical/high risks lack contingency plans

### Risk Level Determination

| Risk Level | Criteria | Impact | Recommendation |
|------------|----------|--------|----------------|
| 🟢 **LOW** | 0-1 risk factors present, score ≥85 | Minimal chance of major issues during execution | Proceed with standard monitoring |
| 🟡 **MEDIUM** | 2 risk factors present, score 70-84 | Moderate chance of delays or quality issues | Enhanced monitoring, weekly risk review |
| 🟠 **HIGH** | 3-4 risk factors present, score 60-69 | High chance of delays, rework, or quality issues | Daily monitoring, mitigation plan activation, consider descoping |
| 🔴 **CRITICAL** | 5+ risk factors OR score <60 OR any auto-fail triggered | Epic likely to fail or require major rework | Do NOT proceed, major fixes required |

---

## Output Format

### Epic Readiness Report

```markdown
# Epic Quality Gate Report
**Epic ID:** [EPIC-ID]
**Epic Title:** [Title]
**Validated On:** [Date]
**Validated By:** Epic Quality Gate Skill v1.0

---

## 📊 Overall Results

| Metric | Value | Status |
|--------|-------|--------|
| **Epic Readiness Score** | [X]/100 | [PASS/FAIL/CONDITIONAL] |
| **Risk Level** | [LOW/MEDIUM/HIGH/CRITICAL] | [🟢/🟡/🟠/🔴] |
| **Result** | [✅ PASS / ⚠️ CONDITIONAL PASS / ❌ FAIL] | |

**Decision:** [PROCEED TO JIRA / FIX ISSUES THEN PROCEED / MAJOR REWORK REQUIRED]

---

## 🔍 Detailed Validation Results

### 1. Acceptance Criteria Measurability (20 points)
**Score:** [X]/20
**Status:** [✅ PASS / ⚠️ WARNING / ❌ FAIL]

**Analysis:**
- Total AC: [N]
- Measurable AC: [M] ([%]%)
- Vague AC: [V] ([%]%)

**Issues Found:**
- [Issue 1: "System should be fast" - Missing quantification]
- [Issue 2: ...]

**Recommendations:**
- [Fix AC #3: Change to "P95 latency <2s"]
- [...]

---

### 2. KPI Definition (15 points)
**Score:** [X]/15
**Status:** [✅ PASS / ⚠️ WARNING / ❌ FAIL]

**Analysis:**
- Total KPIs: [N]
- Complete KPIs (all 7 columns): [M] ([%]%)
- Incomplete KPIs: [I] ([%]%)

**Issues Found:**
- [KPI "Improve CSAT" missing baseline and measurement method]
- [...]

**Recommendations:**
- [Add baseline: Current CSAT = 72]
- [Add measurement: "Post-interaction survey, 5-point scale"]
- [...]

---

### 3. Analytical Formulas (15 points)
**Score:** [X]/15 [OR: N/A - Non-analytics epic]
**Status:** [✅ PASS / ⚠️ WARNING / ❌ FAIL]

**Analysis:**
- Total metrics requiring formulas: [N]
- Complete formulas: [M] ([%]%)
- Missing formulas: [I] ([%]%)

**Issues Found:**
- [Metric "Average Resolution Time" - Formula not documented]
- [Metric "Customer Effort Score" - Data source missing]
- [...]

**Recommendations:**
- [Document formula: AVG(closed_timestamp - created_timestamp) WHERE status='resolved']
- [Specify data source: interactions table, PostgreSQL]
- [...]

---

### 4. Dependencies Documentation (15 points)
**Score:** [X]/15
**Status:** [✅ PASS / ⚠️ WARNING / ❌ FAIL]

**Analysis:**
- Total dependencies: [N]
- Critical blockers: [B]
- Complete dependencies (all fields): [M] ([%]%)
- Incomplete dependencies: [I] ([%]%)

**Issues Found:**
- [Dependency "Data pipeline upgrade" - No mitigation plan]
- [Dependency "AWS API access" - Owner is team, not person]
- [...]

**Recommendations:**
- [Add mitigation: "Use batch processing with 30s delay if pipeline not ready"]
- [Specify owner: "John Smith (Data Platform PM)"]
- [...]

---

### 5. Risks Documentation (15 points)
**Score:** [X]/15
**Status:** [✅ PASS / ⚠️ WARNING / ❌ FAIL]

**Analysis:**
- Total risks: [N]
- Critical/High risks: [H]
- Risks with contingency plans: [M] ([%]%)
- Risks without contingency: [I] ([%]%)

**Issues Found:**
- [Critical Risk "AWS accuracy <85%" - No contingency plan]
- [High Risk "Alert fatigue" - Mitigation vague ("test thoroughly")]
- [...]

**Recommendations:**
- [Add contingency: "Switch to Azure Cognitive Services (2-week delay, already POC'd)"]
- [Improve mitigation: "A/B test thresholds with 2-3 pilot teams, tune based on feedback"]
- [...]

---

### 6. Success Criteria Testability (10 points)
**Score:** [X]/10
**Status:** [✅ PASS / ⚠️ WARNING / ❌ FAIL]

**Analysis:**
- Total success criteria: [N]
- Testable criteria (clear verification): [M] ([%]%)
- Untestable/subjective criteria: [I] ([%]%)

**Issues Found:**
- [Criterion "User-friendly interface" - Subjective, no test method]
- [Criterion "Fast performance" - No verification method specified]
- [...]

**Recommendations:**
- [Make testable: "80% of users complete task without help in usability test (N=50)"]
- [Add verification: "Load test with 1000 sessions, measure P95 latency <2s"]
- [...]

---

### 7. Scope Drift Check (10 points)
**Score:** [X]/10 [OR: N/A - No transcript available]
**Status:** [✅ PASS / ⚠️ WARNING / ❌ FAIL]

**Analysis:**
- Transcript features discussed: [T]
- Features in epic (In Scope): [S]
- Features in Out of Scope (with rationale): [O]
- Missing transcript features: [M]
- Unexplained additions: [A]

**Issues Found:**
- [Transcript discussed "Voice sentiment analysis" but not in epic (neither In Scope nor Out of Scope)]
- [Epic includes "Multi-language support" which was NOT discussed in transcript]
- [...]

**Recommendations:**
- [Add to Out of Scope: "Voice sentiment - Rationale: Deferred to Phase 2 due to transcription latency"]
- [Document: "Multi-language support added post-discovery based on stakeholder request (CEO email March 3)"]
- [...]

---

## ⚠️ Auto-Fail Triggers

[IF ANY AUTO-FAIL TRIGGERED:]
❌ **AUTO-FAIL: Epic cannot proceed regardless of score**

**Triggered Auto-Fail Conditions:**
- [Condition 1: >20% of AC are vague/unmeasurable (actual: 35%)]
- [Condition 2: Critical risk "Data pipeline delay" has no contingency plan]
- [...]

**Required Actions:**
- [Fix all vague AC to include specific numbers/percentages]
- [Document contingency plan for critical risk]

---

[IF NO AUTO-FAIL:]
✅ **No auto-fail conditions triggered**

---

## 🎯 Risk Assessment

**Risk Level:** [🟢 LOW / 🟡 MEDIUM / 🟠 HIGH / 🔴 CRITICAL]

**Risk Factors Present:** [X]/5
1. Dependency Risk: [YES/NO] - [Details]
2. Quality Risk: [YES/NO] - [Details]
3. Scope Risk: [YES/NO] - [Details]
4. Testability Risk: [YES/NO] - [Details]
5. Contingency Risk: [YES/NO] - [Details]

**Impact:** [Description of what risks mean for execution]

**Monitoring Recommendations:**
- [Recommendation 1: Weekly dependency status sync with Data Platform PM]
- [Recommendation 2: Daily monitoring of API latency during first 2 weeks]
- [...]

---

## ✅ Strengths

[List 3-5 things epic does well:]
- [✅ All KPIs have clear measurement methods and baselines]
- [✅ User personas are well-defined with quantified pain points]
- [✅ Success metrics table is comprehensive with all 7 columns]
- [...]

---

## 🔧 Required Fixes (Before JIRA Creation)

[IF FAIL OR CONDITIONAL PASS, list required fixes:]

**Critical (Must Fix):**
1. [Fix vague AC #3, #5, #7 - Add specific thresholds]
2. [Add contingency plan for critical risk "AWS accuracy"]
3. [...]

**Important (Should Fix):**
1. [Specify owner for dependency "Data pipeline upgrade"]
2. [Add measurement method for KPI "Customer Satisfaction"]
3. [...]

**Nice-to-Have (Recommended):**
1. [Add example calculation for "Average Resolution Time" metric]
2. [Document rationale for "Multi-language support" scope addition]
3. [...]

---

## 📝 Recommendations for Improvement

[Suggestions to improve quality, even if passing:]
- [Consider adding leading indicators for churn reduction (e.g., negative sentiment rate)]
- [Add more specific test data requirements (sample size, duration)]
- [Document escalation path for critical dependency delays]
- [...]

---

## 🚦 Final Decision

**Score:** [X]/100
**Result:** [✅ PASS / ⚠️ CONDITIONAL PASS / ❌ FAIL]
**Risk Level:** [🟢 LOW / 🟡 MEDIUM / 🟠 HIGH / 🔴 CRITICAL]

**Recommendation:**
[IF PASS (90-100):]
✅ **PROCEED TO JIRA CREATION**
Epic is high quality and ready for immediate JIRA creation. Address optional recommendations during sprint planning.

[IF PASS (80-89):]
✅ **PROCEED WITH MINOR REFINEMENTS**
Epic is ready for JIRA creation. Recommend addressing [N] recommendations before sprint planning for optimal quality.

[IF CONDITIONAL PASS (70-79):]
⚠️ **PROCEED WITH CAUTION**
Epic has notable gaps but may proceed if timeline is critical. Address all [N] critical fixes before development starts. Document acceptable risks and plan for enhanced monitoring.

[IF FAIL (60-69):]
❌ **DO NOT PROCEED - NEEDS WORK**
Epic has significant gaps. Address all [N] critical fixes and [M] important fixes before JIRA creation. Estimated rework time: [X] hours.

[IF FAIL (<60):]
❌ **DO NOT PROCEED - MAJOR REWORK REQUIRED**
Epic is incomplete or low quality. Major restructuring needed. Recommend re-running Epic Structurer skill or revisiting discovery discussion. Estimated rework time: [X] hours.

**On any FAIL or auto-fail trigger, the calling agent must apply the Blocking-Gate Enforcement Contract from Skill: epic-readiness-gate-conventions** — hard stop (do not proceed to JIRA creation), post a structured comment on the epic tagging the owner via a real ADF `mention` node (not plain `@Name` text), and require either a fix + re-validation or an explicit logged human override before proceeding. This skill scoring FAIL is not itself the enforcement — the calling agent performing the stop-and-notify is.

---

**Next Steps:**
1. [Address all critical fixes]
2. [Re-run quality gate validation]
3. [If score ≥80, proceed to JIRA creation]
4. [If score <80, iterate on fixes]

---

**Report Generated:** [Timestamp]
**Tool Version:** Epic Quality Gate Skill v1.0
```

---

## Validation Process

### Step 1: Gather Inputs
```markdown
Required:
- Complete epic (all 9 sections from Epic Structurer)
- Epic ID and title

Optional but recommended:
- Original discovery meeting transcript (for scope drift check)
- Team context (velocity, capacity) for risk assessment
```

### Step 2: Run Validation Checks
Systematically validate each of 7 categories, scoring 0-[max points] for each.

### Step 3: Calculate Scores
- Total score = sum of all category scores
- Adjust for N/A categories (redistribute points)
- Check auto-fail conditions

### Step 4: Determine Risk Level
- Count risk factors (0-5)
- Map to risk level (Low/Medium/High/Critical)

### Step 5: Generate Report
- Detailed validation results for each category
- Issues found with specific examples
- Recommendations prioritized (Critical/Important/Nice-to-Have)
- Final PASS/FAIL decision with reasoning

### Step 6: Provide Actionable Feedback
- Specific fixes with examples
- Estimated rework time
- Next steps

---

## Integration with Other Skills

### Workflow Position
```
Transcript → [Conversation Extractor] → Structured Data 
→ [Epic Structurer] → Draft Epic 
→ [Epic Quality Gate] ← VALIDATION CHECKPOINT
   ├─ PASS → JIRA Creation → [Story Decomposer] → Stories
   └─ FAIL → Fix Issues → [Re-run Quality Gate]
```

### Before Epic Quality Gate
Run **Epic Structurer** to create formal epic with all 9 sections.

### After Epic Quality Gate
If **PASS**:
1. Create epic in JIRA
2. Run **Story Decomposer** to break into user stories
3. Begin sprint planning

If **FAIL**:
1. Address critical fixes
2. Re-run **Epic Structurer** if major rework needed
3. Re-run **Epic Quality Gate** validation
4. Iterate until PASS

---

## Tips for Success

### 💡 Run Early and Often
Don't wait until "epic is done" to validate. Run quality gate on draft epic to catch issues early.

### 💡 Use as Checklist During Epic Writing
Reference validation criteria while writing epic to avoid common issues.

### 💡 Aim for 85+ Score
90+ is excellent, but 85+ is realistic target for first pass. Iterate to improve.

### 💡 Don't Ignore Conditional Pass Warnings
Score 70-79 means notable gaps exist. Address them before development to avoid rework.

### 💡 Auto-Fail is Serious
If any auto-fail triggered, stop and fix immediately. These are fundamental quality issues.

### 💡 Scope Drift Check Requires Transcript
If no transcript available, redistribute 10 points across other categories. Consider this a risk factor.

### 💡 Insights Formulas are Critical
For analytics epics, missing formulas = major rework later. Invest time upfront to document.

---

## Common Validation Failures & Fixes

### ❌ Failure: Vague Acceptance Criteria (>20%)
**Example Issues:**
- "System should be fast and responsive"
- "User-friendly interface"
- "Robust error handling"

**Fixes:**
- "P95 latency <2 seconds, measured via APM over 7 days"
- "80% of users complete task without help in usability test (N=50)"
- "Zero critical errors in production, <0.1% error rate for non-critical"

---

### ❌ Failure: Incomplete KPIs
**Example Issues:**
- "Improve customer satisfaction" (no target, baseline, or method)
- Missing measurement frequency or owner

**Fixes:**
- Target: +10 points (from 72 to 82)
- Baseline: 72 (current 90-day average)
- Method: Post-interaction CSAT survey (5-point scale)
- Frequency: Monthly average (1st of month)
- Owner: Sarah Johnson (Customer Success Director)
- Threshold: ≥82 for 2 consecutive months

---

### ❌ Failure: Missing Analytical Formulas
**Example Issues:**
- "Average Resolution Time" metric with no formula
- Data source not specified

**Fixes:**
- Formula: `AVG(TIMESTAMPDIFF(MINUTE, created_at, resolved_at))`
- Data Source: `support_tickets` table (PostgreSQL)
- Filter: `WHERE status = 'resolved' AND created_at >= NOW() - INTERVAL 30 DAY`
- Aggregation: Daily average, reported as 30-day rolling average
- Example: If 100 tickets resolved in 30 days with total 50,000 minutes → Avg = 500 min (8.3 hours)

---

### ❌ Failure: Dependencies Without Mitigation
**Example Issues:**
- "Depends on Data Platform Team" (no owner, ETA, or mitigation)

**Fixes:**
- Dependency: Data pipeline upgrade to v3.2 with real-time streaming
- From: John Smith (Data Platform PM)
- Status: In Progress (60% complete)
- ETA: March 15, 2026
- Impact if blocked: Entire epic blocked, 6-8 week delay
- Mitigation: Weekly sync every Monday 10am; Backup plan: Use batch processing with 30s delay (degrades to near-real-time)
- Tracking: `/dashboard/pipeline-status` (updated daily)

---

### ❌ Failure: Risks Without Contingency Plans
**Example Issues:**
- "AWS Comprehend accuracy may be low. Mitigation: Test thoroughly."

**Fixes:**
- Risk: AWS Comprehend accuracy <85% threshold
- Impact: 🔴 Critical - Cannot launch, core requirement not met
- Probability: 30%
- Mitigation: POC testing with 1000 production-like interactions in Sprint 1-2
- **Contingency Plan:** 
  - Option 1: Switch to Azure Cognitive Services (2-3 week delay, already POC'd)
  - Option 2: Hybrid model - use both APIs and average (more expensive, +40% cost)
  - Option 3: Reduce threshold to 80% with business approval

---

### ❌ Failure: Scope Drift
**Example Issues:**
- Transcript discussed "Voice sentiment analysis" but not in epic
- Epic includes "Multi-language support" not discussed in transcript

**Fixes:**
- Add to Out of Scope section: "Voice sentiment analysis - Rationale: MVP focuses chat-only due to complexity of real-time voice transcription + sentiment timing. Voice support requires separate technical spike and is planned for Phase 2 (Q2 2026)."
- Document scope addition: "Multi-language support added post-discovery based on CEO request (email March 3, 2026). Spanish and French are priority based on 15% of customer base being non-English."

---

**Last Updated:** March 6, 2026

---

## Hook: Run Logger

Use the **run-logger** skill's standard format and location — `~/.claude/agents/logs/epic-quality-gate/YYYY-MM-DD-<epic-key>.md` — rather than a bespoke log path. Include the Score/Status/Risk Level/Blocking summary block from **Skill: epic-readiness-gate-conventions** in the log's Output section.
