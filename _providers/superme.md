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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-01'
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
  name: SuperMe MCP Server
  slug: superme-mcp-server
modified: '2026-07-21'
name: SuperMe
nav: Providers
network: true
overview: 'SuperMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Professional Network, and Expert Knowledge.


  SuperMe''s developer surface includes authentication, signup flow, support, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- MCP
website: https://superme.ai
---
