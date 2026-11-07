---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: wss://ws.gemini.com
  baseurl_source: declared
  description: 'The production Gemini WebSocket API at wss://ws.gemini.com: request/response methods, market data streams (book ticker, partial and differential depth, trades), authenticated account streams for order'
  name: Gemini WebSocket API
  slug: gemini-websocket-api
- description: The official first-party Model Context Protocol server from the gemini/developer-platform monorepo, exposing Gemini market data, orders, funds, account, margin, staking, prediction-market and native-O
  name: Gemini MCP Server
  slug: gemini-mcp-server
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Account Administration API from Gemini Trust Company — 5 operation(s) for account administration.
  name: Gemini Trust Company Account Administration API
  phrasing_intents:
  - id: getAccountDetail
    intent: Get details about an exchange account
    question: Which users and country code are attached to my Gemini account?
  - id: createNewAccount
    intent: Create a new account in the master group
    question: How do I add a new sub-account to my master group with an API key?
  - id: renameAccount
    intent: Rename an account or change its shortname
    question: Can I change the display name of an existing account in my group?
  - id: listAccountsInGroup
    intent: List the accounts in a master group
    question: What accounts exist under my master API key's group?
  - id: getRoles
    intent: Check which role an API key has
    question: What role is assigned to the API key I'm using?
  phrasing_ops: 5
  slug: gemini-trust-account-administration-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Clearing API from Gemini Trust Company — 8 operation(s) for clearing.
  name: Gemini Trust Company Clearing API
  phrasing_intents:
  - id: createNewClearingOrder
    intent: Submit a new clearing order to a counterparty
    question: How do I settle an off-exchange trade with a counterparty through Gemini Clearing?
  - id: getClearingOrder
    intent: Check the status of a clearing order
    question: Has my clearing order been confirmed or settled yet?
  - id: cancelClearingOrder
    intent: Cancel a pending clearing order
    question: Can I withdraw a clearing order before the counterparty confirms it?
  - id: confirmClearingOrder
    intent: Confirm a clearing order as the counterparty
    question: A counterparty sent me a clearing order. How do I accept it?
  - id: listClearingOrders
    intent: List my clearing orders with filters
    question: Which of my clearing orders are still waiting on a counterparty?
  - id: listClearingBrokers
    intent: List broker-facilitated clearing orders
    question: As a broker, which clearing orders have I arranged between customers?
  - id: createNewBrokerOrder
    intent: Broker a clearing trade between two customers
    question: Can a broker set up a trade between two Gemini customers that both sides must confirm?
  - id: listClearingTrades
    intent: List settled clearing trades
    question: Which clearing trades have actually settled on my accounts?
  phrasing_ops: 8
  slug: gemini-trust-clearing-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: Public endpoints for discovering and inspecting combo contracts, plus an authenticated endpoint to create or retrieve a canonical combo. Combos are multi-leg contracts; order entry uses the same place
  name: Gemini Trust Company Combos API
  phrasing_intents:
  - id: listCombos
    intent: List combo prediction contracts
    question: What combo contracts are active on Gemini's prediction markets right now?
  - id: createCombo
    intent: Create a combo from several contract legs
    question: How do I bundle two to six prediction contracts into one combo?
  - id: getComboByInstrumentSymbol
    intent: Get a combo contract by its instrument symbol
    question: What legs make up a specific combo contract?
  phrasing_ops: 3
  slug: gemini-trust-combos-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Derivatives API from Gemini Trust Company — 6 operation(s) for derivatives.
  name: Gemini Trust Company Derivatives API
  phrasing_intents:
  - id: getAccountMargin
    intent: Get account margin for a perpetuals symbol
    question: How much margin am I using on my perpetuals account for a given pair?
  - id: listFundingPayments
    intent: List perpetual funding payments
    question: Which funding payments have I paid or received on my perpetual positions?
  - id: getFundingPaymentReportFile
    intent: Download funding payment report as Excel
    question: Can I export my funding payment history as a spreadsheet?
  - id: getFundingPaymentReportJson
    intent: Get funding payment report as JSON
    question: Is there a JSON version of the funding payment report I can parse in code?
  - id: getOpenPositions
    intent: List open derivatives positions
    question: What perpetual positions do I currently have open?
  - id: getRiskStats
    intent: Get risk stats for a perpetual contract
    question: What are the current risk statistics for the BTC perpetual?
  phrasing_ops: 6
  slug: gemini-trust-derivatives-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Fund Management API from Gemini Trust Company — 16 operation(s) for fund management.
  name: Gemini Trust Company Fund Management API
  phrasing_intents:
  - id: getAvailableBalances
    intent: Get available balances per currency
    question: How much of each currency is available to trade or withdraw in my account?
  - id: getNotionalBalances
    intent: Get balances valued in a chosen currency
    question: What are my holdings worth in US dollars right now?
  - id: listDepositAddresses
    intent: List deposit addresses on a network
    question: Which deposit addresses have I already generated on Ethereum?
  - id: createNewDepositAddress
    intent: Generate a new crypto deposit address
    question: How do I get a fresh address to deposit crypto into my account?
  - id: listPastTransfers
    intent: List past deposits and withdrawals
    question: What deposits and withdrawals have gone through my account recently?
  - id: listCustodyFeeTransfers
    intent: List custody fee charges
    question: What custody fees have been charged to my account?
  - id: getGasFeeEstimation
    intent: Estimate the network fee for a withdrawal
    question: How much gas will it cost to withdraw ETH to an outside address?
  - id: withdrawCryptoFunds
    intent: Withdraw crypto to an external address
    question: How do I send bitcoin from my exchange account to my own wallet?
  phrasing_ops: 16
  slug: gemini-trust-fund-management-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Instant API from Gemini Trust Company — 2 operation(s) for instant.
  name: Gemini Trust Company Instant API
  phrasing_intents:
  - id: getInstantQuote
    intent: Get a quote for an instant buy or sell
    question: What price would I get for an instant buy of bitcoin with $500?
  - id: executeInstantOrder
    intent: Execute an instant order from a quote
    question: How do I lock in an instant quote I just received?
  phrasing_ops: 2
  slug: gemini-trust-instant-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Margin Trading API from Gemini Trust Company — 3 operation(s) for margin trading.
  name: Gemini Trust Company Margin Trading API
  phrasing_intents:
  - id: getMarginAccount
    intent: Get a spot margin account summary
    question: How close is my spot margin account to liquidation?
  - id: getMarginRates
    intent: Get margin borrowing interest rates
    question: What interest rate do I pay to borrow assets on margin?
  - id: previewMarginOrder
    intent: Preview how an order affects margin risk
    question: Can I see how a trade would change my margin risk before placing it?
  phrasing_ops: 3
  slug: gemini-trust-margin-trading-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Market Data API from Gemini Trust Company — 15 operation(s) for market data.
  name: Gemini Trust Company Market Data API
  phrasing_intents:
  - id: listSymbols
    intent: List all tradable symbols
    question: Which trading pairs can I trade on Gemini?
  - id: getSymbolDetails
    intent: Get order size and tick rules for a symbol
    question: What is the minimum order size and tick size for a trading pair?
  - id: getAssetsForNetwork
    intent: List tokens enabled on a blockchain network
    question: Which tokens can my account deposit or withdraw on the Solana network?
  - id: getTokenNetworkV2
    intent: Get the networks a token supports
    question: On which blockchains can I deposit or withdraw USDC?
  - id: getTicker
    intent: Get the latest bid, ask and last price
    question: What is the current bid, ask and last trade for BTCUSD?
  - id: getCurrentOrderBook
    intent: Get the current order book for a symbol
    question: What bids and asks are resting on the book for ETHUSD right now?
  - id: listTrades
    intent: List recent public trades for a symbol
    question: What trades have executed recently on the BTCUSD market?
  - id: listPrices
    intent: Get the price feed for all pairs
    question: Can I get current prices for every pair in one request?
  phrasing_ops: 15
  slug: gemini-trust-market-data-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: Public endpoints for browsing prediction markets. **Market Data:** Use these REST endpoints to discover active events and each contract's `instrumentSymbol` (e.g., `GEMI-FEDJAN26-DN25`). For active tr
  name: Gemini Trust Company Markets API
  phrasing_intents:
  - id: listEvents
    intent: Browse and search prediction market events
    question: What prediction market events can I bet on right now?
  - id: getEvent
    intent: Get a prediction market event by ticker
    question: What contracts are available inside a specific event?
  - id: getEventStrike
    intent: Get the strike price for an event
    question: What strike price was set for a crypto Up/Down contract?
  - id: listNewlyListedEvents
    intent: List events listed in the last 24 hours
    question: Which prediction events were added in the last day?
  - id: listRecentlySettledEvents
    intent: List events settled in the last 24 hours
    question: Which prediction markets resolved in the last day?
  - id: listUpcomingEvents
    intent: List approved events that have not launched
    question: What prediction markets are approved but not trading yet?
  - id: getCategories
    intent: List prediction market event categories
    question: What categories of prediction events exist?
  phrasing_ops: 7
  slug: gemini-trust-markets-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The OAuth API from Gemini Trust Company — 1 operation(s) for oauth.
  name: Gemini Trust Company OAuth API
  phrasing_intents:
  - id: revokeOAuthToken
    intent: Revoke the current OAuth access token
    question: How do I invalidate an OAuth access token my app no longer needs?
  phrasing_ops: 1
  slug: gemini-trust-oauth-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Orders API from Gemini Trust Company — 11 operation(s) for orders.
  name: Gemini Trust Company Orders API
  phrasing_intents:
  - id: createNewOrder
    intent: Place a new exchange limit order
    question: How do I place a limit order to buy bitcoin at a set price?
  - id: cancelOrder
    intent: Cancel one exchange order
    question: Can I cancel a single open order by its order ID?
  - id: cancelAllActiveOrders
    intent: Cancel every open order on the account
    question: How do I cancel all my open orders at once, including ones placed in the web UI?
  - id: cancelAllSessionOrders
    intent: Cancel orders opened by this API session
    question: Can I cancel only the orders this API session opened and leave the rest?
  - id: getOrderStatus
    intent: Check the status of an exchange order
    question: Has my order filled yet, or is it still open?
  - id: listActiveOrders
    intent: List my open exchange orders
    question: Which of my exchange orders are still open?
  - id: listPastOrders
    intent: List closed exchange orders
    question: Where can I see orders that have already closed?
  - id: listPastTrades
    intent: List my executed trades
    question: What trades have I executed on ETHUSD?
  phrasing_ops: 11
  slug: gemini-trust-orders-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: Authenticated endpoints for viewing positions and order history. Use REST positions for recovery or audit snapshots after reconnects, missed WebSocket messages, and settlement windows.
  name: Gemini Trust Company Positions API
  phrasing_intents:
  - id: getActiveOrders
    intent: List open prediction market orders
    question: Which of my prediction market orders are still open?
  - id: getOrderHistory
    intent: List filled or cancelled prediction orders
    question: What prediction market orders of mine were filled last week?
  - id: getPositions
    intent: List current prediction market positions
    question: What prediction market positions am I holding right now?
  - id: getSettledPositions
    intent: List settled prediction positions and payouts
    question: How much did I get paid out on contracts that have resolved?
  - id: getVolumeMetrics
    intent: Get my share volume for an event
    question: How many contracts have I traded as maker versus taker in an event?
  phrasing_ops: 5
  slug: gemini-trust-positions-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: Endpoints for the Maker Rebate and Liquidity Rewards programs. - **Maker Rebate** — per-fill rebates earned by resting limit orders that get filled. Rates and rebate multipliers are configured per cat
  name: Gemini Trust Company Rewards API
  phrasing_intents:
  - id: getMakerRebateRates
    intent: Get the maker rebate rate schedule
    question: What share of maker fees is rebated on prediction markets?
  - id: listMakerRebatePayouts
    intent: List my maker rebate payouts
    question: Which maker rebate payouts have I received?
  - id: getMakerRebateLifetimeSummary
    intent: Get total maker rebates earned
    question: How much have I earned in maker rebates in total?
  - id: getLiquidityRewardsConfig
    intent: Get the liquidity rewards program settings
    question: What is the maximum spread allowed to qualify for liquidity rewards?
  - id: listLiquidityRewardsEvents
    intent: List events in the liquidity rewards program
    question: Which prediction events currently pay liquidity rewards?
  - id: getLiquidityRewardsDailySummary
    intent: Get daily liquidity reward payouts
    question: How much did I earn in liquidity rewards each day this month?
  - id: getLiquidityRewardsLifetimeSummary
    intent: Get total liquidity rewards earned
    question: What is my all-time liquidity rewards total?
  phrasing_ops: 7
  slug: gemini-trust-rewards-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Session API from Gemini Trust Company — 1 operation(s) for session.
  name: Gemini Trust Company Session API
  phrasing_intents:
  - id: sendHeartbeat
    intent: Keep an API session alive
    question: How do I stop my session from timing out and cancelling my orders?
  phrasing_ops: 1
  slug: gemini-trust-session-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: The Staking API from Gemini Trust Company — 6 operation(s) for staking.
  name: Gemini Trust Company Staking API
  phrasing_intents:
  - id: listStakingBalances
    intent: Get staking balances
    question: How much of my crypto is currently staked?
  - id: stakeCryptoFunds
    intent: Stake crypto with a staking provider
    question: How do I start staking ETH from my exchange balance?
  - id: listStakingEventHistory
    intent: List staking deposits, redemptions and interest
    question: What staking deposits and redemptions have I made?
  - id: listStakingRates
    intent: Get current staking interest rates
    question: What staking yield does each asset earn right now?
  - id: listStakingRewards
    intent: List historical staking reward payments
    question: How much have I earned in staking rewards over time?
  - id: unstakeCryptoFunds
    intent: Unstake crypto from a staking provider
    question: How do I take my crypto out of staking?
  phrasing_ops: 6
  slug: gemini-trust-staking-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: Read, check, and accept the latest Prediction Markets terms for API key and OAuth trading flows.
  name: Gemini Trust Company Terms API
  phrasing_intents:
  - id: getPredictionMarketsTerms
    intent: Get the prediction markets terms text
    question: Where can I read the current Prediction Markets terms before agreeing?
  - id: getPredictionMarketsTermsStatus
    intent: Check if the account accepted the terms
    question: Has my account group accepted the latest prediction markets terms?
  - id: acceptPredictionMarketsTerms
    intent: Accept the latest prediction markets terms
    question: How do I accept the prediction markets terms for my account group?
  phrasing_ops: 3
  slug: gemini-trust-terms-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: Authenticated REST endpoints for placing and managing orders. Treat REST order placement as payload reference or a one-off server workflow; for active trading and market making, prefer WebSocket order
  name: Gemini Trust Company Trading API
  phrasing_intents:
  - id: placeOrder
    intent: Place a prediction market order
    question: How do I buy Yes contracts on a prediction market at a limit price?
  - id: placeOrderBatch
    intent: Place up to 20 prediction orders at once
    question: Can I submit several prediction market orders in a single request?
  - id: cancelOrder
    intent: Cancel one prediction market order
    question: How do I cancel a single prediction market order?
  - id: cancelOrderBatch
    intent: Cancel up to 20 prediction orders at once
    question: Can I cancel a list of prediction orders in one call?
  phrasing_ops: 4
  slug: gemini-trust-trading-api
