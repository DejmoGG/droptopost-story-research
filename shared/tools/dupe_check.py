"""Flag possible repeats in a new report against everything shown before.

Checks two things against the global index and every earlier report in both
systems: (1) the same URL, (2) a specific person/company name from the index
appearing in a new card. Warnings are for review: a shared generic name is
not automatically a repeat, and a real UPDATE card is allowed.

Usage: python3 shared/tools/dupe_check.py <new-report.md>
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "shared" / "global-story-index" / "index.md"
# Names too generic to signal a repeat on their own.
GENERIC = {"tiktok", "youtube", "instagram", "reddit", "google", "amazon", "tesco",
           "sec", "us doj", "fbi", "openai", "chatgpt", "meta", "facebook", "x",
           "twitter", "netflix", "shark tank", "wix", "jpmorgan", "barclays",
           "goldman sachs", "hindenburg", "tiktok shop", "bandai namco"}

new_path = Path(sys.argv[1]).resolve()
new_text = new_path.read_text(encoding="utf-8")
cards = re.split(r"\n(?=### )", new_text)

# Index rows: | ID | First shown | Report | Cat | Story | Key people / companies | Event date | Main URL |
entities = []
for line in INDEX.read_text(encoding="utf-8").splitlines():
    cols = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cols) < 6 or not re.match(r"^\d{4}-\d{2}-\d{2}", cols[0]) and not cols[0].startswith("REF"):
        continue
    for name in re.split(r"[,;/]| and ", cols[5]):
        name = re.sub(r"\(.*?\)", "", name).strip()
        if len(name) >= 4 and name.lower() not in GENERIC:
            entities.append((cols[0], name))

old_urls = {}
for p in ROOT.glob("*/reports/*.md"):
    if p.resolve() == new_path:
        continue
    for u in re.findall(r"\]\((https?://[^)]+)\)", p.read_text(encoding="utf-8")):
        old_urls.setdefault(u.rstrip("/"), p.relative_to(ROOT).as_posix())

warnings = 0
for card in cards:
    if not card.startswith("### "):
        continue
    head = card.splitlines()[0][4:60]
    if "UPDATE of" in card:
        continue
    for u in re.findall(r"\]\((https?://[^)]+)\)", card):
        if u.rstrip("/") in old_urls:
            warnings += 1
            print(f"URL REPEAT  [{head}] {u}  (used in {old_urls[u.rstrip('/')]})")
    low = card.lower()
    for sid, name in entities:
        if re.search(r"(?<![a-z])" + re.escape(name.lower()) + r"(?![a-z])", low):
            warnings += 1
            print(f"NAME MATCH  [{head}] '{name}'  (index {sid})")

print(f"cards={sum(c.startswith('### ') for c in cards)} warnings={warnings}")
