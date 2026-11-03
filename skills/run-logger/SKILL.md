---
name: run-logger
description: Standard execution logging template for all agents — write a run log to ~/.claude/agents/logs/ after every agent execution
---

# Agent Run Logger

Every agent must write an execution log at the end of each run. This skill defines the standard format.

## Log File Location

```
~/.claude/agents/logs/<agent-name>/YYYY-MM-DD-<key-identifier>.md
```

**Key identifier**: the Jira ticket ID, epic key, test name, or primary input — whichever is most searchable. Use lowercase with hyphens.

Examples:
- `~/.claude/agents/logs/jira-test-plan-generator/2026-06-15-PROJ-102.md`
- `~/.claude/agents/logs/bug-filing-agent/2026-06-15-PROJ-122.md`
- `~/.claude/agents/logs/playwright-test-runner/2026-06-15-smoke-ENV.md`

## Log Format

```markdown
# <Agent Name> — Run Log
**Date**: YYYY-MM-DD HH:MM
**Input**: <primary input — ticket ID, file, tag, etc.>
**Status**: ✅ Success | ❌ Failed | ⚠️ Partial

## Summary
<1-3 sentences: what was done and what was the outcome>

## Steps Completed
- [ ] Step 1 description — result
- [ ] Step 2 description — result
...

## Tool Calls
| Tool | Purpose | Result |
|------|---------|--------|
| mcp__claude_ai_Atlassian__getJiraIssue | Fetch epic PROJ-102 | ✅ |
| mcp__claude_ai_Atlassian__createConfluencePage | Publish test plan | ✅ |

## Outputs
- <links, file paths, or IDs of things created>

## Errors / Notes
<any warnings, skipped steps, or follow-up needed>
```

## Instructions

1. Create the log directory if it doesn't exist: `~/.claude/agents/logs/<agent-name>/`
2. Write the log file at the END of the agent run (success or failure)
3. Use absolute paths — never relative paths for log files
4. If the run partially failed, still write the log with status `⚠️ Partial` and note what failed