- baseURL: https://api.gemini.com
  baseurl_source: declared
  description: Public, unauthenticated prediction-market trade volume by category and UTC period.
  name: Gemini Trust Company Volume API
  phrasing_intents:
  - id: getPredictionMarketDailyVolume
    intent: Get a day's prediction market volume by category
    question: How much prediction market volume traded in each category yesterday?
  - id: getPredictionMarketHourlyVolume
    intent: Get hourly prediction market volume for a day
    question: Which hours of the day had the most prediction market trading?
  phrasing_ops: 2
  slug: gemini-trust-volume-api
artifact_total: 34
asyncapis:
- description: Machine-readable contract for the production Gemini WebSocket API at `wss://ws.gemini.com`. This specification models the shared JSON request/response envelope, market data streams, authenticated orde
  name: Gemini WebSocket API
  slug: gemini-trust-websocket-asyncapi
common:
- group: other
  href: https://artifacts.apis.io/gemini-trust/overlays/gemini-trust-prediction-markets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gemini-trust-prediction-markets-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.gemini.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gemini.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gemini.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.gemini.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.gemini.com/get-started/sandbox
- group: operate
  title: ''
  type: Support
  url: https://support.gemini.com
- group: company
  title: ''
  type: Blog
  url: https://www.gemini.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gemini
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gemini.com/fees
- group: start
  title: ''
  type: SignUp
  url: https://exchange.gemini.com/register
