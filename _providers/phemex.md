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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Phemex Agentic Access
  operation_count: 89
  slug: phemex-agentic-access
  summary_line: 89 operations · 32 acting
api_count: 9
apis:
- description: The Account API from Phemex — 10 operation(s) for account.
  name: Phemex Account API
  slug: phemex-account-api
- description: The Conversion API from Phemex — 2 operation(s) for conversion.
  name: Phemex Conversion API
  slug: phemex-conversion-api
- description: The Market Data API from Phemex — 12 operation(s) for market data.
  name: Phemex Market Data API
  slug: phemex-market-data-api
- description: The Orders API from Phemex — 26 operation(s) for orders.
  name: Phemex Orders API
  slug: phemex-orders-api
- description: The Positions API from Phemex — 6 operation(s) for positions.
  name: Phemex Positions API
  slug: phemex-positions-api
- description: The Sub-Account Transfers API from Phemex — 2 operation(s) for sub-account transfers.
  name: Phemex Sub-Account Transfers API
  slug: phemex-sub-account-transfers-api
- description: The Trades API from Phemex — 7 operation(s) for trades.
  name: Phemex Trades API
  slug: phemex-trades-api
- description: The Transfers API from Phemex — 2 operation(s) for transfers.
  name: Phemex Transfers API
  slug: phemex-transfers-api
- description: The Wallets API from Phemex — 8 operation(s) for wallets.
  name: Phemex Wallets API
  slug: phemex-wallets-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/phemex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phemex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/phemex-authentication.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/phemex/phemex-api-docs
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/phemex/refs/heads/main/json-ld/phemex.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/phemex/refs/heads/main/vocabulary/phemex-vocabulary.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/phemex/phemex-api-docs
- group: auth
  title: ''
  type: Authentication
  url: https://github.com/phemex/phemex-api-docs/blob/master/Generic-API-Info.en.md
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/phemex/refs/heads/main/rate-limits/overview.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/phemex/refs/heads/main/plans/plans.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/phemex/refs/heads/main/finops/finops.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://phemex.com/help-center
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ccxt/ccxt
- group: build
  title: ''
  type: JavaClient
  url: https://github.com/phemex/java-client
- group: design
  title: ''
  type: ErrorCodes
  url: https://github.com/phemex/phemex-api-docs/blob/master/TradingErrorCode.md
- group: operate
  title: ''
  type: StatusPage
  url: https://status.phemex.com
- group: other
  title: ''
  type: Testnet
  url: https://testnet.phemex.com
created: '2026-06-13'
description: Phemex is a cryptocurrency derivatives exchange offering REST and WebSocket APIs for spot trading, perpetual contracts, futures, hedged perpetual contracts, asset transfers, and real-time market data. The platform provides low-latency trading infrastructure with HMAC SHA256 authentication and tiered rate limiting for institutional and retail traders.
examples:
- key_count: 5
  name: Place Contract Order
  slug: place-contract-order
- key_count: 5
  name: Place Spot Order
  slug: place-spot-order
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phemex.png
json_schemas:
- name: Phemex Order
  property_count: 27
  slug: order
- name: Phemex Position
  property_count: 19
  slug: position
jsonld:
- class_count: 0
  name: Phemex Context
  property_count: 0
  slug: phemex
layout: provider
modified: '2026-06-13'
name: Phemex
nav: Providers
network: true
overview: 'Phemex publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Conversion API, Market Data API, and 6 more. Tagged areas include Cryptocurrency, Derivatives, Spot Trading, Perpetual Contracts, and Futures.


  The Phemex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Phemex''s developer surface includes authentication, documentation, and 15 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 15
rate_limits:
- limit_count: 0
  name: Contract
  slug: contract
- limit_count: 0
  name: Hedged Perpetual
  slug: hedged-perpetual
- limit_count: 0
  name: Overview
  slug: overview
- limit_count: 0
  name: Spot
  slug: spot
- limit_count: 0
  name: Transfer
  slug: transfer
rules:
- name: Phemex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: phemex-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.8
  delta: -3.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 15.8
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phemex/refs/heads/main/screenshots/phemex-2026-06-20T191642.png
security:
- kind: authentication
  name: Phemex Authentication
  slug: phemex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Phemex Domain Security
  slug: phemex-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: phemex
tags:
- Cryptocurrency
- Derivatives
- Spot Trading
- Perpetual Contracts
- Futures
- WebSocket
- Market Data
---
