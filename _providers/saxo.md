---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 146
  human_in_the_loop: 3
  name: Saxo Agentic Access
  operation_count: 301
  slug: saxo-agentic-access
  summary_line: 301 operations · 146 acting · 3 human-in-the-loop
api_count: 80
apis:
- description: The Saxo Bank FIX API delivers institutional-grade multi-asset liquidity via the industry-standard Financial Information eXchange (FIX) protocol. It provides a stable, fast, and fully documented elect
  name: Saxo Bank FIX Trading API
  slug: saxo-bank-fix-trading-api
- description: Provides account summary values, on each individual account and rolled up..
  name: Saxo Bank Account Values API
  slug: saxo-account-values-api
- description: 'End points serving account groups. The set of account groups is restricted by the supplied query parameters as well as whether or not the identity represented by the authorization token has access to '
  name: Saxo Bank AccountGroups API
  slug: saxo-accountgroups-api
- description: Provide services to get account template and create account.
  name: Saxo Bank Accounts API
  slug: saxo-accounts-api
- description: Endpoints serving strategies information.
  name: Saxo Bank AlgoStrategies API
  slug: saxo-algostrategies-api
- description: Add or modify allocation keys.
  name: Saxo Bank Allocation Keys API
  slug: saxo-allocation-keys-api
- description: Provides OAuth app secrets related endpoints
  name: Saxo Bank Apps API
  slug: saxo-apps-api
- description: End point for querying order activities
  name: Saxo Bank Audit - OrderActivities API
  slug: saxo-audit-orderactivities-api
- description: Read-only endpoint serving client and account balances. The client or account balance is identified by the supplied ClientKey, AccountGroupKey or AccountKey. Access to balance data is further restrict
  name: Saxo Bank Balances API
  slug: saxo-balances-api
- description: This endpoint provides the functionality to manage beneficiary instructions
  name: Saxo Bank Cash Management - Beneficiary Instructions API
  slug: saxo-cash-management-beneficiary-instructions-api
- description: This endpoint provides the functionality necessary to allow a client to withdraw money from his account
  name: Saxo Bank CashManagement - Cash Withdrawal API
  slug: saxo-cashmanagement-cash-withdrawal-api
- description: Provides endpoints for cash available for withdrawal.
  name: Saxo Bank CashManagement - Cash Withdrawal Limits API
  slug: saxo-cashmanagement-cash-withdrawal-limits-api
- description: This endpoint provides the functionality necessary for a client to transfer money between different accounts all belonging to the same client.
  name: Saxo Bank CashManagement - Inter Account Transfer API
  slug: saxo-cashmanagement-inter-account-transfer-api
- description: Get wiretransfer instructions for specified client and account
  name: Saxo Bank CashManagement - WireTransfers API
  slug: saxo-cashmanagement-wiretransfers-api
- description: Allows you to set up subscriptions for streamed charts data.
  name: Saxo Bank Charts API
  slug: saxo-charts-api
- description: Provides subscription endpoints to stream client related events.
  name: Saxo Bank Client Activities API
  slug: saxo-client-activities-api
- description: The Client Renewals resource is only implemented in LIVE environment. Implementation in simulation system only returns sample data and response. Provides functionality to get and update client data in
  name: Saxo Bank Client Renewals API
  slug: saxo-client-renewals-api
- description: End point for accessing summary information for a specified client.
  name: Saxo Bank ClientInfo API
  slug: saxo-clientinfo-api
- description: End points serving client related resources The set of clients is restricted by the supplied query parameters as well as whether or not the identity represented by the authorization token has access t
  name: Saxo Bank Clients API
  slug: saxo-clients-api
- description: 'Read only end points serving closed positions and the underlying closed positions making up the net closed position. The set of closed positions is restricted by the supplied query parameters as well '
  name: Saxo Bank ClosedPositions API
  slug: saxo-closedpositions-api
- description: The Cm API from Saxo Bank — 1 operation(s) for cm.
  name: Saxo Bank Cm API
  slug: saxo-cm-api
- description: Provides information about countries.
  name: Saxo Bank Countries API
  slug: saxo-countries-api
- description: End points serving culture information.
  name: Saxo Bank Cultures API
  slug: saxo-cultures-api
- description: Provides information about currencies supported by Saxo Bank.
  name: Saxo Bank Currencies API
  slug: saxo-currencies-api
- description: Provides information about currency pairs supported by Saxo Bank.
  name: Saxo Bank CurrencyPairs API
  slug: saxo-currencypairs-api
- description: This collection provides endpoints for client diagnostics and can be used to verify HTTP methods. An access token is not required for requests to any of the below endpoints. However, if a token is pro
  name: Saxo Bank Diagnostics API
  slug: saxo-diagnostics-api
- description: Provide services to save\upload documents.
  name: Saxo Bank Documents API
  slug: saxo-documents-api
- description: Endpoints for election instructions
  name: Saxo Bank Elections API
  slug: saxo-elections-api
