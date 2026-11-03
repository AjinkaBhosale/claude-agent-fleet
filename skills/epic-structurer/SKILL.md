---
name: epic-structurer
description: "Use when converting extraction/discovery data into a formal, well-structured JIRA Epic with measurable criteria and clear scope."
---

# Epic Structurer Skill

## Purpose
Convert structured extraction data (from conversations, requirements, or discovery sessions) into a formal, well-structured JIRA Epic format with measurable criteria and clear scope definition.

## Execution Logging

**Log key processing steps when using this skill.**

Maintain an execution log that captures:
- Processing step description  
- Input data summary (structured data sections)
- Processing duration
- Output summary (epic sections generated, quality checks)

Save execution log to: `skill-execution-logs/epic-structurer-[TIMESTAMP].log`

**Log Entry Example:**
```markdown
### Epic Structurer Skill Execution
**Timestamp**: 2026-03-06 14:35:00  
**Input**: Structured data with 8 categories populated  
**Processing Duration**: 3.2s  

**Generated Epic Sections**:
- Business Objective: ✅ Complete
- User Personas: ✅ Complete (4 personas)
- Success Metrics: ✅ Complete (7 KPIs with all 7 columns)
- In Scope: ✅ Complete (15 items)
- Out of Scope: ✅ Complete (8 items with rationale)
- Dependencies: ✅ Complete (6 deps with mitigation)
- Risks: ✅ Complete (8 risks, 2 critical with contingency)
- Acceptance Criteria: ✅ Complete (12 AC, all measurable)
- Technical Implementation: ✅ Complete

**Quality Gates**: 9/9 passed  
**NO VAGUE AC Check**: ✅ Passed (0 vague terms found)  
**Result**: ✅ Success  
---
```

## Core Principle
**NO VAGUE ACCEPTANCE CRITERIA ALLOWED**
- ❌ "System should be fast"
- ✅ "System responds within 2 seconds for 95% of requests"
- ❌ "User interface should be intuitive"
- ✅ "New users complete onboarding within 5 minutes without assistance"

## Behavior

### Input Requirements
Accepts structured data containing:
- Business objectives and goals
- User roles and needs
- Technical requirements
- KPIs and metrics
- Dependencies
- Risks
- Scope information (features, constraints)

Can work with:
- Output from Transcript Intelligence skill
- Manual structured input
- JIRA research data
- Requirements documents

### Output Guarantees
Produces a complete Epic structure with:
1. ✅ **Measurable** success metrics (with numbers, thresholds, or observable outcomes)
2. ✅ **Clear** scope boundaries (explicit in/out of scope)
3. ✅ **Specific** acceptance criteria (testable and verifiable)
4. ✅ **Actionable** dependencies and risks
5. ✅ **User-centered** personas and objectives

## Epic Structure Template

### 1. Epic Title
**Format**: `[Capability Name]: [Primary User Benefit]`

**Guidelines:**
- Action-oriented (verb + outcome)
- 5-12 words maximum
- User benefit clear from title
- No jargon or acronyms unless universal

**Examples:**
- ✅ "Customer Sentiment Analysis: Real-Time Risk Detection"
- ✅ "Multi-Channel Dashboard: Unified Agent Experience"
- ❌ "Sentiment Feature" (too vague)
- ❌ "Implement NLP-based customer emotion detection system using AWS Comprehend" (too technical/long)

**Template:**
```
[Capability]: [User Outcome]
```

### 2. Business Objective
**Format**: Clear problem statement + measurable business impact

**Must Answer:**
- **What problem** are we solving?
- **Who** is affected by this problem?
- **Why** is this important now?
- **What value** will this deliver? (quantified if possible)

**Structure:**
```markdown
## Business Objective

**Problem Statement:**
[Current state and pain point - specific and observable]

**Target Outcome:**
[Desired future state - with measurable improvement]

**Business Value:**
- Primary: [Main business metric impact - quantified]
- Secondary: [Supporting benefits - quantified where possible]

**Strategic Alignment:**
[How this supports company/product strategy]
```

**Quality Checks:**
- [ ] Problem is specific and observable
- [ ] Outcome is measurable
- [ ] Business value is quantified
- [ ] Strategic fit is clear

**Example:**
```markdown
## Business Objective

**Problem Statement:**
Contact center supervisors cannot proactively identify at-risk customer interactions during live calls, resulting in missed intervention opportunities and escalations that could have been prevented. Current post-call analysis reveals 30% of churned customers had negative sentiment in their final interaction.

**Target Outcome:**
Enable real-time identification of negative sentiment during live interactions, allowing supervisor intervention before customer dissatisfaction leads to churn. Target 50% reduction in sentiment-related escalations within 6 months.

**Business Value:**
- Primary: Reduce customer churn by 15% through early intervention (estimated $2M annual savings)
- Secondary: Improve CSAT scores by 10 points, reduce escalation handling costs by 20%

**Strategic Alignment:**
Supports FY26 initiative to enhance proactive customer experience management and leverage AI capabilities across the platform.
```

### 3. User Personas
**Format**: Role-based personas with specific needs

**Must Include:**
- Role name and description
- Current pain points (specific, observable)
- Goals and desired outcomes (measurable)
- Success criteria for this persona

**Structure:**
```markdown
## User Personas

### Primary Persona: [Role Name]
**Who they are:** [Brief description of role and responsibilities]

**Current Pain Points:**
- [Specific, observable problem 1 - with context]
- [Specific, observable problem 2 - with context]

**Goals with This Feature:**
- [Measurable goal 1]
- [Measurable goal 2]

**Success Looks Like:**
[Specific, observable outcome that indicates this persona's needs are met]

### Secondary Persona: [Role Name]
[Same structure]
```

**Quality Checks:**
- [ ] Pain points are specific and observable
- [ ] Goals are measurable
- [ ] Success criteria are testable
- [ ] At least one primary persona defined