- group: start
  title: ''
  type: Login
  url: https://exchange.gemini.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gemini.com/legal/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gemini.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gemini.com
- group: operate
  href: https://artifacts.apis.io/gemini-trust/changelog/gemini-trust-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gemini-trust-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.gemini.com/changelog/revision-history
- group: agent
  href: https://artifacts.apis.io/gemini-trust/llms/gemini-trust-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gemini-trust-llms.txt
- group: other
  href: https://artifacts.apis.io/gemini-trust/a2a/gemini-trust-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gemini-trust-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gemini-trust/mcp/gemini-trust-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gemini-trust-mcp.yml
- group: build
  href: https://artifacts.apis.io/gemini-trust/mcp/gemini-trust-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gemini-trust-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gemini-trust/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/gemini-trust/packages/gemini-trust-packages.yml
  title: ''
  type: Packages
  url: packages/gemini-trust-packages.yml
- group: build
  href: https://artifacts.apis.io/gemini-trust/packages/gemini-trust-packages.yml
  title: ''
  type: SDKs
  url: packages/gemini-trust-packages.yml
- group: build
  href: https://artifacts.apis.io/gemini-trust/cli/gemini-trust-cli.yml
  title: ''
  type: CLI
  url: cli/gemini-trust-cli.yml
- group: agent
  href: https://artifacts.apis.io/gemini-trust/well-known/gemini-trust-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gemini-trust-well-known.yml
