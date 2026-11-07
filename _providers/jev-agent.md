---
access_model:
  confidence: high
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Jev Agent (Jagent) API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Jev Agent (Jagent) API
  slug: jev-agent-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/jev-agent/rate-limits/jev-agent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jev-agent-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jev-agent/plans/jev-agent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jev-agent-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jev-agent/rules/jev-agent-rules.yml
  title: ''
  type: Spectral
  url: rules/jev-agent-rules.yml
- group: design
  href: https://artifacts.apis.io/jev-agent/json-ld/jev-agent-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jev-agent-context.jsonld
- group: design
  href: https://artifacts.apis.io/jev-agent/vocabulary/jev-agent-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jev-agent-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jev-agent/data-model/jev-agent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jev-agent-data-model.yml
- group: auth
  href: https://artifacts.apis.io/jev-agent/authentication/jev-agent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jev-agent-authentication.yml
- group: design
  href: https://artifacts.apis.io/jev-agent/conformance/jev-agent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jev-agent-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jev-agent/llms/jev-agent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jev-agent-llms.txt
- group: agent
  href: https://artifacts.apis.io/jev-agent/well-known/jev-agent-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jev-agent-well-known.yml
- group: other
  href: https://artifacts.apis.io/jev-agent/hosts/jev-agent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jev-agent-hosts.yml
- group: other
  href: https://artifacts.apis.io/jev-agent/vendors/jev-agent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jev-agent-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jev-agent.com/terms
- group: start
  title: ''
  type: Sandbox
  url: https://jev-agent.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jev-agent.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://jev-agent.com/getting-started
- group: auth
  href: https://artifacts.apis.io/jev-agent/security/jev-agent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jev-agent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jev-agent.com/api-access
- group: docs
  title: ''
  type: Documentation
  url: https://jev-agent.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://jev-agent.com/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://jev-agent.com/pricing
coverage:
  checked: '2026-10-18'
  detail: The provider's documentation page https://jev-agent.com/docs returns HTML with no discoverable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://jev-agent.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Jev Agent (Jagent) is an independent relay offering access to TypeSafe AI’s Jev decision model. It provides API keys without waitlists or credit cards, enabling developers to integrate Jev’s choice, score, and noul decision capabilities via its own gateway or directly through TypeSafe. The service includes documentation, playground, pricing plans, and various use‑case demos, positioning itself as a convenient front‑end for the Jev model.
image: https://jev-agent.com/opengraph-image?13b076b2458fadef
json_schemas:
- name: GetApiV1ModelsResponse
  property_count: 5
  slug: jev-agent-get-api-v1-models-response
- name: PostApiV1DecisionsRequest
  property_count: 8
  slug: jev-agent-post-api-v1-decisions-request
- name: PostApiV1SystemoneRequest
  property_count: 2
  slug: jev-agent-post-api-v1-systemone-request
- name: PostApiV1ToolsResumeCheckResponse
  property_count: 9
  slug: jev-agent-post-api-v1-tools-resume-check-response
- name: PostV1DecisionsRequest
  property_count: 7
  slug: jev-agent-post-v1-decisions-request
- name: PostV1SystemoneResponse
  property_count: 4
  slug: jev-agent-post-v1-systemone-response
jsonld:
- class_count: 17
  name: Jev Agent Context
  property_count: 42
  slug: jev-agent-context
layout: provider
modified: '2026-10-17'
name: Jev Agent (Jagent)
nav: Providers
network: true
overview: 'Jev Agent (Jagent) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI API, Classification, Token Billing, and Developer Tools.


  The Jev Agent (Jagent) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Jev Agent (Jagent)''s developer surface includes authentication, sandbox, getting-started guide, documentation, API reference, pricing, and 15 more developer resources.'
plans:
- name: Jev Agent Plans Pricing
  plan_count: 5
  slug: jev-agent-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Jev Agent Rate Limits
  slug: jev-agent-rate-limits
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Jev Agent (Jagent) API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: jev-agent-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 72.8
    catalog_earned_first_party: 20.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 29.8
    discoverability: 55.4
    operational_transparency: 21.1
  previous_composite: 40.0
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jev-agent/jev-agent-2026-11-03T134138.png
security:
- kind: authentication
  name: Jev Agent Authentication
  slug: jev-agent-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jev Agent Domain Security
  slug: jev-agent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jev-agent
tags:
- AI API
- Classification
- Token Billing
- Developer Tools
website: https://jev-agent.com/api-access
---
