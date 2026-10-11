#!/bin/bash
# governed-arch-trend 일일 실행 (VM 크론 06:30 KST가 본체).
# 결정적 단계(감시 목록·수집·매칭·렌더·메일)는 스크립트로, 판단 단계(큐레이션)만 headless claude로.
# 환경: GAT_REPO(공개 저장소 경로) · GAT_STATE(비공개 상태 폴더) · GAT_PULL_REPO=1(VM에서만 공개 저장소 pull)
export PATH="/opt/homebrew/bin:$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin${PATH:+:$PATH}"
export LANG="ko_KR.UTF-8"

SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPTS")"
export GAT_REPO="${GAT_REPO:-$(cd "$SKILL_DIR/../../.." && pwd)}"
export GAT_STATE="${GAT_STATE:-$HOME/한양대학교/governed-arch-trend}"
DATA="$GAT_STATE/_data"
TODAY=$(date +%Y-%m-%d)
LOG="$DATA/cron.log"
mkdir -p "$DATA"

# headless claude 인증 — 맥은 키체인, VM은 호출자가 CLAUDE_CODE_OAUTH_TOKEN을 넘긴다
if [ -z "$CLAUDE_CODE_OAUTH_TOKEN" ] && command -v security >/dev/null 2>&1; then
  T=$(security find-generic-password -s claude-oauth-token -w 2>/dev/null); [ -n "$T" ] && export CLAUDE_CODE_OAUTH_TOKEN="$T"
fi

notify() { bash "$SCRIPTS/notify_failure.sh" "$1" "$2" >> "$LOG" 2>&1; }
push_state() {
  [ -d "$GAT_STATE/.git" ] || return 0
  git -C "$GAT_STATE" add -A && git -C "$GAT_STATE" commit -qm "$TODAY $1" 2>/dev/null
  git -C "$GAT_STATE" push -q 2>>"$LOG" || echo "[!] 상태 리포 push 실패 — 다음 실행에서 다시 push" >> "$LOG"
}

echo "===================== $(date) 시작 =====================" >> "$LOG"

# 네트워크 게이트 — 횟수가 아니라 벽시계 기한(8시간) 기준(아르고스·헤르메스 9/11 교훈)
DEADLINE=$(( $(date +%s) + 28800 )); TRY=0; NET_OK=""
while [ "$(date +%s)" -lt "$DEADLINE" ]; do
  if curl -s -m 10 https://aws.amazon.com -o /dev/null || curl -s -m 10 https://api.github.com -o /dev/null; then NET_OK=1; break; fi
  TRY=$((TRY + 1)); [ $((TRY % 10)) -eq 1 ] && echo "$(date) 네트워크 대기 중 (시도 $TRY)" >> "$LOG"; sleep 60
done
[ -z "$NET_OK" ] && { echo "$(date) 기한 내 네트워크 미연결 — 종료(다음 실행에서 재시도)" >> "$LOG"; exit 0; }

# 최신 상태 받기 — 공개 저장소는 VM에서만 pull(맥에서는 유경의 작업 사본이라 건드리지 않음)
[ "$GAT_PULL_REPO" = "1" ] && { git -C "$GAT_REPO" pull -q --ff-only >> "$LOG" 2>&1 || echo "[!] 공개 저장소 pull 실패 — 이전 refs로 진행" >> "$LOG"; }
[ -d "$GAT_STATE/.git" ] && { git -C "$GAT_STATE" pull -q --rebase --autostash >> "$LOG" 2>&1 || echo "[!] 상태 리포 pull 실패" >> "$LOG"; }

MONDAY=$([ "$(date +%u)" = "1" ] && echo 1)
send_weekly() {
  [ -n "$MONDAY" ] || return 0
  [ -f "$DATA/mail_sent/$TODAY" ] && return 0
  if python3 "$SCRIPTS/weekly_mail.py" "$TODAY" >> "$LOG" 2>&1; then
    mkdir -p "$DATA/mail_sent" && touch "$DATA/mail_sent/$TODAY"
  else
    echo "[!] 주간 메일 실패 — 다음 실행에서 재시도" >> "$LOG"
  fi
}

# 오늘 몫이 이미 끝났으면 메일만 확인하고 종료
if [ -f "$DATA/digests/$TODAY.json" ] && [ -f "$GAT_STATE/queue/$TODAY.md" ]; then
  echo "[skip] 오늘($TODAY) 큐 노트 있음" >> "$LOG"; send_weekly; push_state "메일"; exit 0
fi

# 1. 감시 목록
python3 "$SCRIPTS/build_watch.py" >> "$LOG" 2>&1 || { notify "governed-arch-trend: 감시 목록 없음" "refs에 「선택지 요약」 표가 있는 파일이 없다. GAT_REPO=$GAT_REPO"; exit 1; }

# 2. 수집 — 마지막 큐 노트 이후 공백만큼 창을 넓힌다. 같은 날 재실행은 수집분 재활용
LAST=$(ls -1 "$GAT_STATE/queue/"2*.md 2>/dev/null | tail -1 | xargs -I{} basename {} .md)
DAYS=2
if [ -n "$LAST" ]; then
  if date -j >/dev/null 2>&1; then GAP=$(( ( $(date -j -f %Y-%m-%d "$TODAY" +%s) - $(date -j -f %Y-%m-%d "$LAST" +%s) ) / 86400 ))
  else GAP=$(( ( $(date -d "$TODAY" +%s) - $(date -d "$LAST" +%s) ) / 86400 )); fi
  [ "$GAP" -gt 2 ] && DAYS=$((GAP + 1))
