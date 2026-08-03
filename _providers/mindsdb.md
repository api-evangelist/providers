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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: SQL-over-HTTP query engine plus RESTful resources for projects, databases, knowledge bases, tables, views, files, jobs, and AI agents. Self-hosted by default (http://127.0.0.1:47334); MindsDB Cloud is
  name: MindsDB HTTP REST API
  slug: mindsdb-http-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindsdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mindshub.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mindshub.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindshub.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mindsdb.com/rest/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mindsdb.com/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mindsdb
- group: company
  title: ''
  type: Blog
  url: https://mindshub.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://mindshub.ai/discord
- group: commercial
  title: ''
  type: Pricing
  url: https://mindshub.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.mindshub.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mindshub.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mindshub.ai/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/mindsdb-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mindsdb-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mindsdb-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mindsdb-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/mindsdb-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mindsdb-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mindsdb-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mindsdb-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mindsdb-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.mindsdb.com
created: '2026-07-17'
description: MindsDB is an open-source (MIT) AI data platform and semantic query engine that lets AI agents securely query, transform, and act on data from any datasource using SQL. It connects to 200+ databases, applications, and vector stores, builds knowledge bases for hybrid vector + keyword search, trains and serves models, and runs open-source AI agents and automated jobs — all through a SQL-over-HTTP REST API, the MySQL wire protocol, official Python and JavaScript SDKs, and a first-party Model Context Protocol (MCP) server. The company now operates as MindsHub (mindshub.ai), a unified AI workspace where knowledge workers delegate multi-step projects to agents, all built on the MindsDB engine. Originally surfaced as a Benchmark portfolio company; enriched by the API Evangelist pipeline.
image: https://github.com/mindsdb.png
layout: provider
mcp_servers:
- description: ''
  name: mindsdb-mcp.yml
  slug: mindsdb-mcpyml
modified: '2026-07-20'
name: MindsDB
nav: Providers
network: true
overview: 'MindsDB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, AI Agents, and Data.


  MindsDB''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 16 more developer resources.'
random_paper: 72
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 35.8
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Mindsdb Authentication
  slug: mindsdb-authentication
  summary_line: none/session/oauth2 · 3 schemes
- kind: domain-security
  name: Mindsdb Domain Security
  slug: mindsdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mindsdb
tags:
- Company
- Artificial Intelligence
- Machine Learning
- AI Agents
- Data
- Database
- SQL
- Knowledge Base
- MCP
- Open Source
website: https://mindshub.ai
---
