# DropToPost Story Research

Two research reports every morning at **07:00 Ljubljana time**, written by a Claude cloud routine on the Claude subscription. No paid AI APIs.

## Story Desk (phone)
Rate every new DropToPost story on your phone, no GitHub needed: **https://claude.ai/artifact/3ZMwN8TQ1wy24ur4NEykxM** (Run it / Spike it / Later + a reason).
New stories appear there around 07:40 each morning: a scheduled task in the Claude app on the PC copies `reports/YYYY-MM-DD.desk.json` onto the Desk. If the PC is off, it catches up when the app next opens.

## Latest
- **Report A — Business & investment:** [2026-11-11](business-research/reports/2026-11-11.md) (6 stories)
- **Report B — DropToPost audience:** [2026-11-11](droptopost-research/reports/2026-11-11.md) (no pick; 2 candidates)

## All reports
- [Report A archive](business-research/reports/)
- [Report B archive](droptopost-research/reports/)

## Approve / reject
Open the history file and change a story's **Status** from `new` to `approved`, `rejected` or `later`. On GitHub: pencil icon → edit → commit.
- [Report A history](business-research/history/history.md)
- [Report B history](droptopost-research/history/history.md)

## How it works
- `CLAUDE.md`: the daily run procedure the cloud routine follows.
- `business-research/BRIEF.md`, `droptopost-research/BRIEF.md`: what each report looks for.
- `shared/global-story-index/index.md`: every story ever shown, used so no story repeats across either report.
- `shared/tools/`: Ljubljana time check (summer time), link checker, duplicate checker.

## Historical research
A separate backlog of true business stories from 1900–2025, built in batches beside the daily reports: [historical-research/](historical-research/README.md) · latest: [batch 1, 2026-11-04](historical-research/batches/2026-11-04-batch-1.md). Its stories sit on the Story Desk under **Historical**.
