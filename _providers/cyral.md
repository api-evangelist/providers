---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.cyral.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cyralinc
- group: docs
  title: ''
  type: Documentation
  url: https://registry.terraform.io/providers/cyralinc/cyral/latest/docs
- group: build
  title: ''
  type: Packages
  url: packages/cyral-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cyral-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyral-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cyral-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cyral-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cyral-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyral-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cyral-llms.txt
created: '2026-07-17'
description: 'Cyral is a data security and governance platform (founded 2018, Milpitas CA; acquired by Varonis in March 2025) that provides an agentless, stateless data-layer sidecar for monitoring and governing access to data repositories such as Snowflake, PostgreSQL, MySQL, MongoDB, Amazon S3, Kafka, and Oracle. Cyral was built API-first: its Control Plane exposes a REST API secured with OAuth2 client-credentials, fully automatable through the official Cyral Terraform provider (cyralinc/cyral) and supporting Terraform modules for AWS, Azure, and Okta. Following the Varonis acquisition, cyral.com now redirects to Varonis'' Database Activity Monitoring product, but the first-party developer tooling remains published on the cyralinc GitHub organization and the Terraform Registry.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cyral.png
layout: provider
modified: '2026-07-18'
name: Cyral
nav: Providers
network: true
overview: 'Cyral is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Data Security, Database Activity Monitoring, and Data Governance.


  Cyral''s developer surface includes documentation, authentication, changelog, and 8 more developer resources.'
random_paper: 87
score:
  band: emerging
  composite: 15.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 15.2
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyral/refs/heads/main/screenshots/cyral-2026-07-25T211100.png
security:
- kind: authentication
  name: Cyral Authentication
  slug: cyral-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Cyral Domain Security
  slug: cyral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cyral
tags:
- Company
- Cybersecurity
- Data Security
- Database Activity Monitoring
- Data Governance
- Access Control
- Terraform
- SCIM
- OAuth
website: https://www.cyral.com/
---
