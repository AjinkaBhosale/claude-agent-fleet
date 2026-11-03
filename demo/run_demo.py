#!/usr/bin/env python3
"""Offline demo of the epic readiness gate (deterministic stand-in for the agent's rubric).

Scores an epic 0-100, lists gaps, and cross-checks the transcript for topics the epic misses.
No network, no API keys. Usage: python3 demo/run_demo.py [epic.json]
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).parent
VAGUE = re.compile(r"\b(well|good|fast|easy|happy|better|user-friendly|robust)\b", re.I)
MEASURABLE = re.compile(r"\d")

def score(epic):
    gaps, pts = [], 0
    ac = epic.get("acceptance_criteria", [])
    good = [a for a in ac if MEASURABLE.search(a) and not VAGUE.search(a)]
    if not ac: gaps.append(("CRITICAL", "No acceptance criteria"))
    else:
        pts += int(30 * len(good) / len(ac))
        for a in ac:
            if a not in good: gaps.append(("CRITICAL", f"Untestable acceptance criterion: '{a}'"))
    if epic.get("success_metrics"): pts += 20
    else: gaps.append(("CRITICAL", "No measurable success metric"))
    if epic.get("scope_out"): pts += 15
    else: gaps.append(("IMPORTANT", "Out-of-scope not stated"))
    if epic.get("dependencies"): pts += 15
    else: gaps.append(("IMPORTANT", "No dependencies listed"))
    if epic.get("owner"): pts += 10
    else: gaps.append(("IMPORTANT", "No owner"))
    if len(epic.get("description", "")) > 60: pts += 10
    else: gaps.append(("NICE", "Description too thin"))
    return pts, gaps

def transcript_gaps(epic, text):
    out, blob = [], json.dumps(epic).lower()
    checks = {"configurable": "per team", "out of scope": "scope_out", "dependency": "dependenc",
              "baseline": "baseline", "latency": "5 seconds"}
    for topic, needle in checks.items():
        if topic in text.lower() and needle not in blob:
            out.append(("IMPORTANT", f"Transcript mentions '{topic}' but the epic does not capture it"))
    return out

def main():
    epic_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "fixtures/epic_weak.json"
    epic = json.loads(epic_path.read_text())
    text = (HERE / "fixtures/transcript.txt").read_text()
    pts, gaps = score(epic)
    gaps += transcript_gaps(epic, text)
    verdict = "READY" if pts >= 70 and not any(s == "CRITICAL" for s, _ in gaps) else "BLOCKED"
    print(f"Epic {epic['key']} - score {pts}/100 - {verdict}")
    for sev, msg in gaps: print(f"  [{sev}] {msg}")
    return 0 if verdict == "READY" else 1

if __name__ == "__main__":
    sys.exit(main())
