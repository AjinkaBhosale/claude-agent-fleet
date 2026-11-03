# Claude Code Agent Fleet — QA & Delivery Automation

A set of Claude Code **sub-agents** and **skills** I designed and ran day to day to automate the delivery loop of an analytics product team: from a discovery-meeting transcript, to a readiness-scored epic, to stories with acceptance criteria, to test plans and Jira/XRay test cases, to Playwright execution and failure triage, to filed bugs.

> All company-specific names, IDs, URLs and data have been replaced with neutral placeholders (`PROJ-123`, `example.atlassian.net`, `<CLOUD_ID>`). Prompts and workflows are shown as design examples, not as a runnable drop-in for any particular company.

## Why
Manual grooming and test-failure triage were slow and inconsistent. The goal: repeatable, auditable agent workflows with human confirmation at every write to a shared system.

## Architecture
See [docs/architecture.md](docs/architecture.md) for the full Mermaid diagram.

```
Transcript + Epic -> Requirements-Intelligence-Agent -> quality gate (blocking)
   -> Epic-Gap-Resolver-Agent (if blocked) -> stories + AC (preview, confirm, create)
   -> test plan + BDD tests -> Playwright run + triage -> linked bug (after confirmation)
```

## Try it in two minutes (no keys needed)
```
python3 demo/run_demo.py                                  # weak epic: BLOCKED, with gaps
python3 demo/run_demo.py demo/fixtures/epic_good.json     # strong epic: READY
python3 tools/lint_fleet.py && python3 -m pytest -q tests # fleet lint + tests
```
The demo is a deterministic stand-in for the gate's rubric, so the behaviour can be shown and tested offline; the real agents apply the same idea with an LLM.

## What is in the repo
| Path | Contents |
|---|---|
| `agents/` | 16 agents: requirements, test planning, Playwright, bug filing/investigation, API testing, fleet audit |
| `skills/` | 15 reusable skills: Jira conventions, ADF formatting, epic gates, story decomposition, logging, Playwright rules |
| `demo/`, `tests/`, `tools/` | Offline demo, tests, and a fleet linter (CI runs them) |
| `docs/` | Architecture diagram, decisions and trade-offs, safety notes, quickstart |

## Design decisions worth discussing
1. **Single source of config.** Cloud IDs, field IDs and parent pages live in one skill (`jira-defaults`); agents reference it and never hardcode.
2. **Human-in-the-loop on writes.** Preview, then confirm, then create. Dry-run and pipeline modes exist for automation.
3. **Blocking quality gates with shared vocabulary.** One severity/risk contract (`epic-readiness-gate-conventions`) reused by every gate, so results are comparable.
4. **Consolidate, don't accumulate.** Overlapping agents were audited and superseded; old ones carry a pointer to the replacement. A health-auditor agent checks that every referenced agent, tool and hook really exists.
5. **Honest triage.** The failure analyzer separates test-infrastructure problems (fixed in test code) from product bugs (drafted, filed only after confirmation), and treats "green with skips" as something to verify.
6. **Evidence and logs.** Every run writes a structured log; bug reports carry screenshots/logs and links back to the test case and epic.
7. **Verified IDs.** Custom-field and account IDs are re-verified against live metadata instead of trusted from memory.

## Case studies
### 1. Transcript to ready epic
*Problem:* discovery decisions were lost between the meeting and the ticket. *Approach:* score the epic against the transcript, list gaps, propose stories with measurable AC, create after confirmation. *Result:* consistent story quality and a traceable gap history. *Next:* auto-detect owners and stale gaps.

### 2. Test plan and XRay generation
*Problem:* slow, inconsistent test documentation. *Approach:* a gatekeeper rejects epics that are not ready, then the agent generates a Confluence plan and BDD tests linked to the epic. *Next:* generate Playwright specs from the same BDD source.

### 3. Failure triage and fleet health
*Problem:* flaky runs hid real bugs; the agent fleet itself grew messy. *Approach:* classify every failure, account for each skip, audit agents, skills and hooks for broken references. *Next:* scheduled weekly audit.

## Tech
Claude Code (agents, skills, hooks, MCP), Jira/Confluence/XRay via MCP, Playwright (TypeScript), Postman, Snowflake for data checks, GitHub.

## Fill in before sharing
Add your own numbers only where you are permitted to (agents built, hours saved, tests generated), and a short screen recording run on dummy data.
