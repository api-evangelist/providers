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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Orgs API from Rill Data — 17 operation(s) for orgs.
  name: Rill Data Orgs API
  slug: rill-data-orgs-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.rilldata.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rilldata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rilldata.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rilldata.com/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rilldata.com/home/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.rilldata.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rilldata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ui.rilldata.com
- group: start
  title: ''
  type: Login
  url: https://ui.rilldata.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rilldata.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/2ubRfjC7Rh
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rilldata
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rilldata.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rill-data-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rill-data-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/rill-data-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/rill-data-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rill-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rill-data-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rill-data-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rill-data-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rill-data-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.rilldata.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/rill-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rill-data-domain-security.yml
created: '2026-07-17'
description: Rill Data builds Rill, an operational business-intelligence tool for fast, exploratory dashboards on large event and time-series data. Developers connect data sources, model last-mile transformations in SQL/YAML, define a governed metrics layer, and publish interactive dashboards — locally with the free Rill Developer app or hosted on Rill Cloud. Rill is open source (Go/TypeScript) and exposes a Protobuf-defined admin API over gRPC/Connect and JSON/HTTP at api.rilldata.com, a first-party CLI, embeddable dashboards, custom data APIs, and an official hosted Model Context Protocol (MCP) server that lets LLMs query its governed metrics views. Rill Data is a portfolio company of Bloomberg Beta, DCVC, and Sierra Ventures.
image: https://www.rilldata.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: rill-data-mcp.yml
  slug: rill-data-mcpyml
modified: '2026-07-21'
name: Rill Data
nav: Providers
network: true
overview: 'Rill Data publishes 1 API on the [APIs.io](https://apis.io/) network: Orgs API. Tagged areas include Company, Analytics, Business Intelligence, Dashboards, and Metrics.


  Rill Data''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 19 more developer resources.'
random_paper: 21
scopes:
- name: Rill Data Scopes
  scope_count: 1
  slug: rill-data-scopes
  summary_line: 1 scope · authorizationCode/deviceCode
score:
  band: developing
  composite: 46.8
  delta: 0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 31.4
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 46.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rill Data Authentication
  slug: rill-data-authentication
  summary_line: http-bearer/oauth2 · 2 schemes
- kind: domain-security
  name: Rill Data Domain Security
  slug: rill-data-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Rill Data Trust Center
  slug: rill-data-trust-center
  summary_line: SOC 2
slug: rill-data
tags:
- Company
- Analytics
- Business Intelligence
- Dashboards
- Metrics
- Data
- OLAP
- Open Source
- Developer Tools
website: https://www.rilldata.com
---
