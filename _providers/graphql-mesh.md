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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'GraphQL federation framework that composes any API service — REST, OpenAPI, gRPC, SOAP, OData, JSON Schema, GraphQL, and databases — into a unified, type-safe GraphQL schema with built-in transforms, '
  name: GraphQL Mesh API
  slug: api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-mesh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/mesh
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/mesh/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://the-guild.dev/graphql/mesh/docs/getting-started
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-guild-software
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/the-guild-org
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ardatan/graphql-mesh
- group: company
  title: ''
  type: Blog
  url: https://the-guild.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://the-guild.dev/graphql/hive/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-mesh-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-mesh-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-mesh-finops.md
created: '2026-03-26'
description: Universal API integration layer from The Guild that unifies REST, gRPC, SOAP, OData, Thrift, and databases into a single GraphQL schema, acting as a query gateway and SDK generator with support for federation, transforms, caching, and deployment to Node.js, serverless, and edge runtimes.
finops:
- name: Graphql Mesh Finops
  service_category: API
  slug: graphql-mesh-finops
graphqls:
- description: GraphQL Mesh is a framework by The Guild that unifies REST, gRPC, SOAP, OData, Thrift, GraphQL, and database sources into a single GraphQL schema. When deployed as a gateway using `mesh start` or `mes
  name: GraphQL Mesh GraphQL API
  slug: graphql-mesh-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphql-mesh.png
json_schemas:
- name: GraphQL Mesh Configuration
  property_count: 8
  slug: meshrc-configuration
layout: provider
modified: '2026-06-14'
name: GraphQL Mesh
nav: Providers
network: true
overview: 'GraphQL Mesh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, API Gateway, Federation, Schema Composition, and REST.


  The GraphQL Mesh catalog on APIs.io includes 1 Spectral governance ruleset.


  GraphQL Mesh''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Graphql Mesh Plans Pricing
  plan_count: 3
  slug: graphql-mesh-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Graphql Mesh Rate Limits
  slug: graphql-mesh-rate-limits
rules:
- name: GraphQL Mesh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: graphql-mesh-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.6
  delta: 7.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.6
    developer_ergonomics: 21.7
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 40.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/graphql-mesh/refs/heads/main/screenshots/graphql-mesh-2026-06-20T182334.png
security:
- kind: domain-security
  name: Graphql Mesh Domain Security
  slug: graphql-mesh-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: graphql-mesh
tags:
- GraphQL
- API Gateway
- Federation
- Schema Composition
- REST
- gRPC
- Open Source
website: https://the-guild.dev/graphql/mesh
---
