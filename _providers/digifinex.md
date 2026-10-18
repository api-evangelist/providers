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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.6
  scored_at: '2026-10-17'
api_count: 6
apis:
- baseURL: https://openapi.digifinex.com/v3
  baseurl_source: declared
  description: The Account API from DigiFinex — 16 operation(s) for account.
  name: DigiFinex Account API
  slug: digifinex-account-api
- baseURL: https://openapi.digifinex.com/v3
  baseurl_source: declared
  description: The Copy Trading API from DigiFinex — 11 operation(s) for copy trading.
  name: DigiFinex Copy Trading API
  slug: digifinex-copy-trading-api
- baseURL: https://openapi.digifinex.com/v3
  baseurl_source: declared
  description: The Margin API from DigiFinex — 5 operation(s) for margin.
  name: DigiFinex Margin API
  slug: digifinex-margin-api
- baseURL: https://openapi.digifinex.com/v3
  baseurl_source: declared
  description: The Market Data API from DigiFinex — 21 operation(s) for market data.
  name: DigiFinex Market Data API
  slug: digifinex-market-data-api
- baseURL: https://openapi.digifinex.com/v3
  baseurl_source: declared
  description: The Orders API from DigiFinex — 9 operation(s) for orders.
  name: DigiFinex Orders API
  slug: digifinex-orders-api
- baseURL: https://openapi.digifinex.com/v3
  baseurl_source: declared
  description: The Trading API from DigiFinex — 8 operation(s) for trading.
  name: DigiFinex Trading API
  slug: digifinex-trading-api
artifact_total: 10
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/rate-limits/digifinex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digifinex-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/rules/digifinex-rules.yml
  title: ''
  type: Spectral
  url: rules/digifinex-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/vocabulary/digifinex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/digifinex-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/conventions/digifinex-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digifinex-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/authentication/digifinex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digifinex-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/errors/digifinex-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/digifinex-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/conformance/digifinex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digifinex-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/hosts/digifinex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digifinex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/vendors/digifinex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digifinex-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/digifinex/refs/heads/main/security/digifinex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digifinex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digifinex.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digifinex.com/en-ww/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.digifinex.com/en-ww/spot/v3/rest.html
- group: operate
  title: ''
  type: Support
  url: https://support.digifinex.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://www.digifinex.com/en-ww/n/login
- group: start
  title: ''
  type: SignUp
  url: https://www.digifinex.com/en-ww/n/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DigiFinex
- group: company
  title: ''
  type: About
  url: https://www.digifinex.com/en-ww/about
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digifinex.com/en-ww/spot/v1/websocket.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digifinex.com/en-ww/swap/v2/websocket.html
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.digifinex.com/mcp
  - status: 401
    url: https://support.digifinex.com/mcp
  - status: 200
    url: https://www.digifinex.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'DigiFinex is a centralized cryptocurrency exchange offering spot, margin and perpetual swap (USDT-margined) trading, OTC, copy trading and a crypto card. It publishes a public developer API: a signed REST API for spot and margin (openapi.digifinex.com/v3), a REST API for perpetual swaps (openapi.digifinex.com/swap/v2), and WebSocket market and account streams, documented at docs.digifinex.com. Private endpoints are signed with ACCESS-KEY, ACCESS-SIGN (HMAC-SHA256) and ACCESS-TIMESTAMP headers.'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-10-13'
name: DigiFinex
nav: Providers
network: true
overview: 'DigiFinex is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Copy Trading API, Margin API, and 3 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Derivatives.


  The DigiFinex catalog on APIs.io includes 1 Spectral governance ruleset.


  DigiFinex''s developer surface includes authentication, documentation, API reference, support, signup flow, and 15 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 4
  name: Digifinex Rate Limits
  slug: digifinex-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: DigiFinex API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: digifinex-rules
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 11.8
    developer_ergonomics: 33.3
    discoverability: 71.4
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Digifinex Authentication
  slug: digifinex-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Digifinex Domain Security
  slug: digifinex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: digifinex
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Derivatives
- WebSocket
website: https://www.digifinex.com
---
