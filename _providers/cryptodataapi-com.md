---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Cryptodataapi Com Agentic Access
  operation_count: 234
  slug: cryptodataapi-com-agentic-access
  summary_line: 234 operations · 32 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The AlgoBrain API from cryptodataapi-com — 3 operation(s) for algobrain.
  name: cryptodataapi-com Algo Brain API
  slug: cryptodataapi-com-algobrain-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: API key management — create, inspect, rotate, and revoke `cdk_live_` keys.
  name: cryptodataapi-com Authentication API
  slug: cryptodataapi-com-authentication-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Historical archives — daily snapshots, klines, funding, liquidations, and bulk Parquet downloads.
  name: cryptodataapi-com Backtesting API
  slug: cryptodataapi-com-backtesting-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Coin profiles, search, top lists, and curated category groups.
  name: cryptodataapi-com Coins API
  slug: cryptodataapi-com-coins-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: One-call daily market overview — health scores, derivatives, sentiment, macro, cycle indicators, and coin profiles. Rebuilt 20:00 UTC.
  name: cryptodataapi-com Daily Snapshot API
  slug: cryptodataapi-com-daily-snapshot-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Futures funding rates, open interest, and long/short ratios — Binance plus cross-exchange aggregates.
  name: cryptodataapi-com Derivatives API
  slug: cryptodataapi-com-derivatives-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Trending DEX pairs, new pools, and token security checks.
  name: cryptodataapi-com DEX & Meme Coins API
  slug: cryptodataapi-com-dex-meme-coins-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Forward catalyst calendar — token unlocks, macro prints, depegs — with event-risk scoring.
  name: cryptodataapi-com Event / Catalyst Regime API
  slug: cryptodataapi-com-event-catalyst-regime-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Live market events — liquidations, $1M+ whale transfers, funding prints, OI jumps — over Server-Sent Events (Pro), as recent JSON (any key), or as a keyless 30-minute-delayed preview.
  name: cryptodataapi-com Event Stream API
  slug: cryptodataapi-com-event-stream-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The Exchanges API from cryptodataapi-com — 2 operation(s) for exchanges.
  name: cryptodataapi-com Exchanges API
  slug: cryptodataapi-com-exchanges-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Policy and geopolitical shock regime with driving headlines.
  name: cryptodataapi-com Geopolitical / Policy Shock Regime API
  slug: cryptodataapi-com-geopolitical-policy-shock-regime-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Service liveness probe (no API key required).
  name: cryptodataapi-com Health API
  slug: cryptodataapi-com-health-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Hyperliquid perp market data — prices, funding, open interest, candles, L2 books.
  name: cryptodataapi-com Hyperliquid API
  slug: cryptodataapi-com-hyperliquid-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Top-trader leaderboard, wallet positions/signals/trades, watchlists, and copy signals.
  name: cryptodataapi-com Hyperliquid Traders API
  slug: cryptodataapi-com-hyperliquid-traders-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: SIGNUM RGG trend radar and the technical/structural regime screener.
  name: cryptodataapi-com Indicators API
  slug: cryptodataapi-com-indicators-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: L2 depth snapshots, OI/price divergence, and the liquidity regime classifier.
  name: cryptodataapi-com Liquidity / Market Depth API
  slug: cryptodataapi-com-liquidity-market-depth-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Spot klines, tickers, prices, and exchange info.
  name: cryptodataapi-com Market Data API
  slug: cryptodataapi-com-market-data-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Dual-score (long-term + short-term) market health system with component breakdowns and history.
  name: cryptodataapi-com Market Health API
  slug: cryptodataapi-com-market-health-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: ETF flows, liquidations, options, exchange balances, Coinbase premium, BTC cycle indicators, and more.
  name: cryptodataapi-com Market Intelligence API
  slug: cryptodataapi-com-market-intelligence-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The Market-Moving News API from cryptodataapi-com — 4 operation(s) for market-moving news.
  name: cryptodataapi-com Market-Moving News API
  slug: cryptodataapi-com-market-moving-news-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Meme/speculative lifecycle regimes and the market-wide hype score.
  name: cryptodataapi-com Meme Regime API
  slug: cryptodataapi-com-meme-regime-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The meta API from cryptodataapi-com — 1 operation(s) for meta.
  name: cryptodataapi-com Meta API
  slug: cryptodataapi-com-meta-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: NFT market overview, volume, collections, and correlations.
  name: cryptodataapi-com NFTs API
  slug: cryptodataapi-com-nfts-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Stablecoin reserves, exchange flows, miner reserves, dormancy/MVRV, and whale accumulation.
  name: cryptodataapi-com On-Chain Intelligence API
  slug: cryptodataapi-com-on-chain-intelligence-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Subscription plans, x402 agent subscribe, and invoices.
  name: cryptodataapi-com Payments API
  slug: cryptodataapi-com-payments-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The Pricing API from cryptodataapi-com — 1 operation(s) for pricing.
  name: cryptodataapi-com Pricing API
  slug: cryptodataapi-com-pricing-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: HMM regime engine — market and per-coin probabilities, trader positioning, gamma exposure, whale activity, and history.
  name: cryptodataapi-com Quant API
  slug: cryptodataapi-com-quant-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Long-horizon 10-state market-cycle taxonomy and the current detected regime.
  name: cryptodataapi-com Regimes API
  slug: cryptodataapi-com-regimes-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Hack/exploit event feed and the security regime score.
  name: cryptodataapi-com Security / Black Swan Regime API
  slug: cryptodataapi-com-security-black-swan-regime-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Fear & Greed index, macro indicators, and stablecoin supply flows.
  name: cryptodataapi-com Sentiment & Macro API
  slug: cryptodataapi-com-sentiment-macro-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The Strategies API from cryptodataapi-com — 3 operation(s) for strategies.
  name: cryptodataapi-com Strategies API
  slug: cryptodataapi-com-strategies-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The trading-strategy meta-basket catalogue.
  name: cryptodataapi-com Strategy Baskets API
  slug: cryptodataapi-com-strategy-baskets-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The Token Supply API from cryptodataapi-com — 2 operation(s) for token supply.
  name: cryptodataapi-com Token Supply API
  slug: cryptodataapi-com-token-supply-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Per-asset realized-vol regime classifier, market-wide stress score, and per-symbol detail.
  name: cryptodataapi-com Volatility Regime API
  slug: cryptodataapi-com-volatility-regime-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: The Volume Scanner API from cryptodataapi-com — 2 operation(s) for volume scanner.
  name: cryptodataapi-com Volume Scanner API
  slug: cryptodataapi-com-volume-scanner-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Wallet-signature login — challenge, verify, session.
  name: cryptodataapi-com Wallet Auth API
  slug: cryptodataapi-com-wallet-auth-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: On-chain USDC plan upgrades and invoices.
  name: cryptodataapi-com Wallet Payments API
  slug: cryptodataapi-com-wallet-payments-api
