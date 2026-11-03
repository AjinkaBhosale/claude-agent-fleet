---
name: story-decomposer
description: "Use when breaking a JIRA epic into vertical INVEST user stories with measurable acceptance criteria."
---

# Story Decomposer Skill

## Purpose
Break JIRA epics into vertical user stories that deliver incremental value while following INVEST principles and maintaining measurable acceptance criteria.

## Execution Logging

See **Hook: Run Logger** at the end of this file for the single, canonical logging location and format — do not maintain a second execution log elsewhere.

---

## Core Principles

### 1. Vertical Slicing (Not Horizontal Layers)
✅ **Vertical:** "As a supervisor, I can view real-time sentiment indicator (green/yellow/red) on my dashboard"
- Delivers end-to-end value (UI + API + data)
- User can see and use the feature
- Testable in production

❌ **Horizontal:** "Create sentiment database schema"
- No user value by itself
- Technical task only
- Cannot be demoed to stakeholders

### 2. INVEST Compliance (Mandatory)

| Letter | Principle | Requirement | Example |
|--------|-----------|-------------|---------|
| **I** | Independent | Story can be delivered without other stories being complete first | Story doesn't depend on Story 3 finishing |
| **N** | Negotiable | Implementation details flexible, outcome defined | "Display sentiment" not "Use React component X" |
| **V** | Valuable | Delivers user/business value when deployed | User can accomplish something new |
| **E** | Estimable | Team can estimate effort (size known within range) | Small enough to estimate (not 13+ story points) |
| **S** | Small | Completable in single sprint (typically 1-5 days) | 1-8 story points, fits in 2-week sprint |
| **T** | Testable | Clear acceptance criteria, can verify done | Pass/fail test cases can be written |

### 3. No Technical-Task-Only Stories
Every story must deliver user value. Technical work is embedded in user stories.

❌ **Wrong:** "Set up InfluxDB database"
✅ **Right:** "As a supervisor, I can view sentiment history for past 7 days" (includes setting up InfluxDB as implementation detail)

### 4. Measurable Acceptance Criteria
Same rule as Epic Structurer: NO VAGUE AC. Every AC must have numbers, percentages, or observable outcomes.

---

## Story Template

```markdown
### [STORY-ID] [User Role] - [Action/Capability]

**As a** [user role]  
**I want** [capability]  
**So that** [business value]

**Story Type:** [UI | API | Analytics | Data | Infra | Mixed]

**Story Points:** [1, 2, 3, 5, 8] (Fibonacci)

**Acceptance Criteria:**
1. **Given** [context]  
   **When** [action]  
   **Then** [measurable outcome with specific threshold]
   - **Verify:** [how to test - automated/manual]

2. [Additional AC...]

**Technical Notes:**
- [Implementation hints: APIs to call, data structures, performance targets]
- [Dependencies on infrastructure/platform capabilities]

**Definition of Done:**
- [ ] Code reviewed and merged
- [ ] Unit tests ≥80% coverage
- [ ] AC verified in staging
- [ ] Documentation updated
- [ ] Deployed to production

**Dependencies:**
- [External dependencies if any - with owner and status]

**Risks:**
- [Technical or delivery risks specific to this story]
```

---

## Story Classification System

### 🎨 UI (User Interface)
**Focus:** Frontend changes, user interactions, visual elements

**Typical patterns:**
- Display data in new component/view
- Add button/form/filter to existing page
- Update styling/layout
- Add client-side validation

**Example:** "As a supervisor, I can view real-time sentiment indicator (color-coded badge) on my active interactions panel"

---

### 🔌 API (Backend Services)
**Focus:** Data processing, business logic, integrations

**Typical patterns:**
- New REST/GraphQL endpoint
- Third-party API integration
- Data transformation/calculation
- Authentication/authorization logic

**Example:** "As a system, I can retrieve sentiment scores from AWS Comprehend with P95 latency <500ms"

---

### 📊 Analytics (Reporting & Insights)
**Focus:** Dashboards, reports, metrics, data visualization

**Typical patterns:**
- Add chart/graph to dashboard
- Create new report with filters
- Calculate aggregated metrics
- Export data capability

**Example:** "As a operations manager, I can view weekly sentiment trends by team in analytics dashboard"

---

### 💾 Data (Data Layer)
**Focus:** Schema changes, data migration, storage optimization

**Typical patterns:**
- Database schema updates
- Data migration scripts
- Indexing for performance
- Data retention policies

