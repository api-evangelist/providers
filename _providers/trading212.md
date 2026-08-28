---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Trading212 Agentic Access
  operation_count: 22
  slug: trading212-agentic-access
  summary_line: 22 operations · 10 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: Access fundamental information about your trading account. Retrieve details such as your account ID, currency, and current cash balance.
  name: Trading 212 Accounts API
  slug: trading212-accounts-api
- description: Review your account's trading history. Access detailed records of past orders, dividend payments, and cash transactions, or generate downloadable CSV reports for analysis and record-keeping.
  name: Trading 212 Historical events API
  slug: trading212-historical-events-api
- description: Discover what you can trade. These endpoints provide comprehensive lists of all tradable instruments and the exchanges they belong to, including details like tickers and trading hours.
  name: Trading 212 Instruments API
  slug: trading212-instruments-api
- description: '**⚠️ Order Limitations** * Orders can be executed only in the **main account currency** Place, monitor, and cancel equity trade orders. This section provides the core functionality for programmaticall'
  name: Trading 212 Orders API
  slug: trading212-orders-api
- description: Manage your investment Pies. Use these endpoints to create, view, update, and delete your custom portfolios, making automated and diversified investing simple. **Deprecation notice:** The current stat
  name: Trading 212 Pies (Deprecated) API
  slug: trading212-pies-deprecated-api
- description: Get a real-time overview of all your open positions, including quantity, average price, and current profit or loss.
  name: Trading 212 Positions API
  slug: trading212-positions-api
artifact_total: 83
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trading 212 Public Accounts API
  slug: open-trading212-accounts-api
- collection_type: open
  name: Trading 212 Public Accounts Historical events API
  slug: open-trading212-historical-events-api
- collection_type: open
  name: Trading 212 Public Accounts Instruments API
  slug: open-trading212-instruments-api
- collection_type: open
  name: Trading 212 Public Accounts Orders API
  slug: open-trading212-orders-api
- collection_type: open
  name: Trading 212 Public Accounts Pies (Deprecated) API
  slug: open-trading212-pies-deprecated-api
- collection_type: open
  name: Trading 212 Public Accounts Positions API
  slug: open-trading212-positions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trading212-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trading212-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trading212-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trading212-authentication.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trading212.com/legal-documentation/API-Terms_EN.pdf
- group: auth
  title: ''
  type: Authentication
  url: https://docs.trading212.com/api/section/authentication
- group: operate
  title: ''
  type: RateLimiting
  url: https://docs.trading212.com/api/section/rate-limiting/how-it-works
- group: operate
  title: ''
  type: Community
  url: https://community.trading212.com/
- group: operate
  title: ''
  type: HelpCentre
  url: https://helpcentre.trading212.com/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/trading212/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/trading212/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/trading212/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Trading 212 is a commission-free investing platform offering a REST API for accessing portfolio data, managing orders, viewing positions, retrieving instrument metadata, and accessing account information. The API supports Invest and Stocks ISA account types and provides both a live trading environment and a paper trading (demo) environment for safe development and testing.
examples:
- key_count: 7
  name: Delete_Api_V0_Equity_Orders_Id
  slug: delete_api_v0_equity_orders_id
- key_count: 7
  name: Delete_Api_V0_Equity_Pies_Id
  slug: delete_api_v0_equity_pies_id
- key_count: 7
  name: Get_Api_V0_Equity_Account_Summary
  slug: get_api_v0_equity_account_summary
- key_count: 7
  name: Get_Api_V0_Equity_History_Dividends
  slug: get_api_v0_equity_history_dividends
- key_count: 7
  name: Get_Api_V0_Equity_History_Exports
  slug: get_api_v0_equity_history_exports
- key_count: 7
  name: Get_Api_V0_Equity_History_Orders
  slug: get_api_v0_equity_history_orders
- key_count: 7
  name: Get_Api_V0_Equity_History_Transactions
  slug: get_api_v0_equity_history_transactions
- key_count: 7
  name: Get_Api_V0_Equity_Metadata_Exchanges
  slug: get_api_v0_equity_metadata_exchanges
- key_count: 7
  name: Get_Api_V0_Equity_Metadata_Instruments
  slug: get_api_v0_equity_metadata_instruments
- key_count: 7
  name: Get_Api_V0_Equity_Orders
  slug: get_api_v0_equity_orders
- key_count: 7
  name: Get_Api_V0_Equity_Orders_Id
  slug: get_api_v0_equity_orders_id
- key_count: 7
  name: Get_Api_V0_Equity_Pies
  slug: get_api_v0_equity_pies
- key_count: 7
  name: Get_Api_V0_Equity_Pies_Id
  slug: get_api_v0_equity_pies_id
- key_count: 7
  name: Get_Api_V0_Equity_Positions
  slug: get_api_v0_equity_positions
- key_count: 7
  name: Post_Api_V0_Equity_History_Exports
  slug: post_api_v0_equity_history_exports
