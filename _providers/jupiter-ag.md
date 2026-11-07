---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Jupiter Ag Agentic Access
  operation_count: 2
  slug: jupiter-ag-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
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
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Events API from Jupiter — 6 operation(s) for events.
  name: Jupiter Events API
  slug: jupiter-ag-events-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Forecast API from Jupiter — 1 operation(s) for forecast.
  name: Jupiter Forecast API
  slug: jupiter-ag-forecast-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The History API from Jupiter — 1 operation(s) for history.
  name: Jupiter History API
  slug: jupiter-ag-history-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Leaderboards API from Jupiter — 1 operation(s) for leaderboards.
  name: Jupiter Leaderboards API
  slug: jupiter-ag-leaderboards-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Markets API from Jupiter — 3 operation(s) for markets.
  name: Jupiter Markets API
  slug: jupiter-ag-markets-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Orderbook API from Jupiter — 1 operation(s) for orderbook.
  name: Jupiter Orderbook API
  slug: jupiter-ag-orderbook-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Orders API from Jupiter — 4 operation(s) for orders.
  name: Jupiter Orders API
  slug: jupiter-ag-orders-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Positions API from Jupiter — 3 operation(s) for positions.
  name: Jupiter Positions API
  slug: jupiter-ag-positions-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Profile API from Jupiter — 2 operation(s) for profile.
  name: Jupiter Profile API
  slug: jupiter-ag-profile-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Trades API from Jupiter — 1 operation(s) for trades.
  name: Jupiter Trades API
  slug: jupiter-ag-trades-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Trading API from Jupiter — 1 operation(s) for trading.
  name: Jupiter Trading API
  slug: jupiter-ag-trading-api
- baseURL: https://api.jup.ag/swap
  baseurl_source: declared
  description: The Vault API from Jupiter — 1 operation(s) for vault.
  name: Jupiter Vault API
  slug: jupiter-ag-vault-api
artifact_total: 31
collections:
- collection_type: open
  name: Jupiter Swap API
  slug: open-jupiter-ag-swap-api
- collection_type: open
  name: Jupiter Swap API
  slug: open-jupiter-ag
common:
- group: commercial
  href: https://artifacts.apis.io/jupiter-ag/plans/jupiter-ag-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jupiter-ag-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/jupiter-ag/rate-limits/jupiter-ag-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jupiter-ag-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jupiter-ag/finops/jupiter-ag-finops.yml
  title: ''
  type: FinOps
  url: finops/jupiter-ag-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jup-ag/jupiter-quote-api-node/issues
- group: agent
  href: https://artifacts.apis.io/jupiter-ag/agentic-access/jupiter-ag-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jupiter-ag-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/jupiter-ag/security/jupiter-ag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jupiter-ag-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jupiter-ag/authentication/jupiter-ag-authentication.yml
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
- has_sources: false
  method: generated
  name: Jupiter Ag Finops
  primary_unit: ''
  service_category: API
  slug: jupiter-ag-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupiter-ag.png
layout: provider
modified: '2026-05-23'
name: Jupiter
nav: Providers
network: true
overview: 'Jupiter publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Events API, Forecast API, History API, and 19 more. Tagged areas include Solana, DeFi, DEX Aggregator, Swap, and Perpetuals.


  The Jupiter catalog on APIs.io includes 1 Spectral governance ruleset.


  Jupiter''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Jupiter Ag Plans Pricing
  plan_count: 1
  slug: jupiter-ag-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Jupiter Ag Rate Limits
  slug: jupiter-ag-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Jupiter API Rules
  rule_count: 60
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 3
  slug: jupiter-ag-rules
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 51.5
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 85.7
      total: 14
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jupiter-ag/jupiter-ag-2026-06-20T183836.png
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
