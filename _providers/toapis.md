---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-08'
api_count: 1
apis:
- description: OpenAI-compatible REST API covering chat/completions, image generation, video generation, and model listing (plus Anthropic Messages and OpenAI Responses formats). Key-authenticated via Bearer token.
  name: ToAPIs API
  slug: toapis-api
artifact_total: 7
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
  title: ''
  type: DomainSecurity
  url: security/toapis-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/toapis-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/toapis-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toapis-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/toapis-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/toapis-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/toapis-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/toapis-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/toapis-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toapis-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/toapis-conventions.yml
- group: design
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
image: https://docs.toapis.com/logo/light.svg
layout: provider
mcp_servers:
- description: ''
  name: ToAPIs MCP Server
  slug: toapis-mcp-server
modified: '2026-09-07'
name: ToAPIs
nav: Providers
network: true
overview: 'ToAPIs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI API, LLM/AI gateway, model aggregation, OpenAI-compatible, and model routing.


  The ToAPIs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ToAPIs'' developer surface includes authentication, pricing, developer portal, support, and 17 more developer resources.'
plans:
- name: Toapis Plans Pricing
  plan_count: 0
  slug: toapis-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Toapis Rate Limits
  slug: toapis-rate-limits
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 46.0
    catalog_earned_first_party: 12.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 54.8
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 43.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Toapis Authentication
  slug: toapis-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Toapis Domain Security
  slug: toapis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toapis
tags:
- AI API
- LLM/AI gateway
- model aggregation
- OpenAI-compatible
- model routing
- provider failover
- text generation
- image generation
- video generation
- developer tools
website: https://toapis.com
---
