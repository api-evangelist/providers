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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 90.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Polygon Agentic Access
  operation_count: 175
  slug: polygon-agentic-access
  summary_line: 175 operations
api_count: 12
apis:
- description: Real-time streaming WebSocket clusters per asset class (stocks/options/indices/forex/crypto). Subscribers authenticate with an API key and subscribe to channels for trades, quotes, aggregates, and boo
  name: Polygon WebSocket API
  slug: websocket-api
- description: Crypto aggregate bars.
  name: Polygon Aggregates API
  slug: polygon-aggregates-api
- description: Level-2 order book.
  name: Polygon Books API
  slug: polygon-books-api
- description: Option contract reference data.
  name: Polygon Contracts API
  slug: polygon-contracts-api
- description: Real-time currency conversion.
  name: Polygon Conversion API
  slug: polygon-conversion-api
- description: Stock splits and dividends.
  name: Polygon CorporateActions API
  slug: polygon-corporateactions-api
- description: Daily open/close.
  name: Polygon DailyBars API
  slug: polygon-dailybars-api
- description: Markets, exchanges, holidays, and status.
  name: Polygon Markets API
  slug: polygon-markets-api
- description: Ticker news.
  name: Polygon News API
  slug: polygon-news-api
- description: FX quote endpoints.
  name: Polygon Quotes API
  slug: polygon-quotes-api
- description: Snapshot endpoints.
  name: Polygon Snapshots API
  slug: polygon-snapshots-api
- description: Ticker reference and metadata.
  name: Polygon Tickers API
  slug: polygon-tickers-api
arazzos:
- description: Resolve a ticker, then list its stock splits and dividends history.
  name: Polygon Corporate Actions Review
  slug: polygon-corporate-actions-workflow
- description: Check market status, snapshot a crypto pair, and read its daily open/close.
  name: Polygon Crypto Daily Comparison
  slug: polygon-crypto-daily-comparison-workflow
- description: Snapshot a crypto pair, pull its aggregate bars, and read its Level-2 order book.
  name: Polygon Crypto Pair Analysis
  slug: polygon-crypto-pair-analysis-workflow
- description: Read a currency pair's last quote, convert an amount, and pull its aggregate bars.
  name: Polygon Forex Pair Analysis
  slug: polygon-forex-pair-analysis-workflow
- description: Check market status, pull grouped daily bars for all US stocks, and profile one symbol.
  name: Polygon Grouped Market Scan
  slug: polygon-grouped-market-scan-workflow
- description: Snapshot an index, pull its aggregate bars, and read its previous close.
  name: Polygon Index Analysis
  slug: polygon-index-analysis-workflow
- description: Check current US market status, then pull a stock's daily open/close and previous close.
  name: Polygon Market-Gated Stock Daily Snapshot
  slug: polygon-market-gated-stock-daily-workflow
- description: Resolve an underlying's details, scan its options chain, and read its previous close.
  name: Polygon Options Chain Scan
  slug: polygon-options-chain-scan-workflow
- description: List an underlying's option contracts, snapshot the top contract, and pull its bars.
  name: Polygon Options Contract Deep Dive
  slug: polygon-options-contract-deep-dive-workflow
- description: Resolve a stock ticker's reference details, pull its aggregate bars, and read its previous close.
  name: Polygon Stock Research
  slug: polygon-stock-research-workflow
- description: Search active stock tickers, resolve the top match's details, and pull its recent bars.
  name: Polygon Ticker Discovery and Profile
  slug: polygon-ticker-discovery-workflow
- description: Resolve a ticker's details, pull recent news, and read its previous close.
  name: Polygon Ticker News Context
  slug: polygon-ticker-news-context-workflow
artifact_total: 78
asyncapis:
- description: 'Polygon real-time market data WebSocket clusters. Each asset class (stocks, options, indices, forex, crypto) has its own dedicated cluster at `wss://socket.polygon.io/{cluster}`. Clients authenticate '
  name: Polygon WebSocket Streaming API
  slug: polygon-websocket-asyncapi
collections:
- collection_type: postman
  name: Polygon Crypto REST API
  slug: postman-polygon-crypto
- collection_type: postman
  name: Polygon Forex REST API
  slug: postman-polygon-forex
