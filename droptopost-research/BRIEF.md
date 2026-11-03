# REPORT B — DropToPost viral story research (editorial master brief)

**Central theme:** "The unbelievable stories behind how businesses attract attention, win customers, and grow."
**The owner's highest commercial priority.** Story QUALITY beats quantity.

We are **not** a marketing news channel, **not** an AI-software review channel and **not** a business-advice channel. We tell extraordinary true stories that a normal person would watch even if they don't care about marketing, and that naturally attract **business owners, entrepreneurs, marketing and content agencies, founders and SaaS operators, and professional creators**: the people who might buy DropToPost (automated content production). The viewer should finish thinking **"I can't believe that actually happened"**, and the business owner should also think **"I need better content for my business."**

Run procedure, shared fact rules and history format: root `CLAUDE.md`. **This brief overrides `CLAUDE.md` on scoring and card format for Report B.**

## Categories (up to 10 each, ranked)
(The owner's wording calls these Category A/B/C. In this repo they are B1/B2/B3, because Report A already uses A1–A3.)

**B1. Viral marketing miracles & disasters.** One viral video saved a whole business · brilliant stunts with extraordinary results · ridiculous marketing mistakes · complaints turned into viral campaigns · ordinary people accidentally generating millions of views for a business · products becoming worldwide sensations overnight · controversies turned into publicity · extraordinary results from simple content.

**B2. AI, automation & the future of content.** AI avatars that became unexpectedly successful or controversial · businesses making content without filming · AI ads outperforming expensive campaigns · small companies replacing production teams with automation · entrepreneurs building media businesses with AI · AI influencers · AI content causing extraordinary public reactions · huge cost cuts with quality kept.
**Not:** model releases, benchmarks, features or technical announcements. We want surprising HUMAN stories about what happened when people used AI.

**B3. Small businesses winning through content.** Restaurants saved by TikTok · ordinary businesses suddenly getting thousands of customers · small brands beating giants with storytelling · founders growing through educational entertainment · boring products turned viral · audiences built before the product · unusual social strategies with real sales · personality, humour, controversy or curiosity driving growth. **Prefer real commercial outcomes over views.**

## Gold standard (calibration examples: `REF-*` in the index, never present them as new)
1. A brewery created a fake AI woman. Customers hated her, then her videos exploded.
2. A 19-year-old was about to lose his restaurant, then he posted one TikTok.
3. An AI app got four million views before anyone could download it.
4. A woman filmed her burned-out car, and her Stanley cup still had ice in it.
5. A woman sold one chocolate bar a week, then TikTok turned it into a worldwide craze (Dubai chocolate).
6. A random woman made a silly Dr Pepper song, and the company turned it into a national ad.
7. Dove turned brutally honest Reddit reviews into a massive campaign.
8. A luggage designer explained a suitcase on a whiteboard, and millions watched.
9. IKEA reacted to a viral baby monkey, and suddenly everyone wanted its stuffed toy.
10. Levi's spent hours filming seconds of handmade animation while competitors rushed toward AI.
They set the **storytelling standard**, not verified performance claims. Find NEW stories at least this strong.

## Research (every run)
- **Sources:** Reddit (`site:reddit.com`, a signal and never proof), Google Trends US/UK, original TikTok/YouTube/Instagram posts, Marketing Dive, Adweek, The Drum, Social Media Today, CNBC, Business Insider, Starter Story, Indie Hackers, founder interviews, agency case studies (claims only), brand announcements, independent reporting and documented sales results.
- **Four time windows, all searched:** breaking (48 h) · recent (7 days) · rediscovered (90 days) · evergreen (extraordinary historical stories not shown before). Never only today's news.
- **Breadth:** examine **60–100 distinct candidates** when sources allow, and write the real number in the header.
- Check every candidate against `shared/global-story-index/index.md` (both reports) before deep-checking it.
- Read `performance/performance.md`. When real results exist, favour the story types that brought the **right** viewers (watch time, saves, qualified visits, leads), not just views.

## Ruthless selection
**Reject immediately:** generic advice · routine AI announcements · boring statistics · unverified agency success claims · ordinary launches · no human emotion · no surprising development · needs too much explaining · no clear business relevance · already shown without a meaningful update.
**Every surviving story has:** (1) a shocking, instantly understandable opening · (2) a real person, brand or business · (3) a clear situation or problem · (4) an unexpected action or development · (5) emotional stakes, controversy, humour or suspense · (6) a meaningful outcome · (7) strong visual-storytelling potential.
**Test:** "Would a normal person who doesn't care about marketing still watch this entire story?" If not, reject it.

## Scoring (editorial judgement, not a prediction)
**Story score /100:** curiosity and hook 25 · emotion, suspense, surprise or controversy 20 · structure and payoff 15 · relevance to DropToPost buyers 15 · demonstrated audience interest 10 · original visual evidence 10 · freshness or rediscovery 5.
**Evidence** separately: High / Medium / Low, plus **Verified / Self-reported / Uncertain** for the business results.
Views are not customers. Sales are not profit. One video going viral alongside growth does not prove the video caused it: say so. An agency's claim is not an independent result.
**Freshness category:** Breaking · Recent · Rediscovered · Evergreen.

## Card (concise, readable in under 30 seconds)
```
### B1-1 · Story 92 · Evidence High · Recent
**TITLE (immediate curiosity)**
- **Hook:** the opening sentence of a 60–180 s video
- **What happened:** 3–5 short sentences, including the outcome
- **Biggest twist:**
- **Why people will watch:** the emotional trigger or curiosity gap
- **Why our buyers care:** what it shows about content, marketing, acquisition or growth (one line)
- **Real business results:** labelled Verified / Self-reported / Uncertain, or "unknown"
- **Audience evidence:** real views, Reddit engagement, Trends signals with source, or "not available"
- **Original visuals:** direct links to the original post, video, ad or interview, or "none found"
- **Dates:** original event · latest development
- **Sources:** [outlet](url) · [outlet](url)
```

## TOP 5 (first section of the report)
Stories that can become exceptional videos **today**: real footage or strong visual evidence, powerful emotion, an easy narrative, an unexpected ending, and a clear link to entrepreneurs. **Mix the story types** (not five of the same kind unless the quality gap is overwhelming). One line each on **why produce it today**.

## Same-day rule
If today's Report B already exists, **audit and improve it** (replace weak picks, add stronger finds, fix the TOP 5) instead of writing a second report. Stories already shown stay in history, even if demoted.

## Report file
`droptopost-research/reports/YYYY-MM-DD.md`: header (see `CLAUDE.md`) · `## TOP 5 STORIES TO PRODUCE TODAY` · `## B1. VIRAL MARKETING MIRACLES & DISASTERS` · `## B2. AI, AUTOMATION & THE FUTURE OF CONTENT` · `## B3. SMALL BUSINESSES WINNING THROUGH CONTENT` · optional `## Dropped`.
Card IDs: `B1-1 …`, `B2-1 …`, `B3-1 …`. History/index ID = `YYYY-MM-DD-B1-1`.
