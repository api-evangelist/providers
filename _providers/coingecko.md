---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Coingecko Agentic Access
  operation_count: 68
  slug: coingecko-agentic-access
  summary_line: 68 operations
api_count: 4
apis:
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: List all asset platforms (blockchains) supported by CoinGecko.
  name: CoinGecko Asset Platforms API
  slug: coingecko-asset-platforms-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: List cryptocurrency categories and their market data.
  name: CoinGecko Categories API
  slug: coingecko-categories-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Comprehensive coin data including current prices, market data, historical data, tickers, and OHLCV charts.
  name: CoinGecko Coins API
  slug: coingecko-coins-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Public company cryptocurrency holdings data.
  name: CoinGecko Companies API
  slug: coingecko-companies-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Query coin data by contract address on a specific asset platform.
  name: CoinGecko Contract API
  slug: coingecko-contract-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Derivatives market data including tickers and exchange information.
  name: CoinGecko Derivatives API
  slug: coingecko-derivatives-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: List decentralized exchanges on specific networks.
  name: CoinGecko DEXes API
  slug: coingecko-dexes-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: BTC exchange rates against other currencies.
  name: CoinGecko Exchange Rates API
  slug: coingecko-exchange-rates-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Exchange data including volumes, tickers, and status updates.
  name: CoinGecko Exchanges API
  slug: coingecko-exchanges-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Global cryptocurrency and DeFi market data.
  name: CoinGecko Global API
  slug: coingecko-global-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: List and query supported blockchain networks.
  name: CoinGecko Networks API
  slug: coingecko-networks-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Open, High, Low, Close, Volume candlestick chart data for liquidity pools.
  name: CoinGecko OHLCV API
  slug: coingecko-ohlcv-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Check API server status
  name: CoinGecko Ping API
  slug: coingecko-ping-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Query liquidity pool data including specific pools, top pools, new pools, and multi-pool lookups.
  name: CoinGecko Pools API
  slug: coingecko-pools-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Search for coins, exchanges, and categories.
  name: CoinGecko Search API
  slug: coingecko-search-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Simple price and token price lookups without the overhead of full coin data responses.
  name: CoinGecko Simple API
  slug: coingecko-simple-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Token list endpoints for paid plan subscribers providing standardized token lists by asset platform.
  name: CoinGecko Token Lists API
  slug: coingecko-token-lists-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Query token data by contract address including price, volume, top pools, and token information.
  name: CoinGecko Tokens API
  slug: coingecko-tokens-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Recent trade data for specific liquidity pools.
  name: CoinGecko Trades API
  slug: coingecko-trades-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Trending coins, NFTs, and categories on CoinGecko.
  name: CoinGecko Trending API
  slug: coingecko-trending-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: Discover trending liquidity pools across networks based on web visits and onchain activity.
  name: CoinGecko Trending Pools API
  slug: coingecko-trending-pools-api
- baseURL: https://api.coingecko.com/api/v3
  baseurl_source: declared
  description: NFT collection data including floor prices and market information.
  name: CoinGecko NF Ts API
  slug: coingecko-nfts-api
- baseURL: https://pro-api.coingecko.com/api/v3
  baseurl_source: declared
  description: The Entities API from CoinGecko — 1 operation(s) for entities.
  name: CoinGecko Entities API
  slug: coingecko-entities-api
- baseURL: https://pro-api.coingecko.com/api/v3
  baseurl_source: declared
  description: The Insights API from CoinGecko — 1 operation(s) for insights.
  name: CoinGecko Insights API
  slug: coingecko-insights-api
- baseURL: https://pro-api.coingecko.com/api/v3
  baseurl_source: declared
  description: The Key API from CoinGecko — 1 operation(s) for key.
  name: CoinGecko Key API
  slug: coingecko-key-api
- baseURL: https://pro-api.coingecko.com/api/v3
  baseurl_source: declared
  description: The News API from CoinGecko — 1 operation(s) for news.
  name: CoinGecko News API
  slug: coingecko-news-api
- baseURL: https://pro-api.coingecko.com/api/v3
  baseurl_source: declared
  description: The Public Treasury API from CoinGecko — 4 operation(s) for public treasury.
  name: CoinGecko Public Treasury API
  slug: coingecko-public-treasury-api
