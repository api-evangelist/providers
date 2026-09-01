---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Oanda Agentic Access
  operation_count: 105
  slug: oanda-agentic-access
  summary_line: 105 operations · 31 acting
api_count: 13
apis:
- description: Manage and retrieve OANDA trading account details, summaries, tradeable instruments, and configuration settings. Supports polling for account state changes since a specified transaction ID.
  name: OANDA Account API
  slug: oanda-account-api
- description: Create, list, modify, and cancel orders in an OANDA trading account. Supports market, limit, stop, take profit, stop loss, and trailing stop order types with FOK, IOC, DAY, GTD, and GTC durations.
  name: OANDA Order API
  slug: oanda-order-api
- description: List, retrieve, partially or fully close open trades, and manage dependent orders (take profit, stop loss, trailing stop loss) for trades in an OANDA account.
  name: OANDA Trade API
  slug: oanda-trade-api
- description: List all positions (historical and open) and close out open positions for a specific instrument in an OANDA trading account.
  name: OANDA Position API
  slug: oanda-position-api
- description: 'Access full transaction history for an OANDA trading account with time-based and ID-range queries. Includes a streaming endpoint for real-time transaction notifications from the moment the request is '
  name: OANDA Transaction API
  slug: oanda-transaction-api
- description: Retrieve real-time bid/ask pricing, stream live price updates at up to 4 per second, and access historical OHLC candlestick data for any tradeable instrument. Historical data is available from 2005 on
  name: OANDA Pricing API
  slug: oanda-pricing-api
- description: Institutional-grade foreign exchange data service covering 200+ currencies and 38,000+ currency pairs. Provides daily average rates, period averages, ECB and national bank rates, forward rates, stream
  name: OANDA Exchange Rates API
  slug: oanda-exchange-rates-api
- description: The Accounts API from OANDA — 29 operation(s) for accounts.
  name: OANDA Accounts API
  slug: oanda-accounts-api
- description: The Instruments API from OANDA — 5 operation(s) for instruments.
  name: OANDA Instruments API
  slug: oanda-instruments-api
- description: The Pricing API from OANDA — 2 operation(s) for pricing.
  name: OANDA Pricing API
  slug: oanda-pricing-api
- description: The Users API from OANDA — 2 operation(s) for users.
  name: OANDA Users API
  slug: oanda-users-api
artifact_total: 234
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OANDA v20 REST Accounts API
  slug: open-oanda-accounts-api
- collection_type: open
  name: OANDA v20 REST Accounts Instruments API
  slug: open-oanda-instruments-api
- collection_type: open
  name: OANDA v20 REST Accounts Pricing API
  slug: open-oanda-pricing-api
- collection_type: open
  name: OANDA v20 REST Accounts Users API
  slug: open-oanda-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/oanda-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oanda-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oanda-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.oanda.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.oanda.com/rest-live-v20/introduction/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.oanda.com/rest-live-v20/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.oanda.com/rest-live-v20/account-ep/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.oanda.com/rest-live-v20/authentication/
- group: other
  title: ''
  type: BestPractices
  url: https://developer.oanda.com/rest-live-v20/best-practices/
- group: other
  title: ''
  type: APIComparison
  url: https://developer.oanda.com/rest-live-v20/api-comparison/
- group: docs
  title: ''
  type: OpenAPISource
  url: https://github.com/oanda/v20-openapi
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/oanda/v20-python
- group: build
  title: ''
  type: CodeSamples
  url: https://github.com/oanda/v20-python-samples
- group: build
  title: ''
  type: JavaScriptSDK
  url: https://github.com/oanda/v20-javascript
- group: build
  title: ''
  type: JavaSDK
  url: https://github.com/oanda/v20-java
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oanda
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oanda.com/foreign-exchange-data-services/en/exchange-rates-api/api-plans/
- group: company
  title: ''
  type: Website
  url: https://www.oanda.com/
