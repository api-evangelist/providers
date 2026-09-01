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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Korso-AI/Shepherd/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Korso-AI/Shepherd/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/korso-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/korso-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/korso-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/korso-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/korso-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/korso-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/korso-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/korso-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/korso-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/korso-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Korso-AI/Shepherd/blob/main/CHANGELOG.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/korso-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/korso-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Korso-AI/Shepherd/blob/main/SECURITY.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/korso-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://korsoai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://korsoai.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://korsoai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://korsoai.com/docs/mcp-tools/work
- group: start
  title: ''
  type: GettingStarted
  url: https://korsoai.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:support@korsoai.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Korso-AI
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Korso-AI/Shepherd
- group: start
  title: ''
  type: SignUp
  url: https://korsoai.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://korsoai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://korsoai.com/privacy
created: '2026-07-17'
description: 'Korso is a Los Angeles based company (Y Combinator Spring 2026) building tooling for the next generation of software. Its flagship open source product, Shepherd, is a coordination layer for AI coding agents: a Fastify + Postgres hub, a published stdio Model Context Protocol server (@korso/shepherd on npm), a shared zod wire contract, and a React dashboard (@korso/shepherd-ui). Shepherd lets a fleet of agents working across sessions, worktrees, and team members claim files, release claims, broadcast announcements, and refresh a shared workspace landscape so they stop producing merge conflicts and overwriting each other. The MCP surface exposes seven documented tools (work, done, announce, sync, link, unlink, decline). Korso also runs a beta Trading API over its own quantitative trading desk and Korso Research, an AI-native research workspace.'
image: https://korsoai.com/docs/favicon.svg
layout: provider
mcp_servers:
- description: Shepherd is a coordination layer for AI coding agents. The MCP server is a thin stdio client that forwards agent tool calls to a Shepherd hub (Fastify + Postgres), letting a fleet of agents across ses
  name: Shepherd MCP server
  slug: shepherd-mcp-server
modified: '2026-07-19'
name: Korso
nav: Providers
network: true
overview: 'Korso is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, MCP, and Developer Tools.


  Korso''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, signup flow, and 22 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 63.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 60.0
  previous_composite: 31.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/korso/refs/heads/main/screenshots/korso-2026-07-25T224225.png
security:
- kind: authentication
  name: Korso Authentication
  slug: korso-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Korso Domain Security
  slug: korso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Korso Vulnerability Disclosure
  slug: korso-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: korso
tags:
- Company
- Artificial Intelligence
- Agents
- MCP
- Developer Tools
- Open-Source
- Agent Coordination
- Y Combinator
website: https://korsoai.com/
---
