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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-08-26'
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
artifact_total: 29
asyncapis:
- description: The TradeStation Streaming API provides real-time HTTP streaming endpoints for market data and brokerage events. Streams use HTTP chunked transfer encoding with newline-delimited JSON objects. Each st
  name: TradeStation Streaming API
  slug: tradestation-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TradeStation Accounts API
  slug: open-tradestation-accounts-api
- collection_type: open
  name: TradeStation API
  slug: open-tradestation-api
- collection_type: open
  name: TradeStation Accounts Market Data API
  slug: open-tradestation-market-data-api
- collection_type: open
  name: TradeStation Accounts Options API
  slug: open-tradestation-options-api
- collection_type: open
  name: TradeStation Accounts Order Execution API
  slug: open-tradestation-order-execution-api
- collection_type: open
  name: TradeStation Accounts Reference Data API
  slug: open-tradestation-reference-data-api
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
random_paper: 17
rate_limits:
- limit_count: 5
  name: Tradestation Rate Limits
  slug: tradestation-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: TradeStation API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: tradestation-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: TradeStation API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: tradestation-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: TradeStation API Rules
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
  composite: 45.6
  delta: 1.8
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 73.1
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 43.8
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tradestation/refs/heads/main/screenshots/tradestation-2026-08-17T125935.png
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
