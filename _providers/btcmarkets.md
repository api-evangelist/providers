---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Btcmarkets Agentic Access
  operation_count: 35
  slug: btcmarkets-agentic-access
  summary_line: 35 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.btcmarkets.net
  baseurl_source: declared
  description: The Account APIs API from BTC Markets — 4 operation(s) for account apis.
  name: BTC Markets Account APIs API
  slug: btcmarkets-account-apis-api
- baseURL: https://api.btcmarkets.net
  baseurl_source: declared
  description: The Batch Order APIs API from BTC Markets — 2 operation(s) for batch order apis.
  name: BTC Markets Batch Order APIs API
  slug: btcmarkets-batch-order-apis-api
- baseURL: https://api.btcmarkets.net
  baseurl_source: declared
  description: The Fund Management APIs API from BTC Markets — 9 operation(s) for fund management apis.
  name: BTC Markets Fund Management APIs API
  slug: btcmarkets-fund-management-apis-api
- baseURL: https://api.btcmarkets.net
  baseurl_source: declared
  description: The Market Data APIs API from BTC Markets — 7 operation(s) for market data apis.
  name: BTC Markets Market Data APIs API
  slug: btcmarkets-market-data-apis-api
- baseURL: https://api.btcmarkets.net
  baseurl_source: declared
  description: The Misc APIs API from BTC Markets — 1 operation(s) for misc apis.
  name: BTC Markets Misc APIs API
  slug: btcmarkets-misc-apis-api
- baseURL: https://api.btcmarkets.net
  baseurl_source: declared
  description: The Order Placement APIs API from BTC Markets — 2 operation(s) for order placement apis.
  name: BTC Markets Order Placement APIs API
  slug: btcmarkets-order-placement-apis-api
- baseURL: https://api.btcmarkets.net
  baseurl_source: declared
  description: The Report APIs API from BTC Markets — 2 operation(s) for report apis.
  name: BTC Markets Report APIs API
  slug: btcmarkets-report-apis-api
- baseURL: https://api.btcmarkets.net
  baseurl_source: declared
  description: The Trade APIs API from BTC Markets — 2 operation(s) for trade apis.
  name: BTC Markets Trade APIs API
  slug: btcmarkets-trade-apis-api
artifact_total: 21
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/rate-limits/btcmarkets-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/btcmarkets-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/agentic-access/btcmarkets-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/btcmarkets-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/rules/btcmarkets-rules.yml
  title: ''
  type: Spectral
  url: rules/btcmarkets-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/json-ld/btcmarkets-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/btcmarkets-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/vocabulary/btcmarkets-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/btcmarkets-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/data-model/btcmarkets-data-model.yml
  title: ''
  type: DataModel
  url: data-model/btcmarkets-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.btcmarkets.net/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/errors/btcmarkets-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/btcmarkets-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/conformance/btcmarkets-conformance.yml
  title: ''
  type: Conformance
  url: conformance/btcmarkets-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/well-known/btcmarkets-v3-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/btcmarkets-v3-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/well-known/btcmarkets-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/btcmarkets-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/well-known/btcmarkets-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/btcmarkets-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/well-known/btcmarkets-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/btcmarkets-docs-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/well-known/btcmarkets-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/btcmarkets-app-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/well-known/btcmarkets-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/btcmarkets-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/well-known/btcmarkets-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/btcmarkets-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/hosts/btcmarkets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/btcmarkets-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/vendors/btcmarkets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/btcmarkets-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/packages/btcmarkets-packages.yml
  title: ''
  type: SDKs
  url: packages/btcmarkets-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/packages/btcmarkets-packages.yml
  title: ''
  type: Packages
  url: packages/btcmarkets-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.btcmarkets.net/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.btcmarkets.net/blog/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.btcmarkets.net/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.btcmarkets.net/prices
- group: start
  title: ''
  type: Login
  url: https://app.btcmarkets.net/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BTCMarkets
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/security/btcmarkets-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/btcmarkets-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/security/btcmarkets-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/btcmarkets-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/btcmarkets/refs/heads/main/security/btcmarkets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/btcmarkets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.btcmarkets.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.btcmarkets.net/
- group: company
  title: ''
  type: Blog
  url: https://www.btcmarkets.net/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.btcmarkets.net/
- group: operate
  title: ''
  type: Support
  url: https://support.btcmarkets.net/
created: '2026-10-13'
description: BTC Markets is an Australian cryptocurrency exchange. Its public v3 REST API at api.btcmarkets.net covers market data (markets, tickers, order books, trades, candles), trading (orders, batch orders, trades), funding (deposits, withdrawals, transfers, addresses) and account data (balances, fees, transactions, reports), with a WebSocket feed at wss://socket.btcmarkets.net/v2 and a FIX API.
image: https://assets.btcmarkets.net/images/marketing/og-images/og-default.jpg
json_schemas:
- name: CancelOrderResponse
  property_count: 2
  slug: btcmarkets-cancel-order-response
- name: CreateReportRequest
  property_count: 2
  slug: btcmarkets-create-report-request
- name: CreateWithdrawRequest
  property_count: 10
  slug: btcmarkets-create-withdraw-request
- name: Order
  property_count: 16
  slug: btcmarkets-order
- name: PlaceOrderRequest
  property_count: 11
  slug: btcmarkets-place-order-request
- name: ReplaceOrderRequest
  property_count: 3
  slug: btcmarkets-replace-order-request
jsonld:
- class_count: 13
  name: Btcmarkets Context
  property_count: 31
  slug: btcmarkets-context
layout: provider
modified: '2026-10-13'
name: BTC Markets
nav: Providers
network: true
overview: 'BTC Markets publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account APIs API, Batch Order APIs API, Fund Management APIs API, and 5 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Market Data.


  The BTC Markets catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BTC Markets'' developer surface includes pricing, documentation, engineering blog, support, and 30 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 8
  name: Btcmarkets Rate Limits
  slug: btcmarkets-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: BTC Markets API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: btcmarkets-rules
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 59.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 88.9
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 27.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Btcmarkets Domain Security
  slug: btcmarkets-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Btcmarkets Vulnerability Disclosure
  slug: btcmarkets-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Btcmarkets Trust Center
  slug: btcmarkets-trust-center
  summary_line: ISO 27001
slug: btcmarkets
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Market Data
- Australia
website: https://www.btcmarkets.net
---
