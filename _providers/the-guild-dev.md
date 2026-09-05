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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.7
  scored_at: '2026-09-04'
api_count: 10
apis:
- description: The @envelop/core package exposes the envelop() function and a set of built-in plugins (useSchema, useEngine, useLogger, useMaskedErrors, useExtendContext) that wrap the GraphQL execution pipeline — p
  name: Envelop API
  slug: envelop-api
- description: GraphQL Code Generator generates typed code from GraphQL schemas and operations, supporting TypeScript, React Query, Apollo Client, and many other frameworks through its plugin system.
  name: GraphQL Code Generator
  slug: graphql-code-generator
- description: The public GraphQL API for Hive Console allows developers to build custom workflows, administer users and access tokens, retrieve usage metrics, manage schema registries, publish schemas, validate com
  name: GraphQL Hive Console GraphQL API
  slug: graphql-hive-console-graphql-api
- description: Command-line tool for comparing two GraphQL schemas and generating a detailed list of breaking, non-breaking, and dangerous changes. Also validates documents and fragments, measures schema coverage, a
  name: GraphQL Inspector CLI
  slug: graphql-inspector-cli
- description: 'GraphQL federation framework that composes any API service — REST, OpenAPI, gRPC, SOAP, OData, JSON Schema, GraphQL, and databases — into a unified, type-safe GraphQL schema with built-in transforms, '
  name: GraphQL Mesh API
  slug: graphql-mesh-api
- description: Open-source TypeScript/JavaScript library providing 80+ custom GraphQL scalar types (DateTime, EmailAddress, UUID, IPv4, IBAN, JSONObject, etc.) for building precise, type-safe GraphQL schemas compati
  name: GraphQL Scalars API
  slug: graphql-scalars-api
- description: A set of utilities for faster GraphQL development, enabling SDL-first schema building, type-safe resolver composition, schema stitching across multiple services, fine-grained mocking, and schema trans
  name: GraphQL Tools API
  slug: graphql-tools-api
- description: 'GraphQL Yoga is a self-hosted GraphQL server library — each deployment exposes its own GraphQL endpoint (default: /graphql). The library handles request parsing, execution, subscriptions, file uploads'
  name: GraphQL Yoga Server
  slug: graphql-yoga-server
- description: Hive Gateway is a federated GraphQL routing engine from The Guild that supports both Apollo Federation and Schema Stitching approaches to compose distributed GraphQL services.
  name: Hive Gateway
  slug: hive-gateway
- description: Schema Stitching is a GraphQL technique for combining multiple GraphQL schemas into a single unified API gateway. The @graphql-tools/stitch package creates a combined proxy layer that delegates reques
  name: Schema Stitching
  slug: schema-stitching
artifact_total: 53
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dotansimha/graphql-code-generator/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/dotansimha/graphql-code-generator/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/dotansimha/graphql-code-generator/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-hive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/hive
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/hive/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/graphql-hive
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/the-guild-software
- group: company
  title: ''
  type: Blog
  url: https://the-guild.dev/graphql/hive/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://the-guild.dev/graphql/hive/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.graphql-hive.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TheGuildDev
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-hive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-hive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-hive-finops.yml
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-yoga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/yoga-server
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/yoga-server/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-guild-of-developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotansimha/graphql-yoga
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-yoga-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-yoga-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-yoga-finops.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/tools
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/tools/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ardatan/graphql-tools
- group: commercial
  title: ''
  type: Pricing
  url: https://the-guild.dev/graphql/tools/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-tools-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-tools-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-tools-finops.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-code-generator-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/codegen
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/codegen/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://the-guild.dev/graphql/hive#pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-code-generator-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-code-generator-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-code-generator-finops.md
- group: company
  title: ''
  type: Blog
  url: https://graphql-codegen.com/feed
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-codegen-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/codegen/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotansimha/graphql-code-generator
- group: build
  title: ''
  type: Plugins
  url: https://the-guild.dev/graphql/codegen/plugins
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-inspector-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/inspector
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/inspector/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graphql-hive
- group: company
  title: ''
  type: Blog
  url: https://the-guild.dev/blog/tag/graphql-inspector
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/marketplace/graphql-inspector
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-inspector-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-inspector-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-inspector-finops.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-scalars-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/scalars
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/scalars/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graphql-hive/graphql-scalars
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-scalars-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-scalars-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-scalars-finops.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envelop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/envelop
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/envelop/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graphql-hive/envelop
- group: commercial
  title: ''
  type: Pricing
  url: https://the-guild.dev/graphql/envelop/plugins
