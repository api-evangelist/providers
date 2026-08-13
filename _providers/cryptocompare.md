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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cryptocompare Agentic Access
  operation_count: 54
  slug: cryptocompare-agentic-access
  summary_line: 54 operations
api_count: 18
apis:
- description: 'Single secure WebSocket endpoint multiplexing every subscription via tilde-delimited subscription strings (e.g. 5~CCCAGG~BTC~USD). Channel types: Trade (0), Ticker (2), Aggregate Index / CCCAGG (5), O'
  name: CryptoCompare Streaming WebSocket
  slug: streamer
- description: Quantitative ranking of integrated exchanges across Legal, KYC and Transaction Risk, Team, Data Provision, Asset Quality and Diversity, Market Quality, Security, and Negative Reports Penalty. Grade po
  name: CryptoCompare Exchange Benchmark
  slug: exchange-benchmark
- description: Asset metadata, overview, supply, and reference data.
  name: CryptoCompare Asset API
  slug: cryptocompare-asset-api
- description: On-chain blockchain data including history and balance distribution.
  name: CryptoCompare Blockchain API
  slug: cryptocompare-blockchain-api
- description: General coin listing, mapping, and reference metadata.
  name: CryptoCompare Coins API
  slug: cryptocompare-coins-api
- description: Exchange metadata and exchange-pair listings.
  name: CryptoCompare Exchanges API
  slug: cryptocompare-exchanges-api
- description: Futures market data across integrated derivatives venues.
  name: CryptoCompare Futures API
  slug: cryptocompare-futures-api
- description: Historical OHLCV candle data by day, hour, and minute.
  name: CryptoCompare Historical API
  slug: cryptocompare-historical-api
- description: CoinDesk Indices (CADLI, CCIX, CCIXBE) latest tick, historical values, and composition.
  name: CryptoCompare Index API
  slug: cryptocompare-index-api
- description: Crypto news articles, sources, categories, and search.
  name: CryptoCompare News API
  slug: cryptocompare-news-api
- description: On-chain blockchain metrics aggregated across chains.
  name: CryptoCompare On-Chain API
  slug: cryptocompare-on-chain-api
- description: Options market data across integrated derivatives venues.
  name: CryptoCompare Options API
  slug: cryptocompare-options-api
- description: Top-of-book order book data across integrated exchanges.
  name: CryptoCompare Order Book API
  slug: cryptocompare-order-book-api
- description: Cross-cutting overview endpoints (market cap, dominance).
  name: CryptoCompare Overview API
  slug: cryptocompare-overview-api
- description: Real-time and historical price endpoints for single and multi-symbol queries.
  name: CryptoCompare Price API
  slug: cryptocompare-price-api
- description: Social statistics for coins and assets.
  name: CryptoCompare Social API
  slug: cryptocompare-social-api
- description: Spot market data including latest tick, historical OHLCV, trades, order book L1, and instrument metadata.
  name: CryptoCompare Spot API
  slug: cryptocompare-spot-api
- description: Top list endpoints by 24h volume, market cap, exchange volume, and pair volume.
  name: CryptoCompare Top Lists API
  slug: cryptocompare-top-lists-api
arazzos:
- description: Rank assets, read one asset's detail and supply history, then search news.
  name: CryptoCompare Asset Research
  slug: cryptocompare-asset-research-workflow
- description: Resolve a coin, read its live price, full ticker, and daily OHLCV history.
  name: CryptoCompare Coin Price Snapshot
  slug: cryptocompare-coin-price-snapshot-workflow
- description: Read latest and historical social stats for a coin alongside its live price.
  name: CryptoCompare Coin Social Pulse
  slug: cryptocompare-coin-social-pulse-workflow
- description: List exchanges, read general info, then rank top exchanges for a pair.
  name: CryptoCompare Exchange Discovery
  slug: cryptocompare-exchange-discovery-workflow
- description: Rank coins by market cap, read full multi-symbol prices, then daily history.
  name: CryptoCompare Market Cap Leaders
  slug: cryptocompare-market-cap-leaders-workflow
- description: Resolve news categories and sources, then pull a filtered latest-news feed.
  name: CryptoCompare News Feed Filter
  slug: cryptocompare-news-feed-filter-workflow
- description: Confirm a market, read instrument metadata, latest tick, then daily OHLCV.
  name: CryptoCompare Spot Instrument Analysis
  slug: cryptocompare-spot-instrument-analysis-workflow
- description: Rank coins by 24h volume, pull full data, then branch into the news feed.
  name: CryptoCompare Top Volume Deep Dive
  slug: cryptocompare-top-volume-deep-dive-workflow
artifact_total: 82
asyncapis:
- description: AsyncAPI 2.6 description of the CryptoCompare (now CoinDesk) WebSocket streaming API. Clients open a single secure WebSocket to `wss://streamer.cryptocompare.com/v2` and multiplex any number of subscr
  name: CryptoCompare Streaming API
  slug: cryptocompare-asyncapi
collections:
- collection_type: postman
  name: CoinDesk Data API (CCData)
  slug: postman-cryptocompare-data-api
