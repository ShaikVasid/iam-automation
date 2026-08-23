# Azure IAM / RBAC Automation

A Python project for automating and validating **Azure RBAC assignments** with a focus on least privilege, scope control, auditability, and testability.

The project treats access changes as configuration: validate the requested assignment first, run an audit without changing Azure, and keep the Azure SDK behind a small client layer.

## What it covers

- Azure RBAC role assignments
- Microsoft Entra ID and service-principal concepts
- Managed identity patterns
- Least-privilege validation
- Subscription, resource-group, and resource scope checks
- Dry-run style audit workflow
- JSON audit reports
- Unit tests without requiring a live Azure change
- GitHub Actions CI

## Architecture

```text
YAML configuration
        ↓
Validation / policy checks
        ↓
   +----+----+
   |         |
 Audit     Azure SDK
   |         |
   +----+----+
        ↓
   JSON report
```

## Repository layout

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
│   └── test_validator.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Example configuration

```yaml
assignments:
  - name: app-reader
    principal_id: "<principal-id>"
    role: Reader
    scope: "/subscriptions/<subscription-id>/resourceGroups/rg-example"
```

Before making an access change, the validator checks questions such as:

- Does the workload really need `Owner` or `Contributor`?
- Can a narrower built-in role be used?
- Does the assignment need subscription scope?
- Is the principal identified correctly?
- Is the RBAC scope present and valid?

## Run an audit

Install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the local configuration audit:

```bash
python scripts/audit_assignments.py \
  --config config/example_assignments.yaml \
  --output reports/rbac-audit.json
```

The command does **not** change Azure. It validates the configuration and writes a JSON report.

## Azure authentication

The Azure client uses `DefaultAzureCredential`. This supports standard Azure authentication mechanisms such as Azure CLI locally and managed or workload identity in Azure-hosted environments.

Never commit client secrets, certificates, tokens, subscription credentials, or generated reports containing sensitive information.

## Code organization

The Azure SDK interaction is isolated in `client.py`. Policy construction lives in `policies.py`, validation lives in `validator.py`, and reporting is handled separately. This keeps the business logic testable without requiring a live Azure subscription.

## CI

GitHub Actions runs:

```text
Checkout
   ↓
Python setup
   ↓
Dependency installation
   ↓
Python compile check
   ↓
pytest
```

The CI workflow does not require Azure credentials because the unit tests operate on local data.

## Security principles

- Least privilege by default
- Prefer resource or resource-group scope over subscription-wide permissions
- Avoid broad roles unless there is a documented requirement
- Use managed/workload identity instead of static credentials
- Separate validation from mutation
- Keep audit output reviewable
- Test security policy logic before production use

## Technologies

**Python · Azure SDK · Microsoft Entra ID · Azure RBAC · Managed Identity · YAML · pytest · GitHub Actions**

## Portfolio connection

This repository represents the **identity and security automation layer** of my Cloud / DevOps portfolio:

```text
Terraform Azure Infrastructure
             ↓
        Azure RBAC
             ↓
       Azure AKS Platform
             ↓
        GitOps / Argo CD
             ↓
      SRE / Observability
```

## Author

**Vasid Shaik**  
Cloud / DevOps / SRE Engineer
