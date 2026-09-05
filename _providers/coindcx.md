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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Cryptocurrency Trading Platform
  name: CoinDCX
  slug: coindcx
- baseURL: https://stream.coindcx.com
  baseurl_source: declared
  description: Real-time Socket.IO streaming at stream.coindcx.com for public spot and futures market data (orderbook depth, public trades, current prices, price statistics, last-traded price, candlesticks) and auth
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
random_paper: 9
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: CoinDCX API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: coindcx-asyncapi-spectral-rules
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 45.8
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 0.0
  previous_composite: 20.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
