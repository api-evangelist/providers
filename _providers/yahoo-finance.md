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
- description: Real time low latency Yahoo Finance API for stock market, crypto currencies, and currency exchange
  name: Yahoo Finance
  slug: yahoo-finance
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yahoo-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yahoofinanceapi.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Real time low latency Yahoo Finance API for stock market, crypto currencies, and currency exchange
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yahoo-finance.png
layout: provider
modified: '2026-05-28'
name: Yahoo Finance
nav: Providers
network: true
overview: Yahoo Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.
random_paper: 17
score:
  band: minimal
  composite: 5.7
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Yahoo Finance Domain Security
  slug: yahoo-finance-domain-security
  summary_line: DMARC
slug: yahoo-finance
tags:
- Finance
- Public APIs
website: https://www.yahoofinanceapi.com/
---