- collection_type: postman
  name: CryptoCompare min-api (Legacy)
  slug: postman-cryptocompare-min-api
- collection_type: open
  name: CoinDesk Data API (CCData)
  slug: open-cryptocompare-data-api
- collection_type: open
  name: CryptoCompare min-api (Legacy)
  slug: open-cryptocompare-min-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cryptocompare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cryptocompare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cryptocompare-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cryptocompare/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cryptocompare-asset-research-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cryptocompare-coin-price-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cryptocompare-coin-social-pulse-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cryptocompare-exchange-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cryptocompare-market-cap-leaders-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cryptocompare-news-feed-filter-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cryptocompare-spot-instrument-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cryptocompare-top-volume-deep-dive-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://data.coindesk.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.coindesk.com/
- group: start
  title: ''
  type: Signup
  url: https://www.cryptocompare.com/cryptopian/api-keys
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.coindesk.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.coindesk.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://data.coindesk.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://developers.coindesk.com/support
- group: company
  title: ''
  type: Blog
  url: https://data.coindesk.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CryptoCompare
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoCompare/API
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoCompare/CryptoCompareIOS
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/cryptocompare-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cryptocompare-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cryptocompare-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/cryptocompare-structure.json
- group: commercial
  title: ''
  type: Plans
  url: plans/cryptocompare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cryptocompare-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cryptocompare-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.coindesk.com/documentation/data-api/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.coindesk.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.coindesk.com/documentation/data-api/introduction
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coindesk.com
- group: operate
  title: ''
  type: Deprecation
  url: https://downloads.coindesk.com/cd3/CDI/IA/CoinDesk%20Indices_CCData_API_Migration_Guide.pdf
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cryptocompare-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cryptocompare-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cryptocompare-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cryptocompare-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cryptocompare-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/cryptocompare-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cryptocompare-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cryptocompare-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cryptocompare-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/cryptocompare-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cryptocompare-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-28'
description: 'CryptoCompare (now CoinDesk Data / CCData, acquired by CoinDesk in late 2024) is a long-standing crypto market data aggregator covering 300+ exchanges, 10,000+ assets, and 300,000+ trading pairs. The platform exposes two REST API surfaces — the legacy min-api.cryptocompare.com (Price, Historical OHLCV, Top Lists, News, Social, Order Book, Exchanges, Blockchain) and the modern data-api.cryptocompare.com / CoinDesk Data API (Spot, Index / Reference Rates including CADLI and CCIX, Asset, News, On-Chain, Futures, Options, Overview) — plus a unified WebSocket streamer at wss://streamer.cryptocompare.com/v2 that multiplexes Trade, Ticker, CCCAGG aggregate index, Order Book L2 updates and snapshots, Full Volume, Top Tier Full Volume, OHLC Candles, and Top of Book channels. Authentication uses an API key supplied as the api_key query parameter or as an `Authorization: Apikey {key}` header. Access is metered by monthly call credits with per-second / per-minute / per-hour / per-day ceilings;
  the Free tier issues 100,000 monthly credits and commercial Starter / Professional / Enterprise tiers escalate credit budgets, history depth, and surface coverage (news, social, on-chain, derivatives, full streamer, on-demand bulk exports, reference-rate licensing).'
examples:
- key_count: 2
  name: Cryptocompare Gethistoricaldailyohlcv Example
  slug: cryptocompare-getHistoricalDailyOHLCV-example
- key_count: 2
  name: Cryptocompare Getindexlatesttick Example
  slug: cryptocompare-getIndexLatestTick-example
- key_count: 2
  name: Cryptocompare Getlatestnewsarticles Example
  slug: cryptocompare-getLatestNewsArticles-example
- key_count: 2
  name: Cryptocompare Getsinglesymbolprice Example
  slug: cryptocompare-getSingleSymbolPrice-example
- key_count: 2
  name: Cryptocompare Gettoplistbytotalvolumefull Example
  slug: cryptocompare-getTopListByTotalVolumeFull-example
features:
- description: Default price source aggregating across 300+ integrated exchanges with outlier filtering.
  name: Cross-exchange aggregate index (CCCAGG)
- description: Regulated index methodology suitable for derivatives settlement and institutional mark-to-market.
  name: Institutional reference rates (CADLI, CCIX)
- description: Single secure socket multiplexes Trade, Ticker, CCCAGG, Order Book L2, OHLC, and Top of Book channels.
  name: Real-time WebSocket streamer
- description: Crypto-native news across hundreds of sources with category tagging and POSITIVE / NEUTRAL / NEGATIVE sentiment.
  name: News aggregation with sentiment
- description: Aggregated Twitter, Reddit, Facebook, and source-repo engagement metrics.
  name: Per-coin social statistics
- description: Transaction count, active addresses, hashrate, difficulty, and balance distribution across 30+ chains.
  name: On-chain blockchain data
- description: Quantitative exchange ranking (AA / A / B / C / D / E / F) across Legal, KYC, Security, and Market Quality dimensions.
  name: Exchange Benchmark grading
