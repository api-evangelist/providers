---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Upstox operates a hosted, OAuth-protected Model Context Protocol server at https://mcp.upstox.com/mcp that gives AI assistants — Claude Desktop and the Claude web app, Claude Code, ChatGPT in Develope
  name: Upstox MCP Server
  slug: upstox-mcp-server
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Charge API from Upstox — 2 operation(s) for charge.
  name: Upstox Charge API
  phrasing_intents:
  - id: postMargin
    intent: Calculate margin required for instruments
    question: How much margin do I need before placing these trades on Upstox?
  - id: getBrokerage
    intent: Estimate brokerage and charges for an order
    question: What brokerage and charges will I pay on a trade before I place it?
  phrasing_ops: 2
  slug: upstox-charge-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The events-controller-v-2 API from Upstox — 1 operation(s) for events-controller-v-2.
  name: Upstox Events Controller V 2 API
  phrasing_intents:
  - id: publishEvent
    intent: Publish an event
    question: How do I send an event with a type and payload to Upstox?
  phrasing_ops: 1
  slug: upstox-events-controller-v-2-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Expired Instrument API from Upstox — 4 operation(s) for expired instrument.
  name: Upstox Expired Instrument API
  phrasing_intents:
  - id: getExpiredOptionContracts
    intent: List expired option contracts for an underlying
    question: How do I find option contracts that have already expired for an index?
  - id: getExpiredHistoricalCandleData
    intent: Get historical candles for an expired contract
    question: How do I get OHLC candles for a futures or options contract that has already expired?
  - id: getExpiredFutureContracts
    intent: List expired futures contracts for an underlying
    question: Where can I find futures contracts that expired on a past date?
  - id: getExpiriesResponse
    intent: List past expiry dates for an instrument
    question: Which expiry dates are available for historical data on an underlying?
  phrasing_ops: 4
  slug: upstox-expired-instrument-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Fundamentals API from Upstox — 8 operation(s) for fundamentals.
  name: Upstox Fundamentals API
  phrasing_intents:
  - id: getShareHoldings
    intent: Get a company's shareholding pattern
    question: How much of a company do promoters, FIIs and the public own?
  - id: getCompanyProfile
    intent: Get a company's profile
    question: What does a company do, and what are its basic profile details, given its ISIN?
  - id: getKeyRatios
    intent: Get a company's key financial ratios
    question: What are the P/E, ROE and other key ratios for a stock?
  - id: getIncomeStatement
    intent: Get a company's income statement
    question: What were a company's revenue and profit over recent quarters?
  - id: getCorporateActions
    intent: List a company's corporate actions
    question: Has a company announced dividends, splits or bonus issues?
  - id: getCashFlow
    intent: Get a company's cash flow statement
    question: How much cash does a company generate from operations?
  - id: getBalanceSheet
    intent: Get a company's balance sheet
    question: What are a company's assets, liabilities and debt levels?
  - id: getCompetitors
    intent: List a company's competitors
    question: Which companies compete with a given stock?
  phrasing_ops: 8
  slug: upstox-fundamentals-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The History API from Upstox — 3 operation(s) for history.
  name: Upstox History API
  phrasing_intents:
  - id: getHistoricalCandleData_2
    intent: Get historical candles up to an end date
    question: How do I get past daily candles for a stock ending on a certain date without picking a start?
  - id: getHistoricalCandleData_3
    intent: Get historical candles for a date range
    question: Can I fetch OHLC candles between a specific start and end date?
  - id: getIntraDayCandleData_1
    intent: Get today's intraday candles
    question: How do I get today's intraday candles for a stock while the market is open?
  phrasing_ops: 3
  slug: upstox-history-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: Historical Candle Data V3
  name: Upstox History V3 API
  phrasing_intents:
  - id: getHistoricalCandleData
    intent: Get custom-interval candles up to an end date
    question: Can I get candles in custom units like 3 minutes or 2 hours up to an end date?
  - id: getHistoricalCandleData_1
    intent: Get custom-interval candles for a date range
    question: How do I fetch 5-minute or 4-hour candles between two dates?
  - id: getIntraDayCandleData
    intent: Get today's candles in a custom interval
    question: How do I get today's intraday bars in a custom size like 3 minutes?
  phrasing_ops: 3
  slug: upstox-history-v3-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Instruments API from Upstox — 1 operation(s) for instruments.
  name: Upstox Instruments API
  phrasing_intents:
  - id: searchInstrument
    intent: Search for tradable instruments
    question: How do I find the instrument key for a stock or option by typing its name?
  phrasing_ops: 1
  slug: upstox-instruments-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The IPO API from Upstox — 4 operation(s) for ipo.
  name: Upstox IPO API
  phrasing_intents:
  - id: getIpoOrders
    intent: List my IPO applications
    question: Which IPOs have I applied for?
  - id: applyForIpo
    intent: Apply for an IPO
    question: How do I apply for an upcoming IPO with my UPI ID?
  - id: getIpoListing
    intent: Browse IPOs by status
    question: What IPOs are open right now?
  - id: getIpoDetails
    intent: Get details of an IPO
    question: What is the price band, lot size and dates for a particular IPO?
  - id: getIpoOrderById
    intent: Check one IPO application
    question: What is the status of the IPO application I just submitted?
  - id: cancelIpoOrder
    intent: Cancel an IPO application
    question: Can I withdraw an IPO application after submitting it?
  phrasing_ops: 6
  slug: upstox-ipo-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Login API from Upstox — 4 operation(s) for login.
  name: Upstox Login API
  phrasing_intents:
  - id: initTokenRequestForIndieUser
    intent: Start an access token request for an indie app
    question: How do I kick off token generation as an individual developer without a redirect flow?
  - id: token
    intent: Exchange an authorization code for an access token
    question: How do I exchange the auth code from the redirect for an access token?
  - id: authorize
    intent: Open the login dialog for user authorization
    question: Where do I send a user to log in and authorize my trading app?
  - id: logout
    intent: Log out and end the session
    question: How do I invalidate my current access token?
  phrasing_ops: 4
  slug: upstox-login-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Market Holidays and Timings API from Upstox — 13 operation(s) for market holidays and timings.
  name: Upstox Market Holidays and Timings API
  phrasing_intents:
  - id: getExchangeTimings
    intent: Get exchange trading hours on a date
    question: What time do NSE and MCX open and close on a particular day?
  - id: getMarketStatus
    intent: Check whether an exchange is open
    question: Is the NSE market open right now?
  - id: getSmartlistOptions
    intent: List top options by activity or movement
    question: Which options are most actively traded today?
  - id: getSmartlistMtf
    intent: List stocks eligible for margin trade funding
    question: Which stocks can I buy with margin trade funding?
  - id: getSmartlistFutures
    intent: List top futures by activity or movement
    question: Which futures contracts are most traded today?
  - id: getPcrData
    intent: Get put-call ratio for an underlying and expiry
    question: What is the put-call ratio for Nifty options this expiry?
  - id: getOiData
    intent: Get open interest for an underlying and expiry
    question: What is the open interest across strikes for an index option expiry?
  - id: getMaxPainData
    intent: Get max pain level for an options expiry
    question: What is the max pain strike for this week's Bank Nifty expiry?
  phrasing_ops: 13
  slug: upstox-market-holidays-and-timings-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Market Quote API from Upstox — 3 operation(s) for market quote.
  name: Upstox Market Quote API
  phrasing_intents:
  - id: getFullMarketQuote
    intent: Get full market quotes with depth
    question: How do I get the full quote snapshot, including depth and volume, for several stocks?
  - id: getMarketQuoteOHLC
    intent: Get OHLC quotes for instruments (v2)
    question: What are today's open, high, low and close for a list of stocks?
  - id: ltp
    intent: Get last traded prices (v2)
    question: What is the last traded price of a stock right now?
  phrasing_ops: 3
  slug: upstox-market-quote-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Market Quote V3 API from Upstox — 3 operation(s) for market quote v3.
  name: Upstox Market Quote V3 API
  phrasing_intents:
  - id: getMarketQuoteOptionGreek
    intent: Get option Greeks for contracts
    question: What are the delta, gamma, theta and vega of an option contract?
  - id: getMarketQuoteOHLCV3
    intent: Get OHLC quotes for instruments (v3)
    question: How do I get live and previous OHLC bars for a batch of instruments on the v3 quote API?
  - id: getLtp
    intent: Get last traded prices (v3)
    question: What is the latest traded price for a set of instrument keys on the v3 API?
  phrasing_ops: 3
  slug: upstox-market-quote-v3-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Mutual Fund API from Upstox — 4 operation(s) for mutual fund.
  name: Upstox Mutual Fund API
  phrasing_intents:
  - id: getMutualFundSips
    intent: List my mutual fund SIPs
    question: Which SIPs do I have running or paused?
  - id: getMutualFundOrders
    intent: List recent mutual fund orders
    question: What mutual fund orders did I place in the last week?
  - id: getMutualFundOrder
    intent: Get a mutual fund order
    question: What happened to a specific mutual fund order I placed?
  - id: getMutualFundHoldings
    intent: List my mutual fund holdings
    question: Which mutual funds do I currently hold and how many units?
  phrasing_ops: 4
  slug: upstox-mutual-fund-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The News API from Upstox — 1 operation(s) for news.
  name: Upstox News API
  phrasing_intents:
  - id: getNews
    intent: Get news for stocks or my portfolio
    question: What's the latest news on the stocks I hold?
  phrasing_ops: 1
  slug: upstox-news-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Options API from Upstox — 2 operation(s) for options.
  name: Upstox Options API
  phrasing_intents:
  - id: getOptionContracts
    intent: List active option contracts for an underlying
    question: Which option contracts are currently tradable on an index or stock?
  - id: getPutCallOptionChain
    intent: Get the option chain for an expiry
    question: What does the Nifty option chain look like for this expiry?
  phrasing_ops: 2
  slug: upstox-options-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Order API from Upstox — 18 operation(s) for order.
  name: Upstox Order API
  phrasing_intents:
  - id: modifyOrder
    intent: Modify an open order (v3)
    question: How do I change the price of a pending order using the v3 order API?
  - id: modifyGTTOrder
    intent: Modify a GTT order
    question: How do I change the trigger rules on my good-till-triggered order?
  - id: modifyOrder_1
    intent: Modify an open order (older v2)
    question: How do I modify a pending order on the older v2 endpoint?
  - id: placeOrder
    intent: Place an order (v3, with auto-slicing)
    question: How do I place a buy order with the v3 order API?
  - id: placeGTTOrder
    intent: Place a GTT order
    question: How do I set a good-till-triggered order that fires when a price is hit?
  - id: exitPositions
    intent: Exit all open positions
    question: How do I square off all my open positions at once?
  - id: placeOrder_1
    intent: Place an order (older v2)
    question: How do I place an order on the older v2 place endpoint?
  - id: placeMultiOrder
    intent: Place several orders in one request
    question: Can I send a basket of orders to the exchange in a single call?
  phrasing_ops: 18
  slug: upstox-order-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The PAYMENTS API from Upstox — 4 operation(s) for payments.
  name: Upstox PAYMENTS API
  phrasing_intents:
  - id: modifyPayout
    intent: Change the amount of a pending withdrawal
    question: Can I change how much I'm withdrawing after I've requested a payout?
  - id: cancelPayout
    intent: Cancel a pending withdrawal
    question: How do I cancel a withdrawal request before it's processed?
  - id: getPayoutHistory
    intent: List my withdrawal history
    question: What withdrawals have I made from my trading account?
  - id: initiatePayout
    intent: Withdraw funds to my bank
    question: How do I withdraw money from my trading account to my bank?
  - id: getPayoutModes
    intent: List available withdrawal modes
    question: Which withdrawal methods can I use right now?
  - id: getPayinHistory
    intent: List my deposit history
    question: What funds have I added to my trading account?
  phrasing_ops: 6
  slug: upstox-payments-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Portfolio API from Upstox — 4 operation(s) for portfolio.
  name: Upstox Portfolio API
  phrasing_intents:
  - id: convertPositions
    intent: Convert a position's product type
    question: How do I convert an intraday position to delivery?
  - id: getMtfPositions
    intent: List my margin trade funding positions
    question: Which stocks am I holding on margin trade funding?
  - id: getPositions
    intent: List today's open positions
    question: What positions do I have open today?
  - id: getHoldings
    intent: List my long-term holdings
    question: Which shares do I hold in my demat account?
  phrasing_ops: 4
  slug: upstox-portfolio-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Post Trade API from Upstox — 1 operation(s) for post trade.
  name: Upstox Post Trade API
  phrasing_intents:
  - id: getTradesByDateRange
    intent: Get trade history for a date range
    question: How do I get all my trades from past months, not just today?
  phrasing_ops: 1
  slug: upstox-post-trade-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Trade Profit And Loss API from Upstox — 3 operation(s) for trade profit and loss.
  name: Upstox Trade Profit And Loss API
  phrasing_intents:
  - id: getTradeWiseProfitAndLossMetaData
    intent: Get P&L report metadata
    question: How many trades are in my realised P&L report and what page size is allowed?
  - id: getTradeWiseProfitAndLossData
    intent: Get trade-wise realised profit and loss
    question: What profit or loss did I book on each trade this financial year?
  - id: getProfitAndLossCharges
    intent: Get charges paid on my trades
    question: How much have I paid in brokerage, taxes and fees this financial year?
  phrasing_ops: 3
  slug: upstox-trade-profit-and-loss-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The User API from Upstox — 5 operation(s) for user.
  name: Upstox User API
  phrasing_intents:
  - id: getUserIps
    intent: Get my registered static IPs
    question: Which static IP addresses are registered for my API orders?
  - id: updateUserIp
    intent: Update my registered static IPs
    question: How do I register a new static IP for placing orders through the API?
  - id: getKillSwitch
    intent: Check kill switch status by segment
    question: Which trading segments have I disabled with the kill switch?
  - id: updateKillSwitch
    intent: Enable or disable trading segments
    question: How do I turn on the kill switch to stop myself trading F&O?
  - id: getUserFundMarginV3
    intent: Get detailed funds and margin breakdown (v3)
    question: How much of my balance is pledged margin versus cash available to trade?
  - id: getProfile
    intent: Get my account profile
    question: Which exchanges, products and order types are enabled on my account?
  - id: getUserFundMargin
    intent: Get funds and margin by segment (v2)
    question: How much money do I have for equity versus commodity trading?
  phrasing_ops: 7
  slug: upstox-user-api
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Websocket API from Upstox — 4 operation(s) for websocket.
  name: Upstox Websocket API
  phrasing_intents:
  - id: getPortfolioStreamFeed
    intent: Connect to the portfolio updates stream
    question: How do I get real-time order and position updates pushed to my app?
  - id: getPortfolioStreamFeedAuthorize
    intent: Get the authorized portfolio stream URL
    question: Where do I get the authorized socket URI for portfolio updates?
  - id: getMarketDataFeed
    intent: Connect to the live market data stream
    question: How do I stream live ticks for stocks over a WebSocket?
  - id: getMarketDataFeedAuthorize
    intent: Get the authorized market data stream URL
    question: Where do I get the authorized socket URI for market data?
  phrasing_ops: 4
  slug: upstox-websocket-api
