"""Channel A feed scan: recent posts from the watchlist's Reddit RSS feeds and Google Trends RSS.

Usage: python3 shared/tools/feeds.py [days]   (default 7)
Prints one line per item: date | source | title | link. Feeds come from
droptopost-research/sources/WATCHLIST.md (lines starting with "- feed:").
Honest user agent, a pause between requests, no login. A feed that fails prints FAIL and the scan goes on.
"""
import re, sys, time, urllib.request, html
from datetime import datetime, timedelta, timezone

UA = "droptopost-research/0.1 (story research; contact via github.com/DejmoGG)"
days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
cutoff = datetime.now(timezone.utc) - timedelta(days=days)
feeds = re.findall(r"^- feed: (\S+)\s+\|\s*(.+)$", open("droptopost-research/sources/WATCHLIST.md", encoding="utf-8").read(), re.M)

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")

for url, name in feeds:
    try:
        x = get(url)
    except Exception as e:
        print(f"FAIL | {name} | {e}")
        time.sleep(45 if "reddit" in url else 2)
        continue
    items = re.findall(r"<entry>(.*?)</entry>", x, re.S) or re.findall(r"<item>(.*?)</item>", x, re.S)
    if not items:
        print(f"FAIL | {name} | no items (rate-limited or blocked)")
    for it in items:
        title = html.unescape(re.sub(r"<[^>]+>", "", (re.search(r"<title>(.*?)</title>", it, re.S) or [None, ""])[1])).strip()
        link = re.search(r'<link href="([^"]+)"', it) or re.search(r"<link>(.*?)</link>", it, re.S)
        date = re.search(r"<updated>(.*?)</updated>", it) or re.search(r"<published>(.*?)</published>", it) or re.search(r"<pubDate>(.*?)</pubDate>", it)
        traffic = re.search(r"<ht:approx_traffic>(.*?)</ht:approx_traffic>", it)
        d = date.group(1).strip() if date else ""
        try:
            dt = datetime.fromisoformat(d.replace("Z", "+00:00")) if "T" in d else datetime.strptime(d, "%a, %d %b %Y %H:%M:%S %z")
            if dt < cutoff:
                continue
            d = dt.strftime("%Y-%m-%d")
        except ValueError:
            pass
        extra = f" ({traffic.group(1)} searches)" if traffic else ""
        print(f"{d} | {name} | {title}{extra} | {link.group(1).strip() if link else ''}")
    time.sleep(45 if "reddit" in url else 2)
