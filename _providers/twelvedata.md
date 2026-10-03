---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.0
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Twelvedata Agentic Access
  operation_count: 199
  slug: twelvedata-agentic-access
  summary_line: 199 operations · 1 acting
api_count: 2
apis:
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: 'Real-time price streaming over a persistent, bidirectional WebSocket at wss://ws.twelvedata.com/v1/quotes/price. Clients authenticate with an apikey query parameter, send JSON subscribe / unsubscribe '
  name: Twelve Data WebSocket Streaming API
  slug: twelvedata-websocket-streaming-api
- baseURL: https://api.twelvedata.com
  baseurl_source: declared
  description: Real-time quotes, latest prices, and end-of-day data.
  name: Twelve Data Core Data API
  phrasing_intents:
  - id: getEndOfDay
    intent: Get the latest end-of-day closing price
    question: What did this stock close at on the last trading day?
  - id: getQuote
    intent: Get a real-time quote with daily stats
    question: Can I get open, high, low, volume and the 52-week range for a symbol in one call?
  - id: getPrice
    intent: Get the latest real-time trading price
    question: What is the current trading price of this ticker right now?
  - id: getMarketMovers
    intent: List today's top gainers and losers
    question: Which stocks are the biggest gainers and losers today?
  - id: getMarketState
    intent: Check whether exchanges are open or closed
    question: Is the stock exchange open right now?
  phrasing_ops: 5
  slug: twelvedata-core-data-api
- baseURL: https://api.twelvedata.com
  baseurl_source: declared
  description: Company profiles, statements, dividends, earnings, and analysis.
  name: Twelve Data Fundamentals API
  phrasing_intents:
  - id: GetBalanceSheet
    intent: Get a company's balance sheet
    question: What are a company's total assets, liabilities and shareholders' equity?
  - id: GetBalanceSheetConsolidated
    intent: Get a company's raw consolidated balance sheet
    question: Where can I get the raw consolidated balance sheet as the company reported it?
  - id: GetCashFlow
    intent: Get a company's cash flow statement
    question: How much cash did this company generate from operations last year?
  - id: GetCashFlowConsolidated
    intent: Get a company's raw consolidated cash flow
    question: Can I see the consolidated cash flow statement in its raw reported form?
  - id: GetDividends
    intent: Get a stock's dividend payment history
    question: How much has this stock paid in dividends over the last ten years?
  - id: GetDividendsCalendar
    intent: See upcoming and past dividends across companies
    question: Which companies go ex-dividend next week?
  - id: GetEarnings
    intent: Get a company's estimated vs actual EPS history
    question: Did this company beat or miss its EPS estimates in past quarters?
  - id: GetEarningsCalendar
    intent: See which companies report earnings on given dates
    question: Which companies are announcing earnings today?
  phrasing_ops: 20
  slug: twelvedata-fundamentals-api
- baseURL: https://api.twelvedata.com
  baseurl_source: declared
  description: Catalogs of instruments, exchanges, and supporting metadata.
  name: Twelve Data Reference Data API
  phrasing_intents:
  - id: GetBonds
    intent: List available bonds
    question: Which bonds and fixed income instruments are available?
  - id: GetCommodities
    intent: List available commodity pairs
    question: What commodities can I get prices for, like gold or wheat?
  - id: GetCountries
    intent: List countries with ISO codes and currencies
    question: What ISO country codes and currencies are supported?
  - id: GetCrossListings
    intent: Find other exchanges where a security is listed
    question: On which other exchanges is this stock also traded?
  - id: GetCryptocurrencies
    intent: List available cryptocurrency pairs
    question: Which crypto pairs quoted in USD are available?
  - id: GetCryptocurrencyExchanges
    intent: List supported cryptocurrency exchanges
    question: Which crypto exchanges does the data come from?
  - id: GetEarliestTimestamp
    intent: Find how far back data goes for an instrument
    question: How far back does 1-minute history go for this stock?
  - id: GetEtf
    intent: List all available ETFs
    question: Which ETFs are tradable on a particular exchange?
  phrasing_ops: 19
  slug: twelvedata-reference-data-api