- group: start
  title: ''
  type: Signup
  url: https://www.oanda.com/us-en/trading/demo-account/
created: '2026-06-13'
description: OANDA is a forex and CFD trading broker offering REST APIs for live and practice trading. The v20 REST API provides access to real-time forex rates, order management, trade lifecycle, position tracking, and historical OHLC candle data dating back to 2005. A separate Exchange Rates Data API delivers institutional-grade FX rates across 200+ currencies for data services use cases.
examples:
- key_count: 6
  name: Cancelorder
  slug: cancelOrder
- key_count: 6
  name: Closeposition
  slug: closePosition
- key_count: 6
  name: Closetrade
  slug: closeTrade
- key_count: 6
  name: Configureaccount
  slug: configureAccount
- key_count: 6
  name: Createorder
  slug: createOrder
- key_count: 6
  name: Getaccount
  slug: getAccount
- key_count: 6
  name: Getaccountchanges
  slug: getAccountChanges
- key_count: 6
  name: Getaccountinstruments
  slug: getAccountInstruments
- key_count: 6
  name: Getaccountsummary
  slug: getAccountSummary
- key_count: 6
  name: Getbaseprices
  slug: getBasePrices
- key_count: 6
  name: Getexternaluserinfo
  slug: getExternalUserInfo
- key_count: 6
  name: Getinstrumentcandles
  slug: getInstrumentCandles
- key_count: 6
  name: Getinstrumentprice
  slug: getInstrumentPrice
- key_count: 6
  name: Getinstrumentpricerange
  slug: getInstrumentPriceRange
- key_count: 6
  name: Getorder
  slug: getOrder
- key_count: 6
  name: Getposition
  slug: getPosition
- key_count: 6
  name: Getpricerange
  slug: getPriceRange
- key_count: 6
  name: Getprices
  slug: getPrices
- key_count: 6
  name: Gettrade
  slug: getTrade
- key_count: 6
  name: Gettransaction
  slug: getTransaction
- key_count: 6
  name: Gettransactionrange
  slug: getTransactionRange
- key_count: 6
  name: Gettransactionssinceid
  slug: getTransactionsSinceId
- key_count: 6
  name: Getuserinfo
  slug: getUserInfo
- key_count: 6
  name: Get_Instruments_{Instrument}_Orderbook
  slug: get_instruments_{instrument}_orderBook
- key_count: 6
  name: Get_Instruments_{Instrument}_Positionbook
  slug: get_instruments_{instrument}_positionBook
- key_count: 6
  name: Listaccounts
  slug: listAccounts
- key_count: 6
  name: Listopenpositions
  slug: listOpenPositions
- key_count: 6
  name: Listopentrades
  slug: listOpenTrades
- key_count: 6
  name: Listorders
  slug: listOrders
- key_count: 6
  name: Listpendingorders
  slug: listPendingOrders
- key_count: 6
  name: Listpositions
  slug: listPositions
- key_count: 6
  name: Listtrades
  slug: listTrades
- key_count: 6
  name: Listtransactions
  slug: listTransactions
- key_count: 6
  name: Replaceorder
  slug: replaceOrder
- key_count: 6
  name: Setorderclientextensions
  slug: setOrderClientExtensions
- key_count: 6
  name: Settradeclientextensions
  slug: setTradeClientExtensions
- key_count: 6
  name: Settradedependentorders
  slug: setTradeDependentOrders
- key_count: 6
  name: Streampricing
  slug: streamPricing
- key_count: 6
  name: Streamtransactions
  slug: streamTransactions
