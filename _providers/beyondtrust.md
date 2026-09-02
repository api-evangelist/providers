---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Beyondtrust Agentic Access
  operation_count: 14
  slug: beyondtrust-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 6
apis:
- description: API authentication and authorization
  name: BeyondTrust Authentication API
  slug: beyondtrust-authentication-api
- description: Manage privileged account credentials and passwords
  name: BeyondTrust Credentials API
  slug: beyondtrust-credentials-api
- description: Manage privileged accounts and their configurations
  name: BeyondTrust Managed Accounts API
  slug: beyondtrust-managed-accounts-api
- description: Manage systems registered in Password Safe
  name: BeyondTrust Managed Systems API
  slug: beyondtrust-managed-systems-api
- description: Submit and manage access requests for privileged accounts
  name: BeyondTrust Requests API
  slug: beyondtrust-requests-api
- description: Manage secrets and secret store entries
  name: BeyondTrust Secrets API
  slug: beyondtrust-secrets-api
artifact_total: 77
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BeyondTrust Password Safe Authentication API
  slug: open-beyondtrust-authentication-api
- collection_type: open
  name: BeyondTrust Password Safe Authentication Credentials API
  slug: open-beyondtrust-credentials-api
- collection_type: open
  name: BeyondTrust Password Safe Authentication Managed Accounts API
  slug: open-beyondtrust-managed-accounts-api
- collection_type: open
  name: BeyondTrust Password Safe Authentication Managed Systems API
  slug: open-beyondtrust-managed-systems-api
- collection_type: open
  name: BeyondTrust Password Safe Authentication Requests API
  slug: open-beyondtrust-requests-api
- collection_type: open
  name: BeyondTrust Password Safe Authentication Secrets API
  slug: open-beyondtrust-secrets-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beyondtrust-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/beyondtrust-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beyondtrust-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beyondtrust-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beyondtrust
- group: start
  title: ''
  type: Portal
  url: https://docs.beyondtrust.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beyondtrust.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BeyondTrust
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/rules/beyondtrust-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/vocabulary/beyondtrust-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.beyondtrust.com/llms.txt
created: '2025-02-17'
description: BeyondTrust is a cybersecurity company specializing in privileged access management (PAM) and vulnerability management solutions. Their products help organizations prevent data breaches, malware attacks, and insider threats by identifying and controlling the access of privileged users, accounts, and credentials across the enterprise.
examples:
- key_count: 5
  name: Beyondtrust Create Request Body Example
  slug: beyondtrust-create-request-body-example
- key_count: 6
  name: Beyondtrust Create Secret Request Example
  slug: beyondtrust-create-secret-request-example
- key_count: 2
  name: Beyondtrust Credential Response Example
  slug: beyondtrust-credential-response-example
- key_count: 8
  name: Beyondtrust Managed Account Example
  slug: beyondtrust-managed-account-example
- key_count: 6
  name: Beyondtrust Managed System Example
  slug: beyondtrust-managed-system-example
- key_count: 11
  name: Beyondtrust Request Example
  slug: beyondtrust-request-example
- key_count: 7
  name: Beyondtrust Secret Example
  slug: beyondtrust-secret-example
- key_count: 7
  name: Beyondtrust Secret With Value Example
  slug: beyondtrust-secret-with-value-example
- key_count: 4
  name: Beyondtrust Session Response Example
  slug: beyondtrust-session-response-example
- key_count: 2
  name: Beyondtrust Sign App In Request Example
  slug: beyondtrust-sign-app-in-request-example
- key_count: 2
  name: Beyondtrust Update Request Body Example
  slug: beyondtrust-update-request-body-example
features:
- description: Automatically discover, manage, and rotate passwords for privileged accounts across systems.
  name: Privileged Password Management
- description: Grant time-limited, approval-based access to privileged accounts minimizing standing privileges.
  name: Just-In-Time Privileged Access
- description: Store, manage, and retrieve application secrets, API keys, and credentials securely.
  name: Secrets Safe
- description: Record, monitor, and control privileged remote sessions for audit and compliance.
  name: Session Management
- description: Remove admin rights from endpoints while allowing approved applications to run.
  name: Endpoint Privilege Management
- description: Provide secure remote access to privileged systems without VPN or exposed credentials.
  name: Privileged Remote Access
- description: Identify and prioritize vulnerabilities across the attack surface.
  name: Vulnerability Management
- description: Extend Active Directory authentication and group policies to Unix and Linux systems.
  name: AD Bridge
finops:
- name: Beyondtrust Finops
  service_category: API
  slug: beyondtrust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beyondtrust.png
integrations:
- description: Integrate access requests with ServiceNow ITSM workflows for approval management.
  name: ServiceNow
- description: Sync users, groups, and managed accounts from Active Directory.
  name: Active Directory
- description: Manage privileged access to AWS IAM roles and EC2 instances.
  name: AWS