**Example:** "As a system admin, I can store 90 days of sentiment data with retrieval time <2 seconds for time-series queries"

---

### 🏗️ Infra (Infrastructure & Platform)
**Focus:** DevOps, deployment, monitoring, scalability

**Typical patterns:**
- CI/CD pipeline updates
- Monitoring/alerting setup
- Load balancing/scaling
- Security hardening

**Example:** "As an SRE, I can monitor sentiment API latency with alerts when P95 >2 seconds for 5+ minutes"

---

### 🔀 Mixed (Cross-cutting)
**Focus:** Stories spanning multiple layers (use sparingly)

**When to use:** Feature requires UI + API + Data changes tightly coupled (cannot be split further without losing value)

**Example:** "As a supervisor, I can configure team-level sentiment alert thresholds and see changes reflected in real-time alerts within 10 seconds"

---

## Decomposition Process

### Step 1: Analyze Epic Scope
Review epic sections:
- **User Personas:** Identify all user roles (each may need separate stories)
- **In Scope:** List all capabilities and features
- **Success Metrics:** Identify what needs instrumentation for measurement
- **Acceptance Criteria:** These become story-level AC when decomposed

### Step 2: Identify User Journeys
Map end-to-end user flows:
1. What is the first thing user needs to do?
2. What is the minimum valuable step?
3. What comes next to add value?

**Example (Sentiment Analysis Epic):**
- Journey 1 (Agent): See sentiment indicator → Understand what it means → Adjust behavior
- Journey 2 (Supervisor): Receive alert → View context → Intervene in interaction
- Journey 3 (Admin): Configure thresholds → Monitor adoption → Review metrics

### Step 3: Slice Vertically by User Journey
Each slice delivers end-to-end value for one user journey step.

**Sentiment Analysis Decomposition:**

**Story 1:** "As an agent, I can view real-time sentiment indicator (green/yellow/red badge) on my active chat interaction panel"
- **Type:** Mixed (UI + API)
- **Value:** Agent sees sentiment for first time
- **Includes:** UI component + API integration + mock data for initial release

**Story 2:** "As an agent, I can see sentiment confidence percentage next to indicator for my active interactions"
- **Type:** UI
- **Value:** Agent understands certainty of sentiment
- **Builds on:** Story 1 (incrementally adds detail)

**Story 3:** "As a supervisor, I can receive real-time alert when sentiment drops to Negative ≥70% confidence on any team interaction"
- **Type:** Mixed (UI + API + Data)
- **Value:** Supervisor learns about problems in real-time
- **Includes:** Alert panel UI + WebSocket connection + alert logic + alerting data storage

### Step 4: Apply INVEST Check
For each story, verify:
- ✅ **Independent:** Can be built without waiting for other stories?
- ✅ **Negotiable:** Implementation flexible?
- ✅ **Valuable:** Delivers user value when deployed alone?
- ✅ **Estimable:** Team can estimate size?
- ✅ **Small:** Fits in 1-5 days (1-8 story points)?
- ✅ **Testable:** AC are measurable and testable?

### Step 5: Sequence Stories by Dependency
Order stories front-to-back:
1. **Foundation stories** (infrastructure, core API)
2. **MVP stories** (minimum user value)
3. **Enhancement stories** (additional features)
4. **Optimization stories** (performance, scale)

### Step 6: Classify Each Story
Assign story type: UI, API, Analytics, Data, Infra, Mixed

### Step 7: Add Cross-Story Validation
Check for:
- ❌ **Hidden dependencies:** Story A needs Story B's data structure
- ❌ **Ambiguous boundaries:** Two stories modify same component (merge or clarify)
- ❌ **Technical-only stories:** No user value (merge into user-facing story)
- ❌ **Overly large stories:** >8 story points (split further)

---

## Anti-Patterns (Common Mistakes)

### ❌ Anti-Pattern 1: Horizontal Layer Stories
**Wrong:**
- Story 1: "Create database schema for sentiment data"
- Story 2: "Build sentiment API endpoints"
- Story 3: "Create sentiment UI components"

**Problem:** No story delivers user value. All 3 must complete before user sees anything.

**Right:**
- Story 1: "As an agent, I can view real-time sentiment indicator on my dashboard" (includes DB + API + UI)

---

### ❌ Anti-Pattern 2: Technical Tasks Disguised as Stories
**Wrong:** "Refactor sentiment calculation module for performance"

**Problem:** No user value. Pure technical work.

