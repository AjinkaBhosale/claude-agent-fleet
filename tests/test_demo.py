import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "demo"))
import run_demo
F = pathlib.Path(__file__).resolve().parent.parent / "demo/fixtures"
load = lambda n: json.loads((F / n).read_text())

def test_weak_epic_is_blocked():
    pts, gaps = run_demo.score(load("epic_weak.json"))
    assert pts < 70 and any(s == "CRITICAL" for s, _ in gaps)

def test_good_epic_is_ready():
    pts, gaps = run_demo.score(load("epic_good.json"))
    assert pts >= 70 and not any(s == "CRITICAL" for s, _ in gaps)

def test_transcript_gaps_flagged_for_weak_epic():
    assert run_demo.transcript_gaps(load("epic_weak.json"), (F / "transcript.txt").read_text())
