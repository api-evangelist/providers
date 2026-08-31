---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 66.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Eodhd Agentic Access
  operation_count: 84
  slug: eodhd-agentic-access
  summary_line: 84 operations
api_count: 2
apis:
- description: Provides intraday historical OHLCV data at 1-minute, 5-minute, and 1-hour intervals for US stocks and other supported markets, with multi-year lookbacks depending on the resolution.
  name: EODHD Intraday Historical Data API
  slug: intraday-historical-data-api
- description: Returns live or 15-20 minute delayed stock quotes including last price, change, volume, and bid/ask data for stocks, ETFs, indices, and forex pairs across global exchanges.
  name: EODHD Live (Delayed) Stock Prices API
  slug: live-prices-api
- description: Streams real-time trade and quote updates over WebSockets for US stocks, forex, and cryptocurrencies, allowing low-latency consumption of live market data.
  name: EODHD WebSockets Real-Time API
  slug: websockets-api
- description: Provides company fundamentals including general info, financial statements (income statement, balance sheet, cash flow), earnings, valuation ratios, ETF holdings, and mutual fund details.
  name: EODHD Fundamental Data API
  slug: fundamental-data-api
- description: Returns US stock options chain data with strikes, expirations, bid/ask, open interest, implied volatility, and Greeks (delta, gamma, theta, vega).
  name: EODHD Stock Options API
  slug: options-data-api
- description: Computes common technical indicators server-side, including SMA, EMA, RSI, MACD, Bollinger Bands, ATR, and stochastic oscillators, on top of the EODHD historical price database.
  name: EODHD Technical Indicators API
  slug: technical-indicators-api
- description: Provides a global economic calendar of macroeconomic releases including country, event name, scheduled time, prior, forecast, and actual values.
  name: EODHD Economic Events Calendar API
  slug: economic-events-api
- description: Delivers financial news articles tagged by ticker symbol with sentiment scoring (positive, negative, neutral) for use in research, trading signals, and news-driven workflows.
  name: EODHD Financial News and Sentiment API
  slug: news-sentiment-api
- description: Lists supported exchanges and instruments with metadata including ticker, exchange code, name, type, and identifier mappings (CUSIP, ISIN, FIGI) to support symbol lookup and reference data workflows.
  name: EODHD Exchanges and Symbols API
  slug: exchanges-and-tickers-api
- description: The Eod API from EODHD — 1 operation(s) for eod.
  name: EODHD Eod API
  slug: eodhd-eod-api
- description: Calendar events including earnings, IPOs, splits, dividends, and trends
  name: EODHD Calendar API
  slug: eodhd-calendar-api
- description: CBOE index data and listings
  name: EODHD CBOE API
  slug: eodhd-cboe-api
- description: Symbol changes and insider transactions
  name: EODHD Corporate Actions API
  slug: eodhd-corporate-actions-api
- description: Sovereign risk premiums, credit ratings, CDS spreads, and corporate credit metrics
  name: EODHD Credit & Sovereign Risk API
  slug: eodhd-credit-sovereign-risk-api
- description: Dividend and split history
  name: EODHD Dividends & Splits API
  slug: eodhd-dividends-splits-api
- description: Economic events and macro indicators
  name: EODHD Economic Data API
  slug: eodhd-economic-data-api
- description: Historical and current end-of-day price data
  name: EODHD End-of-Day Data API
  slug: eodhd-end-of-day-data-api
- description: Environmental, Social, and Governance ratings (Investverte)
  name: EODHD ESG API
  slug: eodhd-esg-api
- description: Exchange information and symbols
  name: EODHD Exchanges API
  slug: eodhd-exchanges-api
- description: Fundamental data for stocks and companies
  name: EODHD Fundamentals API
  slug: eodhd-fundamentals-api
- description: S&P/Dow Jones indices data and components
  name: EODHD Indices API
  slug: eodhd-indices-api
- description: Reference rates, central bank policy rates, and funding-stress spreads
  name: EODHD Interest Rates API
  slug: eodhd-interest-rates-api
- description: Intraday historical price data (time-based bars)
  name: EODHD Intraday Data API
  slug: eodhd-intraday-data-api
- description: Risk scoring, bond analysis, bank financials, reports (PRAAMS)
  name: EODHD Investment Analytics API
  slug: eodhd-investment-analytics-api
- description: Delayed real-time stock prices and US delayed quotes
  name: EODHD Live (Delayed) Data API
  slug: eodhd-live-delayed-data-api
- description: Company and ticker logos
  name: EODHD Logos API
  slug: eodhd-logos-api
- description: Market capitalization and other market data
  name: EODHD Market Data API
  slug: eodhd-market-data-api
- description: Financial news and sentiment analysis
  name: EODHD News API
  slug: eodhd-news-api
- description: Options contracts and pricing data
  name: EODHD Options API
  slug: eodhd-options-api
- description: Sanctioned entities, vessels, programs, and sources (OFAC and others)
  name: EODHD Sanctions API
  slug: eodhd-sanctions-api
- description: Stock screening tools
  name: EODHD Screening API
  slug: eodhd-screening-api
- description: Technical analysis indicators
  name: EODHD Technical API
  slug: eodhd-technical-api