**Right:** "As a supervisor, I can view sentiment updates with <2 second latency for 1000 concurrent sessions" (forces performance work to deliver user outcome)

---

### ❌ Anti-Pattern 3: Massive "Implement Feature X" Story
**Wrong:** "As a supervisor, I can monitor and manage all sentiment-related activities" (13+ story points)

**Problem:** Too large, not estimable, takes multiple sprints.

**Right:** Break into smaller stories:
- Story A: "View real-time alerts" (3 points)
- Story B: "Configure alert thresholds" (2 points)
- Story C: "View sentiment trend charts" (5 points)

---

### ❌ Anti-Pattern 4: Stories with Hidden Dependencies
**Wrong:**
- Story 1: "Display sentiment indicator" 
- Story 2: "Store sentiment data"
- **Problem:** Story 1 can't work without Story 2, but dependency not documented

**Right:**
- Story 1: "Store and display real-time sentiment data" (combine)
- OR Story 1: "Display sentiment indicator (mock data)" + Story 2: "Integrate live sentiment data" (explicit sequence)

---

### ❌ Anti-Pattern 5: Ambiguous Acceptance Criteria
**Wrong:** "System should respond quickly to sentiment changes"

**Right:** "Sentiment indicator updates within 2 seconds (P95) of sentiment change, verified by load test with 100 concurrent sessions"

---

## Example: Epic → Stories Decomposition

### Input: Epic Scope (Excerpt)
**Epic:** Customer Sentiment Analysis - Real-Time Risk Detection

**In Scope:**
- Real-time sentiment analysis for chat interactions
- Sentiment indicator (3-level: Positive, Neutral, Negative) with confidence %
- Supervisor alert panel with threshold configuration
- Historical sentiment timeline in interaction details

---

### Output: Decomposed Stories

#### 📱 Story 1 (MVP Foundation): Agent Sentiment Indicator
```markdown
### PROJ-123: Agent - View Real-Time Sentiment Indicator

**As an** agent handling customer interactions  
**I want** to see a real-time sentiment indicator (green/yellow/red badge with confidence %) on my active chat panel  
**So that** I can be aware of customer sentiment and adjust my communication approach

**Story Type:** Mixed (UI + API)
**Story Points:** 5

**Acceptance Criteria:**
1. **Given** agent has an active chat interaction  
   **When** customer sends a message with negative sentiment  
   **Then** sentiment indicator updates to RED with confidence % (e.g., "Negative 85%") within 2 seconds (P95 measured)
   - **Verify:** Automated test sends 100 test messages, measures P95 UI update latency <2000ms

2. **Given** sentiment indicator is displayed  
   **When** agent views the badge  
   **Then** color matches sentiment: Green (Positive), Yellow (Neutral), Red (Negative)
   - **Verify:** Manual test with positive/neutral/negative messages confirms color mapping

3. **Given** sentiment shifts during interaction  
   **When** customer tone changes from positive to negative  
   **Then** indicator updates in real-time without page refresh (WebSocket connection)
   - **Verify:** Manual test observes indicator change mid-interaction without reload

**Technical Notes:**
- Integrate with AWS Comprehend API (sentiment analysis)
- Use WebSocket for real-time updates to UI
- Place indicator in interaction panel header (non-intrusive)
- Cache sentiment for 5 seconds to reduce API calls

**Definition of Done:**
- [x] Code merged to main branch
- [x] Unit tests ≥80% coverage (sentiment service + UI component)
- [x] All 3 AC verified in staging with test accounts
- [x] Load test: 100 concurrent agents, P95 latency <2s
- [x] Deployed to production with feature flag (enabled for pilot team only)

**Dependencies:** None (AWS Comprehend access already provisioned)

**Risks:** AWS API latency >500ms would degrade UX (mitigated by caching)
```

---

