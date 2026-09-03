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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bitstamp Agentic Access
  operation_count: 7
  slug: bitstamp-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: Real-time WebSocket API providing live market data streams including order book updates, live trades, ticker data, and private account event channels via authenticated token-based subscriptions.
  name: Bitstamp WebSocket API
  slug: bitstamp-websocket-api
- baseURL: https://www.bitstamp.net
  baseurl_source: declared
  description: Public market data endpoints (no authentication required)
  name: Bitstamp Market Data API
  slug: bitstamp-market-data-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bitstamp Market Data API
  slug: open-bitstamp-market-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitstamp-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitstamp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitstamp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitstamp-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://www.bitstamp.net/api/#authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitstamp.net/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitstamp.net/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bitstamp.net/
- group: operate
  title: ''
  type: Support
  url: https://www.bitstamp.net/support/
- group: start
  title: ''
  type: Login
  url: https://www.bitstamp.net/account/login/
- group: start
  title: ''
  type: Signup
  url: https://www.bitstamp.net/account/register/
- group: other
  title: ''
  type: FeeSchedule
  url: https://www.bitstamp.net/fee_schedule/
- group: company
  title: ''
  type: Blog
  url: https://www.bitstamp.net/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bitstamp/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Bitstamp
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Bitstamp/
created: '2026-06-13'
description: European cryptocurrency exchange offering REST and WebSocket APIs for spot trading, order management, market data, account balances, and transaction history across major crypto pairs. Founded in 2011, Bitstamp provides institutional-grade infrastructure with HMAC-SHA256 authenticated private endpoints, real-time WebSocket streaming, margin trading, derivatives, staking, and travel-rule compliance tooling.
examples:
- key_count: 5
  name: Getcurrencies
  slug: getcurrencies
- key_count: 5
  name: Gethourlyticker
  slug: gethourlyticker
- key_count: 5
  name: Getohlcdata
  slug: getohlcdata
- key_count: 5
  name: Getorderbook
  slug: getorderbook
- key_count: 5
  name: Getticker
  slug: getticker
- key_count: 5
  name: Gettradingpairsinfo
  slug: gettradingpairsinfo
- key_count: 5
  name: Gettransactions
  slug: gettransactions
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitstamp.png
json_schemas:
- name: ErrorResponse
  property_count: 3
  slug: errorresponse
- name: OhlcEntry
  property_count: 6
  slug: ohlcentry
- name: OhlcResponse
  property_count: 1
  slug: ohlcresponse
- name: OrderBook
  property_count: 4
  slug: orderbook
- name: Ticker
  property_count: 13
  slug: ticker
- name: TradingPairInfo
  property_count: 9
  slug: tradingpairinfo
- name: Transaction
  property_count: 5
  slug: transaction
layout: provider
modified: '2026-06-13'
name: Bitstamp
nav: Providers
network: true
overview: 'Bitstamp publishes 1 API on the [APIs.io](https://apis.io/) network: Market Data API. Tagged areas include Cryptocurrency, Exchange, Trading, Bitcoin, and Ethereum.


  The Bitstamp catalog on APIs.io includes 1 Spectral governance ruleset.


  Bitstamp''s developer surface includes authentication, support, signup flow, engineering blog, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 7
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bitstamp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bitstamp-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 9.8
    contract_quality: 55.1
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 40.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitstamp/refs/heads/main/screenshots/bitstamp-2026-06-20T173325.png
security:
- kind: authentication
  name: Bitstamp Authentication
  slug: bitstamp-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bitstamp Domain Security
  slug: bitstamp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bitstamp Vulnerability Disclosure
  slug: bitstamp-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: bitstamp
tags:
- Cryptocurrency
- Exchange
- Trading
- Bitcoin
- Ethereum
- Spot Trading
- WebSocket
- Market Data
- Order Management
- Finance
---
