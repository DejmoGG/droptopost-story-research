# REPORT B — DropToPost stories (editorial brief, v5 · 2026-11-03)

**What we look for, in one sentence:**
> A real business got into an unbelievable situation, a post, video, reply, AI or automation decided what happened next, and the result was money, customers or ruin.

Shape of every story: **unbelievable event → content moment → business outcome.**
The viewer watches because they can't believe it happened. The business owner watching also thinks "content decides whether a business wins or dies, and I need it." That second thought is why DropToPost exists, and the story never has to say it out loud.

Run procedure, git and history format: root `CLAUDE.md`. **This brief overrides `CLAUDE.md` for Report B.**
Before choosing anything, read **`droptopost-research/TASTE.md`** (what the owner approved and rejected, and why). It outranks your own judgement. Its section **"What the approved stories share"** is the target shape: *someone did X in public to get Y, got the opposite, and then it got bigger.*

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
1. **Discover**: build a wide pool, **local news first** (see *Where the effort goes*), with the **narrative-pattern searches** below. Don't filter on "business lesson" yet: a fascinating event goes in the pool even if its business link isn't obvious; investigate the link before dropping it. And the reverse: an ordinary scandal doesn't get in just because a company is involved.
2. **Signals**: for each pool item, record the audience numbers you can actually read (see `sources/WATCHLIST.md` → *Audience numbers*). Unknown is "not measured". Signals help you find stories; they never replace judgment. A million views doesn't make a story.
3. **Investigate** the strongest 5–8: what happened before, what happened next, is there a turn after the turn? Chase the latest development (Mo's Chicken's October follow-up was the best part).
4. **Verify**: dates, numbers and consequences from 2+ independent sources; local-language originals where possible.
5. **Select**: only the six-point arc at 8.5+ becomes a pick. Then check the business link: business decisions, customer attention, reputation, content or commercial consequences. A random viral or an ordinary scandal that merely happened at a business doesn't qualify.
6. **Visual check**: find the original footage/post (see *Footage, not articles*) and propose the 2-second opener.

**Discovery pool:** every run appends what it looked at to `droptopost-research/discovery/YYYY-MM-DD.md`: one line per candidate with channel, source, original link, event date, signals and status (`pool` / `investigated` / `card B-n` / `dropped: reason`). The Desk only shows cards.

### Narrative-pattern searches (every run, at least 8 of the searches)
Search for the *shape*, not the topic. These are ways to **find** stories, never templates to force a story into.

| Pattern | English | Chinese | Japanese | Korean |
|---|---|---|---|---|
| Tried to fix it, made it worse | backfired, "made it worse", apology "sparked" | 弄巧成拙 · 适得其反 · 回应 翻车 | 逆効果 · 謝罪 炎上 | 역효과 · 해명 논란 |
| Begged customers not to, they came more | "asked customers to stop", "please don't come" | 求别来 · 劝退 · 别再来了 | 来ないで · 来店 自粛 お願い | 오지 마세요 · 손님 자제 |
| Set out to prove a critic wrong, proved them right | "to prove", "invited critics", "opened its kitchen" | 自证 · 开放后厨 · 打脸 | 証明 · 公開 裏目 | 증명 · 공개 역풍 |
| An accident, crime or complaint turned into something extraordinary | stolen + "turned into", mistake + "sold out" | 将错就错 · 失误 爆火 · 被偷 营销 | ミス 逆に 売れた · 盗難 話題 | 실수 대박 · 도난 화제 |
| Famous overnight, then the consequences | "overwhelmed", "went viral" + closed / staff / queue | 爆火之后 · 一夜爆红 后 · 网红店 关门 | バズった 閉店 · 行列 迷惑 | 대박 후 폐업 · 줄서기 민원 |
| A clever campaign got the opposite result | "campaign" + "opposite", Streisand | 营销 翻车 · 反向 | キャンペーン 裏目 | 마케팅 역풍 |
| A ridiculous decision that worked | "ridiculous", "joke" + "actually worked" | 离谱 · 奇葩 老板 · 反转 | まさかの · 珍対応 | 황당 · 반전 |
| A small event, a chain reaction | "domino", "sparked", "chain reaction" | 连锁反应 · 引发 | 連鎖 · 波紋 | 연쇄 · 파장 |

