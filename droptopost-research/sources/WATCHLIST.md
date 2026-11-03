# Source watchlist (Report B)

Only sources that were **actually tested** are listed. Status is what worked on the date shown. Nothing here needs a login, a paid API or a new service.
Update the **Yield** table every run (see the bottom). After 3–4 weeks, cut sources that produce nothing and spend the searches on the ones that produce picks.

## Channel A: original posts and videos

### Feeds scanned by `python3 shared/tools/feeds.py 7` (tested 2026-11-03 from the owner's PC)
Reddit RSS gives titles, links and dates, **not** vote or comment counts (Reddit refuses its JSON to scripts; don't work around it). **Reddit rate-limits hard**: in the 3 Nov test, 15 of 18 subreddit feeds returned 429. So the scanner reads only the 6 best subreddits, 45 seconds apart (~5 minutes). Swap one in and out each week from the rotation list.
- feed: https://www.reddit.com/r/nottheonion/top/.rss?t=week | r/nottheonion (absurd real news; 3 Nov: robot hit-and-run, riot-proof glass, Cheesecake Factory, Chili's)
- feed: https://www.reddit.com/r/LivestreamFail/top/.rss?t=week | r/LivestreamFail (streamers vs businesses; had Lacy/Zauo in its top 5)
- feed: https://www.reddit.com/r/OutOfTheLoop/top/.rss?t=week | r/OutOfTheLoop (explains what's blowing up)
- feed: https://www.reddit.com/r/TikTokCringe/top/.rss?t=week | r/TikTokCringe (original viral TikToks)
- feed: https://www.reddit.com/r/smallbusiness/top/.rss?t=week | r/smallbusiness
- feed: https://www.reddit.com/r/singapore/top/.rss?t=week | r/singapore (local news links; 3 Nov: coconut-shake shop)
- feed: https://trends.google.com/trending/rss?geo=US | Google Trends US
- feed: https://trends.google.com/trending/rss?geo=GB | Google Trends UK
- feed: https://trends.google.com/trending/rss?geo=SG | Google Trends Singapore
- feed: https://trends.google.com/trending/rss?geo=JP | Google Trends Japan
- feed: https://trends.google.com/trending/rss?geo=KR | Google Trends Korea

Rotation (not scanned by default): r/PublicFreakout · r/KitchenConfidential · r/TalesFromRetail · r/MaliciousCompliance · r/assholedesign · r/Entrepreneur (3 Nov: only advice threads, no events) · r/japan · r/korea · r/China · r/unitedkingdom · r/australia.
Google Trends daily feeds are mostly sport and politics (3 Nov: nothing usable for B). Use them to **confirm** interest in a candidate, not to discover.

### Searched with the WebSearch tool (works in the cloud)
- **x.com**: returns original posts (aggregator accounts like @InternetH0F, @Dexerto, @TMZ, @ChipGotIt_ surface clips within hours). Domain filter works.
- **tiktok.com**: returns videos and "discover" pages; no view counts in results.
- **youtube.com**: returns videos and Shorts; news-clip channels (香港01, Global Times) carry Asian footage.
- **douyin.com**: returns Chinese originals (found Liu Yuxin's Mo's Chicken video page).
- **reddit.com: REFUSED by WebSearch** (domain not accessible; `site:reddit.com` returns nothing). Use the RSS feeds above instead.
- **instagram.com**: rarely returned by search. Open known posts through the embed page (`/p/<id>/embed/captioned/`) in the built-in browser.

### Audience numbers we can actually read (from the owner's PC)
| Source | What we get | How |
|---|---|---|
| X | likes, reply count, date, media type | `cdn.syndication.twimg.com/tweet-result?id=<id>&token=4` (public embed data) |
| YouTube | views, upload date, channel | the public watch page (`"viewCount"`) |
| Instagram | likes (as shown on the embed) | embed page in the built-in browser |
| TikTok | author and title only, **no views** | `tiktok.com/oembed?url=` |
| Reddit | titles, links, dates, **no votes** | RSS |
| Google Trends | trending terms + approximate searches, per country | daily RSS |
TikTok Creative Center and Reddit JSON were tested and refused (redirect/403). Not used.

## Channel B: original local reporting (WebSearch, domain filter)
Tested and productive (produced a pick or a strong candidate): sixthtone.com · scmp.com · globaltimes.cn · dexerto.com · koreaherald.com · koreatimes.co.kr · view.asiae.co.kr · en.nocutnews.co.kr · mothership.sg · ibtimes.co.uk · today.com · weartv.com/wkrg.com (local TV).
Tested and working, not yet productive: nbcnews.com · cbsnews.com · abcnews.go.com · foxbusiness.com · dailydot.com · futurism.com · 404media.co · sfgate.com · inc.com · entrepreneur.com · modernretail.co · glossy.co · retaildive.com · restaurantbusinessonline.com · nrn.com · soranews24.com · japantoday.com · koreajoongangdaily.joins.com · koreabizwire.com · abc.net.au · stuff.co.nz · nzherald.co.nz · thethaiger.com · kr-asia.com · hk01.com.
Chinese-language (search in Chinese, no domain filter): 极目新闻 ctdsb.net · 香港01 · 新京报 bjnews.com.cn · 36kr · 每日经济新闻 nbd.com.cn · 中华网 · 网易 163.com.
Refused by the search tool's domain filter (search without a filter): reddit.com · straitstimes.com · smh.com.au · 9news.com.au · asahi.com · eater.com · foodandwine.com · nypost.com · bbc · guardian · businessinsider.

### Front pages (read with WebFetch for the past 7 days; tested 2026-11-03)
Productive or promising: sixthtone.com (home) · scmp.com/news/people-culture/trending-china (list works; article pages 403) · globaltimes.cn/china/society/index.html · ctdsb.net (Jimu, Chinese) · j-cast.com (Japanese) · soranews24.com · dexerto.com/food/ · mothership.sg · koreatimes.co.kr/southkorea/society.
Working, nothing usable yet: nlab.itmedia.co.jp (consumer listicles) · thestandard.com.hk · hk01.com zone pages · taiwannews.com.tw · worldofbuzz.com · e.vnexpress.net/news/trend · thethaiger.com/hot-news.
Unreachable: whatsonweibo.com · unseen-japan.com · insight.co.kr · toutiao.com · mrjjxw.com (DNS) · japantoday.com (Akamai block) · koreajoongangdaily (refused) · tophub.today (403) · koreaherald list URL (404; find the right section URL).
Refused by the search tool's domain filter (3 Nov): mainichi.jp · news.com.au · 7news.com.au · threads.net · UK regional papers (Manchester Evening News, Liverpool Echo, WalesOnline, Birmingham Mail, Chronicle Live, Irish Mirror, Independent.ie).

## Yield (stories per source per week)
One row per run. Count where each story was **first found**, not where it was verified. Picks = cards rated ≥ 8.5; owner RUN = the owner's verdict.

| Week | Source | Candidates found | Cards shown | Picks | Owner RUN |
|---|---|---|---|---|---|
| 2026-W45 | Sixth Tone / SCMP / Global Times (B) | 6 | 2 | 2 | 2 (Mo's, Xibei) |
| 2026-W45 | Dexerto (B) | 2 | 1 | 1 | 1 (Lacy/Zauo) |
| 2026-W45 | Korea Herald / Korea Times / Asiae / Nocut (B) | 5 | 2 | 1 | 0 |
| 2026-W45 | Mothership (B) | 6 | 2 | 0 | 0 |
| 2026-W45 | TODAY / NBC / CBS local / local TV (B) | 10 | 4 | 0 | 0 |
| 2026-W45 | Chinese-language outlets: Jimu, HK01, NBD, Beijing News (B) | 4 | 0 | 0 | 0 (but found Mo's Chicken's October third act) |
| 2026-W45 | r/nottheonion RSS (A) | 5 | 0 | 0 | 0 |
| 2026-W45 | r/LivestreamFail RSS (A) | 1 (Lacy, already found) | 0 | 0 | 0 |
| 2026-W45 | r/singapore RSS (A) | 1 | 0 | 0 | 0 |
| 2026-W45 | X via search + embed data (A) | 10 | 0 | 0 | 0 (but gave Lacy's original clips + engagement) |
| 2026-W45 | TikTok via search (A) | 4 | 0 | 0 | 0 |
| 2026-W45 | YouTube / Bilibili / Douyin via search (A) | 6 | 0 | 0 | 0 (but gave Mo's original + HK01 clip) |
| 2026-W45 | Google Trends RSS (A) | 0 | 0 | 0 | 0 |
| 2026-W45 (r6) | Front pages of proven outlets: Sixth Tone, Global Times, SCMP list, Jimu, J-CAST, Korea Times, Mothership (B) | 11 | 1 (B-19) | 0 | pending |
| 2026-W45 (r6) | Chinese-language search → udn / HK01 (B) | 1 | 1 (B-20) | 0 | pending |
| 2026-W45 (r6) | Narrative-pattern searches, 4 languages | 2 (both old) | 0 | 0 | 0 |
| 2026-W45 (r6) | Reddit RSS + Trends RSS (A) | 1 | 0 | 0 | 0 |
