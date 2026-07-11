#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Heart session-start status guard.

The guard is intentionally read-only. It never refreshes or writes another
workflow; it only reports whether the privacy-safe Visual status panorama is
fresh enough to use as a routing hint.
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path


try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DESKTOP = Path(__file__).resolve().parents[2]
VISUAL_STATUS = DESKTOP / "Visual Workflow Collection" / "reports" / "workflow_panorama_latest.html"
REGISTRY = DESKTOP / "Technical expert" / "ecosystem" / "registry.json"
MAX_AGE_HOURS = 24


def status() -> dict:
    result = {
        "schema_version": "heart-session-context-v1",
        "status": "WARN",
        "visual_status_exists": VISUAL_STATUS.is_file(),
        "visual_status_age_hours": None,
        "registry_valid": False,
        "business_context_loaded": False,
        "message": "只使用已核实资料；当前业务真值未知。",
    }
    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        result["registry_valid"] = len(registry.get("workflows", [])) == 7
    except (OSError, ValueError, json.JSONDecodeError):
        pass
    if VISUAL_STATUS.is_file():
        modified = dt.datetime.fromtimestamp(VISUAL_STATUS.stat().st_mtime).astimezone()
        age = (dt.datetime.now().astimezone() - modified).total_seconds() / 3600
        result["visual_status_age_hours"] = round(age, 2)
        if age <= MAX_AGE_HOURS and result["registry_valid"]:
            result["status"] = "OK"
            result["message"] = (
                "七 Agent 状态元数据新鲜；它只用于路由/新鲜度，不代表交易、资产或心理业务真值。"
            )
    return result


if __name__ == "__main__":
    payload = status()
    print(f"[Heart 状态] {json.dumps(payload, ensure_ascii=False)}", flush=True)
    raise SystemExit(0)
