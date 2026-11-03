---
name: execution-logging-template
description: "Shared execution logging format used by all QA agents. Reference when you need the standard per-step table and final summary template instead of inlining the boilerplate."
model: sonnet
color: cyan
---

# Execution Logging Template

All QA agents in this project use a consistent execution logging format. Apply it as follows.

## Token Estimation Rules

- 1 token ≈ 4 characters of text
- Code generation: ~1 token per 4 chars of code
- File reads: ~50 input tokens, then ~1 token per 4 chars of output
- Bash commands: ~50–100 input, ~200–2000 output depending on test count
- Jira/Confluence tool calls: ~300–500 input, ~100–300 output
- Playwright MCP interactions: ~100–300 tokens per action

## Tool Categories

- `file` — Read, Write, Edit, Glob, Grep
- `browser` — Playwright MCP tools (navigate, click, snapshot)
- `system` — Bash, Git commands
- `jira` — Atlassian MCP tools (Jira, Confluence)

## Per-Step Logging Format

After each significant step, output:

```markdown
### Step [N]: [Description]
**Timestamp**: [Current time]
**Duration**: [Xs]

#### Tool Execution
| Tool | Category | Input Tokens | Output Tokens | Duration | Status |
|------|----------|--------------|---------------|----------|--------|
| [tool] | [category] | [est] | [est] | [Xs] | ✅/❌ |

**Parameters**: [Key params used]
**Result**: [One-line summary]
---
```

## Final Execution Summary Format

At the end of every agent run, output:

```markdown
## Execution Summary

### Task Overview
- **Agent**: [agent-name]
- **Task**: [brief description]
- **Status**: Success / Failed / Partial
- **Total Duration**: [Xm Xs]

### Token Usage
| Metric | Count |
|--------|-------|
| Total Input Tokens | [X] |
| Total Output Tokens | [X] |
| **Total Tokens** | **[X]** |

### Tool Usage
| Tool | Category | Calls | Duration | Tokens (In/Out) |
|------|----------|-------|----------|-----------------|
| [tool] | [cat] | [N] | [Xs] | [X/X] |
| **Total** | — | **[N]** | **[Xs]** | **[X/X]** |

### Time Breakdown
| Phase | Duration | % of Total |
|-------|----------|------------|
| [Phase name] | [Xs] | [X%] |
```

## Usage Note

Replace the long inline `## Execution Logging (MANDATORY)` section in each agent with:

```markdown
## Execution Logging

Use the **execution-logging-template** skill for per-step and final summary logging format.

At the end of every run, use the **run-logger** skill to write an execution log to:
`~/.claude/agents/logs/[agent-name]/YYYY-MM-DD-<task-identifier>.md`
```