features:
- REST v20 API with JSON over HTTP; stateless and language-agnostic
- Bearer token (Personal Access Token) authentication via fxTrade AMP
- Live and practice (demo) trading environments
- Real-time forex rates for all tradeable pairs 24 hours a day
- Historical candlestick data from 2005 onward (S5 to Monthly granularity)
- Streaming pricing endpoint at up to 4 price updates per second
- Full order lifecycle — market, limit, stop, OCO (TP/SL pair), trailing stop
- Trade management including partial close and dependent order updates
- Position closeout by instrument
- Unlimited recent transaction history with streaming endpoint
- Rate limit of 30 requests per user; aggregate of 20 streaming connections
- New connection limit of 2 per second; persistent connections up to 100 per second
- Exchange Rates Data API covering 200+ currencies and 38,000+ currency pairs
- Exchange Rates free 7-day trial with unlimited quotes
- FIX API for institutional customers
- MT4 integration for backtesting support
finops:
- name: Oanda Finops
  service_category: Financial Services
  slug: oanda-finops
image: https://www.oanda.com/img/oanda-logo.png
json_schemas:
- name: AcceptDatetimeFormat
  property_count: 0
  slug: AcceptDatetimeFormat
- name: Account
  property_count: 39
  slug: Account
- name: AccountChanges
  property_count: 9
  slug: AccountChanges
- name: AccountChangesState
  property_count: 16
  slug: AccountChangesState
- name: AccountFinancingMode
  property_count: 0
  slug: AccountFinancingMode
- name: AccountID
  property_count: 0
  slug: AccountID
- name: AccountProperties
  property_count: 3
  slug: AccountProperties
- name: AccountSummary
  property_count: 36
  slug: AccountSummary
- name: AccountUnits
  property_count: 0
  slug: AccountUnits
- name: CalculatedAccountState
  property_count: 13
  slug: CalculatedAccountState
- name: CalculatedPositionState
  property_count: 5
  slug: CalculatedPositionState
- name: CalculatedTradeState
  property_count: 3
  slug: CalculatedTradeState
- name: CancellableOrderType
  property_count: 0
  slug: CancellableOrderType
- name: Candlestick
  property_count: 6
  slug: Candlestick
- name: CandlestickData
  property_count: 4
  slug: CandlestickData
- name: CandlestickGranularity
  property_count: 0
  slug: CandlestickGranularity
- name: ClientComment
  property_count: 0
  slug: ClientComment
- name: ClientConfigureRejectTransaction
  property_count: 10
  slug: ClientConfigureRejectTransaction
- name: ClientConfigureTransaction
  property_count: 9
  slug: ClientConfigureTransaction
- name: ClientExtensions
  property_count: 3
  slug: ClientExtensions
- name: ClientID
  property_count: 0
  slug: ClientID
- name: ClientPrice
  property_count: 11
  slug: ClientPrice
- name: ClientRequestID
  property_count: 0
  slug: ClientRequestID
- name: ClientTag
  property_count: 0
  slug: ClientTag
- name: CloseTransaction
  property_count: 7
  slug: CloseTransaction
- name: CreateTransaction
  property_count: 12
  slug: CreateTransaction
- name: Currency
  property_count: 0
  slug: Currency
- name: DailyFinancingTransaction
  property_count: 11
  slug: DailyFinancingTransaction
- name: DateTime
  property_count: 0
  slug: DateTime
- name: DecimalNumber
  property_count: 0
  slug: DecimalNumber
- name: DelayedTradeClosureTransaction
  property_count: 9
  slug: DelayedTradeClosureTransaction
- name: Direction
  property_count: 0
  slug: Direction
- name: DynamicOrderState
  property_count: 4
  slug: DynamicOrderState
- name: FixedPriceOrder
  property_count: 21
  slug: FixedPriceOrder
- name: FixedPriceOrderReason
  property_count: 0
  slug: FixedPriceOrderReason
- name: FixedPriceOrderTransaction
  property_count: 18
  slug: FixedPriceOrderTransaction
- name: FundingReason
  property_count: 0
  slug: FundingReason
- name: GuaranteedStopLossOrderEntryData
  property_count: 3
  slug: GuaranteedStopLossOrderEntryData
