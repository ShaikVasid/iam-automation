"""Azure RBAC role-assignment policy helpers."""

from __future__ import annotations

from typing import Iterable


def build_role_assignment(
    principal_id: str,
    role_definition_id: str,
    principal_type: str = "ServicePrincipal",
) -> dict[str, str]:
    """Build parameters accepted by the Azure RBAC API."""
    return {
        "principalId": principal_id,
        "roleDefinitionId": role_definition_id,
        "principalType": principal_type,
    }


def normalize_scopes(scopes: Iterable[str]) -> list[str]:
    """Return normalized, unique Azure resource scopes."""
    return sorted({scope.rstrip("/").lower() for scope in scopes if scope})