#### 🔔 Story 2: Supervisor Alert Panel (Core)
```markdown
### PROJ-124: Supervisor - Receive Real-Time Negative Sentiment Alerts

**As a** contact center supervisor  
**I want** to receive real-time alerts when sentiment drops to Negative (≥70% confidence) on any team interaction  
**So that** I can intervene before customer dissatisfaction escalates

**Story Type:** Mixed (UI + API + Data)
**Story Points:** 8

**Acceptance Criteria:**
1. **Given** sentiment analysis detects Negative ≥70% confidence on active team interaction  
   **When** event occurs  
   **Then** alert appears in Supervisor Alert Panel within 5 seconds with: interaction ID, agent name, customer context, current sentiment score, timestamp
   - **Verify:** Automated test triggers negative sentiment, measures alert display latency P95 <5s

2. **Given** supervisor has multiple alerts  
   **When** viewing alert panel  
   **Then** alerts are sorted by timestamp (newest first) and limited to active interactions only (closed interactions removed automatically)
   - **Verify:** Manual test with 10 alerts confirms sort order and auto-removal on interaction close

3. **Given** supervisor clicks on alert  
   **When** "View Interaction" button clicked  
   **Then** system navigates to live interaction detail page within 1 second
   - **Verify:** Manual test measures navigation time <1s for 10 different alerts

**Technical Notes:**
- Store alerts in Redis (in-memory cache) for fast retrieval
- WebSocket push to supervisor UI (no polling)
- Alert auto-expires when interaction ends (status=closed)
- Default threshold: Negative ≥70% (configurable in Story 3)

**Definition of Done:**
- [x] Code merged, unit tests ≥80%
- [x] All AC verified in staging
- [x] Load test: 50 supervisors, 500 interactions, no alert loss
- [x] Monitoring: Alert delivery latency dashboard in Datadog
- [x] Deployed to production

**Dependencies:** Story 1 complete (sentiment data pipeline exists)

**Risks:** 
- WebSocket connection drops may miss alerts (mitigated by connection retry + fallback HTTP polling)
- Alert storm risk if many negative interactions (mitigated by rate limiting: max 50 alerts/supervisor)
```

---

#### ⚙️ Story 3: Configurable Alert Thresholds
```markdown
### PROJ-125: Supervisor - Configure Team-Level Alert Thresholds

**As a** contact center supervisor  
**I want** to configure team-level sentiment alert thresholds (sentiment level + confidence %)  
**So that** I can reduce false positive alerts based on my team's interaction patterns

**Story Type:** UI + API
**Story Points:** 3

**Acceptance Criteria:**
1. **Given** supervisor is on Alert Settings page  
   **When** adjusting threshold slider (0-100% confidence)  
   **Then** new threshold saves and applies to new alerts within 10 seconds, displaying success confirmation message
   - **Verify:** Manual test changes threshold to 80%, confirms new alerts use 80% (not default 70%)

2. **Given** threshold configuration saved  
   **When** viewing current settings  
   **Then** displays: Current threshold (%), Default threshold (70%), Last modified timestamp, Modified by (username)
   - **Verify:** Manual test confirms all 4 fields display correctly

3. **Given** threshold change applied  
   **When** active alerts exist from old threshold  
   **Then** old alerts remain visible + labeled with "(old threshold)", new alerts use new threshold
   - **Verify:** Manual test with alerts spanning threshold change confirms labeling

**Technical Notes:**
- Store threshold in team settings table (PostgreSQL)
- Broadcast threshold change to alert service via Redis pub/sub
- Validate threshold: 50-100% range only (prevent too-sensitive alerts)

**Definition of Done:**
- [x] Code merged, unit tests ≥80%
- [x] All AC verified
- [x] Settings page deployed
- [x] Documentation: "How to Configure Alert Thresholds" guide published

**Dependencies:** Story 2 complete (alert system exists)

**Risks:** None (low-risk configuration feature)
```

---

#### 📊 Story 4: Sentiment History Timeline
```markdown
### PROJ-126: Supervisor - View Sentiment History for Completed Interaction

**As a** supervisor reviewing past interactions  
**I want** to see sentiment timeline chart (line graph) showing how sentiment changed over the conversation  
**So that** I can understand interaction dynamics and coach agents on specific moments

**Story Type:** Analytics + Data
**Story Points:** 5

**Acceptance Criteria:**
1. **Given** completed interaction with sentiment data  
   **When** viewing interaction detail page  
   **Then** sentiment timeline displays as line graph with X-axis=time, Y-axis=sentiment (-1 to +1 scale), color-coded by sentiment (green/yellow/red regions)
   - **Verify:** Manual test with 10 completed interactions confirms chart renders correctly

2. **Given** sentiment timeline displayed  
   **When** hovering over any point on graph  
   **Then** tooltip shows: timestamp, sentiment label (Positive/Neutral/Negative), confidence %, corresponding message text
   - **Verify:** Manual test hovers 5 random points, confirms tooltip data matches interaction transcript

3. **Given** sentiment timeline chart  
   **When** clicking on point  
   **Then** page scrolls to corresponding message in transcript (highlight message for 3 seconds)
   - **Verify:** Manual test clicks 5 points, confirms scroll and highlight behavior

**Technical Notes:**
- Use Chart.js or D3.js for visualization
- Query sentiment data from InfluxDB (time-series database)
- Limit to last 90 days of data (per retention policy)
- Cache rendered chart for 5 minutes (reduce DB load)

**Definition of Done:**
- [x] Code merged, unit tests ≥80%
- [x] All AC verified
- [x] Performance test: Chart renders <2s for 60-min interaction (1000+ messages)
- [x] Deployed to production

**Dependencies:** Story 1 complete (sentiment data stored in InfluxDB)

**Risks:** Large interactions (2+ hours, 2000+ messages) may render slowly (mitigated by downsampling: show 1 data point per 30 seconds for long interactions)
```

