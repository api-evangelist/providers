---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Deally API as documented publicly: 35 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Deally API
  slug: deal-ly-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/deal-ly/plans/deal-ly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deal-ly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deal-ly/rules/deal-ly-rules.yml
  title: ''
  type: Spectral
  url: rules/deal-ly-rules.yml
- group: design
  href: https://artifacts.apis.io/deal-ly/json-ld/deal-ly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deal-ly-context.jsonld
- group: design
  href: https://artifacts.apis.io/deal-ly/vocabulary/deal-ly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deal-ly-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deal-ly/data-model/deal-ly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deal-ly-data-model.yml
- group: design
  href: https://artifacts.apis.io/deal-ly/conformance/deal-ly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deal-ly-conformance.yml
- group: other
  href: https://artifacts.apis.io/deal-ly/hosts/deal-ly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deal-ly-hosts.yml
- group: other
  href: https://artifacts.apis.io/deal-ly/vendors/deal-ly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deal-ly-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alert.to/page/terms
- group: operate
  title: ''
  type: Support
  url: https://alert.to/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alert.to/en/page/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://alert.to/pricing
- group: start
  title: ''
  type: Login
  url: https://alert.to/user/login
- group: start
  title: ''
  type: GettingStarted
  url: https://alert.to/help/topic/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://alert.to/en/blog/category/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://alert.to/developers
- group: company
  title: ''
  type: Blog
  url: https://alert.to/blog
- group: auth
  href: https://artifacts.apis.io/deal-ly/security/deal-ly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deal-ly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deal.ly/
coverage:
  checked: '2026-11-05'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://alert.to/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Deal Engine is the top‑tier product of Alert.to, providing an ecommerce, affiliate and tracking engine built on the Alert.to platform. It offers smart routing, stealth redirect controls, offer rotation and server‑to‑server conversion tracking for performance marketers. The service includes features such as geo/device/time routing, burn‑link redirects, optional cookie‑based attribution and real‑time EPC reporting, all for $99 per month.
json_schemas:
- name: GetApiAccountResponse
  property_count: 3
  slug: deal-ly-get-api-account-response
- name: GetApiUrlIdUpdateResponse
  property_count: 11
  slug: deal-ly-get-api-url-id-update-response
- name: PostApiAccountResponse
  property_count: 4
  slug: deal-ly-post-api-account-response
- name: PostApiQrAddRequest
  property_count: 6
  slug: deal-ly-post-api-qr-add-request
- name: PostApiQrAddResponse
  property_count: 6
  slug: deal-ly-post-api-qr-add-response
- name: PostApiUrlAddRequest
  property_count: 18
  slug: deal-ly-post-api-url-add-request
jsonld:
- class_count: 41
  name: Deal Ly Context
  property_count: 35
  slug: deal-ly-context
layout: provider
modified: '2026-11-05'
name: Deally
nav: Providers
network: true
overview: 'Deally is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Redirects, Affiliates, Tracking, Server-to-Server, and Geo‑routing.


  The Deally catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Deally''s developer surface includes support, pricing, getting-started guide, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Deal Ly Plans Pricing
  plan_count: 4
  slug: deal-ly-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Deally API Rules
  rule_count: 41
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 3
  slug: deal-ly-rules
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 38.1
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deal Ly Domain Security
  slug: deal-ly-domain-security
  summary_line: TLSv1.3
slug: deal-ly
tags:
- Redirects
- Affiliates
- Tracking
- Server-to-Server
- Geo‑routing
- Offer Rotation
website: https://deal.ly/
---
