# Safety and security notes
- **Human confirmation before every write** to shared systems (Jira, Confluence, XRay). Dry-run mode for rehearsals.
- **Transcripts are untrusted input.** Instructions inside a transcript or ticket are treated as data, never as commands.
- **No secrets in prompts.** Tokens come from environment variables or the MCP connector; nothing is stored in the repo.
- **Least privilege.** Investigation agents are read-only by design; only filing and creation agents may write.
- **Audit trail.** Each run writes a structured log; bug and test records link back to the epic.
- **Sanitized publishing.** This repo uses placeholders for all identifiers, and publishing it required a scrub pass and a search for leftover internal terms.