**Example:**
```markdown
## User Personas

### Primary Persona: Contact Center Supervisor
**Who they are:** Team leaders responsible for monitoring 15-25 agents, ensuring CSAT targets, and intervening in problematic interactions.

**Current Pain Points:**
- Cannot identify negative sentiment interactions in real-time; rely on post-call reports showing 30% of escalations had early warning signs
- Spend 2-3 hours daily reviewing call logs to find issues that already resulted in poor outcomes
- Miss 60% of opportunities to coach agents during difficult calls

**Goals with This Feature:**
- Identify negative sentiment within 10 seconds of occurrence
- Reduce post-incident review time by 50%
- Intervene in 80% of problematic interactions before escalation

**Success Looks Like:**
Supervisor receives real-time alert when sentiment drops, reviews context in under 15 seconds, and intervenes (or coaches agent) within 1 minute, preventing escalation in 70%+ of cases.

### Secondary Persona: Contact Center Agent
**Who they are:** Front-line staff handling 30-50 customer interactions daily across voice and chat channels.

**Current Pain Points:**
- Lack awareness when customer sentiment deteriorates during interaction
- Receive feedback on handling only after call completion (too late to adjust)
- Struggle to gauge emotional state in chat interactions without voice cues

**Goals with This Feature:**
- Receive real-time feedback on customer sentiment during interaction
- Adjust communication approach within same interaction based on sentiment indicators
- Improve personal CSAT scores by 10+ points

**Success Looks Like:**
Agent sees visual sentiment indicator update in real-time (within 2 seconds), recognizes negative trend, and successfully applies de-escalation techniques, resulting in sentiment improvement by end of interaction.
```

### 4. Success Metrics (Measurable)
**Format**: Table of KPIs with targets, baselines, and measurement methods

**Must Be:**
- **Measurable**: Has a number, percentage, threshold, or clear pass/fail
- **Time-bound**: When will we measure this?
- **Baseline-aware**: What's the current state?
- **Achievable**: Is the target realistic?

**Structure:**
```markdown
## Success Metrics

| Metric Name | Target | Baseline | Measurement Method | Measurement Frequency | Owner | Success Threshold |
|-------------|--------|----------|-------------------|----------------------|-------|-------------------|
| [KPI 1] | [Specific target with unit] | [Current value] | [How measured] | [When measured] | [Team/Person] | [When is this "successful"] |

**Leading Indicators** (early signals of success):
- [Measurable indicator 1] - [Target]
- [Measurable indicator 2] - [Target]

**Lagging Indicators** (final outcome measures):
- [Measurable indicator 1] - [Target]
- [Measurable indicator 2] - [Target]
```

**Quality Checks:**
- [ ] Every metric has a specific number or threshold
- [ ] Baseline is documented (or marked "TBD - needs measurement")
- [ ] Measurement method is clear and actionable
- [ ] Success threshold is defined
- [ ] No subjective terms like "better", "faster", "easier" without quantification

**Example:**
```markdown
## Success Metrics

| Metric Name | Target | Baseline | Measurement Method | Measurement Frequency | Owner | Success Threshold |
|-------------|--------|----------|-------------------|----------------------|-------|-------------------|
| Real-time Processing Latency | < 2 seconds | N/A (new feature) | P95 latency from utterance timestamp to UI display | Real-time monitoring | Engineering | 95% of events under 2s for 7 consecutive days |
| Sentiment Accuracy | ≥ 85% | N/A | Comparison vs manual reviewer annotations (sample 200 interactions/week) | Weekly | QA + ML Team | 85% agreement on positive/negative/neutral classification |
| Early Intervention Rate | 70% of negative sentiment interactions | 10% (post-hoc) | (Supervisor interventions within 2 min) / (Total negative sentiment events) | Daily dashboard | Operations | 70% rate sustained for 30 days |
| Churn Reduction (sentiment-related) | 15% reduction | 30% of churned customers had negative final interaction | Monthly churn analysis filtered by sentiment flag | Monthly | Analytics | 15% reduction (from 30% to 25.5% or lower) within 6 months |
| CSAT Improvement | +10 points | 72 (current average) | Standard CSAT survey for interactions with sentiment monitoring | Monthly | Customer Success | Reach 82+ and maintain for 2 consecutive months |
| System Concurrent Capacity | 1,000+ concurrent sessions | N/A | Load testing + production monitoring | Load test pre-release, continuous prod monitoring | Engineering | Handle 1,000 concurrent with <2s latency and 99.9% uptime |

**Leading Indicators** (early signals of success):
- Platform adoption: 80% of supervisors use sentiment alerts daily within 4 weeks of launch
- Alert response time: Supervisors respond to alerts within 90 seconds in 70% of cases
- Agent awareness: 90% of agents report seeing sentiment indicators in post-launch survey

**Lagging Indicators** (final outcome measures):
- Churn reduction: 15% reduction in sentiment-related churn within 6 months
- CSAT improvement: +10 points sustained for 2 months
- Escalation reduction: 50% reduction in sentiment-related escalations within 6 months
```

### 5. In Scope
**Format**: Explicit list of capabilities, features, and deliverables included in this epic

**Guidelines:**
- Be specific about what IS included
- Group by capability area or user flow
- Include MVP vs future considerations
- Reference any existing stories/requirements

**Structure:**
```markdown
## In Scope

### Core Capabilities
- [Specific feature/capability 1 - with brief description]
- [Specific feature/capability 2 - with brief description]

### User Experience
- [Specific UX deliverable 1]
- [Specific UX deliverable 2]

### Technical Implementation
- [Specific technical component 1]
- [Specific technical component 2]

### Data & Analytics
- [Specific data requirement 1]
- [Specific data requirement 2]

### MVP Deliverables (Phase 1)
- [Must-have item 1]
- [Must-have item 2]

### Post-MVP Enhancements (Future)
- [Nice-to-have item 1] - *deferred to Phase 2*
- [Nice-to-have item 2] - *deferred to Phase 2*
```

**Quality Checks:**
- [ ] Each item is specific and actionable
- [ ] MVP vs future is clearly marked
- [ ] No ambiguous terms like "support", "enable", "allow" without specifics
- [ ] Technical and UX scope are both covered

