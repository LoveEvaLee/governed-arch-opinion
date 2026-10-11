#!/bin/bash
# 파이프라인 치명 실패 알림 — 로그 + 볼트 알림파일 + 메일.
# 사용법: notify_failure.sh "<제목>" "<상세>"
# 메일은 GMAIL_APP_PASSWORD(VM: /root/.harness-env) 또는 키체인 argus-gmail(맥)에서 자격을 얻는다.
# 자격이 없으면 조용히 알림파일만 남긴다(알림 실패가 파이프라인을 죽이지 않는다).
TITLE="${1:-파이프라인 실패}"
BODY="${2:-}"
HOST="$(hostname)"
WHEN="$(date '+%Y-%m-%d %H:%M:%S %Z')"

# 알림 파일 — 볼트에 남아 git 동기화·Obsidian에서 바로 보인다.
STATE_DIR="${GAT_STATE:-$HOME/한양대학교/governed-arch-trend}"
ALERTS="$STATE_DIR/_data/alerts.log"
mkdir -p "$(dirname "$ALERTS")" 2>/dev/null
printf '[%s] %s — %s\n%s\n\n' "$WHEN" "$HOST" "$TITLE" "$BODY" >> "$ALERTS"
echo "[알림] $TITLE (기록: $ALERTS)"

# 메일 — 유경 개인 메일로 운영 알림
TO="${HARNESS_ALERT_TO:-soda027@gmail.com}"
PW="$GMAIL_APP_PASSWORD"
[ -z "$PW" ] && PW="$(security find-generic-password -s argus-gmail -w 2>/dev/null)"
if [ -z "$PW" ]; then
  echo "[알림] 메일 자격 없음 — 파일 기록만 남김"
  exit 0
fi
if [ -n "$HARNESS_ALERT_DRYRUN" ]; then
  echo "[알림] dry-run — 메일 발송 생략"
  exit 0
fi
PW="$PW" TO="$TO" TITLE="$TITLE" BODY="$BODY" HOST="$HOST" WHEN="$WHEN" python3 - <<'PY'
import os, smtplib, ssl
from email.message import EmailMessage
m = EmailMessage()
m["From"] = "soda027@gmail.com"
m["To"] = os.environ["TO"]
m["Subject"] = f"[governed-arch-trend 경보] {os.environ['TITLE']}"
m.set_content(
    f"호스트: {os.environ['HOST']}\n시각: {os.environ['WHEN']}\n\n{os.environ['BODY']}\n"
)
try:
    # Hetzner VM은 25/465 차단, 587만 열림 — 587(STARTTLS) 우선, 465 폴백.
    try:
        c = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
        c.starttls(context=ssl.create_default_context())
    except OSError:
        c = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context(), timeout=30)
    with c as s:
        s.login("soda027@gmail.com", os.environ["PW"].strip())
        s.send_message(m)
    print("[알림] 메일 발송 완료")
except Exception as e:
    print(f"[알림] 메일 발송 실패: {e}")
PY
exit 0
