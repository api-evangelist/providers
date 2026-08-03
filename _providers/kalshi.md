---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 31
  human_in_the_loop: 1
  name: Kalshi Agentic Access
  operation_count: 98
  slug: kalshi-agentic-access
  summary_line: 98 operations · 31 acting · 1 human-in-the-loop
api_count: 21
apis:
- description: Demo / sandbox environment for the Kalshi Trade API - mirrors production semantics with simulated balances and markets for safe development and automated testing.
  name: Kalshi Trade API (Demo)
  slug: trade-api-demo
- description: Real-time streaming feed for market data, order book updates, fills, and portfolio events on Kalshi. Documented as an AsyncAPI spec alongside the OpenAPI REST surface.
  name: Kalshi WebSocket Streaming API
  slug: websocket
- description: Machine-readable AsyncAPI description of the Kalshi WebSocket streaming API. Suitable for generating async clients and documenting message schemas.
  name: Kalshi AsyncAPI Specification
  slug: asyncapi
- description: Official Python starter / SDK published by Kalshi for connecting to the Trade REST API and WebSocket streams. Includes request signing, authentication helpers, and example trading flows.
  name: Kalshi Python Starter Kit
  slug: python-starter
- description: The account API from Kalshi — 2 operation(s) for account.
  name: Kalshi account API
  slug: kalshi-account-api
- description: API key management endpoints
  name: Kalshi api-keys API
  slug: kalshi-api-keys-api
- description: Request-for-quote (RFQ) endpoints
  name: Kalshi communications API
  slug: kalshi-communications-api
- description: Event endpoints
  name: Kalshi events API
  slug: kalshi-events-api
- description: Exchange status and information endpoints
  name: Kalshi exchange API
  slug: kalshi-exchange-api
- description: FCM member specific endpoints
  name: Kalshi fcm API
  slug: kalshi-fcm-api
- description: The historical API from Kalshi — 7 operation(s) for historical.
  name: Kalshi historical API
  slug: kalshi-historical-api
- description: Incentive program endpoints
  name: Kalshi incentive-programs API
  slug: kalshi-incentive-programs-api
- description: Live data endpoints
  name: Kalshi live-data API
  slug: kalshi-live-data-api
- description: The market API from Kalshi — 9 operation(s) for market.
  name: Kalshi market API
  slug: kalshi-market-api
- description: Milestone endpoints
  name: Kalshi milestone API
  slug: kalshi-milestone-api
- description: Multivariate event collection endpoints
  name: Kalshi multivariate API
  slug: kalshi-multivariate-api
- description: Order group management endpoints
  name: Kalshi order-groups API
  slug: kalshi-order-groups-api
- description: Order management endpoints
  name: Kalshi orders API
  slug: kalshi-orders-api
- description: Portfolio and balance information endpoints
  name: Kalshi portfolio API
  slug: kalshi-portfolio-api
- description: Search and filtering endpoints
  name: Kalshi search API
  slug: kalshi-search-api
- description: Structured targets endpoints
  name: Kalshi structured-targets API
  slug: kalshi-structured-targets-api
artifact_total: 30
asyncapis:
- description: Real-time WebSocket streaming feed for the Kalshi CFTC-regulated event contracts exchange. Publishes orderbook updates, public trades, market tickers, user orders, user fills, market positions, market
  name: Kalshi WebSocket Streaming API
  slug: kalshi-asyncapi
collections:
- collection_type: open
  name: Kalshi Trade API Manual Endpoints
  slug: open-kalshi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kalshi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kalshi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kalshi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://kalshi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kalshi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kalshi.com/api-reference
- group: operate
  title: ''
  type: Help
  url: https://help.kalshi.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Kalshi
- group: commercial
  title: ''
  type: Developer Agreement
  url: https://kalshi.com/developer-agreement
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kalshi/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.kalshi.com/llms.txt
created: '2026-05-23'
description: Kalshi is a CFTC-regulated US exchange for binary event contracts on real-world outcomes - elections, economics, weather, sports, and more. The platform exposes a public REST trading API and WebSocket streams for market data, orders, positions, and portfolio actions, with a published OpenAPI 3 specification and AsyncAPI definition for the streaming surface. A demo environment mirrors production for safe development. Official Python and community SDKs are provided.
finops:
- name: Kalshi Finops
  service_category: API
  slug: kalshi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kalshi.png
layout: provider
modified: '2026-05-29'
name: Kalshi
nav: Providers
network: true
overview: 'Kalshi publishes 19 APIs on the [APIs.io](https://apis.io/) network, including WebSocket Streaming API, AsyncAPI Specification, account API, and 16 more. Tagged areas include Prediction Markets, Event Contracts, Exchange, CFTC, and Trading.


  The Kalshi catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kalshi''s developer surface includes authentication, documentation, API reference, GitHub presence, and 7 more developer resources.'
plans:
- name: Kalshi Plans Pricing
  plan_count: 1
  slug: kalshi-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Kalshi Rate Limits
  slug: kalshi-rate-limits
rules:
- name: Kalshi API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: kalshi-asyncapi-spectral-rules
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 68.8
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kalshi/refs/heads/main/screenshots/kalshi-2026-06-20T183909.png
security:
- kind: authentication
  name: Kalshi Authentication
  slug: kalshi-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Kalshi Domain Security
  slug: kalshi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kalshi
tags:
- Prediction Markets
- Event Contracts
- Exchange
- CFTC
- Trading
- Markets
website: https://kalshi.com/
---
