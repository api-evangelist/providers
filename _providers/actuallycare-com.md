---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI‑Ready REST API for Real Estate Transaction Management
  name: ActuallyCare API
  slug: actuallycare-api
- baseURL: https://api.actuallycare.com/v1
  baseurl_source: declared
  description: AI-Ready REST API for Real Estate Transaction Management
  name: ActuallyCare API V1 API
  slug: actuallycare-api-v1-api
artifact_total: 15
asyncapis:
- description: ''
  name: Actuallycare Com Webhooks
  slug: actuallycare-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/actuallycare-com/rules/actuallycare-com-rules.yml
  title: ''
  type: Spectral
  url: rules/actuallycare-com-rules.yml
- group: design
  href: https://artifacts.apis.io/actuallycare-com/json-ld/actuallycare-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/actuallycare-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/actuallycare-com/vocabulary/actuallycare-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/actuallycare-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/actuallycare-com/conformance/actuallycare-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/actuallycare-com-conformance.yml
- group: operate
  href: https://artifacts.apis.io/actuallycare-com/rate-limits/actuallycare-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/actuallycare-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/actuallycare-com/plans/actuallycare-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/actuallycare-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/actuallycare-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/actuallycare-com/asyncapi/actuallycare-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/actuallycare-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/actuallycare-com/data-model/actuallycare-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/actuallycare-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/actuallycare-com/conventions/actuallycare-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/actuallycare-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/actuallycare-com/authentication/actuallycare-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/actuallycare-com-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.actuallycare.com/api/versioning.md
- group: design
  href: https://artifacts.apis.io/actuallycare-com/lifecycle/actuallycare-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/actuallycare-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/actuallycare-com/errors/actuallycare-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/actuallycare-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/actuallycare-com/llms/actuallycare-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actuallycare-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/actuallycare-com/well-known/actuallycare-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/actuallycare-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/actuallycare-com/well-known/actuallycare-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/actuallycare-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/actuallycare-com/hosts/actuallycare-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actuallycare-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/actuallycare-com/vendors/actuallycare-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/actuallycare-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/actuallycare-com/security/actuallycare-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actuallycare-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actuallycare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.actuallycare.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.actuallycare.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.actuallycare.com/mcp/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://actuallycare.com/pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://actuallycare.com/roadmap
- group: operate
  title: ''
  type: Changelog
  url: https://actuallycare.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://actuallycare.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actuallycare.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actuallycare.com/terms
created: '2026-10-31'
description: ActuallyCare is a real‑estate CRM platform designed for agents who truly care about their clients. It centralises client relationships, automates busywork with an AI assistant, and provides features like deal tracking, follow‑up reminders, and AI‑driven insights. Founded by licensed agent Jayden Metz, the service aims to make caring provable, offering a free‑setup, AI specialist support, and continuous feature releases to improve agent productivity and client satisfaction.
image: https://www.actuallycare.com/opengraph-image.png?opengraph-image.f1456ffe.png
json_schemas:
- name: Appointment
  property_count: 18
  slug: actuallycare-com-appointment
- name: Client
  property_count: 20
  slug: actuallycare-com-client
- name: Escrow
  property_count: 30
  slug: actuallycare-com-escrow
- name: Lead
  property_count: 19
  slug: actuallycare-com-lead
- name: Listing
  property_count: 26
  slug: actuallycare-com-listing
- name: ScannedBusinessCard
  property_count: 17
  slug: actuallycare-com-scanned-business-card
jsonld:
- class_count: 14
  name: Actuallycare Com Context
  property_count: 119
  slug: actuallycare-com-context
layout: provider
modified: '2026-10-31'
name: ActuallyCare
nav: Providers
network: true
overview: 'ActuallyCare publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Real Estate CRM, AI Assistant, Deal Tracking, and Partner Network.


  The ActuallyCare catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ActuallyCare''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, changelog, support, and 23 more developer resources.'
plans:
- name: Actuallycare Com Plans Pricing
  plan_count: 3
  slug: actuallycare-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 7
  name: Actuallycare Com Rate Limits
  slug: actuallycare-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: ActuallyCare API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: actuallycare-com-rules
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 35.0
    discoverability: 57.1
    operational_transparency: 56.6
  previous_composite: 56.8
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Actuallycare Com Authentication
  slug: actuallycare-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Actuallycare Com Domain Security
  slug: actuallycare-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: actuallycare-com
tags:
- Real Estate CRM
- AI Assistant
- Deal Tracking
- Partner Network
website: https://actuallycare.com/
---
