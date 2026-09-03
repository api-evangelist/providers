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
  score: 28.2
  scored_at: '2026-09-03'
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
  name: Wato MCP Server
  slug: wato-mcp-server
modified: '2026-07-21'
name: Wato
nav: Providers
network: true
overview: 'Wato publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, AI Agents, Agent Governance, and Team Memory.


  Wato''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, signup flow, pricing, and 14 more developer resources.'
plans:
- name: Wato Plans
  plan_count: 3
  slug: wato-plans
random_paper: 2
scopes:
- name: Wato Scopes
  scope_count: 4
  slug: wato-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 29.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wato/refs/heads/main/screenshots/wato-2026-09-02T170454.png
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
