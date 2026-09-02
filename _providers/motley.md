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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: SLayer is Motley's open-core, agent-first semantic layer and query engine. Agents and applications describe measures, dimensions, and filters and SLayer compiles and runs the correct SQL across many d
  name: Motley SLayer Semantic Layer
  slug: motley-slayer-semantic-layer
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/MotleyAI/slayer/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/MotleyAI/slayer/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/MotleyAI/slayer/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/MotleyAI/slayer/blob/main/LICENSE
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
- description: SLayer runs as a Model Context Protocol (MCP) server so AI agents (Claude, Cursor, etc.) can discover and query data conversationally. It exposes the same tools across two transports.
  name: Motley MCP Server
  slug: motley-mcp-server
modified: '2026-07-20'
name: Motley
nav: Providers
network: true
overview: 'Motley publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semantic Layer, Business Intelligence, Analytics, and AI Agents.


  Motley''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 25 more developer resources.'
random_paper: 15
scopes:
- name: Motley Scopes
  scope_count: 7
  slug: motley-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 50.0
  previous_composite: 35.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/motley/refs/heads/main/screenshots/motley-2026-08-07T184333.png
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
