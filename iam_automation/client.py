"""Azure Resource Manager client abstraction."""

from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient


class AzureAuthorizationClient:
    """Small wrapper around Azure RBAC APIs.

    DefaultAzureCredential supports local Azure CLI authentication, managed
    identity, workload identity, and other standard Azure credential sources.
    """

    def __init__(self, subscription_id: str):
        self.subscription_id = subscription_id
        credential = DefaultAzureCredential()
        self.client = AuthorizationManagementClient(credential, subscription_id)

    def list_role_assignments(self, scope: str | None = None):
        target_scope = scope or f"/subscriptions/{self.subscription_id}"
        return self.client.role_assignments.list_for_scope(target_scope)

    def create_role_assignment(self, scope: str, assignment_id: str, parameters: dict):
        return self.client.role_assignments.create(scope, assignment_id, parameters)
