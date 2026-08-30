from iam_automation.policies import build_role_assignment, normalize_scopes


def test_build_role_assignment_defaults_to_service_principal():
    assignment = build_role_assignment(
        principal_id="principal-123",
        role_definition_id="role-reader",
    )

    assert assignment == {
        "principalId": "principal-123",
        "roleDefinitionId": "role-reader",
        "principalType": "ServicePrincipal",
    }


def test_build_role_assignment_supports_custom_principal_type():
    assignment = build_role_assignment(
        principal_id="group-123",
        role_definition_id="role-reader",
        principal_type="Group",
    )

    assert assignment["principalType"] == "Group"


def test_normalize_scopes_removes_duplicates_and_trailing_slashes():
    scopes = normalize_scopes(
        [
            "/subscriptions/ABC/resourceGroups/Prod/",
            "/subscriptions/abc/resourceGroups/prod",
            "",
        ]
    )

    assert scopes == ["/subscriptions/abc/resourcegroups/prod"]
