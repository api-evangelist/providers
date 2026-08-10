---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 9
  human_in_the_loop: 3
  name: Monid Agentic Access
  operation_count: 33
  slug: monid-agentic-access
  summary_line: 33 operations · 9 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The Monid HTTP API lets developers and AI agents discover data endpoints with natural language, inspect their details, run them, and manage runs, wallet balance, spend controls (budgets and run-caps),
  name: Monid API
  slug: monid-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monid-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/monid-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monid-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/monid-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/monid-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/monid-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/monid-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monid-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monid-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.monid.ai
- group: design
  title: ''
  type: DataModel
  url: data-model/monid-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/monid-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/monid-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/monid-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monid-llms.txt
- group: company
  title: ''
  type: Website
  url: https://monid.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://monid.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://monid.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://monid.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://monid.ai/docs/guide/quickstart-api.md
- group: company
  title: ''
  type: Blog
  url: https://monid.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monid-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.monid.ai
created: 2026-07-23
description: Monid is a San Francisco-based data-access and agent-tool integration platform that gives developers and AI agents on-demand, pay-per-use access to hundreds of web data endpoints and 1,300+ tools across 13+ providers (Semrush, Apollo, ElevenLabs, web scrapers, and more) through a single integration. Agents discover, inspect, compare, and execute tools at runtime and pay only for actual usage, with a unified balance and no per-tool API key management or subscriptions. Monid exposes its catalog through four connection methods — an MCP (Model Context Protocol) server for Claude and other AI assistants, a Skill integration for Claude Code and Cursor, a CLI for shell access, and an HTTP API for programmatic integration — with OAuth, proxy, and master API key options for embedded use.
layout: provider
mcp_servers:
- description: ''
  name: monid-mcp.yml
  slug: monid-mcpyml
modified: 2026-07-23
name: Monid
nav: Providers
network: true
overview: 'Monid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agents, MCP, Tools, and Data.


  Monid''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, engineering blog, signup flow, and 18 more developer resources.'
random_paper: 71
scopes:
- name: Monid Scopes
  scope_count: 5
  slug: monid-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 44.9
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 58.9
    developer_ergonomics: 69.6
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/screenshots/monid-2026-08-07T184201.png
security:
- kind: authentication
  name: Monid Authentication
  slug: monid-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Monid Domain Security
  slug: monid-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: monid
tags:
- Company
- Agents
- MCP
- Tools
- Data
- API Marketplace
website: https://monid.ai
---
