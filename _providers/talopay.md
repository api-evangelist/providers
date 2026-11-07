---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://sandbox-api.talo.com.ar
  baseurl_source: declared
  description: 'Talo Pay API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Talo Pay API
  slug: talopay-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/talopay/rules/talopay-rules.yml
  title: ''
  type: Spectral
  url: rules/talopay-rules.yml
- group: design
  href: https://artifacts.apis.io/talopay/json-ld/talopay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/talopay-context.jsonld
- group: design
  href: https://artifacts.apis.io/talopay/vocabulary/talopay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/talopay-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/talopay/data-model/talopay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/talopay-data-model.yml
- group: start
  href: https://artifacts.apis.io/talopay/sandbox/talopay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/talopay-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/talopay/authentication/talopay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/talopay-authentication.yml
- group: design
  href: https://artifacts.apis.io/talopay/conformance/talopay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/talopay-conformance.yml
- group: agent
  href: https://artifacts.apis.io/talopay/llms/talopay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/talopay-llms.txt
- group: agent
  href: https://artifacts.apis.io/talopay/well-known/talopay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/talopay-well-known.yml
- group: other
  href: https://artifacts.apis.io/talopay/hosts/talopay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/talopay-hosts.yml
- group: other
  href: https://artifacts.apis.io/talopay/vendors/talopay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/talopay-vendors.yml
- group: build
  href: https://artifacts.apis.io/talopay/packages/talopay-packages.yml
  title: ''
  type: SDKs
  url: packages/talopay-packages.yml
- group: build
  href: https://artifacts.apis.io/talopay/packages/talopay-packages.yml
  title: ''
  type: Packages
  url: packages/talopay-packages.yml
- group: start
  title: ''
  type: Login
  url: https://talopay.com/login
- group: auth
  href: https://artifacts.apis.io/talopay/security/talopay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/talopay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://talopay.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.talo.com.ar
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.talo.com.ar/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://talopay.com/ar/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://talopay.com/ar/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://talopay.com/ar/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.com.ar/api/mcp
  - status: 401
    url: https://talopay.com/mcp
  - status: 200
    url: https://talopay.com
  reason: partner-login
  state: gated
created: '2026-10-27'
description: Talo Pay is an Argentine fintech company offering automated bank transfer payment solutions for online merchants. It enables merchants to add bank transfer as a payment method, providing low‑cost commissions, instant payment confirmation, and tools to manage employee permissions. The platform includes a dashboard, API integrations, and support for partners, aiming to improve liquidity and reduce chargeback risk for e‑commerce businesses in Argentina.
image: https://talopay.com/landing.jpeg
json_schemas:
- name: GetCustomersResponse
  property_count: 1
  slug: talopay-get-customers-response
- name: GetCustomersResponse2
  property_count: 9
  slug: talopay-get-customers-response2
- name: GetPaymentsResponse
  property_count: 1
  slug: talopay-get-payments-response
- name: GetSplitPaymentsSplitpaymentidResponse
  property_count: 10
  slug: talopay-get-split-payments-splitpaymentid-response
- name: PostCustomersResponse
  property_count: 1
  slug: talopay-post-customers-response
- name: PostUsersUseridStoresResponse
  property_count: 11
  slug: talopay-post-users-userid-stores-response
jsonld:
- class_count: 35
  name: Talopay Context
  property_count: 55
  slug: talopay-context
layout: provider
modified: '2026-10-27'
name: Talo Pay
nav: Providers
network: true
overview: 'Talo Pay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Argentina, E-Commerce, and Bank Transfers.


  The Talo Pay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Talo Pay''s developer surface includes sandbox, authentication, documentation, getting-started guide, pricing, and 16 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Talo Pay API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: talopay-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 36.9
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - argentina
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/talopay/talopay-2026-11-03T144312.png
security:
- kind: authentication
  name: Talopay Authentication
  slug: talopay-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Talopay Domain Security
  slug: talopay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: talopay
tags:
- Fintech
- Payments
- Argentina
- E-Commerce
- Bank Transfers
website: https://talopay.com
---
