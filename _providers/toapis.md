---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: OpenAI-compatible REST API covering chat/completions, image generation, video generation, and model listing (plus Anthropic Messages and OpenAI Responses formats). Key-authenticated via Bearer token.
  name: ToAPIs API
  slug: toapis-api
artifact_total: 9
asyncapis:
- description: ''
  name: Toapis Webhooks
  slug: toapis-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://toapis.com
- group: auth
  href: https://artifacts.apis.io/toapis/security/toapis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toapis-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/toapis/mcp/toapis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/toapis-mcp.yml
- group: other
  href: https://artifacts.apis.io/toapis/a2a/toapis-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/toapis-a2a.yml
- group: agent
  href: https://artifacts.apis.io/toapis/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/toapis/llms/toapis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toapis-llms.txt
- group: agent
  href: https://artifacts.apis.io/toapis/well-known/toapis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/toapis-well-known.yml
- group: design
  href: https://artifacts.apis.io/toapis/asyncapi/toapis-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/toapis-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/toapis/rate-limits/toapis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/toapis-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/toapis/plans/toapis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/toapis-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/toapis/errors/toapis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/toapis-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/toapis/authentication/toapis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toapis-authentication.yml
- group: design
  href: https://artifacts.apis.io/toapis/conventions/toapis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/toapis-conventions.yml
- group: design
  href: https://artifacts.apis.io/toapis/conformance/toapis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toapis-conformance.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://toapis.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toapis.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toapis.com/privacy
- group: start
  title: ''
  type: Login
  url: https://toapis.com/login
- group: start
  title: ''
  type: Portal
  url: https://toapis.com/dashboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/toapis
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/hvnszCrJ73
created: '2026-09-07'
description: An OpenAI-compatible AI API gateway/aggregator fronting 50+ text, image, and video models (GPT, Claude, Gemini, DeepSeek, Qwen, Sora/Veo/Kling, etc.) behind a single integration, with model routing, provider failover, unified usage tracking, and consolidated billing.
finops:
- has_sources: true
  method: derived
  name: Toapis Finops
  primary_unit: second
  service_category: ''
  slug: toapis-finops
  template: false
image: https://docs.toapis.com/logo/light.svg
layout: provider
mcp_servers:
- description: Remote MCP server at docs.toapis.com; 3 tools listed.
  name: ToAPIs MCP Server
  slug: toapis-mcp-yml
modified: '2026-09-07'
name: ToAPIs
nav: Providers
network: true
overview: 'ToAPIs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI API, LLM/AI gateway, model aggregation, OpenAI-Compatible, and Model Routing.


  The ToAPIs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ToAPIs'' developer surface includes authentication, pricing, developer portal, support, and 17 more developer resources.'
plans:
- name: Toapis Plans Pricing
  plan_count: 3
  slug: toapis-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Toapis Rate Limits
  slug: toapis-rate-limits
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 54.8
    discoverability: 66.7
    operational_transparency: 44.7
  previous_composite: 45.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/toapis/toapis-2026-10-11T130955.png
security:
- kind: authentication
  name: Toapis Authentication
  slug: toapis-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Toapis Domain Security
  slug: toapis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Apis
  slug: toapis-apis
slug: toapis
tags:
- AI API
- LLM/AI gateway
- model aggregation
- OpenAI-Compatible
- Model Routing
- provider failover
- Text Generation
- Image Generation
- Video Generation
- Developer Tools
- A2A
website: https://toapis.com
---