**Example:**
```markdown
## In Scope

### Core Capabilities
- Real-time sentiment analysis for live voice and chat interactions using AWS Comprehend or Azure Cognitive Services
- Sentiment scoring on 3-point scale (Positive, Neutral, Negative) with confidence percentage
- Continuous sentiment tracking throughout interaction lifecycle (updated every 5-10 seconds)
- Alert generation when sentiment drops below configurable threshold

### User Experience
- Real-time sentiment indicator on agent dashboard (color-coded: green/yellow/red with confidence %)
- Supervisor alert panel showing active negative sentiment interactions with context
- Configurable alert thresholds per team (global default: trigger on "Negative" with >70% confidence)
- Historical sentiment timeline view for completed interactions
- Sentiment trend visualization in interaction analytics dashboard

### Technical Implementation
- REST API endpoint for sentiment analysis requests (`POST /api/v1/sentiment/analyze`)
- Integration with Real-Time Analytics engine for live data streaming
- WebSocket connection for real-time sentiment updates to UI
- Sentiment data storage in time-series database (InfluxDB) for historical analysis
- Batch processing job for historical sentiment analysis of past 90 days of interactions

### Data & Analytics
- Sentiment score storage with timestamp, interaction ID, channel, and confidence level
- Aggregate sentiment metrics in daily/weekly/monthly reporting
- Sentiment-tagged interaction records for churn and CSAT correlation analysis
- GDPR-compliant data retention (90 days detailed, 2 years aggregated)

### Compliance & Security
- Data encryption at rest and in transit for sentiment data
- GDPR-compliant data retention and deletion policies
- Audit logging for all sentiment data access
- Role-based access controls (Supervisors: read/configure, Agents: read-only)

### MVP Deliverables (Phase 1)
- Real-time sentiment analysis for chat interactions (voice in Phase 2)
- Basic 3-level sentiment indicator on agent UI
- Supervisor alert panel with threshold configuration
- 30-day historical storage and basic reporting
- Integration with AWS Comprehend

### Post-MVP Enhancements (Future)
- Voice interaction sentiment analysis - *Phase 2 post-MVP*
- Multi-language sentiment support (currently English only) - *Phase 3*
- Emotion detection (angry, frustrated, delighted) beyond positive/neutral/negative - *Phase 3*
- Predictive churn modeling based on sentiment patterns - *Phase 4*
- Agent coaching recommendations based on sentiment trends - *Phase 4*
```

### 6. Out of Scope
**Format**: Explicit list of what is NOT included to prevent scope creep

**Guidelines:**
- Be as specific as in-scope items
- Explain WHY something is out of scope
- Note if it's "never" vs "not now"
- Reference future epics if applicable

**Structure:**
```markdown
## Out of Scope

### Explicitly Excluded (Not in This Epic)
- [Specific item 1] - *Rationale: [why it's excluded]*
- [Specific item 2] - *Rationale: [why it's excluded]*

### Future Considerations (Separate Epics)
- [Item 1] - *See: [Future Epic ID or Initiative]*
- [Item 2] - *See: [Future Epic ID or Initiative]*

### Assumptions (Not Delivered by This Team)
- [Item 1 handled by another team] - *Dependency on: [Team/Epic]*
- [Item 2 already exists] - *Provided by: [System/Team]*

### Intentional Limitations (MVP)
- [Limitation 1] - *Will be addressed in: [Phase 2 or future epic]*
- [Limitation 2] - *Will be addressed in: [Phase 2 or future epic]*
```

**Quality Checks:**
- [ ] Items are specific (not generic "advanced features")
- [ ] Rationale is provided for each exclusion
- [ ] Future path is indicated where applicable
- [ ] Prevents predictable scope creep questions

**Example:**
```markdown
## Out of Scope

### Explicitly Excluded (Not in This Epic)
- **Voice interaction sentiment analysis** - *Rationale: MVP focuses on chat only due to complexity of voice transcription + sentiment timing. Voice support planned for Phase 2 (Q2 2026)*
- **Multi-language sentiment support** - *Rationale: English-only for MVP. Multi-language requires separate ML models and adds 3x cost. Future enhancement if demand exists*
- **Automated response recommendations** - *Rationale: Beyond sentiment detection. Requires separate AI capability. See future "Agent Assist" initiative*
- **Root cause analysis of negative sentiment** - *Rationale: This is descriptive analytics; root cause requires separate analytical capability and data science work*
- **Customer journey sentiment mapping** - *Rationale: Requires cross-interaction correlation and customer data platform integration. Separate epic planned for Q3 2026*
- **Integration with external CRM systems** - *Rationale: External integrations require separate API gateway work and partner certifications. Not needed for MVP*

### Future Considerations (Separate Epics)
- **Emotion detection beyond sentiment** (angry, frustrated, delighted) - *See: Future "Advanced Emotion AI" epic - pending ML team capacity*
- **Predictive churn modeling based on sentiment** - *See: "Predictive Analytics Platform" initiative - Q4 2026*
- **Agent performance insights based on sentiment trends** - *See: Future "Quality Management Enhancement" epic*
- **Sentiment-based automatic call routing** - *See: "Intelligent Routing" epic - Q3 2026*

### Assumptions (Not Delivered by This Team)
- **Real-Time Analytics engine availability** - *Dependency on: Platform Team's "Real-Time Streaming" epic (in progress, ETA March 2026)*
- **Data pipeline upgrade** - *Dependency on: Data Platform Team (BLOCKER - must complete before this epic starts)*
- **Agent dashboard infrastructure** - *Provided by: UI Platform Team - already exists, we add sentiment component only*
- **Time-series database (InfluxDB)** - *Provided by: Infrastructure Team - already provisioned*

### Intentional Limitations (MVP)
- **Sentiment history limited to 30 days detailed** (vs 90+ days) - *Cost optimization for MVP. Will extend to 90 days in Phase 2 if storage costs are manageable*
- **No mobile app sentiment display** - *Web only for MVP. Mobile support in Phase 2 (Q2 2026) pending mobile platform updates*
- **Manual threshold configuration only** - *No ML-based automatic threshold optimization in MVP. Phase 3 enhancement if data supports it*
- **Basic 3-level sentiment** (positive/neutral/negative) - *No granular 5 or 7-point scale. Simplicity for MVP. Phase 3 if users need finer granularity*
- **Aggregate reporting only** (no drill-down to individual interactions) - *MVP dashboards show trends only. Detailed drill-down in Phase 2*
```

### 7. Dependencies
**Format**: Structured dependency matrix with ownership and status