- baseURL: https://api.twelvedata.com
  baseurl_source: declared
  description: 100+ technical analysis indicators computed over time series.
  name: Twelve Data Technical Indicators API
  phrasing_intents:
  - id: getRSI
    intent: Get the RSI momentum indicator for an instrument
    question: Is this stock overbought according to its RSI?
  - id: getMACD
    intent: Get the MACD indicator for an instrument
    question: What is the MACD reading for this ticker?
  - id: getBBands
    intent: Get Bollinger Bands for an instrument
    question: Is the price touching the upper or lower Bollinger Band?
  - id: listTechnicalIndicators
    intent: List all available technical indicators
    question: Which technical indicators can I request?
  phrasing_ops: 4
  slug: twelvedata-technical-indicators-api
- baseURL: https://api.twelvedata.com
  baseurl_source: declared
  description: Historical and real-time OHLCV time series.
  name: Twelve Data Time Series API
  phrasing_intents:
  - id: getTimeSeries
    intent: Get historical OHLCV bars for an instrument
    question: How do I pull daily open, high, low, close and volume history for a ticker?
  - id: getTimeSeriesCross
    intent: Compute a cross-rate series between two instruments
    question: Can I get a price history for an exotic currency pair that is not quoted directly?
  phrasing_ops: 2
  slug: twelvedata-time-series-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The advanced API from Twelve Data — 2 operation(s) for advanced.
  name: Twelve Data Advanced API
  phrasing_intents:
  - id: GetApiUsage
    intent: Check my API request usage and limits
    question: How many API requests have I used so far today?
  - id: advanced
    intent: Fetch data for many symbols in one batch request
    question: Can I request quotes and time series for several symbols in a single call?
  phrasing_ops: 2
  slug: twelvedata-advanced-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The analysis API from Twelve Data — 9 operation(s) for analysis.
  name: Twelve Data Analysis API
  phrasing_intents:
  - id: GetAnalystRatingsLight
    intent: Get an analyst ratings snapshot for a stock
    question: What is the quick summary of analyst buy, hold and sell ratings on a stock outside the US?
  - id: GetAnalystRatingsUsEquities
    intent: Get detailed analyst ratings for a US stock
    question: Which analyst firms have rated this US stock, and did they upgrade or downgrade it?
  - id: GetEarningsEstimate
    intent: Get analyst EPS estimates for a company
    question: What EPS are analysts expecting for this company next quarter and next year?
  - id: GetEpsRevisions
    intent: Track recent analyst EPS forecast revisions
    question: Have analysts raised or cut their EPS forecasts for this stock over the past week or month?
  - id: GetEpsTrend
    intent: See how EPS estimates have trended over time
    question: How has the consensus EPS estimate for a company moved over the last 90 days?
  - id: GetGrowthEstimates
    intent: Get consensus growth rate projections
    question: What growth rate do analysts project for this company over the next five years?
  - id: GetPriceTarget
    intent: Get analyst price targets for a security
    question: What is the average analyst price target for this stock?
  - id: GetRecommendations
    intent: Get the average analyst recommendation
    question: Is the overall analyst consensus on this stock a strong buy, buy, hold or sell?
  phrasing_ops: 9
  slug: twelvedata-analysis-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The currencies API from Twelve Data — 2 operation(s) for currencies.
  name: Twelve Data Currencies API
  phrasing_intents:
  - id: GetCurrencyConversion
    intent: Convert an amount between two currencies
    question: How much is 500 US dollars in euros at the current rate?
  - id: GetExchangeRate
    intent: Get the current exchange rate for a currency pair
    question: What is the EUR/USD exchange rate right now?
  phrasing_ops: 2
  slug: twelvedata-currencies-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The market_data API from Twelve Data — 6 operation(s) for market_data.
  name: Twelve Data Market Data API
  phrasing_intents:
  - id: GetEod
    intent: Get the end-of-day price for an instrument
    question: What was the closing price of this ETF on a specific date?
  - id: GetMarketMovers
    intent: List the day's top gaining and losing assets
    question: Which stocks are up the most since yesterday's close?
  - id: GetPrice
    intent: Get the latest market price for an instrument
    question: What is the last traded price of this ticker?
  - id: GetQuote
    intent: Get a real-time quote with open, high, low and volume
    question: What are today's open, high, low and volume for a stock?
  - id: GetTimeSeries
    intent: Get historical price bars for an instrument
    question: How do I download a stock's daily price history?
  - id: GetTimeSeriesCross
    intent: Get a cross-rate price history between two assets
    question: What has Apple's price looked like in Indian rupees over time?
  phrasing_ops: 6
  slug: twelvedata-market-data-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The money_market_funds API from Twelve Data — 2 operation(s) for money_market_funds.
  name: Twelve Data Money Market Funds API
  phrasing_intents:
  - id: GetMoneyMarketFundsList
    intent: Browse the money market funds directory
    question: Which money market funds are the largest by fund size?
  - id: GetMoneyMarketFundsWorld
    intent: Get full data for a money market fund
    question: What is a money market fund's yield, liquidity and weighted average maturity?
  phrasing_ops: 2
  slug: twelvedata-money-market-funds-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The mutual_funds API from Twelve Data — 11 operation(s) for mutual_funds.
  name: Twelve Data Mutual Funds API
  phrasing_intents:
  - id: GetMutualFundsFamily
    intent: List mutual fund families
    question: Which investment companies manage mutual fund families in this country?
  - id: GetMutualFundsList
    intent: Browse the mutual funds directory
    question: Which are the largest mutual funds by total assets?
  - id: GetMutualFundsType
    intent: List mutual fund types
    question: What types of mutual funds exist, such as equity, bond or balanced?
  - id: GetMutualFundsWorld
    intent: Get full data for a mutual fund
    question: Can I get a mutual fund's performance, risk, ratings and composition all together?
  - id: GetMutualFundsWorldComposition
    intent: See a mutual fund's holdings and sector mix
    question: What does this mutual fund actually hold?
  - id: GetMutualFundsWorldPerformance
    intent: Get a mutual fund's historical returns
    question: What are this mutual fund's trailing and quarterly returns?
  - id: GetMutualFundsWorldPurchaseInfo
    intent: Get minimum investment and where to buy a fund
    question: What is the minimum investment to buy into this mutual fund?
  - id: GetMutualFundsWorldRatings
    intent: Get ratings for a mutual fund
    question: How is this mutual fund rated by Twelve Data and other institutions?
  phrasing_ops: 11
  slug: twelvedata-mutual-funds-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The regulatory API from Twelve Data — 7 operation(s) for regulatory.
  name: Twelve Data Regulatory API
  phrasing_intents:
  - id: GetDirectHolders
    intent: See who directly holds a company's shares
    question: Who holds shares directly on a company's share registry?
  - id: GetEdgarFilingsArchive
    intent: Search a company's SEC EDGAR filings
    question: Where can I find a company's 10-K and 10-Q filings with the SEC?
  - id: GetFundHolders
    intent: See which mutual funds own a stock
    question: Which mutual funds hold this stock, and how many shares?
  - id: GetInsiderTransactions
    intent: Get insider buying and selling for a stock
    question: Have executives or directors been buying or selling this stock?
  - id: GetInstitutionalHolders
    intent: See which institutions own a stock
    question: Which pension funds and investment firms own this stock?
  - id: GetSourceSanctionedEntities
    intent: List entities sanctioned by an authority
    question: Who is on the OFAC sanctions list?
  - id: GetTaxInfo
    intent: Get tax rates and codes for an instrument
    question: What taxes apply when trading this security?
  phrasing_ops: 7
  slug: twelvedata-regulatory-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The technical_indicator API from Twelve Data — 102 operation(s) for technical_indicator.
  name: Twelve Data Technical Indicator API
  phrasing_intents:
  - id: GetTimeSeriesAd
    intent: Get the accumulation/distribution line
    question: Is money flowing into or out of this stock based on the accumulation/distribution line?
  - id: GetTimeSeriesAdd
    intent: Add two price or indicator series together
    question: Can I sum two price series, like high plus low, point by point?
  - id: GetTimeSeriesAdOsc
    intent: Get the accumulation/distribution oscillator
    question: Is buying or selling pressure shifting according to the Chaikin A/D oscillator?
  - id: GetTimeSeriesAdx
    intent: Measure trend strength with ADX
    question: Is this market trending strongly or just moving sideways, according to ADX?
  - id: GetTimeSeriesAdxr
    intent: Get the smoothed ADX rating (ADXR)
    question: What is the ADXR, the smoothed rating of directional movement, for a symbol?
  - id: GetTimeSeriesApo
    intent: Get the absolute price oscillator
    question: What is the gap between a fast and a slow moving average in price terms?
  - id: GetTimeSeriesAroon
    intent: Get Aroon up and down lines
    question: How long ago did this stock make its highest high and lowest low?
  - id: GetTimeSeriesAroonOsc
    intent: Get the Aroon oscillator
    question: What is the difference between Aroon up and Aroon down for this asset?
  phrasing_ops: 102
  slug: twelvedata-technical-indicator-api
