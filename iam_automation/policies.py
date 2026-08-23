"""Azure RBAC role assignment helpers."""

from __future__ import annotations

from typing import Iterable


def build_role_assignment(
    principal_id: str,
    role_definition_id: str,
    scope: str,
) -> dict:
    """Build an Azure RBAC role-assignment payload."""
    return {
        "principalId": principal_id,
        "roleDefinitionId": role_definition_id,
        "principalType": "ServicePrincipal",
        "scope": scope,
    }


def normalize_scopes(scopes: Iterable[str]) -> list[str]:
    """Return normalized, unique Azure resource scopes."""
    return sorted({scope.rstrip("/").lower() for scope in scopes})