**Must Include:**
- What we depend on (specific deliverable)
- Who/what provides it
- Current status
- Impact if blocked
- Mitigation plan

**Structure:**
```markdown
## Dependencies

### Critical Path Dependencies (Blockers)
| We Need | From | Status | ETA | Impact if Blocked | Mitigation | Owner |
|---------|------|--------|-----|-------------------|------------|-------|
| [Specific deliverable] | [Team/System] | [Status] | [Date] | [What gets blocked] | [Backup plan] | [Name] |

### Important Dependencies (Non-Blocking)
| We Need | From | Status | ETA | Impact if Delayed | Mitigation | Owner |
|---------|------|--------|-----|-------------------|------------|-------|
| [Specific deliverable] | [Team/System] | [Status] | [Date] | [Impact] | [Backup plan] | [Name] |

### External Dependencies
- [External service/API] - [Status and risk level]
- [Third-party integration] - [Status and risk level]

### Dependency Management Plan
- **Tracking**: [How dependencies are monitored]
- **Escalation**: [Process if dependency is at risk]
- **Communication**: [Sync frequency with dependency owners]
```

**Quality Checks:**
- [ ] Each dependency is specific (not "need platform team")
- [ ] Status is current and tracked
- [ ] Impact is clear and quantified
- [ ] Mitigation exists for critical dependencies
- [ ] Owner is assigned for tracking each dependency

**Example:**
```markdown
## Dependencies

### Critical Path Dependencies (Blockers)
| We Need | From | Status | ETA | Impact if Blocked | Mitigation | Owner |
|---------|------|--------|-----|-------------------|------------|-------|
| Data pipeline upgrade (v3.2 with real-time streaming) | Data Platform Team (EPIC-789) | In Progress (60% complete) | March 15, 2026 | Cannot process live sentiment data; entire epic blocked | Emergency: Use batch processing only (degrades to near-real-time with 30s delay) | John Smith (Data Platform PM) |
| Real-Time Analytics engine API access | Platform Team | Done (deployed Feb 28) | Complete | Would block WebSocket sentiment updates | N/A - Already complete | Sarah Lee (Platform Lead) |
| AWS Comprehend API production access + budget approval | Finance + Cloud Operations | Pending Approval | March 10, 2026 | Cannot call sentiment API; blocks all testing beyond dev | Use Azure Cognitive Services as backup (requires 2-week integration work) | Mike Chen (FinOps) |

### Important Dependencies (Non-Blocking)
| We Need | From | Status | ETA | Impact if Delayed | Mitigation | Owner |
|---------|------|--------|-----|-------------------|------------|-------|
| InfluxDB time-series database provisioning | Infrastructure Team | Scheduled | March 20, 2026 | Historical analysis delayed by 2 weeks | Use PostgreSQL with TimescaleDB extension temporarily (migration needed later) | DevOps Team |
| Agent dashboard component framework update | UI Platform Team | In Progress | March 18, 2026 | Sentiment indicator UI work delayed; adds 1 week to timeline | Build custom component if not ready (technical debt) | Emily Zhang (UI Platform) |
| GDPR compliance review for sentiment data retention | Legal/Compliance | Not Started | April 1, 2026 | Cannot launch to EU customers; US-only launch if delayed | Document retention policy proactively for faster review; plan US-first rollout | Legal Team |

### External Dependencies
- **AWS Comprehend API** (External SaaS) - Risk: Medium
  - Status: Vendor relationship established, pilot access approved
  - Risk: API rate limits or pricing changes; Mitigation: Azure Cognitive Services as backup
  - Contact: AWS Account Manager (Jane Doe, jane.doe@aws.com)

- **Azure Cognitive Services API** (Backup External SaaS) - Risk: Low
  - Status: POC completed, can activate if needed
  - Risk: Switching mid-project adds 2-week delay; Mitigation: Parallel development approach
  - Contact: Azure Account Manager (Bob Wilson, bob.wilson@microsoft.com)

### Dependency Management Plan
- **Tracking**: Weekly dependency status sync every Monday with all dependency owners; Status updates in shared dashboard (link: /dashboard/dependencies)
- **Escalation**: If dependency slips >1 week from ETA, escalate to Director level within 24 hours; Business continuity plan triggered if critical dependency at risk
- **Communication**: Bi-weekly stakeholder updates via email; Slack channel #epic-sentiment-dependencies for real-time coordination
- **Risk Monitoring**: Dependency risk reviewed in every sprint planning; Red/Yellow/Green status indicators updated weekly
```

### 8. Risks
**Format**: Risk register with mitigation and contingency plans

**Must Include:**
- Specific risk description
- Category and impact level
- Probability assessment
- Mitigation strategy
- Contingency plan if risk occurs
- Owner for monitoring

**Structure:**
```markdown
## Risks

### Critical Risks (High Impact + High Probability)
| Risk | Impact | Probability | Mitigation Strategy | Contingency Plan | Status | Owner |
|------|--------|-------------|---------------------|------------------|--------|-------|
| [Specific risk] | [Quantified impact] | [%] | [Preventive actions] | [If it happens, then...] | [Status] | [Name] |

### High Risks (Requires Active Management)
[Same table structure]

### Medium Risks (Monitor)
[Same table structure]

### Risk Management Plan
- **Review Frequency**: [How often risks are reviewed]
- **Escalation Triggers**: [When to escalate]
- **Risk Owners**: [Who monitors each risk category]
```

**Quality Checks:**
- [ ] Risks are specific, not generic ("technical issues")
- [ ] Impact is quantified (cost, timeline, quality)
- [ ] Mitigation is actionable (not "be careful")
- [ ] Contingency plan exists for critical risks
- [ ] Risk status is tracked