---

#### 📈 Story 5: Sentiment Analytics Dashboard
```markdown
### PROJ-127: Operations Manager - View Team Sentiment Trends (Weekly Dashboard)

**As an** operations manager  
**I want** to view weekly sentiment trend dashboard showing % Positive/Neutral/Negative by team  
**So that** I can identify teams needing additional coaching or process improvements

**Story Type:** Analytics
**Story Points:** 5

**Acceptance Criteria:**
1. **Given** operations manager is on Analytics Dashboard  
   **When** selecting "Sentiment Trends" tab  
   **Then** displays: Stacked bar chart with weeks (X-axis), % distribution (Y-axis), color-coded by sentiment, filterable by team (dropdown)
   - **Verify:** Manual test confirms chart displays for last 8 weeks, filters work correctly

2. **Given** dashboard data  
   **When** viewing metrics  
   **Then** displays: Total interactions analyzed, Average sentiment score (numerical), % Negative alerts, Week-over-week trend (up/down arrow + %)
   - **Verify:** Manual test confirms all 4 metrics display with correct calculations (spot-check vs raw data)

3. **Given** dashboard refresh  
   **When** data updates (daily batch job at 2am)  
   **Then** dashboard reflects prior day's data by 3am, displays "Last Updated" timestamp
   - **Verify:** QA checks dashboard at 9am, confirms includes previous day's data + timestamp <3am

**Technical Notes:**
- Batch job aggregates sentiment data from InfluxDB daily
- Store aggregates in PostgreSQL reporting schema
- Dashboard queries PostgreSQL (not real-time InfluxDB)
- Retain 2 years of weekly aggregates

**Definition of Done:**
- [x] Code merged, unit tests ≥80%
- [x] All AC verified
- [x] Batch job tested and scheduled in production (cron: 0 2 * * *)
- [x] Dashboard responsive (loads <3s)
- [x] Deployed to production

**Dependencies:** Story 1 complete (sentiment data available)

**Risks:** None (low-risk reporting feature)
```

---

## Story Sizing Guidelines

### Story Points (Fibonacci Scale)

| Points | Effort | Typical Scope | Example |
|--------|--------|---------------|---------|
| **1** | Few hours | Trivial change, minimal testing | Change label text, update config value |
| **2** | ~1 day | Simple feature, clear implementation | Add new field to form with basic validation |
| **3** | 1-2 days | Small feature with minor complexity | Simple API endpoint + UI integration |
| **5** | 2-4 days | Medium feature, some unknowns | New dashboard with charts + data pipeline |
| **8** | 4-5 days | Complex feature, multiple components | End-to-end user journey with UI + API + data |
| **13+** | >1 week | TOO LARGE - Split into smaller stories | Epic-level work (not a story) |

**Rule:** If story is >8 points, decompose further into smaller stories.

---

## Cross-Story Validation Checklist

After decomposing epic, validate entire story set:

### ✅ INVEST Compliance
- [ ] Every story is **Independent** (can be delivered in any order, minimal dependencies)
- [ ] Every story is **Negotiable** (implementation flexible, not overly prescriptive)
- [ ] Every story is **Valuable** (delivers user value when deployed)
- [ ] Every story is **Estimable** (team can estimate size - not too vague or too large)
- [ ] Every story is **Small** (fits in single sprint, 1-8 points)
- [ ] Every story is **Testable** (measurable AC, clear pass/fail criteria)

### ✅ Vertical Slicing
- [ ] Zero technical-task-only stories (every story has user value)
- [ ] Each story delivers end-to-end value (not just UI layer or API layer)
- [ ] Stories can be demoed to stakeholders individually

