# Epic Quality Gate - Quick Reference

## 🎯 Purpose
Validate epic readiness before JIRA creation - enforce measurability, completeness, and traceability.

---

## ⚡ Quick Validation Checklist

### ✅ Run Before JIRA Creation
- [ ] All 9 epic sections complete (from Epic Structurer)
- [ ] Original transcript available (for scope drift check)
- [ ] Ready to address issues if validation fails

---

## 📊 Scoring Categories (100 points total)

| Category | Points | Must Have | Auto-Fail If... |
|----------|--------|-----------|-----------------|
| **AC Measurability** | 20 | All AC have numbers/percentages/observables | >20% AC are vague |
| **KPI Definition** | 15 | All 7 columns filled (Target, Baseline, Method, Frequency, Owner, Threshold) | Zero KPIs OR no measurement methods |
| **Analytical Formulas** | 15 | Formulas + data sources + examples (Insights only) | Core metrics lack formulas (analytics epics) |
| **Dependencies** | 15 | All have owner, ETA, impact, mitigation | Critical blockers have no mitigation |
| **Risks** | 15 | All critical/high risks have contingency plans | Critical risks have no contingency |
| **Testability** | 10 | All criteria have verification methods | >30% criteria not testable |
| **Scope Drift** | 10 | Epic matches transcript (or explains deviations) | Critical features missing from epic |

---

## 🚦 PASS/FAIL Thresholds

| Score | Result | Action |
|-------|--------|--------|
| **90-100** | ✅ **PASS (Excellent)** | Proceed to JIRA immediately |
| **80-89** | ✅ **PASS (Good)** | Address minor recommendations, then proceed |
| **70-79** | ⚠️ **CONDITIONAL PASS** | Fix critical issues, document risks, proceed with caution |
| **60-69** | ❌ **FAIL (Needs Work)** | Address all critical feedback before JIRA |
| **<60** | ❌ **FAIL (Major Issues)** | Major rework required, do not proceed |

---

## 🔴 Auto-Fail Conditions (Immediate FAIL)

Regardless of score, epic **FAILS** if ANY of these are true:

| # | Condition | Fix |
|---|-----------|-----|
| 1 | >20% of AC are vague/unmeasurable | Add specific numbers to all AC |
| 2 | Zero KPIs OR all KPIs lack measurement methods | Define 5-10 KPIs with all 7 columns |
| 3 | Critical dependencies have no mitigation plan | Document realistic mitigation for each blocker |
| 4 | Critical risks have no contingency plan | Define what WILL happen if risk occurs |
| 5 | >30% of success criteria cannot be tested | Make all criteria testable with verification method |
| 6 | Critical transcript capabilities missing from epic | Add to In Scope or Out of Scope with rationale |

---

## 🎯 Risk Level Determination

### Risk Factors (Count 0-5)
- [ ] **Dependency Risk:** Critical dependencies ETA >2 weeks OR status "At Risk"
- [ ] **Quality Risk:** >20% AC vague OR >20% KPIs incomplete
- [ ] **Scope Risk:** Scope drift score <5/10
- [ ] **Testability Risk:** >20% criteria not testable
- [ ] **Contingency Risk:** Critical/high risks lack contingency plans

### Risk Levels

| Factors | Level | Recommendation |
|---------|-------|----------------|
| **0-1** | 🟢 **LOW** | Standard monitoring |
| **2** | 🟡 **MEDIUM** | Weekly risk review |
| **3-4** | 🟠 **HIGH** | Daily monitoring, mitigation activation |
| **5+** | 🔴 **CRITICAL** | Do NOT proceed |

---

## 📝 Validation Categories Detail

### 1. AC Measurability (20 points)
**Check:**
- ✅ Zero vague terms without numbers ("fast", "intuitive", "robust" alone)
- ✅ All AC have Given/When/Then structure
- ✅ All AC have verification method (how to test)
- ✅ All AC have success threshold (number, %, or observable)

**Example Fix:**
- ❌ "System should be fast"
- ✅ "P95 latency <2 seconds over 7 consecutive days, verified by APM"

---

### 2. KPI Definition (15 points)
**Check:**
- ✅ 5-10 KPIs defined
- ✅ All 7 columns: Metric Name, Target, Baseline, Method, Frequency, Owner, Threshold
- ✅ Targets are specific (not "improve")
- ✅ Owners are people (not teams)

**Example Fix:**
- ❌ "Improve customer satisfaction"
- ✅ "+10 points (from 72 to 82), measured by post-interaction survey, monthly, Owner: Sarah Johnson, ≥82 for 2 months"

---

### 3. Analytical Formulas (15 points - Insights only)
**Check:**
- ✅ All metrics have formulas documented
- ✅ Data sources identified (table, API)
- ✅ Aggregation methods (SUM, AVG, COUNT, P95)
- ✅ Time windows (daily, weekly, rolling)
- ✅ Filters/conditions (WHERE clauses)
- ✅ Example calculations

**Example Fix:**
- ❌ "Average Resolution Time" (no formula)
- ✅ "AVG(TIMESTAMPDIFF(MINUTE, created_at, resolved_at)) FROM support_tickets WHERE status='resolved' AND created_at >= NOW() - INTERVAL 30 DAY"

**Skip if:** Epic is NOT Insights-related (redistribute 15 points)

---

