---
name: adf-formatter
description: How to format Jira custom field values as Atlassian Document Format (ADF) — required for description, custom text fields, and comments via MCP
---

# Atlassian Document Format (ADF)

Jira MCP calls require **ADF objects** for `description` and rich-text custom fields — plain strings will be rejected.

## Minimal ADF Paragraph

```json
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "Your text here"
        }
      ]
    }
  ]
}
```

## ADF with Multiple Paragraphs

```json
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "paragraph",
      "content": [{ "type": "text", "text": "First paragraph." }]
    },
    {
      "type": "paragraph",
      "content": [{ "type": "text", "text": "Second paragraph." }]
    }
  ]
}
```

## ADF Bullet List

```json
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "bulletList",
      "content": [
        {
          "type": "listItem",
          "content": [
            { "type": "paragraph", "content": [{ "type": "text", "text": "Item 1" }] }
          ]
        },
        {
          "type": "listItem",
          "content": [
            { "type": "paragraph", "content": [{ "type": "text", "text": "Item 2" }] }
          ]
        }
      ]
    }
  ]
}
```

## ADF Heading + Body

```json
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "heading",
      "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "Section Title" }]
    },
    {
      "type": "paragraph",
      "content": [{ "type": "text", "text": "Body text here." }]
    }
  ]
}
```

## ADF Ordered List (Numbered Steps)

For numbered steps such as Steps-to-Reproduce custom fields. Use this when input text uses `1.`, `2.`, `3.` numbering or when content is sequential procedural steps.

```json
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "orderedList",
      "attrs": { "order": 1 },
      "content": [
        {
          "type": "listItem",
          "content": [
            { "type": "paragraph", "content": [{ "type": "text", "text": "First step" }] }
          ]
        },
        {
          "type": "listItem",
          "content": [
            { "type": "paragraph", "content": [{ "type": "text", "text": "Second step" }] }
          ]
        }
      ]
    }
  ]
}
```

When parsing input text, strip leading `\d+[\.\)]\s*` from each line before placing it in the `text` field.

## ADF Code Block (Stack Traces, Logs)

For multi-line technical content like stack traces, error logs, or code snippets. Always use `language: "none"` unless the content is genuinely a recognised language.

```json
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "codeBlock",
      "attrs": { "language": "none" },
      "content": [
        { "type": "text", "text": "Error: connect ETIMEDOUT 10.0.0.1:443\n    at TCPConnectWrap.afterConnect" }
      ]
    }
  ]
}
```

## ADF Mixed Content (Description with Multiple Blocks)

For full bug descriptions that combine paragraphs, lists, and code blocks. Compose by appending each block to `content[]`:

```json
{
  "type": "doc",
  "version": 1,
  "content": [
    { "type": "heading", "attrs": { "level": 2 }, "content": [{ "type": "text", "text": "Steps to Reproduce" }] },
    { "type": "orderedList", "attrs": { "order": 1 }, "content": [
      { "type": "listItem", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Step 1" }] }] },
      { "type": "listItem", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Step 2" }] }] }
    ] },
    { "type": "heading", "attrs": { "level": 2 }, "content": [{ "type": "text", "text": "Error Details" }] },
    { "type": "codeBlock", "attrs": { "language": "none" }, "content": [{ "type": "text", "text": "stack trace text" }] }
  ]
}
```

## ADF Mentions (CRITICAL — required for any comment that tags a person)

**Any comment that tags a person MUST be posted as ADF with a real `mention` node — never the markdown `[~accountid:...]` / `[~owner]` shorthand.** That markdown shorthand is escaped to literal text by the MCP markdown converter (it is not valid CommonMark), so it renders as visible text but sends **no notification ping**. This was a real production failure (PROJ-103, 2026-07-14): a comment tagging four people posted successfully and displayed the names, but nobody was notified.

**Procedure for every notification comment:**

1. **Resolve each person to an accountId** — never guess or hardcode:
   - Prefer values already on the issue: `epic.fields.assignee.accountId`, `reporter.accountId`.
   - Otherwise use `mcp__claude_ai_Atlassian__lookupJiraAccountId` (cloud ID from `jira-defaults`) with the email/name.
   - Both accountId formats are valid: `<ACCOUNT_ID>` (hex) and `712020:<uuid>` (tenant:uuid).
2. **Post the comment with `contentFormat: "adf"`**, building the body as a raw ADF document. Each mention is a node:
   ```json
   { "type": "mention", "attrs": { "id": "<accountId>", "text": "@Display Name" } }
   ```
   embedded in a paragraph's `content` array alongside `text` nodes, e.g.:
   ```json
   {
     "type": "doc", "version": 1,
     "content": [
       { "type": "paragraph", "content": [
         { "type": "mention", "attrs": { "id": "<ACCOUNT_ID>", "text": "@Shreyansh Lunawat" } },
         { "type": "text", "text": " Epic scope updated — please review." }
       ]}
     ]
   }
   ```
3. **Verify** the response renders the mention server-side (a live mention element), not escaped text. If a mention comes back as literal `[~owner]` text, you used markdown by mistake — switch to ADF and re-post.

**Any agent-authored template using `[~<owner>]`-style placeholders is authoring shorthand only** — resolve each to an ADF `mention` node at post time. Never send `[~owner]` verbatim as the literal comment body.

This applies to every agent that posts Jira comments with @mentions (bug-filing-agent, Epic-Gap-Resolver-Agent, Requirements-Intelligence-Agent, jira-test-case-creator-agent, etc.) — not just one. If your agent's comment template shows `[~owner]`, treat that as a reminder to apply this procedure, not literal content to send.

## Safety Rule — Validation Before Submission

Before posting ADF to JIRA, verify these invariants:

1. Top-level object has `"type": "doc"`, `"version": 1`, and `"content"` is a non-empty array
2. Every `text` node has a non-null `text` field (empty string is rejected by JIRA)
3. `listItem` always contains at least one `paragraph` child — listItems cannot contain bare text nodes
4. `codeBlock.content` is an array of `text` nodes only — never paragraphs

**If any invariant fails**: the agent calling this skill MUST NOT submit the ADF to a custom field. The agent must fall back to including the content in the description body (which has more permissive validation) and surface a warning to the user.

## Rules

- Always use `"version": 1`
- `description` field on Jira issues **must** be ADF — never a plain string
- For comments (`addCommentToJiraIssue`), the `body` field must also be ADF
- Any comment that @mentions a person **must** use `contentFormat: "adf"` with real `mention` nodes — see **ADF Mentions (CRITICAL)** above; markdown mentions silently fail to notify
- Custom text fields (e.g. acceptance criteria) that accept rich text must use ADF
- Simple string fields (summary, priority, labels) do NOT use ADF — use plain strings
