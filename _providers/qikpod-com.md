---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for QikPod locker control and data management as described in the partner API documentation.
  name: QikPod API
  slug: qikpod-api
- description: 'QikPod API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: QikPod API
  slug: qikpod-com-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/qikpod-com/rules/qikpod-com-rules.yml
  title: ''
  type: Spectral
  url: rules/qikpod-com-rules.yml
- group: design
  href: https://artifacts.apis.io/qikpod-com/json-ld/qikpod-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qikpod-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/qikpod-com/vocabulary/qikpod-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qikpod-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/qikpod-com/data-model/qikpod-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qikpod-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/qikpod-com/conformance/qikpod-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qikpod-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/qikpod-com/hosts/qikpod-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qikpod-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/qikpod-com/security/qikpod-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qikpod-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.qikpod.com
- group: docs
  title: ''
  type: Documentation
  url: https://leapmile-website.blr1.digitaloceanspaces.com/production/QikPodapp_flow.pdf
- group: operate
  title: ''
  type: Support
  url: https://leapmile.com/qikpod
- group: commercial
  title: ''
  type: Pricing
  url: https://leapmile.com/pricing-and-refunds
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leapmile.com/terms-and-privacy#terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leapmile.com/terms-and-privacy#privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI/GraphQL spec could be retrieved.
  evidence:
  - status: 200
    url: https://docs.leapmile.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: QikPod is a modular, low‑cost parcel locker system offered by Leapmile Robotics that enables contact‑less, self‑service parcel management for apartments, offices, retail and campuses. The solution combines IoT‑enabled smart lockers with a cloud platform that provides APIs for locker remote control, user data management, package tracking, reporting and analytics. QikPod’s hardware‑agnostic design allows easy deployment, scalability and integration with existing mobile apps, supporting 24/7 access, OTP‑based pickup, and customizable workflows for last‑mile delivery, click‑and‑collect, digital mailrooms and university parcel hubs.
image: https://leapmile-website.blr1.digitaloceanspaces.com/production/leapmile_thum.jpg
json_schemas:
- name: PostApiOrderRequest
  property_count: 3
  slug: qikpod-com-post-api-order-request
- name: PostNanostoreBinsWithRequest
  property_count: 3
  slug: qikpod-com-post-nanostore-bins-with-request
- name: PostNanostoreOrdersWithRequest
  property_count: 5
  slug: qikpod-com-post-nanostore-orders-with-request
- name: PostNanostoreProductCatalogWithRequest
  property_count: 6
  slug: qikpod-com-post-nanostore-product-catalog-with-request
- name: PostNanostoreProductsWithRequest
  property_count: 3
  slug: qikpod-com-post-nanostore-products-with-request
- name: PostNanostoreTraysWithRequest
  property_count: 5
  slug: qikpod-com-post-nanostore-trays-with-request
jsonld:
- class_count: 21
  name: Qikpod Com Context
  property_count: 23
  slug: qikpod-com-context
layout: provider
modified: '2026-10-28'
name: QikPod
nav: Providers
network: true
overview: 'QikPod is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Parcel, Automation, Robotics, and IoT.


  The QikPod catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  QikPod''s developer surface includes documentation, support, pricing, and 10 more developer resources.'
plans:
- name: Qikpod Com Plans Pricing
  plan_count: 0
  slug: qikpod-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Qikpod Com Rate Limits
  slug: qikpod-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: QikPod API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: qikpod-com-rules
scopes:
- name: Qikpod Com Scopes
  scope_count: 0
  slug: qikpod-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 15.8
    contract_governance: 19.7
    contract_quality: 23.5
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 24.4
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/qikpod-com/qikpod-com-2026-11-03T141755.png
security:
- kind: authentication
  name: Qikpod Com Authentication
  slug: qikpod-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Qikpod Com Domain Security
  slug: qikpod-com-domain-security
  summary_line: DMARC
slug: qikpod-com
tags:
- Logistics
- Parcel
- Automation
- Robotics
- IoT
website: http://www.qikpod.com
---