### ✅ Measurable AC
- [ ] Zero vague acceptance criteria (no "fast", "intuitive", "robust" without numbers)
- [ ] Every AC has verification method (how to test)
- [ ] Every AC has success threshold (specific number, percentage, or observable outcome)

### ✅ Dependency Management
- [ ] All dependencies explicitly documented in story
- [ ] Dependency owners named (person, not team)
- [ ] No circular dependencies (Story A depends on B, B depends on A)
- [ ] Foundation stories sequenced before dependent stories

### ✅ Classification
- [ ] Every story has type assigned (UI, API, Analytics, Data, Infra, Mixed)
- [ ] "Mixed" used sparingly (only when truly inseparable)

### ✅ Coverage
- [ ] All epic "In Scope" items covered by at least one story
- [ ] All epic personas have stories delivering value to them
- [ ] All epic success metrics have stories instrumenting measurement
- [ ] MVP stories clearly marked (vs post-MVP enhancements)

---

## Output Format

### Summary Table (Story List)

| Story ID | Title | Type | Points | Sprint | Persona | Value |
|----------|-------|------|--------|--------|---------|-------|
| PROJ-123 | Agent - View Sentiment Indicator | Mixed | 5 | Sprint 1 | Agent | See real-time sentiment with confidence % |
| PROJ-124 | Supervisor - Receive Alerts | Mixed | 8 | Sprint 2 | Supervisor | Intervene on negative sentiment within 5s |
| PROJ-125 | Supervisor - Configure Thresholds | UI+API | 3 | Sprint 2 | Supervisor | Reduce false positive alerts |
| PROJ-126 | Supervisor - View History Timeline | Analytics | 5 | Sprint 3 | Supervisor | Understand interaction dynamics for coaching |
| PROJ-127 | Ops Mgr - View Team Trends | Analytics | 5 | Sprint 3 | Ops Manager | Identify teams needing coaching |
| **TOTAL** | **5 stories** | - | **26 points** | **3 sprints** | - | - |

### Detailed Story Backlog
- [Full story details using template format shown above]

---

## Integration with Epic Structurer

**Workflow:**
1. **Epic Structurer** → Creates formal JIRA epic with 9 sections
2. **Story Decomposer** → Breaks epic into vertical stories

## Also used by

This skill's INVEST/vertical-slicing principles and anti-patterns are the canonical decomposition methodology for this fleet, reused (not reimplemented) by:
- **Requirements-Intelligence-Agent** (Step 7, when offering to create stories under an existing epic)
- **requirements-to-stories** (Step 2, when grouping raw requirements into stories with no epic yet)

Those two differ from this skill only in entry point (has-epic vs. no-epic-yet) and in omitting story points by design — they should still apply this skill's quality bar, not a lighter version of it.

**Inputs from Epic:**
- **User Personas** → Each persona gets stories delivering value
- **In Scope** → Capabilities become stories
- **Success Metrics** → Stories must enable metric measurement
- **Acceptance Criteria** → Epic AC decompose into story-level AC
- **Dependencies** → Story dependencies documented explicitly

**Example:**
- Epic AC: "Sentiment displays within 2 seconds for 95% of messages"
- Story AC (Agent Sentiment Indicator): "Sentiment indicator updates within 2 seconds (P95) of sentiment change"

---

## Tips for Success

### 💡 Tip 1: Start with User Journeys
Don't decompose by technical architecture (UI, API, DB). Decompose by user value delivery.

Ask: "What is the smallest thing I can ship that a user will care about?"

### 💡 Tip 2: One User Role per Story (Usually)
Avoid stories like "As an agent OR supervisor..." (too broad)

Split into:
- "As an agent, I can X"
- "As a supervisor, I can Y"

### 💡 Tip 3: Build Incrementally
Story 1: Basic version (MVP)
Story 2: Add detail/refinement
Story 3: Add advanced features

### 💡 Tip 4: Validate with "Demo Test"
Can you demo this story to a stakeholder and they'll understand the value? If not, it's probably too technical or incomplete.

### 💡 Tip 5: Dependencies = Red Flag
If story has many dependencies, consider:
- Combine dependent stories into one larger story
- Re-sequence to remove dependency
- Split story differently to isolate dependency

---

**Last Updated:** March 6, 2026

---

## Hook: Run Logger

Use the **run-logger** skill's standard format and location — `~/.claude/agents/logs/story-decomposer/YYYY-MM-DD-<epic-key>.md` — rather than a bespoke log path.
