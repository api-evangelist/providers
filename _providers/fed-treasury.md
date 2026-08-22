---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: U.S. Department of the Treasury Data
  name: Fed Treasury
  slug: fed-treasury
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fed-treasury-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fiscaldata.treasury.gov/api-documentation/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: U.S. Department of the Treasury Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fed-treasury.png
layout: provider
modified: '2026-05-28'
name: Fed Treasury
nav: Providers
network: true
overview: Fed Treasury publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.
random_paper: 4
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fed-treasury/refs/heads/main/screenshots/fed-treasury-2026-06-20T181109.png
security:
- kind: domain-security
  name: Fed Treasury Domain Security
  slug: fed-treasury-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: fed-treasury
tags:
- Finance
- Public APIs
website: https://fiscaldata.treasury.gov/api-documentation/
---
