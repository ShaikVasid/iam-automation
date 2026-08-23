# Azure IAM / RBAC Automation

A small Python project for automating and checking Azure RBAC assignments.

I built this around a common cloud-operations problem: access changes tend to become messy when they are done manually. The idea here is to keep the requested assignments in configuration, validate them before making changes, and have an audit output that can be reviewed later.

## What it covers

- Azure RBAC role assignments
- Microsoft Entra ID / service-principal concepts
- Managed identity patterns
- Least-privilege checks
- Scope checks for subscriptions, resource groups, and resources
- Dry-run support
- JSON audit output
- Unit tests without making live Azure changes

This is a portfolio implementation. It is meant to show the way I approach access automation, not to suggest that it is a complete enterprise IAM platform.

## How it works

```text
role-assignment config
        |
        v
   validation
        |
   +----+----+
   |         |
 dry-run   Azure API
   |         |
   +----+----+
        |
     audit report
```

## Repository layout

```text
.
├── iam_automation/
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
├── .github/workflows/ci.yml
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Example

The example configuration describes an Azure principal, role, and scope. Before an assignment is created, the validator looks for things I would normally question during an access review.

For example:

- Why does this workload need `Owner`?
- Can `Contributor` be replaced with a narrower role?
- Does the assignment really need subscription scope?
- Is the principal identified correctly?

Run the validation locally with:

```bash
python -m iam_automation.validator config/example_assignments.yaml
```

For an audit run without changing Azure:

```bash
python scripts/audit_assignments.py --config config/example_assignments.yaml --dry-run
```

## Authentication

The Azure client uses `DefaultAzureCredential`. That keeps credentials out of the code and lets the same code work with Azure CLI authentication locally and managed/workload identity in an Azure environment.

Never commit client secrets, certificates, tokens, or subscription credentials.

## Why I built it this way

I kept the Azure API calls behind a small client layer so the validation logic does not need a live Azure subscription to be tested. The policy and validation code can therefore be exercised with normal unit tests.

The next logical step would be to add Microsoft Entra access-review integration and Azure Resource Graph discovery, but I have intentionally kept this version focused on RBAC automation.

## Technologies

**Python · Azure SDK · Microsoft Entra ID · Azure RBAC · Managed Identity · YAML · pytest · GitHub Actions**