- name: GuaranteedStopLossOrderLevelRestriction
  property_count: 2
  slug: GuaranteedStopLossOrderLevelRestriction
- name: GuaranteedStopLossOrderMode
  property_count: 0
  slug: GuaranteedStopLossOrderMode
- name: HomeConversions
  property_count: 4
  slug: HomeConversions
- name: Instrument
  property_count: 13
  slug: Instrument
- name: InstrumentCommission
  property_count: 3
  slug: InstrumentCommission
- name: InstrumentName
  property_count: 0
  slug: InstrumentName
- name: InstrumentType
  property_count: 0
  slug: InstrumentType
- name: LimitOrder
  property_count: 25
  slug: LimitOrder
- name: LimitOrderReason
  property_count: 0
  slug: LimitOrderReason
- name: LimitOrderRejectTransaction
  property_count: 22
  slug: LimitOrderRejectTransaction
- name: LimitOrderRequest
  property_count: 13
  slug: LimitOrderRequest
- name: LimitOrderTransaction
  property_count: 22
  slug: LimitOrderTransaction
- name: LiquidityRegenerationSchedule
  property_count: 1
  slug: LiquidityRegenerationSchedule
- name: LiquidityRegenerationScheduleStep
  property_count: 3
  slug: LiquidityRegenerationScheduleStep
- name: MT4TransactionHeartbeat
  property_count: 2
  slug: MT4TransactionHeartbeat
- name: MarginCallEnterTransaction
  property_count: 7
  slug: MarginCallEnterTransaction
- name: MarginCallExitTransaction
  property_count: 7
  slug: MarginCallExitTransaction
- name: MarginCallExtendTransaction
  property_count: 8
  slug: MarginCallExtendTransaction
- name: MarketIfTouchedOrder
  property_count: 27
  slug: MarketIfTouchedOrder
- name: MarketIfTouchedOrderReason
  property_count: 0
  slug: MarketIfTouchedOrderReason
- name: MarketIfTouchedOrderRejectTransaction
  property_count: 23
  slug: MarketIfTouchedOrderRejectTransaction
- name: MarketIfTouchedOrderRequest
  property_count: 14
  slug: MarketIfTouchedOrderRequest
- name: MarketIfTouchedOrderTransaction
  property_count: 23
  slug: MarketIfTouchedOrderTransaction
- name: MarketOrder
  property_count: 26
  slug: MarketOrder
- name: MarketOrderDelayedTradeClose
  property_count: 3
  slug: MarketOrderDelayedTradeClose
- name: MarketOrderMarginCloseout
  property_count: 1
  slug: MarketOrderMarginCloseout
- name: MarketOrderMarginCloseoutReason
  property_count: 0
  slug: MarketOrderMarginCloseoutReason
- name: MarketOrderPositionCloseout
  property_count: 2
  slug: MarketOrderPositionCloseout
- name: MarketOrderReason
  property_count: 0
  slug: MarketOrderReason
- name: MarketOrderRejectTransaction
  property_count: 24
  slug: MarketOrderRejectTransaction
- name: MarketOrderRequest
  property_count: 11
  slug: MarketOrderRequest
- name: MarketOrderTradeClose
  property_count: 3
  slug: MarketOrderTradeClose
- name: MarketOrderTransaction
  property_count: 23
  slug: MarketOrderTransaction
- name: OpenTradeFinancing
  property_count: 2
  slug: OpenTradeFinancing
- name: Order
  property_count: 4
  slug: Order
- name: OrderBook
  property_count: 5
  slug: OrderBook
- name: OrderBookBucket
  property_count: 3
  slug: OrderBookBucket
- name: OrderCancelReason
  property_count: 0
  slug: OrderCancelReason
- name: OrderCancelRejectTransaction
  property_count: 10
  slug: OrderCancelRejectTransaction
- name: OrderCancelTransaction
  property_count: 11
  slug: OrderCancelTransaction
