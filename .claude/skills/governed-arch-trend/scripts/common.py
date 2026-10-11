"""governed-arch-trend 공통 경로·입출력.

코드와 refs는 공개 저장소(governed-arch-opinion)에서, 수집 상태와 후보 큐는
비공개 상태 폴더(GAT_STATE, 기본 ~/한양대학교/governed-arch-trend)에서 읽고 쓴다.
"""
import json
import os
import pathlib

SKILL = pathlib.Path(__file__).resolve().parent.parent
REPO = pathlib.Path(os.environ.get("GAT_REPO", SKILL.parent.parent.parent))
REFS = REPO / "refs"
STATE = pathlib.Path(os.environ.get("GAT_STATE", pathlib.Path.home() / "한양대학교" / "governed-arch-trend"))
DATA = STATE / "_data"
QUEUE = STATE / "queue"


def load(path, default=None):
    p = pathlib.Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def save(path, obj):
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(p)
