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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Apollo Federation enables declarative composition of multiple subgraph APIs into a single federated supergraph. The Apollo Router orchestrates requests across subgraphs, combining GraphQL APIs and RES
  name: Apollo Federation
  slug: apollo-federation
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-federation-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.apollographql.com/docs/federation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apollographql.com/docs/federation/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apollographql
- group: build
  title: Federation Spec
  type: GitHubRepository
  url: https://github.com/apollographql/federation
- group: build
  title: Apollo Router
  type: GitHubRepository
  url: https://github.com/apollographql/router
- group: build
  title: Rover CLI
  type: GitHubRepository
  url: https://github.com/apollographql/rover
- group: build
  title: Subgraph Compatibility Tests
  type: GitHubRepository
  url: https://github.com/apollographql/apollo-federation-subgraph-compatibility
- group: build
  title: JVM Support
  type: SDKs
  url: https://github.com/apollographql/federation-jvm
- group: company
  title: ''
  type: Blog
  url: https://www.apollographql.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apollographql.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://studio.apollographql.com/signup
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/apollographql/apollo-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://www.apollographql.com/llms.txt
created: '2026-03-26'
description: Apollo Federation is an architecture and platform for building a unified supergraph that composes multiple GraphQL APIs (subgraphs) into a single distributed GraphQL endpoint, enabling teams to work independently on different parts of the graph while delivering a unified API to consumers. Federation 2 is the current stable version, supported by the Apollo Router written in Rust and the Rover CLI for schema management.
features:
- description: Compose multiple subgraph schemas into a single unified supergraph schema.
  name: Supergraph Composition
- description: Declarative federation directives (@key, @external, @requires, @provides, @shareable, @link) for schema coordination.
  name: Federation Directives
- description: High-performance Rust-based router that orchestrates queries across subgraphs.
  name: Apollo Router
- description: Declarative integration of REST APIs into federated graphs without writing a separate GraphQL server.
  name: Apollo Connectors
- description: Apollo GraphOS schema registry for publishing, checking, and managing supergraph schemas.
  name: Schema Registry
- description: Command-line tool for publishing subgraph schemas, running checks, and managing the supergraph.
  name: Rover CLI
- description: Intelligent query planning that decomposes client queries into efficient subgraph requests.
  name: Query Planning
- description: Federation-compatible subgraphs can be built in any language or framework.
  name: Subgraph Compatibility
- description: Progressive schema rollout with incremental migration from monolith to federated graph.
  name: Gray Release Support
finops:
- name: Apollo Federation Finops
  service_category: API
  slug: apollo-federation-finops
graphqls:
- description: Apollo Federation enables declarative composition of multiple subgraph APIs into a single federated supergraph. The Apollo Router orchestrates requests across subgraphs, combining GraphQL APIs and RES
  name: Apollo Federation GraphQL API
  slug: apollo-federation-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-federation.png
json_schemas:
- name: Apollo Router Configuration
  property_count: 8
  slug: router-configuration
- name: Apollo Federation Supergraph Configuration
  property_count: 2
  slug: supergraph-configuration
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Apollo Federation
nav: Providers
network: true
overview: 'Apollo Federation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Gateway, Federation, GraphQL, Microservices, and Open Source.


  The Apollo Federation catalog on APIs.io includes 1 Spectral governance ruleset.


  Apollo Federation''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Apollo Federation Plans Pricing
  plan_count: 3
  slug: apollo-federation-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Apollo Federation Rate Limits
  slug: apollo-federation-rate-limits
rules:
- name: Apollo Federation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apollo-federation-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.1
  delta: -4.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 16.1
    developer_ergonomics: 37.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-federation/refs/heads/main/screenshots/apollo-federation-2026-06-20T172310.png
security:
- kind: domain-security
  name: Apollo Federation Domain Security
  slug: apollo-federation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apollo-federation
tags:
- API Gateway
- Federation
- GraphQL
- Microservices
- Open Source
- Subgraphs
- Supergraph
use_cases:
- description: Enable independent teams to own and develop separate subgraphs while delivering a unified API.
  name: Distributed Team Development
- description: Gradually expose existing REST APIs as GraphQL via Apollo Connectors without full rewrites.
  name: REST API Modernization
- description: Consolidate multiple disparate APIs into a single unified supergraph for consumers.
  name: API Consolidation
- description: Add a federated GraphQL layer over existing microservice architectures.
  name: Microservices GraphQL Layer
- description: Enforce schema design standards across all subgraphs via composition checks.
  name: Schema Governance
---
