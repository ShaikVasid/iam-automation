"""Validate Azure RBAC configuration and optionally write an audit report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from iam_automation.report import write_json_report
from iam_automation.validator import validate_assignments


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, help="Path to YAML assignment configuration")
    parser.add_argument(
        "--output",
        default="reports/rbac-audit.json",
        help="Path for the JSON audit report",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    assignments = config.get("assignments", [])
    findings = validate_assignments(assignments)

    report = {
        "assignment_count": len(assignments),
        "finding_count": sum(len(items) for items in findings.values()),
        "findings": findings,
    }

    write_json_report(report, args.output)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
