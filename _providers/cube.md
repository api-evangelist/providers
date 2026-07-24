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
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: GraphQL API that enables Cube to deliver data over HTTP to GraphQL-enabled data applications. Exposes measures, dimensions, segments, and filters defined in the Cube semantic layer for use in front-en
  name: Cube GraphQL API
  slug: graphql-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cube-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cube-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cube.dev
- group: docs
  title: ''
  type: Documentation
  url: https://cube.dev/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cube-dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cube-js
- group: commercial
  title: ''
  type: Pricing
  url: https://cube.dev/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/cube-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cube-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/cube-finops.md
- group: company
  title: ''
  type: Blog
  url: https://cube.dev/blog
created: 2026-06-14
description: Semantic layer and headless BI platform with a GraphQL API for querying measures, dimensions, and segments across any SQL database or data warehouse.
graphqls:
- description: Cube exposes a GraphQL API that sits on top of its semantic layer, allowing front-end applications and embedded analytics tools to query measures, dimensions, and time dimensions defined across any co
  name: Cube GraphQL API
  slug: cube-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cube.png
layout: provider
modified: 2026-06-14
name: Cube
nav: Providers
network: true
overview: 'Cube publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Semantic Layer, Business Intelligence, Embedded Analytics, and Data Warehouse.


  Cube''s developer surface includes documentation, pricing, engineering blog, and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 14.5
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cube/refs/heads/main/screenshots/cube-2026-06-20T175326.png
security:
- kind: domain-security
  name: Cube Domain Security
  slug: cube-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cube Trust Center
  slug: cube-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: cube
tags:
- GraphQL
- Semantic Layer
- Business Intelligence
- Embedded Analytics
- Data Warehouse
website: https://cube.dev
---
