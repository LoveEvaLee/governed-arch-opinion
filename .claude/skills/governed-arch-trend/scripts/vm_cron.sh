#!/bin/bash
# governed-arch-trend VM 크론 래퍼 — harness-vm에서 매일 06:30 KST.
# 시크릿 주입(/root/.harness-env) → run_daily.sh(공개 저장소 pull + 상태 리포 pull/push 포함).
# 공개 저장소는 https 읽기 전용 clone이라 VM에서 refs가 바뀌어도 밖으로 나가지 않는다.
export PATH="/root/.local/bin:/usr/local/bin:/usr/bin:/bin"
[ -x /root/.local/bin/claude ] && export CLAUDE_BIN=/root/.local/bin/claude
set -a; . /root/.harness-env; set +a
export GAT_REPO=/root/한양대학교/governed-arch-opinion
export GAT_STATE=/root/한양대학교/governed-arch-trend
export GAT_PULL_REPO=1
export PYTHONDONTWRITEBYTECODE=1
# 코드도 공개 저장소에 있으므로 실행 전에 받는다 — run_daily.sh 안의 pull은 이미 읽기 시작한 스크립트에 늦다
git -C "$GAT_REPO" pull -q --ff-only || echo "$(date) [vm] 공개 저장소 pull 실패 — 이전 코드로 진행"
exec bash "$GAT_REPO/.claude/skills/governed-arch-trend/scripts/run_daily.sh"