### 4. Dependencies (15 points)
**Check:**
- ✅ Critical blockers flagged
- ✅ All have: Description, From (person), Status, ETA, Impact, Mitigation
- ✅ Mitigation plans are realistic (not "TBD")
- ✅ Tracking frequency defined

**Example Fix:**
- ❌ "Depends on Data Platform Team"
- ✅ "Data pipeline v3.2 - From: John Smith (PM) - Status: 60% - ETA: Mar 15 - Impact: 6-8 week delay - Mitigation: Weekly sync + backup batch processing plan"

---

### 5. Risks (15 points)
**Check:**
- ✅ 3-5 risks identified
- ✅ All critical/high risks have: Impact, Probability, Mitigation, **Contingency**
- ✅ Risk owners assigned (person)
- ✅ Review frequency for critical/high
- ✅ Contingencies are specific (not "escalate")

**Example Fix:**
- ❌ "AWS accuracy may be low. Mitigation: Test."
- ✅ "AWS accuracy <85% - Impact: Critical - 30% prob - Mitigation: POC in Sprint 1 - **Contingency:** Switch to Azure (2-week delay, already POC'd)"

---

### 6. Testability (10 points)
**Check:**
- ✅ All criteria link to KPI or AC
- ✅ Test scenarios can be written
- ✅ Success thresholds are binary (pass/fail)
- ✅ Verification methods specified
- ✅ Test data requirements identified

**Example Fix:**
- ❌ "User-friendly interface"
- ✅ "80% of users complete task without help in usability test (N=50), measured via task completion tracking"

---

### 7. Scope Drift (10 points)
**Check:**
- ✅ All transcript features in In Scope or Out of Scope
- ✅ No unexplained additions
- ✅ Personas match transcript
- ✅ KPIs align with transcript
- ✅ Risks match concerns raised

**Example Fix:**
- ❌ Transcript discussed "Voice analysis" but not in epic
- ✅ Add to Out of Scope: "Voice analysis - Rationale: Deferred to Phase 2 due to transcription latency"

**Skip if:** No transcript available (redistribute 10 points)

---

## 📤 Output Format Summary

### Report Includes:
1. **Overall Score** (0-100) + PASS/FAIL + Risk Level
2. **Detailed Results** for each 7 categories with issues found
3. **Auto-Fail Triggers** (if any)
4. **Risk Assessment** (factors + level)
5. **Strengths** (3-5 things done well)
6. **Required Fixes** (Critical / Important / Nice-to-Have)
7. **Recommendations** (even if passing)
8. **Final Decision** with next steps

---

## 🔄 Workflow Integration

```
Epic Structurer (creates epic)
↓
Epic Quality Gate ← CHECKPOINT
├─ PASS (≥80) → JIRA Creation → Story Decomposer
└─ FAIL (<80) → Fix Issues → Re-run Quality Gate
```

---

## 💡 Pro Tips

### ✅ Tip 1: Run on Draft Epic
Don't wait until "done" - validate early to catch issues.

### ✅ Tip 2: Aim for 85+
90+ is excellent, 85+ is realistic for first pass.

### ✅ Tip 3: Auto-Fail = Stop Immediately
These are fundamental issues - fix before anything else.

### ✅ Tip 4: Use as Writing Checklist
Reference validation criteria while writing epic to avoid issues.

### ✅ Tip 5: Conditional Pass = Proceed with Caution
Score 70-79 means gaps exist - address before development starts.

### ✅ Tip 6: Insights = Document Formulas
For analytics epics, missing formulas = rework later. Invest time upfront.

---

## 🚨 Common Failures & Quick Fixes

| Failure | Quick Fix |
|---------|-----------|
| Vague AC "fast" | "P95 latency <2s over 7 days via APM" |
| Incomplete KPI | Add all 7 columns: Target, Baseline, Method, Frequency, Owner, Threshold |
| Missing formula | "AVG(column) FROM table WHERE condition" + data source + example |
| No mitigation | "Weekly sync + backup plan: use batch processing" |
| No contingency | "If risk occurs: Switch to Azure API (2-week delay)" |
| Untestable AC | "80% pass in usability test (N=50)" |
| Scope drift | Add to Out of Scope with rationale |

---

## 📊 Example Scores

| Epic Quality | Score | AC Issue | KPI Issue | Result |
|--------------|-------|----------|-----------|--------|
| **Excellent** | 92 | 0% vague | All complete | ✅ PASS - Proceed |
| **Good** | 84 | 5% vague | 1 missing baseline | ✅ PASS - Minor fixes |
| **Conditional** | 76 | 15% vague | 2 incomplete | ⚠️ Fix critical first |
| **Needs Work** | 64 | 25% vague | 4 incomplete | ❌ FAIL - Rework |
| **Major Issues** | 48 | 40% vague | No methods | ❌ FAIL - Major rework |

---

## 📚 See Also

- **[Epic Quality Gate Skill (Full)](epic-quality-gate-skill.md)** - Complete validation guide
- **[Epic Structurer Skill](epic-structurer-skill.md)** - Run this BEFORE quality gate
- **[Story Decomposer Skill](story-decomposer-skill.md)** - Run this AFTER passing quality gate
- **[Workflow Guide](WORKFLOW-GUIDE.md)** - End-to-end process

---

**Last Updated:** March 6, 2026
