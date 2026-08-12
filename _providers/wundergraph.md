---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Wundergraph Agentic Access
  operation_count: 38
  slug: wundergraph-agentic-access
  summary_line: 38 operations · 24 acting
api_count: 11
apis:
- description: Access graph analytics, metrics, and performance data.
  name: WunderGraph Analytics API
  slug: wundergraph-analytics-api
- description: Manage API keys for platform authentication.
  name: WunderGraph API Keys API
  slug: wundergraph-api-keys-api
- description: Manage feature flags for gradual rollout of graph changes.
  name: WunderGraph Feature Flags API
  slug: wundergraph-feature-flags-api
- description: Manage feature subgraphs for experimental feature development.
  name: WunderGraph Feature Subgraphs API
  slug: wundergraph-feature-subgraphs-api
- description: Manage federated graphs composed from multiple subgraphs using label matchers.
  name: WunderGraph Federated Graphs API
  slug: wundergraph-federated-graphs-api
- description: Manage monographs - non-federated graphs limited to a single subgraph.
  name: WunderGraph Monographs API
  slug: wundergraph-monographs-api
- description: Manage namespaces for organizing graphs and subgraphs.
  name: WunderGraph Namespaces API
  slug: wundergraph-namespaces-api
- description: Manage router configuration and authentication tokens.
  name: WunderGraph Router API
  slug: wundergraph-router-api
- description: Manage schema contracts for providing filtered graph views to different consumers.
  name: WunderGraph Schema Contracts API
  slug: wundergraph-schema-contracts-api
- description: Manage subgraphs - isolated GraphQL schemas that compose into federated graphs.
  name: WunderGraph Subgraphs API
  slug: wundergraph-subgraphs-api
- description: The WunderGraph Cosmo GraphQL API provides full lifecycle management of federated GraphQL APIs, including schema registry operations, composition checks, analytics queries, subgraph management, and ro
  name: WunderGraph Cloud GraphQL API
  slug: graphql-api
artifact_total: 72
collections:
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics API
  slug: postman-wundergraph-analytics-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics API Keys API
  slug: postman-wundergraph-api-keys-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics Feature Flags API
  slug: postman-wundergraph-feature-flags-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics Feature Subgraphs API
  slug: postman-wundergraph-feature-subgraphs-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics Federated Graphs API
  slug: postman-wundergraph-federated-graphs-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics Monographs API
  slug: postman-wundergraph-monographs-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics Namespaces API
  slug: postman-wundergraph-namespaces-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics Router API
  slug: postman-wundergraph-router-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics Schema Contracts API
  slug: postman-wundergraph-schema-contracts-api
- collection_type: postman
  name: WunderGraph Cosmo Platform Analytics Subgraphs API
  slug: postman-wundergraph-subgraphs-api
- collection_type: open
  name: WunderGraph Cosmo Platform API
  slug: open-wundergraph-cosmo-platform
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wundergraph/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wundergraph-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wundergraph-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wundergraph-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wundergraph
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wundergraph
- group: company
  title: ''
  type: Website
  url: https://wundergraph.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://wundergraph.com/pricing
- group: other
  title: ''
  type: Customers
  url: https://wundergraph.com/customers
- group: company
  title: ''
  type: Blog
  url: https://wundergraph.com/blog
- group: learn
  title: ''
  type: Learning
  url: https://wundergraph.com/learn
- group: other
  title: ''
  type: Architecture
  url: https://cosmo-docs.wundergraph.com/architecture
- group: auth
  title: ''
  type: Security
  url: https://cosmo-docs.wundergraph.com/security-and-compliance
- group: auth
  title: ''
  type: Compliance
  url: https://cosmo-docs.wundergraph.com/security-and-compliance
- group: learn
  title: ''
  type: Tutorials
  url: https://cosmo-docs.wundergraph.com/tutorial
- group: build
  title: ''
  type: CLI
  url: https://cosmo-docs.wundergraph.com/cli/intro
- group: start
  title: ''
  type: Login
  url: https://cosmo.wundergraph.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wundergraph.com/privacy-policy
- group: auth
  title: ''
  type: Trust
  url: https://trust.wundergraph.com/
- group: operate
  title: ''
  type: Support
  url: https://wundergraph.com/contact/sales
- group: company
  title: ''
  type: Blog
  url: https://wundergraph.com/blog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wundergraph-mcp.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/wundergraph/graphql-federation-skill