- baseURL: https://cryptodataapi.com
  baseurl_source: declared
  description: Register and manage webhook subscriptions.
  name: cryptodataapi-com Webhooks API
  slug: cryptodataapi-com-webhooks-api
artifact_total: 55
common:
- group: agent
  href: https://artifacts.apis.io/cryptodataapi-com/agentic-access/cryptodataapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cryptodataapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/cryptodataapi-com/rate-limits/cryptodataapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cryptodataapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cryptodataapi-com/plans/cryptodataapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cryptodataapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cryptodataapi-com/rules/cryptodataapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cryptodataapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptodataapi-com/json-ld/cryptodataapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cryptodataapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cryptodataapi-com/vocabulary/cryptodataapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cryptodataapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cryptodataapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cryptodataapi-com/data-model/cryptodataapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cryptodataapi-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cryptodataapi-com/changelog/cryptodataapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cryptodataapi-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/cryptodataapi-com/authentication/cryptodataapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cryptodataapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cryptodataapi-com/errors/cryptodataapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cryptodataapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cryptodataapi-com/conformance/cryptodataapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cryptodataapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cryptodataapi-com/llms/cryptodataapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptodataapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cryptodataapi-com/mcp/cryptodataapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cryptodataapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cryptodataapi-com/well-known/cryptodataapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cryptodataapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cryptodataapi-com/hosts/cryptodataapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptodataapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptodataapi-com/vendors/cryptodataapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptodataapi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptodataapi.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://cryptodataapi.com/status
