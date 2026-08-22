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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bitso Agentic Access
  operation_count: 12
  slug: bitso-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 5
apis:
- description: Real-time streaming channels for trades, order-book diffs, and full order-book snapshots. Used by trading clients and market-data consumers that need sub-second updates.
  name: Bitso WebSocket API
  slug: websocket
- description: Cross-border disbursement and collection API powered by stablecoin and LATAM rails. Lets businesses fund into Bitso, convert between assets and fiat, and pay out to destination accounts across support
  name: Bitso Payouts and Pay-Ins API
  slug: payouts-funding
- description: Juno is Bitso's programmable-money platform for Mexican peso (MXN) rails and stablecoin operations. The API supports account creation, SPEI funding, MXNB stablecoin mint / redeem and on-chain transfer
  name: Juno API
  slug: juno
- description: Authenticated account and trading endpoints.
  name: Bitso Private API
  slug: bitso-private-api
- description: Public market data endpoints. No authentication required.
  name: Bitso Public API
  slug: bitso-public-api
artifact_total: 18
asyncapis:
- description: Bitso's public real-time WebSocket feed for the Bitso cryptocurrency exchange. Clients connect to a single endpoint and subscribe to one or more channels per order book (e.g. btc_mxn). Three public ch
  name: Bitso WebSocket API
  slug: bitso-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bitso Trading Private API
  slug: open-bitso-private-api
- collection_type: open
  name: Bitso Trading Private Public API
  slug: open-bitso-public-api
- collection_type: open
  name: Bitso Trading API
  slug: open-bitso
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitso-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bitso-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitso-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitso-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://bitso.com/
- group: other
  title: ''
  type: Business
  url: https://bitso.com/business
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitso.com/
- group: docs
  title: ''
  type: OpenAPI Index
  url: https://docs.bitso.com/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bitso
- group: build
  title: ''
  type: GitHub
  url: https://github.com/bitso
- group: operate
  title: ''
  type: Status
  url: https://status.bitso.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.bitso.com/
created: '2026-05-23'
description: Bitso is one of Latin America's largest cryptocurrency exchanges and stablecoin-rail providers, serving Mexico, Argentina, Brazil, Colombia, and other LATAM markets. Bitso exposes a public REST trading API and a WebSocket feed at bitso.com/api/v3 for market data, order management, conversions, OTC / RFQ, and account operations; a Payouts & Pay-Ins API for cross-border crypto and fiat disbursements; and the Juno API for Mexican peso (MXN) rails and stablecoin programmable money. API and OpenAPI references are catalogued at docs.bitso.com.
finops:
- name: Bitso Finops
  service_category: API
  slug: bitso-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitso.png
layout: provider
modified: '2026-05-23'
name: Bitso
nav: Providers
network: true
overview: 'Bitso publishes 3 APIs on the [APIs.io](https://apis.io/) network: WebSocket API, Private API, and Public API. Tagged areas include Cryptocurrency, Exchange, Trading, Stablecoins, and Payouts.


  The Bitso catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bitso''s developer surface includes authentication, documentation, GitHub presence, status page, engineering blog, and 7 more developer resources.'
plans:
- name: Bitso Plans Pricing
  plan_count: 1
  slug: bitso-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Bitso Rate Limits
  slug: bitso-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Bitso API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: bitso-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.2
  delta: -3.1
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 11.4
    contract_quality: 55.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 26.3
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitso/refs/heads/main/screenshots/bitso-2026-06-20T173323.png
security:
- kind: authentication
  name: Bitso Authentication
  slug: bitso-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bitso Domain Security
  slug: bitso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bitso Trust Center
  slug: bitso-trust-center
  summary_line: ISO 27001
slug: bitso
tags:
- Cryptocurrency
- Exchange
- Trading
- Stablecoins
- Payouts
- Cross Border
- Latin America
- Mexico
- Fintech
website: https://bitso.com/
---
