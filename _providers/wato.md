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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
  score: 24.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Wato exposes each team's reviewed memory and approved connector tools through a single remote MCP (Model Context Protocol) gateway over Streamable HTTP with OAuth. Any MCP-capable client (Claude Code,
  name: Wato MCP Gateway
  slug: wato-mcp-gateway
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.watolabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.watolabs.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.watolabs.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.watolabs.com/docs/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.watolabs.com/docs/quickstart-automation
- group: company
  title: ''
  type: Blog
  url: https://blog.watolabs.com
- group: start
  title: ''
  type: SignUp
  url: https://mesh.watolabs.com/onboarding
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.watolabs.com/docs/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.watolabs.com/tos
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wato-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wato-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wato-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wato-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wato-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wato-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wato-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/wato-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wato-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wato-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wato-plans.yml
created: '2026-07-17'
description: Wato is the control point for AI agents at work — a governed, shared AI workspace that gives teams reviewed memory, approved MCP connectors and tools, versioned skills, cloud agent sessions, triggered automations, live artifacts and dashboards, and full tool-call tracing, all exposed to Claude Code, Codex, Cursor, and any MCP-compatible client through a single remote MCP gateway. Login, SSO, and directory sync are handled by WorkOS; agents only ever see a team's reviewed memory and approved tools, never raw credentials, and every MCP call is recorded as an auditable trace. Wato is a Y Combinator (Spring 2026) company based in San Francisco.
image: https://framerusercontent.com/images/oDm7nRGsCsNtN5bMfKuMpJdKzJg.png
layout: provider
mcp_servers:
- description: ''
  name: wato-mcp.yml
  slug: wato-mcpyml
modified: '2026-07-21'
name: Wato
nav: Providers
network: true
overview: 'Wato publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Model Context Protocol, AI Agents, and Agent Governance.


  Wato''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, signup flow, pricing, and 14 more developer resources.'
plans:
- name: Wato Plans
  plan_count: 3
  slug: wato-plans
random_paper: 48
scopes:
- name: Wato Scopes
  scope_count: 4
  slug: wato-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: thin
  composite: 33.9
  delta: -1.1
  facets:
    commercial_clarity: 65.8
    contract_quality: 0.0
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 35.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wato Authentication
  slug: wato-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wato Domain Security
  slug: wato-domain-security
  summary_line: TLSv1.2 · HSTS
slug: wato
tags:
- Company
- MCP
- Model Context Protocol
- AI Agents
- Agent Governance
- Team Memory
- Connectors
- Agent Skills
- Automation
- Developer Tools
- Y Combinator
website: https://docs.watolabs.com/
---
