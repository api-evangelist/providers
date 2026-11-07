---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.routerplus.com
  baseurl_source: declared
  description: 'RouterPlus API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: RouterPlus API
  slug: routerplus-com-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/routerplus-com/rate-limits/routerplus-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/routerplus-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/routerplus-com/rules/routerplus-com-rules.yml
  title: ''
  type: Spectral
  url: rules/routerplus-com-rules.yml
- group: design
  href: https://artifacts.apis.io/routerplus-com/json-ld/routerplus-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/routerplus-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/routerplus-com/vocabulary/routerplus-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/routerplus-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/routerplus-com/data-model/routerplus-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/routerplus-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/routerplus-com/conformance/routerplus-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/routerplus-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/routerplus-com/llms/routerplus-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/routerplus-com-llms.txt
- group: other
  href: https://artifacts.apis.io/routerplus-com/hosts/routerplus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/routerplus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/routerplus-com/vendors/routerplus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/routerplus-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://app.routerplus.com/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://app.routerplus.com/docs/pricing
- group: start
  title: ''
  type: Login
  url: https://app.routerplus.com/login
- group: company
  title: ''
  type: Blog
  url: https://routerplus.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.routerplus.com/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://dev.routerplus.com/
- group: auth
  href: https://artifacts.apis.io/routerplus-com/security/routerplus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/routerplus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://routerplus.com
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://app.routerplus.com/docs/overview
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: RouterPlus provides AI inference and LLM routing on your own evaluations, offering a catalog of models with both open and closed weights. It emphasizes data compliance, regional routing, and production‑grade SLAs, handling millions of requests daily. Users can reserve capacity, integrate via API endpoints for chat completions, image generation, video creation, and more, with detailed docs, pricing, and support.
image: https://cdn.ploy.ai/a8b36ce4-92a1-4fb9-8c39-f876dcdbc872/user/3c75141e-home-routerplus-20261003.webp
json_schemas:
- name: GetApiIdentityMembersResponse
  property_count: 4
  slug: routerplus-com-get-api-identity-members-response
- name: GetApiIdentityOrganizationsResponse
  property_count: 4
  slug: routerplus-com-get-api-identity-organizations-response
- name: GetApiIdentityWorkspacesResponse
  property_count: 5
  slug: routerplus-com-get-api-identity-workspaces-response
- name: GetV1ChatCompletionsResponse
  property_count: 6
  slug: routerplus-com-get-v1-chat-completions-response
- name: GetV1GenerationResponse
  property_count: 29
  slug: routerplus-com-get-v1-generation-response
- name: PostApiIdentityMembersRequest
  property_count: 3
  slug: routerplus-com-post-api-identity-members-request
jsonld:
- class_count: 17
  name: Routerplus Com Context
  property_count: 32
  slug: routerplus-com-context
layout: provider
modified: '2026-10-28'
name: RouterPlus
nav: Providers
network: true
overview: 'RouterPlus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Inference, LLM, Routing, and Cloud.


  The RouterPlus catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RouterPlus'' developer surface includes sandbox, pricing, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 4
  name: Routerplus Com Rate Limits
  slug: routerplus-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: RouterPlus API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: routerplus-com-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 11.8
    contract_governance: 19.7
    contract_quality: 26.0
    developer_ergonomics: 15.5
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 29.8
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
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/routerplus-com/routerplus-com-2026-11-03T142426.png
security:
- kind: domain-security
  name: Routerplus Com Domain Security
  slug: routerplus-com-domain-security
  summary_line: TLSv1.3
slug: routerplus-com
tags:
- Artificial Intelligence
- Inference
- LLM
- Routing
- Cloud
- Platform
website: https://routerplus.com
---