- description: Find Corporate action voluntary events.
  name: Saxo Bank Events API
  slug: saxo-events-api
- description: End points serving exchange information.
  name: Saxo Bank Exchanges API
  slug: saxo-exchanges-api
- description: Read only end points serving exposure of positions. The exposure results are restricted by the supplied query parameters as well as whether or not the identity represented by the authorization token h
  name: Saxo Bank Exposure API
  slug: saxo-exposure-api
- description: Extended Account provides abstraction on top of accounts and account risk-profiles to make them appear as one Account. It gives semblance of Bink style Secutity Account where it is possible to book tr
  name: Saxo Bank ExtendedAccounts API
  slug: saxo-extendedaccounts-api
- description: Provide feature flags related endpoints.
  name: Saxo Bank Feature Flags API
  slug: saxo-feature-flags-api
- description: Provides endpoints for querying availability of features.
  name: Saxo Bank Features API
  slug: saxo-features-api
- description: Account Statement Report.
  name: Saxo Bank Historical Report Data - Account Statement API
  slug: saxo-historical-report-data-account-statement-api
- description: Aggregated Amounts Report Data.
  name: Saxo Bank Historical Report Data - Aggregated amounts API
  slug: saxo-historical-report-data-aggregated-amounts-api
- description: Bookings Report Data.
  name: Saxo Bank Historical Report Data - Bookings API
  slug: saxo-historical-report-data-bookings-api
- description: Closed Positions Report Data.
  name: Saxo Bank Historical Report Data - Closed positions API
  slug: saxo-historical-report-data-closed-positions-api
- description: Portfolio Report
  name: Saxo Bank Historical Report Data - Portfolio Management API
  slug: saxo-historical-report-data-portfolio-management-api
- description: Trade Details Report.
  name: Saxo Bank Historical Report Data - Trade Details API
  slug: saxo-historical-report-data-trade-details-api
- description: Trades Report Data.
  name: Saxo Bank Historical Report Data - Trades API
  slug: saxo-historical-report-data-trades-api
- description: Trades Executed Report.
  name: Saxo Bank Historical Report Data - Trades Executed API
  slug: saxo-historical-report-data-trades-executed-api
- description: End points serving historical positions (a.k.a. closed positions)
  name: Saxo Bank HistoricalPositions API
  slug: saxo-historicalpositions-api
- description: Endpoints for client holdings
  name: Saxo Bank Holdings API
  slug: saxo-holdings-api
- description: Provides end points for polling and subscribing to Info prices. Info prices are primarily intended to serve application scenarios, where the user is anonymous, or where an application wants to setup a
  name: Saxo Bank Info Prices API
  slug: saxo-info-prices-api
- description: Provides endpoints that returns a document for requested instrument.
  name: Saxo Bank Instrument Document API
  slug: saxo-instrument-document-api
- description: End points serving instrument resources.
  name: Saxo Bank Instruments API
  slug: saxo-instruments-api
- description: InteractiveIdVerificationV1Controller
  name: Saxo Bank InteractiveIdVerification API
  slug: saxo-interactiveidverification-api
- description: End points for fetching and updating investment items.
  name: Saxo Bank Investments API
  slug: saxo-investments-api
- description: End points serving ISO 639-1 language information
  name: Saxo Bank Languages API
  slug: saxo-languages-api
- description: Provides end points for polling and subscribing to messages which should be displayed to the user. Only messages, which have not yet been marked as 'seen' will be returned. The structure in this refer
  name: Saxo Bank Messages API
  slug: saxo-messages-api
- description: 'Read only end points serving net positions and the positions making up the net position. The set of net positions is restricted by the supplied query parameters as well as whether or not the identity '
  name: Saxo Bank NetPositions API
  slug: saxo-netpositions-api
- description: 'The Options Chain is a construct made specifically for displaying a number of options (ETOs or FxOptions) in a classic "Options Board" that orders the options according to Expiries and Strikes. It is '
  name: Saxo Bank Options Chain API
  slug: saxo-options-chain-api
- description: Read only end points serving orders.
  name: Saxo Bank Orders API
  slug: saxo-orders-api
- description: Provides partner bulk booking related endpoints.
  name: Saxo Bank Partner Bulk Bookings API
  slug: saxo-partner-bulk-bookings-api
- description: Provides AssetTransfers related endpoints.
  name: Saxo Bank Partner - Cash Transfer API
  slug: saxo-partner-cash-transfer-api
- description: Provides endpoints for cash available for transfer.
  name: Saxo Bank Partner - Cash Transfer Limits API
  slug: saxo-partner-cash-transfer-limits-api
- description: IB can credit their client account on pre-advice
  name: Saxo Bank Partner - Prefunding API
  slug: saxo-partner-prefunding-api
- description: Provides performance metrics for historical positions.
  name: Saxo Bank Performance API
  slug: saxo-performance-api
