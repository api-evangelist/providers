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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: Public REST API endpoints for querying market data, instruments, tickers, options boards, implied volatility, settlement history, and liquidity pool analytics without authentication.
  name: Lyra Public REST API
  slug: lyra-public-rest-api
- description: Authenticated REST API endpoints for managing subaccounts, submitting and cancelling orders, transferring collateral and positions, accessing order history, handling RFQs, and performing margin calcul
  name: Lyra Private REST API
  slug: lyra-private-rest-api
- description: WebSocket API for real-time streaming of market data, order book updates, ticker subscriptions, and private account notifications. Authentication uses wallet-signed timestamps via the login endpoint.
  name: Lyra WebSocket API
  slug: lyra-websocket-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lyra-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.derive.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/derivexyz
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/derive
- group: company
  title: ''
  type: Blog
  url: https://insights.derive.xyz/
- group: other
  title: ''
  type: BlockExplorer
  url: https://explorer.lyra.finance
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.derive.xyz/reference/rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.derive.xyz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://derive.xyz/terms
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/lyra/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/lyra/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/lyra/refs/heads/main/finops/finops.yml
created: '2026-06-14'
description: Lyra (now Derive) is an institutional-grade options AMM protocol built on Ethereum, offering REST and WebSocket APIs for querying options boards, strike prices, implied volatility, trading positions, and liquidity pool analytics. The platform provides onchain options and perpetual futures trading with TradFi-level speed via an OP Stack rollup (Chain ID 957).
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lyra.png
layout: provider
modified: '2026-06-14'
name: Lyra
nav: Providers
network: true
overview: 'Lyra publishes 1 API on the [APIs.io](https://apis.io/) network: Public REST API. Tagged areas include Options, AMM, DeFi, Derivatives, and Implied Volatility.


  Lyra''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 32
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 30.7
  delta: -1.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.7
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.2
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lyra/refs/heads/main/screenshots/lyra-2026-06-20T184813.png
security:
- kind: domain-security
  name: Lyra Domain Security
  slug: lyra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lyra
tags:
- Options
- AMM
- DeFi
- Derivatives
- Implied Volatility
- Perpetuals
- Crypto
- Finance
---
