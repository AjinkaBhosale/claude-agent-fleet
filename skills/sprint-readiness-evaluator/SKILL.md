---
name: sprint-readiness-evaluator
description: "Use when evaluating whether an epic meets Definition of Ready for sprint planning."
---

# Sprint Readiness Evaluator Skill

## Overview
Evaluates whether an epic is ready for sprint planning by assessing Definition of Ready (DoR) criteria from a Scrum/Agile perspective.

## Purpose
- Validate epic against industry-standard Definition of Ready
- Identify sprint blockers before planning begins
- Provide Scrum Master with ceremony recommendations
- Calculate sprint risk score

See **Skill: epic-readiness-gate-conventions** for the shared severity vocabulary and blocking-gate enforcement contract. This skill's 6 Definition-of-Ready criteria below are specific to sprint-planning readiness and are not shared with `epic-quality-gate` (a different, pre-JIRA-creation checkpoint) — only the surrounding vocabulary and "what happens on BLOCKED" behavior are common.

## Input Parameters
```typescript
interface SprintReadinessInput {
  epic: JiraEpic;                    // Full epic data from JIRA
  stories: JiraStory[];              // List of stories under epic
  transcriptAnalysis: TranscriptData; // Parsed transcript insights
  teamContext?: {
    velocity?: number;               // Team's average velocity
    sprintLength?: number;           // Sprint duration in weeks
    capacity?: number;               // Team capacity for next sprint
  };
}
```

## Output Structure
```typescript
interface SprintReadinessOutput {
  overallScore: number;              // 0-100 score
  status: 'READY' | 'NEEDS_WORK' | 'BLOCKED';
  dorCriteria: {
    clearBusinessValue: DorCheck;
    measurableSuccess: DorCheck;
    dependenciesIdentified: DorCheck;
    acceptanceCriteriaTestable: DorCheck;
    storiesDecomposed: DorCheck;
    noUnresolvedQuestions: DorCheck;
  };
  sprintPlannability: {
    canStartPlanning: boolean;
    estimatedPlanningDuration: string; // e.g., "2 hours"
    recommendedAgenda: string[];
    blockers: string[];
  };
  refinementNeeded: {
    required: boolean;
    estimatedDuration: string;        // e.g., "1.5 hours"
    focus: string[];                  // What to refine
  };
  risks: SprintRisk[];
}

interface DorCheck {
  status: 'PASS' | 'FAIL' | 'PARTIAL';
  score: number;                      // 0-10
  evidence: string;                   // What was found
  gap?: string;                       // What's missing
  remediation?: string;               // How to fix
}

interface SprintRisk {
  type: 'DEPENDENCY' | 'TECHNICAL' | 'RESOURCE' | 'SCOPE';
  severity: 'HIGH' | 'MEDIUM' | 'LOW';
  description: string;
  impact: string;                     // Impact on sprint
  mitigation?: string;                // How to mitigate
  owner?: string;                     // Who owns resolution
}
```

## Evaluation Logic

### Definition of Ready Checklist

#### 1. Clear Business Value (Weight: 20%)
- **PASS**: Epic has defined business problem, value proposition, and KPIs
- **PARTIAL**: Business value stated but KPIs missing or vague
- **FAIL**: No clear business justification

**Scoring**:
```typescript
if (hasBusinessProblem && hasValueProp && hasQuantifiableKPIs) {
  score = 10;
} else if (hasBusinessProblem && hasValueProp) {
  score = 6;
} else if (hasBusinessProblem) {
  score = 3;
} else {
  score = 0;
}
```

#### 2. Measurable Success Criteria (Weight: 25%)
- **PASS**: All stories have quantifiable acceptance criteria
- **PARTIAL**: >70% of stories have measurable ACs
- **FAIL**: <70% of stories have measurable ACs

