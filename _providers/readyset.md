---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    well_known_catalog: true
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://readyset.io
- group: docs
  title: ''
  type: Documentation
  url: https://readyset.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://readyset.io/docs/cache/install-rs
- group: company
  title: ''
  type: Blog
  url: https://readyset.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://readyset.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://readyset.cloud
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/readysettech
- group: operate
  title: ''
  type: Support
  url: https://github.com/readysettech/readyset/issues
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://readyset.io/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/readysettech/readyset/releases
- group: agent
  title: ''
  type: MCPServer
  url: mcp/readyset-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/readyset-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/readyset-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/readyset-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/readyset-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/readyset-api-catalog.json
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/readyset-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/readyset-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/readyset-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Readyset is a realtime SQL caching engine for Postgres and MySQL. It sits between applications and the database as a wire-compatible proxy, automatically caching the results of costly SELECT queries and keeping them up to date from the database replication stream with no application code changes or manual invalidation. Written in Rust and available as open source (BSL 1.1), a self-managed Private deployment, and a fully managed Readyset Cloud offering on AWS, it also ships Readyset AI — an MCP server plus the rdst diagnostics CLI — so AI assistants and developers can inspect caches, analyze slow queries, and deploy caches directly. Backed by Amplify Partners and Index Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/readyset.png
layout: provider
mcp_servers:
- description: 'Official Readyset MCP server ("Readyset AI"). Exposes a running Readyset caching engine over the Model Context Protocol so AI assistants can inspect caches, query performance, and replication health, '
  name: Readyset MCP server (Readyset AI)
  slug: readyset-mcp-server-readyset-ai
modified: '2026-07-20'
name: ReadySet
nav: Providers
network: true
overview: 'ReadySet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Database, Caching, and SQL.


  ReadySet''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 13 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 22.3
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 22.3
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Readyset Domain Security
  slug: readyset-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: readyset
tags:
- Company
- Developer Tools
- Database
- Caching
- SQL
- PostgreSQL
- MySQL
- Performance
- MCP
website: https://readyset.io
---
