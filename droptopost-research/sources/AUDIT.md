# Source-access audit

Re-run with `bash shared/tools/source_probe.sh`. The daily routine copies its result into the report's Gaps line, so this audit refreshes itself.

## 2026-11-03 (tested live from the owner's PC; the cloud routine's first probe runs at the next 07:00 run)

| Source | Used before today? | Access | Content seen | Engagement available | Real example retrieved |
|---|---|---|---|---|---|
| **Reddit** | No. Earlier reports said "not measured" | Search tool: **refused** (reddit.com blocked; `site:reddit.com` returns nothing). JSON API: **403** (refused to scripts, not worked around). Public RSS: **works, but rate-limited** (3 of 18 feeds got through in a burst) | Titles, links, post dates | **No** votes or comment counts | r/nottheonion top of week: "Chinese glassmaker finds unlikely publicity as French protesters fail to smash window" (31 Oct) |
| **Google Trends** | No | Daily trending RSS per country: **works** | Trending terms with approximate search volume | Approximate searches only | US, 3 Nov: "tornado warning", 200,000+ searches. Explore/API pages: 404, not used |
| **YouTube / Shorts** | Barely (no views read) | Search tool: works. Watch pages: **work** | Title, channel, upload date, view count, description. **Not the video itself** (Claude can't watch video) | Views yes; comments not read | HK01 clip on Mo's Chicken: 248,326 views, uploaded 5 Apr 2026 |
| **TikTok** | No | Search tool: works but returns mostly "discover" pages. oEmbed: works. Creative Center: **redirect, not usable without login** | Title and author | **No** views or likes | TikTok discover pages for "client refuse to pay" etc. (no counts) |
| **Instagram Reels/posts** | Yes (Lahaina Tacos, 3 Nov) | Embed pages through the built-in browser: work | Caption and like count shown on the embed | Likes yes, views no | @lahainatacos "Loveys, today I review Lahaina Tacos": 408,947 likes |
| **X / Twitter** | Partly (search results only) | Search tool: works. Public embed data (`cdn.syndication.twimg.com`): **works** | Post text, date, media type | **Likes and reply counts yes**; views no | TMZ's Lacy clip: 48,675 likes, 1,033 replies, posted 28 Oct 2026 |
| **Douyin / Bilibili / Weibo** | No | Search tool: works | Titles, dates; Bilibili page metadata via fetch | Bilibili views yes; Douyin likes only via news reports | Bilibili October roundup: 645K views; Liu Yuxin's Mo's video 1.32M likes (via HK01) |
| **International local news** | Yes, the main source so far | Search tool with domain filter; some domains refused (see WATCHLIST) | Full articles where not paywalled | Rarely | Jimu News (极目新闻), 2 Oct 2026: Mo's Chicken staff fell from ~180 to 30-odd |

**Honest limits:** Claude reads text, metadata and images, never video or audio. "What the clip shows" always comes from the post text, the outlet's description or a thumbnail, so the owner watches before scripting. Reddit vote counts and TikTok view counts are not available without logging in or using a paid API; neither is used.
