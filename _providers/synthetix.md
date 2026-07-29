---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Synthetix Agentic Access
  operation_count: 31
  slug: synthetix-agentic-access
  summary_line: 31 operations
api_count: 11
apis:
- description: Public REST API for accessing Synthetix market data including markets, prices, candles, funding rates, collateral configurations, contract specs, orderbook depth, exchange status, and fee tier informa
  name: Synthetix Info API
  slug: synthetix-info-api
- description: Authenticated REST API for trading operations and account management on the Synthetix perpetuals exchange. Supports order placement, cancellation, position management, collateral operations, subaccoun
  name: Synthetix Trade API
  slug: synthetix-trade-api
- description: Public WebSocket API for real-time Synthetix market data subscriptions including live market prices, candles, and orderbook depth updates. No authentication required. Supports heartbeat management for
  name: Synthetix WebSocket Info API
  slug: synthetix-websocket-info-api
- description: 'Authenticated WebSocket API for real-time trading operations and account event streaming on Synthetix. Supports live order management, position updates, account activity subscriptions, and delegation '
  name: Synthetix WebSocket Trade API
  slug: synthetix-websocket-trade-api
- description: The escrowed-balance API from Synthetix — 4 operation(s) for escrowed-balance.
  name: Synthetix escrowed-balance API
  slug: synthetix-escrowed-balance-api
- description: The health-check API from Synthetix — 2 operation(s) for health-check.
  name: Synthetix health-check API
  slug: synthetix-health-check-api
- description: The staking API from Synthetix — 2 operation(s) for staking.
  name: Synthetix staking API
  slug: synthetix-staking-api
- description: The stats API from Synthetix — 1 operation(s) for stats.
  name: Synthetix stats API
  slug: synthetix-stats-api
- description: The supply API from Synthetix — 2 operation(s) for supply.
  name: Synthetix supply API
  slug: synthetix-supply-api
- description: The v3 API from Synthetix — 19 operation(s) for v3.
  name: Synthetix v3 API
  slug: synthetix-v3-api
- description: The vested-balance API from Synthetix — 1 operation(s) for vested-balance.
  name: Synthetix vested-balance API
  slug: synthetix-vested-balance-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synthetix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthetix-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.synthetix.io/
- group: start
  title: ''
  type: PortalDocumentation
  url: https://docs.synthetix.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Synthetixio
- group: build
  title: ''
  type: X-python-sdk
  url: https://synthetixio.github.io/python-sdk/
- group: commercial
  title: ''
  type: Plans
  url: https://synthetix.io/plans.html
- group: commercial
  title: ''
  type: FinOps
  url: https://synthetix.io/finops.html
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.synthetix.io/developer-resources/api/rate-limits
- group: operate
  title: ''
  type: X-discord
  url: https://discord.gg/synthetix
- group: company
  title: ''
  type: X-twitter
  url: https://twitter.com/synthetix_io
- group: build
  title: ''
  type: X-github
  url: https://github.com/Synthetixio/synthetix-v3
- group: other
  title: ''
  type: X-deposit-contract
  url: https://etherscan.io/address/0xD62595c3c23B690BAEE0935e107A209Cb1Dbd37B
- group: docs
  title: ''
  type: X-authentication-docs
  url: https://developers.synthetix.io/developer-resources/api/authentication
- group: design
  title: ''
  type: X-error-handling
  url: https://developers.synthetix.io/developer-resources/api/error-handling
description: Synthetix is a derivatives liquidity protocol built on Ethereum and EVM-compatible L2 networks (Optimism, Base). It provides perpetual futures trading with deep onchain liquidity, supporting a wide range of synthetic assets. The platform exposes REST and WebSocket APIs for querying collateral, managing positions, accessing funding rates, monitoring liquidations, tracking staking rewards, and interacting with V3 markets across Optimism and Base.
examples:
- key_count: 29
  name: Examples
  slug: examples
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Synthetix exposes GraphQL APIs via The Graph protocol, providing indexed blockchain data for the Synthetix V3 derivatives liquidity protocol. Subgraphs are available for the core protocol (pools, coll
  name: Synthetix GraphQL API
  slug: synthetix-graphql
image: https://synthetix.io/favicon.ico
json_schemas:
- name: Synthetix API Schemas
  property_count: 0
  slug: synthetix
layout: provider
modified: '2026-06-14'
name: Synthetix
nav: Providers
network: true
overview: 'Synthetix publishes 7 APIs on the [APIs.io](https://apis.io/) network, including escrowed-balance API, health-check API, staking API, and 4 more. Tagged areas include DeFi, Derivatives, Perpetuals, Synthetic Assets, and Liquidity Protocol.


  The Synthetix catalog on APIs.io includes 1 Spectral governance ruleset.


  Synthetix''s developer surface includes documentation and 14 more developer resources.'
plans:
- name: Plans
  plan_count: 9
  slug: plans
random_paper: 36
rate_limits:
- limit_count: 11
  name: Rate Limits
  slug: rate-limits
rules:
- name: Synthetix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: synthetix-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.4
  delta: -0.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.4
    developer_ergonomics: 8.7
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synthetix/refs/heads/main/screenshots/synthetix-2026-06-20T194832.png
security:
- kind: domain-security
  name: Synthetix Domain Security
  slug: synthetix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: synthetix
tags:
- DeFi
- Derivatives
- Perpetuals
- Synthetic Assets
- Liquidity Protocol
- Blockchain
- Ethereum
- Optimism
- Base
- Trading
website: https://synthetix.io/
---
