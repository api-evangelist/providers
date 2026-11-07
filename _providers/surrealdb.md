---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.6
  scored_at: '2026-11-06'
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
  href: https://artifacts.apis.io/surrealdb/security/surrealdb-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/surrealdb-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/surrealdb/security/surrealdb-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/surrealdb-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/surrealdb/security/surrealdb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surrealdb-domain-security.yml
- group: design
  href: https://artifacts.apis.io/surrealdb/json-ld/surrealdb-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/surrealdb-context.jsonld
- group: company
  href: https://artifacts.apis.io/surrealdb/blogs/blogs.json
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
  href: https://artifacts.apis.io/surrealdb/plans/surrealdb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/surrealdb-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/surrealdb/rate-limits/surrealdb-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/surrealdb-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/surrealdb/finops/surrealdb-finops.yml
  title: ''
  type: FinOps
  url: finops/surrealdb-finops.yml
created: '2026-06-12'
description: SurrealDB is a multi-model database that unifies documents, graphs, vectors, time-series, full-text search, and relational data within a single ACID transaction framework. It exposes a native HTTP REST API and supports SurrealQL, a powerful query language designed for multi-model data access. The platform includes built-in authentication with JWT tokens, row-level security, and live query subscriptions for real-time applications. SurrealDB Cloud provides a managed hosting option with usage-based pricing, while the open-source engine can be self-hosted. The database also ships a Model Context Protocol (MCP) server enabling AI agents and tools such as Claude, Cursor, and VS Code to query and manage data directly.
finops:
- has_sources: true
  method: generated
  name: Surrealdb Finops
  primary_unit: ''
  service_category: Database
  slug: surrealdb-finops
  template: false
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
overview: 'SurrealDB is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Multi-Model, Graph Database, Document Database, and Vector Search.


  The SurrealDB catalog on APIs.io includes 1 JSON-LD context.


  SurrealDB''s developer surface includes documentation, engineering blog, pricing, changelog, and 13 more developer resources.'
plans:
- name: Surrealdb Plans Pricing
  plan_count: 3
  slug: surrealdb-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Surrealdb Rate Limits
  slug: surrealdb-rate-limits
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 59.0
    catalog_earned_first_party: 12.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.5
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 43.6
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 42.1
  previous_composite: 29.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/surrealdb/surrealdb-2026-06-20T194741.png
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
- Vector Search
- Time Series
- SurrealQL
- Artificial Intelligence
- MCP
website: https://surrealdb.com
---
