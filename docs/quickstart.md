# Quickstart
1. Run the offline demo: `python3 demo/run_demo.py` (weak epic, blocked) and `python3 demo/run_demo.py demo/fixtures/epic_good.json` (ready).
2. Check the fleet: `python3 tools/lint_fleet.py`, then `pip install pytest && python3 -m pytest -q tests`.
3. Use with Claude Code: copy `agents/` and `skills/` into `~/.claude/`, fill in `skills/jira-defaults/SKILL.md` with your site, project and field IDs, then connect an Atlassian MCP server.
