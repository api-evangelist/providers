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
- description: Stock market data (real-time & historical)
  name: Twelve Data
  slug: twelve-data
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/twelve-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twelve-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://twelvedata.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Stock market data (real-time & historical)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/twelve-data.png
layout: provider
modified: '2026-05-28'
name: Twelve Data
nav: Providers
network: true
overview: Twelve Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.
random_paper: 78
score:
  band: minimal
  composite: 7.3
  delta: -1.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twelve-data/refs/heads/main/screenshots/twelve-data-2026-06-20T195844.png
security:
- kind: domain-security
  name: Twelve Data Domain Security
  slug: twelve-data-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Twelve Data Trust Center
  slug: twelve-data-trust-center
  summary_line: SOC 2, GDPR
slug: twelve-data
tags:
- Finance
- Public APIs
website: https://twelvedata.com/
---