- name: OrderClientExtensionsModifyRejectTransaction
  property_count: 12
  slug: OrderClientExtensionsModifyRejectTransaction
- name: OrderClientExtensionsModifyTransaction
  property_count: 11
  slug: OrderClientExtensionsModifyTransaction
- name: OrderFillReason
  property_count: 0
  slug: OrderFillReason
- name: OrderFillTransaction
  property_count: 26
  slug: OrderFillTransaction
- name: OrderID
  property_count: 0
  slug: OrderID
- name: OrderIdentifier
  property_count: 2
  slug: OrderIdentifier
- name: OrderPositionFill
  property_count: 0
  slug: OrderPositionFill
- name: OrderRequest
  property_count: 0
  slug: OrderRequest
- name: OrderSpecifier
  property_count: 0
  slug: OrderSpecifier
- name: OrderState
  property_count: 0
  slug: OrderState
- name: OrderStateFilter
  property_count: 0
  slug: OrderStateFilter
- name: OrderTriggerCondition
  property_count: 0
  slug: OrderTriggerCondition
- name: OrderType
  property_count: 0
  slug: OrderType
- name: Position
  property_count: 10
  slug: Position
- name: PositionAggregationMode
  property_count: 0
  slug: PositionAggregationMode
- name: PositionBook
  property_count: 5
  slug: PositionBook
- name: PositionBookBucket
  property_count: 3
  slug: PositionBookBucket
- name: PositionFinancing
  property_count: 3
  slug: PositionFinancing
- name: PositionSide
  property_count: 8
  slug: PositionSide
- name: Price
  property_count: 9
  slug: Price
- name: PriceBucket
  property_count: 2
  slug: PriceBucket
- name: PriceStatus
  property_count: 0
  slug: PriceStatus
- name: PriceValue
  property_count: 0
  slug: PriceValue
- name: PricingHeartbeat
  property_count: 2
  slug: PricingHeartbeat
- name: QuoteHomeConversionFactors
  property_count: 2
  slug: QuoteHomeConversionFactors
- name: ReopenTransaction
  property_count: 7
  slug: ReopenTransaction
- name: RequestID
  property_count: 0
  slug: RequestID
- name: ResetResettablePLTransaction
  property_count: 7
  slug: ResetResettablePLTransaction
- name: StatementYear
  property_count: 0
  slug: StatementYear
- name: StopLossDetails
  property_count: 6
  slug: StopLossDetails
- name: StopLossOrder
  property_count: 23
  slug: StopLossOrder
- name: StopLossOrderReason
  property_count: 0
  slug: StopLossOrderReason
- name: StopLossOrderRejectTransaction
  property_count: 20
  slug: StopLossOrderRejectTransaction
- name: StopLossOrderRequest
  property_count: 10
  slug: StopLossOrderRequest
- name: StopLossOrderTransaction
  property_count: 21
  slug: StopLossOrderTransaction
- name: StopOrder
  property_count: 26
  slug: StopOrder
- name: StopOrderReason
  property_count: 0
  slug: StopOrderReason
- name: StopOrderRejectTransaction
  property_count: 23
  slug: StopOrderRejectTransaction
- name: StopOrderRequest
  property_count: 14
  slug: StopOrderRequest
- name: StopOrderTransaction
  property_count: 23
  slug: StopOrderTransaction
- name: TakeProfitDetails
  property_count: 4
  slug: TakeProfitDetails
- name: TakeProfitOrder
  property_count: 20
  slug: TakeProfitOrder
- name: TakeProfitOrderReason
  property_count: 0
  slug: TakeProfitOrderReason
- name: TakeProfitOrderRejectTransaction
  property_count: 18
  slug: TakeProfitOrderRejectTransaction
- name: TakeProfitOrderRequest
  property_count: 8
  slug: TakeProfitOrderRequest
- name: TakeProfitOrderTransaction
  property_count: 18
  slug: TakeProfitOrderTransaction
