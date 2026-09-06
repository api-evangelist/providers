---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: One Inch Agentic Access
  operation_count: 15
  slug: one-inch-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 1
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
- baseURL: https://api.1inch.dev/swap/v6.0
  baseurl_source: declared
  description: The Balance API from 1inch — 1 operation(s) for balance.
  name: 1inch Balance API
  slug: one-inch-balance-api
- baseURL: https://api.1inch.dev/swap/v6.0
  baseurl_source: declared
  description: The GasPrice API from 1inch — 1 operation(s) for gasprice.
  name: 1inch GasPrice API
  slug: one-inch-gasprice-api
- baseURL: https://api.1inch.dev/swap/v6.0
  baseurl_source: declared
  description: The Orderbook API from 1inch — 2 operation(s) for orderbook.
  name: 1inch Orderbook API
  slug: one-inch-orderbook-api
- baseURL: https://api.1inch.dev/swap/v6.0
  baseurl_source: declared
  description: The Portfolio API from 1inch — 1 operation(s) for portfolio.
  name: 1inch Portfolio API
  slug: one-inch-portfolio-api
- baseURL: https://api.1inch.dev/swap/v6.0
  baseurl_source: declared
  description: The SpotPrice API from 1inch — 1 operation(s) for spotprice.
  name: 1inch SpotPrice API
  slug: one-inch-spotprice-api
- baseURL: https://api.1inch.dev/swap/v6.0
  baseurl_source: declared
  description: The Swap API from 1inch — 8 operation(s) for swap.
  name: 1inch Swap API
  slug: one-inch-swap-api
- baseURL: https://api.1inch.dev/swap/v6.0
  baseurl_source: declared
  description: The Token API from 1inch — 1 operation(s) for token.
  name: 1inch Token API
  slug: one-inch-token-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 1inch Developer Portal APIs Balance API
  slug: open-one-inch-balance-api
- collection_type: open
  name: 1inch Developer Portal APIs Balance GasPrice API
  slug: open-one-inch-gasprice-api
- collection_type: open
  name: 1inch Developer Portal APIs Balance Orderbook API
  slug: open-one-inch-orderbook-api
- collection_type: open
  name: 1inch Developer Portal APIs Balance Portfolio API
  slug: open-one-inch-portfolio-api
- collection_type: open
  name: 1inch Developer Portal APIs Balance SpotPrice API
  slug: open-one-inch-spotprice-api
- collection_type: open
  name: 1inch Developer Portal APIs Balance Swap API
  slug: open-one-inch-swap-api
- collection_type: open
  name: 1inch Developer Portal APIs Balance Token API
  slug: open-one-inch-token-api
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
random_paper: 8
rate_limits:
- limit_count: 4
  name: One Inch Rate Limits
  slug: one-inch-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Multi-Chain
- Limit Orders
- Fusion
- Cross-Chain
website: https://business.1inch.com/
---