- description: Historical and marketplace tick-level trade data
  name: EODHD Tick Data API
  slug: eodhd-tick-data-api
- description: US Treasury interest rates (bills, yields, long-term, real yields)
  name: EODHD US Treasury API
  slug: eodhd-us-treasury-api
- description: User account and subscription information
  name: EODHD User API
  slug: eodhd-user-api
artifact_total: 54
asyncapis:
- description: Real-time streaming of US equity trades and quotes, forex, and cryptocurrency prices over WebSockets with sub-50ms latency. Authenticates with the same api_token used by the REST API (validated during
  name: EODHD WebSockets Real-Time API
  slug: eodhd-websockets-asyncapi
collections:
- collection_type: postman
  name: EODHD End-Of-Day Historical Data Eod API
  slug: postman-eodhd-eod-api
- collection_type: postman
  name: EODHD Financial Data API
  slug: postman-eodhd-financial-data
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EODHD End-Of-Day Historical Data Eod API
  slug: open-eodhd-eod-api
- collection_type: open
  name: EODHD End-Of-Day Historical Data API
  slug: open-eodhd-eod-historical-data
- collection_type: open
  name: EODHD Financial Data API
  slug: open-eodhd-financial-data
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/eodhd/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eodhd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eodhd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eodhd-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eodhd-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/eodhd-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eodhd-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eodhd-well-known.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/eodhd-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eodhd-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/eodhd-financial-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/eodhd-eod-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/eodhd-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eodhd-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eodhd-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eodhd-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eodhd-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eodhd-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/eodhd-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eodhd-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eodhd-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EodHistoricalData
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eodhd-apis
- group: company
  title: ''
  type: Website
  url: https://eodhd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://eodhd.com/financial-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://eodhd.com/financial-apis/
- group: docs
  title: ''
  type: APIReference
  url: https://eodhd.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://eodhd.com/financial-apis
- group: commercial
  title: ''
  type: Pricing
  url: https://eodhd.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://eodhd.com/register
- group: start
  title: ''
  type: Login
  url: https://eodhd.com/login
- group: operate
  title: ''
  type: Support
  url: https://forum.eodhd.com/
- group: other
  title: ''
  type: Marketplace
  url: https://eodhd.com/marketplace
- group: company
  title: ''
  type: Blog
  url: https://eodhd.com/financial-apis-blog/
- group: operate
  title: ''
  type: Forums
  url: https://forum.eodhd.com/
- group: learn
  title: ''
  type: Training
  url: https://eodhd.com/financial-academy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/eodhd
- group: other
  title: ''
  type: Affiliate
  url: https://eodhd.com/financial-apis/eodhd-affiliate-program
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eodhd.com/financial-apis/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eodhd.com/financial-apis/terms-conditions
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eodhd-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://eodhd.com/financial-apis-blog/eodhd-mcp-server-update-75-tools-oauth-and-api-versioning
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://eodhd.com/financial-apis-blog/announcing-eodhd-claude-skills-teach-your-ai-the-entire-financial-api
- group: agent
  title: ''
  type: LlmsText
  url: https://eodhd.com/llms.txt
created: '2025-02-24'
description: Access historical end-of-day stock prices, intraday data, US stock options, and real-time prices with free and advanced plans. EODHD provides financial data for 150,000+ tickers, including stocks, ETFs, funds, and currencies worldwide, through 68+ REST endpoints, WebSocket streaming, an official OpenAPI 3.1.0 specification, an OAuth-secured MCP server with 86 tools, and a published Claude Skills plugin.
finops:
- name: Eodhd Finops
  service_category: Market Data
  slug: eodhd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eodhd.png
json_schemas:
- name: EodBar
  property_count: 7
  slug: eodhd-eodbar
json_structures:
- name: Eodhd Structure
  property_count: 0
  slug: eodhd-structure
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: ''
  name: MCP Server announcement
  slug: mcp-server-announcement
modified: '2026-07-22'
name: EODHD
nav: Providers
network: true
overview: 'EODHD publishes 27 APIs on the [APIs.io](https://apis.io/) network, including WebSockets Real-Time API, Eod API, Calendar API, and 24 more. Tagged areas include Financial, Market Data, Stock Options, Stocks, and ETFs.


  The EODHD catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  EODHD''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, pricing, and 38 more developer resources.'
plans:
- name: Eodhd Plans Pricing
  plan_count: 6
  slug: eodhd-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Eodhd Rate Limits
  slug: eodhd-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: EODHD API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: eodhd-jsonschema-spectral-rules
scopes:
- name: Eodhd Scopes
  scope_count: 12
  slug: eodhd-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 31
    catalog_gap: 65.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 14.4
    contract_quality: 62.2
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 14.4
    operational_transparency: 26.3
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eodhd/refs/heads/main/screenshots/eodhd-2026-06-20T180745.png
security:
- kind: authentication
  name: Eodhd Authentication
  slug: eodhd-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Eodhd Domain Security
  slug: eodhd-domain-security
  summary_line: TLSv1.2
slug: eodhd
tags:
- Financial
- Market Data
- Stock Options
- Stocks
- ETFs
- Forex
- Cryptocurrency
- Fundamentals
- News
website: https://eodhd.com/
---
