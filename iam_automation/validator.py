"""Azure RBAC security validation helpers."""

from __future__ import annotations

from typing import Any

BROAD_ROLES = {"Owner", "Contributor", "User Access Administrator"}


def validate_assignment(assignment: dict[str, Any]) -> list[str]:
    """Return security findings for an Azure RBAC assignment."""
    findings: list[str] = []
    role = assignment.get("role", "")
    scope = assignment.get("scope", "")

    if role in BROAD_ROLES:
        findings.append(f"Broad role detected: {role}")

    if scope.lower().startswith("/subscriptions/") and scope.lower().count("/") == 2:
        findings.append("Subscription-wide scope detected; prefer resource-group or resource scope")

    if not assignment.get("principal_id"):
        findings.append("Missing principal_id")

    if not scope:
        findings.append("Missing RBAC scope")

    return findings


def validate_assignments(assignments: list[dict[str, Any]]) -> dict[str, list[str]]:
    return {
        str(index): validate_assignment(assignment)
        for index, assignment in enumerate(assignments)
        if validate_assignment(assignment)
    }