- baseURL: wss://ws.twelvedata.com/v1/quotes/price
  baseurl_source: declared
  description: The etfs API from Twelve Data — 8 operation(s) for etfs.
  name: Twelve Data Etfs API
  phrasing_intents:
  - id: GetETFsFamily
    intent: List ETF fund families
    question: Which ETF fund families are available in a given country?
  - id: GetETFsList
    intent: Browse the ETF directory ranked by assets
    question: Which are the largest ETFs by total assets?
  - id: GetETFsType
    intent: List ETF categories by market
    question: What ETF categories like Large Blend or Equity Precious Metals exist in Singapore?
  - id: GetETFsWorld
    intent: Get full data for a global ETF
    question: Can I get an ETF's summary, performance, risk and holdings in a single response?
  - id: GetETFsWorldComposition
    intent: See an ETF's holdings and sector weights
    question: What stocks does this ETF hold and what are their weights?
  - id: GetETFsWorldPerformance
    intent: Get trailing and annual returns for an ETF
    question: How has this ETF performed over the past one, three and five years?
  - id: GetETFsWorldRisk
    intent: Get volatility and beta risk metrics for an ETF
    question: How volatile is this ETF and what is its beta?
  - id: GetETFsWorldSummary
    intent: Get a quick overview of an ETF
    question: What is the short overview of an ETF, like its name and current value?
  phrasing_ops: 8
  slug: twelvedata-etfs-api
