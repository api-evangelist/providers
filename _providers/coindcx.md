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
    asyncapi_events: true
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
  score: 5.8
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Cryptocurrency Trading Platform
  name: CoinDCX
  slug: coindcx
- description: Real-time Socket.IO streaming at stream.coindcx.com for public spot and futures market data (orderbook depth, public trades, current prices, price statistics, last-traded price, candlesticks) and auth
  name: CoinDCX Streaming Socket.IO API
  slug: streaming-api
artifact_total: 5
asyncapis:
- description: 'AsyncAPI 2.6 description of CoinDCX''s public and authenticated streaming interface. CoinDCX exposes a Socket.IO endpoint at https://stream.coindcx.com that delivers real-time orderbook, trade, price, '
  name: CoinDCX Streaming Socket.IO API
  slug: coindcx-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coindcx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.coindcx.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Cryptocurrency Trading Platform
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coindcx.png
layout: provider
modified: '2026-05-30'
name: CoinDCX
nav: Providers
network: true
overview: 'CoinDCX publishes 1 API on the [APIs.io](https://apis.io/) network: Streaming Socket.IO API. Tagged areas include Cryptocurrency and Public APIs.


  The CoinDCX catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 64
rules:
- name: CoinDCX API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: coindcx-asyncapi-spectral-rules
score:
  band: emerging
  composite: 22.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 33.3
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 60.5
    operational_transparency: 0.0
  previous_composite: 22.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coindcx/refs/heads/main/screenshots/coindcx-2026-06-20T174731.png
security:
- kind: domain-security
  name: Coindcx Domain Security
  slug: coindcx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coindcx
tags:
- Cryptocurrency
- Public APIs
website: https://docs.coindcx.com/
---
