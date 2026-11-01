---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-10-31'
api_count: 3
apis:
- baseURL: https://api.nereo.io
  baseurl_source: declared
  description: 'Nereo Overview API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: Nereo Overview API
  slug: api-reference-api
- baseURL: https://api.nereo.io
  baseurl_source: declared
  description: 'Nereo core API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: Nereo core API
  slug: core-api
- baseURL: https://api.nereo.io
  baseurl_source: declared
  description: 'Nereo Overview API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: Nereo Overview API
  slug: models-api
artifact_total: 25
common:
- group: operate
  href: https://artifacts.apis.io/nereo/rate-limits/nereo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nereo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nereo/plans/nereo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nereo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nereo/rules/nereo-rules.yml
  title: ''
  type: Spectral
  url: rules/nereo-rules.yml
- group: design
  href: https://artifacts.apis.io/nereo/json-ld/nereo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nereo-context.jsonld
- group: design
  href: https://artifacts.apis.io/nereo/vocabulary/nereo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nereo-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/nereo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nereo/data-model/nereo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nereo-data-model.yml
- group: auth
  href: https://artifacts.apis.io/nereo/authentication/nereo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nereo-authentication.yml
- group: design
  href: https://artifacts.apis.io/nereo/lifecycle/nereo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nereo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nereo/errors/nereo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nereo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nereo/conformance/nereo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nereo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nereo/llms/nereo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nereo-llms.txt
- group: agent
  href: https://artifacts.apis.io/nereo/mcp/nereo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nereo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nereo/well-known/nereo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nereo-well-known.yml
- group: other
  href: https://artifacts.apis.io/nereo/hosts/nereo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nereo-hosts.yml
- group: other
  href: https://artifacts.apis.io/nereo/vendors/nereo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nereo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nereo.io/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nereo.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nereo.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://api.nereo.io/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://api.nereo.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.nereo.io/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/nereo/security/nereo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nereo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nereo.io/
- group: company
  title: ''
  type: Blog
  url: https://www.nereo.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nereo.io/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.nereo.io/mcp
  - status: 200
    url: https://www.nereo.io/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Nereo is an AI‑powered video generation platform that enables creators, marketers, and businesses to produce high‑quality 4K videos from simple text prompts, images, or reference footage. Leveraging proprietary AI models such as Kling 4.0, Genjutsu, and OmniHuman 2.0, Nereo offers tools for text‑to‑video, image‑to‑video, AI‑shorts, video upscaling, lip‑sync, and a suite of ecommerce‑focused video ads. Users can start for free, generate videos with realistic physics and native audio, and integrate the output into marketing campaigns, product showcases, and social media content, democratizing professional video creation without extensive editing expertise.
image: https://www.nereo.io/logo.png
json_schemas:
- name: GetApiV1Response
  property_count: 1
  slug: nereo-get-api-v1-response
- name: GetResponse
  property_count: 7
  slug: nereo-get-response
- name: PostApiV1Requests7C1K2N0Q8X4M3V9D5A6BStatusRequest
  property_count: 1
  slug: nereo-post-api-v1-requests7-c1-k2-n0-q8-x4-m3-v9-d5-a6-bstatus-request
- name: PostApiV1Requests7C1K2N0Q8X4M3V9D5A6BStatusResponse
  property_count: 4
  slug: nereo-post-api-v1-requests7-c1-k2-n0-q8-x4-m3-v9-d5-a6-bstatus-response
- name: PostFirstFramePngRequest
  property_count: 3
  slug: nereo-post-first-frame-png-request
- name: PostFirstFramePngResponse
  property_count: 4
  slug: nereo-post-first-frame-png-response
- name: PostHooksGenerationRequest
  property_count: 1
  slug: nereo-post-hooks-generation-request
- name: PostInputMp4Request
  property_count: 2
  slug: nereo-post-input-mp4-request
- name: PostInputMp4Response
  property_count: 4
  slug: nereo-post-input-mp4-response
- name: PostInputPngRequest
  property_count: 2
  slug: nereo-post-input-png-request
- name: PostInputPngResponse
  property_count: 4
  slug: nereo-post-input-png-response
- name: PostRequest
  property_count: 1
  slug: nereo-post-request
- name: PostResponse
  property_count: 3
  slug: nereo-post-response
jsonld:
- class_count: 13
  name: Nereo Context
  property_count: 18
  slug: nereo-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.nereo.io.
  name: Nereo MCP Server
  slug: nereo-mcp-yml
modified: '2026-10-30'
name: Nereo
nav: Providers
network: true
overview: 'Nereo is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Overview API, core API, and 1 more. Tagged areas include AI, Video Generation, Marketing, Creator Tools, and SaaS.


  The Nereo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nereo''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Nereo Plans Pricing
  plan_count: 4
  slug: nereo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Nereo Rate Limits
  slug: nereo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Nereo API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: nereo-rules
scopes:
- name: Nereo Scopes
  scope_count: 0
  slug: nereo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.1
    developer_ergonomics: 42.1
    discoverability: 70.0
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nereo Authentication
  slug: nereo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nereo Domain Security
  slug: nereo-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: nereo-overview
  slug: nereo-overview
slug: nereo
tags:
- AI
- Video Generation
- Marketing
- Creator Tools
- SaaS
website: https://www.nereo.io/
---
