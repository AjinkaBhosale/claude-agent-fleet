---
name: transcript-intelligence
description: "Use when extracting structured data from messy meeting transcripts or unstructured discussion text."
---

# Transcript Intelligence Skill

## Purpose
Extract structured data from messy conversation transcripts, meeting notes, or unstructured discussion text. Transform chaotic discussions into organized, actionable information.

## Execution Logging

**Log key processing steps when using this skill.**

Maintain an execution log that captures:
- Processing step description
- Input data summary (transcript length, format)
- Processing duration
- Output summary (items extracted per category)

Save execution log to: `skill-execution-logs/transcript-intelligence-[TIMESTAMP].log`

**Log Entry Example:**
```markdown
### Transcript Intelligence Skill Execution
**Timestamp**: 2026-03-06 14:32:00  
**Input**: 2,450 words, 8 speakers, 45-minute meeting  
**Processing Duration**: 2.5s  

**Extracted Data**:
- Business Objectives: 3 primary, 2 secondary
- KPIs: 7 metrics identified
- Assumptions: 12 found (4 high-risk)
- Risks: 8 identified (2 critical)
- User Roles: 4 personas
- Dependencies: 6 external, 3 internal
- Decisions: 15 made, 3 deferred
- Unresolved: 5 open questions

**Result**: ✅ Success  
---
```

## Behavior

### Core Extraction Capabilities

#### 1. Identify Business Objective
**Detection Patterns:**
- Goal statements: "we need to", "our goal is", "the purpose of this"
- Problem statements: "the issue is", "we're trying to solve", "customers are complaining"
- Value propositions: "this will help us", "the benefit is", "ROI will be"
- Strategic intent: "to improve", "to reduce", "to increase"

**Extraction Logic:**
- Prioritize executive/PM statements about "why" we're doing this
- Look for quantifiable goals (e.g., "reduce churn by 10%")
- Identify primary vs secondary objectives
- Capture both explicit and implicit business drivers

**Output Format:**
```
Business Objective:
- Primary: [Main goal with measurable outcome]
- Secondary: [Supporting goals]
- Problem Being Solved: [Customer/business pain point]
- Expected Value: [Business impact or ROI]
```

#### 2. Extract KPIs Mentioned
**Detection Patterns:**
- Numeric metrics: "10% improvement", "1000 users", "5 seconds"
- Performance indicators: "response time", "accuracy rate", "customer satisfaction"
- Success criteria: "must achieve", "target is", "baseline is"
- Measurement keywords: "measure", "track", "monitor", "metric", "KPI"

**Extraction Logic:**
- Capture metric name + target value + timeframe
- Distinguish between input metrics and outcome metrics
- Identify baseline vs target values
- Note measurement frequency (real-time, daily, monthly)

**Output Format:**
```
KPIs:
- [Metric Name]: [Target Value] ([Baseline if mentioned])
  - Measurement: [How it's measured]
  - Frequency: [When it's tracked]
  - Priority: [High/Medium/Low]
```

#### 3. Detect Assumptions
**Detection Patterns:**
- Conditional statements: "assuming that", "if we can", "provided that"
- Implicit assumptions: "we'll use existing", "based on current", "similar to"
- Dependency assumptions: "once X is done", "after Y releases"
- Resource assumptions: "with the team we have", "given the budget"

**Extraction Logic:**
- Separate validated vs unvalidated assumptions
- Identify risky assumptions (those with low confidence)
- Capture who stated the assumption
- Note if assumption was challenged or accepted

**Output Format:**
```
Assumptions:
- [Assumption Statement]
  - Type: [Technical/Business/Resource/Timeline]
  - Risk Level: [High/Medium/Low]
  - Validation Status: [Unvalidated/To Be Verified/Validated]
  - Stated By: [Person/Role]
```

#### 4. Detect Risks
**Detection Patterns:**
- Risk keywords: "risk", "concern", "worried", "problem", "challenge", "blocker"
- Uncertainty phrases: "not sure if", "might be difficult", "could fail"
- Past failures: "last time we tried", "previous project had"
- Constraint mentions: "limited by", "constrained by", "shortage of"

**Extraction Logic:**
- Categorize risk type (technical, schedule, resource, dependency)
- Assess severity based on urgency/emphasis in conversation
- Identify if mitigation was discussed
- Link risks to specific features/stories

**Output Format:**
```
Risks:
- [Risk Description]
  - Category: [Technical/Schedule/Resource/Dependency/Business]
  - Impact: [High/Medium/Low]
  - Probability: [High/Medium/Low]
  - Mitigation Discussed: [Yes/No - briefly describe]
  - Raised By: [Person/Role]
```

