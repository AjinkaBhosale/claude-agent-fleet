---
name: confluence-publisher
description: "Use when publishing pipeline output (epics, user stories, quality-gate assessments) to a Confluence page."
---

# Confluence Publisher Skill

## Purpose
Publishes pipeline output (epics, user stories, quality gate assessments) to a user-specified Confluence page.

## Trigger
When user requests to publish pipeline results to Confluence or save output to wiki.

## Input Requirements

### Required User Input
1. **Space Key** - Confluence space identifier (e.g., `ENG`, `DEV`)
2. **Parent Page ID or Path** - Either:
   - Numeric page ID (e.g., `0000000000`)
   - Page path/title under which to create the new page
3. **Page Title** - Title for the new Confluence page

### Pipeline Output (Auto-collected)
- Epic definition with acceptance criteria
- User stories with story points
- Quality gate assessment scores
- Discovery extraction summary (if available)

## Execution Steps

### Step 1: Gather User Input
Prompt the user for:
```
Please provide Confluence publishing details:
1. Space Key (e.g., 'ENG'):
2. Parent Page ID or title:
3. New Page Title:
```

### Step 2: Retrieve Credentials
Read Atlassian credentials from `~/.claude/settings.json`:
```json
{
  "mcpServers": {
    "atlassian": {
      "env": {
        "ATLASSIAN_SITE_URL": "https://example.atlassian.net",
        "ATLASSIAN_USER_EMAIL": "<email>",
        "ATLASSIAN_API_TOKEN": "<token>"
      }
    }
  }
}
```

### Step 3: Format Content for Confluence
Convert pipeline output to Confluence Storage Format (XHTML):

#### Epic Section
```xml
<h1>Epic: {epic_title}</h1>
<ac:structured-macro ac:name="panel">
  <ac:parameter ac:name="title">Epic Summary</ac:parameter>
  <ac:rich-text-body>
    <p><strong>Business Value:</strong> {business_value}</p>
    <p><strong>Scope:</strong> {scope}</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>Acceptance Criteria</h2>
<ul>
  {acceptance_criteria_list}
</ul>
```

#### User Stories Section
```xml
<h2>User Stories</h2>
<table>
  <tr>
    <th>Story</th>
    <th>Points</th>
    <th>Acceptance Criteria</th>
  </tr>
  {story_rows}
</table>
```

#### Quality Gate Section
```xml
<h2>Quality Gate Assessment</h2>
<ac:structured-macro ac:name="status">
  <ac:parameter ac:name="colour">{pass_color}</ac:parameter>
  <ac:parameter ac:name="title">{score}/100 - {status}</ac:parameter>
</ac:structured-macro>

<table>
  <tr><th>Category</th><th>Score</th><th>Max</th></tr>
  {score_breakdown_rows}
</table>
```

### Step 4: Create Confluence Page via API

#### Find Parent Page ID (if title provided)
```bash
curl -s -X GET \
  "https://{site}/wiki/rest/api/content?title={parent_title}&spaceKey={space_key}&expand=version" \
  -H "Authorization: Basic {base64_credentials}" \
  -H "Content-Type: application/json"
```

#### Create New Page
```bash
curl -s -X POST \
  "https://{site}/wiki/rest/api/content" \
  -H "Authorization: Basic {base64_credentials}" \
  -H "Content-Type: application/json" \
  -d @payload.json
```

Payload structure:
```json
{
  "type": "page",
  "title": "{page_title}",
  "space": {"key": "{space_key}"},
  "ancestors": [{"id": "{parent_page_id}"}],
  "body": {
    "storage": {
      "value": "{confluence_storage_format_content}",
      "representation": "storage"
    }
  }
}
```

### Step 5: Return Confirmation
Provide the user with:
- Created page URL: `https://{site}/wiki/spaces/{space_key}/pages/{page_id}/{page_title}`
- Page ID for future reference
- Confirmation of content published

## Output Format

### Success Response
```
Confluence Page Created Successfully

Page Title: {title}
Space: {space_key}
Page ID: {page_id}
URL: {page_url}

Content Published:
- Epic: {epic_title}
- User Stories: {story_count} stories ({total_points} points)
- Quality Gate: {score}/100 ({status})
```

### Error Handling
| Error | Resolution |
|-------|------------|
| 401 Unauthorized | Verify credentials in ~/.claude/settings.json |
| 404 Space/Parent not found | Verify space key and parent page ID |
| 400 Title exists | Append timestamp or prompt for new title |
| Network error | Retry with exponential backoff |

## Example Usage

### User Prompt
```
/confluence-publish
```

### Agent Response
```
Please provide Confluence publishing details:
1. Space Key (e.g., 'ENG'): ENG
2. Parent Page ID or title: AI Experiment Lab
3. New Page Title: Assist Opportunity - Pipeline Results

Publishing pipeline output to Confluence...

Confluence Page Created Successfully

Page Title: Assist Opportunity - Pipeline Results
Space: ENG
Page ID: 0000000000
URL: https://example.atlassian.net/wiki/spaces/<SPACE_KEY>/pages/0000000000

Content Published:
- Epic: Implement IEX Integration for Agent Augmentation and Scheduling Automation
- User Stories: 8 stories (36 points)
- Quality Gate: 82/100 (PASS - Good)
```

## Dependencies
- Atlassian credentials configured in `~/.claude/settings.json`
- curl available in environment
- Pipeline must have been executed with output available

## Related Skills
- `transcript-intelligence-skill.md` - Source of discovery extraction
- `epic-structurer-skill.md` - Source of epic definition
- `story-decomposer-skill.md` - Source of user stories
- `epic-quality-gate-skill.md` - Source of quality assessment

---

## Hook: Run Logger

At the end of every invocation, write a log file to:
`.claude/logs/confluence-publisher-skill/YYYY-MM-DD-<page-title>.md`

**Log file content:**

```markdown
# Confluence Publisher Skill — Run Log
**Date:** YYYY-MM-DD HH:MM
**Input:** Page title or epic key
**Status:** COMPLETE | BLOCKED | PARTIAL

## Actions Taken
- <e.g. "Published discovery output for PROJ-102 to Confluence">
- <e.g. "Page URL: <URL>">

## Output
- Page Created: <URL> | Status: Published/Draft

## Key Points
- <notable decision or assumption>

## Next Steps
- <what should happen next>
```