- name: TimeInForce
  property_count: 0
  slug: TimeInForce
- name: Trade
  property_count: 19
  slug: Trade
- name: TradeClientExtensionsModifyRejectTransaction
  property_count: 11
  slug: TradeClientExtensionsModifyRejectTransaction
- name: TradeClientExtensionsModifyTransaction
  property_count: 10
  slug: TradeClientExtensionsModifyTransaction
- name: TradeID
  property_count: 0
  slug: TradeID
- name: TradeOpen
  property_count: 7
  slug: TradeOpen
- name: TradePL
  property_count: 0
  slug: TradePL
- name: TradeReduce
  property_count: 7
  slug: TradeReduce
- name: TradeSpecifier
  property_count: 0
  slug: TradeSpecifier
- name: TradeState
  property_count: 0
  slug: TradeState
- name: TradeStateFilter
  property_count: 0
  slug: TradeStateFilter
- name: TradeSummary
  property_count: 19
  slug: TradeSummary
- name: TrailingStopLossDetails
  property_count: 4
  slug: TrailingStopLossDetails
- name: TrailingStopLossOrder
  property_count: 21
  slug: TrailingStopLossOrder
- name: TrailingStopLossOrderReason
  property_count: 0
  slug: TrailingStopLossOrderReason
- name: TrailingStopLossOrderRejectTransaction
  property_count: 18
  slug: TrailingStopLossOrderRejectTransaction
- name: TrailingStopLossOrderRequest
  property_count: 8
  slug: TrailingStopLossOrderRequest
- name: TrailingStopLossOrderTransaction
  property_count: 18
  slug: TrailingStopLossOrderTransaction
- name: Transaction
  property_count: 6
  slug: Transaction
- name: TransactionFilter
  property_count: 0
  slug: TransactionFilter
- name: TransactionHeartbeat
  property_count: 3
  slug: TransactionHeartbeat
- name: TransactionID
  property_count: 0
  slug: TransactionID
- name: TransactionRejectReason
  property_count: 0
  slug: TransactionRejectReason
- name: TransactionType
  property_count: 0
  slug: TransactionType
- name: TransferFundsRejectTransaction
  property_count: 11
  slug: TransferFundsRejectTransaction
- name: TransferFundsTransaction
  property_count: 11
  slug: TransferFundsTransaction
- name: UnitsAvailable
  property_count: 4
  slug: UnitsAvailable
- name: UnitsAvailableDetails
  property_count: 2
  slug: UnitsAvailableDetails
- name: UserInfo
  property_count: 4
  slug: UserInfo
- name: UserInfoExternal
  property_count: 3
  slug: UserInfoExternal
- name: UserSpecifier
  property_count: 0
  slug: UserSpecifier
- name: WeeklyAlignment
  property_count: 0
  slug: WeeklyAlignment
jsonld:
- class_count: 5
  name: Oanda Context
  property_count: 0
  slug: oanda
layout: provider
modified: '2026-06-13'
name: OANDA
nav: Providers
network: true
overview: 'OANDA publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Pricing API, Accounts API, Instruments API, and 2 more. Tagged areas include Forex, FX Trading, CFD Trading, Financial-Services, and Trading APIs.


  The OANDA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OANDA''s developer surface includes developer portal, documentation, getting-started guide, API reference, authentication, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Oanda Plans Pricing
  plan_count: 6
  slug: oanda-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Oanda Rate Limits
  slug: oanda-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OANDA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oanda-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 54.8
    developer_ergonomics: 50.0
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 36.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oanda/refs/heads/main/screenshots/oanda-2026-06-20T190546.png
security:
- kind: domain-security
  name: Oanda Domain Security
  slug: oanda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oanda
tags:
- Forex
- FX Trading
- CFD Trading
- Financial-Services
- Trading APIs
website: https://www.oanda.com/
---
