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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Archome AI API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Archome AI API
  slug: archome-ai-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/archome-ai/rules/archome-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/archome-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/archome-ai/json-ld/archome-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/archome-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/archome-ai/vocabulary/archome-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/archome-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/archome-ai/data-model/archome-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/archome-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/archome-ai/conformance/archome-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/archome-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/archome-ai/llms/archome-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archome-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/archome-ai/well-known/archome-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/archome-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/archome-ai/hosts/archome-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/archome-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/archome-ai/vendors/archome-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/archome-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://archome.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://archome.ai/legal/privacy
- group: auth
  href: https://artifacts.apis.io/archome-ai/security/archome-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archome-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://archome.ai/
- group: operate
  title: ''
  type: Support
  url: https://archome.ai/help
- group: commercial
  title: ''
  type: Pricing
  url: https://archome.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://archome.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://archome.ai/auth/register
- group: start
  title: ''
  type: Login
  url: https://archome.ai/auth/login
coverage:
  checked: '2026-11-01'
  detail: API endpoints require authentication (MCP endpoint returns 401) and no public spec is available.
  evidence:
  - status: 401
    url: https://archome.ai/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Archome AI provides AI‑powered virtual staging, architectural rendering, and design tools for architects, designers, and real‑estate professionals. The platform offers instant photorealistic renders from sketches, floor plans, or photos, with a suite of AI tools for interior, exterior, material swapping, video creation, and more. Over 750 K users across 180 countries rely on Archome AI to accelerate design workflows, reduce costs, and deliver client‑ready visualizations in seconds. Free trial credits are available without a credit card, and paid plans scale for individuals to enterprises.
image: https://archome.ai/logo.webp
json_schemas:
- name: PostApiV1RenderRequest
  property_count: 3
  slug: archome-ai-post-api-v1-render-request
- name: PostApiV1RenderResponse
  property_count: 4
  slug: archome-ai-post-api-v1-render-response
jsonld:
- class_count: 2
  name: Archome Ai Context
  property_count: 7
  slug: archome-ai-context
layout: provider
modified: '2026-11-01'
name: Archome AI
nav: Providers
network: true
overview: 'Archome AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Virtual Staging, Architectural Rendering, Design Tools, and Software-as-a-Service.


  The Archome AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Archome AI''s developer surface includes support, pricing, engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Archome Ai Plans Pricing
  plan_count: 0
  slug: archome-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Archome Ai Rate Limits
  slug: archome-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Archome AI API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: archome-ai-rules
scopes:
- name: Archome Ai Scopes
  scope_count: 0
  slug: archome-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 25.6
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Archome Ai Authentication
  slug: archome-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Archome Ai Domain Security
  slug: archome-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: archome-ai
tags:
- Artificial Intelligence
- Virtual Staging
- Architectural Rendering
- Design Tools
- Software-as-a-Service
website: https://archome.ai/
---