- collection_type: postman
  name: Polygon Indices REST API
  slug: postman-polygon-indices
- collection_type: postman
  name: Polygon Options REST API
  slug: postman-polygon-options
- collection_type: postman
  name: Polygon Reference REST API
  slug: postman-polygon-reference
- collection_type: postman
  name: Polygon Stocks REST API
  slug: postman-polygon-stocks
- collection_type: open
  name: Polygon Crypto REST API
  slug: open-polygon-crypto
- collection_type: open
  name: Polygon Forex REST API
  slug: open-polygon-forex
- collection_type: open
  name: Polygon Indices REST API
  slug: open-polygon-indices
- collection_type: open
  name: Polygon Options REST API
  slug: open-polygon-options
- collection_type: open
  name: Polygon Reference REST API
  slug: open-polygon-reference
- collection_type: open
  name: Polygon Stocks REST API
  slug: open-polygon-stocks
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/polygon-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/polygon-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/polygon-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/polygon-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polygon-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/polygon-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/polygon-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/polygon-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/polygon-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polygon-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/polygon-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/polygon-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/polygon-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/polygon-data-model.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/polygon-scopes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polygon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polygon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polygon-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/polygon/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-corporate-actions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-crypto-daily-comparison-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-crypto-pair-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-forex-pair-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-grouped-market-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-index-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-market-gated-stock-daily-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-options-chain-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-options-contract-deep-dive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-stock-research-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-ticker-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/polygon-ticker-news-context-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://polygon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://polygon.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://polygon.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://polygon.io/docs/getting-started
- group: start
  title: ''
  type: Signup
  url: https://polygon.io/dashboard/signup
- group: start
  title: ''
  type: Login
  url: https://polygon.io/dashboard/login
- group: commercial
  title: ''
  type: Pricing
  url: https://polygon.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.polygon.io/
- group: company
  title: ''
  type: Blog
  url: https://polygon.io/blog
- group: operate
  title: ''
  type: Support
  url: https://polygon.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://polygon.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://polygon.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/polygon-io
- group: build
  title: Official Polygon (Massive) MCP Server
  type: Tools
  url: https://github.com/polygon-io/mcp_polygon
- group: build
  title: Official PHP SDK
  type: SDKs
  url: https://github.com/polygon-io/client-php
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/polygon-api-client/
- group: build
  title: JavaScript / TypeScript SDK
  type: SDKs
  url: https://www.npmjs.com/package/@polygon.io/client-js
- group: build
  title: Kotlin / JVM SDK
  type: SDKs
  url: https://central.sonatype.com/artifact/io.polygon.kotlin.sdk/polygon-kotlin-sdk-jvm
- group: build
  title: Go SDK
  type: SDKs
  url: https://pkg.go.dev/github.com/polygon-io/client-go
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polygon-io
- group: commercial
  title: ''
  type: Plans
  url: plans/polygon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/polygon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/polygon-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/polygon-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/polygon-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/polygon-context.jsonld
created: '2026-05-28'
description: Polygon (Polygon.io, rebranded as Massive in early 2026) provides real-time and historical market data APIs across US stocks, options, indices, forex, cryptocurrencies, and futures. Coverage is delivered through REST endpoints and WebSocket streams under a single api.polygon.io surface plus an S3 flat files product, with tiered subscription plans for retail developers and Business contracts for redistribution and exchange-licensed data.
examples:
- key_count: 2
  name: Polygon Forex Conversion Example
  slug: polygon-forex-conversion-example
- key_count: 2
  name: Polygon Options Chain Snapshot Example
  slug: polygon-options-chain-snapshot-example
- key_count: 2
  name: Polygon Reference Tickers Example
  slug: polygon-reference-tickers-example
- key_count: 2
  name: Polygon Stocks Aggregate Bars Example
  slug: polygon-stocks-aggregate-bars-example
- key_count: 3
  name: Polygon Websocket Subscribe Example
  slug: polygon-websocket-subscribe-example
features:
- description: Unified REST and WebSocket surface for stocks, options, indices, forex, crypto, and futures.
  name: Multi-asset market data
- description: Sub-second live feeds plus 20+ years of historical aggregates depending on tier.
  name: Real-time and historical
- description: Dedicated streaming clusters for stocks, options, indices, forex, and crypto subscriptions.
  name: WebSocket clusters per asset class
