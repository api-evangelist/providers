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
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Genspark's hosted (remote) Model Context Protocol server, exposing Genspark's AI agent tools, resources, and prompts to MCP-capable clients over HTTP under OAuth 2.1.
  name: Genspark MCP Server
  slug: genspark-mcp-server
artifact_total: 5
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/genspark-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://www.genspark.ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/genspark-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/genspark-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/genspark-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/genspark-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/genspark-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genspark-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genspark-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.genspark.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.genspark.ai/helpcenter
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.genspark.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.genspark.ai/privacy
created: '2026-07-17'
description: Genspark is an all-in-one AI workspace and autonomous "Super Agent" platform that plans and executes multi-step tasks on a user's behalf. It bundles a suite of AI agent tools — deep research, AI slides, AI sheets, AI docs, AI chat, a "Call For Me" voice agent, and a built-in AI browser — into a single natural-language workspace, alongside companion products such as Genspark Claw, Speakly, GenClipboard, and GenTerminal and native iOS and Android apps. For developers and agents, Genspark operates a hosted, remote Model Context Protocol (MCP) server at /api/mcp that exposes its tools, resources, and prompts over HTTP, gated by OAuth 2.1 (authorization_code with PKCE, refresh tokens, and dynamic client registration). Genspark is backed by Emergence Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genspark.png
layout: provider
mcp_servers:
- description: ''
  name: genspark-mcp.yml
  slug: genspark-mcpyml
modified: '2026-07-19'
name: Genspark
nav: Providers
network: true
overview: 'Genspark publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Artificial Intelligence, AI Agents, and MCP.


  Genspark''s developer surface includes authentication, engineering blog, support, and 10 more developer resources.'
random_paper: 47
scopes:
- name: Genspark Scopes
  scope_count: 4
  slug: genspark-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 19.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genspark/refs/heads/main/screenshots/genspark-2026-07-25T215631.png
security:
- kind: authentication
  name: Genspark Authentication
  slug: genspark-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Genspark Domain Security
  slug: genspark-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: genspark
tags:
- Company
- Ai
- Artificial Intelligence
- AI Agents
- MCP
- Model Context Protocol
- Productivity
- Automation
- Search
- Workspace
website: https://www.genspark.ai
---