- group: auth
  href: https://artifacts.apis.io/gemini-trust/well-known/gemini-trust-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gemini-trust-security.txt
- group: auth
  href: https://artifacts.apis.io/gemini-trust/authentication/gemini-trust-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gemini-trust-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gemini-trust/scopes/gemini-trust-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gemini-trust-scopes.yml
- group: design
  href: https://artifacts.apis.io/gemini-trust/conventions/gemini-trust-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gemini-trust-conventions.yml
- group: design
  href: https://artifacts.apis.io/gemini-trust/conventions/gemini-trust-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/gemini-trust-conventions.yml
- group: design
  href: https://artifacts.apis.io/gemini-trust/errors/gemini-trust-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gemini-trust-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gemini-trust/errors/gemini-trust-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/gemini-trust-error-codes.yml
- group: operate
  href: https://artifacts.apis.io/gemini-trust/rate-limits/gemini-trust-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gemini-trust-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gemini-trust/plans/gemini-trust-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gemini-trust-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gemini-trust/lifecycle/gemini-trust-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gemini-trust-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/gemini-trust/sandbox/gemini-trust-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gemini-trust-sandbox.yml
- group: design
  href: https://artifacts.apis.io/gemini-trust/conformance/gemini-trust-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gemini-trust-conformance.yml
