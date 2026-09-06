---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 50
  human_in_the_loop: 6
  name: Mexc Agentic Access
  operation_count: 142
  slug: mexc-agentic-access
  summary_line: 142 operations · 50 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: The MEXC Spot WebSocket Streams deliver real-time market data and user account updates via persistent WebSocket connections. Public channels provide ticker data, order book depth, trade feeds, and kli
  name: MEXC Spot WebSocket Streams
  slug: spot-websocket-streams
- description: The MEXC Futures WebSocket API streams real-time derivatives market data and account events over persistent WebSocket connections. Public channels include ticker data, trade transactions, order book d
  name: MEXC Futures WebSocket API
  slug: futures-websocket-api
- description: 'The MEXC Broker API enables institutional partners to manage sub-accounts and provide trading services to their users. MEXC supports three broker modes: API Broker for copy-trading and trading bot pla'
  name: MEXC Broker API
  slug: broker-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The Accounts and Transactions API from MEXC — 59 operation(s) for accounts and transactions.
  name: MEXC Accounts and Transactions API
  slug: mexc-accounts-and-transactions-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The EFT API from MEXC — 1 operation(s) for eft.
  name: MEXC EFT API
  slug: mexc-eft-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The Margin API from MEXC — 14 operation(s) for margin.
  name: MEXC Margin API
  slug: mexc-margin-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The Market Date Endpoints API from MEXC — 13 operation(s) for market date endpoints.
  name: MEXC Market Date Endpoints API
  slug: mexc-market-date-endpoints-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The Parent child account API from MEXC — 6 operation(s) for parent child account.
  name: MEXC Parent child account API
  slug: mexc-parent-child-account-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The Quote API from MEXC — 12 operation(s) for quote.
  name: MEXC Quote API
  slug: mexc-quote-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The Rebate API from MEXC — 4 operation(s) for rebate.
  name: MEXC Rebate API
  slug: mexc-rebate-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The Spot Account/Trade API from MEXC — 8 operation(s) for spot account/trade.
  name: MEXC Spot Account/Trade API
  slug: mexc-spot-account-trade-api
- baseURL: https://api.mexc.com
  baseurl_source: declared
  description: The Wallet API from MEXC — 10 operation(s) for wallet.
  name: MEXC Wallet API
  slug: mexc-wallet-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions API
  slug: open-mexc-accounts-and-transactions-api
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions EFT API
  slug: open-mexc-eft-api
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions Margin API
  slug: open-mexc-margin-api
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions Market Date Endpoints API
  slug: open-mexc-market-date-endpoints-api
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions Parent child account API
  slug: open-mexc-parent-child-account-api
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions Quote API
  slug: open-mexc-quote-api
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions Rebate API
  slug: open-mexc-rebate-api
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions Spot Account/Trade API
  slug: open-mexc-spot-account-trade-api
- collection_type: open
  name: MEXC Futures REST API v1 Accounts and Transactions Wallet API
  slug: open-mexc-wallet-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mexc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mexc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mexc-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.mexc.com/mexc-api
- group: docs
  title: ''
  type: Documentation
  url: https://mexcdevelop.github.io/apidocs/spot_v3_en/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mexc.com/api-docs/spot-v3/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mexcdevelop
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mexcdevelop/mexc-api-sdk
- group: commercial
  title: ''
  type: Plans
  url: plans/mexc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mexc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mexc-finops.yml
- group: other
  title: ''
  type: Announcements
  url: https://www.mexc.com/announcements/api-updates
- group: operate
  title: ''
  type: Status
  url: https://www.mexc.com/support/articles/17827791520875
- group: operate
  title: ''
  type: Support
  url: https://t.me/MEXC_API
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mexc-jsonld.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mexc-vocabulary.json
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.mexc.com/feed/
created: '2026-06-13'
description: MEXC is a global cryptocurrency exchange providing REST and WebSocket APIs for spot trading, perpetual futures, market data, order management, account management, and wallet operations across 1,200+ trading pairs. MEXC supports institutional users through a Broker API with sub-account management and a Market Maker Program with tiered rate limits and competitive fee schedules.
examples:
- key_count: 4
  name: Mexc Futures Place Order Example
  slug: mexc-futures-place-order-example
- key_count: 4
  name: Mexc Get Ticker Example
  slug: mexc-get-ticker-example
- key_count: 4
  name: Mexc Place Order Example
  slug: mexc-place-order-example
features:
- description: Buy and sell 1,200+ cryptocurrency pairs with limit, market, and stop-loss orders.
  name: Spot Trading
- description: Trade perpetual futures contracts with leverage via REST and WebSocket APIs.
  name: Futures Trading
- description: Real-time and historical price tickers, order book depth, klines, and funding rates.
  name: Market Data
- description: Low-latency real-time market data and account event streams.
  name: WebSocket Streams
- description: Manage deposits, withdrawals, deposit addresses, and currency information.
  name: Wallet Management
- description: Create and manage up to 30 sub-accounts per master account with independent API keys.
  name: Sub-Account Management
- description: API Broker, Independent Broker, and OAuth Broker modes for institutional partners.
  name: Broker Program
- description: Tiered market maker program with enhanced API rate limits and competitive fee rebates.
  name: Market Maker Program
finops:
- name: Mexc Finops
  service_category: Financial Services / Trading
  slug: mexc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mexc.png
json_schemas:
- name: MEXC Order
  property_count: 16
  slug: mexc-order
- name: MEXC Ticker
  property_count: 17
  slug: mexc-ticker
layout: provider
modified: '2026-06-13'
name: MEXC
nav: Providers
network: true
overview: 'MEXC publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts and Transactions API, EFT API, Margin API, and 6 more. Tagged areas include Cryptocurrency, Exchange, Trading, Futures, and Market Data.


  The MEXC catalog on APIs.io includes 1 Spectral governance ruleset.


  MEXC''s developer surface includes authentication, developer portal, documentation, getting-started guide, status page, support, and 11 more developer resources.'
plans:
- name: Mexc Plans Pricing
  plan_count: 5
  slug: mexc-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 12
  name: Mexc Rate Limits
  slug: mexc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: MEXC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mexc-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 72.3
    catalog_earned_first_party: 0.0
    catalog_gap: 42.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 50.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 34.2
  previous_composite: 46.1
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mexc/refs/heads/main/screenshots/mexc-2026-06-20T185344.png
security:
- kind: authentication
  name: Mexc Authentication
  slug: mexc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mexc Domain Security
  slug: mexc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mexc
tags:
- Cryptocurrency
- Exchange
- Trading
- Futures
- Market Data
- Finance
- Blockchain
use_cases:
- description: Build automated trading bots using MEXC REST and WebSocket APIs for spot and futures.
  name: Algorithmic Trading
- description: Aggregate real-time prices, order books, and trade feeds across 1,200+ pairs.
  name: Market Data Aggregation
- description: Track and rebalance cryptocurrency portfolios across spot and futures accounts.
  name: Portfolio Management
- description: Exploit price differences across MEXC spot and futures markets programmatically.
  name: Arbitrage Trading
- description: Build copy-trading platforms, trading bots, and wallet apps using the Broker API.
  name: Broker Integration
website: https://www.mexc.com/mexc-api
---
