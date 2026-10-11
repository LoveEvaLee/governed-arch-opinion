"""수집분을 감시 대상과 맞춰 큐레이션할 후보 풀(_data/matched/{날짜}.json)을 만든다. 결정적 단계.

- 선택지 별칭에 걸린 항목 → 기존 선택지 관련(갱신 · 새 근거 후보)
- 별칭에는 안 걸리고 영역 키워드에만 걸린 항목 → 새 선택지 후보 풀(영역당 최대 KEYWORD_CAP건)
사용법: match.py [YYYY-MM-DD]
"""
import datetime as dt
import re
import sys

from common import DATA, load, save

KEYWORD_CAP = 15


def pattern(alias):
    # 짧은 별칭(dbt, DAG 등)은 단어 경계로만 — 'dbt'가 다른 단어 속에 걸리지 않게
    esc = re.escape(alias)
    return re.compile(rf"(?<![A-Za-z0-9]){esc}(?![A-Za-z0-9])", re.I)


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
    watch = load(DATA / "watch.json")
    col = load(DATA / "collected" / f"{date}.json")
    if not watch or col is None:
        print("[match] watch.json 또는 수집분 없음")
        return 1
    out = []
    for area, a in watch["areas"].items():
        opt_pats = {o: [pattern(x) for x in al] for o, al in a["options"].items()}
        kw_pats = [pattern(k) for k in a["keywords"]]
        kw_only = 0
        for it in col["items"]:
            text = f"{it['title']} {it['summary']}"
            hit = [o for o, ps in opt_pats.items() if any(p.search(text) for p in ps)]
            if hit:
                out.append({**it, "area": area, "area_file": a["file"], "matched_options": hit, "pool": "선택지"})
            elif kw_pats and any(p.search(text) for p in kw_pats) and kw_only < KEYWORD_CAP:
                out.append({**it, "area": area, "area_file": a["file"], "matched_options": [], "pool": "영역 키워드"})
                kw_only += 1
    save(DATA / "matched" / f"{date}.json", {"date": date, "count": len(out), "items": out})
    by = {}
    for x in out:
        by[x["pool"]] = by.get(x["pool"], 0) + 1
    print(f"[match] {date} 후보 풀 {len(out)}건 {by} (수집 {len(col['items'])}건 중)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
