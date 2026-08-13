---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Tastytrade Agentic Access
  operation_count: 96
  slug: tastytrade-agentic-access
  summary_line: 96 operations · 20 acting
api_count: 29
apis:
- description: Real-time market data streaming via DXLink, a WebSocket-based protocol backed by dxFeed. Clients fetch a quote token from the tastytrade REST API and use it to authenticate with the DXLink WebSocket e
  name: tastytrade DXLink Market Data Streaming API
  slug: tastytrade-dxlink-market-data-streaming-api
- description: WebSocket-based account streaming that delivers real-time notifications for order fills, position changes, account balance updates, and margin requirement changes. Clients authenticate using a tastytr
  name: tastytrade Account Streamer API
  slug: tastytrade-account-streamer-api
- description: Operations about accounts
  name: tastytrade accounts API
  slug: tastytrade-accounts-api
- description: Operations about api-quote-tokens
  name: tastytrade api-quote-tokens API
  slug: tastytrade-api-quote-tokens-api
- description: The Available Dates API from tastytrade — 1 operation(s) for available dates.
  name: tastytrade Available Dates API
  slug: tastytrade-available-dates-api
- description: The Backtests API from tastytrade — 4 operation(s) for backtests.
  name: tastytrade Backtests API
  slug: tastytrade-backtests-api
- description: Operations about balance-snapshots
  name: tastytrade balance-snapshots API
  slug: tastytrade-balance-snapshots-api
- description: Allows an API client to retreive information about complex orders on a per account basis.
  name: tastytrade complex-orders API
  slug: tastytrade-complex-orders-api
- description: Operations about customers
  name: tastytrade customers API
  slug: tastytrade-customers-api
- description: Operations about futures-option-chains
  name: tastytrade futures-option-chains API
  slug: tastytrade-futures-option-chains-api
- description: Operations about instruments
  name: tastytrade instruments API
  slug: tastytrade-instruments-api
- description: allows a client to fetch margin-requirements for positions and orders
  name: tastytrade margin-requirements API
  slug: tastytrade-margin-requirements-api
- description: Operations about margin-requirements-public-configurations
  name: tastytrade margin-requirements-public-configuration API
  slug: tastytrade-margin-requirements-public-configuration-api
- description: The market-data-controller API from tastytrade — 1 operation(s) for market-data-controller.
  name: tastytrade market-data-controller API
  slug: tastytrade-market-data-controller-api
- description: The Market Metrics API from tastytrade — 3 operation(s) for market metrics.
  name: tastytrade Market Metrics API
  slug: tastytrade-market-metrics-api
- description: Operations about market-times
  name: tastytrade market-time API
  slug: tastytrade-market-time-api
- description: The net-liq-controller API from tastytrade — 1 operation(s) for net-liq-controller.
  name: tastytrade net-liq-controller API
  slug: tastytrade-net-liq-controller-api
- description: Operations about option-chains
  name: tastytrade option-chains API
  slug: tastytrade-option-chains-api
- description: Allows an API client to view, filter, create, cancel and replace orders.
  name: tastytrade orders API
  slug: tastytrade-orders-api
- description: Allows an API client to fetch pairs watchlists.
  name: tastytrade pairs-watchlists API
  slug: tastytrade-pairs-watchlists-api
- description: Operations about positions
  name: tastytrade positions API
  slug: tastytrade-positions-api
- description: Allows an API client to fetch tastyworks watchlists.
  name: tastytrade public-watchlists API
  slug: tastytrade-public-watchlists-api
- description: Operations about quote-alerts
  name: tastytrade quote-alerts API
  slug: tastytrade-quote-alerts-api
- description: The Simulate Trade API from tastytrade — 1 operation(s) for simulate trade.
  name: tastytrade Simulate Trade API
  slug: tastytrade-simulate-trade-api
- description: Operations about spans
  name: tastytrade span API
  slug: tastytrade-span-api
- description: The Symbols API from tastytrade — 1 operation(s) for symbols.
  name: tastytrade Symbols API
  slug: tastytrade-symbols-api
- description: Allows an API client to request information about the basic trade status of an account. \ This includes information about the strategies an account can trade.
  name: tastytrade trading-status API
  slug: tastytrade-trading-status-api
- description: Operations about transactions
  name: tastytrade transactions API
  slug: tastytrade-transactions-api
- description: Allows an API client to fetch a user's watchlists.
  name: tastytrade user-watchlists API
  slug: tastytrade-user-watchlists-api
artifact_total: 141
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tastytrade-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tastytrade-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.tastytrade.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tastytrade.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.tastytrade.com/oauth/
- group: start
  title: ''
  type: Sandbox
  url: https://developer.tastytrade.com/sandbox/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.tastytrade.com/faq/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.tastytrade.com/release-notes/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tastytrade/
