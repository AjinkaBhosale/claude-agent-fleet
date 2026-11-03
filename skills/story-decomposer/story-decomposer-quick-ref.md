# Story Decomposer - Quick Reference

## 🎯 Purpose
Break epics into vertical user stories following INVEST principles with measurable acceptance criteria.

---

## ⚡ Quick Process (5 Steps)

### 1. Identify User Journeys
Map end-to-end flows for each persona from epic.

### 2. Slice Vertically
Each story = end-to-end value (UI + API + Data), not just one layer.

### 3. Ensure INVEST
- ✅ **I**ndependent - No blocking dependencies
- ✅ **N**egotiable - Implementation flexible
- ✅ **V**aluable - Delivers user value
- ✅ **E**stimable - Team can size it
- ✅ **S**mall - 1-8 points, fits in sprint
- ✅ **T**estable - Measurable AC

### 4. Add Measurable AC
Given/When/Then with specific thresholds (no vague terms).

### 5. Classify Stories
Assign type: UI, API, Analytics, Data, Infra, Mixed.

---

## 📝 Story Template (Condensed)

```markdown
### [STORY-ID] [User Role] - [Action]

**As a** [role]  
**I want** [capability]  
**So that** [value]

**Type:** [UI|API|Analytics|Data|Infra|Mixed]  
**Points:** [1,2,3,5,8]

**AC:**
1. **Given** [context] **When** [action] **Then** [measurable outcome]
   - Verify: [how to test]

**Tech Notes:** [implementation hints]

**DoD:**
- [ ] Code reviewed, tests ≥80%
- [ ] AC verified in staging
- [ ] Deployed to production

**Dependencies:** [if any]
```

---

## ❌ Anti-Patterns to Avoid

| ❌ Wrong | ✅ Right |
|---------|---------|
| "Create database schema" (technical task) | "As a user, I can view X" (includes DB as implementation) |
| "Refactor module Y" (no user value) | "As a user, I can do X with <2s latency" (forces performance) |
| Horizontal layers (UI story, API story, DB story) | Vertical slices (each story = UI + API + DB) |
| "System should be fast" (vague AC) | "P95 latency <2 seconds" (measurable) |
| 13+ story points (too large) | Split into multiple 3-5 point stories |

---

## 🏷️ Story Classification

| Type | Focus | Example |
|------|-------|---------|
| **🎨 UI** | Frontend, display, user interaction | "View sentiment indicator on dashboard" |
| **🔌 API** | Backend logic, integrations | "Retrieve sentiment from AWS Comprehend API" |
| **📊 Analytics** | Reports, dashboards, metrics | "View weekly sentiment trend chart" |
| **💾 Data** | Schema, storage, migration | "Store 90 days of sentiment data with <2s query time" |
| **🏗️ Infra** | DevOps, monitoring, scale | "Monitor API latency with alerts" |
| **🔀 Mixed** | Spans multiple layers (use sparingly) | "Configure thresholds + see real-time updates" |

---

## 📏 Story Sizing Guide

| Points | Duration | Scope |
|--------|----------|-------|
| **1** | Few hours | Trivial change (label, config) |
| **2** | ~1 day | Simple feature (add form field) |
| **3** | 1-2 days | Small feature (simple API + UI) |
| **5** | 2-4 days | Medium feature (dashboard + data) |
| **8** | 4-5 days | Complex feature (end-to-end journey) |
| **13+** | >1 week | TOO LARGE - Split further |

**Rule:** Stories >8 points must be decomposed.

---

## ✅ Quality Checklist

### Before Marking Story "Ready"
- [ ] INVEST principles satisfied
- [ ] All AC are measurable (no vague terms)
- [ ] Story delivers user value (not just technical task)
- [ ] Story is small (1-8 points, fits in sprint)
- [ ] Dependencies documented with owners
- [ ] Story type classified
- [ ] Can be demoed to stakeholders

### After Decomposing Epic
- [ ] All epic "In Scope" items covered
- [ ] All personas have stories
- [ ] All success metrics have instrumentation stories
- [ ] No circular dependencies
- [ ] Stories sequenced logically (foundation → enhancements)
- [ ] MVP stories clearly marked

---

## 🔄 Integration: Epic → Stories

```
Epic (Epic Structurer output)
↓
Identify User Journeys (per persona)
↓
Slice Vertically (each slice = user value)
↓
Apply INVEST Check
↓
Add Measurable AC
↓
Classify by Type
↓
Validate Cross-Story (dependencies, gaps)
↓
Story Backlog (Ready for Sprint Planning)
```

---

## 💡 Pro Tips

### ✅ Tip 1: Think User Value First
Ask: "Can I demo this to a user and they'll care?" If no → rethink the story.

### ✅ Tip 2: Vertical > Horizontal
❌ Story 1: UI, Story 2: API, Story 3: DB (horizontal layers)
✅ Story 1: Feature A (UI+API+DB), Story 2: Feature B (UI+API+DB)

### ✅ Tip 3: Incremental Delivery
- Story 1: Basic version with core value
- Story 2: Add refinement/detail
- Story 3: Add advanced features

### ✅ Tip 4: One Persona per Story (Usually)
❌ "As an agent OR supervisor..." (too broad)
✅ "As an agent..." (focused on one user role)

### ✅ Tip 5: Dependencies = Warning Sign
Many dependencies? Consider:
- Combine into one story
- Re-sequence to remove dependency
- Split differently

---

## 📊 Example Output: Story Summary Table

| Story ID | Title | Type | Points | Sprint | Value |
|----------|-------|------|--------|--------|-------|
| PROJ-123 | Agent - View Sentiment Indicator | Mixed | 5 | 1 | See real-time sentiment |
| PROJ-124 | Supervisor - Receive Alerts | Mixed | 8 | 2 | Intervene on negative sentiment |
| PROJ-125 | Supervisor - Configure Thresholds | UI+API | 3 | 2 | Reduce false positives |
| PROJ-126 | Supervisor - View History | Analytics | 5 | 3 | Coach based on trends |
| PROJ-127 | Ops Manager - Team Trends | Analytics | 5 | 3 | Identify coaching needs |
| **TOTAL** | **5 stories** | - | **26** | **3** | - |

---

## 📚 See Also

- **[Story Decomposer Skill (Full)](story-decomposer-skill.md)** - Complete skill definition
- **[Epic Structurer Skill](epic-structurer-skill.md)** - Creates epics (runs before story decomposer)
- **[Workflow Guide](WORKFLOW-GUIDE.md)** - End-to-end discovery → epic → stories process

---

**Last Updated:** March 6, 2026
