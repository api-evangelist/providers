---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.dispatchmind.ai
  baseurl_source: declared
  description: 'DispatchMind API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DispatchMind API
  slug: dispatchmind-ai-api
artifact_total: 12
asyncapis:
- description: ''
  name: Dispatchmind Ai Webhooks
  slug: dispatchmind-ai-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/dispatchmind-ai/plans/dispatchmind-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dispatchmind-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dispatchmind-ai/rules/dispatchmind-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dispatchmind-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dispatchmind-ai/json-ld/dispatchmind-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dispatchmind-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/dispatchmind-ai/vocabulary/dispatchmind-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dispatchmind-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dispatchmind-ai/asyncapi/dispatchmind-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dispatchmind-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dispatchmind-ai/data-model/dispatchmind-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dispatchmind-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/dispatchmind-ai/conformance/dispatchmind-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dispatchmind-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dispatchmind-ai/llms/dispatchmind-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dispatchmind-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/dispatchmind-ai/well-known/dispatchmind-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dispatchmind-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dispatchmind-ai/hosts/dispatchmind-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dispatchmind-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dispatchmind-ai/vendors/dispatchmind-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dispatchmind-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://app.dispatchmind.ai/status
- group: auth
  href: https://artifacts.apis.io/dispatchmind-ai/security/dispatchmind-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dispatchmind-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dispatchmind.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dispatchmind.ai/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://dispatchmind.ai/help/
- group: docs
  title: ''
  type: APIReference
  url: https://app.dispatchmind.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://dispatchmind.ai/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://dispatchmind.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://dispatchmind.ai/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dispatchmind.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dispatchmind.ai/privacy/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on the provider's documentation or API hosts.
  evidence:
  - status: 200
    url: https://dispatchmind.ai/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DispatchMind provides job management software for service companies, offering features like dispatch, calendar, estimates, invoicing, AI‑driven dispatch assistance, and mobile apps. It targets home‑service businesses such as HVAC, plumbing, electrical, and logistics, with a 14‑day free trial and flexible pricing plans.
image: https://app.dispatchmind.ai/og.jpg
json_schemas:
- name: PostOauthTokenRequest
  property_count: 6
  slug: dispatchmind-ai-post-oauth-token-request
- name: PostV1HooksRequest
  property_count: 2
  slug: dispatchmind-ai-post-v1-hooks-request
- name: PostV1HooksResponse
  property_count: 3
  slug: dispatchmind-ai-post-v1-hooks-response
- name: PostV1JobsIdNotesRequest
  property_count: 2
  slug: dispatchmind-ai-post-v1-jobs-id-notes-request
- name: PostV1JobsRequest
  property_count: 8
  slug: dispatchmind-ai-post-v1-jobs-request
- name: PostV1LeadsRequest
  property_count: 9
  slug: dispatchmind-ai-post-v1-leads-request
jsonld:
- class_count: 6
  name: Dispatchmind Ai Context
  property_count: 22
  slug: dispatchmind-ai-context
layout: provider
modified: '2026-11-05'
name: DispatchMind
nav: Providers
network: true
overview: 'DispatchMind is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software, Field Service Management, Dispatch, Software-as-a-Service, and Job Management.


  The DispatchMind catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DispatchMind''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Dispatchmind Ai Plans Pricing
  plan_count: 4
  slug: dispatchmind-ai-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: DispatchMind API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: dispatchmind-ai-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 23.7
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dispatchmind Ai Domain Security
  slug: dispatchmind-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dispatchmind-ai
tags:
- Software
- Field Service Management
- Dispatch
- Software-as-a-Service
- Job Management
website: https://dispatchmind.ai/
---