- description: S3-style daily aggregate, trade, and quote files for bulk historical loads on paid tiers.
  name: Flat files
- description: Basic / Starter / Developer / Advanced / Business plans per asset class with distinct rate limits.
  name: Tiered subscriptions
finops:
- name: Polygon Finops
  service_category: Fintech
  slug: polygon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polygon.png
integrations:
- description: Polygon data feeds integrate with charting libraries used by trading apps.
  name: TradingView
- description: Python SDK returns DataFrames for direct use in research notebooks.
  name: Pandas and DataFrames
- description: Flat files load into modern data warehouses for SQL-based market analytics.
  name: Snowflake and Databricks
- description: WebSocket feeds bridge into Kafka, Redpanda, and Kinesis for downstream processing.
  name: Kafka and streaming platforms
json_schemas:
- name: Polygon Aggregate Bar
  property_count: 9
  slug: polygon-aggregate-bar
- name: Polygon Options Contract
  property_count: 9
  slug: polygon-options-contract
- name: Polygon NBBO Quote Tick
  property_count: 9
  slug: polygon-quote
- name: Polygon Ticker
  property_count: 12
  slug: polygon-ticker
- name: Polygon Trade Tick
  property_count: 8
  slug: polygon-trade
json_structures:
- name: Polygon Aggregate Bar Structure
  property_count: 9
  slug: polygon-aggregate-bar-structure
- name: Polygon Options Contract Structure
  property_count: 9
  slug: polygon-options-contract-structure
- name: Polygon Ticker Structure
  property_count: 12
  slug: polygon-ticker-structure
jsonld:
- class_count: 10
  name: Polygon Context
  property_count: 40
  slug: polygon-context
layout: provider
modified: '2026-07-22'
name: Polygon
nav: Providers
network: true
overview: 'Polygon publishes 12 APIs on the [APIs.io](https://apis.io/) network, including WebSocket API, Aggregates API, Books API, and 9 more. Tagged areas include Finance, Fintech, Market Data, Stocks, and Options.


  The Polygon catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Polygon''s developer surface includes changelog, authentication, developer portal, documentation, API reference, getting-started guide, signup flow, and 51 more developer resources.'
plans:
- name: Polygon Plans Pricing
  plan_count: 12
  slug: polygon-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Polygon Rate Limits
  slug: polygon-rate-limits
rules:
- name: Polygon API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: polygon-asyncapi-spectral-rules
- name: Polygon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: polygon-jsonschema-spectral-rules
- name: Polygon API Rules
  rule_count: 21
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 13
  slug: polygon-rules
scopes:
- name: Polygon Scopes
  scope_count: 6
  slug: polygon-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 75.3
  delta: 0.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 69.5
    developer_ergonomics: 87.0
    discoverability: 67.5
    governance: 65.8
    operational_transparency: 68.4
  previous_composite: 75.2
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polygon/refs/heads/main/screenshots/polygon-2026-06-20T191902.png
security:
- kind: authentication
  name: Polygon Authentication
  slug: polygon-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Polygon Domain Security
  slug: polygon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polygon
solutions:
- description: Tiered plans for consumer-facing investing apps and personal-finance tools.
  name: Retail brokerages and fintech apps
- description: Business contracts for redistribution and full SIP / OPRA / CME exchange-licensed data.
  name: Quant funds and prop trading
- description: Flat files and historical APIs for ML feature engineering and financial NLP.
  name: Data and AI research
tags:
- Finance
- Fintech
- Market Data
- Stocks
- Options
- Forex
- Crypto
- Indices
- Futures
- WebSockets
- Real-time
- Historical
- Public APIs
use_cases:
- description: Power retail and institutional trading UIs with consolidated real-time quotes and bars.
  name: Trading platform price feeds
- description: Pull decades of aggregated bars and tick data for systematic strategy research.
  name: Backtesting and research
- description: Stream live trades and quotes into compliance, surveillance, and risk engines.
  name: Risk and surveillance
- description: Build market dashboards, terminals, and embedded charts across asset classes.
  name: Analytics dashboards
- description: Drive options Greeks, volatility surfaces, and FX hedging models with reliable feeds.
  name: Quant pipelines
website: https://polygon.io/
---
