---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amberdata Agentic Access
  operation_count: 240
  slug: amberdata-agentic-access
  summary_line: 240 operations
api_count: 10
apis:
- description: Low-latency real-time WebSocket streaming over a JSON-RPC 2.0 subscribe interface for spot trades and prices, DEX data, and on-chain events, authenticated with the x-api-key header.
  name: Amberdata WebSocket Streaming API
  slug: websocket-streaming
- description: Decentralized finance (DEX and lending) data.
  name: Amberdata DeFi API
  slug: amberdata-defi-api
- description: Futures and perpetuals market data and derivatives analytics (funding rates, open interest, liquidations, basis).
  name: Amberdata Futures API
  slug: amberdata-futures-api
- description: On-chain blockchain data (blocks, transactions, addresses, tokens).
  name: Amberdata On-Chain API
  slug: amberdata-on-chain-api
- description: Options market data and volatility analytics (implied volatility, Greeks, surfaces, term structures).
  name: Amberdata Options API
  slug: amberdata-options-api
- description: Spot market analytics across supported exchanges (order-book depth, trade analytics).
  name: Amberdata Spot API
  slug: amberdata-spot-api
- description: Spot, futures, and options market data — exchanges reference, tickers, trades, OHLCV, order-book snapshots and events, funding rates, open interest, and liquidations.
  name: Amberdata Market Data API
  slug: amberdata-market-data-api
- description: Latest and historical global asset and pair prices, VWAP, TWAP, and reference rates.
  name: Amberdata Price API
  slug: amberdata-price-api
- description: Cross-market metrics and analytics series for digital assets.
  name: Amberdata Market Metrics API
  slug: amberdata-market-metrics-api
- description: Asset Reference & Classification (ARC) — reference data, classifications, and updates for digital assets.
  name: Amberdata ARC API
  slug: amberdata-arc-api
artifact_total: 19
asyncapis:
- description: AsyncAPI 2.6 description of Amberdata's **real-time WebSocket streaming** surface. Unlike the Groq reference (which exposes no WebSocket), Amberdata DOES publish a documented public WebSocket API. Cli
  name: Amberdata WebSocket Streaming API
  slug: amberdata-asyncapi
collections:
- collection_type: open
  name: Amberdata API
  slug: open-amberdata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amberdata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amberdata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amberdata-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.amberdata.io/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amberdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amberdata
- group: company
  title: ''
  type: Website
  url: https://www.amberdata.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amberdata.io
- group: commercial
  title: ''
  type: Plans
  url: plans/amberdata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amberdata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/amberdata-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amberdata.io/data-dictionary/api-specs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amberdata.io/real-time/websocket-getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@amberdata.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amberdata.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amberdata.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amberdata.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.amberdata.io
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.amberdata.io/changelog/api-changes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amberdata-changelog.yml
- group: build
  title: ''
  type: Postman
  url: collections/amberdata.postman_collection.json
- group: build
  title: ''
  type: Packages
  url: packages/amberdata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amberdata-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amberdata-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amberdata-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amberdata-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/amberdata-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amberdata-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amberdata-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amberdata-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amberdata-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amberdata-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-06-21'
description: Amberdata delivers institutional-grade digital asset and blockchain data through its REST API at https://api.amberdata.com. Coverage spans spot market data (prices, OHLCV, tickers, trades, order books), derivatives across futures and options (funding rates, open interest, liquidations, implied volatility, Greeks), DeFi (DEX trades and lending), and on-chain blockchain data (blocks, transactions, addresses, tokens, transfers), plus low-latency WebSocket streaming.
finops:
- name: Amberdata Finops
  service_category: Analytics and Data
  slug: amberdata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amberdata.png
layout: provider
modified: '2026-07-22'
name: Amberdata
nav: Providers
network: true
overview: 'Amberdata publishes 10 APIs on the [APIs.io](https://apis.io/) network, including WebSocket Streaming API, DeFi API, Futures API, and 7 more. Tagged areas include Crypto, Blockchain, Market Data, Digital Assets, and Derivatives.


  The Amberdata catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Amberdata''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 26 more developer resources.'
plans:
- name: Amberdata Plans Pricing
  plan_count: 2
  slug: amberdata-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Amberdata Rate Limits
  slug: amberdata-rate-limits
rules:
- name: Amberdata API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: amberdata-asyncapi-spectral-rules
score:
  band: strong
  composite: 62.0
  delta: 17.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.5
    developer_ergonomics: 69.6
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 76.3
  previous_composite: 44.1
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/amberdata/refs/heads/main/screenshots/amberdata-2026-07-22T202146.png
security:
- kind: authentication
  name: Amberdata Authentication
  slug: amberdata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amberdata Domain Security
  slug: amberdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amberdata
tags:
- Crypto
- Blockchain
- Market Data
- Digital Assets
- Derivatives
- DeFi
- On-Chain
website: https://www.amberdata.io
---
