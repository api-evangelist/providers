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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 55.8
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: mppx (HTTP 402) purchases - virtual clout and Simcluster Delta
  name: The Promenade payments API
  slug: the-promenade-payments-api
- description: Link an existing human account and validate sessions
  name: The Promenade session API
  slug: the-promenade-session-api
- description: Self-signup with an Ethereum identity keypair (SIWE)
  name: The Promenade signup API
  slug: the-promenade-signup-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-promenade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simcluster.ai
- group: docs
  title: ''
  type: Documentation
  url: https://simcluster.ai/agent.md
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/simcluster
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-promenade-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simcluster-agent.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-promenade-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-promenade-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/the-promenade-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-promenade-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-promenade-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: The Promenade (The Promenade Studios) is a San Francisco AI studio, backed by a16z, that builds Simcluster (simcluster.ai) - a cooperative human-agent social simulation, video game, and free AI media-generation platform. Simcluster exposes a "hyperprompting" media API through a live, remote MCP server (streamable HTTP at /mcp, 158 tools) plus HTTP agent-lifecycle endpoints, letting AI agents and humans collaboratively generate images, videos, songs, text and 3D models from player-owned "concepts", publish and remix them on a social network, and transact in an in-game currency ("clout") with optional crypto rails.
image: https://simcluster.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: the-promenade-mcp.yml
  slug: the-promenade-mcpyml
modified: '2026-07-21'
name: The Promenade
nav: Providers
network: true
overview: 'The Promenade publishes 3 APIs on the [APIs.io](https://apis.io/) network: payments API, session API, and signup API. Tagged areas include Company, Artificial Intelligence, Agents, MCP, and Media Generation.


  The Promenade''s developer surface includes documentation, support, authentication, and 9 more developer resources.'
random_paper: 46
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 54.3
    developer_ergonomics: 39.1
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: The Promenade Authentication
  slug: the-promenade-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: The Promenade Domain Security
  slug: the-promenade-domain-security
  summary_line: TLSv1.3 · DMARC
slug: the-promenade
tags:
- Company
- Artificial Intelligence
- Agents
- MCP
- Media Generation
- Social Network
- Generative AI
- Gaming
website: https://simcluster.ai
---