- group: build
  title: ''
  type: JavaScriptSDK
  url: https://github.com/tastytrade/tastytrade-api-js
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/tastytradeapi/tastytrade-api/documentation/p5jnvzh/tastytrade-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.tastyworks.com/production/documents/USA/open_api_terms_and_conditions.pdf
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:api.support@tastytrade.com
- group: company
  title: ''
  type: Website
  url: https://tastytrade.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/finops.yml
created: '2026-06-13'
description: tastytrade is an options-focused brokerage offering a public Open API that provides full read and write access to real-time account data, positions, balances, transaction history, market data, option chains, and order execution across equities, options, futures, and crypto. The API uses REST over HTTPS with JSON payloads for synchronous operations and WebSocket connections (DXLink for market data, dedicated account streamer for real-time account updates). OAuth 2.0 and session-token authentication are both supported, with a safe sandbox environment for development and testing.
examples:
- key_count: 6
  name: Account Status Getaccountsaccountnumbertradingstatus
  slug: account-status-getAccountsAccountNumberTradingStatus
- key_count: 6
  name: Accounts And Customers Getapiquotetokens
  slug: accounts-and-customers-getApiQuoteTokens
- key_count: 6
  name: Accounts And Customers Getcustomerscustomerid
  slug: accounts-and-customers-getCustomersCustomerId
- key_count: 6
  name: Accounts And Customers Getcustomerscustomeridaccounts
  slug: accounts-and-customers-getCustomersCustomerIdAccounts
- key_count: 6
  name: Backtesting Getbacktests
  slug: backtesting-GetBacktests
- key_count: 6
  name: Backtesting Getbacktestslogs
  slug: backtesting-GetBacktestsLogs
- key_count: 6
  name: Backtesting Getusersbacktests
  slug: backtesting-GetUsersBacktests
- key_count: 6
  name: Balances And Positions Getaccountsaccountnumberbalancesnapshots
  slug: balances-and-positions-getAccountsAccountNumberBalanceSnapshots
- key_count: 6
  name: Balances And Positions Getaccountsaccountnumberbalances
  slug: balances-and-positions-getAccountsAccountNumberBalances
- key_count: 6
  name: Balances And Positions Getaccountsaccountnumberbalancescurrency
  slug: balances-and-positions-getAccountsAccountNumberBalancesCurrency
- key_count: 6
  name: Instruments Getfuturesoptionchainssymbol
  slug: instruments-getFuturesOptionChainsSymbol
- key_count: 6
  name: Instruments Getfuturesoptionchainssymbolnested
  slug: instruments-getFuturesOptionChainsSymbolNested
- key_count: 6
  name: Instruments Getinstrumentscryptocurrencies
  slug: instruments-getInstrumentsCryptocurrencies
- key_count: 6
  name: Margin Requirements Createmarginaccountsaccountnumberdryrun
  slug: margin-requirements-createMarginAccountsAccountNumberDryRun
- key_count: 6
  name: Margin Requirements Getmarginaccountsaccountnumberrequirements
  slug: margin-requirements-getMarginAccountsAccountNumberRequirements
- key_count: 6
  name: Market Data Getmarketdatabytype
  slug: market-data-getMarketDataByType
- key_count: 6
  name: Market Metrics Getmarketmetricsdividendssymbol
  slug: market-metrics-getMarketMetricsDividendsSymbol
- key_count: 6
  name: Market Metrics Getmarketmetricsearningssymbol
  slug: market-metrics-getMarketMetricsEarningsSymbol
- key_count: 6
  name: Market Metrics Getmarketmetricsindex
  slug: market-metrics-getMarketMetricsIndex
- key_count: 6
  name: Market Sessions Getmarkettimeequitiessessionscurrent
  slug: market-sessions-getMarketTimeEquitiesSessionsCurrent
- key_count: 6
  name: Market Sessions Getmarkettimesessions
  slug: market-sessions-getMarketTimeSessions
- key_count: 6
  name: Market Sessions Getmarkettimesessionscurrent
  slug: market-sessions-getMarketTimeSessionsCurrent
- key_count: 6
  name: Net Liquidating Value History Getnetliqhistory
  slug: net-liquidating-value-history-getNetLiqHistory
- key_count: 6
  name: Orders Getaccountsaccountnumbercomplexorders
  slug: orders-getAccountsAccountNumberComplexOrders
- key_count: 6
  name: Orders Getaccountsaccountnumbercomplexorderslive
  slug: orders-getAccountsAccountNumberComplexOrdersLive
- key_count: 6
  name: Orders Postaccountsaccountnumbercomplexordersdryrun
  slug: orders-postAccountsAccountNumberComplexOrdersDryRun
- key_count: 6
  name: Quote Alerts Deletequotealertsalertexternalid
  slug: quote-alerts-deleteQuoteAlertsAlertExternalId