artifact_total: 35
asyncapis:
- description: ''
  name: Upstox Webhooks
  slug: upstox-webhooks
common:
- group: other
  href: https://artifacts.apis.io/upstox/overlays/upstox-developer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/upstox-developer-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://upstox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://upstox.com/trading-api/
- group: docs
  title: ''
  type: Documentation
  url: https://upstox.com/developer/api-documentation/open-api
- group: docs
  title: ''
  type: APIReference
  url: https://upstox.com/developer/api-documentation/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://upstox.com/developer/api-documentation/installing-sdk
- group: operate
  title: ''
  type: Support
  url: https://upstox.com/help-center/
- group: operate
  title: ''
  type: Community
  url: https://community.upstox.com/
- group: company
  title: ''
  type: Blog
  url: https://upstox.com/market-talk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upstox
- group: commercial
  title: ''
  type: Pricing
  url: https://upstox.com/brokerage-charges/
- group: start
  title: ''
  type: SignUp
  url: https://upstox.com/open-demat-account/
- group: start
  title: ''
  type: Login
  url: https://login.upstox.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upstox.com/terms-of-use-and-privacy-policy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upstox.com/terms-of-use-and-privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://gist.github.com/Rahulzz/a0da2ad28a7dcc81e887f24cfdbc80a8
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upstox.com/
- group: operate
  href: https://artifacts.apis.io/upstox/changelog/upstox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/upstox-changelog.yml
