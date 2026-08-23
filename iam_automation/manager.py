"""IAM role lifecycle operations with dry-run support."""

from __future__ import annotations

import json

from .client import IAMClient


class RoleManager:
    def __init__(self, client: IAMClient | None = None):
        self.iam = client or IAMClient()

    def audit(self) -> list[dict]:
        """Return a normalized inventory of IAM roles."""
        return [
            {
                "role_name": role["RoleName"],
                "arn": role["Arn"],
                "path": role.get("Path", "/"),
            }
            for role in self.iam.list_roles()
        ]

    @staticmethod
    def render_audit(roles: list[dict]) -> str:
        return json.dumps(roles, indent=2, default=str)
