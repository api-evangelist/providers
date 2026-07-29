---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: One Inch Agentic Access
  operation_count: 15
  slug: one-inch-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 14
apis:
- description: Quote and swap endpoints supporting classic aggregation, Fusion intent-based swaps, and cross-chain (Fusion+).
  name: 1inch Swap API
  slug: swap-api
- description: Limit-order placement, query, fill, and cancellation endpoints.
  name: 1inch Orderbook API
  slug: orderbook-api
- description: Wallet balance lookup across supported EVM chains.
  name: 1inch Balance API
  slug: balance-api
- description: On-chain spot price feeds for tokens across supported EVM chains.
  name: 1inch Spot Price API
  slug: spot-price-api
- description: Token metadata and discovery endpoints.
  name: 1inch Token API
  slug: token-api
- description: Portfolio composition, P&L, and historical valuation across supported networks.
  name: 1inch Portfolio API
  slug: portfolio-api
- description: Gas price estimates for EIP-1559 across supported EVM chains.
  name: 1inch Gas Price API
  slug: gas-price-api
- description: The Balance API from 1inch — 1 operation(s) for balance.
  name: 1inch Balance API
  slug: one-inch-balance-api
- description: The GasPrice API from 1inch — 1 operation(s) for gasprice.
  name: 1inch GasPrice API
  slug: one-inch-gasprice-api
- description: The Orderbook API from 1inch — 2 operation(s) for orderbook.
  name: 1inch Orderbook API
  slug: one-inch-orderbook-api
- description: The Portfolio API from 1inch — 1 operation(s) for portfolio.
  name: 1inch Portfolio API
  slug: one-inch-portfolio-api
- description: The SpotPrice API from 1inch — 1 operation(s) for spotprice.
  name: 1inch SpotPrice API
  slug: one-inch-spotprice-api
- description: The Swap API from 1inch — 8 operation(s) for swap.
  name: 1inch Swap API
  slug: one-inch-swap-api
- description: The Token API from 1inch — 1 operation(s) for token.
  name: 1inch Token API
  slug: one-inch-token-api
artifact_total: 21
collections:
- collection_type: open
  name: 1inch Developer Portal APIs
  slug: open-one-inch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/one-inch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/one-inch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/one-inch-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/1inch
- group: start
  title: ''
  type: Portal
  url: https://business.1inch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://business.1inch.com/portal/documentation/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://business.1inch.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/1inch
- group: commercial
  title: ''
  type: Plans
  url: plans/one-inch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/one-inch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/one-inch-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://1inch.com/llms.txt
created: '2026-05-08'
description: 1inch is the leading DEX aggregator. The 1inch Developer Portal exposes 13+ APIs covering Swap (classic, Fusion intent, cross-chain), Orderbook, Balance, Spot Price, Token, Token Details, Portfolio, Gas Price, NFT, Traces, History, Transaction Gateway, Web3 RPC, Charts, and Domains. APIs serve 12+ EVM chains. Authentication via Authorization Bearer header.
finops:
- name: One Inch Finops
  service_category: DeFi Infrastructure
  slug: one-inch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/one-inch.png
layout: provider
modified: '2026-05-08'
name: 1inch
nav: Providers
network: true
overview: '1inch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Balance API, GasPrice API, Orderbook API, and 4 more. Tagged areas include Web3, DeFi, DEX, Aggregator, and Swap.


  1inch''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, and 7 more developer resources.'
plans:
- name: One Inch Plans Pricing
  plan_count: 4
  slug: one-inch-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 4
  name: One Inch Rate Limits
  slug: one-inch-rate-limits
score:
  band: thin
  composite: 40.4
  delta: -2.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/one-inch/refs/heads/main/screenshots/one-inch-2026-06-20T190708.png
security:
- kind: authentication
  name: One Inch Authentication
  slug: one-inch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: One Inch Domain Security
  slug: one-inch-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: one-inch
tags:
- Web3
- DeFi
- DEX
- Aggregator
- Swap
- Multi-chain
- Limit Orders
- Fusion
- Cross-chain
website: https://business.1inch.com/
---
