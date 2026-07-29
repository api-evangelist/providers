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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: US federal spending data
  name: USAspending.gov
  slug: usaspendinggov
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usaspending-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.usaspending.gov/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: US federal spending data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usaspending-gov.png
layout: provider
modified: '2026-05-28'
name: USAspending.gov
nav: Providers
network: true
overview: USAspending.gov publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 42
score:
  band: minimal
  composite: 6.5
  delta: -1.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usaspending-gov/refs/heads/main/screenshots/usaspending-gov-2026-06-20T200644.png
security:
- kind: domain-security
  name: Usaspending Gov Domain Security
  slug: usaspending-gov-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: usaspending-gov
tags:
- Government
- Public APIs
website: https://api.usaspending.gov/
---
