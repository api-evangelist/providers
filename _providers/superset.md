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
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 29.8
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'Hosted REST + MCP surface (api.superset.sh, v2) that lets agents and automation manage workspaces, tasks, agents, terminals, automations, projects, and hosts. Authenticated with OAuth 2.1 or API keys '
  name: Superset Agent API
  slug: superset-agent-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superset-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://superset.sh
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.superset.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superset.sh
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.superset.sh
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superset-sh
- group: company
  title: ''
  type: Blog
  url: https://superset.sh/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://superset.sh/pricing
- group: start
  title: ''
  type: SignUp
  url: https://superset.sh/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superset.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superset.sh/privacy
- group: operate
  title: ''
  type: Support
  url: https://superset.sh/community
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superset.sh
- group: operate
  title: ''
  type: ChangeLog
  url: https://superset.sh/changelog
- group: build
  title: ''
  type: Packages
  url: packages/superset-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/superset-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/superset-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superset-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superset-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/superset-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/superset-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superset-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superset-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superset-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/superset-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superset-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Superset is an open-source, terminal-first code editor built for the AI-agent era, letting engineers run 100+ CLI coding agents (Claude Code, Cursor, OpenCode, Gemini, Copilot, Mistral Vibe and more) in parallel, each isolated in its own Git worktree so work never collides. The desktop app pairs with a standalone CLI, a TypeScript SDK (@superset_sh/sdk), and a hosted MCP server at api.superset.sh so agents and automation can create and manage workspaces, tasks, terminals, and scheduled automations programmatically. Backed by Y Combinator (Spring 2026), Superset reached 12k+ GitHub stars and #1 on Product Hunt shortly after launch. Features include remote workspaces on any network-connected device, an infinite-scroll diff viewer, port forwarding, an in-app browser, IDE integration, and cross-device OAuth login.'
image: https://avatars.githubusercontent.com/superset-sh
layout: provider
mcp_servers:
- description: ''
  name: superset-mcp.yml
  slug: superset-mcpyml
modified: '2026-07-21'
name: Superset
nav: Providers
network: true
overview: 'Superset publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, AI Agents, Code Editor, and IDE.


  Superset''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 20 more developer resources.'
random_paper: 24
scopes:
- name: Superset Scopes
  scope_count: 4
  slug: superset-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Superset Authentication
  slug: superset-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Superset Domain Security
  slug: superset-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: superset
tags:
- Company
- Developer Tools
- AI Agents
- Code Editor
- IDE
- Coding Agents
- MCP
- CLI
- SDK
- Git Worktrees
- Automation
- Y Combinator
website: https://superset.sh
---