**Example:**
```markdown
## Risks

### Critical Risks (High Impact + High Probability)
| Risk | Impact | Probability | Mitigation Strategy | Contingency Plan | Status | Owner |
|------|--------|-------------|---------------------|------------------|--------|-------|
| Data pipeline dependency blocked or delayed beyond April 1 | Epic blocked entirely; 6-8 week delay; miss Q1 commitment | 40% | Weekly status sync with Data Platform PM; Executive escalation path prepared; Buffer 2 weeks in timeline | Switch to batch-only processing (30s delay vs real-time); Launch with degraded performance, upgrade when pipeline ready | Active - Tracking Weekly | PM - John Doe |
| AWS Comprehend accuracy below 85% threshold | Core requirement not met; may need to switch APIs (4-week delay); or reduce accuracy target (business impact) | 30% | POC testing with production-like data (1000 sample interactions) before full build; Accuracy tested in Sprint 2 | Switch to Azure Cognitive Services (2-week delay); Or reduce threshold to 80% with business approval; Or hybrid model (more expensive) | Mitigating - POC in progress | ML Engineer - Sarah Lee |

### High Risks (Requires Active Management)
| Risk | Impact | Probability | Mitigation Strategy | Contingency Plan | Status | Owner |
|------|--------|-------------|---------------------|------------------|--------|-------|
| False positive rate >20% causing alert fatigue | Supervisors ignore alerts; Feature adoption <50%; Business value not realized | 50% | Tune confidence thresholds during beta; A/B test different alert configurations; Pilot with 2-3 teams before rollout | Add manual feedback loop for supervisors to mark false positives; ML team retrains model; Temporary increase threshold (fewer alerts but higher precision) | Mitigating - Beta plan includes tuning | QA Lead - Mike Chen |
| API costs exceed budget by 30%+ | Budget approval needed mid-project (2-3 week delay); Or forced to reduce concurrent capacity | 35% | Detailed cost modeling in Sprint 1; Usage-based circuit breaker in architecture; Pilot with 100 users to validate cost model | Reduce concurrent capacity from 1000 to 500 sessions; Implement API call caching (30% cost reduction); Request additional budget | Mitigating - Cost model in progress | Tech Lead - Emily Zhang |
| GDPR review identifies compliance gaps | Cannot launch to EU customers (30% of user base); US-only launch reduces business value by 40% | 25% | Early Legal engagement (starting March); Document retention policy proactively; GDPR-by-design approach | US-only launch initially; EU launch deferred to Phase 2 (Q2); Business accepts reduced initial value | Monitoring - Legal sync scheduled | Compliance - Legal Team |
| Real-time latency >2 seconds under load | Core UX requirement not met; Supervisors see stale data; Feature not useful for intervention | 30% | Performance testing in Sprint 3 (before UI work); Load testing with 1500 concurrent (150% capacity); Architecture review with Platform team | Reduce concurrent capacity to 700 (meets latency); Or switch to near-real-time (5s delay, lower UX but acceptable); Or phase rollout (limit to key teams initially) | Mitigating - Perf test planned Sprint 3 | Tech Lead - Emily Zhang |

### Medium Risks (Monitor)
| Risk | Impact | Probability | Mitigation Strategy | Contingency Plan | Status | Owner |
|------|--------|-------------|---------------------|------------------|--------|-------|
| Team velocity 20% below planned | 2-week timeline slip; miss end-of-Q1 target | 40% | Sprint velocity tracking; Buffer built into timeline (2 weeks); Daily standups to identify blockers early | Descope post-MVP enhancements; Launch with MVP only; Move 2 nice-to-have stories to Phase 2 | Monitoring - Tracking velocity | Scrum Master |
| AWS/Azure API service interruption | Sentiment analysis unavailable during outage; Supervisors lack real-time data | 15% | Multi-region API deployment; Automatic failover between AWS/Azure; 99.9% SLA from vendors | Graceful degradation: System continues without sentiment; Alert supervisors of outage; Batch process post-outage | Accepted - SLA acceptable | DevOps Team |
| Historical batch processing takes >24 hours | Reporting data delayed; Analytics insights not timely | 20% | Performance testing batch job with 90-day dataset; Optimize queries; Consider incremental processing | Run batch processing over weekend only; Accept 1-week delay for historical analysis; Or reduce history to 30 days | Monitoring - Will test Sprint 4 | Data Engineer |

### Risk Management Plan
- **Review Frequency**: 
  - Critical risks: Reviewed weekly in core team sync + documented status update
  - High risks: Reviewed bi-weekly in sprint planning
  - Medium risks: Reviewed monthly or when status changes
  
- **Escalation Triggers**: 
  - Critical risk probability increases above 50%: Escalate to Director immediately
  - High risk materializes: Escalate to PM and discuss contingency activation
  - Any risk blocks sprint goal: Escalate in daily standup
  
- **Risk Owners**: 
  - Technical risks: Tech Lead (Emily Zhang)
  - Dependency risks: PM (John Doe)
  - Compliance risks: Legal liaison + PM
  - Business risks: Product Owner (Jane Smith)
  
- **Monitoring**:
  - Risk dashboard updated weekly: [link to dashboard]
  - Risk register reviewed in every sprint retro
  - Contingency plans tested in disaster recovery exercises (quarterly)
```

### 9. Acceptance Criteria (Measurable)
**Format**: Testable, verifiable, measurable criteria that define "done"

**CRITICAL RULES:**
- ❌ **NEVER use vague terms**: "system should be fast", "UI should be intuitive", "good performance"
- ✅ **ALWAYS use measurable terms**: numbers, percentages, thresholds, observable outcomes
- ✅ **ALWAYS describe how to test**: verification method must be clear
- ✅ **ALWAYS link to success metrics**: AC should roll up to success metrics

**Structure:**
```markdown
## Acceptance Criteria

### Functional Criteria

#### 1. [Capability Name]
**Acceptance Criterion:**
Given [precondition]
When [action]
Then [measurable outcome]

**Verification Method:** [How to test this]
**Success Threshold:** [Pass/fail criteria with numbers]
**Links to Success Metric:** [Which KPI this supports]

---

#### 2. [Next Capability]
[Same structure]

### Non-Functional Criteria

#### Performance
- [Measurable performance criterion 1]
  - **Measured by:** [Tool/method]
  - **Pass criteria:** [Specific threshold]
  
#### Scalability
[Same structure]

#### Security
[Same structure]

#### Compliance
[Same structure]

### Definition of Done Checklist
- [ ] All functional AC verified in staging environment
- [ ] All non-functional AC verified via automated tests
- [ ] Performance benchmarks met for 7 consecutive days  
- [ ] Security scan passed with zero critical vulnerabilities
- [ ] Documentation complete and reviewed
- [ ] Monitoring and alerts configured
- [ ] Rollback plan tested
- [ ] Success metrics baseline captured
```

