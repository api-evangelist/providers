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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Wazirx Agentic Access
  operation_count: 27
  slug: wazirx-agentic-access
  summary_line: 27 operations · 6 acting
api_count: 1
apis:
- description: The WazirX WebSocket API provides real-time streaming for market data including trades, 24hr tickers, candlestick (kline) data, and order book depth updates. Private streams for account balance change
  name: WazirX WebSocket API
  slug: wazirx-websocket-api
- description: Authenticated endpoints for account information and balances
  name: WazirX Account API
  slug: wazirx-account-api
- description: General API endpoints for connectivity and system information
  name: WazirX General API
  slug: wazirx-general-api
- description: Public market data endpoints for price, volume, and order book information
  name: WazirX Market Data API
  slug: wazirx-market-data-api
- description: Authenticated endpoints for sub-account management and fund transfers
  name: WazirX Sub-Account API
  slug: wazirx-sub-account-api
- description: Authenticated endpoints for order management and trade history
  name: WazirX Trading API
  slug: wazirx-trading-api
- description: Authenticated endpoints for coin and withdrawal/deposit management
  name: WazirX Wallet API
  slug: wazirx-wallet-api
- description: Endpoints for WebSocket authentication token generation
  name: WazirX WebSocket API
  slug: wazirx-websocket-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WazirX REST Account API
  slug: open-wazirx-account-api
- collection_type: open
  name: WazirX REST Account General API
  slug: open-wazirx-general-api
- collection_type: open
  name: WazirX REST Account Market Data API
  slug: open-wazirx-market-data-api
- collection_type: open
  name: WazirX REST Account Sub-Account API
  slug: open-wazirx-sub-account-api
- collection_type: open
  name: WazirX REST Account Trading API
  slug: open-wazirx-trading-api
- collection_type: open
  name: WazirX REST Account Wallet API
  slug: open-wazirx-wallet-api
- collection_type: open
  name: WazirX REST Account WebSocket API
  slug: open-wazirx-websocket-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wazirx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wazirx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wazirx-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wazirx.com/
- group: company
  title: ''
  type: Blog
  url: https://wazirx.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.wazirx.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/WazirX
- group: operate
  title: ''
  type: Status
  url: https://wazirx.statuspage.io/
- group: start
  title: ''
  type: Signup
  url: https://wazirx.com/register
- group: start
  title: ''
  type: Login
  url: https://wazirx.com/login
- group: auth
  title: ''
  type: ApiKeysSettings
  url: https://wazirx.com/settings/keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wazirx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wazirx.com/privacy
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/wazirx/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/wazirx/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/wazirx/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: WazirX is an Indian cryptocurrency exchange (transitioning to Zettai) providing REST and WebSocket APIs for spot trading on INR and crypto markets, order management, market data, account management, and wallet operations. The exchange supports automated trading via HMAC SHA256-authenticated endpoints and real-time streaming through WebSocket connections.
examples:
- key_count: 3
  name: Exchange Info Response
  slug: exchange-info-response
- key_count: 3
  name: Order Book Response
  slug: order-book-response
- key_count: 9
  name: Order Create Request
  slug: order-create-request
- key_count: 12
  name: Order Response
  slug: order-response
- key_count: 0
  name: Ping Response
  slug: ping-response
- key_count: 11
  name: Ticker 24Hr Response
  slug: ticker-24hr-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wazirx.png
json_schemas:
- name: WazirX Order
  property_count: 12
  slug: order
- name: WazirX 24hr Ticker
  property_count: 11
  slug: ticker
- name: WazirX Trade
  property_count: 6
  slug: trade
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
layout: provider
modified: '2026-06-13'
name: WazirX
nav: Providers
network: true
overview: 'WazirX publishes 8 APIs on the [APIs.io](https://apis.io/) network, including WebSocket API, Account API, General API, and 5 more. Tagged areas include Cryptocurrency, Exchange, Trading, INR, and India.


  The WazirX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WazirX''s developer surface includes authentication, engineering blog, support, GitHub presence, status page, signup flow, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WazirX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wazirx-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 58.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 9.8
    contract_quality: 54.9
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wazirx/refs/heads/main/screenshots/wazirx-2026-06-20T201306.png
security:
- kind: authentication
  name: Wazirx Authentication
  slug: wazirx-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Wazirx Domain Security
  slug: wazirx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wazirx
tags:
- Cryptocurrency
- Exchange
- Trading
- INR
- India
- Bitcoin
- WebSocket
- Market Data
website: https://wazirx.com/
---
