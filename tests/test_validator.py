from iam_automation.validator import validate_assignment, validate_assignments


def test_flags_broad_subscription_assignment():
    findings = validate_assignment(
        {
            "principal_id": "principal",
            "role": "Contributor",
            "scope": "/subscriptions/12345678-1234-1234-1234-123456789012",
        }
    )

    assert "Broad role detected: Contributor" in findings
    assert any("Subscription-wide scope" in item for item in findings)


def test_accepts_narrow_reader_assignment():
    findings = validate_assignment(
        {
            "principal_id": "principal",
            "role": "Reader",
            "scope": "/subscriptions/123/resourceGroups/example",
        }
    )

    assert findings == []


def test_returns_only_assignments_with_findings():
    assignments = [
        {
            "principal_id": "principal",
            "role": "Reader",
            "scope": "/subscriptions/123/resourceGroups/example",
        },
        {
            "principal_id": "principal",
            "role": "Owner",
            "scope": "/subscriptions/123",
        },
    ]

    findings = validate_assignments(assignments)

    assert "0" not in findings
    assert "1" in findings
