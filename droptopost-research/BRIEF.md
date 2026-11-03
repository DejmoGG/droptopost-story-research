# REPORT B — DropToPost stories (editorial brief, v4 · 2026-11-03)

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
1. **Last 7 days** · 2. **last 30 days** · 3. **last 90 days**. The owner's extra preference (3 Nov 2026): **events still unfolding in the past 7 days**, like the Zauo QR-code story.
4. Older **only** as an "Unknown classic": say in one line why this audience is unlikely to have seen it. Never more than 1 per run.

Labels: **Breaking** (≤48 h) · **Recent** (≤7 days) · **This month** (≤30 days) · **Last 90 days** · **Unknown classic**.

## Workflow (every run, in this order)
1. **Discover**: build a wide pool from **two channels** (below). Don't filter on "business lesson" yet: a fascinating event goes in the pool even if its business link isn't obvious.
2. **Signals**: for each pool item, record the audience numbers you can actually read (see `sources/WATCHLIST.md` → *Audience numbers*). Unknown is "not measured". Signals help you find stories; they never replace judgment. A million views doesn't make a story.
3. **Investigate** the strongest 5–8: what happened before, what happened next, is there a turn after the turn? Chase the latest development (Mo's Chicken's October follow-up was the best part).
4. **Verify**: dates, numbers and consequences from 2+ independent sources; local-language originals where possible.
5. **Select**: only the six-point arc at 8.5+ becomes a pick. Then check the business link: business decisions, customer attention, reputation, content or commercial consequences. A random viral or an ordinary scandal that merely happened at a business doesn't qualify.
6. **Visual check**: find the original footage/post (see *Footage, not articles*) and propose the 2-second opener.

**Discovery pool:** every run appends what it looked at to `droptopost-research/discovery/YYYY-MM-DD.md`: one line per candidate with channel, source, original link, event date, signals and status (`pool` / `investigated` / `card B-n` / `dropped: reason`). The Desk only shows cards.

### Channel A: original posts and videos
- Run `python3 shared/tools/feeds.py 7` (Reddit RSS + Google Trends RSS from the watchlist). If it can't reach the internet from the cloud, write "Channel A feeds: unreachable" in **Gaps**.
- Search the platforms with the search tool's domain filter: **x.com, tiktok.com, youtube.com, douyin.com, bilibili.com, weibo.com**. Search by event words, not "viral": QR code, livestream, streamer, prank, refund, sold out, queue, owner, stolen, glitch, AI, apology, boycott, bill, review. In Chinese: 老板 / 店主 / 爆火 / 反转 / 排队 / 直播. Japanese: 店主 / 炎上 / 行列. Korean: 사장님 / 논란 / 손님.
- Aggregator accounts surface events within hours (@InternetH0F, @Dexerto, @TMZ on X; 香港01 「01秒看新聞」 and TVBS on YouTube; Bilibili monthly roundups 「逆天月报」). Use them to find the event, then find the original.
- Reddit through the search tool is refused; use the RSS feeds only. Never work around a site that refuses scripts.

### Channel B: original local reporting
The outlets in `sources/WATCHLIST.md` → Channel B, by domain filter, plus local-language queries (Chinese, Japanese, Korean) on named outlets. Generic local-language queries return SEO blogs; name the outlet. Never use marketing blogs or "viral marketing case study" pages as a discovery source.

## Where to look
- **Local and national news, date-sorted:** "went viral" + small business / restaurant / bakery / shop / owner; "AI" + restaurant / store / small business / mistake / backlash; "Facebook post" / "TikTok" + owner; stolen / theft + brand response.
- **Reddit (signal, never proof):** r/smallbusiness, r/Entrepreneur, r/KitchenConfidential, r/mildlyinfuriating, r/antiwork, r/TalesFromRetail, r/AIfails and city subreddits.
- **Trade press:** Restaurant Business, Restaurant Dive, Marketing Dive, Modern Retail, The Drum, Adweek, Social Media Today, Retail Dive.
- **AI incident trackers:** OECD AI incidents, AI Incident Database, regulators (FTC, ICO, PDPC).
- **Google Trends US/UK.**
- **Never claim a trend, view count or Reddit engagement you didn't see in a source.** If the cloud sandbox can't open a page, say "not measured".