- group: agent
  title: ''
  type: LlmsText
  url: https://cosmo-docs.wundergraph.com/llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/wundergraph-platform.proto
- group: other
  title: ''
  type: gRPC
  url: grpc/wundergraph-protobuf.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wundergraph-cloud-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wundergraph-cloud-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wundergraph-cloud-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/wundergraph-cloud-finops.md
created: '2025-06-05T00:00:00.000Z'
description: Full Lifecycle API Management for (Federated) GraphQL. Schema Registry, composition checks, analytics, metrics, tracing and routing. Deploy 100% on-prem or use our Managed Service. Apache 2.0 licensed, no vendor-lock.
features:
- name: Advanced Request Tracing
- name: Analytics, Metrics & Tracing
- name: API Gateway
- name: Audit Log
- name: Authentication & Authorization
- name: AWS Lambda Router
- name: Breaking Change Detection
- name: Cache Warmer
- name: Composition Checks
- name: Compositions
- name: Event Driven Federated Subscriptions (Edfs)
- name: Feature Flags
- name: Graph Access Control
- name: Graphql Federation V1 & V2
- name: Graphql Router / Gateway
- name: Graphql Subscriptions for Federation
- name: Managed Service
- name: Mcp Gateway
- name: Oidc
- name: Opentelemetry & Distributed Tracing
- name: Persisted Operations
- name: Pull-Request-Based Schema Workflows
- name: Rbac
- name: Schema Change Notifications
- name: Schema Contracts
- name: Schema Registry
- name: Schema Usage Reporting
finops:
- name: Wundergraph Finops
  service_category: API
  slug: wundergraph-finops
graphqls:
- description: The WunderGraph Cosmo Platform API provides programmatic access to manage federated GraphQL architectures at scale. It powers the Cosmo CLI (wgc) and Cosmo Studio, enabling management of federated gra
  name: WunderGraph GraphQL API
  slug: wundergraph-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wundergraph.png
json_schemas:
- name: WunderGraph Cosmo API Key
  property_count: 5
  slug: api-key
- name: WunderGraph Cosmo Changelog Entry
  property_count: 6
  slug: changelog-entry
- name: WunderGraph Cosmo Feature Flag
  property_count: 8
  slug: feature-flag
- name: WunderGraph Cosmo Federated Graph
  property_count: 11
  slug: federated-graph
- name: WunderGraph Cosmo Monograph
  property_count: 9
  slug: monograph
- name: WunderGraph Cosmo Namespace
  property_count: 3
  slug: namespace
- name: WunderGraph Cosmo Operation Response
  property_count: 2
  slug: operation-response
- name: WunderGraph Cosmo Router Token
  property_count: 4
  slug: router-token
- name: WunderGraph Cosmo Schema Contract
  property_count: 9
  slug: schema-contract
- name: WunderGraph Cosmo Subgraph
  property_count: 11
  slug: subgraph
jsonld:
- class_count: 0
  name: Wundergraph Context
  property_count: 10
  slug: wundergraph-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-08-03'
name: WunderGraph
nav: Providers
network: true
overview: 'WunderGraph publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, API Keys API, Feature Flags API, and 7 more. Tagged areas include Federation, GraphQL, Management, Schema Registry, and API Gateway.


  The WunderGraph catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WunderGraph''s developer surface includes authentication, pricing, engineering blog, CLI, support, and 25 more developer resources.'
plans:
- name: Wundergraph Plans Pricing
  plan_count: 3
  slug: wundergraph-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Wundergraph Rate Limits
  slug: wundergraph-rate-limits
rules:
- name: WunderGraph API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wundergraph-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.3
  delta: -6.5
  facets:
    commercial_clarity: 65.8
    contract_quality: 28.4
    developer_ergonomics: 43.5
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 23.7
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wundergraph/refs/heads/main/screenshots/wundergraph-2026-06-20T201655.png
security:
- kind: authentication
  name: Wundergraph Authentication
  slug: wundergraph-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wundergraph Cloud Domain Security
  slug: wundergraph-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: domain-security
  name: Wundergraph Domain Security
  slug: wundergraph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: graphql-federation
  slug: graphql-federation
slug: wundergraph
tags:
- Federation
- GraphQL
- Management
- Schema Registry
- API Gateway
- Observability
- Agents
- Developer Tools
use_cases:
- name: GraphQL Federation
website: https://wundergraph.com/
---
