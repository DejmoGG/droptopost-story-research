# DropToPost story research: daily run procedure

This repo holds two independent daily research reports. Both are produced by Claude (Claude Code subscription, cloud routine). **No paid AI APIs.**

| Report | Brief | Reports | History |
|---|---|---|---|
| **A — Business & investment stories** | `business-research/BRIEF.md` | `business-research/reports/YYYY-MM-DD.md` | `business-research/history/history.md` |
| **B — DropToPost audience stories** | `droptopost-research/BRIEF.md` | `droptopost-research/reports/YYYY-MM-DD.md` | `droptopost-research/history/history.md` |

Shared duplicate index (both reports): `shared/global-story-index/index.md`.
Rules that apply to both reports: the **Shared rules** section below. Format reference: the existing reports.

---

## Daily run (follow exactly)

The routine prompt says `MODE=scheduled` or `MODE=test`.

### 0. Time guard (MODE=scheduled only)
The routine fires at 05:00 and 06:00 UTC. Run `python3 shared/tools/ljubljana_time.py`. It prints `HOUR=<local hour>` and `DATE=<local date>` with EU summer time built in, so it doesn't need tzdata.
- `HOUR=07`: continue.
- `HOUR=08`: continue **only if** a report for `DATE` is still missing (catch-up if the 07:00 run failed).
- Anything else: reply "Not 07:00 in Ljubljana. Nothing to do." and stop.

`MODE=test` skips the time guard. Use the `DATE` it prints and name files `DATE-test.md` (not `DATE.md`). If the prompt gives a `LIMIT`, research only that many stories per category. Test stories are real and are added to history and the index like any other.

### 1. Sync with the canonical state
```
git fetch origin
git checkout main && git reset --hard origin/main
git merge --ff-only origin/claude/daily-state 2>/dev/null || true   # only exists if an earlier run couldn't push to main
```
`main` is canonical. Never work from a stale checkout.

### 2. Read the history (both reports, always)
Read `shared/global-story-index/index.md` in full, plus both `history/history.md` files. Every story ever shown, in either report, is listed there. The same underlying story must never appear again (different headline, URL or outlet counts as the same story). It may return **only** when something significant happened after its last appearance (new charge, verdict, sentence, funding, collapse, campaign). Then mark the card `UPDATE of <ID>` and lead with the new development.

### 3. Report A, then Report B (sequentially, never in parallel)
For each report whose file for `DATE` doesn't exist yet:
1. Read its `BRIEF.md`.
2. Research it (see **Shared rules**). Keep a candidate list. Before deep-checking a candidate, check its people and companies against the index.
3. Write the report file.
4. `python3 shared/tools/dupe_check.py <report file>`. Read every warning. Drop or replace true repeats (a shared generic word like "TikTok" is not a repeat).
5. `bash shared/tools/check_links.sh <report file>`. Replace any 404/410/000 link. A 403 from bot-blocking sites is acceptable if the URL came from a search result. If curl itself can't reach the internet, write that in the report's **Gaps** line. Don't pretend links were checked.
6. Append one row per story to that report's `history/history.md` **and** to `shared/global-story-index/index.md`.
7. **Commit and push this report before starting the next one** (step 4), so a later failure can't lose it.

If a source or tool fails, carry on with the others and list what failed in the report's **Gaps** line.

### 4. Commit and push to main
```
git add -A
git commit -m "Report <A|B> <DATE>"
git pull --rebase origin main && git push origin HEAD:main
```
If pushing to `main` is refused: `git push origin HEAD:claude/daily-state --force-with-lease` and write "PUSHED TO claude/daily-state, NOT main" at the top of the final message. The next run merges it in step 1.

### 5. Update the phone index and finish
Update `README.md` so the **Latest** section links to today's two reports. Commit and push. Final message: links to both reports on GitHub, the number of stories per category, gaps, and confirmation that no paid API was used.

---

## Shared rules (both reports)

**Time windows, all searched every day:** (1) breaking, past 24–48 h · (2) past 7 days · (3) past 90 days · (4) exceptional historical stories worth rediscovering. Fresh or newly trending stories come first, but never at the cost of quality. Every card shows the **event date** and the **latest development date**. A publication date is not an event date.

**Sources:** web search across Google Trends (US, UK, SI, via search and the "trending now" pages), Reddit threads (`site:reddit.com …`; Reddit is a signal, never proof), Reuters, AP, BBC, CNBC, Bloomberg, Fortune, Business Insider, Marketing Dive, Adweek, The Drum, Social Media Today, TechCrunch, Starter Story, Indie Hackers, founder interviews, regulator and court releases (SEC, US DOJ, FTC, UK SFO/FCA, Europol), original TikTok/YouTube/Instagram posts where accessible, international business press, AJPES and Slovenian outlets for Slovenia checks. Respect paywalls and access limits.

**Ruthless selection:** up to 10 per category, ranked strongest first. **Never fill a quota with a weak story.** Report the real count and why it's short. Reject: generic advice, routine announcements, industry news, unverified money claims, stories that need too much explaining, weak "case studies" pretending to be viral wins, and topics already covered.

**Scoring (editorial judgment, not a prediction):** viral score /100 = hook and curiosity 25 · emotion/surprise/controversy 20 · narrative and unexpected outcome 15 · verified audience interest 15 · audience relevance and commercial value 15 · visual potential 10. Target ≥ 75. **Evidence confidence** is separate: High / Medium / Low. A high viral score never overrides weak evidence.

**Facts (mandatory):** never invent stories, numbers, views, Reddit engagement or search volume. Unknown means writing "unknown". Label every figure: revenue / profit / loss / valuation / raised / customers / company claim / seller claim / estimate. Evidence labels: **Verified** (official record or 2+ independent outlets) · **Partially verified** · **Alleged** (charges or lawsuits: "prosecutors say", never "fraudster"). Keep direct URLs. Leave out anything you can't verify.

**Card format (phone-friendly, concise):**
```
### A1-1 · Viral 92 · Evidence High · Verified
**COMPELLING CAPS HEADLINE**
- **Hook:** one sentence
- **What happened:** 3–5 plain sentences
- **Biggest twist:**
- **Why it could go viral:**
- **Why our audience cares:**
- **Financial results:** labelled figures, or "unknown"
- **Audience signals:** real metrics with source, or "not measured"
- **Original visuals:** direct links to the original video/ad/post/interview, or "none found"
- **Dates:** event · latest development
- **Sources:** [outlet](url) · [outlet](url)
```
**A3 (extraordinary business models worldwide)** uses its own card and Model score. See `business-research/BRIEF.md` → A3.
**Report B** has its own rules: three pass/fail tests, freshest first, at most 5 stories, its own card and Story score. Read `droptopost-research/BRIEF.md` and `droptopost-research/TASTE.md` (the owner's verdicts) before researching.

**Report header:** date · candidates reviewed · stories included per category · cost: €0 (subscription; no paid API) · gaps (failed or skipped sources) · **TOP 5** of that report.

**History row format** (both `history.md` and the index): `| ID | First shown | Report | Cat | Story | Key people / companies (specific names) | Event date | Main URL |`. History files also have a `Status` column the owner edits (`new` → `approved` / `rejected` / `later` → `produced`). Never delete rows.