- key_count: 7
  name: Post_Api_V0_Equity_Orders_Limit
  slug: post_api_v0_equity_orders_limit
- key_count: 7
  name: Post_Api_V0_Equity_Orders_Market
  slug: post_api_v0_equity_orders_market
- key_count: 7
  name: Post_Api_V0_Equity_Orders_Stop
  slug: post_api_v0_equity_orders_stop
- key_count: 7
  name: Post_Api_V0_Equity_Orders_Stop_Limit
  slug: post_api_v0_equity_orders_stop_limit
- key_count: 7
  name: Post_Api_V0_Equity_Pies
  slug: post_api_v0_equity_pies
- key_count: 7
  name: Post_Api_V0_Equity_Pies_Id
  slug: post_api_v0_equity_pies_id
- key_count: 7
  name: Post_Api_V0_Equity_Pies_Id_Duplicate
  slug: post_api_v0_equity_pies_id_duplicate
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trading212.png
json_schemas:
- name: AccountBucketDetailedResponse
  property_count: 10
  slug: AccountBucketDetailedResponse
- name: AccountBucketInstrumentResult
  property_count: 6
  slug: AccountBucketInstrumentResult
- name: AccountBucketInstrumentsDetailedResponse
  property_count: 2
  slug: AccountBucketInstrumentsDetailedResponse
- name: AccountBucketResultResponse
  property_count: 6
  slug: AccountBucketResultResponse
- name: AccountSummary
  property_count: 5
  slug: AccountSummary
- name: Cash
  property_count: 3
  slug: Cash
- name: DividendDetails
  property_count: 3
  slug: DividendDetails
- name: DuplicateBucketRequest
  property_count: 2
  slug: DuplicateBucketRequest
- name: EnqueuedReportResponse
  property_count: 1
  slug: EnqueuedReportResponse
- name: Exchange
  property_count: 3
  slug: Exchange
- name: Fill
  property_count: 7
  slug: Fill
- name: FillWalletImpact
  property_count: 5
  slug: FillWalletImpact
- name: HistoricalOrder
  property_count: 2
  slug: HistoricalOrder
- name: HistoryDividendItem
  property_count: 11
  slug: HistoryDividendItem
- name: HistoryTransactionItem
  property_count: 5
  slug: HistoryTransactionItem
- name: Instrument
  property_count: 4
  slug: Instrument
- name: InstrumentIssue
  property_count: 2
  slug: InstrumentIssue
- name: InvestmentResult
  property_count: 4
  slug: InvestmentResult
- name: Investments
  property_count: 4
  slug: Investments
- name: LimitRequest
  property_count: 4
  slug: LimitRequest
- name: MarketRequest
  property_count: 3
  slug: MarketRequest
- name: Order
  property_count: 18
  slug: Order
- name: PaginatedResponseHistoricalOrder
  property_count: 2
  slug: PaginatedResponseHistoricalOrder
- name: PaginatedResponseHistoryDividendItem
  property_count: 2
  slug: PaginatedResponseHistoryDividendItem
- name: PaginatedResponseHistoryTransactionItem
  property_count: 2
  slug: PaginatedResponseHistoryTransactionItem
- name: PieRequest
  property_count: 6
  slug: PieRequest
- name: Position
  property_count: 8
  slug: Position
- name: PositionWalletImpact
  property_count: 5
  slug: PositionWalletImpact
- name: PublicReportRequest
  property_count: 3
  slug: PublicReportRequest
- name: ReportDataIncluded
  property_count: 4
  slug: ReportDataIncluded
- name: ReportResponse
  property_count: 6
  slug: ReportResponse
- name: StopLimitRequest
  property_count: 5
  slug: StopLimitRequest
- name: StopRequest
  property_count: 4
  slug: StopRequest
- name: Tax
  property_count: 4
  slug: Tax
- name: TimeEvent
  property_count: 2
  slug: TimeEvent
- name: TimeValidity
  property_count: 0
  slug: TimeValidity
- name: TradableInstrument
  property_count: 10
  slug: TradableInstrument
- name: WorkingSchedule
  property_count: 2
  slug: WorkingSchedule
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 38
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-06-13'
name: Trading 212
nav: Providers
network: true
overview: 'Trading 212 publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Historical events API, Instruments API, and 3 more. Tagged areas include Investing, Finance, Trading, Stocks, and Portfolio.


  The Trading 212 catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Trading 212''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 12
rate_limits:
- limit_count: 18
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trading 212 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trading212-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.3
  delta: 4.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 68.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 31.6
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trading212/refs/heads/main/screenshots/trading212-2026-06-20T195528.png
security:
- kind: authentication
  name: Trading212 Authentication
  slug: trading212-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Trading212 Domain Security
  slug: trading212-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Trading212 Vulnerability Disclosure
  slug: trading212-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: trading212
tags:
- Investing
- Finance
- Trading
- Stocks
- Portfolio
- Commission-Free
- ISA
---
