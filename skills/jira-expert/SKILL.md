---
name: jira-expert
description: Use when the user asks to check, create, update, transition, triage, or report on Jira issues in the PROJ project - stories, tasks, bugs, subtasks, epics, sprint status, "my open tickets", "what's blocked", standup or sprint summaries, or when a Jira transition/create fails on required fields (Fix versions, Story Points, Team Name, Components).
---

# Jira Expert (PROJ, team <TEAM_NAME>)

## Overview
Act as a Jira power-user for the user's team. Read freely; **write only after the user confirms**. Fields are never invented: they are copied from a live reference issue of the team's current sprint.

Connection: cloudId `<UUID>`, site `https://example.atlassian.net`, project `PROJ`. Atlassian tools are deferred: load them with ToolSearch (`select:mcp__plugin_engineering_atlassian__searchJiraIssuesUsingJql,...getJiraIssue,...createJiraIssue,...editJiraIssue,...transitionJiraIssue,...getTransitionsForJiraIssue,...lookupJiraAccountId,...addCommentToJiraIssue,...createIssueLink`).

## Verified field IDs (PROJ, checked 2026-10-02)
| Field | ID | Value format |
|---|---|---|
| Team Name | `customfield_XXXXX` | `{"id":"<TEAM_OPTION_ID>"}` = "<TEAM_NAME>". **Always this team.** JQL: `"Team Name" = "<TEAM_NAME>"` |
| Story Points | `customfield_XXXXX` | number |
| Sprint | `customfield_XXXXX` | read-only here |
| Fix versions | `fixVersions` | `[{"id":"<VERSION_ID>"}]` (26.4 at time of check) |
| Components | `components` | `[{"name":"Actions"}]` |
| Epic link | `parent` | epic key |
| Capitalize | `customfield_XXXXX` | `{"id":"11177"}`. Required to move to In Progress. Cost-accounting choice: **ask the user**, never default. Options: 11175 Cap-Architecture/LL design, 11176 Cap-Bug fix (not in prod), 11177 Cap-New Product Dev, 11178 NonCap-Bug fix (in prod), 11179 NonCap-NFR, 11180 NonCap-Tech research/POC |

Transitions can require different fields at each step (New → Ready for Dev needed Fix versions, Story Points, Team Name, Components; Ready for Dev → In Progress needed Capitalize). Check the transition's required fields with `getTransitionsForJiraIssue(transitionId, expand="transitions.fields")` (huge output, so save to a file and parse it).

`customfield_XXXXX` / `10016` (Team / Story Points in the `jira-defaults` skill) are **wrong for PROJ**: they return null. Use the IDs above. If a create or transition errors with an unknown field, re-discover with `getJiraIssueTypeMetaWithFields(projectIdOrKey=PROJ, issueTypeId, requiredFieldsOnly=false)`. The output is huge, so save it to a file and grep or parse it.

## Reference-issue rule (before any create, or any transition that asks for required fields)
1. Run: `project = PROJ AND "Team Name" = "<TEAM_NAME>" AND sprint in openSprints() ORDER BY updated DESC` with fields `fixVersions, components, customfield_XXXXX, customfield_XXXXX, assignee, issuetype`.
2. Take **Fix version** and **Team** from those results (use the most common fix version). Take **Components** from the sibling issues in the same epic or area, else the most common.
3. **Story Points:** propose a value by matching the size of similar team issues (scale seen: 1, 2, 3, 5, 8, 13). State the proposal and why.
4. Show the user the full field set and get a yes before writing.

## Create workflow
1. Clarify type: Epic, Story, Task, Bug, or Sub-task. Sub-tasks need `parent` = story and often a different required-field set, so check createmeta for that issue type.
2. **Ask who to assign.** Offer the user (`user@example.com`, accountId `<ACCOUNT_ID>`) and the assignees seen in the sprint query. Resolve other names with `lookupJiraAccountId`; never guess IDs. Unassigned only if the user says so.
3. Apply the reference-issue rule, preview the issue (summary, description, assignee, parent, team, fix version, points, components), wait for confirmation, create.
4. Link to the epic via `parent`; add `createIssueLink` for blocks/relates when asked.
5. Descriptions: markdown with a Goal, Scope and Acceptance criteria. For custom ADF fields or mentions, use the `adf-formatter` skill.
6. After creating, report keys and URLs.

## Status workflow
- Read transitions with `getTransitionsForJiraIssue`; the available set depends on the current status (seen: New → Ready for Dev → In Progress → In Review → Done).
- Transitions can be blocked by required fields. Fill them from the reference-issue rule, confirm, then retry. Do not guess values.
- Propose status changes from evidence (subtasks done, PR merged, work finished) and ask before moving. Never move an issue to Done on inference alone.
- Parent stories should follow their subtasks: all subtasks Done means propose Done; any In Progress means the parent is In Progress.

## Getting more from Jira (offer proactively, once, briefly)
| Need | JQL / action |
|---|---|
| My open work | `assignee = currentUser() AND statusCategory != Done ORDER BY updated DESC` |
| Team sprint board | `"Team Name" = "<TEAM_NAME>" AND sprint in openSprints()` |
| Stale in-progress | `... AND status = "In Progress" AND updated <= -5d` |
| Unassigned or unpointed | `... AND (assignee is EMPTY OR "Story Points" is EMPTY)` |
| Epic rollup | `parent = EPIC-KEY`, then subtasks via `parent in (...)` (the first query only returns direct children) |
| Missing fields before sprint | `fixVersion is EMPTY OR component is EMPTY` |
| Standup | Yesterday's updates: `assignee = currentUser() AND updated >= -1d` |
| Time | `addWorklogToJiraIssue` when the user logs effort |

Also: summarize an epic's health (done vs in progress vs new, who is blocked), flag parent/child status mismatches, draft acceptance criteria, and split large stories (13+ points) into subtasks.

## Rules
- Read-only calls need no confirmation. Create, edit, transition, comment, link and worklog calls do.
- Batch independent reads in parallel; use `fields` lists to keep responses small (never `*all` on searches).
- A search returns only direct children of an epic; fetch subtasks with a second `parent in (...)` query.
- Never put real people's names or emails in new issue text beyond assignee fields.

## Common mistakes
| Mistake | Fix |
|---|---|
| Using `customfield_XXXXX` / `10016` | Use 10098 / 10038 |
| Team as plain text "<team name>" | Option object `{"id":"<TEAM_OPTION_ID>"}` |
| Creating without asking the assignee | Always ask first |
| Retrying a failed transition unchanged | Read the required-field list and fill it from a sprint reference issue |
| Reporting only the epic's direct children | Also query subtasks |