- baseURL: https://pro-api.coingecko.com/api/v3
  baseurl_source: declared
  description: The Rwas API from CoinGecko — 7 operation(s) for rwas.
  name: CoinGecko Rwas API
  slug: coingecko-rwas-api
- baseURL: https://pro-api.coingecko.com/api/v3
  baseurl_source: declared
  description: The On Chain API from CoinGecko — 38 operation(s) for on chain.
  name: CoinGecko On Chain API
  slug: coingecko-on-chain-api
artifact_total: 93
asyncapis:
- description: 'Real-time cryptocurrency price streaming via WebSocket. ## Authentication Required To use this WebSocket, you need a CoinGecko Pro API key.'
  name: CoinGecko WebSocket API
  slug: coingecko-asyncapi
collections:
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms API
  slug: postman-coingecko-asset-platforms-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Categories API
  slug: postman-coingecko-categories-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Coins API
  slug: postman-coingecko-coins-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Companies API
  slug: postman-coingecko-companies-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Contract API
  slug: postman-coingecko-contract-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Derivatives API
  slug: postman-coingecko-derivatives-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms DEXes API
  slug: postman-coingecko-dexes-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Exchange Rates API
  slug: postman-coingecko-exchange-rates-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Exchanges API
  slug: postman-coingecko-exchanges-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Global API
  slug: postman-coingecko-global-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Networks API
  slug: postman-coingecko-networks-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms NFTs API
  slug: postman-coingecko-nfts-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms OHLCV API
  slug: postman-coingecko-ohlcv-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Ping API
  slug: postman-coingecko-ping-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Pools API
  slug: postman-coingecko-pools-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Search API
  slug: postman-coingecko-search-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Simple API
  slug: postman-coingecko-simple-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Token Lists API
  slug: postman-coingecko-token-lists-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Tokens API
  slug: postman-coingecko-tokens-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Trades API
  slug: postman-coingecko-trades-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Trending API
  slug: postman-coingecko-trending-api
- collection_type: postman
  name: CoinGecko Crypto Market Data Asset Platforms Trending Pools API
  slug: postman-coingecko-trending-pools-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms API
  slug: open-coingecko-asset-platforms-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Categories API
  slug: open-coingecko-categories-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Coins API
  slug: open-coingecko-coins-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Companies API
  slug: open-coingecko-companies-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Contract API
  slug: open-coingecko-contract-api
- collection_type: open
  name: CoinGecko Crypto Market Data API
  slug: open-coingecko-crypto-market-data-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Derivatives API
  slug: open-coingecko-derivatives-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms DEXes API
  slug: open-coingecko-dexes-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Exchange Rates API
  slug: open-coingecko-exchange-rates-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Exchanges API
  slug: open-coingecko-exchanges-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Global API
  slug: open-coingecko-global-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Networks API
  slug: open-coingecko-networks-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms NFTs API
  slug: open-coingecko-nfts-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms OHLCV API
  slug: open-coingecko-ohlcv-api
- collection_type: open
  name: CoinGecko Onchain DEX API
  slug: open-coingecko-onchain-dex-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Ping API
  slug: open-coingecko-ping-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Pools API
  slug: open-coingecko-pools-api
- collection_type: open
  name: CoinGecko Pro API
  slug: open-coingecko-pro-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Search API
  slug: open-coingecko-search-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Simple API
  slug: open-coingecko-simple-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Token Lists API
  slug: open-coingecko-token-lists-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Tokens API
  slug: open-coingecko-tokens-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Trades API
  slug: open-coingecko-trades-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Trending API
  slug: open-coingecko-trending-api
- collection_type: open
  name: CoinGecko Crypto Market Data Asset Platforms Trending Pools API
  slug: open-coingecko-trending-pools-api
common:
- group: other
  href: https://artifacts.apis.io/coingecko/capabilities/coingecko-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/coingecko-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/coingecko/plans/coingecko-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coingecko-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/coingecko/rate-limits/coingecko-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coingecko-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coingecko/finops/coingecko-finops.yml
  title: ''
  type: FinOps
  url: finops/coingecko-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/coingecko/overview
- group: agent
  href: https://artifacts.apis.io/coingecko/agentic-access/coingecko-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coingecko-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/coingecko/security/coingecko-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coingecko-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/coingecko/authentication/coingecko-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coingecko-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coingecko
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coingecko
- group: start
  title: ''
  type: Portal
  url: https://www.coingecko.com/en/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coingecko.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coingecko.com/en/api/pricing