- group: operate
  href: https://artifacts.apis.io/upstox/lifecycle/upstox-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/upstox-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/upstox/lifecycle/upstox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/upstox-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://upstox.com/bug-bounty/
- group: auth
  href: https://artifacts.apis.io/upstox/security/upstox-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/upstox-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/upstox/security/upstox-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/upstox-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/upstox/conformance/upstox-conformance.yml
  title: ''
  type: Compliance
  url: conformance/upstox-conformance.yml
- group: design
  href: https://artifacts.apis.io/upstox/conformance/upstox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/upstox-conformance.yml
- group: auth
  href: https://artifacts.apis.io/upstox/security/upstox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upstox-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/upstox/authentication/upstox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upstox-authentication.yml
- group: auth
  href: https://artifacts.apis.io/upstox/scopes/upstox-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/upstox-scopes.yml
- group: build
  href: https://artifacts.apis.io/upstox/packages/upstox-packages.yml
  title: ''
  type: Packages
  url: packages/upstox-packages.yml
- group: build
  href: https://artifacts.apis.io/upstox/packages/upstox-packages.yml
  title: ''
  type: SDKs
  url: packages/upstox-packages.yml
- group: agent
  href: https://artifacts.apis.io/upstox/well-known/upstox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upstox-well-known.yml
