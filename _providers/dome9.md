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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Dome9 Agentic Access
  operation_count: 17
  slug: dome9-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 7
apis:
- description: Main API for managing cloud accounts, security policies, compliance policies, and security groups across multiple cloud platforms.
  name: Dome9 API
  slug: dome9-api
- description: The AWSAccounts API from Dome9 — 2 operation(s) for awsaccounts.
  name: Dome9 AWSAccounts API
  slug: dome9-awsaccounts-api
- description: The AzureAccounts API from Dome9 — 2 operation(s) for azureaccounts.
  name: Dome9 AzureAccounts API
  slug: dome9-azureaccounts-api
- description: The Compliance API from Dome9 — 1 operation(s) for compliance.
  name: Dome9 Compliance API
  slug: dome9-compliance-api
- description: The GoogleAccounts API from Dome9 — 1 operation(s) for googleaccounts.
  name: Dome9 GoogleAccounts API
  slug: dome9-googleaccounts-api
- description: The Roles API from Dome9 — 2 operation(s) for roles.
  name: Dome9 Roles API
  slug: dome9-roles-api
- description: The Users API from Dome9 — 1 operation(s) for users.
  name: Dome9 Users API
  slug: dome9-users-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dome9 / CloudGuard AWSAccounts API
  slug: open-dome9-awsaccounts-api
- collection_type: open
  name: Dome9 / CloudGuard AWSAccounts AzureAccounts API
  slug: open-dome9-azureaccounts-api
- collection_type: open
  name: Dome9 / CloudGuard AWSAccounts Compliance API
  slug: open-dome9-compliance-api
- collection_type: open
  name: Dome9 / CloudGuard AWSAccounts GoogleAccounts API
  slug: open-dome9-googleaccounts-api
- collection_type: open
  name: Dome9 / CloudGuard AWSAccounts Roles API
  slug: open-dome9-roles-api
- collection_type: open
  name: Dome9 / CloudGuard AWSAccounts Users API
  slug: open-dome9-users-api
- collection_type: open
  name: Dome9 / CloudGuard API
  slug: open-dome9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dome9-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dome9-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dome9-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dome9-security
- group: company
  title: ''
  type: Website
  url: https://www.checkpoint.com/cloudguard/
- group: company
  title: ''
  type: Blog
  url: https://blog.checkpoint.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dome9
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.checkpoint.com/about-us/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.checkpoint.com/about-us/privacy-policy/
created: '2024-01-01'
description: Dome9 (now Check Point CloudGuard) provides cloud security and compliance solutions with APIs for managing cloud infrastructure security posture, compliance policies, and threat protection across AWS, Azure, and Google Cloud Platform.
finops:
- name: Dome9 Finops
  service_category: API
  slug: dome9-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dome9.png
layout: provider
modified: '2026-04-28'
name: Dome9
nav: Providers
network: true
overview: 'Dome9 publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AWSAccounts API, AzureAccounts API, and 5 more. Tagged areas include Cloud Security, Compliance, Infrastructure Security, Multi-Cloud, and Security Posture Management.


  Dome9''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Dome9 Plans Pricing
  plan_count: 3
  slug: dome9-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Dome9 Rate Limits
  slug: dome9-rate-limits
score:
  band: thin
  composite: 28.3
  delta: -4.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dome9/refs/heads/main/screenshots/dome9-2026-07-25T212245.png
security:
- kind: authentication
  name: Dome9 Authentication
  slug: dome9-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dome9 Domain Security
  slug: dome9-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dome9
tags:
- Cloud Security
- Compliance
- Infrastructure Security
- Multi-Cloud
- Security Posture Management
website: https://www.checkpoint.com/cloudguard/
---
