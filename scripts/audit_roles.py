#!/usr/bin/env python3
"""Audit AWS IAM roles. Use --dry-run to demonstrate the workflow without AWS changes."""

from __future__ import annotations

import argparse

from iam_automation.manager import RoleManager
from iam_automation.report import write_json_report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="run inventory/report workflow without mutation")
    parser.add_argument("--output", default="reports/iam-roles.json")
    args = parser.parse_args()

    if args.dry_run:
        print("DRY RUN: IAM audit only; no resources will be modified.")

    manager = RoleManager()
    roles = manager.audit()
    write_json_report(roles, args.output)
    print(f"Audited {len(roles)} IAM roles -> {args.output}")


if __name__ == "__main__":
    main()
