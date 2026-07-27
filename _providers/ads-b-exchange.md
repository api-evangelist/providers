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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Access real-time and historical data of any and all airborne aircraft
  name: ADS-B Exchange
  slug: ads-b-exchange
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ads-b-exchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adsbexchange.com/data/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Access real-time and historical data of any and all airborne aircraft
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ads-b-exchange.png
layout: provider
modified: '2026-05-28'
name: ADS-B Exchange
nav: Providers
network: true
overview: ADS-B Exchange publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.
random_paper: 43
score:
  band: minimal
  composite: 6.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ads-b-exchange/refs/heads/main/screenshots/ads-b-exchange-2026-06-20T165139.png
security:
- kind: domain-security
  name: Ads B Exchange Domain Security
  slug: ads-b-exchange-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ads-b-exchange
tags:
- Transportation
- Public APIs
website: https://www.adsbexchange.com/data/
---
