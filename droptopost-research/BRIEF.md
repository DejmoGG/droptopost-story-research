# REPORT B — DropToPost stories (editorial brief, v3 · 2026-11-03)

**What we look for, in one sentence:**
> A real business got into an unbelievable situation, a post, video, reply, AI or automation decided what happened next, and the result was money, customers or ruin.

Shape of every story: **unbelievable event → content moment → business outcome.**
The viewer watches because they can't believe it happened. The business owner watching also thinks "content decides whether a business wins or dies, and I need it." That second thought is why DropToPost exists, and the story never has to say it out loud.

Run procedure, git and history format: root `CLAUDE.md`. **This brief overrides `CLAUDE.md` for Report B.**
Before choosing anything, read **`droptopost-research/TASTE.md`** (what the owner approved and rejected, and why). It outranks your own judgement.

## The three tests (pass/fail: fail one and the story is out, no score)
1. **The "what the fuck" test.** Would someone with zero interest in business be desperate to know what happened next? Write the opening line first. It must work **without** the words marketing, brand, campaign or strategy. If it needs context to land, it fails.
2. **The owner test.** Would a business owner, agency or creator see themselves in it? The main character is a business with real stakes (rent, sales, staff, reputation). Small and mid-size businesses come first. A giant brand counts only if the same thing could happen to anyone.
3. **The content test.** Did a post, video, reply, AI or automation cause the turn, for better or worse? And could a small business copy it, or avoid it, without a big budget? Stunts paid for with millions fail.

## Automatic rejects
- **Famous marketing case studies**, anything a marketer has seen in a "best campaigns" list (Dollar Shave Club, Blendtec, Ocean Spray, Popeyes, KFC "FCK", Grimace, Old Spice and the like).
- **Stories whose only interest is their results**: impressive numbers, nothing unbelievable happening.
- **Feel-good brand stunts and predictable success stories.**
- **Pure accidents with no business response.**
- **Stories where the business is a bystander** (a prank filmed in a shop, a celebrity mention).
- **Anything already in `shared/global-story-index/index.md`**, unless there's a major new development (`UPDATE of <ID>`).
- **Anything on TASTE.md's "Already known to the owner" list**, and any story the owner or ChatGPT pasted in. Stories the owner hands you show the type; they're never material.
- **A story every outlet led with for days**, unless it's the strongest of the run. If you include one, the card's Note says "you may have seen this".

## Freshness (search in this order, every run)
1. **Last 7 days** · 2. **last 30 days** · 3. **last 90 days**.
4. Older **only** as an "Unknown classic": say in one line why this audience is unlikely to have seen it. Never more than 1 per run.

Labels: **Breaking** (≤48 h) · **Recent** (≤7 days) · **This month** (≤30 days) · **Last 90 days** · **Unknown classic**.

## Where to look
- **Local and national news, date-sorted:** "went viral" + small business / restaurant / bakery / shop / owner; "AI" + restaurant / store / small business / mistake / backlash; "Facebook post" / "TikTok" + owner; stolen / theft + brand response.
- **Reddit (signal, never proof):** r/smallbusiness, r/Entrepreneur, r/KitchenConfidential, r/mildlyinfuriating, r/antiwork, r/TalesFromRetail, r/AIfails and city subreddits.
- **Trade press:** Restaurant Business, Restaurant Dive, Marketing Dive, Modern Retail, The Drum, Adweek, Social Media Today, Retail Dive.
- **AI incident trackers:** OECD AI incidents, AI Incident Database, regulators (FTC, ICO, PDPC).
- **Google Trends US/UK.**
- **Never claim a trend, view count or Reddit engagement you didn't see in a source.** If the cloud sandbox can't open a page, say "not measured".

## How hard to search (every run)
- **At least 30 searches**, and write the count in the header. Generic queries ("viral small business story") return vendor blogs, so search **by outlet** and by headline wording: "owner", "went viral", "TikTok", "review", "scam", "AI", "sold out", "backlash", "Facebook post".
- Outlets that work from the cloud search tool: today.com, nbcnews.com, cbsnews.com (local stations), abcnews.go.com, foxbusiness.com, dailydot.com, dexerto.com, futurism.com, 404media.co, sfgate.com, inc.com, entrepreneur.com, modernretail.co, glossy.co, retaildive.com, restaurantbusinessonline.com, nrn.com, mothership.sg. BBC, Guardian, Business Insider, People, Eater, The Verge, NY Post and USA Today refuse domain-filtered search, so search those without a filter.
- Cover at least 3 countries (US local news, UK, Singapore/Australia).
- Search every candidate's people and company names in the index and in TASTE.md before writing a card.

## How many
**Maximum 5 stories per run. Zero is allowed.** Two the owner will use beat 27 nobody uses. Never pad. If fewer than 3 pass, say so plainly in the header and say what was rejected.

## Ranking (only stories that passed all three tests)
**Story score /100:** "what the fuck" factor 40 · owner identification 25 · content caused the outcome 20 · freshness 15.
Business results earn **no points**. They're required proof, labelled **Verified / Self-reported / Uncertain**, or "unknown".
Views are not customers, sales are not profit, and going viral alongside growth doesn't prove the video caused it: say so.

## Card (readable in 20 seconds)
```
### B-2026-11-03-1 · Story 94 · This month · Evidence High
**OPENING LINE THAT WORKS WITH NO CONTEXT**
- **What happened:** 3–4 short sentences, ending with the outcome
- **The twist:** one line
- **Why a business owner cares:** one line, never a lecture
- **Result:** labelled Verified / Self-reported / Uncertain, or "unknown"
- **Dates:** event · latest development
- **Proof:** [outlet](url) · [outlet](url) (2+ independent where possible; original post if found)
```

## Report file
`droptopost-research/reports/YYYY-MM-DD.md`: header (date · candidates looked at · how many passed · cost €0 · gaps) · the cards in rank order · `## Rejected today` (one line each: story, which test it failed).
History/index ID = `YYYY-MM-DD-B-<n>`.

**Also write `droptopost-research/reports/YYYY-MM-DD.desk.json`** (same stories, for the Story Desk; a local task copies it there every morning). Copy the shape of `reports/2026-11-03.desk.json`: `{"round": "<D Mon YYYY>", "stories": [{"id", "sort", "score", "freshness", "evidence", "headline", "what", "twist", "why", "result", "dates", "proof": [{"label","url"}], "note"}]}`.
- `sort` = YYYYMMDD × 100 + (99 − rank), so rank 1 on 4 Nov 2026 is `2026110498`.
- `headline` is in normal sentence case (not caps); the other fields are the card's text, with no markdown.
- If you improve a report the same day, rewrite the desk file too.

## Same-day rule
If today's report exists, improve it (replace weaker cards with stronger ones) rather than writing a second one. Shown stories stay in history.

## Learning loop
- Owner verdicts live in `history/history.md` (Status `approved` / `rejected`, with a reason) and on the Story Desk page (https://claude.ai/artifact/3ZMwN8TQ1wy24ur4NEykxM). They're copied into `TASTE.md`.
- Once there are 10 or more verdicts, write the approval rate in the header. **Target: 80% approved.** If it falls below that two weeks running, the rules are wrong. Flag it, don't just search harder.
- `performance/performance.md` holds real results from published videos. Once there are 5 or more rows, favour the story types that brought watch time, saves, site visits and leads.
