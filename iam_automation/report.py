"""Audit report helpers."""

from __future__ import annotations

import json
from pathlib import Path


def write_json_report(data: object, output: str | Path) -> None:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, default=str) + "\n", encoding="utf-8")