- description: Read only end points serving individual positions. The set of positions is restricted by the supplied query parameters as well as whether or not the identity represented by the authorization token has
  name: Saxo Bank Positions API
  slug: saxo-positions-api
- description: Provides endpoints for managing price alert definitions and notification settings.
  name: Saxo Bank Price Alerts API
  slug: saxo-price-alerts-api
- description: 'Provides end points for polling and subscribing to a stream of potentially tradable prices. Compared to "InfoPrices": * A single price subscription can only return prices for a single valid instrument'
  name: Saxo Bank Prices API
  slug: saxo-prices-api
- description: Get proxy voting events or subscribe for proxy voting
  name: Saxo Bank Proxy Voting API
  slug: saxo-proxy-voting-api
- description: Allows a user to provide a list of securities to be transfereed into or out of Saxo Bank
  name: Saxo Bank Securities Transfers API
  slug: saxo-securities-transfers-api
- description: Session management endpoints.
  name: Saxo Bank Sessions API
  slug: saxo-sessions-api
- description: The Signups resource is only implemented in LIVE environment. Implementation in simulation system only returns sample data and response. Full client registrations. The Signups resource is intended for
  name: Saxo Bank Signups API
  slug: saxo-signups-api
- description: Provides end points for retrieving standard dates.
  name: Saxo Bank StandardDates API
  slug: saxo-standarddates-api
- description: A Standing instruction is a rule that defines how an election should be applied automatically. Standing instructions only applicable to event types Dividend Reinvestment (DRIP) and Dividend Option (DV
  name: Saxo Bank Standing Instructions API
  slug: saxo-standing-instructions-api
- description: Central Subscriptions Management (CSM) providing broadcast commanding such as delete of multiple subscriptions in a single request.
  name: Saxo Bank Subscriptions API
  slug: saxo-subscriptions-api
- description: Endpoints to support upload and retrieval of client support cases
  name: Saxo Bank Support - Cases API
  slug: saxo-support-cases-api
- description: Provides information about time zones supported by Saxo Bank.
  name: Saxo Bank TimeZones API
  slug: saxo-timezones-api
- description: End points for fetching follower information.
  name: Saxo Bank Trade Followers API
  slug: saxo-trade-followers-api
- description: End points for fetching tradeLeader information.
  name: Saxo Bank Trade Leaders API
  slug: saxo-trade-leaders-api
- description: Provides trading conditions for regular instruments
  name: Saxo Bank Trading Conditions API
  slug: saxo-trading-conditions-api
- description: Provides trading conditions for contract options
  name: Saxo Bank Trading Conditions - Contract Option API
  slug: saxo-trading-conditions-contract-option-api
- description: Provides pre-trade cost illustration for regular instruments
  name: Saxo Bank Trading Conditions - Cost API
  slug: saxo-trading-conditions-cost-api
- description: 'This resource provides access to various data-granularities of unsettled amounts of the requesting entity. The endpoints each provide a subset of the amounts structured in the hiearchy: Exchange - Cur'
  name: Saxo Bank Unsettled Amounts API
  slug: saxo-unsettled-amounts-api
- description: Provides non stream price update endpoint
  name: Saxo Bank Update pricing API
  slug: saxo-update-pricing-api
- description: Endpoints for users.
  name: Saxo Bank User API
  slug: saxo-user-api
- description: Provides services for resetting user passwords.
  name: Saxo Bank Users API
  slug: saxo-users-api
artifact_total: 88
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/saxo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saxo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/saxo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/saxo-scopes.yml
created: '2026-06-13'
description: Saxo Bank provides an OpenAPI-based REST platform giving developers access to all resources and functionality required to build high-performance multi-asset trading applications. The API covers trading equities, forex, options, futures, and other instruments; real-time and streaming market data; order management; portfolio and account administration; reference data on thousands of tradable instruments; and event notification services. It is the same infrastructure that powers SaxoTraderGO, SaxoTraderPRO, and a broad ecosystem of third-party integrations including TradingView and MultiCharts.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saxo.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Saxo Bank
nav: Providers
network: true
overview: 'Saxo Bank publishes 79 APIs on the [APIs.io](https://apis.io/) network, including Account Values API, AccountGroups API, Accounts API, and 76 more. Tagged areas include Investment Banking, Trading, Equities, Forex, and Options.


  The Saxo Bank catalog on APIs.io includes 1 JSON-LD context.


  Saxo Bank''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 95
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
scopes:
- name: Saxo Scopes
  scope_count: 0
  slug: saxo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 79
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saxo/refs/heads/main/screenshots/saxo-2026-06-20T193446.png
security:
- kind: authentication
  name: Saxo Authentication
  slug: saxo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Saxo Domain Security
  slug: saxo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saxo
tags:
- Investment Banking
- Trading
- Equities
- Forex
- Options
- Futures
- Market Data
- Portfolio Management
- Orders
- Financial
---
