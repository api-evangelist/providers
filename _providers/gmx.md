---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 19.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Gmx Agentic Access
  operation_count: 37
  slug: gmx-agentic-access
  summary_line: 37 operations · 13 acting
api_count: 1
apis:
- description: Stable, read-only REST API providing oracle prices, market information, liquidity snapshots, APY data, and GM/GLV token info for Arbitrum, Avalanche, Botanix, and MegaETH. Primary endpoints live at {c
  name: GMX Oracle API
  slug: oracle-api
- description: Historical on-chain data for GMX via Subsquid-powered GraphQL endpoints. Enables deep queries over trades, liquidity events, positions, and protocol metrics indexed from Arbitrum and Avalanche chains.
  name: GMX GraphQL API
  slug: graphql-api
- description: CoinGecko-compatible trading pairs API for GMX markets on Arbitrum and Avalanche, returning ticker IDs, base and target currencies, product type (Spot or Perpetual), last price, 24-hour high/low, base
  name: GMX Integration API
  slug: integration-api
- description: 'Official @gmx-io/sdk package shipping two clients: GmxSdk (SDK v1) for full read/write access via RPC, and GmxApiSdk (SDK v2) for lightweight read-only HTTP access covering markets, tickers, tokens, p'
  name: GMX TypeScript SDK
  slug: typescript-sdk
- description: The Allowances API from GMX — 1 operation(s) for allowances.
  name: GMX Allowances API
  slug: gmx-allowances-api
- description: The APY API from GMX — 1 operation(s) for apy.
  name: GMX APY API
  slug: gmx-apy-api
- description: The Balances API from GMX — 1 operation(s) for balances.
  name: GMX Balances API
  slug: gmx-balances-api
- description: The Buyback API from GMX — 1 operation(s) for buyback.
  name: GMX Buyback API
  slug: gmx-buyback-api
- description: The GMX Account API from GMX — 4 operation(s) for gmx account.
  name: GMX GMX Account API
  slug: gmx-gmx-account-api
- description: The JIT API from GMX — 2 operation(s) for jit.
  name: GMX JIT API
  slug: gmx-jit-api
- description: The Markets API from GMX — 5 operation(s) for markets.
  name: GMX Markets API
  slug: gmx-markets-api
- description: The Order Transactions API from GMX — 6 operation(s) for order transactions.
  name: GMX Order Transactions API
  slug: gmx-order-transactions-api
- description: The Orders API from GMX — 2 operation(s) for orders.
  name: GMX Orders API
  slug: gmx-orders-api
- description: The Pairs API from GMX — 1 operation(s) for pairs.
  name: GMX Pairs API
  slug: gmx-pairs-api
- description: The Performance API from GMX — 2 operation(s) for performance.
  name: GMX Performance API
  slug: gmx-performance-api
- description: The Positions API from GMX — 2 operation(s) for positions.
  name: GMX Positions API
  slug: gmx-positions-api
- description: The Prices API from GMX — 1 operation(s) for prices.
  name: GMX Prices API
  slug: gmx-prices-api
- description: The Rates API from GMX — 1 operation(s) for rates.
  name: GMX Rates API
  slug: gmx-rates-api
- description: The Staking API from GMX — 1 operation(s) for staking.
  name: GMX Staking API
  slug: gmx-staking-api
- description: The Subaccounts API from GMX — 2 operation(s) for subaccounts.
  name: GMX Subaccounts API
  slug: gmx-subaccounts-api
- description: The Tokens API from GMX — 2 operation(s) for tokens.
  name: GMX Tokens API
  slug: gmx-tokens-api
- description: The Trades API from GMX — 2 operation(s) for trades.
  name: GMX Trades API
  slug: gmx-trades-api
artifact_total: 159
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances API'
  slug: open-gmx-allowances-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances APY API'
  slug: open-gmx-apy-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Balances API'
  slug: open-gmx-balances-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Buyback API'
  slug: open-gmx-buyback-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances GMX Account API'
  slug: open-gmx-gmx-account-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances JIT API'
  slug: open-gmx-jit-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Markets API'
  slug: open-gmx-markets-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Order Transactions API'
  slug: open-gmx-order-transactions-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Orders API'
  slug: open-gmx-orders-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Pairs API'
  slug: open-gmx-pairs-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Performance API'
  slug: open-gmx-performance-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Positions API'
  slug: open-gmx-positions-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Prices API'
  slug: open-gmx-prices-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Rates API'
  slug: open-gmx-rates-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Staking API'
  slug: open-gmx-staking-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Subaccounts API'
  slug: open-gmx-subaccounts-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Tokens API'
  slug: open-gmx-tokens-api
- collection_type: open
  name: '@gmx-io/gmx-public-api Allowances Trades API'
  slug: open-gmx-trades-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gmx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gmx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gmx.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gmx.io/docs/api/overview/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gmx-io
- group: company
  title: ''
  type: Twitter
  url: https://x.com/GMX_IO
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/ymN38YefH9
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@gmx.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.gmx.io/docs/ai-agents/overview/
created: '2026-06-14'
description: 'GMX is a decentralized perpetual and spot exchange deployed on Arbitrum, Avalanche, Botanix, and MegaETH, supporting trades with up to 100x leverage and low-price-impact token swaps powered by oracle-based pricing. The platform exposes four integration surfaces: a GMX REST API (primary, OpenAPI-documented) for account data, orders, analytics, and relayed workflows; an Oracle API (stable) for oracle prices, markets, liquidity snapshots, and APY; a GraphQL API via Subsquid for historical on-chain data; and an MCP server plus TypeScript SDK for AI-agent and programmatic access. Data coverage includes markets, tickers, tokens, positions, orders, rates, APY, performance, wallet balances, GLP/GM/GLV token analytics, OHLCV, buyback stats, and staking power.'
examples:
- key_count: 7
  name: Cancelprepare
  slug: CancelPrepare
- key_count: 7
  name: Collateralprepare
  slug: CollateralPrepare
- key_count: 7
  name: Editprepare
  slug: EditPrepare
- key_count: 7
  name: Fetchstatus
  slug: FetchStatus
- key_count: 7
  name: Getallowances
  slug: GetAllowances
- key_count: 7
  name: Getannualized
  slug: GetAnnualized
- key_count: 7
  name: Getapy
  slug: GetApy
- key_count: 7
  name: Getliquidityhistory
  slug: GetLiquidityHistory
- key_count: 7
  name: Getliquidityinfo
  slug: GetLiquidityInfo
- key_count: 7
  name: Getmarkets
  slug: GetMarkets
- key_count: 7
  name: Getmarketsconfig
  slug: GetMarketsConfig
- key_count: 7
  name: Getmarketsinfo
  slug: GetMarketsInfo
- key_count: 7
  name: Getmarketstickers
  slug: GetMarketsTickers
- key_count: 7
  name: Getmarketsvalues
  slug: GetMarketsValues
- key_count: 7
  name: Getohlcv
  slug: GetOhlcv
- key_count: 7
  name: Getorderbykey
  slug: GetOrderByKey
- key_count: 7
  name: Getordersbyaddress
  slug: GetOrdersByAddress
- key_count: 7
  name: Getpairs
  slug: GetPairs
- key_count: 7
  name: Getpositionbykey
  slug: GetPositionByKey
- key_count: 7
  name: Getpositionsinfo
  slug: GetPositionsInfo
- key_count: 7
  name: Getrates
  slug: GetRates
- key_count: 7
  name: Getsnapshots
  slug: GetSnapshots
- key_count: 7
  name: Getstakingpower
  slug: GetStakingPower
- key_count: 7
  name: Gettokens
  slug: GetTokens
- key_count: 7
  name: Gettokensinfo
  slug: GetTokensInfo
- key_count: 7
  name: Gettrades
  slug: GetTrades
- key_count: 7
  name: Getwalletbalances
  slug: GetWalletBalances
- key_count: 7
  name: Getweeklystats
  slug: GetWeeklyStats
- key_count: 7
  name: Prepare
  slug: Prepare
- key_count: 7
  name: Prepareapproval
  slug: PrepareApproval
- key_count: 7
  name: Preparecrosschaindeposit
  slug: PrepareCrossChainDeposit
- key_count: 7
  name: Preparecrosschainwithdraw
  slug: PrepareCrossChainWithdraw
- key_count: 7
  name: Searchtrades
  slug: SearchTrades
- key_count: 7
  name: Status
  slug: Status
- key_count: 7
  name: Statuscrosschainwithdraw
  slug: StatusCrossChainWithdraw
- key_count: 7
  name: Submit
  slug: Submit
- key_count: 7
  name: Submitcrosschainwithdraw
  slug: SubmitCrossChainWithdraw
finops:
- name: Gmx Finops
  service_category: API
  slug: gmx-finops
graphqls:
- description: GMX exposes historical on-chain data through a Subsquid-powered GraphQL API. The primary endpoint indexes the GMX Synthetics protocol on Arbitrum and provides deep query capabilities over trades, posi
  name: GMX GraphQL API
  slug: gmx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gmx.png
json_schemas:
- name: ApiParameterPeriod
  property_count: 0
  slug: ApiParameterPeriod
- name: ApprovalPrepareRequest
  property_count: 6
  slug: ApprovalPrepareRequest
- name: ApprovalPrepareResponse
  property_count: 6
  slug: ApprovalPrepareResponse
- name: ApyEntry
  property_count: 3
  slug: ApyEntry
- name: ApyResponse
  property_count: 2
  slug: ApyResponse
- name: BigIntToString_BuybackWeeklyStatsData_
  property_count: 2
  slug: BigIntToString_BuybackWeeklyStatsData_
- name: BigIntToString_StakingPowerData_
  property_count: 12
  slug: BigIntToString_StakingPowerData_
- name: BridgeOutParamsDto
  property_count: 5
  slug: BridgeOutParamsDto
- name: BuybackWeeklyStatsResponse
  property_count: 0
  slug: BuybackWeeklyStatsResponse
- name: CancelPrepareRequest
  property_count: 7
  slug: CancelPrepareRequest
- name: CollateralOperation
  property_count: 0
  slug: CollateralOperation
- name: CollateralPrepareRequest
  property_count: 11
  slug: CollateralPrepareRequest
- name: CrossChainDepositPrepareRequest
  property_count: 13
  slug: CrossChainDepositPrepareRequest
- name: CrossChainDepositPrepareResponse
  property_count: 5
  slug: CrossChainDepositPrepareResponse
- name: CrossChainWithdrawPrepareRequest
  property_count: 4
  slug: CrossChainWithdrawPrepareRequest
- name: CrossChainWithdrawPrepareResponse
  property_count: 4
  slug: CrossChainWithdrawPrepareResponse
- name: CrossChainWithdrawSubmitRequest
  property_count: 8
  slug: CrossChainWithdrawSubmitRequest
- name: CrossChainWithdrawSubmitResponse
  property_count: 4
  slug: CrossChainWithdrawSubmitResponse
- name: EditPrepareRequest
  property_count: 10
  slug: EditPrepareRequest
- name: GasPaymentParamsDto
  property_count: 4
  slug: GasPaymentParamsDto
- name: GlvShiftParamsResponse
  property_count: 5
  slug: GlvShiftParamsResponse
- name: GmxAccountStatusRequest
  property_count: 1
  slug: GmxAccountStatusRequest
- name: GmxAccountStatusResponse
  property_count: 8
  slug: GmxAccountStatusResponse
- name: JitLiquidityHistoryPeriod
  property_count: 0
  slug: JitLiquidityHistoryPeriod
- name: JitLiquidityHistoryResponse
  property_count: 1
  slug: JitLiquidityHistoryResponse
- name: JitLiquidityInfoItemResponse
  property_count: 5
  slug: JitLiquidityInfoItemResponse
- name: JitLiquidityInfoResponse
  property_count: 1
  slug: JitLiquidityInfoResponse
- name: JitLiquiditySnapshotResponse
  property_count: 5
  slug: JitLiquiditySnapshotResponse
- name: LeverageTierResponse
  property_count: 3
  slug: LeverageTierResponse
- name: MarketConfigResponse
  property_count: 0
  slug: MarketConfigResponse
- name: MarketDirectionFilter
  property_count: 3
  slug: MarketDirectionFilter
- name: MarketInfoResponse
  property_count: 87
  slug: MarketInfoResponse
- name: MarketRatesResponse
  property_count: 2
  slug: MarketRatesResponse
- name: MarketTickerResponse
  property_count: 27
  slug: MarketTickerResponse
- name: MarketValuesResponse
  property_count: 0
  slug: MarketValuesResponse
- name: MarketWithTiersResponse
  property_count: 11
  slug: MarketWithTiersResponse
- name: OhlcvCandle
  property_count: 5
  slug: OhlcvCandle
- name: Omit_MarketInfoResponse.Exclude_MarketValuesFieldKey.marketTokenAddress__
  property_count: 0
  slug: Omit_MarketInfoResponse.Exclude_MarketValuesFieldKey.marketTokenAddress__
- name: OrderEventCombination
  property_count: 4
  slug: OrderEventCombination
- name: OrderKind
  property_count: 0
  slug: OrderKind
- name: OrderResponse
  property_count: 27
  slug: OrderResponse
- name: OrderTransactionStatus
  property_count: 0
  slug: OrderTransactionStatus
- name: PairResponse
  property_count: 18
  slug: PairResponse
- name: Pick_MarketInfoResponse.Exclude_keyofMarketInfoResponse.Exclude_MarketValuesFieldKey.marketTokenAddress___
  property_count: 68
  slug: Pick_MarketInfoResponse.Exclude_keyofMarketInfoResponse.Exclude_MarketValuesFieldKey.marketTokenAddress___
- name: Pick_MarketInfoResponse.MarketValuesFieldKey_
  property_count: 20
  slug: Pick_MarketInfoResponse.MarketValuesFieldKey_
- name: PositionResponse
  property_count: 50
  slug: PositionResponse
- name: PrepareRequest
  property_count: 24
  slug: PrepareRequest
- name: PrepareResponse
  property_count: 8
  slug: PrepareResponse
- name: RatesResponse
  property_count: 0
  slug: RatesResponse
- name: RatesSnapshotResponse
  property_count: 7
  slug: RatesSnapshotResponse
- name: Record_string.ApyEntry_
  property_count: 0
  slug: Record_string.ApyEntry_
- name: Record_string._name-string--type-string_-Array_
  property_count: 0
  slug: Record_string._name-string--type-string_-Array_
- name: Record_string.any_
  property_count: 0
  slug: Record_string.any_
- name: Record_string.unknown_
  property_count: 0
  slug: Record_string.unknown_
- name: SimpleOrderType
  property_count: 0
  slug: SimpleOrderType
- name: StakingPowerResponse
  property_count: 0
  slug: StakingPowerResponse
- name: StatusRequest
  property_count: 1
  slug: StatusRequest
- name: StatusResponse
  property_count: 13
  slug: StatusResponse
- name: SubaccountStatusRequest
  property_count: 2
  slug: SubaccountStatusRequest
- name: SubaccountStatusResponse
  property_count: 8
  slug: SubaccountStatusResponse
- name: SubmitRequest
  property_count: 5
  slug: SubmitRequest
- name: SubmitResponse
  property_count: 6
  slug: SubmitResponse
- name: TokenAllowance
  property_count: 4
  slug: TokenAllowance
- name: TokenInfoResponse
  property_count: 39
  slug: TokenInfoResponse
- name: TokenResponse
  property_count: 31
  slug: TokenResponse
- name: TradeActionResponse
  property_count: 44
  slug: TradeActionResponse
- name: TradeDirection
  property_count: 0
  slug: TradeDirection
- name: TradeResponse
  property_count: 0
  slug: TradeResponse
- name: TradesListResponse
  property_count: 3
  slug: TradesListResponse
- name: TradesSearchRequest
  property_count: 9
  slug: TradesSearchRequest
- name: TransactionMode
  property_count: 0
  slug: TransactionMode
- name: WalletBalance
  property_count: 4
  slug: WalletBalance
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 6
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-06-14'
name: GMX
nav: Providers
network: true
overview: 'GMX publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Allowances API, APY API, Balances API, and 15 more. Tagged areas include DeFi, Perpetual Exchange, DEX, Trading, and Leverage.


  The GMX catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  GMX''s developer surface includes documentation, GitHub presence, engineering blog, changelog, and 5 more developer resources.'
plans:
- name: Gmx Plans Pricing
  plan_count: 1
  slug: gmx-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Gmx Rate Limits
  slug: gmx-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: GMX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gmx-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 46.5
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gmx/refs/heads/main/screenshots/gmx-2026-06-20T181934.png
security:
- kind: domain-security
  name: Gmx Domain Security
  slug: gmx-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gmx
tags:
- DeFi
- Perpetual Exchange
- DEX
- Trading
- Leverage
- Liquidity Pools
- GLP
- GM Tokens
- GLV
- Arbitrum
- Avalanche
- Web3
website: https://gmx.io
---
