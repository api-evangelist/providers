---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.fxsocket.com
  baseurl_source: declared
  description: 'FxSocket API as documented publicly: 25 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: FxSocket API
  slug: fxsocket-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/fxsocket-com/plans/fxsocket-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fxsocket-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fxsocket-com/rules/fxsocket-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fxsocket-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fxsocket-com/json-ld/fxsocket-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fxsocket-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/fxsocket-com/vocabulary/fxsocket-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fxsocket-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fxsocket-com/data-model/fxsocket-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fxsocket-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/fxsocket-com/authentication/fxsocket-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fxsocket-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/fxsocket-com/conformance/fxsocket-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fxsocket-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fxsocket-com/llms/fxsocket-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fxsocket-com-llms.txt
- group: other
  href: https://artifacts.apis.io/fxsocket-com/hosts/fxsocket-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fxsocket-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fxsocket-com/vendors/fxsocket-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fxsocket-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/fxsocket-com/packages/fxsocket-com-packages.yml
  title: ''
  type: Packages
  url: packages/fxsocket-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fxsocket.com
- group: build
  title: ''
  type: SDKs
  url: https://fxsocket.com/sdks
- group: start
  title: ''
  type: Login
  url: https://app.fxsocket.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://fxsocket.com/docs/mcp
- group: auth
  href: https://artifacts.apis.io/fxsocket-com/security/fxsocket-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fxsocket-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fxsocket.com
- group: docs
  title: ''
  type: Documentation
  url: https://fxsocket.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://fxsocket.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://fxsocket.com/blog
- group: operate
  title: ''
  type: Support
  url: https://fxsocket.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fxsocket.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fxsocket.com/privacy
created: '2026-10-29'
description: FxSocket provides cloud‑hosted MetaTrader (MT4/MT5) REST and WebSocket APIs enabling developers to programmatically trade forex, CFDs and other assets without managing local terminals. The platform offers trade execution, account management, and market data via simple HTTP endpoints and real‑time sockets, supporting multiple languages and SDKs. It targets prop firms, algo traders, and developers seeking automated trading infrastructure.
image: https://fxsocket.com/opengraph-image?ebabf6aae38a5262
json_schemas:
- name: GetV1SubscriptionResponse
  property_count: 10
  slug: fxsocket-com-get-v1-subscription-response
- name: GetV1WalletTopupIdResponse
  property_count: 10
  slug: fxsocket-com-get-v1-wallet-topup-id-response
- name: PostV1OrdersCloseRequest
  property_count: 10
  slug: fxsocket-com-post-v1-orders-close-request
- name: PostV1OrdersRequest
  property_count: 14
  slug: fxsocket-com-post-v1-orders-request
- name: PostV1WalletTopupRequest
  property_count: 4
  slug: fxsocket-com-post-v1-wallet-topup-request
- name: PostV1WalletTopupResponse
  property_count: 10
  slug: fxsocket-com-post-v1-wallet-topup-response
jsonld:
- class_count: 10
  name: Fxsocket Com Context
  property_count: 39
  slug: fxsocket-com-context
layout: provider
modified: '2026-10-29'
name: FxSocket
nav: Providers
network: true
overview: 'FxSocket is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Trading, and Cloud.


  The FxSocket catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FxSocket''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, support, and 17 more developer resources.'
plans:
- name: Fxsocket Com Plans Pricing
  plan_count: 3
  slug: fxsocket-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: FxSocket API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: fxsocket-com-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 26.0
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 45.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fxsocket-com/fxsocket-com-2026-11-03T132425.png
security:
- kind: authentication
  name: Fxsocket Com Authentication
  slug: fxsocket-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fxsocket Com Domain Security
  slug: fxsocket-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fxsocket-com
tags:
- Company
- Fintech
- Trading
- Cloud
website: https://fxsocket.com
---
