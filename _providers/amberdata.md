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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.4
  scored_at: '2026-08-30'
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
- description: The Addresses API from Amberdata — 10 operation(s) for addresses.
  name: Amberdata Addresses API
  slug: amberdata-addresses-api
- description: The Analytics API from Amberdata — 73 operation(s) for analytics.
  name: Amberdata Analytics API
  slug: amberdata-analytics-api
- description: The Blocks API from Amberdata — 1 operation(s) for blocks.
  name: Amberdata Blocks API
  slug: amberdata-blocks-api
- description: The Classifications API from Amberdata — 1 operation(s) for classifications.
  name: Amberdata Classifications API
  slug: amberdata-classifications-api
- description: The Contracts API from Amberdata — 1 operation(s) for contracts.
  name: Amberdata Contracts API
  slug: amberdata-contracts-api
- description: The Depth API from Amberdata — 7 operation(s) for depth.
  name: Amberdata Depth API
  slug: amberdata-depth-api
- description: The Dex API from Amberdata — 6 operation(s) for dex.
  name: Amberdata Dex API
  slug: amberdata-dex-api
- description: The Exchanges API from Amberdata — 5 operation(s) for exchanges.
  name: Amberdata Exchanges API
  slug: amberdata-exchanges-api
- description: The Lending API from Amberdata — 10 operation(s) for lending.
  name: Amberdata Lending API
  slug: amberdata-lending-api
- description: The Liquidity API from Amberdata — 1 operation(s) for liquidity.
  name: Amberdata Liquidity API
  slug: amberdata-liquidity-api
- description: The Marketcap API from Amberdata — 1 operation(s) for marketcap.
  name: Amberdata Marketcap API
  slug: amberdata-marketcap-api
- description: The Metrics API from Amberdata — 7 operation(s) for metrics.
  name: Amberdata Metrics API
  slug: amberdata-metrics-api
- description: The Ohlcv API from Amberdata — 2 operation(s) for ohlcv.
  name: Amberdata Ohlcv API
  slug: amberdata-ohlcv-api
- description: The Prices API from Amberdata — 4 operation(s) for prices.
  name: Amberdata Prices API
  slug: amberdata-prices-api
- description: The Search API from Amberdata — 1 operation(s) for search.
  name: Amberdata Search API
  slug: amberdata-search-api
- description: The Stablecoins API from Amberdata — 1 operation(s) for stablecoins.
  name: Amberdata Stablecoins API
  slug: amberdata-stablecoins-api
- description: The Supply API from Amberdata — 2 operation(s) for supply.
  name: Amberdata Supply API
  slug: amberdata-supply-api
- description: The Tokens API from Amberdata — 6 operation(s) for tokens.
  name: Amberdata Tokens API
  slug: amberdata-tokens-api
- description: The Trade API from Amberdata — 6 operation(s) for trade.
  name: Amberdata Trade API
  slug: amberdata-trade-api
- description: The Transactions API from Amberdata — 1 operation(s) for transactions.
  name: Amberdata Transactions API
  slug: amberdata-transactions-api
- description: The Updates API from Amberdata — 1 operation(s) for updates.
  name: Amberdata Updates API
  slug: amberdata-updates-api
- description: The Volumes API from Amberdata — 2 operation(s) for volumes.
  name: Amberdata Volumes API
  slug: amberdata-volumes-api
artifact_total: 58
asyncapis:
- description: AsyncAPI 2.6 description of Amberdata's **real-time WebSocket streaming** surface. Unlike the Groq reference (which exposes no WebSocket), Amberdata DOES publish a documented public WebSocket API. Cli
  name: Amberdata WebSocket Streaming API
  slug: amberdata-asyncapi
collections:
- collection_type: postman
  name: Asset Reference & Classification API
  slug: postman-amberdata-arc
- collection_type: postman
  name: blockchain-api
  slug: postman-amberdata-blockchain
- collection_type: postman
  name: Amberdata DeFi API
  slug: postman-amberdata-defi-api
- collection_type: postman
  name: Defi Market API
  slug: postman-amberdata-defi-market
- collection_type: postman
  name: Defi API
  slug: postman-amberdata-defi
- collection_type: postman
  name: derivatives-api
  slug: postman-amberdata-derivatives
- collection_type: postman
  name: Amberdata DeFi Futures API
  slug: postman-amberdata-futures-api
- collection_type: postman
  name: market-api
  slug: postman-amberdata-market
- collection_type: postman
  name: Market Metrics
  slug: postman-amberdata-metrics
- collection_type: postman
  name: Amberdata DeFi On-Chain API
  slug: postman-amberdata-on-chain-api
- collection_type: postman
  name: Amberdata DeFi Options API
  slug: postman-amberdata-options-api
- collection_type: postman
  name: Pricing
  slug: postman-amberdata-price
- collection_type: postman
  name: Amberdata DeFi Spot API
  slug: postman-amberdata-spot-api
- collection_type: postman
  name: spot-analytics
  slug: postman-amberdata-spot
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amberdata DeFi API
  slug: open-amberdata-defi-api
- collection_type: open
  name: Amberdata DeFi Futures API
  slug: open-amberdata-futures-api
- collection_type: open
  name: Amberdata DeFi On-Chain API
  slug: open-amberdata-on-chain-api
- collection_type: open
  name: Amberdata DeFi Options API
  slug: open-amberdata-options-api
- collection_type: open
  name: Amberdata DeFi Spot API
  slug: open-amberdata-spot-api
- collection_type: open
  name: Amberdata API
  slug: open-amberdata
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amberdata/overview
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
mcp_servers:
- description: ''
  name: Amberdata MCP Server
  slug: amberdata-mcp-server
modified: '2026-07-22'
name: Amberdata
nav: Providers
network: true
overview: 'Amberdata publishes 28 APIs on the [APIs.io](https://apis.io/) network, including WebSocket Streaming API, DeFi API, Futures API, and 25 more. Tagged areas include Crypto, Blockchain, Market Data, Digital Assets, and Derivatives.


  The Amberdata catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Amberdata''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 27 more developer resources.'
plans:
- name: Amberdata Plans Pricing
  plan_count: 2
  slug: amberdata-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Amberdata Rate Limits
  slug: amberdata-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Amberdata API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: amberdata-asyncapi-spectral-rules
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 25
    catalog_gap: 48.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 15.9
    contract_quality: 62.2
    developer_ergonomics: 32.7
    discoverability: 81.5
    governance: 15.9
    operational_transparency: 65.8
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
