---
name: jira-defaults
description: Shared Jira/Confluence constants and QA defaults for all agents — cloud ID, URLs, assignee, team, space keys, parent page IDs (template: replace placeholders)
---

# Jira & Confluence Defaults (template)

Single source of truth for Jira/Confluence MCP calls. Agents reference this skill instead of hardcoding values inline. Replace every `<PLACEHOLDER>` with your own values.

## Atlassian Connection
| Key | Value |
|-----|-------|
| Cloud ID | `<CLOUD_ID>` |
| Base URL | `https://<your-site>.atlassian.net` |
| Jira Project | `PROJ` |

## QA Defaults (apply unless overridden)
| Field | Value |
|-------|-------|
| Assignee | `<your-email>` |
| Team | `<TEAM_NAME>` (option id `<TEAM_OPTION_ID>`) |
| Test Status on Create | `Under Review` |

## Confluence Defaults
| Key | Value |
|-----|-------|
| Space Key | `<SPACE_KEY>` |
| Test Plans Parent Page ID | `<PAGE_ID>` |
| General Parent Page ID | `<PAGE_ID>` |

## Jira Custom Fields (verify against createmeta for your instance)
| Field | ID | Value format |
|-------|----|--------------|
| Team Name | `customfield_XXXXX` | `{"id":"<TEAM_OPTION_ID>"}` |
| Story Points | `customfield_XXXXX` | number |
| Fix versions | `fixVersions` | `[{"id":"<VERSION_ID>"}]` |
| Components | `components` | `[{"name":"<COMPONENT>"}]` |
| Epic | `parent` | epic key (not Epic Link) |

Some workflow transitions (e.g. New → Ready for Dev) require Team, Story Points, Fix versions and Components. See skill `jira-expert`.

## Standard Stakeholders
Tag these on epic-level readiness/gap comments, plus the epic assignee. Resolve accountIds with `lookupJiraAccountId`; never guess.

| Role | accountId |
|------|-----------|
| Product Owner | `<ACCOUNT_ID>` |
| Tech Lead | `<ACCOUNT_ID>` |

Mentions must use ADF `mention` nodes, not markdown shorthand (see skill `adf-formatter`).
