---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Betfair Agentic Access
  operation_count: 27
  slug: betfair-agentic-access
  summary_line: 27 operations · 26 acting
api_count: 7
apis:
- description: Low-latency, subscription-based push of market and order changes over a persistent raw SSL/TCP socket to stream-api.betfair.com:443. The protocol is CRLF-delimited JSON (one JSON message per line) - N
  name: Betfair Exchange Stream API
  slug: betfair-exchange-stream-api
- description: The Web Vendor Facility for licensed software vendors building web-based betting applications. Uses an OAuth2-style authorization flow so a vendor's web application can obtain access and refresh token
  name: Betfair Vendor API
  slug: betfair-vendor-api
- description: AccountAPING - account funds, details, statement, and app keys.
  name: Betfair Accounts API
  slug: betfair-accounts-api
- description: SportsAPING - market navigation, prices, and bet placement.
  name: Betfair Betting API
  slug: betfair-betting-api
- description: HeartbeatAPING - dead man's switch that cancels unmatched bets.
  name: Betfair Heartbeat API
  slug: betfair-heartbeat-api
- description: Download purchased historical exchange market data.
  name: Betfair Historic Data API
  slug: betfair-historic-data-api
- description: Session login, keep-alive, and logout via Betfair identity SSO.
  name: Betfair Identity API
  slug: betfair-identity-api
artifact_total: 16
asyncapis:
- description: 'AsyncAPI 2.6 description of the Betfair **Exchange Stream API** - Betfair''s low-latency, subscription-based push channel for market and order changes. IMPORTANT TRANSPORT NOTE: this is **NOT a WebSock'
  name: Betfair Exchange Stream API (SSL/TCP)
  slug: betfair-asyncapi
collections:
- collection_type: open
  name: Betfair Exchange API (API-NG)
  slug: open-betfair
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/betfair-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betfair-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/betfair-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/betfair
- group: company
  title: ''
  type: Website
  url: https://www.betfair.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.betfair.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/betfair-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/betfair-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/betfair-finops.yml
created: '2026-07-03'
description: Betfair operates the world's largest online betting exchange, where customers back and lay outcomes against each other rather than against a bookmaker. The Betfair Exchange API (API-NG) gives automated clients programmatic access to the exchange - navigating markets, retrieving live prices, placing and managing bets, and reading account state. It is exposed as lightweight JSON-RPC and REST operations over HTTPS under https://api.betfair.com/exchange (the Betting, Accounts, and Heartbeat APIs), with a separate real-time Exchange Stream API delivered over a raw SSL/TCP socket (CRLF-delimited JSON, not WebSocket) for low-latency market and order updates. A Historic Data API and a licensed Vendor (affiliate) API round out the platform. Auth combines an Application Key with a session token (ssoid) obtained from Betfair's identity SSO login.
finops:
- name: Betfair Finops
  service_category: Betting Exchange and Market Data
  slug: betfair-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betfair.png
layout: provider
modified: '2026-07-03'
name: Betfair
nav: Providers
network: true
overview: 'Betfair publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Exchange Stream API, Accounts API, Betting API, and 3 more. Tagged areas include Betting Exchange, Sports Betting, Wagering, Trading, and Market Data.


  The Betfair catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Betfair''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Betfair Plans Pricing
  plan_count: 4
  slug: betfair-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 7
  name: Betfair Rate Limits
  slug: betfair-rate-limits
rules:
- name: Betfair API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 6
  slug: betfair-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.9
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 46.8
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
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Betfair Authentication
  slug: betfair-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Betfair Domain Security
  slug: betfair-domain-security
  summary_line: TLSv1.3 · DMARC
slug: betfair
tags:
- Betting Exchange
- Sports Betting
- Wagering
- Trading
- Market Data
- JSON-RPC
- Streaming
website: https://www.betfair.com
---
