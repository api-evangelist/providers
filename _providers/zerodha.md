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
    error_semantics: false
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 7
apis:
- baseURL: https://api.kite.trade
  baseurl_source: declared
  description: The Alerts API from Zerodha — 3 operation(s) for alerts.
  name: Zerodha Alerts API
  slug: zerodha-alerts-api
- baseURL: https://api.kite.trade
  baseurl_source: declared
  description: The Gtt API from Zerodha — 1 operation(s) for gtt.
  name: Zerodha Gtt API
  slug: zerodha-gtt-api
- baseURL: https://api.kite.trade
  baseurl_source: declared
  description: The Orders API from Zerodha — 3 operation(s) for orders.
  name: Zerodha Orders API
  slug: zerodha-orders-api
- baseURL: https://api.kite.trade
  baseurl_source: declared
  description: The Portfolio API from Zerodha — 4 operation(s) for portfolio.
  name: Zerodha Portfolio API
  slug: zerodha-portfolio-api
- baseURL: https://api.kite.trade
  baseurl_source: declared
  description: The Session API from Zerodha — 1 operation(s) for session.
  name: Zerodha Session API
  slug: zerodha-session-api
- baseURL: https://api.kite.trade
  baseurl_source: declared
  description: The Trades API from Zerodha — 1 operation(s) for trades.
  name: Zerodha Trades API
  slug: zerodha-trades-api
- baseURL: https://api.kite.trade
  baseurl_source: declared
  description: The User API from Zerodha — 2 operation(s) for user.
  name: Zerodha User API
  slug: zerodha-user-api
artifact_total: 16
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/rules/zerodha-rules.yml
  title: ''
  type: Spectral
  url: rules/zerodha-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/json-ld/zerodha-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zerodha-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/vocabulary/zerodha-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zerodha-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/data-model/zerodha-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zerodha-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/conventions/zerodha-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/zerodha-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/conventions/zerodha-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zerodha-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/conformance/zerodha-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zerodha-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/hosts/zerodha-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zerodha-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/vendors/zerodha-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zerodha-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/packages/zerodha-packages.yml
  title: ''
  type: SDKs
  url: packages/zerodha-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/packages/zerodha-packages.yml
  title: ''
  type: Packages
  url: packages/zerodha-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zerodha.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zerodha.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://zerodha.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://zerodha.com/media
- group: operate
  title: ''
  type: ChangeLog
  url: https://kite.trade/docs/connect/v3/changelog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zerodha/refs/heads/main/security/zerodha-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zerodha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kite.trade
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kite.trade
- group: docs
  title: ''
  type: Documentation
  url: https://kite.trade/docs/connect/v3/
- group: docs
  title: ''
  type: APIReference
  url: https://kite.trade/docs/connect/v3/
- group: start
  title: ''
  type: GettingStarted
  url: https://kite.trade/docs/connect/v3/agent-setup/
- group: operate
  title: ''
  type: Support
  url: https://support.zerodha.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zerodha
- group: start
  title: ''
  type: SignUp
  url: https://developers.kite.trade/signup
created: '2026-10-13'
description: Zerodha is India’s leading retail stock‑broking platform offering a suite of developer‑focused APIs called Kite Connect. The APIs provide REST endpoints and WebSocket streams for order execution, portfolio management, market data, mutual funds, margins, and more. Built for traders, platforms and fintechs, they enable automation of trading strategies and integration with third‑party services, backed by extensive SDKs and documentation.
image: https://zerodha.com/static/images/kite-trade/kite-connect-og.png
json_schemas:
- name: GetUserMarginsSegmentResponse
  property_count: 21
  slug: zerodha-get-user-margins-segment-response
- name: PostAlertsRequest
  property_count: 9
  slug: zerodha-post-alerts-request
- name: PostOrdersVarietyRequest
  property_count: 17
  slug: zerodha-post-orders-variety-request
- name: PostSessionTokenResponse
  property_count: 19
  slug: zerodha-post-session-token-response
- name: PutAlertsUuidRequest
  property_count: 8
  slug: zerodha-put-alerts-uuid-request
- name: PutOrdersVarietyOrderidRequest
  property_count: 9
  slug: zerodha-put-orders-variety-orderid-request
jsonld:
- class_count: 15
  name: Zerodha Context
  property_count: 67
  slug: zerodha-context
layout: provider
modified: '2026-10-13'
name: Zerodha
nav: Providers
network: true
overview: 'Zerodha is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Gtt API, Orders API, and 4 more. Tagged areas include Company, Finance, Trading, and Fintech.


  The Zerodha catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zerodha''s developer surface includes pricing, changelog, documentation, API reference, getting-started guide, support, signup flow, and 18 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Zerodha API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: zerodha-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 19.7
    contract_quality: 28.2
    developer_ergonomics: 50.0
    discoverability: 64.3
    operational_transparency: 21.1
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
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 17.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Zerodha Domain Security
  slug: zerodha-domain-security
  summary_line: TLSv1.3
slug: zerodha
tags:
- Company
- Finance
- Trading
- Fintech
website: https://kite.trade
---