## How hard to search (every run)
- **At least 30 searches, at least 10 of them Channel A**, and write both counts in the header. The pool should hold 30+ candidates.
- **Yield:** at the end of the run add one row per source to the Yield table in `sources/WATCHLIST.md` (candidates found, cards, picks; the owner's RUN verdicts come in later). Each Monday, write a one-line summary of the past week's yield by source in the report header. After 3–4 weeks, cut sources that produced nothing. Generic queries ("viral small business story") return vendor blogs, so search **by outlet** and by headline wording: "owner", "went viral", "TikTok", "review", "scam", "AI", "sold out", "backlash", "Facebook post".
- Outlets that work from the cloud search tool: today.com, nbcnews.com, cbsnews.com (local stations), abcnews.go.com, foxbusiness.com, dailydot.com, dexerto.com, futurism.com, 404media.co, sfgate.com, inc.com, entrepreneur.com, modernretail.co, glossy.co, retaildive.com, restaurantbusinessonline.com, nrn.com, mothership.sg. BBC, Guardian, Business Insider, People, Eater, The Verge, NY Post and USA Today refuse domain-filtered search, so search those without a filter.
- Cover at least 3 countries (US local news, UK, Singapore/Australia).
- Search every candidate's people and company names in the index and in TASTE.md before writing a card.

## The story arc (benchmark: the KitKat theft, 2026-11-03-B1-1)
The best stories get **more unbelievable as they unfold**. Check six things:
1. **An extremely unusual real event.**
2. **Stakes anyone understands instantly.**
3. **Conflict, absurdity, mystery or suspense.**
4. **An unexpected second development** (the turn after the turn).
5. **A remarkable payoff.**
6. **A natural link to business, content or customer attention.**

No second development or no payoff: **7 at most**, however viral it was.

## Rating /10 (honest, calibrated to the owner's verdicts in TASTE.md)
- **5** · real news on a familiar formula (bad review → locals rally → more customers).
- **6–7** · reasonably interesting: one funny or clever idea, no escalation or no payoff.
- **8** · excellent: real conflict, escalation and consequences.
- **9** · a genuinely extraordinary event **and** payoff. KitKat level.
- **10** · exceptionally rare. Expect to give none in most months.

Never rate from views, sales or "went viral". Don't confuse:
- a real news story with an extraordinary story;
- a viral video with a great narrative;
- impressive sales with entertaining content;
- a business lesson with an unexpected twist.

Calibration (owner, 3 Nov 2026): The Local Scoop 8.5 · Art of Play 8 · Lahaina Tacos 7.5 · Kok Sen 6.5 · Oddly Correct 5. Claude had scored them 77–90/100: that is the inflation to avoid.
Round 4 (owner): Zauo QR-code orders 9.5 · Mo's Chicken Hot Pot 9 · Xibei open kitchens 9 · Starbucks Korea "Tank Day" 7.5 · Korean no-show scams 7 · banquet invoice fraud 6.5. **This is the target type**: one business, one absurd event, a reversal, real consequences, source footage.

Caps that apply whatever else the story has:
- **Needs a history or culture lesson before the hook works** → 7.5 at most (LATER, longer explainer).
- **A crime wave or trend summary with no single protagonist** → 7 at most. Find one person who lived it, verified.
- **Ordinary employee or invoice fraud** → not DropToPost; hand it to Report A (A1).

## What a run delivers
- **The goal is ONE exceptional, production-ready story**: 8.5 or more, all six arc points, facts checked. One a week beats five a day.
- If nothing reaches 8.5, the header says **"No pick today"**. That is a normal, good result. The best story of a weak day is still a weak story.
- Below the pick, **up to 4 candidates** rated 7 or more, labelled **Candidate, not a pick**, so the owner can rate them on the Desk. Never pad, never call a candidate a masterpiece.
- Rejected stories never come back unless a major new development materially changes them (`UPDATE of <ID>`).

## Facts in the card
- Business results are proof, not points: labelled **Verified / Self-reported / Reported via <who> / Uncertain**, or "unknown".
- Views are not customers, sales are not profit, and going viral alongside growth doesn't prove the video caused it: say so.
- **Allegations stay allegations.** Charges aren't convictions. A claim from one side is written as "X says". A joke or stunt (a "$15 million" price) is called a joke.
- For a pick, check the key twist independently (e.g. the supplier's own statement). If you can't, say who it comes from.
- **Footage, not articles** (owner, 3 Nov 2026): "An article describing a fantastic video isn't the same as having the footage." Every pick lists **direct links to the original footage**: the original post, stream clip/VOD, the business's own statement, its account, news video. Write "original not found" when you can't find it, and name what you searched. A pick with no findable footage drops to candidate.
- **2-second opener:** every pick proposes the strongest opening visual (what is on screen in the first 2 seconds, and which clip it comes from).

## Card (readable in 20 seconds)
```
### 2026-11-04-B-1 · Pick 8.7/10 · This month · Evidence High      (or: · Candidate 7/10 ·)
**OPENING LINE THAT WORKS WITH NO CONTEXT**
- **What happened:** 3–4 short sentences, ending with the outcome
- **The turn:** the unexpected second development
- **Payoff:** how it ended
- **Why anyone would watch:** one line (the human hook, no business words)
- **Why a business owner cares:** one line, never a lecture
- **Result:** labelled, or "unknown"
- **Audience signals:** numbers you actually read, with source and date (e.g. "TMZ post on X: 48,675 likes, 1,033 replies, read 3 Nov"), or "not measured"
- **Arc check:** which of the six points it hits, and what's missing
- **Dates:** event · latest development
- **Proof:** [outlet](url) · [outlet](url) (2+ independent where possible)
- **Footage:** [original post / clip / statement](url) · … (picks: required, or "original not found: searched X, Y")
- **2-second opener:** what's on screen, from which clip (picks only)
```

## Report file
`droptopost-research/reports/YYYY-MM-DD.md`: header (date · searches run · candidates looked at · **Pick of the day: <title> (rating)** or **No pick today** · cost €0 · gaps) · the cards in rank order · `## Rejected today` (one line each: story, which test it failed).
History/index ID = `YYYY-MM-DD-B-<n>`.

**Also write `droptopost-research/reports/YYYY-MM-DD.desk.json`** (same stories, for the Story Desk; a local task copies it there every morning). Copy the shape of `reports/2026-11-03.desk.json`: `{"round": "<D Mon YYYY>", "stories": [{"id", "sort", "tier" ("pick" or "candidate"), "score" (the /10 rating), "freshness", "evidence", "headline", "what", "twist" (the turn and payoff), "why", "result", "dates", "proof": [{"label","url"}], "note"}]}`.
- `sort` = YYYYMMDD × 100 + (99 − rank), so rank 1 on 4 Nov 2026 is `2026110498`.
- `headline` is in normal sentence case (not caps); the other fields are the card's text, with no markdown.
- If you improve a report the same day, rewrite the desk file too.

## Same-day rule
If today's report exists, improve it (replace weaker cards with stronger ones) rather than writing a second one. Shown stories stay in history.

## Learning loop
- Owner verdicts live in `history/history.md` (Status `approved` / `rejected`, with a reason) and on the Story Desk page (https://claude.ai/artifact/3ZMwN8TQ1wy24ur4NEykxM). They're copied into `TASTE.md`.
- Once there are 10 or more verdicts on **picks**, write the pick approval rate in the header. **Target: 80% of picks approved.** Candidates don't count. If it falls below that two weeks running, the rules are wrong. Flag it, don't just search harder.
- `performance/performance.md` holds real results from published videos. Once there are 5 or more rows, favour the story types that brought watch time, saves, site visits and leads.
