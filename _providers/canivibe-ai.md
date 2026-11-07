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
    mcp_server: documented
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
  score: 20.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Live status API providing JSON availability data for AI coding providers.
  name: Can I Vibe API
  slug: can-i-vibe-api
- description: 'Can I Vibe API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Can I Vibe API
  slug: canivibe-ai-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/canivibe-ai/plans/canivibe-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canivibe-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/canivibe-ai/rules/canivibe-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/canivibe-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/canivibe-ai/json-ld/canivibe-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canivibe-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/canivibe-ai/vocabulary/canivibe-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canivibe-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/canivibe-ai/data-model/canivibe-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canivibe-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/canivibe-ai/conformance/canivibe-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canivibe-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canivibe-ai/llms/canivibe-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canivibe-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/canivibe-ai/hosts/canivibe-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canivibe-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/canivibe-ai/security/canivibe-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canivibe-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canivibe.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://canivibe.ai/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://canivibe.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://canivibe.ai/login
- group: operate
  title: ''
  type: Support
  url: https://canivibe.ai/status
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are HTML without a published OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract.
  evidence:
  - status: 200
    url: https://canivibe.ai/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Can I Vibe provides a live availability monitoring service for AI coding providers. It aggregates status information from 22 providers, offering a free JSON API, CI gate, and instant webhooks. Users can embed status badges in README files and receive alerts when providers experience issues. The platform aims to improve reliability of AI development pipelines by making provider outages visible and actionable.
json_schemas:
- name: GetApiHealthyIdResponse
  property_count: 3
  slug: canivibe-ai-get-api-healthy-id-response
- name: GetApiHealthyResponse
  property_count: 1
  slug: canivibe-ai-get-api-healthy-response
- name: GetApiStatusIdResponse
  property_count: 6
  slug: canivibe-ai-get-api-status-id-response
- name: GetApiStatusResponse
  property_count: 3
  slug: canivibe-ai-get-api-status-response
- name: GetProvidersResponse
  property_count: 1
  slug: canivibe-ai-get-providers-response
- name: GetStatusResponse
  property_count: 3
  slug: canivibe-ai-get-status-response
jsonld:
- class_count: 8
  name: Canivibe Ai Context
  property_count: 16
  slug: canivibe-ai-context
layout: provider
modified: '2026-11-04'
name: Can I Vibe
nav: Providers
network: true
overview: 'Can I Vibe is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Artificial Intelligence, and Status.


  The Can I Vibe catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Can I Vibe''s developer surface includes documentation, pricing, signup flow, support, and 10 more developer resources.'
plans:
- name: Canivibe Ai Plans Pricing
  plan_count: 2
  slug: canivibe-ai-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Can I Vibe API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: canivibe-ai-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 58.8
    catalog_earned_first_party: 8.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 32.9
    contract_governance: 22.0
    contract_quality: 23.6
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canivibe Ai Domain Security
  slug: canivibe-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: canivibe-ai
tags:
- Company
- Monitoring
- Artificial Intelligence
- Status
website: https://canivibe.ai/
---
