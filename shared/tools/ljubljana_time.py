"""Print the current Europe/Ljubljana hour and date without needing tzdata.

EU rule: summer time (UTC+2) runs from the last Sunday of March 01:00 UTC
to the last Sunday of October 01:00 UTC; otherwise UTC+1.
"""
from datetime import datetime, timedelta, timezone


def last_sunday(year, month):
    d = datetime(year, month + 1, 1, tzinfo=timezone.utc) - timedelta(days=1)
    return d - timedelta(days=(d.weekday() + 1) % 7)


now = datetime.now(timezone.utc)
start = last_sunday(now.year, 3).replace(hour=1)
end = last_sunday(now.year, 10).replace(hour=1)
local = now + timedelta(hours=2 if start <= now < end else 1)
print(f"HOUR={local:%H}")
print(f"DATE={local:%Y-%m-%d}")
print(f"UTC={now:%Y-%m-%dT%H:%M}Z")
