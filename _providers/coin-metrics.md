---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Coin Metrics Agentic Access
  operation_count: 203
  slug: coin-metrics-agentic-access
  summary_line: 203 operations · 3 acting
api_count: 19
apis:
- description: Endpoints for creating async jobs for blockchain entities.
  name: Coin Metrics Blockchain Explorer Job API
  slug: coin-metrics-blockchain-explorer-job-api
- description: Blockchain metadata endpoints
  name: Coin Metrics Blockchain Metadata API
  slug: coin-metrics-blockchain-metadata-api
- description: 'Catalog of available for your `api_key` data.<br/> Use the [Full catalog](#tag/Full-catalog) endpoints for the full list of supported by Coin Metrics data. <br/>DEPRECATED: See https://coinmetrics.io/'
  name: Coin Metrics Catalog API
  slug: coin-metrics-catalog-api
- description: Catalog of available for your `api_key` data.<br/> Use the [Full catalog V2](#tag/Full-catalog-v2) endpoints for the full list of supported by Coin Metrics data.
  name: Coin Metrics Catalog v2 API
  slug: coin-metrics-catalog-v2-api
- description: Endpoints for working with chain monitor data.
  name: Coin Metrics Chain Monitor tools API
  slug: coin-metrics-chain-monitor-tools-api
- description: Endpoints for getting the snapshots of various constituents
  name: Coin Metrics Constituent Snapshots API
  slug: coin-metrics-constituent-snapshots-api
- description: Endpoints for getting the timeframes of various constituents
  name: Coin Metrics Constituent Timeframes API
  slug: coin-metrics-constituent-timeframes-api
- description: Endpoints for fetching full blockchain entities.
  name: Coin Metrics Full blockchain entities v2 API
  slug: coin-metrics-full-blockchain-entities-v2-api
- description: The Full catalog returns the full range of data that is supported by Coin Metrics across all our products.<br/> If you are a client looking to understand the data that is available for your API key an
  name: Coin Metrics Full catalog API
  slug: coin-metrics-full-catalog-api
- description: The Full catalog returns the full range of data that is supported by Coin Metrics across all our products.<br/> If you are a client looking to understand the data that is available for your API key an
  name: Coin Metrics Full catalog v2 API
  slug: coin-metrics-full-catalog-v2-api
- description: Jobs API endpoints
  name: Coin Metrics Jobs API
  slug: coin-metrics-jobs-api
- description: Endpoints for fetching lists of blockchain entities.
  name: Coin Metrics List of blockchain entities v2 API
  slug: coin-metrics-list-of-blockchain-entities-v2-api
- description: Profile endpoints
  name: Coin Metrics Profile API
  slug: coin-metrics-profile-api
- description: Metadata information of entities supported by Coin Metrics.
  name: Coin Metrics Reference Data API
  slug: coin-metrics-reference-data-api
- description: Security Master endpoints
  name: Coin Metrics Security Master API
  slug: coin-metrics-security-master-api
- description: Taxonomy endpoints
  name: Coin Metrics Taxonomy API
  slug: coin-metrics-taxonomy-api
- description: Taxonomy Metadata endpoints
  name: Coin Metrics Taxonomy Metadata API
  slug: coin-metrics-taxonomy-metadata-api
- description: Endpoints for fetching metrics, market data, indexes and other time series data.
  name: Coin Metrics Timeseries API
  slug: coin-metrics-timeseries-api
- description: WebSocket endpoints for getting a real-time stream of metrics, market data, indexes and other time series data.
  name: Coin Metrics Timeseries stream API
  slug: coin-metrics-timeseries-stream-api
artifact_total: 25
asyncapis:
- description: WebSocket streaming surface of the Coin Metrics API v4, derived from the published OpenAPI 3.0.2 definition (timeseries-stream tag). Real-time streams of metrics, market trades, quotes, order books, c
  name: Coin Metrics Timeseries Stream API
  slug: coin-metrics-timeseries-stream-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coin-metrics-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coin-metrics-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coin-metrics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://coinmetrics.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.coinmetrics.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coinmetrics.io/access-our-data/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinmetrics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coinmetrics
- group: company
  title: ''
  type: Blog
  url: https://coinmetrics.io/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://coinmetrics.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinmetrics.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinmetrics.io/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://coinmetrics.io/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinmetrics.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coinmetrics.io/api/v4
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coinmetrics.io/getting-started
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/coin-metrics-api-v4-openapi.json
- group: build
  title: ''
  type: Packages
  url: packages/coin-metrics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coin-metrics-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/coinmetrics-api-client/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coin-metrics-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coin-metrics-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coin-metrics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coin-metrics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coin-metrics-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.coinmetrics.io/access-our-data/api#backward-compatibility
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coin-metrics-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/coin-metrics-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coin-metrics-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coin-metrics-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/coin-metrics-timeseries-stream-asyncapi.yml
created: '2026-07-21'
description: 'Coin Metrics is a Boston-based crypto financial intelligence provider founded in 2017, selling institutional-grade cryptoasset network (on-chain) data, exchange market data (trades, quotes, order books, candles, derivatives), CMBI indexes, reference rates, and reference/security-master data. Everything is delivered through a single documented API v4 - REST at api.coinmetrics.io/v4 and WebSocket streaming at wss://api.coinmetrics.io/v4 as paid, API-key products - plus a free, keyless Community API at community-api.coinmetrics.io/v4 under a CC BY-NC 4.0 license, with flat files, Python and R clients, and Google Sheets as additional delivery channels. A complete OpenAPI 3.0.2 definition is published on the docs site. Coin Metrics is now part of Talos: coinmetrics.io 301-redirects to talos.com/our-solutions/data/overview, while docs.coinmetrics.io and the api/community-api hosts remain live under the Coin Metrics brand.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coin-metrics.png
layout: provider
mcp_servers:
- description: ''
  name: coin-metrics-mcp.yml
  slug: coin-metrics-mcpyml
modified: '2026-07-22'
name: Coin Metrics
nav: Providers
network: true
overview: 'Coin Metrics publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Blockchain Explorer Job API, Blockchain Metadata API, Catalog API, and 16 more. Tagged areas include Financial, Market Data, Crypto, Blockchain, and On-Chain Data.


  The Coin Metrics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coin Metrics'' developer surface includes authentication, developer portal, documentation, engineering blog, pricing, support, API reference, and 25 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 6
  name: Coin Metrics Rate Limits
  slug: coin-metrics-rate-limits
score:
  band: developing
  composite: 57.4
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 70.7
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 60.5
  previous_composite: 57.4
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coin-metrics/refs/heads/main/screenshots/coin-metrics-2026-07-22T202257.png
security:
- kind: authentication
  name: Coin Metrics Authentication
  slug: coin-metrics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coin Metrics Domain Security
  slug: coin-metrics-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: coin-metrics
tags:
- Financial
- Market Data
- Crypto
- Blockchain
- On-Chain Data
- Indexes
- Reference Rates
- Order Book
- Real-Time
website: https://coinmetrics.io/
---
