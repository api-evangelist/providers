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
  band: agent-aware
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
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cryptoquant Agentic Access
  operation_count: 12
  slug: cryptoquant-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to the value of tokens.
  name: CryptoQuant Alt Market Data API
  slug: cryptoquant-alt-market-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Discover all available endpoints
  name: CryptoQuant Available Endpoints API
  slug: cryptoquant-available-endpoints-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Entity List of Bitcoin API with Status
  name: CryptoQuant BTC Entity Status API
  slug: cryptoquant-btc-entity-status-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: 'This endpoint returns the flows of BTC into exchange wallets for as far back as we track. We constantly keep updating new exchange wallets, which means that there can be slight modification in values '
  name: CryptoQuant BTC Exchange Flows API
  slug: cryptoquant-btc-exchange-flows-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve Fund Flow ratio, Miners' Position Index(MPI), and etc. We provide certain indicators to avoid any risks, assume upside or downside potentials, and give in
  name: CryptoQuant BTC Flow Indicator API
  slug: cryptoquant-btc-flow-indicator-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace cointains endpoints to retreive metrics related to regulated funds such as trust, including market price, market volume, market premium, and digital asset holdings. These metrics are us
  name: CryptoQuant BTC Fund Data API
  slug: cryptoquant-btc-fund-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve inter entity flows data (e.g. flow between miners and exchanges). Data entries were collected from the first transaction between two entities. We constant
  name: CryptoQuant BTC Inter Entity Flows API
  slug: cryptoquant-btc-inter-entity-flows-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve statistics on Lightning Network. We provide certain metrics such as the number of channel, nodes and network capacity from lightning network. For more det
  name: CryptoQuant BTC Lightning Statistics API
  slug: cryptoquant-btc-lightning-statistics-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to the value of Bitcoin, including price, open interest, market cap, realized cap, etc. On top of providing basic market data like price a
  name: CryptoQuant BTC Market Data API
  slug: cryptoquant-btc-market-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve MVRV(Market-Value-to-Realized-Value), Estimated Leverage Ratio, and etc. We provide certain indicators to avoid any risks, assume upside or downside poten
  name: CryptoQuant BTC Market Indicator API
  slug: cryptoquant-btc-market-indicator-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve statistics on Memory Pool in Bitcoin network. We provide certain metrics such as transaction count, total transaction size, total transaction fee on memor
  name: CryptoQuant BTC Mempool Statistics API
  slug: cryptoquant-btc-mempool-statistics-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve statistics on Bitcoin miners. We provide certain metrics such as rewards from coinbase or miners, the number of production reported from miners, the numbe
  name: CryptoQuant BTC Miner Data API
  slug: cryptoquant-btc-miner-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve data related to Bitcoin miners(i.e. mining pools and its participants). We provide metrics related to miner reserves, inflows, outflows, hashrate, revenue
  name: CryptoQuant BTC Miner Flows API
  slug: cryptoquant-btc-miner-flows-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Bitcoin on-chain network data including but not limited to token movements, fees, supply, address movements, etc. All metrics have data entries starting from the genesis block (block height 0, datetim
  name: CryptoQuant BTC Network Data API
  slug: cryptoquant-btc-network-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: 'This namespace contains endpoints to retrieve NVT ratio, Stock to Flow ratio, and etc. We provide certain indicators to avoid any risks, assume upside or downside potentials, and give insights on the '
  name: CryptoQuant BTC Network Indicator API
  slug: cryptoquant-btc-network-indicator-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Entity List of ERC20 API with Status
  name: CryptoQuant ERC20 Entity Status API
  slug: cryptoquant-erc20-entity-status-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This endpoint returns the flows of ERC20 tokens into exchange wallets for as far back as we track. Please note that the transfer generally occurs after a certain amount of time from the contract creat
  name: CryptoQuant ERC20 Exchange Flows API
  slug: cryptoquant-erc20-exchange-flows-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve entity flow based indicators. We provide certain indicators to avoid any risks, assume upside or downside potentials, and give insights on the value of bi
  name: CryptoQuant ERC20 Flow Indicator API
  slug: cryptoquant-erc20-flow-indicator-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to the value of tokens.
  name: CryptoQuant ERC20 Market Data API
  slug: cryptoquant-erc20-market-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: The ERC20 Network Data API from CryptoQuant — 6 operation(s) for erc20 network data.
  name: CryptoQuant ERC20 Network Data API
  slug: cryptoquant-erc20-network-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Genesis event of ETH 2.0 requires at least 16,384 of 32-ETH validator deposits seven days before Dec 1. If not, the genesis event would postpone seven days after. We have only valid transactions in th
  name: CryptoQuant ETH 2.0 API
  slug: cryptoquant-eth-2-0-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Entity List of Ethereum API with Status
  name: CryptoQuant ETH Entity Status API
  slug: cryptoquant-eth-entity-status-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: 'This endpoint returns the flows of ETH into exchange wallets for as far back as we track. We constantly keep updating new exchange wallets, which means that there can be slight modification in values '
  name: CryptoQuant ETH Exchange Flows API
  slug: cryptoquant-eth-exchange-flows-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve entity flow based indicators. We provide certain indicators to avoid any risks, assume upside or downside potentials, and give insights on the value of bi
  name: CryptoQuant ETH Flow Indicator API
  slug: cryptoquant-eth-flow-indicator-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace cointains endpoints to retreive metrics related to regulated funds such as trust, including market price, market volume, market premium, and digital asset holdings. These metrics are us
  name: CryptoQuant ETH Fund Data API
  slug: cryptoquant-eth-fund-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to the value of ETH including price, etc. We provide USD and USDT spot price of ETH from global exchanges and ETH index price. CryptoQuant
  name: CryptoQuant ETH Market Data API
  slug: cryptoquant-eth-market-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve Estimated Leverage Ratio. We provide certain indicators to avoid any risks, assume upside or downside potentials, and give insights on the value of ethere
  name: CryptoQuant ETH Market Indicator API
  slug: cryptoquant-eth-market-indicator-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Ethereum on-chain network data including but not limited to token movements, fees, supply, address movements, etc. All metrics have data entries starting from the genesis block (block height `0`, date
  name: CryptoQuant ETH Network Data API
  slug: cryptoquant-eth-network-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Data freshness. Append `/latency` to any v1 data endpoint to see how long after a block its data becomes collectable and fully processed.
  name: CryptoQuant Latency API
  slug: cryptoquant-latency-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Entity List of Stablecoin API with Status
  name: CryptoQuant Stablecoin Entity Status API
  slug: cryptoquant-stablecoin-entity-status-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: 'This endpoint returns the flows of Stablecoin tokens into exchange wallets for as far back as we track. Please note that the transfer generally occurs after a certain amount of time from the contract '
  name: CryptoQuant Stablecoin Exchange Flows API
  slug: cryptoquant-stablecoin-exchange-flows-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve entity flow based indicators. We provide certain indicators to avoid any risks, assume upside or downside potentials, and give insights on the value of bi
  name: CryptoQuant Stablecoin Flow Indicator API
  slug: cryptoquant-stablecoin-flow-indicator-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to the value of tokens, including price, market cap, etc.
  name: CryptoQuant Stablecoin Market Data API
  slug: cryptoquant-stablecoin-market-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoint to retrieve on-chain network data for stablecoins including token transfers, issuance, addresses, etc. The earliest data point of each token is listed as Contract Crea
  name: CryptoQuant Stablecoin Network Data API
  slug: cryptoquant-stablecoin-network-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: The TRX DEFI API from CryptoQuant — 2 operation(s) for trx defi.
  name: CryptoQuant TRX DEFI API
  slug: cryptoquant-trx-defi-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to TRX Market Data.
  name: CryptoQuant TRX Market Data API
  slug: cryptoquant-trx-market-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to TRX Network Data.
  name: CryptoQuant TRX Network Data API
  slug: cryptoquant-trx-network-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: 'This namespace contains endpoints to retrieve metrics related to XRP AMM Data. <br/> ### Supported AMM Pairs | Name | AMM Account | AMM | Status | |----------------|-------------|--------------|------'
  name: CryptoQuant XRP AMM Data API
  slug: cryptoquant-xrp-amm-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to XRP Dex.
  name: CryptoQuant XRP Dex Data API
  slug: cryptoquant-xrp-dex-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: 'This namespace contains endpoints to retrieve metrics related to XRP Entity Flows. Currently, We only supports Exchanges for available entities ### Supported Exchanges | Name | |------------| | Binanc'
  name: CryptoQuant XRP Entity Flows API
  slug: cryptoquant-xrp-entity-flows-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: The XRP Entity Status API from CryptoQuant — 1 operation(s) for xrp entity status.
  name: CryptoQuant XRP Entity Status API
  slug: cryptoquant-xrp-entity-status-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to XRP Flow Indicators.
  name: CryptoQuant XRP Flow Indicator API
  slug: cryptoquant-xrp-flow-indicator-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to XRP Market Data.
  name: CryptoQuant XRP Market Data API
  slug: cryptoquant-xrp-market-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to XRP Network Data.
  name: CryptoQuant XRP Network Data API
  slug: cryptoquant-xrp-network-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: This namespace contains endpoints to retrieve metrics related to XRP Network Indicators.
  name: CryptoQuant XRP Network Indicator API
  slug: cryptoquant-xrp-network-indicator-api
artifact_total: 61
collections:
- collection_type: open
  name: CryptoQuant Exchange Flows API
  slug: open-cryptoquant-exchange-flows-api
- collection_type: open
  name: CryptoQuant Exchange Flows Market Data API
  slug: open-cryptoquant-market-data-api
- collection_type: open
  name: CryptoQuant Exchange Flows Miner API
  slug: open-cryptoquant-miner-api
- collection_type: open
  name: CryptoQuant Exchange Flows On-Chain API
  slug: open-cryptoquant-on-chain-api
- collection_type: open
  name: CryptoQuant Exchange Flows Stablecoins API
  slug: open-cryptoquant-stablecoins-api
- collection_type: open
  name: CryptoQuant API
  slug: open-cryptoquant
common:
- group: commercial
  href: https://artifacts.apis.io/cryptoquant/plans/cryptoquant-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cryptoquant-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cryptoquant/rate-limits/cryptoquant-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cryptoquant-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cryptoquant/finops/cryptoquant-finops.yml
  title: ''
  type: FinOps
  url: finops/cryptoquant-finops.yml
- group: agent
  href: https://artifacts.apis.io/cryptoquant/agentic-access/cryptoquant-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cryptoquant-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cryptoquant/security/cryptoquant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptoquant-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cryptoquant/authentication/cryptoquant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cryptoquant-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crypto-quant
- group: company
  title: ''
  type: Website
  url: https://cryptoquant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cryptoquant.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cryptoquant.com/products/api
- group: docs
  href: https://artifacts.apis.io/cryptoquant/openapi/_original/cryptoquant-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/cryptoquant-openapi.yml
- group: docs
  href: https://artifacts.apis.io/cryptoquant/json-schema/cryptoquant-timeseries-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cryptoquant-timeseries-schema.json
- group: design
  href: https://artifacts.apis.io/cryptoquant/json-ld/cryptoquant-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/cryptoquant-context.jsonld
- group: design
  href: https://artifacts.apis.io/cryptoquant/rules/cryptoquant-rules.yml
  title: ''
  type: SpectralRules
  url: rules/cryptoquant-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptoquant/vocabulary/cryptoquant-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cryptoquant-vocabulary.yml
created: '2025-02-12'
description: CryptoQuant is a blockchain data analytics platform providing real-time and historical on-chain, exchange flow, miner, derivatives, and stablecoin metrics for Bitcoin, Ethereum, and other major cryptocurrencies. The API delivers time-series data used by traders, funds, and researchers to gauge market sentiment and capital flows.
finops:
- has_sources: false
  method: generated
  name: Cryptoquant Finops
  primary_unit: request
  service_category: API
  slug: cryptoquant-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cryptoquant.png
json_schemas:
- name: CryptoQuantTimeSeriesResponse
  property_count: 2
  slug: cryptoquant-timeseries
jsonld:
- class_count: 8
  name: Cryptoquant Context
  property_count: 8
  slug: cryptoquant-context
layout: provider
modified: '2026-05-19'
name: CryptoQuant
nav: Providers
network: true
overview: 'CryptoQuant publishes 45 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alt Market Data API, Available Endpoints API, BTC Entity Status API, and 42 more. Tagged areas include Blockchain, Cryptocurrency, On-Chain Analytics, Market Data, and Derivatives.


  The CryptoQuant catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CryptoQuant''s developer surface includes authentication, documentation, pricing, and 12 more developer resources.'
plans:
- name: Cryptoquant Plans Pricing
  plan_count: 3
  slug: cryptoquant-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Cryptoquant Rate Limits
  slug: cryptoquant-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: CryptoQuant — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cryptoquant-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: CryptoQuant API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: cryptoquant-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.4
    catalog_earned_first_party: 0.0
    catalog_gap: 49.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 7.9
    contract_governance: 27.3
    contract_quality: 62.2
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 88.2
      total: 51
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/cryptoquant/cryptoquant-2026-06-20T175316.png
security:
- kind: authentication
  name: Cryptoquant Authentication
  slug: cryptoquant-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cryptoquant Domain Security
  slug: cryptoquant-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cryptoquant
tags:
- Blockchain
- Cryptocurrency
- On-Chain Analytics
- Market Data
- Derivatives
website: https://cryptoquant.com/
---