- description: Integrate with Azure Active Directory and manage Azure privileged identities.
  name: Azure
- description: Bridge BeyondTrust and HashiCorp Vault for secrets management.
  name: HashiCorp Vault
- description: Forward audit logs and session recordings to Splunk for SIEM analysis.
  name: Splunk
- description: Manage BeyondTrust Password Safe resources as infrastructure as code.
  name: Terraform
json_schemas:
- name: CreateRequestBody
  property_count: 5
  slug: beyondtrust-create-request-body
- name: CreateSecretRequest
  property_count: 6
  slug: beyondtrust-create-secret-request
- name: CredentialResponse
  property_count: 2
  slug: beyondtrust-credential-response
- name: ManagedAccount
  property_count: 8
  slug: beyondtrust-managed-account
- name: ManagedSystem
  property_count: 6
  slug: beyondtrust-managed-system
- name: Request
  property_count: 11
  slug: beyondtrust-request
- name: Secret
  property_count: 7
  slug: beyondtrust-secret
- name: SecretWithValue
  property_count: 7
  slug: beyondtrust-secret-with-value
- name: SessionResponse
  property_count: 4
  slug: beyondtrust-session-response
- name: SignAppInRequest
  property_count: 2
  slug: beyondtrust-sign-app-in-request
- name: UpdateRequestBody
  property_count: 2
  slug: beyondtrust-update-request-body
json_structures:
- name: Beyondtrust Create Request Body Structure
  property_count: 5
  slug: beyondtrust-create-request-body-structure
- name: Beyondtrust Create Secret Request Structure
  property_count: 6
  slug: beyondtrust-create-secret-request-structure
- name: Beyondtrust Credential Response Structure
  property_count: 2
  slug: beyondtrust-credential-response-structure
- name: Beyondtrust Managed Account Structure
  property_count: 8
  slug: beyondtrust-managed-account-structure
- name: Beyondtrust Managed System Structure
  property_count: 6
  slug: beyondtrust-managed-system-structure
- name: Beyondtrust Request Structure
  property_count: 11
  slug: beyondtrust-request-structure
- name: Beyondtrust Secret Structure
  property_count: 7
  slug: beyondtrust-secret-structure
- name: Beyondtrust Secret With Value Structure
  property_count: 7
  slug: beyondtrust-secret-with-value-structure
- name: Beyondtrust Session Response Structure
  property_count: 4
  slug: beyondtrust-session-response-structure
- name: Beyondtrust Sign App In Request Structure
  property_count: 2
  slug: beyondtrust-sign-app-in-request-structure
- name: Beyondtrust Update Request Body Structure
  property_count: 2
  slug: beyondtrust-update-request-body-structure
jsonld:
- class_count: 13
  name: Beyondtrust Context
  property_count: 37
  slug: beyondtrust-context
layout: provider
modified: '2026-05-19'
name: BeyondTrust
nav: Providers
network: true
overview: 'BeyondTrust publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Credentials API, Managed Accounts API, and 3 more. Tagged areas include Access, Access Management, Compliance, Credentials, and Privileged Access.


  The BeyondTrust catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BeyondTrust''s developer surface includes authentication, developer portal, getting-started guide, and 8 more developer resources.'
plans:
- name: Beyondtrust Plans Pricing
  plan_count: 3
  slug: beyondtrust-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Beyondtrust Rate Limits
  slug: beyondtrust-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BeyondTrust API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: beyondtrust-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: BeyondTrust API Rules
  rule_count: 29
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 14
  slug: beyondtrust-spectral-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 23.9
    developer_ergonomics: 42.9
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beyondtrust/refs/heads/main/screenshots/beyondtrust-2026-06-20T173216.png
security:
- kind: authentication
  name: Beyondtrust Authentication
  slug: beyondtrust-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Beyondtrust Domain Security
  slug: beyondtrust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Beyondtrust Vulnerability Disclosure
  slug: beyondtrust-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: beyondtrust
tags:
- Access
- Access Management
- Compliance
- Credentials
- Privileged Access
- Security
- Secrets
- Zero Trust
use_cases:
- description: Eliminate persistent privileged access by granting just-in-time credentials on demand.
  name: Zero Standing Privileges
- description: Retrieve credentials and secrets programmatically in CI/CD pipelines without hardcoded credentials.
  name: DevOps Secrets Management
- description: Automatically discover and on-board all privileged accounts across hybrid environments.
  name: Privileged Account Discovery
- description: Generate audit trails for all privileged access to meet SOX, PCI-DSS, and HIPAA requirements.
  name: Compliance Reporting
- description: Prevent lateral movement by removing local admin rights and controlling privileged access.
  name: Ransomware Prevention
- description: Grant temporary, monitored access to vendors and contractors without sharing credentials.
  name: Third-Party Vendor Access
website: https://docs.beyondtrust.com/
---