finops:
- name: Cryptocompare Finops
  service_category: Data Services
  slug: cryptocompare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cryptocompare.png
integrations:
- description: Pull CryptoCompare data into spreadsheets via the Apipheny add-on.
  name: Apipheny / Google Sheets
- description: Community Chainlink adapter wraps CryptoCompare endpoints for oracle consumption.
  name: Chainlink External Adapters
- description: Charting libraries and React TradingView integrations consume the CryptoCompare WebSocket for live charts.
  name: TradingView
- description: Community Node-RED nodes wrap CryptoCompare endpoints for low-code automation.
  name: Node-RED
- description: WebSocket streamer is commonly fanned out into Kafka topics for analytics.
  name: Apache Kafka / streaming pipelines
json_schemas:
- name: CCData Asset
  property_count: 24
  slug: cryptocompare-asset
- name: CryptoCompare Blockchain Data Point
  property_count: 17
  slug: cryptocompare-blockchaindatapoint
- name: CryptoCompare Coin List Entry
  property_count: 17
  slug: cryptocompare-coinlistentry
- name: CryptoCompare Exchange
  property_count: 15
  slug: cryptocompare-exchange
- name: CryptoCompare Full Ticker
  property_count: 42
  slug: cryptocompare-fullticker
- name: CoinDesk Index Tick (CADLI / CCIX / CCIXBE)
  property_count: 30
  slug: cryptocompare-indextick
- name: CryptoCompare News Article
  property_count: 23
  slug: cryptocompare-newsarticle
- name: CryptoCompare OHLCV Candle
  property_count: 9
  slug: cryptocompare-ohlcvcandle
- name: CryptoCompare Order Book Top
  property_count: 12
  slug: cryptocompare-orderbookl1
- name: CryptoCompare Social Stats
  property_count: 6
  slug: cryptocompare-socialstats
json_structures:
- name: Cryptocompare Structure
  property_count: 0
  slug: cryptocompare-structure
jsonld:
- class_count: 0
  name: Cryptocompare Context
  property_count: 7
  slug: cryptocompare-context
layout: provider
mcp_servers:
- description: ''
  name: cryptocompare-mcp.yml
  slug: cryptocompare-mcpyml
modified: '2026-07-22'
name: CryptoCompare
nav: Providers
network: true
overview: 'CryptoCompare publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Streaming WebSocket, Asset API, Blockchain API, and 14 more. Tagged areas include Cryptocurrency, Market Data, Reference Rates, News, and Social.


  The CryptoCompare catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  CryptoCompare''s developer surface includes authentication, developer portal, signup flow, pricing, support, engineering blog, documentation, and 41 more developer resources.'
plans:
- name: Cryptocompare Plans Pricing
  plan_count: 4
  slug: cryptocompare-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 11
  name: Cryptocompare Rate Limits
  slug: cryptocompare-rate-limits
rules:
- name: CryptoCompare API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: cryptocompare-asyncapi-spectral-rules
- name: CryptoCompare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cryptocompare-jsonschema-spectral-rules
- name: CryptoCompare API Rules
  rule_count: 16
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 6
  slug: cryptocompare-rules
score:
  band: exemplar
  composite: 71.6
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 77.8
    developer_ergonomics: 73.4
    discoverability: 87.0
    governance: 63.5
    operational_transparency: 60.5
  previous_composite: 71.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cryptocompare/refs/heads/main/screenshots/cryptocompare-2026-06-20T175310.png
security:
- kind: authentication
  name: Cryptocompare Authentication
  slug: cryptocompare-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Cryptocompare Domain Security
  slug: cryptocompare-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cryptocompare
solutions:
- description: Price, Ticker, Order Book, and OHLC streaming for live trading interfaces.
  name: Real-time market data
- description: Minute / hour / day OHLCV history plus tick-level history for institutional tiers.
  name: Historical and reference data
- description: CADLI / CCIX / CCIXBE for regulated mark-to-market and settlement.
  name: Indices and reference rates
- description: Aggregated crypto news with sentiment, source feeds, and category taxonomy.
  name: News and research
- description: Chain-level supply, address, and transaction metrics for analytics platforms.
  name: On-chain and analytics
tags:
- Cryptocurrency
- Market Data
- Reference Rates
- News
- Social
- Blockchain
- On-Chain
- Order Book
- Streaming
- Index
use_cases:
- description: Aggregate CCCAGG prices into consumer apps and dashboards.
  name: Retail price ticker and portfolio dashboard
- description: Pull minute / hour / day OHLCV history for systematic strategy research.
  name: Trading strategy backtest
- description: Value digital-asset books against CADLI reference rates.
  name: Institutional mark-to-market
- description: Settle futures and options against CCIX index family.
  name: Derivatives settlement
- description: Build sentiment-tagged news products and research dashboards.
  name: Crypto news aggregator
- description: Drive treasury, supply, and address dashboards across major chains.
  name: On-chain analytics
- description: Use the Exchange Benchmark to qualify integrated venues.
  name: Exchange selection and risk monitoring
website: https://data.coindesk.com/
---
