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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Jupiter Ag Agentic Access
  operation_count: 2
  slug: jupiter-ag-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 11
apis:
- description: Returns the best swap route across Solana DEX liquidity and produces a versioned transaction ready to sign and send. Supports quote-then-swap, swap-instructions for custom transaction building, slippa
  name: Jupiter Swap API
  slug: swap-api
- description: Search Solana tokens by mint, symbol, or name; fetch metadata, verification status, tags, and trading metrics. Backs Jupiter's verified token list.
  name: Jupiter Tokens API
  slug: tokens-api
- description: USD pricing for up to 50 Solana tokens per request, sourced from on-chain aggregated liquidity. Used for portfolio valuation, charting, and quote previews.
  name: Jupiter Price API
  slug: price-api
- description: Create, query, and cancel on-chain trigger orders — single limit orders as well as one-cancels-the-other (OCO) and one-triggers-the-other (OTOCO) order structures.
  name: Jupiter Trigger API (Limit Orders)
  slug: trigger-api
- description: Schedule recurring (dollar-cost-averaging) swaps that execute on a time interval. Manage active DCA positions and fetch execution history.
  name: Jupiter Recurring API (DCA)
  slug: recurring-api
- description: REST interface to Jupiter Perpetuals — fetch markets, positions, funding, pricing, and build open / close / modify position transactions.
  name: Jupiter Perps API
  slug: perps-api
- description: Lending product API for supplying, borrowing, repaying, withdrawing, and executing flash loans against Jupiter Lend markets.
  name: Jupiter Lend API
  slug: lend-api
- description: Binary prediction-market API for browsing markets, fetching prices and positions, and constructing trade transactions.
  name: Jupiter Prediction API
  slug: prediction-api
- description: Public, no-key, rate-limited mirror of the Jupiter API surface intended for experimentation, demos, and low-volume integrations.
  name: Jupiter Lite API
  slug: lite-api
- description: Open-source embeddable swap widget that drops a fully-featured Jupiter swap experience into any web app with a few lines of code.
  name: Jupiter Terminal
  slug: terminal
- description: Quote and build Solana DEX-aggregator swap transactions.
  name: Jupiter Swap API
  slug: jupiter-ag-swap-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jupiter Swap API
  slug: open-jupiter-ag-swap-api
- collection_type: open
  name: Jupiter Swap API
  slug: open-jupiter-ag
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jup-ag/jupiter-quote-api-node/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupiter-ag-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupiter-ag-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jupiter-ag-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://jup.ag
- group: other
  title: ''
  type: Developers
  url: https://dev.jup.ag
- group: docs
  title: ''
  type: Documentation
  url: https://dev.jup.ag/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jup-ag
- group: company
  title: ''
  type: Twitter
  url: https://x.com/JupiterExchange
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/jup
- group: company
  title: ''
  type: Blog
  url: https://www.jup.ag/blog
created: '2026-05-23'
description: Jupiter is the liquidity infrastructure powering the majority of DeFi on Solana. It aggregates spot DEXes, runs leveraged perpetuals, supports limit orders, dollar cost averaging, lending and flash loans, prediction markets, and a token launchpad. Developers integrate via production-grade REST APIs at api.jup.ag (and the rate- limited lite-api.jup.ag) covering Swap, Tokens, Price, Lend, Trigger (limit orders), Recurring (DCA), Perps, and Prediction, all behind a single API key. Open-source SDKs and the Jupiter Terminal embed widget extend the platform to wallets, exchanges, and apps.
finops:
- name: Jupiter Ag Finops
  service_category: API
  slug: jupiter-ag-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupiter-ag.png
layout: provider
modified: '2026-05-23'
name: Jupiter
nav: Providers
network: true
overview: 'Jupiter publishes 1 API on the [APIs.io](https://apis.io/) network: Swap API. Tagged areas include Solana, DeFi, DEX Aggregator, Swap, and Perpetuals.


  Jupiter''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Jupiter Ag Plans Pricing
  plan_count: 1
  slug: jupiter-ag-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Jupiter Ag Rate Limits
  slug: jupiter-ag-rate-limits
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupiter-ag/refs/heads/main/screenshots/jupiter-ag-2026-06-20T183836.png
security:
- kind: authentication
  name: Jupiter Ag Authentication
  slug: jupiter-ag-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jupiter Ag Domain Security
  slug: jupiter-ag-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jupiter-ag
tags:
- Solana
- DeFi
- DEX Aggregator
- Swap
- Perpetuals
- Limit Orders
- DCA
- Lending
website: https://jup.ag
---
