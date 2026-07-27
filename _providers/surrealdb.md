---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The SurrealDB HTTP REST API provides stateless access to SurrealDB instances over standard HTTP. It supports CRUD operations on tables and records, SurrealQL query execution via POST /sql, GraphQL que
  name: SurrealDB HTTP REST API
  slug: http-api
- description: SurrealMCP exposes SurrealDB database operations, agent memory, and cloud management as structured tool calls over the Model Context Protocol. It enables MCP-compatible AI clients such as Claude, Curs
  name: SurrealDB MCP Server
  slug: mcp-server
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/surrealdb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/surrealdb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surrealdb-domain-security.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/surrealdb-context.jsonld
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: company
  title: ''
  type: Website
  url: https://surrealdb.com
- group: docs
  title: ''
  type: Documentation
  url: https://surrealdb.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/surrealdb
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/surrealdb
- group: company
  title: ''
  type: Blog
  url: https://surrealdb.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://surrealdb.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.surrealdb.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://surrealdb.com/releases
- group: other
  title: ''
  type: X
  url: https://x.com/SurrealDB
- group: commercial
  title: ''
  type: Plans
  url: plans/surrealdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/surrealdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/surrealdb-finops.yml
created: '2026-06-12'
description: SurrealDB is a multi-model database that unifies documents, graphs, vectors, time-series, full-text search, and relational data within a single ACID transaction framework. It exposes a native HTTP REST API and supports SurrealQL, a powerful query language designed for multi-model data access. The platform includes built-in authentication with JWT tokens, row-level security, and live query subscriptions for real-time applications. SurrealDB Cloud provides a managed hosting option with usage-based pricing, while the open-source engine can be self-hosted. The database also ships a Model Context Protocol (MCP) server enabling AI agents and tools such as Claude, Cursor, and VS Code to query and manage data directly.
finops:
- name: Surrealdb Finops
  service_category: Database
  slug: surrealdb-finops
graphqls:
- description: SurrealDB exposes an experimental GraphQL interface that dynamically generates a complete schema from your database's table definitions, field types, custom functions, and access definitions. Enabling
  name: SurrealDB GraphQL API
  slug: surrealdb-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surrealdb.png
jsonld:
- class_count: 0
  name: Surrealdb Context
  property_count: 34
  slug: surrealdb-context
layout: provider
modified: '2026-06-12'
name: SurrealDB
nav: Providers
network: true
overview: 'SurrealDB publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Multi-Model, Graph Database, Document Database, and Vector Database.


  The SurrealDB catalog on APIs.io includes 1 JSON-LD context.


  SurrealDB''s developer surface includes documentation, engineering blog, pricing, changelog, and 13 more developer resources.'
plans:
- name: Surrealdb Plans Pricing
  plan_count: 3
  slug: surrealdb-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Surrealdb Rate Limits
  slug: surrealdb-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 34.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/surrealdb/refs/heads/main/screenshots/surrealdb-2026-06-20T194741.png
security:
- kind: domain-security
  name: Surrealdb Domain Security
  slug: surrealdb-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Surrealdb Vulnerability Disclosure
  slug: surrealdb-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Surrealdb Trust Center
  slug: surrealdb-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: surrealdb
tags:
- Database
- Multi-Model
- Graph Database
- Document Database
- Vector Database
- Time-Series
- SurrealQL
- AI
- MCP
website: https://surrealdb.com
---