artifact_total: 39
asyncapis:
- description: AsyncAPI 2.6 description of Twelve Data's **real-time price WebSocket**. Unlike a one-way HTTP Server-Sent Events stream, this is a genuine, bidirectional WebSocket (`wss://`) surface. The client open
  name: Twelve Data Real-Time Price WebSocket
  slug: twelvedata-asyncapi
collections:
- collection_type: postman
  name: Twelve Data REST Core Data API
  slug: postman-twelvedata-core-data-api
- collection_type: postman
  name: Twelve Data REST Core Data Fundamentals API
  slug: postman-twelvedata-fundamentals-api
- collection_type: postman
  name: Twelve Data API
  slug: postman-twelvedata-openapi-original
- collection_type: postman
  name: Twelve Data REST Core Data Reference Data API
  slug: postman-twelvedata-reference-data-api
- collection_type: postman
  name: Twelve Data REST Core Data Technical Indicators API
  slug: postman-twelvedata-technical-indicators-api
- collection_type: postman
  name: Twelve Data REST Core Data Time Series API
  slug: postman-twelvedata-time-series-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Twelve Data REST Core Data API
  slug: open-twelvedata-core-data-api
- collection_type: open
  name: Twelve Data REST Core Data Fundamentals API
  slug: open-twelvedata-fundamentals-api
- collection_type: open
  name: Twelve Data API
  slug: open-twelvedata-openapi-original
- collection_type: open
  name: Twelve Data REST Core Data Reference Data API
  slug: open-twelvedata-reference-data-api
- collection_type: open
  name: Twelve Data REST Core Data Technical Indicators API
  slug: open-twelvedata-technical-indicators-api
- collection_type: open
  name: Twelve Data REST Core Data Time Series API
  slug: open-twelvedata-time-series-api
- collection_type: open
  name: Twelve Data REST API
  slug: open-twelvedata
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/twelve-data/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/security/twelvedata-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/twelvedata-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/security/twelvedata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/twelvedata-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/agentic-access/twelvedata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/twelvedata-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/authentication/twelvedata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/twelvedata-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twelve-data
- group: company
  title: ''
  type: Website
  url: https://twelvedata.com
