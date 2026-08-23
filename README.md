# Azure IAM / RBAC Automation

Python-based Azure identity and access automation project demonstrating Microsoft Entra ID, Azure RBAC, managed identities, least-privilege role assignments, policy validation, and audit reporting.

## What this demonstrates

- Azure identity and access automation with Python
- Microsoft Entra ID application and service-principal concepts
- Azure RBAC role-assignment automation
- Managed identity patterns for workloads
- Declarative role-assignment configuration
- Detection of overly broad `Owner` / `Contributor` assignments
- Scope validation for subscription, resource-group, and resource scopes
- Audit-friendly JSON reports
- Dry-run operation for safe changes
- Unit testing without live Azure changes
- CI checks with GitHub Actions

> Portfolio implementation based on Azure patterns. It is not presented as an employer production system.

## Architecture

```text
YAML configuration
       |
       v
+-------------------+
| IAM/RBAC Manager  |
+---------+---------+
          |
    +-----+------+
    |            |
    v            v
Validator    Azure SDK
    |            |
    +------> RBAC assignments
                 |
                 v
            Audit report
```

## Repository structure

```text
.
├── iam_automation/
│   ├── __init__.py
│   ├── client.py
│   ├── manager.py
│   ├── policies.py
│   ├── validator.py
│   └── report.py
├── config/
│   └── example_assignments.yaml
├── scripts/
│   └── audit_assignments.py
├── tests/
│   ├── test_policies.py
│   └── test_validator.py
├── .github/workflows/ci.yml
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

## Example workflow

```bash
python -m iam_automation.validator config/example_assignments.yaml
python scripts/audit_assignments.py --config config/example_assignments.yaml --dry-run
```

The examples are intentionally safe. No Azure credentials, client secrets, or tokens are committed.

## Security controls

The validator flags common Azure RBAC risks including:

- `Owner` assignments where a narrower role should be used
- `Contributor` assignments where a service-specific role is sufficient
- Subscription-wide assignments when resource-group or resource scope is possible
- Missing or overly broad scopes
- Unexpected role definitions

This is a lightweight portfolio validator, not a replacement for Microsoft Entra governance, Azure Policy, or enterprise access-review tooling.

## Engineering principles

### Least privilege

Prefer the narrowest built-in Azure role and smallest practical scope for a workload.

### Workload identity

Prefer managed identities and federated identity patterns over long-lived client secrets.

### Declarative configuration

Role assignments are defined outside the implementation so access changes can be reviewed and version controlled.

### Safe execution

The CLI supports dry-run operation before making Azure changes.

### Testability

Azure API interactions are isolated behind a client layer so policy and validation logic can be tested without live Azure calls.

## Technologies

**Python · Azure SDK · Microsoft Entra ID · Azure RBAC · Managed Identity · Azure Resource Manager · YAML · pytest · GitHub Actions · Cloud Security · DevOps · SRE**
