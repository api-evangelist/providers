---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Payerset Agentic Access
  operation_count: 13
  slug: payerset-agentic-access
  summary_line: 13 operations
api_count: 5
apis:
- description: Billing code classification, categorization, and code type reference data.
  name: Payerset Billing Codes API
  slug: payerset-billing-codes-api
- description: Hospital price transparency machine-readable file discovery (hospitals, systems, payers).
  name: Payerset Hospital MRF API
  slug: payerset-hospital-mrf-api
- description: Payer reference metadata and payer listings.
  name: Payerset Payers API
  slug: payerset-payers-api
- description: Provider (NPI), organization, and tax identification (TIN) reference metadata and mappings.
  name: Payerset Providers API
  slug: payerset-providers-api
- description: Payer-provider negotiated rate lookups from Transparency in Coverage MRFs.
  name: Payerset Rates API
  slug: payerset-rates-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Payerset Data Lake Billing Codes API
  slug: open-payerset-billing-codes-api
- collection_type: open
  name: Payerset Data Lake Billing Codes Hospital MRF API
  slug: open-payerset-hospital-mrf-api
- collection_type: open
  name: Payerset Data Lake Billing Codes Payers API
  slug: open-payerset-payers-api
- collection_type: open
  name: Payerset Data Lake Billing Codes Providers API
  slug: open-payerset-providers-api
- collection_type: open
  name: Payerset Data Lake Billing Codes Rates API
  slug: open-payerset-rates-api
- collection_type: open
  name: Payerset Data Lake API
  slug: open-payerset
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payerset-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payerset-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payerset-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payerset
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/payerset
- group: company
  title: ''
  type: Website
  url: https://www.payerset.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.payerset.com
- group: commercial
  title: ''
  type: Plans
  url: plans/payerset-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payerset-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/payerset-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.payerset.com/insights/
created: '2026-06-21'
description: Payerset is a healthcare price transparency data company that parses every payer Transparency in Coverage (TiC) machine-readable file and compliant hospital MRF each quarter, enriches negotiated rates with provider, payer, and claims metadata, and delivers it as analytics-ready datasets. The Payerset Data Lake API exposes payer-provider negotiated rate lookups, NPI/TIN provider mapping, billing-code classification, and hospital MRF discovery via a REST API authenticated with an x-api-key header.
finops:
- name: Payerset Finops
  service_category: Analytics
  slug: payerset-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payerset.png
layout: provider
modified: '2026-06-21'
name: Payerset
nav: Providers
network: true
overview: 'Payerset publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Billing Codes API, Hospital MRF API, Payers API, and 2 more. Tagged areas include Healthcare, Price Transparency, Negotiated Rates, Machine-Readable Files, and Payer Data.


  Payerset''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Payerset Plans Pricing
  plan_count: 2
  slug: payerset-plans-pricing
random_paper: 132
rate_limits:
- limit_count: 2
  name: Payerset Rate Limits
  slug: payerset-rate-limits
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payerset/refs/heads/main/screenshots/payerset-2026-08-07T191632.png
security:
- kind: authentication
  name: Payerset Authentication
  slug: payerset-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Payerset Domain Security
  slug: payerset-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payerset
tags:
- Healthcare
- Price Transparency
- Negotiated Rates
- Machine-Readable Files
- Payer Data
website: https://www.payerset.com
---
