# Transcript Intelligence - Quick Reference

## One-Line Purpose
Transform messy meeting transcripts into structured, actionable data across 8 key categories.

## Quick Usage

```
Extract structured data from this conversation:
[paste transcript or meeting notes]
```

## What Gets Extracted

| # | Category | What It Finds | Output |
|---|----------|---------------|---------|
| 1 | **Business Objective** | Goals, problems, ROI | Primary + secondary objectives with measurable outcomes |
| 2 | **KPIs** | Metrics, targets, baselines | Table with name, target, baseline, measurement method |
| 3 | **Assumptions** | "Assuming...", "if we..." | List with risk level and validation status |
| 4 | **Risks** | Concerns, blockers, challenges | Categorized risks with impact and mitigation |
| 5 | **Unresolved Decisions** | Open questions, disagreements | Decision matrix with owner and deadline |
| 6 | **Dependencies** | "Depends on...", "blocked by..." | Dependency map showing critical path |
| 7 | **User Roles** | Personas, user needs | Role matrix with goals and pain points |
| 8 | **Technical Constraints** | Limitations, requirements | Constraint list with severity and rationale |

## Common Patterns Detected

### Business Objective Triggers
- "we need to", "goal is", "purpose of"
- "trying to solve", "improve", "reduce"

### KPI Triggers  
- Numeric values: "10%", "1000 users", "2 seconds"
- "target is", "must achieve", "baseline"

### Assumption Triggers
- "assuming that", "if we can", "provided that"
- "based on existing", "similar to"

### Risk Triggers
- "risk", "concern", "worried", "challenge"
- "not sure if", "might fail", "limited by"

### Decision Triggers
- "should we", "which approach", "need to decide"
- "let's discuss later", "not aligned on"

### Dependency Triggers
- "depends on", "blocked by", "waiting for"
- "after", "once", "requires", "prerequisite"

### Role Triggers
- "as a [role]", "users who are", "only admins can"
- Persona names: supervisor, agent, admin

### Constraint Triggers
- "limited to", "maximum", "cannot exceed"
- "must integrate with", "99.9% uptime"
- "GDPR", "SOC2", "encrypted"

## Output Formats

### 1. Markdown Report
Full human-readable analysis with tables and structured sections.

### 2. JSON Structure
Machine-readable format for integration with other tools.

### 3. JIRA-Ready Content
Copy-paste ready epic descriptions and acceptance criteria.

### 4. Action Items List
Prioritized next steps generated from extraction.

## Use Cases

| Scenario | Input | Output Benefit |
|----------|-------|----------------|
| **Post-Meeting** | Meeting transcript | Structured notes, action items, decisions tracker |
| **Requirements Doc** | Free-form requirements | Organized requirements with gaps identified |
| **Epic Creation** | Discovery session notes | JIRA epic with objectives, KPIs, stories |
| **Risk Assessment** | Discussion logs | Risk register with mitigation plans |
| **Dependency Mapping** | Cross-team meetings | Dependency matrix, critical path identification |
| **Decision Log** | Email threads | Open decisions with owners and deadlines |

## Integration Examples

### With Discovery Agent
```
Step 1: Parse transcript
Step 2: Use Transcript Intelligence to get structured data
Step 3: Fetch JIRA epic
Step 4: Compare extracted data vs JIRA
Step 5: Generate gap analysis report
```

### Standalone Usage
```
# Just extract data
Extract structured data from [transcript]

# Extract + create JIRA content
Extract data and generate JIRA epic description for [transcript]

# Extract + identify gaps
Extract data and highlight what's missing for [transcript]
```

## Quality Indicators

**High Confidence Extraction** when:
- Clear speaker attribution
- Explicit statements ("we will", "must have", "target is")
- Quantifiable metrics mentioned
- Decisions explicitly stated

**Medium Confidence** when:
- Inferred from context
- Implicit assumptions
- Priority levels not stated
- Owner not clearly identified

**Low Confidence** when:
- Ambiguous statements
- Missing context
- Rhetorical questions
- Contradictory information

## Typical Results

For a **30-minute discovery meeting**:
- ✓ 1-2 business objectives
- ✓ 3-7 KPIs
- ✓ 5-10 assumptions
- ✓ 4-8 risks
- ✓ 2-6 unresolved decisions
- ✓ 3-6 dependencies
- ✓ 2-5 user roles
- ✓ 4-10 technical constraints

**Processing Time**: 30-60 seconds

## Example Commands

### Basic Extraction
```
Extract structured data from the meeting transcript in 
src/test-data/sample-discovery-transcript.txt
```

### With Specific Focus
```
Extract business objectives, KPIs, and risks from this discussion:
[paste text]
```

### Generate JIRA Content
```
Extract data from this transcript and create JIRA epic description:
[paste text]
```

### Identify Gaps
```
Extract data and tell me what's missing or needs clarification:
[paste text]
```

### Compare Against Template
```
Extract data and compare against our standard discovery checklist:
[paste text]
```

## Pro Tips

1. **Include Context**: Add meeting type, date, participants if available
2. **Clean Input**: Remove join/leave notifications, technical glitches
3. **Speaker Tags**: Include "Person:" format if possible
4. **Review Low-Confidence**: Always validate items marked low-confidence
5. **Cross-Check**: Use extraction to verify nothing was missed
6. **Iterate**: If something missed, provide feedback for improvement

## Common Issues

| Issue | Solution |
|-------|----------|
| Missing extractions | Add more context, check if item was actually discussed |
| Wrong categorization | Review confidence level, may need manual reclassification |
| Duplicates | Normal for cross-cutting concerns, consolidate in review |
| False positives | Review medium/low confidence items carefully |
| Incomplete data | Expected - only extracts what's stated, not what should be |

## Files

- **Skill Definition**: [transcript-intelligence-skill.md](transcript-intelligence-skill.md)
- **Example Output**: [example-extraction-output.md](example-extraction-output.md)
- **Sample Transcript**: `../../acme-service/src/test-data/sample-discovery-transcript.txt`
- **Quick Reference**: This file

## Related Skills

- **Discovery Agent**: Uses this skill for transcript analysis
- **JIRA Test Plan Generator**: Can use extracted data for test case generation
- **Risk Analyzer**: Deep-dive on extracted risks

---

**Skill Type**: Data Extraction  
**Complexity**: Medium-High  
**Best For**: Discovery meetings, requirements analysis, planning sessions  
**Works With**: Any unstructured conversation text
