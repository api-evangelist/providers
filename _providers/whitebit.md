---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 76
  human_in_the_loop: 6
  name: Whitebit Agentic Access
  operation_count: 153
  slug: whitebit-agentic-access
  summary_line: 153 operations · 76 acting · 6 human-in-the-loop
api_count: 6
apis:
- description: Real-time market streams and private account streams over WebSocket (wss://api.whitebit.com/ws).
  name: WhiteBIT WebSocket API
  slug: websocket
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Endpoints for retrieving account information, balances, and transaction history
  name: WhiteBIT Account Endpoints API
  slug: whitebit-account-endpoints-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Address Checker endpoints for B2B address screening
  name: WhiteBIT Address Checker API
  slug: whitebit-address-checker-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: 'OAuth 2.0 authentication endpoints for obtaining and refreshing access tokens. Available Scopes (requested during client setup): - general: General API access - show.userinfo: Access to basic user inf'
  name: WhiteBIT Authentication API
  slug: whitebit-authentication-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: WhiteBIT codes operations
  name: WhiteBIT Codes API
  slug: whitebit-codes-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Endpoints for collateral/margin trading operations
  name: WhiteBIT Collateral Trading API
  slug: whitebit-collateral-trading-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: The Convert API from WhiteBIT — 4 operation(s) for convert.
  name: WhiteBIT Convert API
  slug: whitebit-convert-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Credit line information
  name: WhiteBIT Credit Line API
  slug: whitebit-credit-line-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Fixed crypto lending plans
  name: WhiteBIT Crypto Lending - Fixed API
  slug: whitebit-crypto-lending-fixed-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Flexible crypto lending plans
  name: WhiteBIT Crypto Lending - Flex API
  slug: whitebit-crypto-lending-flex-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Cryptocurrency and fiat deposit operations
  name: WhiteBIT Deposit API
  slug: whitebit-deposit-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Fee information
  name: WhiteBIT Fees API
  slug: whitebit-fees-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: JWT token management
  name: WhiteBIT JWT API
  slug: whitebit-jwt-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Main account balance and operations
  name: WhiteBIT Main Account API
  slug: whitebit-main-account-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Endpoints for querying trading fees
  name: WhiteBIT Market Fee API
  slug: whitebit-market-fee-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Mining pool operations
  name: WhiteBIT Mining Pool API
  slug: whitebit-mining-pool-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Partner-facing endpoints for managing API keys created via the OAuth API key flow. Available on the global server (`https://whitebit.com`) only. The EU server (`https://whitebit.eu`) does not expose t
  name: WhiteBIT OAuth API Keys API
  slug: whitebit-oauth-api-keys-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Public endpoints for market data and trading information
  name: WhiteBIT Public API V1 API
  slug: whitebit-public-api-v1-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Public endpoints for market data, trading information, and platform status
  name: WhiteBIT Public API V4 API
  slug: whitebit-public-api-v4-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Endpoints for spot trading operations
  name: WhiteBIT Spot Trading API
  slug: whitebit-spot-trading-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Sub-account API key management
  name: WhiteBIT Sub-Account API Keys API
  slug: whitebit-sub-account-api-keys-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Sub-account management
  name: WhiteBIT Sub Account API
  slug: whitebit-sub-account-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Balance transfer operations
  name: WhiteBIT Transfer API
  slug: whitebit-transfer-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Travel Rule compliance endpoints for deposits and withdrawals
  name: WhiteBIT Travel Rule API
  slug: whitebit-travel-rule-api
- baseURL: https://whitebit.com
  baseurl_source: spec
  description: Cryptocurrency and fiat withdrawal operations
  name: WhiteBIT Withdraw API
  slug: whitebit-withdraw-api
artifact_total: 92
asyncapis:
- description: 'Subscribe to ADL (Auto-Deleveraging) quantile updates for the account''s open futures positions. The channel does not support query operations — only subscribe, update, and unsubscribe. For a one-time '
  name: WhiteBit ADL Quantile
  slug: whitebit-private-adl-quantile-asyncapi
- description: Authorize WebSocket connection using authentication token. When establishing a WebSocket connection, authorize it via the `authorize` method. After successful authorization, send requests for balances
  name: WhiteBit Private API Authorization
  slug: whitebit-private-authorize-asyncapi
- description: Get and subscribe to margin wallet balance updates. Request for amount on [margin balance](/glossary#balance-collateral). Balance available for [margin trade](/glossary#margin-trading) is equal to `ba
  name: WhiteBit Margin Balance
  slug: whitebit-private-balance-margin-asyncapi
- description: Get and subscribe to [spot balance](/glossary#balance-spotbalance-trade) updates.
  name: WhiteBit Spot Balance
  slug: whitebit-private-balance-spot-asyncapi
- description: Subscribe to borrows updates. The channel does not support query operations — only subscribe, update, and unsubscribe.
  name: WhiteBit Borrows
  slug: whitebit-private-borrows-asyncapi
- description: 'Subscribe to borrows events (margin call and liquidation events). The channel does not support query operations — only subscribe, update, and unsubscribe. ## Event Types | Event Type | Description | |'
  name: WhiteBit Borrows Events
  slug: whitebit-private-borrows-events-asyncapi
- description: Place a margin or futures limit order priced from the current best bid or offer. The role semantics match the spot `order_bbo_place` method, and the same limit order comes back reporting `type` `7`.
  name: WhiteBit Place Margin BBO Order
  slug: whitebit-private-collateral-order-bbo-place-asyncapi
- description: Place a margin or futures limit order over the WebSocket connection. This is the margin counterpart of `order_limit_place`, and like its spot twin it is the only method in the `collateral_*` family th
  name: WhiteBit Place Margin Limit Order
  slug: whitebit-private-collateral-order-limit-place-asyncapi
- description: Place a margin or futures market order over the WebSocket connection. The order opens, extends, reduces, or closes a position at the order book price. Sending the position size on the opposite side is
  name: WhiteBit Place Margin Market Order
  slug: whitebit-private-collateral-order-market-place-asyncapi
- description: Place a One-Cancels-Other pair on a margin or futures market. The pair consists of a limit take-profit leg and a stop-limit stop-loss leg, of which only one can execute. When either leg fills, the oth
  name: WhiteBit Place Margin OCO Order
  slug: whitebit-private-collateral-order-oco-place-asyncapi
- description: 'Place a One-Triggers-Other group on a margin or futures market. An entry order arms its own exit: once the entry fills, the engine creates a take-profit, a stop-loss, or an OCO pair of both. The param'
  name: WhiteBit Place Margin OTO Order
  slug: whitebit-private-collateral-order-oto-place-asyncapi
- description: Place a margin or futures stop order that becomes a BBO order. The order waits as `type` `9` with `price` `"0"`, then prices itself from the order book when the trigger fires.
  name: WhiteBit Place Margin Stop-BBO Order
  slug: whitebit-private-collateral-order-stop-bbo-place-asyncapi
- description: Place a margin or futures stop-limit order over the WebSocket connection. The order waits outside the order book until the market reaches `activation_price`. On activation the engine places a margin l
  name: WhiteBit Place Margin Stop-Limit Order
  slug: whitebit-private-collateral-order-stop-limit-place-asyncapi
- description: 'Place a margin or futures stop-market order over the WebSocket connection. This is the workhorse protective stop: the trigger fires a margin market order. Because `amount` is [stock](/glossary#stock),'
  name: WhiteBit Place Margin Stop-Market Order
  slug: whitebit-private-collateral-order-stop-market-place-asyncapi
- description: Attach a take-profit and a stop-loss to an existing margin or futures position. The pair binds to the position rather than to an order. It carries no size of its own and always exits whatever is open,
  name: WhiteBit Place Margin Take-Profit and Stop-Loss
  slug: whitebit-private-collateral-order-tpsl-place-asyncapi
- description: 'Get and subscribe to deals/trades updates. **Important**: [Market](/glossary#market) should exist. The maximum limit is 100. **Note**: Update events use ARRAY format, not object format.'
  name: WhiteBit Deals
  slug: whitebit-private-deals-asyncapi
- description: 'Subscribe to margin positions events (margin call and liquidation events). The channel does not support query operations — only subscribe, update, and unsubscribe. ## Event Types | Event Type | Descri'
  name: WhiteBit Margin Positions Events
  slug: whitebit-private-margin-positions-events-asyncapi
- description: Place a spot limit order priced from the current best bid or offer. The client chooses the role and the engine chooses the price, which removes the need to read the order book first. The `bbo_role` pa
  name: WhiteBit Place Spot BBO Order
  slug: whitebit-private-order-bbo-place-asyncapi
- description: Withdraw every order the authorized user holds on one market, filtered by trading type. One market per call — no all-markets form exists, so flattening everything means looping over the markets in use
  name: WhiteBit Cancel All Orders
  slug: whitebit-private-order-cancel-all-asyncapi
- description: Cancel a single order over the WebSocket connection. The method covers resting limit orders, plain conditional stop orders, and individual TPSL legs, across spot, margin, and futures markets. The resp
  name: WhiteBit Cancel Order
  slug: whitebit-private-order-cancel-asyncapi
- description: Cancel an OCO or OTO group in one call. Pass the group id from the placement response and every leg is withdrawn atomically. The response mirrors the placement response — same shape, same `type` value
  name: WhiteBit Cancel Conditional Order Group
  slug: whitebit-private-order-cancel-conditional-asyncapi
- description: Place a spot limit order over the WebSocket connection. A limit order rests in the order book at the specified price until it is matched or canceled. This method accepts the full spot execution-flag s
  name: WhiteBit Place Spot Limit Order
  slug: whitebit-private-order-limit-place-asyncapi
- description: Place a spot market order over the WebSocket connection. A market order matches immediately against the order book at the available prices and never rests. The response is already terminal. The unit o
  name: WhiteBit Place Spot Market Order
  slug: whitebit-private-order-market-place-asyncapi
- description: 'Place a spot market order sized in the base asset on both sides. This method behaves like `order_market_place` with one difference: `amount` is always [stock](/glossary#stock), on a buy as well as on '
  name: WhiteBit Place Spot Market Order Sized in Stock
  slug: whitebit-private-order-market-stock-place-asyncapi
- description: Change the size, price, or trigger of a live order over the WebSocket connection. The method works across spot, margin, and futures markets — no `collateral_` variant exists. The `market` parameter ro
  name: WhiteBit Modify Order
  slug: whitebit-private-order-modify-asyncapi
- description: Place a spot stop order that turns into a BBO order. The price is resolved from the order book at activation time rather than at placement, which is why `price` stays `"0"` while the order waits.
  name: WhiteBit Place Spot Stop-BBO Order
  slug: whitebit-private-order-stop-bbo-place-asyncapi
- description: Place a spot stop-limit order over the WebSocket connection. The order waits outside the order book until the market reaches `activation_price`. On activation the engine places a limit order at `price
  name: WhiteBit Place Spot Stop-Limit Order
  slug: whitebit-private-order-stop-limit-place-asyncapi
- description: Place a spot stop-market order over the WebSocket connection. The order waits outside the order book until the market reaches `activation_price`, then fires a market order. Because the resulting order
  name: WhiteBit Place Spot Stop-Market Order
  slug: whitebit-private-order-stop-market-place-asyncapi
- description: Place a spot stop-market order sized in the base asset on both sides. The trigger semantics match `order_stop_market_place`; only the unit of `amount` differs. Here `amount` is always [stock](/glossar
  name: WhiteBit Place Spot Stop-Market Order Sized in Stock
  slug: whitebit-private-order-stop-market-stock-place-asyncapi
- description: 'Get and subscribe to executed orders updates. **Important**: [Market](/glossary#market) should exist. The maximum limit is 100. ## Filter Options | Filter | Executed orders | | ------ | --------------'
  name: WhiteBit Orders Executed
  slug: whitebit-private-orders-executed-asyncapi
- description: 'Query and subscribe to [active orders](/glossary#active-orders) (orders not yet executed). The WebSocket methods use `ordersPending_*` naming for API compatibility. **Important**: [Market](/glossary#m'
  name: WhiteBit Orders Pending
  slug: whitebit-private-orders-pending-asyncapi
- description: Subscribe to positions updates. The channel does not support query operations — only subscribe, update, and unsubscribe.
  name: WhiteBit Positions
  slug: whitebit-private-positions-asyncapi
- description: Real-time best bid/ask (BBO) price and quantity updates. Provides instant snapshots followed by incremental updates.
  name: WhiteBit Book Ticker
  slug: whitebit-public-book-ticker-asyncapi
- description: Real-time order book depth data. Provides full and partial updates of bid/ask levels with support for multiple subscription parameters.
  name: WhiteBit Order Book Depth
  slug: whitebit-public-depth-asyncapi
- description: Historical and real-time kline (candlestick) data for trading pairs. Supports both one-time queries and subscription-based updates.
  name: WhiteBit Kline Data
  slug: whitebit-public-kline-asyncapi
- description: Real-time last price information for trading pairs. Supports both one-time queries and subscription-based updates.
  name: WhiteBit Last Price
  slug: whitebit-public-lastprice-asyncapi
- description: Market statistics for a specified time period including open, close, high, low prices and volume data.
  name: WhiteBit Market Statistics
  slug: whitebit-public-market-asyncapi
- description: Market statistics for the current day in UTC timezone. Includes open, high, low prices and volume data since midnight UTC.
  name: WhiteBit Market Today Statistics
  slug: whitebit-public-market-today-asyncapi
- description: Subscribe to mark price, index price, and funding rate updates for futures markets. The channel does not support query operations — only subscribe, update, and unsubscribe. For a one-time snapshot, us
  name: WhiteBit Premium Index
  slug: whitebit-public-premium-index-asyncapi
- description: Service operations including health checks (ping) and server time
  name: WhiteBit Service Operations
  slug: whitebit-public-service-asyncapi
- description: Real-time market trade data. Supports both historical trade queries and real-time trade subscriptions for specific markets or all markets.
  name: WhiteBit Market Trades
  slug: whitebit-public-trades-asyncapi
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/agentic-access/whitebit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/whitebit-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/rules/whitebit-rules.yml
  title: ''
  type: Spectral
  url: rules/whitebit-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/json-ld/whitebit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/whitebit-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/vocabulary/whitebit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/whitebit-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/data-model/whitebit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whitebit-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/conventions/whitebit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/whitebit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/conventions/whitebit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/whitebit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/errors/whitebit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whitebit-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/conformance/whitebit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whitebit-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/llms/whitebit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whitebit-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/well-known/whitebit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whitebit-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/hosts/whitebit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whitebit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/vendors/whitebit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whitebit-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whitebit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whitebit.com/terms/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://whitebit.com/m/media
- group: company
  title: ''
  type: Blog
  url: https://blog.whitebit.com/en?utm_source=whitebit_exchange
- group: start
  title: ''
  type: Login
  url: https://whitebit.com/auth/login
- group: start
  title: ''
  type: SignUp
  url: https://whitebit.com/auth/register
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/authentication/whitebit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/whitebit-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/security/whitebit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whitebit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whitebit.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.whitebit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.whitebit.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.whitebit.com/platform/overview
- group: agent
  title: ''
  type: LLMs
  url: https://docs.whitebit.com/llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://status.whitebit.com
- group: operate
  title: ''
  type: Support
  url: https://help.whitebit.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whitebit-exchange
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/whitebit-exchange/docs
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/mcp/whitebit-mcp.yml
  title: ''
  type: MCP
  url: mcp/whitebit-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.whitebit.com/mcp
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/packages/whitebit-packages.yml
  title: ''
  type: Packages
  url: packages/whitebit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/packages/whitebit-packages.yml
  title: ''
  type: SDKs
  url: packages/whitebit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whitebit/refs/heads/main/cli/whitebit-cli.yml
  title: ''
  type: CLI
  url: cli/whitebit-cli.yml
created: '2026-10-13'
description: WhiteBIT is a European centralized cryptocurrency exchange offering spot, collateral (margin/futures) trading, and account/wallet services, with public and private REST APIs (v1/v4), OAuth 2.0, and a WebSocket API.
image: https://static.whitebit.com/img/og-image-en.png
json_schemas:
- name: Asset
  property_count: 18
  slug: whitebit-asset
- name: BulkOrderItem
  property_count: 11
  slug: whitebit-bulk-order-item
- name: CheckHistoryResponse
  property_count: 3
  slug: whitebit-check-history-response
- name: CheckResultResponse
  property_count: 5
  slug: whitebit-check-result-response
- name: ConditionalOrderLeg
  property_count: 21
  slug: whitebit-conditional-order-leg
- name: CreateCheckBalanceError
  property_count: 1
  slug: whitebit-create-check-balance-error
- name: CreateCheckResponse
  property_count: 1
  slug: whitebit-create-check-response
- name: FeeInfo
  property_count: 9
  slug: whitebit-fee-info
- name: FuturesMarket
  property_count: 23
  slug: whitebit-futures-market
- name: LimitOrderRequest
  property_count: 13
  slug: whitebit-limit-order-request
- name: MiningReward
  property_count: 13
  slug: whitebit-mining-reward
- name: OcoOrderLeg
  property_count: 22
  slug: whitebit-oco-order-leg
- name: OrderResponse
  property_count: 25
  slug: whitebit-order-response
- name: OrderbookResponse
  property_count: 4
  slug: whitebit-orderbook-response
- name: RefundHistoryRecord
  property_count: 13
  slug: whitebit-refund-history-record
- name: StopLimitOrderRequest
  property_count: 10
  slug: whitebit-stop-limit-order-request
- name: SubAccountApiKey
  property_count: 10
  slug: whitebit-sub-account-api-key
- name: SupportedAsset
  property_count: 2
  slug: whitebit-supported-asset
- name: TransactionHistory
  property_count: 16
  slug: whitebit-transaction-history
- name: WithdrawRequest
  property_count: 14
  slug: whitebit-withdraw-request
jsonld:
- class_count: 56
  name: Whitebit Context
  property_count: 195
  slug: whitebit-context
layout: provider
mcp_servers:
- description: ''
  name: WhiteBIT MCP Server
  slug: mcp
modified: '2026-10-13'
name: WhiteBIT
nav: Providers
network: true
overview: 'WhiteBIT publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including WebSocket API, Account Endpoints API, Address Checker API, and 22 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and WebSocket.


  The WhiteBIT catalog on APIs.io includes 41 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  WhiteBIT''s developer surface includes engineering blog, signup flow, authentication, documentation, API reference, getting-started guide, support, and 28 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: WhiteBIT API Rules
  rule_count: 14
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 4
  slug: whitebit-rules
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 68.5
    developer_ergonomics: 61.9
    discoverability: 73.3
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Whitebit Authentication
  slug: whitebit-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Whitebit Domain Security
  slug: whitebit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: whitebit
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- WebSocket
website: https://whitebit.com
---
