"""Azure RBAC role-assignment lifecycle operations."""

from __future__ import annotations

from typing import Any

from .client import AzureAuthorizationClient
from .policies import build_role_assignment


class RoleManager:
    """Manage Azure RBAC assignments through a small testable abstraction."""

    def __init__(self, client: AzureAuthorizationClient):
        self.client = client

    def list_assignments(self, scope: str | None = None) -> list[dict[str, Any]]:
        """Return a normalized list of role assignments."""
        assignments = self.client.list_role_assignments(scope)
        return [
            {
                "id": assignment.id,
                "principal_id": assignment.principal_id,
                "role_definition_id": assignment.role_definition_id,
                "scope": assignment.scope,
            }
            for assignment in assignments
        ]

    def create_assignment(
        self,
        principal_id: str,
        role_definition_id: str,
        scope: str,
        assignment_id: str,
    ) -> Any:
        """Create an Azure RBAC role assignment."""
        parameters = build_role_assignment(
            principal_id=principal_id,
            role_definition_id=role_definition_id,
        )
        return self.client.create_role_assignment(scope, assignment_id, parameters)