- group: agent
  href: https://artifacts.apis.io/upstox/llms/upstox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upstox-llms.txt
- group: agent
  href: https://artifacts.apis.io/upstox/mcp/upstox-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/upstox-mcp.yml
- group: build
  href: https://artifacts.apis.io/upstox/mcp/upstox-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/upstox-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/upstox/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/upstox/conventions/upstox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/upstox-conventions.yml
- group: design
  href: https://artifacts.apis.io/upstox/errors/upstox-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/upstox-error-codes.yml
- group: operate
  href: https://artifacts.apis.io/upstox/rate-limits/upstox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/upstox-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/upstox/plans/upstox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/upstox-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/upstox/sandbox/upstox-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/upstox-sandbox.yml
- group: design
  href: https://artifacts.apis.io/upstox/data-model/upstox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/upstox-data-model.yml
- group: design
  href: https://artifacts.apis.io/upstox/asyncapi/upstox-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/upstox-webhooks.yml
created: '2026-09-02'
description: Upstox is a SEBI-registered Indian retail brokerage operated by Upstox Securities Private Limited, a wholly owned subsidiary of RKSV Securities India Private Limited, serving over 1.3 crore customers across equities, futures and options, commodities, currency, mutual funds, IPOs, NCDs, fixed deposits and insurance on NSE, BSE and MCX. Its Upstox Developer API is a free, OAuth 2.0 protected REST and WebSocket suite of 101 published operations covering order placement (including V3 slicing, multi-order and GTT/trailing-stop-loss), portfolio holdings and positions, funds and margin, brokerage and charge calculation, market quotes with option greeks, historical and intraday candles, expired-instrument history, company fundamentals, IPO application, mutual funds, payouts, news and market-information analytics. Upstox also runs a hosted, OAuth-protected Model Context Protocol server at mcp.upstox.com giving AI agents read-only access to a user's holdings, orders, positions, mutual
  funds, funds and profile, and publishes an official Agent Skill and Claude plugin marketplace alongside first-party SDKs for Python, Node.js, Java, PHP and .NET.
