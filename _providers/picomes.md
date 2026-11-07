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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 4
apis:
- baseURL: https://your-erp-system.com
  baseurl_source: spec
  description: API for Picomes MES platform, documented at the developer portal.
  name: Picomes API
  slug: picomes-api
- baseURL: https://your-erp-system.com
  baseurl_source: declared
  description: The Graph API from Picomes — 1 operation(s) for graph.
  name: Picomes Graph API
  slug: picomes-graph-api
- baseURL: https://your-erp-system.com
  baseurl_source: declared
  description: The Pico Webhooks API from Picomes — 1 operation(s) for pico webhooks.
  name: Picomes Pico Webhooks API
  slug: picomes-pico-webhooks-api
- baseURL: https://your-erp-system.com
  baseurl_source: declared
  description: The Uploads API from Picomes — 2 operation(s) for uploads.
  name: Picomes Uploads API
  slug: picomes-uploads-api
artifact_total: 17
common:
- group: commercial
  href: https://artifacts.apis.io/picomes/plans/picomes-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/picomes-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/picomes/rules/picomes-rules.yml
  title: ''
  type: Spectral
  url: rules/picomes-rules.yml
- group: design
  href: https://artifacts.apis.io/picomes/json-ld/picomes-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/picomes-context.jsonld
- group: design
  href: https://artifacts.apis.io/picomes/vocabulary/picomes-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/picomes-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/picomes/data-model/picomes-data-model.yml
  title: ''
  type: DataModel
  url: data-model/picomes-data-model.yml
- group: operate
  href: https://artifacts.apis.io/picomes/changelog/picomes-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/picomes-changelog.yml
- group: auth
  href: https://artifacts.apis.io/picomes/authentication/picomes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/picomes-authentication.yml
- group: design
  href: https://artifacts.apis.io/picomes/conformance/picomes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/picomes-conformance.yml
- group: other
  href: https://artifacts.apis.io/picomes/hosts/picomes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/picomes-hosts.yml
- group: other
  href: https://artifacts.apis.io/picomes/vendors/picomes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/picomes-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.picomes.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.picomes.com/resources/news/pico-mes-series-a
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.picomes.com/
- group: auth
  href: https://artifacts.apis.io/picomes/security/picomes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/picomes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.picomes.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.picomes.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.picomes.com/resources/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.picomes.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.picomes.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.picomes.com/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://www.picomes.com/guide/what-is-modular-mes
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.picomes.com/mcp
  - status: 200
    url: https://www.picomes.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Picomes provides a modular Manufacturing Execution System (MES) platform that digitizes work instructions, connects IoT tools, and error‑proofs assembly lines for mid‑sized manufacturers. Their cloud‑based solution enables real‑time monitoring, data collection, and continuous improvement, helping factories reduce errors, increase efficiency, and achieve higher quality production outcomes.
finops:
- has_sources: true
  method: derived
  name: Picomes Finops
  primary_unit: subscription
  service_category: ''
  slug: picomes-finops
  template: false
json_schemas:
- name: GetGraphV2Response
  property_count: 1
  slug: picomes-get-graph-v2-response
- name: PatchUploadsIdRequest
  property_count: 3
  slug: picomes-patch-uploads-id-request
- name: PatchUploadsIdResponse
  property_count: 3
  slug: picomes-patch-uploads-id-response
- name: PostApiPicoWebhooksRequest
  property_count: 2
  slug: picomes-post-api-pico-webhooks-request
- name: PostApiPicoWebhooksResponse
  property_count: 1
  slug: picomes-post-api-pico-webhooks-response
- name: PostGraphV2Request
  property_count: 2
  slug: picomes-post-graph-v2-request
jsonld:
- class_count: 7
  name: Picomes Context
  property_count: 8
  slug: picomes-context
layout: provider
modified: '2026-10-12'
name: Picomes
nav: Providers
network: true
overview: 'Picomes is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Graph API, Pico Webhooks API, and 2 more. Tagged areas include Manufacturing, MES, IoT, ErrorProofing, and Software.


  The Picomes catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Picomes'' developer surface includes changelog, authentication, documentation, pricing, engineering blog, support, getting-started guide, and 14 more developer resources.'
plans:
- name: Picomes Plans Pricing
  plan_count: 4
  slug: picomes-plans-pricing
- name: Picomes Price Estimates
  plan_count: 0
  slug: picomes-price-estimates
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Picomes API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: picomes-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 12.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 23.2
    developer_ergonomics: 26.2
    discoverability: 59.8
    operational_transparency: 21.1
  previous_composite: 41.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/picomes/picomes-2026-11-03T141212.png
security:
- kind: authentication
  name: Picomes Authentication
  slug: picomes-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Picomes Domain Security
  slug: picomes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: picomes
tags:
- Manufacturing
- MES
- IoT
- ErrorProofing
- Software
website: https://www.picomes.com
---