Combine the pattern with a business word (shop, restaurant, owner, founder, brand / 店主 老板 / 店長 / 사장님) and a date limit (this week).

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

## Range (owner, 3 Nov 2026)
Don't overfit to restaurants, China or one story formula. The approved examples show a taste for **extraordinary, escalating consequences**, not for a cuisine or a country. Each run:
- Search across industries (retail, hotels, airlines, transport, tech and apps, banks, sport clubs, beauty, fitness, real estate, factories, farms, creators, local services), not just food.
- Across what's shown (pick + candidates): **at most 2 from the same industry and at most 2 from the same country.** If the strongest stories cluster, say so and show the best of the rest only if it reaches 7.
- The proven outlets stay first, but read them for every kind of business, not only the restaurant stories.

## Where the effort goes (by results, not by assumption)
**Evidence so far (owner, 3 Nov 2026):** all three RUN stories were first found through **international local reporting** (Dexerto, Sixth Tone / SCMP / Global Times). Social platforms found none yet, but they gave the original footage and the engagement numbers. So, for each run of about 30 searches:
- **~60% Channel B**: first the outlets with an owner RUN in the Yield table, then outlets like them in China, Japan, Korea, Taiwan, Singapore, Australia and Europe (see `sources/WATCHLIST.md` → *Channel B*). At least a third of these in Chinese, Japanese or Korean.
- **~25% narrative-pattern searches** (table above), mixed across languages.
- **~15% Channel A discovery** (feeds + platform searches). Channel A is also used for **every shortlisted candidate** to find the original footage and real signals; those searches don't count against the 15%.
- **For the past-7-days window, read the outlets' own front or section pages** (`sources/WATCHLIST.md` → *Front pages*), not search: the search tool doesn't sort by date and returns 2024–25 stories for "this week" queries (round 6, 3 Nov: every fresh lead came from a front page). Use narrative-pattern searches mainly for the 30–90-day window and unknown classics.
- Re-read the Yield table at the start of each run. When a source produces an owner RUN, move effort toward it; when one produces nothing for 3–4 weeks, cut it. The goal is more stories the owner wants, not more sources or searches.

## How hard to search (every run)
- **About 30 searches**, split as above, and write the split in the header. The pool should hold 30+ candidates.
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

### Five separate scores (every investigated candidate, /10 each)
- **Entertainment:** would an ordinary person desperately want to know what happens next?
- **Narrative:** is there a genuinely unexpected escalation or reversal (beats 3–5 in TASTE.md)?
- **Business:** would entrepreneurs and business owners find it especially interesting?
- **Evidence:** can we verify it and show original footage or supporting visuals?
- **Freshness:** new, still developing, or genuinely unfamiliar to this audience?

The overall /10 is an editorial judgment, **not the average**. The owner's verdicts so far show Entertainment and Narrative decide it: a pick needs **both at 8+**, Evidence at 7+ (otherwise candidate), and Business at 6+ after investigating the link. Freshness breaks ties, never rescues a flat story. Write the five scores on the card and in the pool.

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
- **Scores:** Entertainment n · Narrative n · Business n · Evidence n · Freshness n
- **How it unfolds:** for picks and the strongest candidates, the progression in 3–5 steps (what happened, what they did, what the crowd did, what it became), not the business lesson
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
- `headline` is in normal sentence case (not caps); the other fields are the card's text, with no markdown. Start `note` with the five scores ("Entertainment 8 · Narrative 9 · Business 7 · Evidence 8 · Freshness 10.").
- If you improve a report the same day, rewrite the desk file too.

## Same-day rule
If today's report exists, improve it (replace weaker cards with stronger ones) rather than writing a second one. Shown stories stay in history.

## Learning loop
- Owner verdicts live in `history/history.md` (Status `approved` / `rejected`, with a reason) and on the Story Desk page (https://claude.ai/artifact/3ZMwN8TQ1wy24ur4NEykxM). They're copied into `TASTE.md`.
- Once there are 10 or more verdicts on **picks**, write the pick approval rate in the header. **Target: 80% of picks approved.** Candidates don't count. If it falls below that two weeks running, the rules are wrong. Flag it, don't just search harder.
- `performance/performance.md` holds real results from published videos. Once there are 5 or more rows, favour the story types that brought watch time, saves, site visits and leads.
