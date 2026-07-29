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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Official hosted, OAuth-protected Model Context Protocol server that exposes the SuperMe professional network to AI clients (Claude, ChatGPT, Cursor) over SSE / Streamable HTTP.
  name: SuperMe MCP Server
  slug: superme-mcp-server
artifact_total: 4
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superme-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superme-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/superme-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superme-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superme-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://superme.ai
- group: start
  title: ''
  type: SignUp
  url: https://superme.ai/register
- group: start
  title: ''
  type: Login
  url: https://superme.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superme.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superme.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:contact@superme.ai
created: '2026-07-17'
description: SuperMe is a professional network for the AI age that connects people with expert knowledge from real professionals instead of generic answers. It offers Work Groups (curated panels of founders and executives with AI profiles trained on their actual work), My Agent (a personal AI assistant that finds relevant experts and synthesizes their perspectives), and Group Chat (real-time discussions across multiple AI profiles on a topic). SuperMe publishes an official, OAuth-protected hosted MCP server so its network can be used directly from Claude, ChatGPT, and Cursor, with incognito mode and per-item sharing controls (public, private, team-only, or auto-indexed). Backed by Forerunner Ventures and Greylock.
image: https://superme.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: superme-mcp.yml
  slug: superme-mcpyml
modified: '2026-07-21'
name: SuperMe
nav: Providers
network: true
overview: 'SuperMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Professional Network, and Expert Knowledge.


  SuperMe''s developer surface includes authentication, signup flow, support, and 8 more developer resources.'
random_paper: 49
score:
  band: emerging
  composite: 20.3
  delta: -0.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Superme Authentication
  slug: superme-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Superme Domain Security
  slug: superme-domain-security
  summary_line: TLSv1.3 · DMARC
slug: superme
tags:
- Company
- Artificial Intelligence
- AI Agents
- Professional Network
- Expert Knowledge
- Model Context Protocol
- MCP
website: https://superme.ai
---