**Scoring**:
```typescript
const measurablePercentage = (measurableACs / totalACs) * 100;
if (measurablePercentage >= 95) score = 10;
else if (measurablePercentage >= 80) score = 8;
else if (measurablePercentage >= 70) score = 6;
else if (measurablePercentage >= 50) score = 4;
else score = Math.floor(measurablePercentage / 10);
```

#### 3. Dependencies Identified (Weight: 15%)
- **PASS**: All dependencies documented with mitigation plans
- **PARTIAL**: Dependencies identified but missing mitigations
- **FAIL**: Dependencies not identified or no mitigation plans

#### 4. Acceptance Criteria Testable (Weight: 20%)
- **PASS**: All ACs can be verified through automated or manual testing
- **PARTIAL**: Most ACs testable but some require clarification
- **FAIL**: ACs are subjective or not verifiable

#### 5. Stories Decomposed (Weight: 10%)
- **PASS**: Epic broken into right-sized stories (3-13 points estimated)
- **PARTIAL**: Some stories too large or too granular
- **FAIL**: Epic not broken down or stories poorly sized

#### 6. No Unresolved Questions (Weight: 10%)
- **PASS**: 0-2 minor questions remaining
- **PARTIAL**: 3-5 questions with clear owners
- **FAIL**: >5 questions or critical questions unassigned

### Overall Readiness Calculation

```typescript
const weightedScore = 
  (clearBusinessValue.score * 0.20) +
  (measurableSuccess.score * 0.25) +
  (dependenciesIdentified.score * 0.15) +
  (acceptanceCriteriaTestable.score * 0.20) +
  (storiesDecomposed.score * 0.10) +
  (noUnresolvedQuestions.score * 0.10);

const overallScore = Math.round(weightedScore * 10); // Convert to 0-100

if (overallScore >= 85) status = 'READY';
else if (overallScore >= 60) status = 'NEEDS_WORK';
else status = 'BLOCKED';
```

## Usage Example

```typescript
const readiness = await sprintReadinessEvaluator.evaluate({
  epic: jiraEpicData,
  stories: epicStories,
  transcriptAnalysis: parsedTranscript,
  teamContext: {
    velocity: 42,
    sprintLength: 2,
    capacity: 80
  }
});

if (readiness.status === 'READY') {
  console.log('✅ Epic ready for sprint planning');
  console.log(`Recommended planning duration: ${readiness.sprintPlannability.estimatedPlanningDuration}`);
} else if (readiness.status === 'NEEDS_WORK') {
  console.log('⚠️ Refinement needed before sprint planning');
  console.log(`Focus on: ${readiness.refinementNeeded.focus.join(', ')}`);
} else {
  console.log('🚨 Epic blocked - critical gaps found');
  readiness.sprintPlannability.blockers.forEach(blocker => {
    console.log(`  - ${blocker}`);
  });
}
```

## Integration with Requirements-Intelligence-Agent

`Requirements-Intelligence-Agent` can invoke this skill during its gap analysis to provide sprint-focused recommendations (plannability, blockers, refinement duration) alongside its own epic readiness score — the two scores measure different things (epic documentation quality vs. sprint-planning readiness) and should both be surfaced, not merged into one number.

## Best Practices

1. **Always provide remediation steps** - Don't just identify gaps, explain how to fix them
2. **Be specific about timing** - Give realistic estimates for refinement duration
3. **Link risks to sprint impact** - Help teams understand business consequences
4. **Consider team context** - Adjust recommendations based on team velocity and capacity
5. **Document evidence** - Every score should be backed by concrete findings

## Dependencies
- Requires JIRA epic and story data
- Optionally uses team velocity data if available
- Complements `epic-quality-gate` for a full pre-sprint assessment — run both when a comprehensive picture is needed, since they check different things

---

## Hook: Run Logger

Use the **run-logger** skill's standard format and location — `~/.claude/agents/logs/sprint-readiness-evaluator/YYYY-MM-DD-<epic-key>.md` — rather than a bespoke log path. Include the Score/Status/Risk Level/Blocking summary block from **Skill: epic-readiness-gate-conventions** in the log's Output section.
