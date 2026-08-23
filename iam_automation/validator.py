"""Lightweight static checks for common IAM policy risks."""

from __future__ import annotations

from typing import Any


RISKY_ACTIONS = {"*", "iam:*", "sts:*"}


def validate_policy(policy: dict[str, Any]) -> list[str]:
    """Return findings for broad Allow statements."""
    findings: list[str] = []

    for index, statement in enumerate(policy.get("Statement", [])):
        if statement.get("Effect") != "Allow":
            continue

        actions = statement.get("Action", [])
        resources = statement.get("Resource", [])
        if isinstance(actions, str):
            actions = [actions]
        if isinstance(resources, str):
            resources = [resources]

        if any(action in RISKY_ACTIONS for action in actions):
            findings.append(f"statement[{index}]: broad IAM action permission")
        if "*" in resources:
            findings.append(f"statement[{index}]: wildcard resource")
        if not actions:
            findings.append(f"statement[{index}]: missing Action")
        if not resources:
            findings.append(f"statement[{index}]: missing Resource")

    return findings
