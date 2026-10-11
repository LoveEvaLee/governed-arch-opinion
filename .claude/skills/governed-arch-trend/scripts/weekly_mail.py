"""지난 7일 후보 큐를 요약해 개인 메일로 보낸다(월요일 아침, 2026-10-11 유경 결정).

자격: GMAIL_APP_PASSWORD 환경변수(VM: /root/.harness-env) 또는 맥 키체인 argus-gmail.
받는 주소: GAT_MAIL_TO(기본 soda027@gmail.com). --preview면 보내지 않고 HTML만 저장한다.
사용법: weekly_mail.py [YYYY-MM-DD] [--preview]
"""
import datetime as dt
import html
import os
import smtplib
import ssl
import subprocess
import sys
from email.message import EmailMessage

from common import DATA, STATE, load

TO = os.environ.get("GAT_MAIL_TO", "soda027@gmail.com")


def password():
    pw = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
    if pw:
        return pw
    try:
        return subprocess.run(["security", "find-generic-password", "-s", "argus-gmail", "-w"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    preview = "--preview" in sys.argv
    end = dt.date.fromisoformat(args[0]) if args else dt.date.today()
    days = [(end - dt.timedelta(days=i)).isoformat() for i in range(7, 0, -1)]
    rows, total = [], {"갱신": 0, "새 근거": 0, "새 선택지": 0}
    for d in days:
        dg = load(DATA / "digests" / f"{d}.json")
        if not dg:
            continue
        for c in dg.get("candidates", []):
            if not c.get("url_ok"):
                continue
            total[c["kind"]] = total.get(c["kind"], 0) + 1
            rows.append((d, c))
    subject = (f"[governed-arch-trend] 주간 후보 {len(rows)}건 — "
               f"갱신 {total['갱신']} · 새 근거 {total['새 근거']} · 새 선택지 {total['새 선택지']}"
               f" ({days[0]} ~ {days[-1]})")
    trs = "".join(
        f"<tr><td style='padding:6px 8px;border-bottom:1px solid #eee;white-space:nowrap'>{d}</td>"
        f"<td style='padding:6px 8px;border-bottom:1px solid #eee'>{html.escape(c['kind'])}</td>"
        f"<td style='padding:6px 8px;border-bottom:1px solid #eee'>{html.escape(c['option'] or '(새 선택지)')}</td>"
        f"<td style='padding:6px 8px;border-bottom:1px solid #eee'><a href='{html.escape(c['url'])}'>{html.escape(c['title_ko'])}</a>"
        f"<br><span style='color:#666;font-size:12px'>{html.escape(c['grade'])} · {html.escape(c['summary_ko'])}</span></td></tr>"
        for d, c in rows)
    body = (
        "<div style='font-family:sans-serif;font-size:14px;color:#222;max-width:720px'>"
        f"<p>지난 7일({days[0]} ~ {days[-1]}) 후보 큐 요약입니다. 판정은 없고, 반영 여부는 큐 노트에서 체크한 뒤 "
        "\"후보 반영해줘\"로 정합니다.</p>"
        + (f"<table style='border-collapse:collapse;width:100%'>{trs}</table>" if rows else "<p>이번 주 후보가 없습니다.</p>")
        + f"<p style='color:#888;font-size:12px'>큐 노트: {html.escape(str(STATE / 'queue'))}</p></div>")
    if preview:
        out = DATA / "mail_preview.html"
        out.write_text(body, encoding="utf-8")
        print(f"[mail] 미리보기 저장 {out} — {subject}")
        return 0
    pw = password()
    if not pw:
        print("[mail] 메일 자격 없음 — 발송 생략")
        return 1
    m = EmailMessage()
    m["From"], m["To"], m["Subject"] = "soda027@gmail.com", TO, subject
    m.set_content("HTML 메일입니다.")
    m.add_alternative(body, subtype="html")
    try:  # Hetzner VM은 25/465 차단, 587만 열림 — 587 우선, 465 폴백
        c = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
        c.starttls(context=ssl.create_default_context())
    except OSError:
        c = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context(), timeout=30)
    with c as s:
        s.login("soda027@gmail.com", pw)
        s.send_message(m)
    print(f"[mail] 발송 완료 → {TO}: {subject}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