- group: commercial
  title: ''
  type: Plans
  url: plans/envelop-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/envelop-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/envelop-finops.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schema-stitching-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/stitching
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/stitching/docs
- group: other
  title: ''
  type: Handbook
  url: https://the-guild.dev/graphql/stitching/handbook
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ardatan
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/schema-stitching/refs/heads/main/vocabulary/schema-stitching-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/schema-stitching/refs/heads/main/examples/schema-stitching-basic-gateway-example.json
- group: agent
  title: ''
  type: LlmsText
  url: https://graphql-hive.com/llms.txt
- group: docs
  title: ''
  type: GraphQL
  url: graphql/the-guild-dev-hive-console.graphql
created: '2026-08-03'
description: The Guild is an open-source software group building much of the GraphQL ecosystem's tooling, published together at the-guild.dev. Its portfolio spans GraphQL Hive (schema registry, usage observability and breaking-change detection), GraphQL Mesh (composing many APIs into one graph), GraphQL Yoga (server), Envelop (plugin runtime), GraphQL Tools and Schema Stitching (schema composition), GraphQL Code Generator (typed clients and servers), GraphQL Inspector (schema diffing and CI checks) and GraphQL Scalars. Every product listed here shares the-guild.dev as its home, which is why they are profiled as one provider with many APIs rather than as separate companies.
examples:
- key_count: 7
  name: Schema Stitching Basic Gateway Example
  slug: schema-stitching-basic-gateway-example
- key_count: 9
  name: Schema Stitching Type Merging Example
  slug: schema-stitching-type-merging-example
finops:
- name: Graphql Codegen Finops
  service_category: API
  slug: graphql-codegen-finops
- name: Graphql Hive Finops
  service_category: ''
  slug: graphql-hive-finops
- name: Graphql Mesh Finops
  service_category: API
  slug: graphql-mesh-finops
- name: Schema Stitching Finops
  service_category: API
  slug: schema-stitching-finops
graphqls:
- description: Envelop is a lightweight JavaScript/TypeScript plugin system for wrapping the GraphQL execution pipeline. Developed by The Guild, it exposes composable lifecycle hooks that intercept and extend the pa
  name: Envelop GraphQL Plugin API
  slug: envelop-graphql
- description: GraphQL Code Generator is a CLI tool from The Guild that generates TypeScript types, React hooks, resolvers, and SDKs from GraphQL schemas and operations. It has a plugin-based architecture with 50+ c
  name: GraphQL Code Generator – GraphQL Schema
  slug: graphql-code-generator-graphql
- description: GraphQL Code Generator generates typed code from GraphQL schemas and operations, supporting TypeScript, React Query, Apollo Client, and many other frameworks through its plugin system.
  name: GraphQL Code Generator GraphQL API
  slug: graphql-codegen-graphql
- description: GraphQL Hive exposes a public GraphQL API for programmatic management of organizations, projects, targets, and schema registries. Developers use this API to automate schema publishing workflows, retri
  name: GraphQL Hive GraphQL API
  slug: graphql-hive-graphql
- description: GraphQL Inspector is a CLI tool and GitHub Action for schema change detection and validation — it consumes GraphQL schemas rather than exposing a live GraphQL endpoint. There is no public hosted Graph
  name: GraphQL Inspector GraphQL API
  slug: graphql-inspector-graphql