- group: auth
  href: https://artifacts.apis.io/gemini-trust/conformance/gemini-trust-conformance.yml
  title: ''
  type: Compliance
  url: conformance/gemini-trust-conformance.yml
- group: auth
  href: https://artifacts.apis.io/gemini-trust/security/gemini-trust-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gemini-trust-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gemini-trust/security/gemini-trust-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gemini-trust-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gemini-trust/security/gemini-trust-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gemini-trust-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gemini-trust/security/gemini-trust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gemini-trust-domain-security.yml
- group: docs
  href: https://artifacts.apis.io/gemini-trust/asyncapi/gemini-trust-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/gemini-trust-websocket-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/gemini-trust/data-model/gemini-trust-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gemini-trust-data-model.yml
- group: other
  href: https://artifacts.apis.io/gemini-trust/overlays/gemini-trust-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gemini-trust-rest-overlay.yaml
created: '2026-09-15'
description: Gemini Trust Company, LLC is a United States cryptocurrency exchange and custodian, founded in 2014 and headquartered in New York, regulated as a New York State Department of Financial Services trust company. It operates the Gemini Exchange and the Gemini Developer Platform, publishing OpenAPI 3.0.3 contracts for its Crypto Trading REST API and Prediction Markets REST API, an AsyncAPI 3.0.0 contract for the wss://ws.gemini.com WebSocket API, plus a FIX gateway. The platform covers spot, margin, perpetuals, prediction markets, staking, clearing, custody and institutional fund management, with API-key HMAC-SHA384 signing and OAuth 2.0 authorization-code + PKCE, including FDX-namespaced scopes.
finops:
- has_sources: true
  method: derived
  name: Gemini Trust Finops
  primary_unit: ''
  service_category: ''
  slug: gemini-trust-finops
  template: true