**Quality Checks for Each AC:**
- [ ] Contains specific numbers, percentages, or thresholds
- [ ] Describes HOW to verify (test method)
- [ ] Links to at least one success metric
- [ ] Is independently testable
- [ ] Pass/fail is unambiguous
- [ ] Does NOT use words like: "intuitive", "fast", "easy", "user-friendly", "robust", "efficient" without quantification

**Examples:**

**❌ Bad Acceptance Criteria (Vague):**
```markdown
- System should provide real-time sentiment analysis
- UI should be intuitive for supervisors
- Performance should be good under load
- System should handle errors gracefully
```

**✅ Good Acceptance Criteria (Measurable):**
```markdown
## Acceptance Criteria

### Functional Criteria

#### 1. Real-Time Sentiment Analysis Processing
**Acceptance Criterion:**
Given an active chat interaction with a customer
When customer sends a message
Then sentiment score (Positive/Neutral/Negative + confidence %) is calculated and displayed on agent dashboard within 2 seconds for 95% of messages

**Verification Method:** 
- Automated test: Send 1000 test messages across 100 concurrent sessions
- Measure timestamp delta between message received and sentiment displayed in UI
- Calculate P95 latency

**Success Threshold:** 
- P95 latency < 2 seconds (95th percentile under 2000ms)
- P99 latency < 3 seconds (worst case acceptable)
- Zero timeouts or errors

**Links to Success Metric:** "Real-time Processing Latency" KPI (< 2 seconds target)

---

#### 2. Supervisor Alert Generation
**Acceptance Criterion:**
Given sentiment score drops to "Negative" with confidence ≥70%
When this occurs during an active interaction
Then supervisor alert appears in Supervisor Alert Panel within 5 seconds with interaction ID, agent name, customer context, and current sentiment score

**Verification Method:**
- Test script simulates negative sentiment event
- Measure time from sentiment API response to alert visible in supervisor UI
- Verify all required data fields present in alert

**Success Threshold:**
- 100% of negative sentiment events generate alert
- Alert display latency P95 < 5 seconds
- Alert contains all 5 mandatory fields: interaction ID, agent name, customer name/ID, sentiment score, timestamp

**Links to Success Metric:** "Early Intervention Rate" KPI (enables 70% intervention target)

---

#### 3. Sentiment Accuracy
**Acceptance Criterion:**
Given a dataset of 200 chat interactions manually annotated by 3 human reviewers (ground truth)
When sentiment analysis is performed on these interactions
Then system classification (Positive/Neutral/Negative) matches ground truth with ≥85% accuracy

**Verification Method:**
- QA team prepares 200-interaction test set with ground truth labels (inter-reviewer agreement ≥90%)
- Run interactions through sentiment API
- Calculate accuracy: (correct classifications / total classifications) * 100

**Success Threshold:**
- Overall accuracy ≥ 85%
- Per-class accuracy (Positive, Neutral, Negative) ≥ 80% each
- False positive rate for "Negative" < 20% (to minimize alert fatigue)

**Links to Success Metric:** "Sentiment Accuracy" KPI (≥85% target)

---

#### 4. Concurrent Capacity
**Acceptance Criterion:**
Given 1000 concurrent active chat sessions
When all sessions generate sentiment analysis requests (1 message per 30 seconds avg)
Then system processes all requests with P95 latency <2 seconds and 99.9% success rate

**Verification Method:**
- Load testing with 1000 simulated concurrent sessions using JMeter
- Each session sends messages at realistic intervals (30-60 second variance)
- Monitor for 1-hour sustained load test

**Success Threshold:**
- All 1000 concurrent sessions process successfully
- P95 latency remains < 2 seconds throughout test
- API success rate ≥ 99.9% (max 10 failures per 10,000 requests)
- No system crashes or degradation
- CPU utilization < 70%, Memory < 80%

**Links to Success Metric:** "System Concurrent Capacity" KPI (1,000+ concurrent target)

---

#### 5. Configurable Alert Thresholds
**Acceptance Criterion:**
Given a supervisor with admin permissions
When supervisor navigates to Settings > Sentiment Alerts
Then supervisor can configure alert threshold (Positive/Neutral/Negative + confidence %) per team, and changes take effect within 10 seconds for new interactions

**Verification Method:**
- Manual test: Supervisor logs in, navigates to settings
- Change threshold from "Negative ≥70%" to "Negative ≥80%"
- Trigger test interaction with sentiment "Negative 75%"
- Verify alert does NOT fire (threshold now 80%)
- Trigger test interaction with sentiment "Negative 85%"
- Verify alert DOES fire

**Success Threshold:**
- Setting UI renders without errors
- Threshold changes persist (reload page, setting retained)
- Changes apply within 10 seconds (no alert for 75%, alert for 85%)
- Audit log records threshold change with user ID and timestamp

**Links to Success Metric:** "Platform adoption" leading indicator (supervisors can customize for their teams)

### Non-Functional Criteria

#### Performance
- **AC-NF-1: API Response Time**
  - **Criterion:** Sentiment analysis API endpoint (`POST /api/v1/sentiment/analyze`) responds in <500ms for P95 of requests under normal load (500 concurrent)
  - **Measured by:** API performance monitoring (Datadog or New Relic); Load testing with JMeter
  - **Pass criteria:** P95 < 500ms, P99 < 1000ms over 7-day period post-launch

- **AC-NF-2: Database Query Performance**
  - **Criterion:** Historical sentiment queries (last 30 days) return results in <3 seconds for P95 of queries
  - **Measured by:** Database query monitoring; InfluxDB query metrics
  - **Pass criteria:** P95 query time < 3 seconds with 1M+ records

#### Scalability
- **AC-NF-3: Horizontal Scaling**
  - **Criterion:** System automatically scales to handle 50% surge in concurrent load (from 1000 to 1500 sessions) within 2 minutes without manual intervention
  - **Measured by:** AWS Auto Scaling metrics; Load test with staged traffic increase
  - **Pass criteria:** Auto-scaling triggers at 70% CPU; New instances healthy within 2 minutes; Latency remains <2s during scale-up

#### Security
- **AC-NF-4: Data Encryption**
  - **Criterion:** All sentiment data encrypted at rest (AES-256) and in transit (TLS 1.2+)
  - **Measured by:** Security scan; SSL Labs test; AWS S3 encryption verification
  - **Pass criteria:** Zero unencrypted sentiment data found in security audit; SSL Labs rating A+

- **AC-NF-5: Role-Based Access Control**
  - **Criterion:** Agents can view sentiment for their own interactions only; Supervisors can view for their team; Admins can view all
  - **Measured by:** Penetration testing; Manual RBAC test cases
  - **Pass criteria:** 100% of unauthorized access attempts blocked; Zero privilege escalation vulnerabilities

#### Compliance
- **AC-NF-6: GDPR Data Retention**
  - **Criterion:** Detailed sentiment data (per-interaction) deleted after 90 days; Aggregated sentiment (anonymized) retained for 2 years; Deletion verifiable via audit log
  - **Measured by:** Automated retention policy test; Audit log review
  - **Pass criteria:** Zero records older than 90 days in detailed storage; Automated deletion job runs daily with 100% success rate; Audit trail for all deletions

- **AC-NF-7: Data Subject Access Request (DSAR) Support**
  - **Criterion:** When DSAR submitted, all sentiment data for a customer ID exported within 48 hours in machine-readable format (CSV/JSON)
  - **Measured by:** DSAR workflow test case
  - **Pass criteria:** Export completion within 48 hours; Export includes all sentiment records; Data anonymization verified where required

### Definition of Done Checklist

**Functional Completion:**
- [ ] All 5 functional acceptance criteria verified in staging environment
- [ ] All test cases executed with 100% pass rate
- [ ] Edge cases tested (network failures, API timeouts, malformed data)
- [ ] Integration tests pass with upstream/downstream systems

**Non-Functional Completion:**
- [ ] All performance benchmarks met for 7 consecutive days in staging
- [ ] Load testing completed with 1000+ concurrent sessions
- [ ] Security scan passed with zero critical or high vulnerabilities
- [ ] GDPR compliance review completed and approved by Legal
- [ ] Accessibility testing completed (WCAG 2.1 AA standard)

**Quality & Observability:**
- [ ] Code review completed and approved (2+ reviewers)
- [ ] Unit test coverage ≥80% (backend), ≥70% (frontend)
- [ ] API documentation complete (Swagger/OpenAPI)
- [ ] Monitoring dashboards configured (Datadog/Grafana)
- [ ] Alerts configured for all critical metrics (latency, error rate, throughput)
- [ ] Logging implemented at appropriate levels (INFO, WARN, ERROR)

**Operational Readiness:**
- [ ] Runbook documented (troubleshooting, common issues)
- [ ] Rollback plan tested successfully
- [ ] Deployment automation tested (CI/CD pipeline green)
- [ ] Database migration tested (forward and rollback)
- [ ] Feature flags configured for progressive rollout
- [ ] On-call team trained on new feature

**Business Value Verification:**
- [ ] Success metrics baseline captured pre-launch
- [ ] Analytics tracking implemented for all KPIs
- [ ] User acceptance testing (UAT) completed with 2-3 pilot teams
- [ ] UAT feedback incorporated (no critical issues remaining)
- [ ] Product documentation and training materials complete
- [ ] Launch communication plan executed (stakeholders notified)
```

