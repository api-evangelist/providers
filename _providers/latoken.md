---
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
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 34
  human_in_the_loop: 18
  name: Latoken Agentic Access
  operation_count: 80
  slug: latoken-agentic-access
  summary_line: 80 operations · 34 acting · 18 human-in-the-loop
api_count: 5
apis:
- description: STOMP-over-WebSocket API at wss://api.latoken.com/stomp with public market-data and private account topics. Documented in prose only; the provider's Swagger file for it carries no paths, and no AsyncA
  name: LATOKEN Public WebSocket API
  slug: latoken-websocket-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Account API from LATOKEN — 3 operation(s) for account.
  name: LATOKEN Account API
  slug: latoken-account-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The AppealController API from LATOKEN — 2 operation(s) for appealcontroller.
  name: LATOKEN Appeal Controller API
  slug: latoken-appealcontroller-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The BulkOrder API from LATOKEN — 2 operation(s) for bulkorder.
  name: LATOKEN Bulk Order API
  slug: latoken-bulkorder-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Chart API from LATOKEN — 2 operation(s) for chart.
  name: LATOKEN Chart API
  slug: latoken-chart-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The ChatController API from LATOKEN — 1 operation(s) for chatcontroller.
  name: LATOKEN Chat Controller API
  slug: latoken-chatcontroller-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Currency API from LATOKEN — 4 operation(s) for currency.
  name: LATOKEN Currency API
  slug: latoken-currency-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The OfferController API from LATOKEN — 7 operation(s) for offercontroller.
  name: LATOKEN Offer Controller API
  slug: latoken-offercontroller-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Order API from LATOKEN — 9 operation(s) for order.
  name: LATOKEN Order API
  slug: latoken-order-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The OrderController API from LATOKEN — 7 operation(s) for ordercontroller.
  name: LATOKEN Order Controller API
  slug: latoken-ordercontroller-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Pair API from LATOKEN — 2 operation(s) for pair.
  name: LATOKEN Pair API
  slug: latoken-pair-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The PaymentMethodController API from LATOKEN — 4 operation(s) for paymentmethodcontroller.
  name: LATOKEN Payment Method Controller API
  slug: latoken-paymentmethodcontroller-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Spot API from LATOKEN — 2 operation(s) for spot.
  name: LATOKEN Spot API
  slug: latoken-spot-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The StopOrder API from LATOKEN — 8 operation(s) for stoporder.
  name: LATOKEN Stop Order API
  slug: latoken-stoporder-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Ticker API from LATOKEN — 2 operation(s) for ticker.
  name: LATOKEN Ticker API
  slug: latoken-ticker-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Time API from LATOKEN — 1 operation(s) for time.
  name: LATOKEN Time API
  slug: latoken-time-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Trade API from LATOKEN — 6 operation(s) for trade.
  name: LATOKEN Trade API
  slug: latoken-trade-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Transaction API from LATOKEN — 10 operation(s) for transaction.
  name: LATOKEN Transaction API
  slug: latoken-transaction-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The Transfer API from LATOKEN — 4 operation(s) for transfer.
  name: LATOKEN Transfer API
  slug: latoken-transfer-api
- baseURL: https://api.latoken.com/v2
  baseurl_source: declared
  description: The UserController API from LATOKEN — 2 operation(s) for usercontroller.
  name: LATOKEN User Controller API
  slug: latoken-usercontroller-api
- baseURL: wss://api.latoken.com/stomp
  baseurl_source: declared
  description: The Orderbook API from LATOKEN — 1 operation(s) for orderbook.
  name: LATOKEN Orderbook API
  slug: latoken-orderbook-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: Security
  url: https://hackenproof.com/latoken/latoken-exchange
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/security/latoken-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/latoken-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/agentic-access/latoken-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/latoken-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/rules/latoken-rules.yml
  title: ''
  type: Spectral
  url: rules/latoken-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/vocabulary/latoken-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/latoken-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/data-model/latoken-data-model.yml
  title: ''
  type: DataModel
  url: data-model/latoken-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/errors/latoken-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/latoken-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/errors/latoken-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/latoken-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/conformance/latoken-conformance.yml
  title: ''
  type: Conformance
  url: conformance/latoken-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/hosts/latoken-hosts.yml
  title: ''
  type: Hosts
  url: hosts/latoken-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/vendors/latoken-vendors.yml
  title: ''
  type: Vendors
  url: vendors/latoken-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/packages/latoken-packages.yml
  title: ''
  type: SDKs
  url: packages/latoken-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/packages/latoken-packages.yml
  title: ''
  type: Packages
  url: packages/latoken-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/authentication/latoken-authentication.yml
  title: ''
  type: Authentication
  url: authentication/latoken-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/latoken/refs/heads/main/security/latoken-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/latoken-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://latoken.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.latoken.com/doc/v2/
- group: docs
  title: ''
  type: APIReference
  url: https://api.latoken.com/doc/v2/
- group: company
  title: ''
  type: Blog
  url: https://latoken.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://latoken.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://latoken.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LATOKEN
- group: commercial
  title: ''
  type: Pricing
  url: https://latoken.com/fees
created: '2026-10-13'
description: LATOKEN is a centralized cryptocurrency exchange (latoken.com) offering spot trading, a P2P marketplace and token listings. It publishes a public REST API v2 (market data, accounts, orders, stop and bulk orders, transfers, transactions and withdrawals signed with HMAC headers), a P2P API v1 and a STOMP WebSocket API, each documented with Redoc from a Swagger 2.0 contract at api.latoken.com/doc/, plus first-party Python, C# and Java clients.
image: https://latoken.com/images/latoken_sign_link@1191x669.png
layout: provider
modified: '2026-10-13'
name: LATOKEN
nav: Providers
network: true
overview: 'LATOKEN publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Appeal Controller API, Bulk Order API, and 18 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Market Data.


  The LATOKEN catalog on APIs.io includes 1 Spectral governance ruleset.


  LATOKEN''s developer surface includes authentication, documentation, API reference, engineering blog, support, pricing, and 17 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: LATOKEN API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: latoken-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 42.7
    developer_ergonomics: 42.9
    discoverability: 71.4
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Latoken Authentication
  slug: latoken-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Latoken Domain Security
  slug: latoken-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Latoken Vulnerability Disclosure
  slug: latoken-vulnerability-disclosure
  summary_line: disclosure policy published
slug: latoken
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Market Data
- P2P
- WebSocket
website: https://latoken.com
---
