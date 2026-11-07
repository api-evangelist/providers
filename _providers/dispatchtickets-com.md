---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    event_surface_described: true
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
  score: 19.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The API provides REST endpoints for ticketing operations as documented in the API Reference.
  name: Dispatch Tickets API
  slug: dispatch-tickets-api
- baseURL: https://api.dispatchtickets.com
  baseurl_source: declared
  description: 'Dispatch Tickets API as documented publicly: 44 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dispatch Tickets API
  slug: dispatchtickets-com-api
artifact_total: 14
asyncapis:
- description: ''
  name: Dispatchtickets Com Webhooks
  slug: dispatchtickets-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/dispatchtickets-com/plans/dispatchtickets-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dispatchtickets-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dispatchtickets-com/rules/dispatchtickets-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dispatchtickets-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dispatchtickets-com/json-ld/dispatchtickets-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dispatchtickets-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dispatchtickets-com/vocabulary/dispatchtickets-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dispatchtickets-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dispatchtickets-com/asyncapi/dispatchtickets-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dispatchtickets-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dispatchtickets-com/data-model/dispatchtickets-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dispatchtickets-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dispatchtickets-com/authentication/dispatchtickets-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dispatchtickets-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dispatchtickets-com/conformance/dispatchtickets-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dispatchtickets-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dispatchtickets-com/hosts/dispatchtickets-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dispatchtickets-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dispatchtickets-com/vendors/dispatchtickets-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dispatchtickets-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dispatchtickets-com/packages/dispatchtickets-com-packages.yml
  title: ''
  type: Packages
  url: packages/dispatchtickets-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dispatchtickets.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://dispatchtickets.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://dispatchtickets.com/signup/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@dispatchtickets/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dispatchtickets.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://dispatchtickets.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://dispatchtickets.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dispatchtickets.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://dispatchtickets.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/dispatchtickets-com/security/dispatchtickets-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dispatchtickets-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dispatchtickets.com/
coverage:
  detail: API reference page renders a Swagger UI HTML shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://dispatchtickets.com/docs/api-only/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Dispatch Tickets provides an API-first multi‑brand ticketing system and helpdesk software. The platform lets developers integrate customer support directly into their products, offering per‑ticket pricing, unlimited team members, webhooks, custom email domains, and a RESTful API. Founded in 2025, it aims to replace traditional agent‑based pricing with a flexible, usage‑based model for modern SaaS applications.
image: https://dispatchtickets.com/og-image.jpg
json_schemas:
- name: GetV1BrandsBrandidTicketsIdResponse
  property_count: 9
  slug: dispatchtickets-com-get-v1-brands-brandid-tickets-id-response
- name: GetV1BrandsBrandidTicketsResponse
  property_count: 9
  slug: dispatchtickets-com-get-v1-brands-brandid-tickets-response
- name: GetV1FeatureRequestsResponse
  property_count: 6
  slug: dispatchtickets-com-get-v1-feature-requests-response
- name: GetV1WorkspacesWsXxxStatsResponse
  property_count: 6
  slug: dispatchtickets-com-get-v1-workspaces-ws-xxx-stats-response
- name: PostV1WorkspacesWsXxxTicketsRequest
  property_count: 11
  slug: dispatchtickets-com-post-v1-workspaces-ws-xxx-tickets-request
- name: PutV1RoutingConfigRequest
  property_count: 6
  slug: dispatchtickets-com-put-v1-routing-config-request
jsonld:
- class_count: 44
  name: Dispatchtickets Com Context
  property_count: 68
  slug: dispatchtickets-com-context
layout: provider
modified: '2026-11-05'
name: Dispatch Tickets
nav: Providers
network: true
overview: 'Dispatch Tickets is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Ticketing, Help Desk, API-First, Software-as-a-Service, and Multi-brand.


  The Dispatch Tickets catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Dispatch Tickets'' developer surface includes authentication, support, signup flow, pricing, documentation, getting-started guide, and 16 more developer resources.'
plans:
- name: Dispatchtickets Com Plans Pricing
  plan_count: 4
  slug: dispatchtickets-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Dispatch Tickets API Rules
  rule_count: 45
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 5
  slug: dispatchtickets-com-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 54.8
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dispatchtickets Com Authentication
  slug: dispatchtickets-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dispatchtickets Com Domain Security
  slug: dispatchtickets-com-domain-security
  summary_line: TLSv1.3
slug: dispatchtickets-com
tags:
- Ticketing
- Help Desk
- API-First
- Software-as-a-Service
- Multi-brand
website: https://dispatchtickets.com/
---
