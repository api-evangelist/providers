---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Financialmodelingprep Agentic Access
  operation_count: 16
  slug: financialmodelingprep-agentic-access
  summary_line: 16 operations
api_count: 7
apis:
- description: Real-time streaming market data over WebSocket for stocks, crypto, and forex. Clients connect, send a login event carrying their API key, then subscribe to tickers to receive top-of-book quote and las
  name: Financial Modeling Prep Real-Time WebSocket API
  slug: financialmodelingprep-realtime-websocket-api
- description: Consensus estimates, price targets, and rating grades.
  name: Financial Modeling Prep Analyst Estimates API
  slug: financialmodelingprep-analyst-estimates-api
- description: Macroeconomic indicators, treasury rates, and economic calendar.
  name: Financial Modeling Prep Economic Data API
  slug: financialmodelingprep-economic-data-api
- description: Income statement, balance sheet, and cash-flow statement data.
  name: Financial Modeling Prep Financial Statements API
  slug: financialmodelingprep-financial-statements-api
- description: Company profile plus derived key metrics and ratios.
  name: Financial Modeling Prep Fundamentals API
  slug: financialmodelingprep-fundamentals-api
- description: Real-time quotes and historical end-of-day prices.
  name: Financial Modeling Prep Quotes and Prices API
  slug: financialmodelingprep-quotes-and-prices-api
- description: Latest and searchable SEC filings for public companies.
  name: Financial Modeling Prep SEC Filings API
  slug: financialmodelingprep-sec-filings-api
artifact_total: 15
asyncapis:
- description: AsyncAPI 2.6 description of Financial Modeling Prep's real-time market data WebSocket surface, documented at https://site.financialmodelingprep.com/datasets/websocket and https://site.financialmodelin
  name: Financial Modeling Prep Real-Time WebSocket API
  slug: financialmodelingprep-asyncapi
collections:
- collection_type: open
  name: Financial Modeling Prep API
  slug: open-financialmodelingprep
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/financialmodelingprep-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/financialmodelingprep-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FinancialModelingPrepAPI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/financial-modeling-prep
- group: company
  title: ''
  type: Website
  url: https://site.financialmodelingprep.com/
- group: docs
  title: ''
  type: Documentation
  url: https://site.financialmodelingprep.com/developer/docs/stable
- group: commercial
  title: ''
  type: Plans
  url: plans/financialmodelingprep-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/financialmodelingprep-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/financialmodelingprep-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://site.financialmodelingprep.com/market-news
created: '2026-07-11'
description: Financial Modeling Prep (FMP) is a financial data API provider offering real-time and historical market data, company fundamentals, and regulatory filings through more than 100 REST endpoints plus real-time WebSocket streams. Coverage includes income statements, balance sheets, and cash-flow statements; stock, ETF, index, forex, crypto, and commodity quotes; up to 30 years of historical prices; SEC filings (10-K, 10-Q, 8-K); analyst estimates and price targets; key metrics, ratios, and enterprise values; and macroeconomic indicators such as GDP, treasury rates, and inflation. Data is delivered as JSON or CSV over the stable REST base (financialmodelingprep.com/stable) with API-key authentication, and a free tier allows up to 250 requests per day.
finops:
- name: Financialmodelingprep Finops
  service_category: Financial Data and Market Data
  slug: financialmodelingprep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/financialmodelingprep.png
layout: provider
modified: '2026-07-11'
name: Financial Modeling Prep
nav: Providers
network: true
overview: 'Financial Modeling Prep publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Real-Time WebSocket API, Analyst Estimates API, Economic Data API, and 4 more. Tagged areas include Financial Data, Market Data, Fundamentals, SEC Filings, and Stocks.


  The Financial Modeling Prep catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Financial Modeling Prep''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Financialmodelingprep Plans Pricing
  plan_count: 5
  slug: financialmodelingprep-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Financialmodelingprep Rate Limits
  slug: financialmodelingprep-rate-limits
rules:
- name: Financial Modeling Prep API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: financialmodelingprep-asyncapi-spectral-rules
score:
  band: thin
  composite: 41.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Financialmodelingprep Authentication
  slug: financialmodelingprep-authentication
  summary_line: apiKey · 1 scheme
slug: financialmodelingprep
tags:
- Financial Data
- Market Data
- Fundamentals
- SEC Filings
- Stocks
- Economic Indicators
- Quotes
- Regulatory Filings
website: https://site.financialmodelingprep.com/
---
