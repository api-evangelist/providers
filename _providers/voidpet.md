---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 47.1
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The Discovery API from Voidpet — 1 operation(s) for discovery.
  name: Voidpet Discovery API
  slug: voidpet-discovery-api
- description: The Health API from Voidpet — 1 operation(s) for health.
  name: Voidpet Health API
  slug: voidpet-health-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voidpet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voidpet-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voidpet-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/voidpet-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voidpet-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/voidpet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voidpet-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://voidpet.com/.well-known/api-docs.md
- group: docs
  title: ''
  type: APIReference
  url: https://voidpet.com/.well-known/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://voidpet.com/o/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voidpet.com/o/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voidpet.com/o/privacy
created: '2026-07-17'
description: Voidpet is a creative games studio behind emotion-inspired games, stories, characters, and community — including Voidpet Dungeon, a turn-based roguelite RPG about befriending and battling emotion-inspired creatures, and Voidpet Garden, a mental-health companion game for collecting emotions and practicing self care. Beyond the games, Voidpet publishes a small, public, read-only Discovery API (OpenAPI 3.1) plus a hosted Model Context Protocol server and a packaged Agent Skill so agents can discover its public products, pages, and legal documents. The discovery surface exposes no accounts, game state, or authenticated actions — it is agent-facing metadata only.
image: https://voidpet.com/ogimage.png
layout: provider
mcp_servers:
- description: ''
  name: voidpet-mcp.yml
  slug: voidpet-mcpyml
modified: '2026-07-21'
name: Voidpet
nav: Providers
network: true
overview: 'Voidpet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Discovery API and Health API. Tagged areas include Company, Games, Gaming, Mental Health, and Wellness.


  Voidpet''s developer surface includes authentication, documentation, API reference, engineering blog, and 9 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 41.6
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 32.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Voidpet Authentication
  slug: voidpet-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Voidpet Domain Security
  slug: voidpet-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: voidpet
tags:
- Company
- Games
- Gaming
- Mental Health
- Wellness
- Discovery
- Agents
- MCP
- Read Only
---