- key_count: 6
  name: Quote Alerts Getquotealerts
  slug: quote-alerts-getQuoteAlerts
- key_count: 6
  name: Risk Parameters Getaccountsaccountnumbermarginrequirementsunderlyingsymbolef
  slug: risk-parameters-getAccountsAccountNumberMarginRequirementsUnderlyingSymbolEf
- key_count: 6
  name: Risk Parameters Getaccountsaccountnumberpositionlimit
  slug: risk-parameters-getAccountsAccountNumberPositionLimit
- key_count: 6
  name: Risk Parameters Getmarginrequirementspublicconfiguration
  slug: risk-parameters-getMarginRequirementsPublicConfiguration
- key_count: 6
  name: Symbol Search Searchsymbols
  slug: symbol-search-searchSymbols
- key_count: 6
  name: Transactions Getaccountsaccountnumbertransactions
  slug: transactions-getAccountsAccountNumberTransactions
- key_count: 6
  name: Transactions Getaccountsaccountnumbertransactionsid
  slug: transactions-getAccountsAccountNumberTransactionsId
- key_count: 6
  name: Transactions Getaccountsaccountnumbertransactionstotalfees
  slug: transactions-getAccountsAccountNumberTransactionsTotalFees
- key_count: 6
  name: Watchlists Getpublicwatchlists
  slug: watchlists-getPublicWatchlists
- key_count: 6
  name: Watchlists Getpublicwatchlistswatchlistname
  slug: watchlists-getPublicWatchlistsWatchlistName
- key_count: 6
  name: Watchlists Getwatchlists
  slug: watchlists-getWatchlists
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tastytrade.png
json_schemas:
- name: TradingStatus
  property_count: 43
  slug: account-status-TradingStatus
- name: Account
  property_count: 27
  slug: accounts-and-customers-Account
- name: AccountAuthorityDecorator
  property_count: 2
  slug: accounts-and-customers-AccountAuthorityDecorator
- name: Customer
  property_count: 55
  slug: accounts-and-customers-Customer
- name: QuoteStreamerTokenAuthResult
  property_count: 6
  slug: accounts-and-customers-QuoteStreamerTokenAuthResult
- name: AvailableSymbolDates
  property_count: 3
  slug: backtesting-AvailableSymbolDates
- name: BacktestGet
  property_count: 14
  slug: backtesting-BacktestGet
- name: BacktestPost
  property_count: 6
  slug: backtesting-BacktestPost
- name: EntryConditions
  property_count: 6
  slug: backtesting-EntryConditions
- name: ExitConditions
  property_count: 5
  slug: backtesting-ExitConditions
- name: Leg
  property_count: 11
  slug: backtesting-Leg
- name: Snapshot
  property_count: 3
  slug: backtesting-Snapshot
- name: Trial
  property_count: 3
  slug: backtesting-Trial
- name: AccountBalance
  property_count: 71
  slug: balances-and-positions-AccountBalance
- name: AccountBalanceSnapshot
  property_count: 58
  slug: balances-and-positions-AccountBalanceSnapshot
- name: CurrentPosition
  property_count: 33
  slug: balances-and-positions-CurrentPosition
- name: CompactOptionChainSerializer
  property_count: 9
  slug: instruments-CompactOptionChainSerializer
- name: Cryptocurrency
  property_count: 9
  slug: instruments-Cryptocurrency
- name: Equity
  property_count: 26
  slug: instruments-Equity
- name: EquityOption
  property_count: 22
  slug: instruments-EquityOption
- name: Future
  property_count: 33
  slug: instruments-Future
- name: FutureOption
  property_count: 31
  slug: instruments-FutureOption
- name: FutureOptionProduct
  property_count: 13
  slug: instruments-FutureOptionProduct
- name: FutureProduct
  property_count: 26
  slug: instruments-FutureProduct
- name: FuturesNestedOptionChainSerializer
  property_count: 2
  slug: instruments-FuturesNestedOptionChainSerializer
- name: NestedOptionChainSerializer
  property_count: 7
  slug: instruments-NestedOptionChainSerializer
- name: QuantityDecimalPrecision
  property_count: 4
  slug: instruments-QuantityDecimalPrecision
- name: SearchableInstrumentDeserializer
  property_count: 10
  slug: instruments-SearchableInstrumentDeserializer
- name: Warrant
  property_count: 7
  slug: instruments-Warrant
- name: Instrument
  property_count: 6
  slug: market-data-Instrument
- name: InstrumentKey
  property_count: 2
  slug: market-data-InstrumentKey
- name: MarketData
  property_count: 40
  slug: market-data-MarketData
- name: DividendInfo
  property_count: 2
  slug: market-metrics-DividendInfo
- name: EarningsInfo
  property_count: 2
  slug: market-metrics-EarningsInfo
