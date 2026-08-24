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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.7
  scored_at: '2026-08-24'
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
artifact_total: 15
asyncapis:
- description: Webhook event surface for the SpAItial Developer API. Set webhook.url on a POST /v1/worlds request to receive an HTTPS callback on terminal state. Deliveries carry an HMAC-SHA256 signature (X-Spaitial
  name: SpAItial Developer API Webhooks
  slug: spaitial-ai-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SpAItial Developer files API
  slug: open-spaitial-ai-files-api
- collection_type: open
  name: SpAItial Developer files models API
  slug: open-spaitial-ai-models-api
- collection_type: open
  name: SpAItial Developer files panoramas API
  slug: open-spaitial-ai-panoramas-api
- collection_type: open
  name: SpAItial Developer files worlds API
  slug: open-spaitial-ai-worlds-api
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
  name: SpAItial MCP Server
  slug: spaitial-mcp-server
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
random_paper: 10
rate_limits:
- limit_count: 0
  name: Spaitial Ai Rate Limits
  slug: spaitial-ai-rate-limits
score:
  band: strong
  composite: 56.4
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 57.3
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 56.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spaitial-ai/refs/heads/main/screenshots/spaitial-ai-2026-08-17T125411.png
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
