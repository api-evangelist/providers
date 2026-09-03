---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: Executes EdgeQL queries over HTTP against a Gel/EdgeDB instance. Supports GET and POST requests with query, variables, globals, and config fields. Authentication uses HTTP Basic (password), Bearer tok
  name: EdgeDB EdgeQL HTTP API
  slug: edgeql-http-api
- description: 'Provides a GraphQL endpoint for querying an EdgeDB/Gel instance, supporting queries, mutations, and introspection. Enabled via the graphql extension in the schema. Authentication uses the same secret '
  name: EdgeDB GraphQL API
  slug: graphql-api
- description: Managed cloud database service for provisioning and operating EdgeDB/Gel instances. Accessible via the Gel CLI, web dashboard at cloud.geldata.com, and platform integrations. Supports secret key creat
  name: EdgeDB Cloud Management
  slug: cloud-management
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edgedb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.geldata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.geldata.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geldata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geldata
- group: company
  title: ''
  type: Blog
  url: https://www.geldata.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.geldata.com/pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/geldata
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.geldata.com/updates
- group: commercial
  title: ''
  type: Plans
  url: plans/edgedb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edgedb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/edgedb-finops.yml
created: '2026-06-12'
description: EdgeDB (rebranded as Gel in 2025) is an open-source object-relational database built on top of PostgreSQL that combines a modern graph-relational data model with a powerful query language called EdgeQL. It provides an HTTP-based EdgeQL query API and a GraphQL API, allowing developers to query their database over standard HTTP using bearer token authentication. EdgeDB Cloud offers a fully managed hosting service with free and paid tiers, integrating with platforms such as Vercel, Netlify, Fly.io, and Railway. Client libraries are available for TypeScript, Python, Go, Dart, Rust, .NET, and Java.
finops:
- name: Edgedb Finops
  service_category: Database
  slug: edgedb-finops
graphqls:
- description: EdgeDB (rebranded as Gel in 2025) exposes a GraphQL API that automatically reflects your database schema as a full CRUD API. Every object type, computed property, link, and alias defined in your EdgeD
  name: EdgeDB GraphQL API
  slug: edgedb-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edgedb.png
jsonld:
- class_count: 0
  name: Edgedb Context
  property_count: 10
  slug: edgedb-context
layout: provider
modified: '2026-06-12'
name: EdgeDB
nav: Providers
network: true
overview: 'EdgeDB publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, PostgreSQL, Graph Database, Object-Relational, and EdgeQL.


  The EdgeDB catalog on APIs.io includes 1 JSON-LD context.


  EdgeDB''s developer surface includes documentation, engineering blog, pricing, changelog, and 8 more developer resources.'
plans:
- name: Edgedb Plans Pricing
  plan_count: 3
  slug: edgedb-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Edgedb Rate Limits
  slug: edgedb-rate-limits
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 44.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 45.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 36.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edgedb/refs/heads/main/screenshots/edgedb-2026-06-20T180552.png
security:
- kind: domain-security
  name: Edgedb Domain Security
  slug: edgedb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edgedb
tags:
- Database
- PostgreSQL
- Graph Database
- Object-Relational
- EdgeQL
- GraphQL
- HTTP API
- Cloud Database
website: https://www.geldata.com
---
