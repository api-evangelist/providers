---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: true
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Full REST reference — authentication, endpoints, rate limits, overage billing, error codes, and HTTP client examples.
  name: IP Atlas API
  slug: ip-atlas-api
- baseURL: https://api.ip-atlas.io
  baseurl_source: declared
  description: 'ipatlas-dev API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: ipatlas-dev API
  slug: ipatlas-dev-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/ipatlas-dev/plans/ipatlas-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ipatlas-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ipatlas-dev/rules/ipatlas-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/ipatlas-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/ipatlas-dev/json-ld/ipatlas-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ipatlas-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/ipatlas-dev/vocabulary/ipatlas-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ipatlas-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ipatlas-dev/data-model/ipatlas-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ipatlas-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/ipatlas-dev/conventions/ipatlas-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ipatlas-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ipatlas-dev/authentication/ipatlas-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ipatlas-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ipatlas-dev/scopes/ipatlas-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ipatlas-dev-scopes.yml
- group: design
  href: https://artifacts.apis.io/ipatlas-dev/conformance/ipatlas-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ipatlas-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/ipatlas-dev/hosts/ipatlas-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ipatlas-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ipatlas-dev/vendors/ipatlas-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ipatlas-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ip-atlas.io/status
- group: start
  title: ''
  type: Login
  url: https://ip-atlas.io/login
- group: auth
  href: https://artifacts.apis.io/ipatlas-dev/security/ipatlas-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ipatlas-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ip-atlas.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ip-atlas.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://ip-atlas.io/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://ip-atlas.io/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://ip-atlas.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ip-atlas.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ip-atlas.io/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation provides only HTML examples and no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://ip-atlas.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Fast REST API and MMDB downloads for IP geolocation, ASN/org, VPN and datacenter detection. 2,000 free requests/month or 1 country-level MMDB download. Paid plans from $19/mo with monthly full MMDB included.
image: https://ip-atlas.io/logo.svg
json_schemas:
- name: GetJsonIpResponse
  property_count: 8
  slug: ipatlas-dev-get-json-ip-response
- name: GetJsonResponse
  property_count: 8
  slug: ipatlas-dev-get-json-response
- name: GetV1AccountResponse
  property_count: 2
  slug: ipatlas-dev-get-v1-account-response
- name: PostV1AccountRotateResponse
  property_count: 2
  slug: ipatlas-dev-post-v1-account-rotate-response
- name: PostV1AccountSettingsRequest
  property_count: 2
  slug: ipatlas-dev-post-v1-account-settings-request
- name: PostV1BatchResponse
  property_count: 1
  slug: ipatlas-dev-post-v1-batch-response
jsonld:
- class_count: 9
  name: Ipatlas Dev Context
  property_count: 18
  slug: ipatlas-dev-context
layout: provider
modified: '2026-10-30'
name: ipatlas-dev
nav: Providers
network: true
overview: 'ipatlas-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include IP, Geolocation, ASN, VPN, and Data.


  The ipatlas-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ipatlas-dev''s developer surface includes authentication, documentation, getting-started guide, support, pricing, and 16 more developer resources.'
plans:
- name: Ipatlas Dev Plans Pricing
  plan_count: 5
  slug: ipatlas-dev-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ipatlas-dev API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ipatlas-dev-rules
scopes:
- name: Ipatlas Dev Scopes
  scope_count: 3
  slug: ipatlas-dev-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 43.6
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ipatlas-dev/ipatlas-dev-2026-11-03T134021.png
security:
- kind: authentication
  name: Ipatlas Dev Authentication
  slug: ipatlas-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ipatlas Dev Domain Security
  slug: ipatlas-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ipatlas-dev
tags:
- IP
- Geolocation
- ASN
- VPN
- Data
website: https://ip-atlas.io/
---
