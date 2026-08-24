<div align="center">

# Azure IAM / RBAC Automation

### Cloud Security · Least Privilege · Identity Automation · Policy Validation

**A Python-based security automation project for validating Azure RBAC access before it reaches production.**

<p>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/Azure-RBAC-0078D4?style=for-the-badge&logo=microsoftazure" alt="Azure" />
  <img src="https://img.shields.io/badge/Entra_ID-Identity-5E5E5E?style=for-the-badge&logo=microsoft" alt="Microsoft Entra ID" />
  <img src="https://img.shields.io/badge/pytest-Tested-0A9EDC?style=for-the-badge&logo=pytest" alt="pytest" />
  <img src="https://img.shields.io/badge/GitHub_Actions-CI-2088FF?style=for-the-badge&logo=githubactions" alt="GitHub Actions" />
</p>

</div>

---

## 🎯 Why this project exists

IAM mistakes are easy to make and difficult to notice after deployment. This project treats access changes as **configuration that should be validated before mutation**.

The workflow is intentionally conservative:

```text
RBAC configuration
        ↓
Policy validation
        ↓
Security findings
        ↓
Audit report
        ↓
Human review
        ↓
Approved change
```

The current implementation focuses on **detection and auditability**, not blind automated changes to Azure.

---

## 🔐 Security capabilities

- Detects broad roles such as `Owner`, `Contributor` and `User Access Administrator`
- Flags subscription-wide RBAC scope
- Detects missing principal identifiers
- Detects missing RBAC scope
- Encourages resource-group or resource-level permissions
- Separates policy validation from Azure SDK operations
- Supports dry-run style auditing without changing Azure
- Produces reviewable JSON findings
- Uses `DefaultAzureCredential` rather than embedding credentials
- Tests security policy logic without requiring a live Azure subscription

---

## 🏗️ Architecture

```text
                    YAML Configuration
                           │
                           ▼
                  ┌─────────────────┐
                  │ Policy Validator │
                  └────────┬────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
          Security Findings      Azure Client
                 │                   │
                 │             Azure SDK
                 │                   │
                 └─────────┬─────────┘
                           ▼
                    JSON Audit Report
```

### Design principle

The Azure SDK is isolated behind a client layer so that the security rules can be tested independently from cloud-side mutation. This makes the policy engine easier to review and safer to evolve.

---

## 🧩 Repository structure

```text
iam-automation/
│
├── iam_automation/
│   ├── client.py       # Azure SDK boundary
│   ├── manager.py      # IAM workflow orchestration
│   ├── policies.py     # Policy definitions
│   ├── validator.py    # Security validation logic
│   └── report.py       # Audit report generation
│
├── config/
│   └── example_assignments.yaml
│
├── scripts/
│   └── audit_assignments.py
│
├── tests/
│   └── test_validator.py
│
├── .github/workflows/
│   └── ci.yml
│
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## 🧪 Example policy validation

Given an assignment such as:

```yaml
assignments:
  - name: app-reader
    principal_id: "<principal-id>"
    role: Reader
    scope: "/subscriptions/<subscription-id>/resourceGroups/rg-example"
```

the validator asks:

| Check | Security question |
|---|---|
| Role | Is a narrower role sufficient? |
| Scope | Can this be resource or resource-group scoped? |
| Principal | Is the identity explicitly identified? |
| Privilege | Is the requested access broader than required? |
| Auditability | Can the decision be reviewed before mutation? |

Broad roles and subscription-level scope are explicitly surfaced by the validator. fileciteturn38file0L2-L2

---

## 🚀 Run locally

Create an isolated Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the audit:

```bash
python scripts/audit_assignments.py \
  --config config/example_assignments.yaml \
  --output reports/rbac-audit.json
```

The audit validates local configuration and produces findings without requiring an Azure write operation. fileciteturn37file0L2-L2

Run tests:

```bash
pytest -q
```

The test suite covers broad-role detection, subscription-scope detection and clean narrow-scope assignments. fileciteturn39file0L2-L2

---

## ☁️ Azure authentication

The Azure client uses `DefaultAzureCredential`, allowing standard Azure authentication mechanisms such as Azure CLI locally and managed/workload identity in Azure-hosted environments. fileciteturn37file0L2-L2

**Never commit:**

- Client secrets
- Access tokens
- Certificates
- Subscription credentials
- Sensitive generated reports

---

## 🔄 CI/CD

GitHub Actions currently performs:

```text
Checkout
   ↓
Python 3.12
   ↓
Dependency installation
   ↓
Compile check
   ↓
pytest
```

The CI workflow intentionally runs without Azure credentials because the security policy tests operate on local data. fileciteturn40file0L2-L2

---

## 🧠 Engineering decisions

### 1. Validate before mutate

Security policy should be evaluated before an access change is allowed to reach the cloud.

### 2. Prefer narrow scope

Resource or resource-group permissions are preferred over subscription-wide access wherever the workload allows it.

### 3. Keep cloud access isolated

The Azure SDK boundary is separated from validation logic, making the core policy engine independently testable.

### 4. Use identity-based authentication

`DefaultAzureCredential` supports modern Azure authentication patterns and avoids hard-coded credentials.

### 5. Make findings reviewable

The audit produces structured findings that can be consumed by engineers, CI systems or future policy gates.

---

## 📊 Security model

```text
                    Requested Access
                           │
                           ▼
                  ┌─────────────────┐
                  │ Identity Check  │
                  └────────┬────────┘
                           ▼
                  ┌─────────────────┐
                  │ Role Analysis   │
                  └────────┬────────┘
                           ▼
                  ┌─────────────────┐
                  │ Scope Analysis  │
                  └────────┬────────┘
                           ▼
                  ┌─────────────────┐
                  │ Policy Findings │
                  └────────┬────────┘
                           ▼
                    Audit / Review
```

The current policy engine is deliberately small and explicit. Future policy packs can extend it to cover additional IAM risks.

---

## 🔮 Roadmap

- [ ] Add severity levels: Critical / High / Medium / Low
- [ ] Add policy-as-code rules for additional RBAC patterns
- [ ] Add JSON schema validation for configuration
- [ ] Add SARIF output for GitHub code scanning integration
- [ ] Add CI policy gate for high-severity findings
- [ ] Add unused-role / stale-assignment detection
- [ ] Add Azure Resource Graph integration
- [ ] Add automated remediation behind explicit approval
- [ ] Add support for selected Azure built-in role recommendations

---

## 🔗 Portfolio connection

This project represents the **Cloud Security and Identity Automation** layer of my broader Cloud / DevOps / SRE portfolio:

```text
Terraform Cloud Infrastructure
             ↓
      IAM / RBAC Automation
             ↓
      Kubernetes Platform
             ↓
        GitOps / CI/CD
             ↓
      Observability / SRE
```

---

## 👨‍💻 Author

**Vasid Shaik**  
Cloud / DevOps / SRE Engineer

[GitHub](https://github.com/ShaikVasid)
