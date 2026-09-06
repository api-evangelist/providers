---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'REST API to list models and launch/track image and video generations. Endpoints: GET /api/models (unauthenticated catalog & pricing), POST /api/generate, GET /api/generate/status. Uses imk_ bearer-key'
  name: Imaginode REST API
  slug: imaginode-rest-api
- description: 'Hosted MCP server (Streamable HTTP transport) exposing four tools: list_models, generate_image, generate_video, get_generation_status. Authenticated via Authorization: Bearer imk_ header.'
  name: Imaginode MCP Server
  slug: imaginode-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://imaginode.ai
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imaginode-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imaginode-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/imaginode-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imaginode-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/imaginode-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/imaginode-problem-types.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/imaginode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imaginode-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://imaginode.ai/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://imaginode.ai/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://imaginode.ai/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imaginode.ai/en/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imaginode.ai/en/legal/terms
- group: start
  title: ''
  type: Login
  url: https://imaginode.ai/en/login
created: '2026-09-03'
description: Browser-based AI creation studio with a node canvas for generating images, videos, voice-overs and LLM outputs. Provides a REST API, a hosted MCP server, and an llms.txt for programmatic and agent-based generation using a shared credit balance.
image: https://imaginode.ai/icons-512.png
layout: provider
mcp_servers:
- description: ''
  name: Imaginode MCP Server
  slug: imaginode-mcp-server
- description: Official hosted MCP server exposing Imaginode's generation pipeline (images, video, model catalog, job status) to any MCP client over Streamable HTTP. Stateless; billed against the connected account's
  name: Imaginode MCP Server
  slug: imaginode-mcp-server-2
modified: '2026-09-03'
name: Imaginode
nav: Providers
network: true
overview: 'Imaginode publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ai, image generation, video generation, text to speech, and mcp.


  Imaginode''s developer surface includes authentication, documentation, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Imaginode Plans Pricing
  plan_count: 3
  slug: imaginode-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Imaginode Rate Limits
  slug: imaginode-rate-limits
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.8
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Imaginode Authentication
  slug: imaginode-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Imaginode Domain Security
  slug: imaginode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imaginode
tags:
- ai
- image generation
- video generation
- text to speech
- mcp
- generative ai
- llm
- creative tools
website: https://imaginode.ai
---
