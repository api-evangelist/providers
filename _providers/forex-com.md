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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Forex Com Agentic Access
  operation_count: 17
  slug: forex-com-agentic-access
  summary_line: 17 operations · 5 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Authenticate and manage API sessions for the FOREX.com trading platform. A POST request to the session endpoint with username, password, and AppKey returns a session ID used as a header credential for
  name: FOREX.com Session API
  slug: forex-com-session-api
- description: Retrieve client and trading account details including account IDs, balance, available margin, and personal account information. The /useraccount/ClientAndTradingAccount endpoint returns the Trading Ac
  name: FOREX.com Account API
  slug: forex-com-account-api
- description: Search and retrieve market details for tradeable instruments across 80+ forex and CFD markets. Supports full market search by name or tag to resolve Market IDs used in order placement and price subscr
  name: FOREX.com Market API
  slug: forex-com-market-api
- description: Access real-time and historical price data for forex and CFD markets. Real-time bid/ask/offer prices are delivered via Lightstreamer streaming subscriptions using MERGE mode. Historical OHLC price dat
  name: FOREX.com Pricing API
  slug: forex-com-pricing-api
- description: 'Place and manage trade orders on the FOREX.com platform against live streaming prices. Supports market price orders with configurable direction (Buy/Sell), quantity, stop-loss, take-profit, and price '
  name: FOREX.com Order API
  slug: forex-com-order-api
- description: List and manage open trading positions on the FOREX.com platform. Retrieve active positions including unrealised P&L, direction, quantity, and pricing details for all open trades in a trading account.
  name: FOREX.com Position API
  slug: forex-com-position-api
- description: Client and trading account information
  name: FOREX.com Account API
  slug: forex-com-account-api
- description: Account margin and cash balance
  name: FOREX.com Margin API
  slug: forex-com-margin-api
- description: Market search and instrument lookup
  name: FOREX.com Market API
  slug: forex-com-market-api
- description: Trade order placement and management
  name: FOREX.com Orders API
  slug: forex-com-orders-api
- description: Open position management
  name: FOREX.com Positions API
  slug: forex-com-positions-api
- description: Real-time tick history and OHLC bar history
  name: FOREX.com Pricing API
  slug: forex-com-pricing-api
- description: Authentication and session management
  name: FOREX.com Session API
  slug: forex-com-session-api
artifact_total: 37
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forex-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/forex-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forex-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forex-com-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.forex.com/en/trading-tools/api-trading/
- group: docs
  title: ''
  type: Documentation
  url: https://www.forex.com/en/trading-tools/api-trading/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.forex.com/en/trading-tools/api-trading/
- group: other
  title: ''
  type: BaseURL
  url: https://ciapi.cityindex.com/TradingAPI/
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/ali-zahedi/forexcom
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/rickykim93/gcapi-python
- group: commercial
  title: ''
  type: Pricing
  url: https://www.forex.com/en-us/trading-accounts/spread-only-account/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.forex.com/en-us/trading-accounts/raw-pricing-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.forex.com/en-us/help-and-support/pricing-and-fees/
- group: company
  title: ''
  type: Website
  url: https://www.forex.com/
- group: start
  title: ''
  type: Signup
  url: https://www.forex.com/en-us/trading-accounts/new-trading-account/
- group: operate
  title: ''
  type: Support
  url: https://www.forex.com/en/help-and-support/
created: '2026-06-13'
description: FOREX.com is a regulated forex and CFD trading broker (a brand of StoneX Group) offering REST and FIX APIs for automated trading and market data access. The REST API, hosted at ciapi.cityindex.com/TradingAPI, enables algorithmic traders to authenticate sessions, retrieve real-time streaming prices via Lightstreamer, execute buy/sell orders across 80+ forex and CFD markets, and manage account balances, positions, and order history programmatically. A FIX API is available for institutional clients requiring low-latency direct market connectivity.
features:
- REST API using JSON over HTTP at base URL https://ciapi.cityindex.com/TradingAPI/
- Header-based authentication with UserName and Session ID obtained from /session endpoint
- AppKey required — obtained by contacting support.en@forex.com (3 business day activation)
- Real-time bid/ask/offer pricing via Lightstreamer streaming (STREAMINGALL adapter, MERGE mode)
- Historical OHLC price data up to 4,000 records per request with date range and price type options
- Order execution for Buy/Sell with stop-loss, take-profit, and price tolerance slippage control
- Order status streaming subscription for real-time execution updates
- Account balance, available margin, open positions, and historical trade access
- 80+ forex and CFD markets supported including all major and minor currency pairs
- FIX API available for institutional clients requiring lower latency and local liquidity sourcing
- FIX API liquidity sourced locally in London, Tokyo, and New York for reduced latency
- Compatible with Spread-Only and RAW Pricing account types
- RAW Pricing accounts: spreads from 0.2 pips on EUR/USD with $7 USD commission per $100k notional
- Spread-Only accounts: commission-free with wider spreads (avg 1.00 pip on EUR/USD)
- Minimum deposit $100; recommended $2,500 for adequate risk buffer
- Language-agnostic: integrations documented in Python, C++, Perl, VB.NET
finops:
- name: Forex Com Finops
  service_category: Financial Services
  slug: forex-com-finops
image: https://www.forex.com/favicon.ico
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: FOREX.com
nav: Providers
network: true
overview: 'FOREX.com publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Session API, Account API, Market API, and 8 more. Tagged areas include Forex, FX Trading, CFD Trading, Algorithmic Trading, and Financial Services.


  The FOREX.com catalog on APIs.io includes 1 JSON-LD context.


  FOREX.com''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, signup flow, support, and 9 more developer resources.'
plans:
- name: Forex Com Plans Pricing
  plan_count: 3
  slug: forex-com-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 4
  name: Forex Com Rate Limits
  slug: forex-com-rate-limits
score:
  band: developing
  composite: 46.2
  delta: -1.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.9
    developer_ergonomics: 43.5
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forex-com/refs/heads/main/screenshots/forex-com-2026-06-20T181434.png
security:
- kind: authentication
  name: Forex Com Authentication
  slug: forex-com-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Forex Com Domain Security
  slug: forex-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Forex Com Vulnerability Disclosure
  slug: forex-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: forex-com
tags:
- Forex
- FX Trading
- CFD Trading
- Algorithmic Trading
- Financial Services
- Trading APIs
- Currency Exchange
website: https://www.forex.com/
---
