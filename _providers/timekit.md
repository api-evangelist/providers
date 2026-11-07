---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Timekit provides a flexible scheduling API for building custom booking experiences.
  name: Timekit API
  slug: timekit-api-2
- baseURL: https://api.timekit.io
  baseurl_source: declared
  description: 'Timekit API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Timekit API
  slug: timekit-api
artifact_total: 13
common:
- group: auth
  href: https://artifacts.apis.io/timekit/well-known/timekit-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/timekit-status-security.txt
- group: operate
  href: https://artifacts.apis.io/timekit/rate-limits/timekit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/timekit-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/timekit/plans/timekit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/timekit-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/timekit/rules/timekit-rules.yml
  title: ''
  type: Spectral
  url: rules/timekit-rules.yml
- group: design
  href: https://artifacts.apis.io/timekit/json-ld/timekit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/timekit-context.jsonld
- group: design
  href: https://artifacts.apis.io/timekit/vocabulary/timekit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/timekit-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/timekit/data-model/timekit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/timekit-data-model.yml
- group: operate
  href: https://artifacts.apis.io/timekit/changelog/timekit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/timekit-changelog.yml
- group: design
  href: https://artifacts.apis.io/timekit/conformance/timekit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/timekit-conformance.yml
- group: agent
  href: https://artifacts.apis.io/timekit/llms/timekit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/timekit-llms.txt
- group: auth
  href: https://artifacts.apis.io/timekit/well-known/timekit-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/timekit-help-security.txt
- group: agent
  href: https://artifacts.apis.io/timekit/well-known/timekit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/timekit-well-known.yml
- group: other
  href: https://artifacts.apis.io/timekit/hosts/timekit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/timekit-hosts.yml
- group: other
  href: https://artifacts.apis.io/timekit/vendors/timekit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/timekit-vendors.yml
- group: build
  href: https://artifacts.apis.io/timekit/packages/timekit-packages.yml
  title: ''
  type: SDKs
  url: packages/timekit-packages.yml
- group: build
  href: https://artifacts.apis.io/timekit/packages/timekit-packages.yml
  title: ''
  type: Packages
  url: packages/timekit-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.timekit.io/terms-of-service-and-privacy-policy/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.timekit.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.timekit.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.timekit.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: http://help.timekit.io/en/articles/1955020-getting-started-with-timekit
- group: docs
  title: ''
  type: Documentation
  url: https://developers.timekit.io/
- group: auth
  href: https://artifacts.apis.io/timekit/security/timekit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/timekit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.timekit.io
coverage:
  detail: Docs site renders HTML via JavaScript, no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.timekit.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Timekit provides a flexible scheduling API that enables businesses to build custom booking experiences, manage inventory, users, and availability. Their platform offers a developer-friendly REST API, extensive documentation, and SDKs, allowing integration of scheduling features into web and mobile applications at scale.
json_schemas:
- name: GetV2AppResponse
  property_count: 1
  slug: timekit-get-v2-app-response
- name: GetV2ResourcesIdResponse
  property_count: 8
  slug: timekit-get-v2-resources-id-response
- name: GetV2ResourcesResponse
  property_count: 11
  slug: timekit-get-v2-resources-response
- name: GetWebhooksResponse
  property_count: 1
  slug: timekit-get-webhooks-response
- name: PostV2ResourcesRequest
  property_count: 5
  slug: timekit-post-v2-resources-request
- name: PutV2ResourcesIdRequest
  property_count: 6
  slug: timekit-put-v2-resources-id-request
jsonld:
- class_count: 7
  name: Timekit Context
  property_count: 27
  slug: timekit-context
layout: provider
modified: '2026-10-29'
name: Timekit
nav: Providers
network: true
overview: 'Timekit is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Scheduling, Software-as-a-Service, and Booking.


  The Timekit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Timekit''s developer surface includes changelog, support, pricing, getting-started guide, documentation, and 19 more developer resources.'
plans:
- name: Timekit Plans Pricing
  plan_count: 4
  slug: timekit-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Timekit Rate Limits
  slug: timekit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Timekit API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: timekit-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 20.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 27.5
    developer_ergonomics: 20.2
    discoverability: 51.8
    operational_transparency: 55.3
  previous_composite: 41.8
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/timekit/timekit-2026-11-03T144751.png
security:
- kind: domain-security
  name: Timekit Domain Security
  slug: timekit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: timekit
tags:
- Company
- Scheduling
- Software-as-a-Service
- Booking
website: https://www.timekit.io
---