#### 5. Detect Unresolved Decisions
**Detection Patterns:**
- Open questions: "should we", "which approach", "do we want to", "need to decide"
- Deferred decisions: "let's discuss later", "table this for now", "follow up on"
- Disagreement: "I think X but John thinks Y", "not aligned on", "need consensus"
- Action items for decision: "research options", "get input from", "evaluate"

**Extraction Logic:**
- Distinguish between open questions and rhetorical questions
- Identify who needs to make the decision
- Note deadline/urgency for decision
- Capture different viewpoints if discussed

**Output Format:**
```
Unresolved Decisions:
- [Decision to Be Made]
  - Context: [Why this needs to be decided]
  - Options Discussed: [Option A, Option B, ...]
  - Decision Owner: [Person/Team responsible]
  - Deadline: [If mentioned]
  - Blockers: [What's blocked until this is decided]
  - Priority: [Critical/Important/Nice-to-Have]
```

#### 6. Detect Dependencies
**Detection Patterns:**
- Blocking statements: "depends on", "blocked by", "waiting for", "requires"
- Sequential indicators: "after", "once", "before we can", "prerequisite"
- External references: "need from Platform team", "backend API", "third-party"
- Resource dependencies: "need designer", "requires DevOps", "waiting on approval"

**Extraction Logic:**
- Identify dependency type (technical, team, approval, external)
- Map what depends on what (A depends on B)
- Determine if dependency is critical path
- Note dependency owner/provider

**Output Format:**
```
Dependencies:
- [What We Need]: depends on [Provider/System]
  - Type: [Technical/Team/Approval/External/Data]
  - Blocks: [What features/stories are blocked]
  - Status: [Not Started/In Progress/Done/Unknown]
  - Owner: [Team/Person responsible for unblocking]
  - Critical Path: [Yes/No]
```

#### 7. Extract User Roles
**Detection Patterns:**
- Role mentions: "as a [role]", "the [role] needs", "users who are"
- Persona descriptions: "supervisors", "agents", "administrators", "customers"
- User story format: "as a X, I need Y"
- Permission mentions: "only admins can", "agents should be able to"

**Extraction Logic:**
- List all unique user roles/personas mentioned
- Capture needs/goals for each role
- Identify primary vs secondary users
- Note role-specific features or permissions

**Output Format:**
```
User Roles:
- [Role/Persona Name]
  - Description: [Who they are]
  - Goals: [What they want to accomplish]
  - Pain Points: [Current problems they face]
  - Features for This Role: [Mentioned features]
  - Priority: [Primary/Secondary/Edge Case]
```

#### 8. Identify Technical Constraints
**Detection Patterns:**
- Limitation keywords: "limited to", "maximum", "cannot exceed", "constrained by"
- Technology mentions: "uses PostgreSQL", "must integrate with", "API limitation"
- Performance requirements: "within 2 seconds", "handle 1000 concurrent", "99.9% uptime"
- Compliance/security: "GDPR compliant", "must encrypt", "SOC2 requirement"

**Extraction Logic:**
- Distinguish hard constraints from preferences
- Identify technology stack decisions
- Capture performance/scale requirements
- Note compliance/regulatory requirements

**Output Format:**
```
Technical Constraints:
- [Constraint Description]
  - Type: [Performance/Scale/Technology/Compliance/Integration]
  - Severity: [Must Have/Should Have/Nice to Have]
  - Impact: [What it affects]
  - Rationale: [Why this constraint exists]
```

## Processing Workflow

### Step 1: Input Normalization
Accept various input formats:
- Raw text transcript
- Meeting notes (bullet points)
- Email threads
- Chat conversation logs
- Structured JSON with speaker attribution

### Step 2: Context Analysis
Analyze conversation metadata:
- Identify participants and roles (PM, Tech Lead, Designer, etc.)
- Detect meeting type (discovery, planning, retrospective)
- Note timestamp/date for context
- Identify project/epic being discussed

### Step 3: Multi-Pass Extraction
**Pass 1 - Speaker Attribution:**
- Tag each statement with speaker
- Weigh statements by speaker role (PMs for business goals, Tech Leads for constraints)

**Pass 2 - Pattern Matching:**
- Apply detection patterns for each data type
- Use NLP keywords and phrase patterns
- Context-aware extraction (same phrase means different things in different contexts)

**Pass 3 - Relationship Mapping:**
- Link related items (risk → mitigation, decision → blocker)
- Identify what's missing (mentioned risk but no mitigation)
- Cross-reference items (KPI mentioned but not in objective)

**Pass 4 - Validation & Scoring:**
- Confidence score for each extraction (High/Medium/Low)
- Flag ambiguous extractions for human review
- Deduplicate similar items

### Step 4: Output Generation
Generate structured summary in multiple formats:
- Markdown report (human-readable)
- JSON structure (machine-readable)
- JIRA-ready format (for creating tickets)