image: https://gemini.com/static/images/gemini-logomark.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 68 tools listed.
  name: Gemini MCP Server
  slug: gemini-mcp-server
modified: '2026-09-18'
name: Gemini Trust Company
nav: Providers
network: true
overview: 'Gemini Trust Company publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Gemini WebSocket API, Account Administration API, Clearing API, and 17 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Market Data.


  The Gemini Trust Company catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Gemini Trust Company''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
plans:
- name: Gemini Trust Plans Pricing
  plan_count: 0
  slug: gemini-trust-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Gemini Trust Rate Limits
  slug: gemini-trust-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Gemini Trust Company API Rules
  rule_count: 61
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 15
  slug: gemini-trust-rules
scopes:
- name: Gemini Trust Scopes
  scope_count: 32
  slug: gemini-trust-scopes
  summary_line: 32 scopes
score:
  band: exemplar
  composite: 69.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 60.5
    developer_ergonomics: 85.7
    discoverability: 76.7
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 69.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 48.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gemini-trust/gemini-trust-2026-10-11T104745.png
security:
- kind: authentication
  name: Gemini Trust Authentication
  slug: gemini-trust-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Gemini Trust Domain Security
  slug: gemini-trust-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gemini Trust Vulnerability Disclosure
  slug: gemini-trust-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gemini Trust Trust Center
  slug: gemini-trust-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 3
skills:
- name: gemini-candles
  slug: gemini-trust-gemini-candles
- name: gemini-developer
  slug: gemini-trust-gemini-developer
- name: integrate-gemini
  slug: gemini-trust-integrate-gemini
slug: gemini-trust
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Market Data
- Order Management
- Clearing
- Custody
- Financial Services
- Prediction Markets
- Staking
- Derivatives
- WebSocket
- FIX
- Real-Time
- A2A
website: https://www.gemini.com
---
