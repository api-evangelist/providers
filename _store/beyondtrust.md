---
aid: beyondtrust
url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/apis.yml
apis:
  - aid: beyondtrust:beyondtrust-password-safe-api
    name: BeyondTrust Password Safe API
    tags:
      - Privileged Access Management
      - Secrets Management
      - Security
      - Zero Trust
      - Credentials
    humanURL: https://docs.beyondtrust.com/
    baseURL: https://{host}/BeyondTrust/api/public/v3
    properties:
      - url: https://docs.beyondtrust.com/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/openapi/beyondtrust-password-safe-api.yaml
        type: OpenAPI
    description: The BeyondTrust Password Safe API provides programmatic access to privileged credential management, secrets management, session management, and access request workflows. It enables organizations to implement just-in-time privileged access and integrate credential retrieval into automation pipelines and DevOps workflows.
name: BeyondTrust
tags:
  - Access
  - Access Management
  - Compliance
  - Credentials
  - Privileged Access
  - Security
  - Secrets
  - Zero Trust
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-19'
position: Consuming
description: BeyondTrust is a cybersecurity company specializing in privileged access management (PAM) and vulnerability management solutions. Their products help organizations prevent data breaches, malware attacks, and insider threats by identifying and controlling the access of privileged users, accounts, and credentials across the enterprise.
common:
  - type: Portal
    url: https://docs.beyondtrust.com/
  - type: GettingStarted
    url: https://docs.beyondtrust.com/
  - type: GitHubOrganization
    url: https://github.com/BeyondTrust
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/rules/beyondtrust-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/vocabulary/beyondtrust-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/capabilities/privileged-access-management.yaml
  - type: Features
    data:
      - name: Privileged Password Management
        description: Automatically discover, manage, and rotate passwords for privileged accounts across systems.
      - name: Just-In-Time Privileged Access
        description: Grant time-limited, approval-based access to privileged accounts minimizing standing privileges.
      - name: Secrets Safe
        description: Store, manage, and retrieve application secrets, API keys, and credentials securely.
      - name: Session Management
        description: Record, monitor, and control privileged remote sessions for audit and compliance.
      - name: Endpoint Privilege Management
        description: Remove admin rights from endpoints while allowing approved applications to run.
      - name: Privileged Remote Access
        description: Provide secure remote access to privileged systems without VPN or exposed credentials.
      - name: Vulnerability Management
        description: Identify and prioritize vulnerabilities across the attack surface.
      - name: AD Bridge
        description: Extend Active Directory authentication and group policies to Unix and Linux systems.
  - type: UseCases
    data:
      - name: Zero Standing Privileges
        description: Eliminate persistent privileged access by granting just-in-time credentials on demand.
      - name: DevOps Secrets Management
        description: Retrieve credentials and secrets programmatically in CI/CD pipelines without hardcoded credentials.
      - name: Privileged Account Discovery
        description: Automatically discover and on-board all privileged accounts across hybrid environments.
      - name: Compliance Reporting
        description: Generate audit trails for all privileged access to meet SOX, PCI-DSS, and HIPAA requirements.
      - name: Ransomware Prevention
        description: Prevent lateral movement by removing local admin rights and controlling privileged access.
      - name: Third-Party Vendor Access
        description: Grant temporary, monitored access to vendors and contractors without sharing credentials.
  - type: Integrations
    data:
      - name: ServiceNow
        description: Integrate access requests with ServiceNow ITSM workflows for approval management.
      - name: Active Directory
        description: Sync users, groups, and managed accounts from Active Directory.
      - name: AWS
        description: Manage privileged access to AWS IAM roles and EC2 instances.
      - name: Azure
        description: Integrate with Azure Active Directory and manage Azure privileged identities.
      - name: HashiCorp Vault
        description: Bridge BeyondTrust and HashiCorp Vault for secrets management.
      - name: Splunk
        description: Forward audit logs and session recordings to Splunk for SIEM analysis.
      - name: Terraform
        description: Manage BeyondTrust Password Safe resources as infrastructure as code.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
