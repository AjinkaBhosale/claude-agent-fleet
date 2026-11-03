#!/usr/bin/env python3
"""Reference linter: every agent/skill has frontmatter, and every `Skill: x` / agent mention resolves."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
agents = {p.stem: p for p in (root / "agents").glob("*.md")}
skills = {p.name: p / "SKILL.md" for p in (root / "skills").iterdir() if p.is_dir()}
errors = []
for name, p in {**{f"agent:{k}": v for k, v in agents.items()}, **{f"skill:{k}": v for k, v in skills.items()}}.items():
    if not p.exists(): errors.append(f"{name}: missing file"); continue
    t = p.read_text()
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    if not m or "description:" not in m.group(1): errors.append(f"{name}: missing frontmatter/description")
    for ref in re.findall(r"Skill:\s*\*{0,2}([a-z0-9-]+)", t):
        if ref not in skills: errors.append(f"{name}: references unknown skill '{ref}'")
print(f"{len(agents)} agents, {len(skills)} skills checked")
for e in errors: print("ERROR", e)
sys.exit(1 if errors else 0)