fi
if [ -f "$DATA/collected/$TODAY.json" ]; then
  echo "[1/4] 오늘 수집분 있음 — 재활용" >> "$LOG"
else
  echo "[1/4] 수집 (최근 ${DAYS}일)" >> "$LOG"
  python3 "$SCRIPTS/collect.py" --days "$DAYS" >> "$LOG" 2>&1 || { notify "governed-arch-trend: 수집 실패" "로그: $LOG"; exit 1; }
fi
# 수집만 되고 큐레이션 못 한 이전 날 항목을 오늘 수집분에 합친다 — seen에 이미 들어가 유실되는 것을 막음
python3 - "$DATA" "$TODAY" >> "$LOG" 2>&1 <<'PY'
import json, glob, os, sys
data, today = sys.argv[1], sys.argv[2]
tp = os.path.join(data, "collected", today + ".json")
cur = json.load(open(tp)); ids = {i["id"] for i in cur["items"]}; n = 0
for p in sorted(glob.glob(os.path.join(data, "collected", "*.json")))[-7:]:
    d = os.path.basename(p)[:-5]
    if d >= today or os.path.exists(os.path.join(data, "digests", d + ".json")):
        continue
    for it in json.load(open(p)).get("items", []):
        if it["id"] not in ids:
            ids.add(it["id"]); cur["items"].append(it); n += 1
if n:
    json.dump(cur, open(tp, "w"), ensure_ascii=False, indent=1); print(f"[병합] 미큐레이션 이전 수집분 {n}건 합류")
PY

# 3. 매칭
python3 "$SCRIPTS/match.py" "$TODAY" >> "$LOG" 2>&1 || { notify "governed-arch-trend: 매칭 실패" "로그: $LOG"; exit 1; }
POOLED=$(python3 -c "import json;print(json.load(open('$DATA/matched/$TODAY.json'))['count'])")
COLLECTED=$(python3 -c "import json;print(len(json.load(open('$DATA/collected/$TODAY.json'))['items']))")

# 4. 큐레이션 — 후보 풀이 비면 claude를 부르지 않고 빈 digest
if [ "$POOLED" = "0" ]; then
  python3 -c "import json;json.dump({'date':'$TODAY','collected':$COLLECTED,'pooled':0,'dropped':0,'candidates':[]},open('$DATA/digests/$TODAY.json','w'),ensure_ascii=False)"
  echo "[2/4] 후보 풀 0건 — 큐레이션 생략" >> "$LOG"
else
  CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude 2>/dev/null)}"
  for c in "$HOME/.local/bin/claude" /root/.local/bin/claude /opt/homebrew/bin/claude; do [ -z "$CLAUDE_BIN" ] && [ -x "$c" ] && CLAUDE_BIN="$c"; done
  [ -z "$CLAUDE_BIN" ] && { notify "governed-arch-trend: claude 실행 파일 없음" "PATH=$PATH — 수집분은 보존, 다음 실행에서 큐레이션"; push_state "수집만"; exit 1; }
  PROMPT="governed-arch-trend 큐레이션. $SKILL_DIR/SKILL.md 의 「큐레이션 규칙」만 따른다. 입력: $DATA/matched/$TODAY.json (후보 풀 ${POOLED}건, 수집 ${COLLECTED}건). 항목의 area_file은 $GAT_REPO 기준 상대 경로이고 읽기만 한다 — refs를 고치지 마라. 출력: $DATA/digests/$TODAY.json (스키마는 SKILL.md, collected=${COLLECTED}, pooled=${POOLED}, 확인일=$TODAY). 파일 저장 외 설명 생략."
  for try in 1 2 3; do
    echo "[2/4] 큐레이션 (시도 $try, 풀 ${POOLED}건)" >> "$LOG"
    (cd "$GAT_STATE" && "$CLAUDE_BIN" -p "$PROMPT" --permission-mode acceptEdits --add-dir "$GAT_REPO" >> "$LOG" 2>&1)
    python3 -c "import json;json.load(open('$DATA/digests/$TODAY.json'))" 2>/dev/null && break
    echo "[!] 큐레이션 시도 $try 실패(digest 없음 또는 JSON 오류)" >> "$LOG"; rm -f "$DATA/digests/$TODAY.json" 2>/dev/null; sleep 20
  done
  if [ ! -f "$DATA/digests/$TODAY.json" ]; then
    notify "governed-arch-trend: 큐레이션 3회 실패" "날짜=$TODAY 풀=${POOLED}건 — 수집분은 보존, 다음 실행에서 재시도"
    push_state "큐레이션 실패"; exit 0
  fi
fi

# 5. 큐 노트 (URL 확인 포함) · 6. 월요일 요약 메일
echo "[3/4] 큐 노트" >> "$LOG"
python3 "$SCRIPTS/render_queue.py" "$TODAY" >> "$LOG" 2>&1
echo "[4/4] 주간 메일(월요일만)" >> "$LOG"
send_weekly
push_state "큐"
echo "===================== $(date) 완료 =====================" >> "$LOG"