- group: company
  title: ''
  type: Website
  url: https://www.coingecko.com
- group: company
  title: ''
  type: Blog
  url: https://blog.coingecko.com
- group: operate
  title: ''
  type: Support
  url: https://support.coingecko.com
- group: start
  title: ''
  type: Login
  url: https://www.coingecko.com/en/developers/dashboard
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coingecko.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coingecko.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coingecko.com/en/privacy
- group: docs
  href: https://artifacts.apis.io/coingecko/json-schema/coingecko-coin-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/coingecko-coin-schema.json
- group: docs
  href: https://artifacts.apis.io/coingecko/json-schema/coingecko-pool-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/coingecko-pool-schema.json
- group: design
  href: https://artifacts.apis.io/coingecko/json-ld/coingecko-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coingecko-context.jsonld
- group: design
  href: https://artifacts.apis.io/coingecko/rules/coingecko-rules.yml
  title: ''
  type: Spectral Ruleset
  url: rules/coingecko-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.coingecko.com/llms.txt
created: '2026-03-20'
description: 'CoinGecko is a cryptocurrency data aggregator providing market data, analytics, and information on thousands of crypto assets, exchanges, derivatives, NFTs, and on-chain decentralized markets worldwide. The CoinGecko Developer Platform exposes three primary APIs: the public Crypto Market Data API (Demo plan and free tier), the commercial Pro API for higher rate limits and exclusive endpoints, and the Onchain DEX API powered by GeckoTerminal for decentralized exchange data across 250+ networks. Authentication uses x-cg-demo-api-key (Demo) or x-cg-pro-api-key (Pro) headers, with rate limits ranging from 30 calls per minute on Demo to 1,000 calls per minute on top Pro tiers.'
finops:
- has_sources: true
  method: derived
  name: Coingecko Finops
  primary_unit: subscription
  service_category: ''
  slug: coingecko-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coingecko.png
json_schemas:
- name: CoinGecko Coin
  property_count: 17
  slug: coingecko-coin
- name: CoinGecko Onchain Liquidity Pool
  property_count: 4
  slug: coingecko-pool
jsonld:
- class_count: 0
  name: Coingecko Context
  property_count: 7
  slug: coingecko-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.api.coingecko.com over HTTP.
  name: CoinGecko MCP Server
  slug: coingecko
- description: Remote MCP server at mcp.coingecko.com over HTTP.
  name: CoinGecko MCP Server
  slug: coingecko-2
- description: Remote MCP server at mcp.pro-api.coingecko.com over HTTP.
  name: CoinGecko MCP Server
  slug: coingecko-3
modified: '2026-05-29'
name: CoinGecko
nav: Providers
network: true
overview: 'CoinGecko publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Asset Platforms API, Categories API, Coins API, and 26 more. Tagged areas include CoinGecko, Aggregator, Blockchain, Cryptocurrency, and Decentralized Exchanges.


  The CoinGecko catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  CoinGecko''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, and 19 more developer resources.'
plans:
- name: Coingecko Plans Pricing
  plan_count: 10
  slug: coingecko-plans-pricing
- name: Coingecko Price Estimates
  plan_count: 0
  slug: coingecko-price-estimates
random_paper: 10
rate_limits:
- limit_count: 9
  name: Coingecko Rate Limits
  slug: coingecko-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: CoinGecko — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: coingecko-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: CoinGecko — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: coingecko-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: CoinGecko API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 5
  slug: coingecko-rules
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 67.5
    catalog_earned_first_party: 12.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 77.6
    contract_governance: 13.6
    contract_quality: 59.4
    developer_ergonomics: 36.9
    discoverability: 80.0
    operational_transparency: 26.3
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 54
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/coingecko/coingecko-2026-06-20T174737.png
security:
- kind: authentication
  name: Coingecko Authentication
  slug: coingecko-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Coingecko Domain Security
  slug: coingecko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coingecko
tags:
- CoinGecko
- Aggregator
- Blockchain
- Cryptocurrency
- Decentralized Exchanges
- DeFi
- Decentralized Exchange
- Liquidity Pools
- Market Data
- NFT
- On-Chain Data
- Prices
- Real-Time
website: https://www.coingecko.com
---
