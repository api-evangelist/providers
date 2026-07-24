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
- description: The Specific control plane and CLI that builds, deploys and runs agent-defined infrastructure from a single specific.hcl file, spanning local development and production on Specific Cloud.
  name: Specific Platform
  slug: specific-platform
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://specific.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.specific.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.specific.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.specific.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://specific.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://specific.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.specific.dev
- group: start
  title: ''
  type: Login
  url: https://dashboard.specific.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/specific-dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://specific.dev/changelog
- group: build
  title: ''
  type: Packages
  url: packages/specific-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/specific-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/specific-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/specific-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/specific-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/specific-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/specific-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/specific-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/specific-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/specific-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/specific-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Specific is an infrastructure-as-code platform built for coding agents, positioned as "AWS for coding agents." Any coding agent (Claude Code, Cursor, Codex) defines its whole system in a single specific.hcl file — services, managed Postgres, S3-compatible object storage, Redis, real-time Postgres sync (powered by Electric), Temporal workflows, crons, secrets, volumes, custom domains, preview environments and environments — then runs it locally with `specific dev` and ships it to production with `specific deploy`. Everything is reached through the Specific CLI and a hosted docs MCP server rather than proprietary SDKs, so agents can build backends from natural-language prompts and deploy production infrastructure in minutes.
image: https://specific.dev/opengraph-image?2b9073564a4e0222
layout: provider
mcp_servers:
- description: ''
  name: specific-mcp.yml
  slug: specific-mcpyml
modified: '2026-07-21'
name: Specific
nav: Providers
network: true
overview: 'Specific publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Infrastructure as Code, Platform as a Service, and Backend as a Service.


  Specific''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, changelog, CLI, and 15 more developer resources.'
random_paper: 22
score:
  band: thin
  composite: 30.7
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 69.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Specific Authentication
  slug: specific-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Specific Domain Security
  slug: specific-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: specific
tags:
- Company
- Infrastructure
- Infrastructure as Code
- Platform as a Service
- Backend as a Service
- Coding Agents
- Deployment
- PostgreSQL
- Developer Tools
- Cloud
- CLI
- MCP
website: https://specific.dev
---