## Output Format

### Complete Epic Document Template

```markdown
# [Epic Title]
**Epic ID:** [JIRA Epic Key]
**Created:** [Date]
**Owner:** [Product Manager Name]
**Status:** [Draft/In Progress/Delivered]

---

## 📋 Table of Contents
- [Business Objective](#business-objective)
- [User Personas](#user-personas)
- [Success Metrics](#success-metrics)
- [In Scope](#in-scope)
- [Out of Scope](#out-of-scope)
- [Dependencies](#dependencies)
- [Risks](#risks)
- [Acceptance Criteria](#acceptance-criteria)
- [Definition of Done](#definition-of-done)

---

[All sections follow templates defined above]

---

## 📊 Epic Health Dashboard

**Last Updated:** [Date]

| Category | Status | Details |
|----------|--------|---------|
| **Scope** | 🟢 Green | In scope clear, out of scope documented |
| **Dependencies** | 🟡 Yellow | 1 critical dependency at risk (data pipeline) |
| **Risks** | 🟡 Yellow | 2 high risks under mitigation |
| **Team Velocity** | 🟢 Green | On track, 85% of sprint goals met |
| **Success Metrics** | ⚪ Not Started | Baseline capture in progress |

**Overall Epic Health:** 🟡 Yellow (Monitor closely - dependency risk)

---

## 📅 Timeline & Milestones

| Milestone | Target Date | Status | Dependencies |
|-----------|-------------|--------|--------------|
| Epic Kickoff | March 1, 2026 | ✅ Complete | None |
| POC/Technical Spike | March 15, 2026 | 🔄 In Progress | AWS API access |
| MVP Development Sprint 1-3 | March 18 - April 8 | ⏳ Scheduled | Data pipeline complete |
| Beta Testing (Pilot Teams) | April 11-25 | ⏳ Scheduled | MVP complete |
| Production Launch (Phased) | April 29, 2026 | ⏳ Scheduled | Beta feedback incorporated |

---

## 👥 Team & Stakeholders

**Product Owner:** Jane Smith (jane.smith@company.com)
**Engineering Lead:** Emily Zhang (emily.zhang@company.com)
**QA Lead:** Mike Chen (mike.chen@company.com)
**UX Designer:** Alex Kim (alex.kim@company.com)

**Key Stakeholders:**
- VP Customer Experience: Sarah Johnson
- Head of Operations: Tom Williams
- Compliance: Legal Team (contact: legal@company.com)

**Decision Makers:**
- API Selection: Technical Lead + PM
- Budget Approval: Finance + VP CX
- Launch Timing: Product Owner + Operations Head

---

## 📚 Related Documentation

- [Technical Design Doc](link)
- [API Specification](link)
- [UX Mockups](link)
- [Security Review](link)
- [Cost Analysis](link)
- [Pilot Plan](link)

---

## 🔄 Change Log

| Date | Change | Reason | Approver |
|------|--------|--------|----------|
| March 1, 2026 | Epic created | Discovery complete | PM |
| March 5, 2026 | Voice analysis moved to out-of-scope | Complexity reduction for MVP | PM + Tech Lead |
| March 10, 2026 | Added Azure fallback plan | AWS approval delayed | Tech Lead |

---

**Epic Status:** Ready for Development
**Next Review:** March 15, 2026 (Sprint Planning)
```