## Output Format

### Structured Extraction Summary

```markdown
# Transcript Intelligence Report
**Source**: [Meeting/Document Name]
**Date**: [Date]
**Participants**: [List of people]
**Confidence**: [Overall extraction confidence: High/Medium/Low]

---

## 1. Business Objective
**Primary Goal**: [Main measurable objective]

**Secondary Goals**:
- [Goal 1]
- [Goal 2]

**Problem Being Solved**: [Customer/business pain point]

**Expected Value**: [ROI or business impact]

---

## 2. Key Performance Indicators (KPIs)
| KPI | Target | Baseline | Measurement Method | Priority |
|-----|--------|----------|-------------------|----------|
| [Metric 1] | [Value] | [If known] | [How measured] | High |
| [Metric 2] | [Value] | [If known] | [How measured] | Medium |

---

## 3. Assumptions
| Assumption | Type | Risk Level | Validation Status | Owner |
|------------|------|------------|------------------|-------|
| [Assumption 1] | Technical | High | Unvalidated | [Person] |
| [Assumption 2] | Business | Medium | To Be Verified | [Person] |

**High-Risk Assumptions**:
- [List assumptions that need immediate validation]

---

## 4. Risks
| Risk | Category | Impact | Probability | Mitigation | Owner |
|------|----------|--------|-------------|------------|-------|
| [Risk 1] | Technical | High | Medium | [If discussed] | [Person] |
| [Risk 2] | Schedule | Medium | High | [If discussed] | [Person] |

**Critical Risks** (High Impact + High Probability):
- [List critical risks requiring immediate attention]

---

## 5. Unresolved Decisions
| Decision | Options | Owner | Deadline | Blocks | Priority |
|----------|---------|-------|----------|--------|----------|
| [Decision 1] | [A, B, C] | [Person] | [Date] | [What's blocked] | Critical |
| [Decision 2] | [X, Y] | [Team] | TBD | [What's blocked] | Important |

**Immediate Action Required**:
- [Decisions blocking progress]

---

## 6. Dependencies
| We Need | From | Blocks | Status | Critical Path |
|---------|------|--------|--------|---------------|
| [Dependency 1] | [Team/System] | [Feature X] | Unknown | Yes |
| [Dependency 2] | [External API] | [Feature Y] | In Progress | No |

**Critical Path Dependencies**:
- [Dependencies that are on critical path]

---

## 7. User Roles & Personas
| Role | Goals | Pain Points | Priority | Mentioned Features |
|------|-------|-------------|----------|-------------------|
| [Role 1] | [Goals] | [Problems] | Primary | [Features] |
| [Role 2] | [Goals] | [Problems] | Secondary | [Features] |

---

## 8. Technical Constraints
| Constraint | Type | Severity | Impact | Rationale |
|------------|------|----------|--------|-----------|
| [Constraint 1] | Performance | Must Have | [Affects X] | [Why] |
| [Constraint 2] | Compliance | Must Have | [Affects Y] | [Why] |

---

## Summary Statistics
- **Business Objectives Identified**: X
- **KPIs Defined**: X (Target set: Y, Baseline known: Z)
- **Assumptions Captured**: X (High Risk: Y, Unvalidated: Z)
- **Risks Identified**: X (Critical: Y, High: Z)
- **Open Decisions**: X (Critical: Y, Deadline set: Z)
- **Dependencies Mapped**: X (Critical Path: Y, External: Z)
- **User Roles**: X (Primary: Y, Secondary: Z)
- **Technical Constraints**: X (Must Have: Y, Should Have: Z)

---

## Extraction Confidence
- **High Confidence**: [Items clearly stated and unambiguous]
- **Medium Confidence**: [Items inferred from context]
- **Low Confidence**: [Items ambiguous or require validation]

---

## Action Items Generated from Extraction
1. **Validate Assumptions**: [List high-risk assumptions]
2. **Make Decisions**: [List critical open decisions]
3. **Resolve Dependencies**: [List blocking dependencies]
4. **Document Missing Information**: [What wasn't discussed but should be]

---

## Next Steps
1. Review and validate extracted data
2. Create JIRA tickets for unresolved items
3. Schedule follow-up for open decisions
4. Document assumptions for validation
```

## JSON Output Format

For machine-readable integration:

```json
{
  "metadata": {
    "source": "Meeting transcript",
    "date": "2026-03-06",
    "participants": ["PM", "Tech Lead", "Designer"],
    "confidence": "high"
  },
  "businessObjective": {
    "primary": "Main goal",
    "secondary": ["Goal 1", "Goal 2"],
    "problem": "Pain point",
    "expectedValue": "ROI"
  },
  "kpis": [
    {
      "name": "Response Time",
      "target": "< 2 seconds",
      "baseline": "5 seconds",
      "measurement": "Average API response",
      "priority": "high"
    }
  ],
  "assumptions": [
    {
      "statement": "Assumption text",
      "type": "technical",
      "riskLevel": "high",
      "validationStatus": "unvalidated",
      "owner": "Tech Lead"
    }
  ],
  "risks": [
    {
      "description": "Risk description",
      "category": "technical",
      "impact": "high",
      "probability": "medium",
      "mitigation": "Proposed solution",
      "owner": "Tech Lead"
    }
  ],
  "unresolvedDecisions": [
    {
      "decision": "What to decide",
      "options": ["Option A", "Option B"],
      "owner": "PM",
      "deadline": "2026-03-15",
      "blocks": ["Feature X"],
      "priority": "critical"
    }
  ],
  "dependencies": [
    {
      "what": "API integration",
      "from": "Platform team",
      "blocks": ["Feature Y"],
      "status": "in-progress",
      "criticalPath": true
    }
  ],
  "userRoles": [
    {
      "role": "Supervisor",
      "goals": ["Monitor team performance"],
      "painPoints": ["Lack of real-time data"],
      "features": ["Dashboard", "Alerts"],
      "priority": "primary"
    }
  ],
  "technicalConstraints": [
    {
      "description": "Must use PostgreSQL",
      "type": "technology",
      "severity": "must-have",
      "impact": "Database design",
      "rationale": "Existing infrastructure"
    }
  ]
}
```

## Usage Examples

### Example 1: Discovery Meeting Transcript
```
Input: [Paste messy meeting transcript]

Output: 
✓ Extracted 1 primary business objective
✓ Identified 5 KPIs (3 with baselines)
✓ Captured 8 assumptions (2 high-risk)
✓ Found 6 risks (1 critical)
✓ Detected 4 unresolved decisions
✓ Mapped 3 dependencies (1 critical path)
✓ Identified 4 user roles
✓ Listed 5 technical constraints

[Full structured report follows...]
```

### Example 2: Email Thread Analysis
```
Input: [Paste email conversation about feature requirements]

Output:
✓ Business objective extracted from PM's first email
✓ Technical constraints from Engineering responses
✓ 3 unresolved decisions identified from question threads
✓ 2 dependencies noted in blocker mentions

[Structured summary...]
```

## Integration Points

### With Discovery Agent
This skill can be used as **Step 2** in the Discovery Agent workflow:
1. Parse transcript → 2. **Extract structured data** → 3. Fetch JIRA → 4. Compare → 5. Report

### With JIRA
Extracted data maps to JIRA fields:
- Business Objective → Epic Description
- KPIs → Acceptance Criteria
- Risks → Risk field or labels
- Unresolved Decisions → Comments or blockers
- Dependencies → Issue links
- User Roles → User stories

### Standalone Use
Can be used independently for:
- Meeting note cleanup
- Requirements documentation
- Discovery session analysis
- Email thread summarization

## Best Practices

1. **Feed Clean Input**: While this handles messy text, removing meeting join/leave notifications helps
2. **Provide Context**: Include meeting type, participants, date if available
3. **Review Confidence**: Always review low-confidence extractions
4. **Validate Assumptions**: Use as a starting point, not ground truth
5. **Iterative Refinement**: If extraction misses items, provide feedback for pattern improvement

## Limitations

- **Language**: Optimized for English technical/business conversations
- **Domain**: Best for software/product development discussions
- **Ambiguity**: Cannot resolve unclear statements without context
- **Speaker Intent**: May misinterpret sarcasm, jokes, or rhetorical questions
- **Completeness**: Only extracts what's explicitly or implicitly stated

---

**Skill Type**: Data Extraction & Analysis  
**Complexity**: Medium-High  
**Typical Use Case**: Discovery meetings, requirement analysis, planning sessions  
**Output Time**: ~30-60 seconds for a 30-minute meeting transcript

---

## Hook: Run Logger

At the end of every invocation, write a log file to:
`.claude/logs/transcript-intelligence-skill/YYYY-MM-DD-<transcript-name>.md`

**Log file content:**

```markdown
# Transcript Intelligence Skill — Run Log
**Date:** YYYY-MM-DD HH:MM
**Input:** Transcript file name
**Status:** COMPLETE | BLOCKED | PARTIAL

## Actions Taken
- <e.g. "Processed Insights-discovery-meeting.vtt">
- <e.g. "Extracted 14 requirements, 3 open questions, 5 decisions">

## Output
- Requirements: X | Decisions: X | Open Questions: X

## Key Points
- <notable decision or assumption>

## Next Steps
- <what should happen next>
```
