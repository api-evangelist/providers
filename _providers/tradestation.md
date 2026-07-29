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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Tradestation Agentic Access
  operation_count: 23
  slug: tradestation-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 6
apis:
- description: 'The TradeStation Streaming API provides real-time HTTP streaming endpoints using chunked transfer encoding with newline-delimited JSON for market data and brokerage events. Streams deliver live quote '
  name: TradeStation Streaming API
  slug: tradestation-streaming
- description: Retrieve account information including account details, balances, beginning-of-day balances, positions, orders, historical orders, and cryptocurrency wallets.
  name: TradeStation Accounts API
  slug: tradestation-accounts-api
- description: Access real-time and historical market data including quotes, bar charts, symbol information, symbol lists, and cryptocurrency pairs.
  name: TradeStation Market Data API
  slug: tradestation-market-data-api
- description: Retrieve options-related market data including expirations, strike prices, spread types, and risk/reward calculations.
  name: TradeStation Options API
  slug: tradestation-options-api
- description: Place, confirm, modify, and cancel orders for stocks, options, and futures. Includes support for group orders such as bracket and OCO orders.
  name: TradeStation Order Execution API
  slug: tradestation-order-execution-api
- description: Access reference data for order execution including activation triggers and available routing destinations.
  name: TradeStation Reference Data API
  slug: tradestation-reference-data-api
artifact_total: 23
asyncapis:
- description: The TradeStation Streaming API provides real-time HTTP streaming endpoints for market data and brokerage events. Streams use HTTP chunked transfer encoding with newline-delimited JSON objects. Each st
  name: TradeStation Streaming API
  slug: tradestation-streaming-asyncapi
collections:
- collection_type: open
  name: TradeStation API
  slug: open-tradestation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tradestation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradestation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tradestation-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tradestation-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tradestation
- group: company
  title: ''
  type: Website
  url: https://www.tradestation.com
- group: other
  title: ''
  type: Developer
  url: https://developer.tradestation.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.tradestation.com/docs/
- group: auth
  title: ''
  type: Authentication
  url: https://api.tradestation.com/docs/fundamentals/authentication/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tradestation
- group: operate
  title: ''
  type: RateLimiting
  url: https://api.tradestation.com/docs/fundamentals/rate-limiting/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradestation.com/important-information/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.tradestation.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.tradestation.com/insights/feed/
created: '2026-03-24'
description: TradeStation is a financial brokerage and trading platform offering a collection of RESTful brokerage and market data services for building trading applications for stocks, options, futures, and cryptocurrency. The API provides endpoints for account management, order placement and execution, real-time and historical market data, option chains, symbol information, and HTTP streaming for live market feeds. TradeStation supports advanced order types including bracket, OCO, OSO, and multi-leg options orders with OAuth2 authentication.
examples:
- key_count: 2
  name: Tradestation Get Quotes Example
  slug: tradestation-get-quotes-example
- key_count: 2
  name: Tradestation Place Order Example
  slug: tradestation-place-order-example
finops:
- name: Tradestation Finops
  service_category: API
  slug: tradestation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tradestation.png
json_schemas:
- name: TradeStation Order
  property_count: 12
  slug: tradestation-order
json_structures:
- name: Tradestation Order Structure
  property_count: 0
  slug: tradestation-order-structure
jsonld:
- class_count: 0
  name: Tradestation Context
  property_count: 8
  slug: tradestation-context
layout: provider
modified: '2026-05-19'
name: TradeStation
nav: Providers
network: true
overview: 'TradeStation publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Streaming API, Accounts API, Market Data API, and 3 more. Tagged areas include Brokerage, Cryptocurrency, Finance, Futures, and Market Data.


  The TradeStation catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  TradeStation''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Tradestation Plans Pricing
  plan_count: 3
  slug: tradestation-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Tradestation Rate Limits
  slug: tradestation-rate-limits
rules:
- name: TradeStation API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: tradestation-asyncapi-spectral-rules
- name: TradeStation API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: tradestation-jsonschema-spectral-rules
- name: TradeStation API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 5
  slug: tradestation-rules
scopes:
- name: Tradestation Scopes
  scope_count: 3
  slug: tradestation-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 52.8
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 78.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 61.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tradestation Authentication
  slug: tradestation-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tradestation Domain Security
  slug: tradestation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tradestation
tags:
- Brokerage
- Cryptocurrency
- Finance
- Futures
- Market Data
- Options
- Stocks
- Trading
website: https://www.tradestation.com
---