- group: docs
  title: ''
  type: Documentation
  url: https://twelvedata.com/docs
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/plans/twelvedata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/twelvedata-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/rate-limits/twelvedata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/twelvedata-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/finops/twelvedata-finops.yml
  title: ''
  type: FinOps
  url: finops/twelvedata-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://support.twelvedata.com
- group: company
  title: ''
  type: Blog
  url: https://twelvedata.com/blog
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/packages/twelvedata-packages.yml
  title: ''
  type: Packages
  url: packages/twelvedata-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/packages/twelvedata-packages.yml
  title: ''
  type: SDKs
  url: packages/twelvedata-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/cli/twelvedata-cli.yml
  title: ''
  type: CLI
  url: cli/twelvedata-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/well-known/twelvedata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/twelvedata-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/mcp/twelvedata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/twelvedata-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/mcp/twelvedata-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/twelvedata-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/llms/twelvedata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twelvedata-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/conformance/twelvedata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/twelvedata-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.twelvedata.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/errors/twelvedata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/twelvedata-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/lifecycle/twelvedata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/twelvedata-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://twelvedata.isitup.cloud
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.twelvedata.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/changelog/twelvedata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/twelvedata-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/conventions/twelvedata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/twelvedata-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/sandbox/twelvedata-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/twelvedata-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/components/twelvedata-components.yml
  title: ''
  type: Components
  url: components/twelvedata-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/data-model/twelvedata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/twelvedata-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://twelvedata.com/account
- group: docs
  title: ''
  type: APIReference
  url: https://twelvedata.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://twelvedata.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://twelvedata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://twelvedata.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://twelvedata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://twelvedata.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twelvedata
created: '2026-07-11'
description: Twelve Data is a financial market data provider offering real-time and historical data for stocks, forex, cryptocurrencies, ETFs, indices, commodities, and funds through a single REST API and a real-time WebSocket. Coverage spans time series (OHLCV), quotes and prices, 100-plus technical indicators, reference and catalog data, and company fundamentals. Every request is authenticated with an apikey and metered as API credits; a free Basic plan grants 800 API credits per day. Real-time price streaming is delivered over a WebSocket at wss://ws.twelvedata.com/v1/quotes/price.
finops:
- name: Twelvedata Finops
  service_category: Financial Market Data
  slug: twelvedata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/twelvedata.png
layout: provider
mcp_servers:
- description: ''
  name: Twelve Data MCP Server
  slug: twelve-data-mcp-server
modified: '2026-07-22'
name: Twelve Data
nav: Providers
network: true
overview: 'Twelve Data publishes 15 APIs on the [APIs.io](https://apis.io/) network, including WebSocket Streaming API, Core Data API, Fundamentals API, and 12 more. Tagged areas include Market Data, Financial Data, Stocks, Forex, and Crypto.


  The Twelve Data catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Twelve Data''s developer surface includes authentication, documentation, support, engineering blog, CLI, changelog, sandbox, and 33 more developer resources.'
plans:
- name: Twelvedata Plans Pricing
  plan_count: 5
  slug: twelvedata-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Twelvedata Rate Limits
  slug: twelvedata-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Twelve Data API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: twelvedata-asyncapi-spectral-rules
score:
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.4
    catalog_earned_first_party: 0.0
    catalog_gap: 49.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 96.8
    contract_governance: 15.9
    contract_quality: 57.3
    developer_ergonomics: 81.5
    discoverability: 75.0
    operational_transparency: 65.3
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/twelvedata/refs/heads/main/screenshots/twelvedata-2026-08-17T130124.png
security:
- kind: authentication
  name: Twelvedata Authentication
  slug: twelvedata-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Twelvedata Domain Security
  slug: twelvedata-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Twelvedata Trust Center
  slug: twelvedata-trust-center
  summary_line: SOC 2, GDPR
slug: twelvedata
tags:
- Market Data
- Financial Data
- Stocks
- Forex
- Crypto
- Real-Time Data
- Technical Indicators
- Fundamentals
- Real-Time
website: https://twelvedata.com
---
