"""큐레이션 결과(_data/digests/{날짜}.json)를 후보 큐 노트(queue/{날짜}.md)로 쓴다.

후보마다 URL을 실제로 열어 보고(HTTP 200) 열리지 않는 후보는 「URL 확인 실패」로 따로 둔다 —
검수할 때 열어 본 URL만 refs에 들어가게 하려는 것(① 동향수집 「거르는 기준」).
후보가 PDF거나 본문에 백서 · 보고서 PDF 링크가 있으면 files/{날짜}/로 내려받아 노트에 경로를 적는다.
사용법: render_queue.py [YYYY-MM-DD]
"""
import datetime as dt
import hashlib
import re
import sys
import urllib.parse
import urllib.request

from common import DATA, QUEUE, STATE, load, save

KINDS = ["갱신", "새 근거", "새 선택지"]
FILES = STATE / "files"
PDF_LINK = re.compile(r'<a[^>]+href=[\'"]([^\'"]+\.pdf(?:[?#][^\'"]*)?)[\'"][^>]*>(.*?)</a>', re.I | re.S)
PDF_HINT = re.compile(r"(whitepaper|white-paper|report|guide|ebook|백서|보고서|리포트|지침|가이드)", re.I)
MAX_PDF = 25 * 1024 * 1024  # 한 파일 25MB까지 — 상태 리포가 git이라 큰 파일은 경로만 남긴다
MAX_PER_DAY = 5  # 하루 다운로드 상한 — 폭주 방지


def fetch(url):
    """(HTTP 200 여부, Content-Type, 본문 바이트) — 본문은 MAX_PDF+1까지만 읽는다."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 200, (r.headers.get("Content-Type") or "").lower(), r.read(MAX_PDF + 1)
    except Exception:
        return False, "", b""


def save_pdf(url, data, date, cid, ledger):
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    if key in ledger:
        return ledger[key]
    if len(data) > MAX_PDF or not data[:5] == b"%PDF-":
        ledger[key] = None  # 너무 크거나 PDF가 아님 — 다시 시도하지 않게 기록만
        return None
    name = re.sub(r"[^\w.\-가-힣]+", "_", urllib.parse.unquote(url.split("?")[0].rsplit("/", 1)[-1]))[:120]
    rel = f"files/{date}/{cid[:8]}_{name}"
    p = STATE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    ledger[key] = rel
    return rel


def grab_files(c, date, html_body, budget, ledger):
    """후보의 PDF를 모은다 — 후보 URL 자체가 PDF거나, 본문의 백서류 PDF 링크(후보당 2개)."""
    out = []
    links = []
    if c["url"].split("?")[0].lower().endswith(".pdf"):
        links.append(c["url"])
    elif html_body:
        for m in PDF_LINK.finditer(html_body):
            href = urllib.parse.urljoin(c["url"], m.group(1))
            if PDF_HINT.search(href) or PDF_HINT.search(m.group(2) or ""):
                links.append(href)
    for href in list(dict.fromkeys(links))[:2]:
        if budget[0] <= 0:
            break
        key = hashlib.sha1(href.encode()).hexdigest()[:16]
        if key in ledger:
            if ledger[key]:
                out.append(ledger[key])
            continue
        ok, ctype, data = fetch(href)
        if not ok:
            continue
        rel = save_pdf(href, data, date, c["id"], ledger)
        if rel:
            out.append(rel)
            budget[0] -= 1
    return out


def block(c):
    axes = " / ".join(c.get("axes", [])) or "〔미정〕"
    rel = c.get("related_evidence") or "없음"
    lines = [
        f"### [{c['kind']}] {c['option'] or '(새 선택지)'} — {c['title_ko']}",
        "",
        "| 항목 | 내용 |",
        "|---|---|",
        f"| 출처 | {c['source_name']} · {c['url']} |",
        f"| 날짜 | {c['date_info']} |",
        f"| 등급 | {c['grade']} — {c['grade_claim']} |",
        f"| 요지 | {c['summary_ko']} |",
        f"| 걸리는 평가 축 | {axes} |",
        f"| 관련 기존 근거 | {rel} |",
        f"| 왜 후보인가 | {c['why_ko']} |",
    ]
    if c.get("files"):
        links = " · ".join(f"[{rel.rsplit('/', 1)[-1]}](../{rel})" for rel in c["files"])
        lines.append(f"| 자료(내려받음) | {links} |")
    lines += ["", f"- [ ] 반영 · id `{c['id']}`", ""]
    return "\n".join(lines)


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
    dg = load(DATA / "digests" / f"{date}.json")
    if dg is None:
        print(f"[render] {date} digest 없음 — 큐 노트를 만들지 않음")
        return 1
    cands = dg.get("candidates", [])
    ledger = load(DATA / "files_ledger.json", {})
    budget = [MAX_PER_DAY]
    for c in cands:
        ok, ctype, body = fetch(c["url"])
        c["url_ok"] = ok
        if not ok:
            continue
        try:
            if "pdf" in ctype or c["url"].split("?")[0].lower().endswith(".pdf"):
                rel = save_pdf(c["url"], body, date, c["id"], ledger)
                c["files"] = [rel] if rel else []
            else:
                c["files"] = grab_files(c, date, body.decode("utf-8", "ignore") if "html" in ctype else "", budget, ledger)
        except Exception as e:  # 자료 수집 실패가 큐 노트 생성을 막으면 안 된다
            print(f"[render] 자료 수집 실패({c['id']}): {type(e).__name__}: {e}")
            c["files"] = []
    save(DATA / "files_ledger.json", ledger)
    save(DATA / "digests" / f"{date}.json", dg)
    ok = [c for c in cands if c["url_ok"]]
    bad = [c for c in cands if not c["url_ok"]]
    lines = [
        f"# 후보 큐 — {date}",
        "",
        f"수집 {dg.get('collected', '?')}건 → 후보 풀 {dg.get('pooled', '?')}건 → 후보 {len(cands)}건"
        f" (URL 확인 {len(ok)} · 실패 {len(bad)}) · 버림 {dg.get('dropped', '?')}건",
        "",
        "판정(상 · 중 · 하)은 없다. 반영할 후보에 체크하고 \"후보 반영해줘\"라고 하면 ① 동향수집 지침대로 refs에 넣는다.",
        "",
    ]
    if not cands:
        lines.append("오늘은 후보가 없다.")
    for area in sorted({c["area"] for c in cands}):
        lines += [f"## {area}", ""]
        for k in KINDS:
            for c in [c for c in ok if c["area"] == area and c["kind"] == k]:
                lines.append(block(c))
    if bad:
        lines += ["## URL 확인 실패 — 반영 대상 아님", ""]
        lines += [f"- {c['source_name']} · {c['url']} — {c['title_ko']}" for c in bad]
    QUEUE.mkdir(parents=True, exist_ok=True)
    (QUEUE / f"{date}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[render] queue/{date}.md — 후보 {len(ok)}건 (URL 실패 {len(bad)}건)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
