---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
api_count: 15
apis:
- description: REST API for Bitrue spot trading -- market data (depth, trades, klines, tickers), exchange info, account, order placement and cancellation, trade history, deposits and withdrawals, plus a listenKey us
  name: Bitrue Spot API
  slug: bitrue-spot-api
- description: REST API for Bitrue USDT-margined perpetual futures -- contracts, depth, klines, tickers, account, leverage brackets, commission rate, orders, trades and transfer history.
  name: Bitrue USDT-M Futures API
  slug: bitrue-usdt-m-futures-api
- description: REST API for Bitrue coin-margined (inverse) perpetual futures -- market data, account and order management.
  name: Bitrue COIN-M Futures API
  slug: bitrue-coin-m-futures-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Bitrue API API from Bitrue — 2 operation(s) for bitrue api.
  name: Bitrue Bitrue API
  slug: bitrue-bitrue-api-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Etf API from Bitrue — 1 operation(s) for etf.
  name: Bitrue Etf API
  slug: bitrue-etf-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Fapi API from Bitrue — 1 operation(s) for fapi.
  name: Bitrue Fapi API
  slug: bitrue-fapi-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The History API from Bitrue — 1 operation(s) for history.
  name: Bitrue History API
  slug: bitrue-history-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Market API from Bitrue — 1 operation(s) for market.
  name: Bitrue Market API
  slug: bitrue-market-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The MyTrades API from Bitrue — 1 operation(s) for mytrades.
  name: Bitrue My Trades API
  slug: bitrue-mytrades-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Order API from Bitrue — 1 operation(s) for order.
  name: Bitrue Order API
  slug: bitrue-order-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Poseidon API from Bitrue — 2 operation(s) for poseidon.
  name: Bitrue Poseidon API
  slug: bitrue-poseidon-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Sapi API from Bitrue — 2 operation(s) for sapi.
  name: Bitrue Sapi API
  slug: bitrue-sapi-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Ticker API from Bitrue — 1 operation(s) for ticker.
  name: Bitrue Ticker API
  slug: bitrue-ticker-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The User Stream API from Bitrue — 2 operation(s) for user stream.
  name: Bitrue User Stream API
  slug: bitrue-user-stream-api
- baseURL: https://openapi.bitrue.com
  baseurl_source: declared
  description: The Withdraw API from Bitrue — 1 operation(s) for withdraw.
  name: Bitrue Withdraw API
  slug: bitrue-withdraw-api
artifact_total: 25
common:
- group: operate
  href: https://artifacts.apis.io/bitrue/rate-limits/bitrue-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bitrue-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bitrue/rules/bitrue-rules.yml
  title: ''
  type: Spectral
  url: rules/bitrue-rules.yml
- group: design
  href: https://artifacts.apis.io/bitrue/json-ld/bitrue-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bitrue-context.jsonld
- group: design
  href: https://artifacts.apis.io/bitrue/vocabulary/bitrue-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bitrue-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bitrue/data-model/bitrue-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bitrue-data-model.yml
- group: design
  href: https://artifacts.apis.io/bitrue/errors/bitrue-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/bitrue-error-codes.yml
- group: design
  href: https://artifacts.apis.io/bitrue/conformance/bitrue-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitrue-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bitrue/llms/bitrue-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitrue-llms.txt
- group: agent
  href: https://artifacts.apis.io/bitrue/well-known/bitrue-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitrue-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitrue/hosts/bitrue-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitrue-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitrue/vendors/bitrue-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitrue-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bitrue/security/bitrue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitrue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitrue.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bitrue.com/bitrue-api
- group: docs
  title: ''
  type: Documentation
  url: https://www.bitrue.com/api-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bitrue-exchange
- group: company
  title: ''
  type: Blog
  url: https://www.bitrue.com/blog
- group: start
  title: ''
  type: Login
  url: https://www.bitrue.com/user/login
- group: start
  title: ''
  type: SignUp
  url: https://www.bitrue.com/user/register
- group: operate
  title: ''
  type: Support
  url: https://support.bitrue.com/hc/en-001
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.bitrue.com/hc/en-001/articles/4405473185945
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.bitrue.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Bitrue is a centralized cryptocurrency exchange offering spot trading, USDT-margined and coin-margined perpetual futures, copy trading and a crypto wallet. It publishes public REST and WebSocket APIs for market data, account and order management, deposits and withdrawals, with HMAC-SHA256 signed requests, documented at www.bitrue.com/api-docs and in the Bitrue-exchange GitHub organization.
image: https://static.bitrue.com/img/website/uniframe/logo-20221119.png
json_schemas:
- name: GetApiV1EtfNetValueSymbolResponse
  property_count: 9
  slug: bitrue-get-api-v1-etf-net-value-symbol-response
- name: GetApiV1TickerTickeridResponse
  property_count: 19
  slug: bitrue-get-api-v1-ticker-tickerid-response
- name: GetApiV1V1IdResponse
  property_count: 9
  slug: bitrue-get-api-v1-v1-id-response
- name: GetApiV2MytradesResponse
  property_count: 12
  slug: bitrue-get-api-v2-mytrades-response
- name: PostFapiV1OrderRequest
  property_count: 5
  slug: bitrue-post-fapi-v1-order-request
- name: PostSapiV1OrderRequest
  property_count: 5
  slug: bitrue-post-sapi-v1-order-request
jsonld:
- class_count: 17
  name: Bitrue Context
  property_count: 62
  slug: bitrue-context
layout: provider
modified: '2026-10-13'
name: Bitrue
nav: Providers
network: true
overview: 'Bitrue is listed with 15 APIs on the [APIs.io](https://apis.io/) network, including Bitrue API, Etf API, Fapi API, and 12 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Futures.


  The Bitrue catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bitrue''s developer surface includes documentation, engineering blog, signup flow, support, and 17 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 2
  name: Bitrue Rate Limits
  slug: bitrue-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Bitrue API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: bitrue-rules
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 73.0
    catalog_earned_first_party: 8.0
    catalog_gap: 42.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 11.8
    contract_governance: 19.7
    contract_quality: 25.6
    developer_ergonomics: 13.1
    discoverability: 78.6
    operational_transparency: 23.7
  previous_composite: 28.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 12.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bitrue/bitrue-2026-11-03T121814.png
security:
- kind: domain-security
  name: Bitrue Domain Security
  slug: bitrue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitrue
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Futures
- Market Data
- WebSocket
website: https://www.bitrue.com
---
