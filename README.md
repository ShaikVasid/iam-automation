# IAM Automation

Python-based AWS IAM automation project demonstrating identity lifecycle automation, least-privilege policy generation, policy validation, and audit reporting.

## What this demonstrates

- AWS IAM automation with Python and boto3
- Create and manage IAM roles
- Generate least-privilege policy documents from declarative configuration
- Detect wildcard permissions and risky policy statements
- Produce audit-friendly JSON reports
- Dry-run mode for safe operational workflows
- Unit testing with mocked AWS APIs
- CI checks with GitHub Actions

> Portfolio implementation. It is designed to demonstrate engineering practices and is not presented as an employer production system.

## Architecture

```text
YAML/JSON configuration
          |
          v
   +--------------+
   | IAM Manager  |
   +------+-------+
          |
    +-----+------+
    |            |
    v            v
Policy       AWS IAM API
Validator         |
    |             v
    +-------> Audit Report
```

## Repository structure

```text
.
├── iam_automation/
│   ├── __init__.py
│   ├── client.py
│   ├── policies.py
│   ├── validator.py
│   ├── manager.py
│   └── report.py
├── config/
│   └── example_roles.yaml
├── tests/
│   ├── test_policies.py
│   └── test_validator.py
├── scripts/
│   └── audit_roles.py
├── .github/workflows/ci.yml
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

## Example workflow

```bash
python -m iam_automation.validator config/example_roles.yaml

python scripts/audit_roles.py --config config/example_roles.yaml --dry-run
```

The default examples are intentionally safe. No credentials are committed and the example audit workflow uses dry-run mode.

## Security controls

The validator flags common IAM risks including:

- `Action: *`
- `Resource: *`
- Allow statements without an explicit resource boundary
- Unexpected IAM actions
- Policies that are broader than the declared service scope

This is a lightweight portfolio validator, not a replacement for AWS IAM Access Analyzer or an enterprise policy-governance platform.

## Engineering principles

### Least privilege

Policies should grant only the actions required by the workload and constrain resources whenever practical.

### Declarative configuration

Role definitions live outside the Python implementation so the automation can be reviewed and version controlled.

### Safe execution

The CLI supports dry-run operation before making AWS changes.

### Testability

AWS API interactions are isolated behind a client layer so business logic can be tested without making live AWS calls.

## Technologies

**Python · boto3 · AWS IAM · JSON · YAML · pytest · GitHub Actions · Cloud Security · DevOps · SRE**
