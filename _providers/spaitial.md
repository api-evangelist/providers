---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Spaitial Agentic Access
  operation_count: 18
  slug: spaitial-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 4
apis:
- description: File upload endpoints
  name: SpAItial files API
  slug: spaitial-files-api
- description: Model discovery endpoints
  name: SpAItial models API
  slug: spaitial-models-api
- description: The panoramas API from SpAItial — 4 operation(s) for panoramas.
  name: SpAItial panoramas API
  slug: spaitial-panoramas-api
- description: World generation endpoints
  name: SpAItial worlds API
  slug: spaitial-worlds-api
artifact_total: 15
asyncapis:
- description: Webhook event surface for the SpAItial Developer API. Set webhook.url on POST /v1/worlds to receive an HTTPS callback when a world-generation job (or a mesh export) reaches a terminal state. Deliverie
  name: SpAItial Developer API Webhooks
  slug: spaitial-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SpAItial Developer files API
  slug: open-spaitial-files-api
- collection_type: open
  name: SpAItial Developer files models API
  slug: open-spaitial-models-api
- collection_type: open
  name: SpAItial Developer files panoramas API
  slug: open-spaitial-panoramas-api
- collection_type: open
  name: SpAItial Developer files worlds API
  slug: open-spaitial-worlds-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/spaitial-developer-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spaitial-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaitial-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spaitial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spaitial-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spaitial-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/spaitial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spaitial-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spaitial-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spaitial-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spaitial-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spaitial-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spaitial-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/spaitial-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spaitial-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spaitial-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/spaitial-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spaitial-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.spaitial.ai/mcp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.spaitial.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spaitial.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spaitial.ai/api/reference/spaitial-developer-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spaitial.ai/api/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.spaitial.ai/api/credits-billing
- group: company
  title: ''
  type: Blog
  url: https://spaitial.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://developers.spaitial.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spaitial.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spaitial.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spaitial-ai
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.spaitial.ai/overview/release-notes
created: '2026-07-17'
description: SpAItial (SpAItial Ltd, London) is a frontier spatial-AI lab building Echo, a world-model family that turns text prompts, images, and 360-degree panoramas into persistent, explorable 3D Gaussian Splat worlds (SPZ/SOG, plus mesh exports). SpAItial ships a public REST Developer API at api.spaitial.ai for programmatic world generation, panorama editing, file upload, and mesh export, an official hosted Model Context Protocol (MCP) server for AI agents, and an installable Agent Skill for coding assistants. It is a portfolio company of Speedinvest. This profile was enriched from the live OpenAPI spec, docs, llms.txt, and MCP server card.
image: https://spaitial.ai/og-image-default.png
layout: provider
mcp_servers:
- description: Official hosted, remote streamable-HTTP MCP server; 15 tools mapping 1:1 to the Developer API, BYOK (bearer or oauth2). Detail in mcp/spaitial-mcp.yml.
  name: SpAItial MCP Server
  slug: spaitial-mcp-server
modified: '2026-07-21'
name: SpAItial
nav: Providers
network: true
overview: 'SpAItial publishes 4 APIs on the [APIs.io](https://apis.io/) network, including files API, models API, panoramas API, and 1 more. Tagged areas include Company, Spatial AI, World Models, 3D, and Gaussian Splatting.


  The SpAItial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SpAItial''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, pricing, and 24 more developer resources.'
random_paper: 110
scopes:
- name: Spaitial Scopes
  scope_count: 0
  slug: spaitial-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.8
  delta: -1.3
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 57.3
    developer_ergonomics: 61.3
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spaitial/refs/heads/main/screenshots/spaitial-2026-08-17T125348.png
security:
- kind: authentication
  name: Spaitial Authentication
  slug: spaitial-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spaitial Domain Security
  slug: spaitial-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spaitial
tags:
- Company
- Spatial AI
- World Models
- 3D
- Gaussian Splatting
- Generative AI
- Developer API
- MCP
website: https://developers.spaitial.ai
---
