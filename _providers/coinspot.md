---
agent_readiness:
  band: agent-aware
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://www.coinspot.com.au/api/v2
  baseurl_source: declared
  description: The Public API API from CoinSpot — 13 operation(s) for public api.
  name: CoinSpot Public API
  slug: coinspot-public-api-api
- baseURL: https://www.coinspot.com.au/api/v2
  baseurl_source: declared
  description: The Read Only API API from CoinSpot — 14 operation(s) for read only api.
  name: CoinSpot Read Only API
  slug: coinspot-read-only-api-api
- baseURL: https://www.coinspot.com.au/api/v2
  baseurl_source: declared
  description: The Trading API API from CoinSpot — 22 operation(s) for trading api.
  name: CoinSpot Trading API
  slug: coinspot-trading-api-api
artifact_total: 9
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/rate-limits/coinspot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coinspot-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/plans/coinspot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coinspot-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/rules/coinspot-rules.yml
  title: ''
  type: Spectral
  url: rules/coinspot-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/vocabulary/coinspot-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coinspot-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/conventions/coinspot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coinspot-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/authentication/coinspot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coinspot-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/lifecycle/coinspot-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/coinspot-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/lifecycle/coinspot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coinspot-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/errors/coinspot-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinspot-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/errors/coinspot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinspot-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/conformance/coinspot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinspot-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/well-known/coinspot-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinspot-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/well-known/coinspot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinspot-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/hosts/coinspot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinspot-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/vendors/coinspot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinspot-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/packages/coinspot-packages.yml
  title: ''
  type: SDKs
  url: packages/coinspot-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/packages/coinspot-packages.yml
  title: ''
  type: Packages
  url: packages/coinspot-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/security/coinspot-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinspot-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinspot/refs/heads/main/security/coinspot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinspot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coinspot.com.au
- group: docs
  title: ''
  type: Documentation
  url: https://www.coinspot.com.au/v2/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.coinspot.com.au/v2/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coinspot.com.au/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coinspot.com.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinspot.com.au/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.coinspot.com.au/contact
- group: company
  title: ''
  type: Blog
  url: https://www.coinspot.com.au/blog
- group: start
  title: ''
  type: Login
  url: https://www.coinspot.com.au/login
- group: start
  title: ''
  type: SignUp
  url: https://www.coinspot.com.au/Register
- group: company
  title: ''
  type: Newsroom
  url: https://www.coinspot.com.au/press
- group: auth
  title: ''
  type: Security
  url: https://www.coinspot.com.au/Security
created: '2026-10-13'
description: 'CoinSpot is an Australian cryptocurrency exchange (coinspot.com.au, member since 2014) offering buy/sell, swap, market and OTC trading across hundreds of coins. It publishes the CoinSpot API V2 (BETA): an unauthenticated Public API for latest prices and order books, a full-access trading API (quotes, market and instant orders, cancels, coin withdrawals) and a Read Only API for balances and history, all signed with HMAC-SHA512. The legacy V1 API remains active.'
image: https://www.coinspot.com.au/public/img/rocket-thumb.png
layout: provider
modified: '2026-10-13'
name: CoinSpot
nav: Providers
network: true
overview: 'CoinSpot is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Public API, Read Only API, and Trading API. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Australia.


  The CoinSpot catalog on APIs.io includes 1 Spectral governance ruleset.


  CoinSpot''s developer surface includes authentication, documentation, API reference, pricing, support, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Coinspot Plans Pricing
  plan_count: 5
  slug: coinspot-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Coinspot Rate Limits
  slug: coinspot-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: CoinSpot API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: coinspot-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.8
    catalog_earned_first_party: 20.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 13.3
    developer_ergonomics: 42.9
    discoverability: 73.2
    operational_transparency: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Coinspot Authentication
  slug: coinspot-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Coinspot Domain Security
  slug: coinspot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinspot Vulnerability Disclosure
  slug: coinspot-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: coinspot
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Australia
- Bitcoin
- Market Data
website: https://www.coinspot.com.au
---
