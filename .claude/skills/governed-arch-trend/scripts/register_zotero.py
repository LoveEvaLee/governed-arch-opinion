#!/usr/bin/env python3
"""내려받은 자료(PDF)가 있는 후보를 Zotero **그룹 라이브러리**에 서지로 등록 — VM/무인 실행용.

개인 라이브러리(논문 — 헤르메스)와 섞지 않는 것이 요점이다:
- 등록 대상 그룹은 ①환경변수 GAT_ZOTERO_GROUP_ID ②_data/zotero_group.json
  ③이름이 'governed-arch'로 시작하는 그룹 자동 탐색 순으로 정한다.
- 그룹이 없으면 **등록하지 않고 스킵**한다(개인 라이브러리 폴백 금지 — 오염 방지).
  그룹 생성은 zotero.org/groups/new (비공개, 이름 governed-arch-refs 권장) — 1회 수동.
- 파일은 업로드하지 않는다(스토리지 무사용). 서지 + 원문 URL + extra에 로컬 경로.
- API 키: 환경변수 ZOTERO_API_KEY(VM .harness-env) → 맥 키체인 zotero-api 폴백.
  키의 groups 권한은 2026-10-29 확인 — all library+write.
- 장부: _data/zotero_registered.json (후보 id 집합) — 재실행 중복 없음.

오늘치만 보지 않고 최근 14일 digest의 미등록 자료 후보를 소급 등록한다 —
그룹을 나중에 만들어도 그동안 쌓인 자료가 유실되지 않는다.
사용: register_zotero.py (날짜 인자는 받아도 무시 — 항상 최근 14일 스캔)
"""
import glob
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

from common import DATA, load, save

API = "https://api.zotero.org"
UA = "governed-arch-trend/1.0 (mailto:soda027@gmail.com)"
LEDGER = DATA / "zotero_registered.json"
GROUP_CFG = DATA / "zotero_group.json"
GROUP_PREFIX = "governed-arch"


def api_key():
    k = os.environ.get("ZOTERO_API_KEY", "").strip()
    if k:
        return k
    try:
        return subprocess.run(["security", "find-generic-password", "-s", "zotero-api",
                               "-a", "loveva60", "-w"], capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return ""


def fetch(url, key, data=None, method=None):
    headers = {"User-Agent": UA, "Zotero-API-Key": key}
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def find_group(key):
    gid = os.environ.get("GAT_ZOTERO_GROUP_ID", "").strip()
    if gid:
        return gid
    cfg = load(GROUP_CFG)
    if cfg and cfg.get("group_id"):
        return str(cfg["group_id"])
    uid = fetch(f"{API}/keys/current", key)["userID"]
    for g in fetch(f"{API}/users/{uid}/groups", key):
        if g["data"]["name"].lower().startswith(GROUP_PREFIX):
            save(GROUP_CFG, {"group_id": g["id"], "name": g["data"]["name"]})
            return str(g["id"])
    return None


def pub_date(c):
    m = re.search(r"발행 (\d{4}-\d{2}-\d{2})", c.get("date_info", ""))
    return m.group(1) if m else ""


def item_of(c, date):
    extra = [f"등급 {c.get('grade', '?')} — {c.get('grade_claim', '')}"]
    for rel in c.get("files", []):
        extra.append(f"로컬 파일: ~/한양대학교/governed-arch-trend/{rel}")
    return {
        "itemType": "report",
        "title": c.get("title_ko") or c.get("url", ""),
        "institution": c.get("source_name", ""),
        "date": pub_date(c),
        "url": c.get("url", ""),
        "abstractNote": (c.get("summary_ko", "") + ("\n\n왜 후보인가: " + c["why_ko"] if c.get("why_ko") else "")).strip(),
        "extra": "\n".join(extra),
        "tags": [{"tag": f"gat/{c.get('area', 'etc')}"}, {"tag": f"gat/daily/{date}"}],
    }


def main():
    ledger = set(load(LEDGER, []))
    todo, total = [], 0  # (digest 날짜, 후보)
    for p in sorted(glob.glob(str(DATA / "digests" / "2*.json")))[-14:]:
        d = os.path.basename(p)[:-5]
        for c in (load(p) or {}).get("candidates", []):
            if not c.get("files"):
                continue
            total += 1
            if c["id"] not in ledger:
                todo.append((d, c))
    if not todo:
        print(f"[zotero] 신규 등록 대상 없음 (최근 14일 자료 후보 {total}건)")
        return 0
    key = api_key()
    if not key:
        print("[zotero] API 키 없음(env ZOTERO_API_KEY / 키체인 zotero-api) — 스킵")
        return 0
    try:
        gid = find_group(key)
    except Exception as e:
        print(f"[zotero] 그룹 탐색 실패: {e} — 다음 실행에서 재시도")
        return 0
    if not gid:
        print(f"[zotero] '{GROUP_PREFIX}*' 그룹 없음 — 등록 보류(개인 라이브러리에는 넣지 않는다). "
              "zotero.org/groups/new 에서 비공개 그룹(governed-arch-refs)을 만들면 다음 실행부터 자동 등록")
        return 0
    items = [item_of(c, d) for d, c in todo]
    ok = 0
    for i in range(0, len(items), 50):  # Web API 요청당 50건 제한
        batch, bc = items[i:i + 50], todo[i:i + 50]
        try:
            res = fetch(f"{API}/groups/{gid}/items", key, data=json.dumps(batch).encode(), method="POST")
            good = {int(x) for x in res.get("success", {})} | {int(x) for x in res.get("unchanged", {})}
            for j, (_, c) in enumerate(bc):
                if j in good:
                    ledger.add(c["id"])
                    ok += 1
                else:
                    print(f"[zotero] 실패: {c['id']} → {res.get('failed', {}).get(str(j))}")
        except Exception as e:
            print(f"[zotero] 배치 등록 실패: {e} — 다음 실행에서 재시도")
        time.sleep(0.4)
    save(LEDGER, sorted(ledger))
    print(f"[zotero] 그룹 {gid}에 {ok}/{len(items)}건 등록 (장부 {len(ledger)}건)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
