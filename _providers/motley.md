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
    agent_skills: true
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
  score: 27.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: SLayer is Motley's open-core, agent-first semantic layer and query engine. Agents and applications describe measures, dimensions, and filters and SLayer compiles and runs the correct SQL across many d
  name: Motley SLayer Semantic Layer
  slug: motley-slayer-semantic-layer
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://motley.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.motley.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.motley.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.motley.ai/slayer/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.motley.ai/slayer/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://motley.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://motley.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.motley.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://motley.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://motley.ai/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MotleyAI
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/egWxMctHCA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usemotley/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MotleyAI/slayer
- group: build
  title: ''
  type: Packages
  url: packages/motley-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/motley-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/motley-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/motley-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/motley-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/motley-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/motley-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/motley-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/motley-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/motley-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/motley-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/motley-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motley-domain-security.yml
created: '2026-07-17'
description: 'Motley is a Zurich-based company building a governed semantic layer for AI agents and business intelligence. Its open-core product, SLayer (motley-slayer), is a lightweight, agent-first semantic layer and query engine: teams model measures, dimensions, and filters once, and SLayer generates and executes correct SQL across Postgres, MySQL, Snowflake, BigQuery, ClickHouse, DuckDB and more — exposed over MCP, a REST API, a CLI, a Python client, Apache Arrow Flight SQL, and a Postgres facade for BI tools. Motley Cloud adds the managed production layer on top: hosting, OAuth-based access control, row-level security, versioning, and a governed reporting engine that turns agent queries into reports, charts, documents, and presentations. Founded by Egor Kraev (ex-Head of AI at Wise), Artemy Belousov, and Yann Ranchere; backed by Seedcamp.'
image: https://raw.githubusercontent.com/MotleyAI/slayer/main/docs/images/slayer-hero.png
layout: provider
mcp_servers:
- description: ''
  name: motley-mcp.yml
  slug: motley-mcpyml
modified: '2026-07-20'
name: Motley
nav: Providers
network: true
overview: 'Motley publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semantic Layer, Business Intelligence, Analytics, and AI Agents.


  Motley''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 21 more developer resources.'
random_paper: 50
scopes:
- name: Motley Scopes
  scope_count: 7
  slug: motley-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 38.2
  delta: -0.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 87.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 38.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Motley Authentication
  slug: motley-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Motley Domain Security
  slug: motley-domain-security
  summary_line: TLSv1.3 · DMARC
slug: motley
tags:
- Company
- Semantic Layer
- Business Intelligence
- Analytics
- AI Agents
- MCP
- SQL
- Data
- Reporting
website: https://motley.ai
---