finops:
- has_sources: true
  method: derived
  name: Upstox Finops
  primary_unit: ''
  service_category: ''
  slug: upstox-finops
  template: true
image: https://assets.upstox.com/website/images/upstox-new-logo.svg
layout: provider
mcp_servers:
- description: 'Upstox operates a first-party hosted Model Context Protocol server that gives an AI assistant read-only access to a connected Upstox brokerage account. It is a genuine agent surface: an MCP client POS'
  name: Upstox MCP Server
  slug: upstox-mcp-server
modified: '2026-09-02'
name: Upstox
nav: Providers
network: true
overview: 'Upstox publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Charge API, Events Controller V 2 API, Expired Instrument API, and 20 more. Tagged areas include Company, Financial Services, Stock Trading, Brokerage, and Market Data.


  The Upstox catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Upstox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Upstox Plans Pricing
  plan_count: 3
  slug: upstox-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 17
  name: Upstox Rate Limits
  slug: upstox-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Upstox API Rules
  rule_count: 58
  severity_counts:
    error: 39
    hint: 0
    info: 4
    warn: 15
  slug: upstox-rules
scopes:
- name: Upstox Scopes
  scope_count: 2
  slug: upstox-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 77.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 64.6
    developer_ergonomics: 83.3
    discoverability: 75.0
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 76.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 22
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
screenshot: https://apis.io/screenshots/upstox/upstox-2026-10-11T131530.png
security:
- kind: authentication
  name: Upstox Authentication
  slug: upstox-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Upstox Domain Security
  slug: upstox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Upstox Vulnerability Disclosure
  slug: upstox-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Upstox Trust Center
  slug: upstox-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO 22301:2019
skill_count: 1
skills:
- name: upstox
  slug: upstox-agent-skill
slug: upstox
tags:
- Company
- Financial Services
- Stock Trading
- Brokerage
- Market Data
- Investing
- Capital Markets
- Mutual Funds
- Algorithmic Trading
- India
website: https://upstox.com/
---
