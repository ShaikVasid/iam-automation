"""AWS IAM client wrapper."""

from __future__ import annotations

import boto3


class IAMClient:
    """Thin wrapper around boto3 IAM APIs."""

    def __init__(self, client=None):
        self.client = client or boto3.client("iam")

    def list_roles(self) -> list[dict]:
        roles: list[dict] = []
        paginator = self.client.get_paginator("list_roles")
        for page in paginator.paginate():
            roles.extend(page.get("Roles", []))
        return roles

    def get_role(self, role_name: str) -> dict:
        return self.client.get_role(RoleName=role_name)["Role"]