- group: auth
  title: ''
  type: Security
  url: https://cryptodataapi.com/security
- group: start
  title: ''
  type: Login
  url: https://cryptodataapi.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Crypto-Data-API
- group: operate
  title: ''
  type: ChangeLog
  url: https://cryptodataapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/cryptodataapi-com/security/cryptodataapi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cryptodataapi-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cryptodataapi-com/security/cryptodataapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptodataapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptodataapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cryptodataapi.com/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cryptodataapi.com/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cryptodataapi.com/ai-agents
- group: commercial
  title: ''
  type: Pricing
  url: https://cryptodataapi.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptodataapi.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://cryptodataapi.com/blog
created: '2026-10-30'
description: Crypto Data API provides real-time cryptocurrency market data for AI agents and quant traders. It offers live prices, derivatives, funding rates, liquidations, order books, sentiment, on-chain health metrics, and quant regimes across over 190 REST endpoints. The service includes gasless USDC payments via the x402 protocol, one‑call onboarding, and a free tier with optional paid plans in USDC. Designed for AI integration, it supports high‑frequency streaming and comprehensive data coverage.
image: https://cryptodataapi.com/static/crypto-data-api-logo-new.png
json_schemas:
- name: CoinProfile
  property_count: 24
  slug: cryptodataapi-com-coin-profile
- name: CurrentRegime
  property_count: 15
  slug: cryptodataapi-com-current-regime
- name: QuantProbabilityObject
  property_count: 10
  slug: cryptodataapi-com-quant-probability-object
- name: QuantRegimeHistoryResponse
  property_count: 11
  slug: cryptodataapi-com-quant-regime-history-response
- name: SignumRggDetailResponse
  property_count: 37
  slug: cryptodataapi-com-signum-rgg-detail-response
- name: StrategyDetail
  property_count: 17
  slug: cryptodataapi-com-strategy-detail
jsonld:
- class_count: 120
  name: Cryptodataapi Com Context
  property_count: 431
  slug: cryptodataapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at cryptodataapi.com.
  name: cryptodataapi-com MCP Server
  slug: cryptodataapi-com-mcp-yml
modified: '2026-10-30'
name: cryptodataapi-com
nav: Providers
network: true
overview: 'cryptodataapi-com publishes 38 API contracts indexed on the [APIs.io](https://apis.io/) network, including Algo Brain API, Authentication API, Backtesting API, and 35 more. Tagged areas include Company, Cryptocurrency, Finance, Data, and Real-Time.


  The cryptodataapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cryptodataapi-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Cryptodataapi Com Plans Pricing
  plan_count: 1
  slug: cryptodataapi-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Cryptodataapi Com Rate Limits
  slug: cryptodataapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: cryptodataapi-com API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: cryptodataapi-com-rules
scopes:
- name: Cryptodataapi Com Scopes
  scope_count: 0
  slug: cryptodataapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 58.4
    developer_ergonomics: 29.2
    discoverability: 65.0
    operational_transparency: 55.3
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 2.6
      total: 38
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 39.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cryptodataapi-com/cryptodataapi-com-2026-11-03T125711.png
security:
- kind: authentication
  name: Cryptodataapi Com Authentication
  slug: cryptodataapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cryptodataapi Com Domain Security
  slug: cryptodataapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cryptodataapi Com Vulnerability Disclosure
  slug: cryptodataapi-com-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: daily-snapshot
  slug: cryptodataapi-com-daily-snapshot
slug: cryptodataapi-com
tags:
- Company
- Cryptocurrency
- Finance
- Data
- Real-Time
- Market Data
website: https://cryptodataapi.com/
---
