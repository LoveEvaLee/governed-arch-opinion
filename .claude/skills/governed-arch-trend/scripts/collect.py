"""config/sources.json의 RSS·Atom 피드와 GitHub 릴리스를 모아 _data/collected/{날짜}.json에 쓴다.

소스 하나가 실패해도 나머지는 계속한다. 이미 본 항목은 _data/seen.json으로 거른다.
사용법: collect.py [--days N] [--date YYYY-MM-DD]
"""
import argparse
import datetime as dt
import email.utils
import hashlib
import html
import json
import re
import time
import urllib.request
import xml.etree.ElementTree as ET

from common import DATA, SKILL, load, save

UA = {"User-Agent": "Mozilla/5.0 (governed-arch-trend)"}
NS = {"a": "http://www.w3.org/2005/Atom"}


def get(url, accept=None, tries=3):
    headers = dict(UA)
    if accept:
        headers["Accept"] = accept
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
                return r.read()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(5 * (i + 1))


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d


def clean(s, n=600):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    return re.sub(r"\s+", " ", s).strip()[:n]


def rss_items(src, raw):
    root = ET.fromstring(raw)
    out = []
    for it in root.iter("item"):  # RSS 2.0
        out.append({
            "title": clean(it.findtext("title"), 300),
            "url": (it.findtext("link") or "").strip(),
            "published": it.findtext("pubDate") or it.findtext("{http://purl.org/dc/elements/1.1/}date"),
            "summary": clean(it.findtext("description")),
        })
    for e in root.findall("a:entry", NS):  # Atom
        link = ""
        for l in e.findall("a:link", NS):
            if l.get("rel", "alternate") == "alternate":
                link = l.get("href", "")
                break
        out.append({
            "title": clean(e.findtext("a:title", namespaces=NS), 300),
            "url": link,
            "published": e.findtext("a:published", namespaces=NS) or e.findtext("a:updated", namespaces=NS),
            "summary": clean(e.findtext("a:summary", namespaces=NS) or e.findtext("a:content", namespaces=NS)),
        })
    return out


def gh_items(src):
    raw = get(f"https://api.github.com/repos/{src['repo']}/releases?per_page=10", "application/vnd.github+json")
    out = []
    for r in json.loads(raw):
        if r.get("draft"):
            continue
        out.append({
            "title": f"{src['repo']} {r.get('name') or r.get('tag_name')}" + (" (pre-release)" if r.get("prerelease") else ""),
            "url": r.get("html_url", ""),
            "published": r.get("published_at"),
            "summary": clean(r.get("body"), 800),
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=2)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    a = ap.parse_args()
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=a.days)
    cfg = load(SKILL / "config" / "sources.json")
    seen = set(load(DATA / "seen.json", []))
    items, status = [], {}
    jobs = [(s, "rss") for s in cfg["rss"]] + [(s, "gh") for s in cfg["github_releases"]]
    for src, kind in jobs:
        try:
            got = gh_items(src) if kind == "gh" else rss_items(src, get(src["url"]))
        except Exception as e:
            status[src["id"]] = f"실패: {type(e).__name__}: {e}"[:200]
            continue
        n = 0
        for it in got:
            if not it["url"]:
                continue
            d = parse_date(it["published"])
            if d and d < cutoff:
                continue
            iid = hashlib.sha1(it["url"].encode()).hexdigest()[:16]
            if iid in seen:
                continue
            seen.add(iid)
            it.update(id=iid, source=src["id"], source_name=src["name"], source_grade=src["grade"],
                      published=d.date().isoformat() if d else None)
            items.append(it)
            n += 1
        status[src["id"]] = f"{n}건"
    save(DATA / "collected" / f"{a.date}.json", {"date": a.date, "window_days": a.days, "status": status, "items": items})
    save(DATA / "seen.json", sorted(seen))
    fails = [k for k, v in status.items() if v.startswith("실패")]
    print(f"[collect] {a.date} 수집 {len(items)}건 (최근 {a.days}일), 실패 소스 {len(fails)}개 {fails or ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
