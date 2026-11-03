---
name: requirements-to-stories
description: Generates user stories with Acceptance Criteria from any raw requirements input — pasted text, meeting notes, email threads, or file paths. No JIRA epic needed upfront. Shows a preview in chat first, then optionally creates a JIRA epic and stories on confirmation. Use when: 'Generate stories from this requirements doc', 'Create user stories from these meeting notes', 'Turn this email thread into JIRA stories'
---

# Requirements to Stories

Generate user stories with Acceptance Criteria from raw requirements input, preview them in chat, then optionally create in JIRA.

---

## Inputs

### How to invoke

```
# Pasted text
/requirements-to-stories
[paste requirements doc, email thread, meeting notes, or conversation]

# File path
/requirements-to-stories
file: path/to/requirements.md

# With JIRA hints
/requirements-to-stories
epicTitle: "Opportunity Detection Dashboard"
epicKey: PROJ-102
[paste or file:]
```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| Raw text (body) | One of text or file | Pasted requirements, conversation, email, or meeting notes |
| `file:` | One of text or file | Path to `.txt`, `.md`, or `.vtt` file on disk |
| `epicTitle:` | Optional | Title for a new JIRA epic if one needs to be created |
| `epicKey:` | Optional | Existing JIRA epic key to link generated stories under |

### Input detection

- `file:` present → read the file from disk
- Raw text present → use directly
- Both present → use file; treat pasted text as additional context
- Neither present → ask the user to provide input before proceeding

---

## Workflow

```
STEP 1 — PARSE INPUT
  If file: parameter → read file from disk. If file not found → ask user
  to check the path and offer to accept pasted text instead.
  Extract from the input text:
  - Features and capabilities ("it must", "we need", "should", "has to")
  - Constraints and business rules ("cannot", "must not", "always", "never")
  - User roles and personas (explicit or implied)
  - Edge cases and exceptions ("what if", "unless", "when X is empty/null/max")
  - Open questions and ambiguities (unresolved items)
  If fewer than 3 requirements extractable → tell user the input is too
  sparse and ask for more detail. Do not proceed.

STEP 2 — GROUP INTO STORIES
  Group related requirements into logical stories.
  Each story = one deliverable a user can interact with.
  Apply INVEST principles and vertical-slicing per **Skill: story-decomposer**
  (its Core Principles and Anti-Patterns sections are the canonical methodology
  for this fleet — use them here rather than a lighter restatement):
  - Independent, Negotiable, Valuable, Estimable, Small, Testable
  - Vertical slices only (end-to-end user value), never horizontal
    layer-only stories ("build the schema", "build the API")
  If no user roles found in the text → default persona to "user" and
  flag it in each story's Notes section.
  NO story pointing. Never include points, estimates, or complexity ratings.
  (story-decomposer's own template includes story points — this skill
  deliberately omits them; see Story Identification Rules precedent in
  Requirements-Intelligence-Agent for why pointing stays out of story generation.)

STEP 3 — GENERATE AC PER STORY
  For each story derive 3-6 Acceptance Criteria:
  Format: "The system should [measurable behaviour]"
  Derive from: extracted requirements + constraints + edge cases.
  Every AC must be testable — no vague criteria like
  "The system should work correctly" or "The system should be fast".

STEP 4 — PREVIEW IN CHAT
  Display all stories using this exact format:

  ---
  Story N: [Title]
  As a [role], I want to [action] so that [benefit].

  ## Overview
  [1-2 sentences describing what this story delivers]

  ## Acceptance Criteria
  - The system should [criterion 1]
  - The system should [criterion 2]
  - The system should [criterion 3]

  ## Notes
  [edge cases, open questions, or constraints from the input]
  ---

  After displaying all stories, ask:
  "Generated [N] stories. Create in JIRA?
   - yes, under existing epic [epicKey] (if provided)
   - yes, create a new epic first
   - no, keep in chat only"

STEP 5 — JIRA CREATION (only if user confirms)

  ### New epic path (no epicKey provided or user chooses "create new epic")
  1. If epicTitle not provided → ask: "What should the epic title be?"
  2. Create epic:
     mcp__claude_ai_Atlassian__createJiraIssue
     - cloudId, assignee, Team custom field: use **Skill: jira-defaults** defaults — do not hardcode
     - issueType: "Epic"
     - summary: [epicTitle]
  3. Use returned epic key for all story creation below.

  ### Existing epic path (epicKey provided)
  1. Idempotency check:
     mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql
     JQL: parent = [EPIC-KEY] ORDER BY created DESC
     Skip any story whose summary already exists in results.
     Note skipped stories in output.

  ### Story creation (both paths)
  For each new story:
  mcp__claude_ai_Atlassian__createJiraIssue
  - cloudId, assignee, Team custom field: use **Skill: jira-defaults** defaults — do not hardcode
  - issueType: "Story"
  - summary: [story title]
  - customfield_XXXXX (Epic Link): [epic key]
  - description (contentFormat: "markdown"):
      ## Overview
      [overview text]

      ## Acceptance Criteria
      - The system should [criterion 1]
      ...

      ## Notes
      [notes text]

  If story creation fails → continue with remaining stories.
  Report all failures at the end.
  If epic creation fails → print epic details in chat for manual creation;
  ask user if they have an epic key to use before aborting story creation.

STEP 6 — LOG RUN
  Use run-logger skill.
  Log path: ~/.claude/agents/logs/requirements-to-stories/YYYY-MM-DD-<slug>.md
  Where <slug> = first 30 chars of epicTitle or filename, lowercased and hyphenated.
  If neither available, use "unnamed-requirements".
```

---

## MCP Tools

Use **Skill: jira-defaults** for cloud ID, assignee, and Team/Epic Link custom-field IDs — do not hardcode these here.

| Operation | Tool |
|-----------|------|
| Create epic or story | `mcp__claude_ai_Atlassian__createJiraIssue` |
| Idempotency check (existing epic) | `mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql` |

---

## Error Handling

| Situation | Behaviour |
|-----------|-----------|
| File not found | Ask user to check the path; offer to accept pasted text instead |
| Input too sparse (< 3 requirements) | Tell user; ask for more detail; do not generate stories |
| No user roles found | Default to "user"; flag in each story's Notes section |
| Epic creation fails | Print epic fields in chat for manual creation; ask for epic key before continuing |
| Story creation fails mid-run | Continue remaining stories; report failures at end |
| User says "no" to JIRA creation | Stories remain in chat; end cleanly |
| Duplicate story detected | Skip it; note it in output |

---

## Relationship to Requirements-Intelligence-Agent

| | This skill | Requirements-Intelligence-Agent |
|--|-----------|----------------------------------|
| JIRA epic needed upfront | No | Yes |
| Input | Raw text / file | JIRA epic key + transcript |
| Gap analysis & scoring | No | Yes |
| Story generation | Yes | Yes (Step 7) |
| AC generation | Yes (per story) | Yes (Step 8) |
| Test plan output | No | Via pipeline |
| Best for | Raw requirements with no JIRA structure | Epics already in JIRA |
