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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Soda Data Agentic Access
  operation_count: 18
  slug: soda-data-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 6
apis:
- description: Soda is a data quality platform that enables data testing, monitoring, and anomaly detection across data pipelines.
  name: Soda
  slug: soda-data
- description: The Attributes API from Soda — 2 operation(s) for attributes.
  name: Soda Attributes API
  slug: soda-data-attributes-api
- description: The Authentication API from Soda — 1 operation(s) for authentication.
  name: Soda Authentication API
  slug: soda-data-authentication-api
- description: The Checks API from Soda — 2 operation(s) for checks.
  name: Soda Checks API
  slug: soda-data-checks-api
- description: The Contracts API from Soda — 8 operation(s) for contracts.
  name: Soda Contracts API
  slug: soda-data-contracts-api
- description: The Datasets API from Soda — 1 operation(s) for datasets.
  name: Soda Datasets API
  slug: soda-data-datasets-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Soda Cloud REST Attributes API
  slug: open-soda-data-attributes-api
- collection_type: open
  name: Soda Cloud REST Attributes Authentication API
  slug: open-soda-data-authentication-api
- collection_type: open
  name: Soda Cloud REST Attributes Checks API
  slug: open-soda-data-checks-api
- collection_type: open
  name: Soda Cloud REST Attributes Contracts API
  slug: open-soda-data-contracts-api
- collection_type: open
  name: Soda Cloud REST Attributes Datasets API
  slug: open-soda-data-datasets-api
- collection_type: open
  name: Soda Cloud REST API
  slug: open-soda-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soda-data-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/soda-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soda-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soda-data-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sodadata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sodadata
- group: company
  title: ''
  type: Website
  url: https://www.soda.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soda.io
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.soda.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.soda.io/blog
created: '2026-03-27'
description: Soda is a data quality platform that enables data testing, monitoring, and anomaly detection across data pipelines.
finops:
- name: Soda Data Finops
  service_category: API
  slug: soda-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soda-data.png
layout: provider
modified: '2026-03-27'
name: Soda
nav: Providers
network: true
overview: 'Soda publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Authentication API, Checks API, and 2 more. Tagged areas include AIOps and Data Quality.


  Soda''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Soda Data Plans Pricing
  plan_count: 3
  slug: soda-data-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Soda Data Rate Limits
  slug: soda-data-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 15.3
    developer_ergonomics: 23.8
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soda-data/refs/heads/main/screenshots/soda-data-2026-06-20T194129.png
security:
- kind: authentication
  name: Soda Data Authentication
  slug: soda-data-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Soda Data Domain Security
  slug: soda-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Soda Data Trust Center
  slug: soda-data-trust-center
  summary_line: SOC 2, GDPR
slug: soda-data
tags:
- AIOps
- Data Quality
website: https://www.soda.io
---