## Skill Usage

### Command Format
```
Structure this into a formal epic:
[paste structured data from conversation extraction or requirements doc]
```

### Example Usage
```
Structure this into a formal epic with measurable criteria:

Business objective: Enable real-time customer sentiment analysis
Users: Supervisors and agents need sentiment visibility
KPIs: 85% accuracy, 2-second latency, 1000 concurrent sessions
Dependencies: Data pipeline upgrade (blocker)
Risks: False positives, API costs, accuracy below threshold
```

### Output Validation

The skill will automatically check:
- ✅ All acceptance criteria are measurable
- ✅ Success metrics have specific numbers
- ✅ Scope boundaries are clear
- ✅ Dependencies have mitigation plans
- ✅ Risks have contingency plans
- ✅ No vague terms in AC

If any validation fails, skill will:
1. Flag the issue
2. Suggest specific improvements
3. Provide examples of better phrasing

## Integration Points

### With Transcript Intelligence
```
Workflow:
1. Extract structured data from conversation (using Extractor skill)
2. Pass extracted data to Epic Structurer
3. Get formal JIRA-ready epic
```

### With JIRA
- Copy-paste ready epic description
- Formatted for JIRA markdown
- Can be directly imported into JIRA epic field

### Standalone Use
- Can structure any requirements into epic format
- Works with manual input
- Supports iterative refinement

## Quality Gates

Before epic is marked "Ready for Development":

### Mandatory Quality Checks
- [ ] Title follows format: `[Capability]: [User Outcome]`
- [ ] Business objective quantifies problem and value
- [ ] At least one primary persona defined with measurable success criteria
- [ ] Minimum 3 success metrics with specific targets
- [ ] In scope is specific (no vague "support")
- [ ] Out of scope explicitly lists exclusions with rationale
- [ ] All critical dependencies have mitigation plans
- [ ] High risks have contingency plans
- [ ] Every acceptance criterion is measurable and testable
- [ ] Definition of done checklist is complete
- [ ] No use of banned vague terms without quantification

### Advisory Quality Checks (Warnings)
- ⚠️ Consider: Are success metrics aligned with acceptance criteria?
- ⚠️ Consider: Have we documented why items are out of scope?
- ⚠️ Consider: Do we have contingency for all critical risks?
- ⚠️ Consider: Are dependencies actively tracked with owners?

## Banned Vague Terms List

The following terms are **BANNED** in Acceptance Criteria unless quantified:

❌ **Performance Terms (without numbers):**
- "fast", "quick", "slow", "efficient", "performant"
- Must specify: latency in milliseconds, throughput in requests/sec, etc.

❌ **Usability Terms (without metrics):**
- "intuitive", "user-friendly", "easy", "simple", "convenient"
- Must specify: task completion time, error rate, user satisfaction score, etc.

❌ **Quality Terms (without measures):**
- "robust", "reliable", "stable", "good", "better", "high quality"
- Must specify: uptime %, error rate, test coverage %, defect count, etc.

❌ **Scalability Terms (without capacity):**
- "scalable", "handles growth", "can scale"
- Must specify: concurrent users, requests per second, data volume, etc.

❌ **Completeness Terms (without criteria):**
- "comprehensive", "thorough", "complete", "full coverage"
- Must specify: % coverage, number of scenarios, list of items, etc.

✅ **Acceptable Replacements:**
- "Fast" → "Response time < 200ms for P95 of requests"
- "Intuitive" → "New users complete task in <5 minutes without documentation"
- "Robust" → "99.9% uptime over 30 days with <0.1% error rate"
- "Scalable" → "Handles 10,000 concurrent users with <2s latency"
- "Comprehensive" → "Covers all 15 identified user scenarios with ≥80% code coverage"

## Best Practices

1. **Start with Why**: Always begin with clear business objective and user problem
2. **Quantify Everything**: Every claim needs a number, percentage, or observable outcome
3. **Define Boundaries**: Explicit scope prevents endless "can we also add..."
4. **Plan for Failure**: Every risk and dependency needs a backup plan
5. **Test First**: Write AC that can be automated or clearly verified
6. **Iterate**: Epic quality improves with review and refinement
7. **Stakeholder Review**: Get buy-in from engineering, QA, and business before "ready"

## Common Pitfalls to Avoid

| Pitfall | Fix |
|---------|-----|
| "AC: System should be fast" | Be specific: "P95 latency <2s" |
| Scope creep | Document out-of-scope explicitly |
| Forgotten dependencies | Map all technical and team dependencies |
| Unmitigated risks | Every high risk needs mitigation + contingency |
| Unquantified benefits | Convert "improve satisfaction" to "+10 CSAT points" |
| Assuming shared understanding | Write everything explicitly, test for ambiguity |

---

**Skill Type:** Content Generation & Structuring  
**Complexity:** High  
**Best For:** Converting discovery/requirements into formal JIRA epics  
**Ensures:** Measurable criteria, clear scope, actionable acceptance criteria

---

## Hook: Run Logger

At the end of every invocation, write a log file to:
`.claude/logs/epic-structurer-skill/YYYY-MM-DD-<epic-key>.md`

**Log file content:**

```markdown
# Epic Structurer Skill — Run Log
**Date:** YYYY-MM-DD HH:MM
**Input:** Epic key or discovery output
**Status:** COMPLETE | BLOCKED | PARTIAL

## Actions Taken
- <e.g. "Structured epic PROJ-102 from discovery output">
- <e.g. "Generated acceptance criteria, scope, measurable goals">

## Output
- Epic Sections Created: X | Output: <file or Jira link>

## Key Points
- <notable decision or assumption>

## Next Steps
- <what should happen next>
```
