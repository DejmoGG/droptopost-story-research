"""Split a Report B desk file (reports/YYYY-MM-DD.desk.json) into one JSON file per story,
ready for an ArtifactData batch write to the Story Desk's `stories` collection.

usage: python shared/tools/desk_split.py droptopost-research/reports/2026-11-03.desk.json OUT_DIR
prints one line per story: <doc_id> <file path>
"""
import json, os, sys

src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src, encoding="utf-8"))
os.makedirs(out, exist_ok=True)
for s in d["stories"]:
    doc = {k: v for k, v in s.items() if k != "id"}
    doc.setdefault("round", d["round"])
    p = os.path.join(out, s["id"] + ".json")
    json.dump(doc, open(p, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=2)
    print(s["id"], os.path.abspath(p))