- description: GraphQL Mesh is a framework by The Guild that unifies REST, gRPC, SOAP, OData, Thrift, GraphQL, and database sources into a single GraphQL schema. When deployed as a gateway using `mesh start` or `mes
  name: GraphQL Mesh GraphQL API
  slug: graphql-mesh-graphql
- description: GraphQL Scalars provides custom scalar type definitions that can be added to any GraphQL schema. The scalars are defined using the standard `scalar` keyword and are fully compatible with the GraphQL s
  name: GraphQL Scalars — GraphQL Reference
  slug: graphql-scalars-graphql
- description: GraphQL Tools is a modular toolkit from The Guild for building, merging, stitching, transforming, and mocking GraphQL schemas. It is a library — not a hosted API — distributed as a set of npm packages
  name: GraphQL Tools - GraphQL Schema Documentation
  slug: graphql-tools-graphql
- description: 'GraphQL Yoga is a fully-featured, cross-platform GraphQL server from The Guild, built on top of graphql-js with an Envelop plugin system. It runs anywhere JavaScript runs — Node.js (Express, Fastify, '
  name: GraphQL Yoga
  slug: graphql-yoga-graphql
- description: Schema Stitching is a GraphQL technique for combining multiple GraphQL schemas into a single unified API gateway. The @graphql-tools/stitch package creates a combined proxy layer that delegates reques
  name: Schema Stitching GraphQL API
  slug: schema-stitching-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphql-hive.png
json_schemas:
- name: Report
  property_count: 4
  slug: graphql-hive-usage-report-v2
- name: GraphQL Mesh Configuration
  property_count: 8
  slug: meshrc-configuration
- name: Schema Stitching Configuration
  property_count: 4
  slug: schema-stitching-config
json_structures:
- name: Schema Stitching Config Structure
  property_count: 0
  slug: schema-stitching-config-structure
jsonld:
- class_count: 40
  name: Graphql Hive Context
  property_count: 11
  slug: graphql-hive-context
- class_count: 28
  name: Schema Stitching Context
  property_count: 4
  slug: schema-stitching-context
layout: provider
modified: '2026-08-03'
name: The Guild
nav: Providers
network: true
overview: 'The Guild publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL Hive Console GraphQL API. Tagged areas include API Composition, API Gateway, API Observability, Breaking Change Detection, and CI/CD.


  The The Guild catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  The Guild''s developer surface includes documentation, engineering blog, pricing, getting-started guide, GitHub presence, code examples, and 81 more developer resources.'
plans:
- name: Graphql Codegen Plans Pricing
  plan_count: 3
  slug: graphql-codegen-plans-pricing
- name: Graphql Hive Plans Pricing
  plan_count: 3
  slug: graphql-hive-plans-pricing
- name: Graphql Mesh Plans Pricing
  plan_count: 3
  slug: graphql-mesh-plans-pricing
- name: Schema Stitching Plans Pricing
  plan_count: 3
  slug: schema-stitching-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Graphql Codegen Rate Limits
  slug: graphql-codegen-rate-limits
- limit_count: 5
  name: Graphql Hive Rate Limits
  slug: graphql-hive-rate-limits
- limit_count: 5
  name: Graphql Mesh Rate Limits
  slug: graphql-mesh-rate-limits
- limit_count: 5
  name: Schema Stitching Rate Limits
  slug: schema-stitching-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: The Guild API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: graphql-hive-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: The Guild API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: graphql-mesh-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: The Guild API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: schema-stitching-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 69.3
    catalog_earned_first_party: 0.0
    catalog_gap: 45.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 64.9
    developer_ergonomics: 31.0
    discoverability: 72.2
    governance: 25.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 39.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-guild-dev/refs/heads/main/screenshots/schema-stitching-2026-06-20T193517.png
security:
- kind: domain-security
  name: Envelop Domain Security
  slug: envelop-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Graphql Code Generator Domain Security
  slug: graphql-code-generator-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Graphql Codegen Domain Security
  slug: graphql-codegen-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Graphql Hive Domain Security
  slug: graphql-hive-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Graphql Inspector Domain Security
  slug: graphql-inspector-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Graphql Mesh Domain Security
  slug: graphql-mesh-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Graphql Scalars Domain Security
  slug: graphql-scalars-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Graphql Tools Domain Security
  slug: graphql-tools-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Graphql Yoga Domain Security
  slug: graphql-yoga-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: domain-security
  name: Schema Stitching Domain Security
  slug: schema-stitching-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: the-guild-dev
tags:
- API Composition
- API Gateway
- API Observability
- Breaking Change Detection
- CI/CD
- Code Generation
- Developer Tools
- Execution
- Federation
- GitHub Actions
- GraphQL
- JavaScript
- Microservices
- Middleware
- Mocking
- Open-Source
- Plugins
- REST
- SDK
- Scalars
- Schema
- Schema Composition
- Schema Merging
- Schema Registry
- Schema Stitching
- Schema Transformation
- Schema Validation
- Server
- Subscription
- The Guild
- Type Merging
- Type Safety
- TypeScript
- gRPC
website: https://the-guild.dev/graphql/hive
---