- name: MarketMetricInfo
  property_count: 9
  slug: market-metrics-MarketMetricInfo
- name: CurrentSession
  property_count: 8
  slug: market-sessions-CurrentSession
- name: CurrentSessionDeserializer
  property_count: 8
  slug: market-sessions-CurrentSessionDeserializer
- name: MarketCalendarDeserializer
  property_count: 2
  slug: market-sessions-MarketCalendarDeserializer
- name: NextSession
  property_count: 6
  slug: market-sessions-NextSession
- name: PreviousSession
  property_count: 6
  slug: market-sessions-PreviousSession
- name: SimpleSessionDeserializer
  property_count: 5
  slug: market-sessions-SimpleSessionDeserializer
- name: NetLiqOhlc
  property_count: 13
  slug: net-liquidating-value-history-NetLiqOhlc
- name: ComplexOrder
  property_count: 10
  slug: orders-ComplexOrder
- name: Order
  property_count: 41
  slug: orders-Order
- name: PlacedOrderResponse
  property_count: 8
  slug: orders-PlacedOrderResponse
- name: patchAccountsAccountNumberComplexOrdersId
  property_count: 2
  slug: orders-patchAccountsAccountNumberComplexOrdersId
- name: patchAccountsAccountNumberOrdersId
  property_count: 14
  slug: orders-patchAccountsAccountNumberOrdersId
- name: postAccountsAccountNumberComplexOrders
  property_count: 7
  slug: orders-postAccountsAccountNumberComplexOrders
- name: postAccountsAccountNumberComplexOrdersDryRun
  property_count: 7
  slug: orders-postAccountsAccountNumberComplexOrdersDryRun
- name: postAccountsAccountNumberComplexOrdersIdDryRun
  property_count: 2
  slug: orders-postAccountsAccountNumberComplexOrdersIdDryRun
- name: postAccountsAccountNumberOrders
  property_count: 16
  slug: orders-postAccountsAccountNumberOrders
- name: postAccountsAccountNumberOrdersDryRun
  property_count: 16
  slug: orders-postAccountsAccountNumberOrdersDryRun
- name: postAccountsAccountNumberOrdersIdDryRun
  property_count: 14
  slug: orders-postAccountsAccountNumberOrdersIdDryRun
- name: putAccountsAccountNumberOrdersId
  property_count: 14
  slug: orders-putAccountsAccountNumberOrdersId
- name: QuoteAlertDeserializer
  property_count: 16
  slug: quote-alerts-QuoteAlertDeserializer
- name: postQuoteAlerts
  property_count: 8
  slug: quote-alerts-postQuoteAlerts
- name: MarginRequirement
  property_count: 10
  slug: risk-parameters-MarginRequirement
- name: MarginRequirementsGlobalConfiguration
  property_count: 1
  slug: risk-parameters-MarginRequirementsGlobalConfiguration
- name: PositionLimit
  property_count: 11
  slug: risk-parameters-PositionLimit
- name: Row
  property_count: 4
  slug: risk-parameters-Row
- name: SymbolData
  property_count: 7
  slug: symbol-search-SymbolData
- name: Transaction
  property_count: 49
  slug: transactions-Transaction
- name: PairsWatchlist
  property_count: 3
  slug: watchlists-PairsWatchlist
- name: Watchlist
  property_count: 5
  slug: watchlists-Watchlist
- name: postWatchlists
  property_count: 4
  slug: watchlists-postWatchlists
- name: putWatchlistsWatchlistName
  property_count: 4
  slug: watchlists-putWatchlistsWatchlistName
jsonld:
- class_count: 0
  name: Tastytrade Api Context
  property_count: 0
  slug: tastytrade-api
- class_count: 0
  name: Tastytrade Context
  property_count: 562
  slug: tastytrade-context
layout: provider
modified: '2026-06-13'
name: tastytrade
nav: Providers
network: true
overview: 'tastytrade publishes 27 APIs on the [APIs.io](https://apis.io/) network, including accounts API, api-quote-tokens API, Available Dates API, and 24 more. Tagged areas include Finance, Brokerage, Trading, Options, and Futures.


  The tastytrade catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  tastytrade''s developer surface includes developer portal, documentation, authentication, sandbox, FAQ, changelog, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 13
rate_limits:
- limit_count: 4
  name: Rate Limits
  slug: rate-limits
rules:
- name: tastytrade API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tastytrade-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.3
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 45.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tastytrade/refs/heads/main/screenshots/tastytrade-2026-06-20T194927.png
security:
- kind: domain-security
  name: Tastytrade Domain Security
  slug: tastytrade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tastytrade
tags:
- Finance
- Brokerage
- Trading
- Options
- Futures
- Equities
- Crypto
- Market Data
- WebSocket
website: https://tastytrade.com/
---
