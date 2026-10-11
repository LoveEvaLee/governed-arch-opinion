"""큐레이션 결과(_data/digests/{날짜}.json)를 후보 큐 노트(queue/{날짜}.md)로 쓴다.

후보마다 URL을 실제로 열어 보고(HTTP 200) 열리지 않는 후보는 「URL 확인 실패」로 따로 둔다 —
검수할 때 열어 본 URL만 refs에 들어가게 하려는 것(① 동향수집 「거르는 기준」).
사용법: render_queue.py [YYYY-MM-DD]
"""
import datetime as dt
import sys
import urllib.request

from common import DATA, QUEUE, load, save

KINDS = ["갱신", "새 근거", "새 선택지"]


def url_ok(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:
        return False


def block(c):
    axes = " / ".join(c.get("axes", [])) or "〔미정〕"
    rel = c.get("related_evidence") or "없음"
    return "\n".join([
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
        "",
        f"- [ ] 반영 · id `{c['id']}`",
        "",
    ])


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
    dg = load(DATA / "digests" / f"{date}.json")
    if dg is None:
        print(f"[render] {date} digest 없음 — 큐 노트를 만들지 않음")
        return 1
    cands = dg.get("candidates", [])
    for c in cands:
        c["url_ok"] = url_ok(c["url"])
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
