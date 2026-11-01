---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Tourscanner Ai Agentic Access
  operation_count: 15
  slug: tourscanner-ai-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 1
apis:
- description: Unified Tours & Activities API providing search, live availability, and full booking lifecycle.
  name: TourScanner API
  slug: tourscanner-api
artifact_total: 18
common:
- group: design
  href: https://artifacts.apis.io/tourscanner-ai/rules/tourscanner-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/tourscanner-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/tourscanner-ai/json-ld/tourscanner-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tourscanner-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/tourscanner-ai/vocabulary/tourscanner-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tourscanner-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tourscanner-ai/conventions/tourscanner-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tourscanner-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/tourscanner-ai/conventions/tourscanner-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tourscanner-ai-conventions.yml
- group: agent
  href: https://artifacts.apis.io/tourscanner-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tourscanner-ai/data-model/tourscanner-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tourscanner-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tourscanner-ai/authentication/tourscanner-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tourscanner-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/tourscanner-ai/errors/tourscanner-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tourscanner-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tourscanner-ai/conformance/tourscanner-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tourscanner-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tourscanner-ai/llms/tourscanner-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tourscanner-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/tourscanner-ai/hosts/tourscanner-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tourscanner-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/tourscanner-ai/vendors/tourscanner-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tourscanner-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tourscanner-ai/security/tourscanner-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tourscanner-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tourscanner.ai
- group: docs
  title: ''
  type: Documentation
  url: https://tourscanner.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://tourscanner.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://tourscanner.ai/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://tourscanner.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tourscanner.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tourscanner.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://tourscanner.ai/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://tourscanner.ai/openapi.json
  - status: 401
    url: https://tourscanner.ai/api/mcp
  - status: 200
    url: https://tourscanner.ai
  reason: partner-login
  state: gated
created: '2026-10-29'
description: TourScanner AI provides a unified Tours & Activities API, aggregating over 1,000,000 activities from 14 providers across 5,000+ cities and 8 languages. Developers can search, check live availability, and book tours via a simple REST interface, with AI‑enhanced agent capabilities and flexible MCP plans. The platform offers extensive documentation, pricing details, and guides to get started quickly.
image: https://tourscanner.ai/og-image.png
json_schemas:
- name: PostApiAvailabilitySlotsRequest
  property_count: 5
  slug: tourscanner-ai-post-api-availability-slots-request
- name: PostApiBookingConfirmResponse
  property_count: 7
  slug: tourscanner-ai-post-api-booking-confirm-response
- name: PostApiBookingHoldRequest
  property_count: 11
  slug: tourscanner-ai-post-api-booking-hold-request
- name: PostAvailabilitySlotsRequest
  property_count: 5
  slug: tourscanner-ai-post-availability-slots-request
- name: PostBookingConfirmResponse
  property_count: 7
  slug: tourscanner-ai-post-booking-confirm-response
- name: PostBookingHoldRequest
  property_count: 11
  slug: tourscanner-ai-post-booking-hold-request
jsonld:
- class_count: 1
  name: Tourscanner Ai Context
  property_count: 3
  slug: tourscanner-ai-context
layout: provider
modified: '2026-10-29'
name: TourScanner AI
nav: Providers
network: true
overview: 'TourScanner AI publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tours, Activities, API, and Booking.


  The TourScanner AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TourScanner AI''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, and 16 more developer resources.'
plans:
- name: Tourscanner Ai Plans Pricing
  plan_count: 0
  slug: tourscanner-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Tourscanner Ai Rate Limits
  slug: tourscanner-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: TourScanner AI API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: tourscanner-ai-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 33.3
    contract_quality: 7.8
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 66.7
      derived: 5
      marker_coverage: 83.3
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tourscanner Ai Authentication
  slug: tourscanner-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Tourscanner Ai Domain Security
  slug: tourscanner-ai-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: tourscanner-ai-availability-check
  slug: tourscanner-ai-availability-check
- name: tourscanner-ai-booking-flow
  slug: tourscanner-ai-booking-flow
- name: search-activities
  slug: tourscanner-ai-search-activities
- name: search-activities
  slug: tourscanner-ai-search
slug: tourscanner-ai
tags:
- Company
- Tours
- Activities
- API
- Booking
website: https://tourscanner.ai
---
