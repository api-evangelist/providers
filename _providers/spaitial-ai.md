---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 76.0
  scored_at: '2026-07-27'
api_count: 4
apis:
- description: File upload endpoints
  name: SpAItial files API
  slug: spaitial-ai-files-api
- description: Model discovery endpoints
  name: SpAItial models API
  slug: spaitial-ai-models-api
- description: The panoramas API from SpAItial — 4 operation(s) for panoramas.
  name: SpAItial panoramas API
  slug: spaitial-ai-panoramas-api
- description: World generation endpoints
  name: SpAItial worlds API
  slug: spaitial-ai-worlds-api
artifact_total: 10
asyncapis:
- description: Webhook event surface for the SpAItial Developer API. Set webhook.url on a POST /v1/worlds request to receive an HTTPS callback on terminal state. Deliveries carry an HMAC-SHA256 signature (X-Spaitial
  name: SpAItial Developer API Webhooks
  slug: spaitial-ai-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaitial-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spaitial-ai-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.spaitial.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spaitial.ai/overview/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spaitial.ai/api/reference/spaitial-developer-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spaitial.ai/api/getting-started
- group: company
  title: ''
  type: Blog
  url: https://spaitial.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spaitial-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.spaitial.ai/api/credits-billing
- group: start
  title: ''
  type: SignUp
  url: https://developers.spaitial.ai
- group: start
  title: ''
  type: Login
  url: https://app.spaitial.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spaitial.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spaitial.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@spaitial.ai
- group: other
  title: ''
  type: X
  url: https://x.com/SpAItial_AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spaitial-ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.spaitial.ai/overview/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spaitial-ai-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spaitial-ai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spaitial-ai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spaitial-ai-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spaitial-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spaitial-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spaitial-ai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/spaitial-ai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spaitial-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spaitial-ai-plans.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/spaitial-ai-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spaitial-ai-webhooks-asyncapi.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spaitial-ai-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spaitial-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spaitial-ai-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/spaitial-ai-developer-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: SpAItial is a frontier AI lab building physically-grounded world models. Its Echo model turns a single image, a 360-degree panorama, or a text prompt into a persistent, explorable 3D Gaussian Splat world. The SpAItial Developer API is a REST interface for generating, editing, exporting, and downloading these 3D worlds programmatically. Generation is asynchronous (submit a job, then poll or receive a webhook), authenticated with bearer API keys carrying explicit scopes, metered in credits, protected by per-key rate limits and an Idempotency-Key contract, and fully agent-ready through a hosted Model Context Protocol (MCP) server and a published Agent Skill.
image: https://spaitial.ai/og-image-default.png
layout: provider
mcp_servers:
- description: ''
  name: spaitial-ai-mcp.yml
  slug: spaitial-ai-mcpyml
modified: '2026-07-21'
name: SpAItial
nav: Providers
network: true
overview: 'SpAItial publishes 4 APIs on the [APIs.io](https://apis.io/) network, including files API, models API, panoramas API, and 1 more. Tagged areas include Company, World Models, Spatial AI, 3D World Generation, and Gaussian Splatting.


  The SpAItial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SpAItial''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Spaitial Ai Plans
  plan_count: 4
  slug: spaitial-ai-plans
random_paper: 14
rate_limits:
- limit_count: 0
  name: Spaitial Ai Rate Limits
  slug: spaitial-ai-rate-limits
score:
  band: developing
  composite: 58.7
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 59.7
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 58.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Spaitial Ai Authentication
  slug: spaitial-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spaitial Ai Domain Security
  slug: spaitial-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spaitial-ai
tags:
- Company
- World Models
- Spatial AI
- 3D World Generation
- Gaussian Splatting
- Generative AI
- Developer API
- MCP
- Artificial Intelligence
- 3D
website: https://developers.spaitial.ai
---
