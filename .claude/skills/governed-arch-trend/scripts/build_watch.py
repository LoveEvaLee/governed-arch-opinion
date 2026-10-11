"""refs/*.md의 「선택지 요약」 표에서 감시 대상을 뽑아 _data/watch.json을 만든다.

수집이 끝난 영역(선택지 요약 표가 있는 refs)만 감시한다 — 2026-10-11 유경 결정.
별칭·영역 키워드는 config/aliases.json에서 덧붙인다. 별칭이 없는 선택지는 이름만으로 매칭한다.
"""
import re
import sys

from common import DATA, REFS, SKILL, load, save


def options_in(md):
    m = re.search(r"^## 선택지 요약\s*\n(.*?)(?=^## |\Z)", md, re.M | re.S)
    if not m:
        return []
    rows = [l for l in m.group(1).splitlines() if l.startswith("|")]
    names = []
    for row in rows[2:]:  # 머리줄 · 구분줄 건너뜀
        cell = row.strip("|").split("|")[0].strip()
        if cell:
            names.append(cell)
    return names


def main():
    aliases = load(SKILL / "config" / "aliases.json", {}).get("areas", {})
    areas = {}
    for f in sorted(REFS.glob("*.md")):
        if f.stem == "비교표":
            continue
        names = options_in(f.read_text(encoding="utf-8"))
        if not names:
            continue
        a = aliases.get(f.stem, {})
        opt_alias = a.get("options", {})
        areas[f.stem] = {
            "file": f"refs/{f.name}",
            "area_name": a.get("area_name", f.stem),
            "keywords": a.get("keywords", []),
            "options": {n: sorted(set([n] + opt_alias.get(n, []))) for n in names},
        }
        missing = [n for n in names if n not in opt_alias]
        if missing:
            print(f"[watch] {f.stem}: 별칭 없는 선택지 {missing} — 이름으로만 매칭")
    save(DATA / "watch.json", {"areas": areas})
    print(f"[watch] 감시 영역 {len(areas)}개, 선택지 {sum(len(v['options']) for v in areas.values())}개")
    return 0 if areas else 1


if __name__ == "__main__":
    sys.exit(main())
