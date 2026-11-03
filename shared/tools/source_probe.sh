#!/usr/bin/env bash
# Checks which discovery sources this machine can reach. One line per source: OK / FAIL + what came back.
# Honest user agent, one request per source, no login, no workarounds for sites that refuse scripts.
UA="droptopost-research/0.1 (story research; contact via github.com/DejmoGG)"
t() { curl -s -m 20 -A "$UA" "$@"; }

r=$(t "https://www.reddit.com/r/smallbusiness/top/.rss?t=week" | grep -c '<entry>')
[ "$r" -gt 0 ] && echo "OK   Reddit RSS ($r entries; titles/links/dates, no vote counts)" || echo "FAIL Reddit RSS"

r=$(t "https://trends.google.com/trending/rss?geo=US" | grep -c '<ht:approx_traffic>')
[ "$r" -gt 0 ] && echo "OK   Google Trends daily RSS ($r trends with approx traffic)" || echo "FAIL Google Trends RSS"

r=$(t "https://www.youtube.com/watch?v=N_aTLpWLSJc" | grep -o '"viewCount":"[0-9]*"' | head -1)
[ -n "$r" ] && echo "OK   YouTube watch page ($r)" || echo "FAIL YouTube watch page"

r=$(t "https://cdn.syndication.twimg.com/tweet-result?id=2115522862131941553&lang=en&token=4" | grep -o '"favorite_count":[0-9]*')
[ -n "$r" ] && echo "OK   X embed data ($r)" || echo "FAIL X embed data"

r=$(t "https://www.tiktok.com/oembed?url=https://www.tiktok.com/@tiktok/video/7106594312292453675" | grep -o '"provider_name":"TikTok"')
[ -n "$r" ] && echo "OK   TikTok oEmbed ($r; no view counts)" || echo "FAIL TikTok oEmbed"

r=$(t -o /dev/null -w "%{http_code}" "https://www.instagram.com/p/DdmKxc1BfW3/embed/captioned/")
[ "$r" = "200" ] && echo "OK   Instagram embed page (HTTP 200)" || echo "FAIL Instagram embed page (HTTP $r)"

r=$(t -o /dev/null -w "%{http_code}" "https://www.sixthtone.com/news/1018834")
[ "$r" = "200" ] && echo "OK   Sixth Tone (HTTP 200)" || echo "FAIL Sixth Tone (HTTP $r)"
