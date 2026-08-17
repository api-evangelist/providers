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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Jupiter Exchange Agentic Access
  operation_count: 2
  slug: jupiter-exchange-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 7
apis:
- description: Quote and swap endpoints aggregating Solana DEX liquidity.
  name: Jupiter Swap API
  slug: swap-api
- description: USD pricing for Solana tokens, with batch lookup and best-route prices.
  name: Jupiter Price API
  slug: price-api
- description: Verified Solana token list and metadata.
  name: Jupiter Tokens API
  slug: tokens-api
- description: Limit order placement, query, and cancellation on Solana.
  name: Jupiter Trigger (Limit Order) API
  slug: trigger-api
- description: Recurring (dollar-cost-averaging) order automation on Solana.
  name: Jupiter Recurring (DCA) API
  slug: recurring-api
- description: Leveraged perp trading endpoints on Jupiter Perps.
  name: Jupiter Perps API
  slug: perps-api
- description: Quote and build Solana DEX-aggregator swap transactions.
  name: Jupiter Swap API
  slug: jupiter-exchange-swap-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jupiter Swap API
  slug: open-jupiter-exchange-swap-api
- collection_type: open
  name: Jupiter Swap API
  slug: open-jupiter-exchange
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupiter-exchange-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupiter-exchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jupiter-exchange-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://jup.ag/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jup.ag/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://portal.jup.ag/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jup-ag
- group: commercial
  title: ''
  type: Plans
  url: plans/jupiter-exchange-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jupiter-exchange-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jupiter-exchange-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://developers.jup.ag/blog
created: '2026-05-08'
description: Jupiter is the leading Solana DEX aggregator and liquidity infrastructure platform. APIs cover Swap (token exchanges), Tokens (metadata and verification), Price (USD pricing), Lend (yield and borrowing), Trigger (limit orders), Recurring (DCA), Prediction (event markets), and Perps (leveraged trading). The Developer Platform issues a single API key across products.
finops:
- name: Jupiter Exchange Finops
  service_category: DeFi Infrastructure
  slug: jupiter-exchange-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupiter-exchange.png
layout: provider
modified: '2026-05-08'
name: Jupiter
nav: Providers
network: true
overview: 'Jupiter publishes 1 API on the [APIs.io](https://apis.io/) network: Swap API. Tagged areas include Web3, Solana, DEX, Aggregator, and Swap.


  Jupiter''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Jupiter Exchange Plans Pricing
  plan_count: 2
  slug: jupiter-exchange-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Jupiter Exchange Rate Limits
  slug: jupiter-exchange-rate-limits
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 59.7
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupiter-exchange/refs/heads/main/screenshots/jupiter-exchange-2026-06-20T183836.png
security:
- kind: authentication
  name: Jupiter Exchange Authentication
  slug: jupiter-exchange-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jupiter Exchange Domain Security
  slug: jupiter-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jupiter-exchange
tags:
- Web3
- Solana
- DEX
- Aggregator
- Swap
- Limit Orders
- DCA
- Perpetuals
website: https://jup.ag/
---
