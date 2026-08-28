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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Styra Agentic Access
  operation_count: 6
  slug: styra-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 5
apis:
- description: The Batch API from Styra — 1 operation(s) for batch.
  name: Styra Batch API
  slug: styra-batch-api
- description: The Compile API from Styra — 1 operation(s) for compile.
  name: Styra Compile API
  slug: styra-compile-api
- description: The Data API from Styra — 1 operation(s) for data.
  name: Styra Data API
  slug: styra-data-api
- description: The Enterprise OPA REST API API from Styra — 1 operation(s) for enterprise opa rest api.
  name: Styra Enterprise OPA REST API API
  slug: styra-enterprise-opa-rest-api-api
- description: The Health API from Styra — 1 operation(s) for health.
  name: Styra Health API
  slug: styra-health-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Enterprise OPA REST Batch API
  slug: open-styra-batch-api
- collection_type: open
  name: Enterprise OPA REST Batch Compile API
  slug: open-styra-compile-api
- collection_type: open
  name: Enterprise OPA REST Batch Data API
  slug: open-styra-data-api
- collection_type: open
  name: Enterprise OPA REST Batch Enterprise OPA REST API API
  slug: open-styra-enterprise-opa-rest-api-api
- collection_type: open
  name: Enterprise OPA REST Batch Health API
  slug: open-styra-health-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/styra-enterprise-opa-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.openpolicyagent.org/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.openpolicyagent.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.openpolicyagent.org/docs/rest-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StyraOSS
- group: auth
  title: ''
  type: Authentication
  url: authentication/styra-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/styra-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/styra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/styra-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/styra-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/styra-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/styra-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/styra-data-v1.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/styra-bulk-v1-bulk.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/styra-policy-v1-policy.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/styra-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/styra-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/styra-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/styra-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/styra-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/styra-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.openpolicyagent.org
created: '2026-07-17'
description: Styra is the company that created Open Policy Agent (OPA), the Cloud Native Computing Foundation graduated policy engine, and commercialized it as Enterprise OPA and Styra DAS (Declarative Authorization Service) for policy-as-code authorization across Kubernetes, microservices, APIs, and data. Styra was acquired by Akamai in December 2024; the styra.com and docs.styra.com properties no longer resolve, but OPA remains the de facto standard for cloud-native authorization and the open-source technical surface (GitHub, published SDKs, the OpenAPI spec, and gRPC protobufs) is active. The Enterprise OPA / OPA REST API evaluates Rego policy decisions, batch decisions, and partial-evaluation "data filtering" that compiles authorization into UCAST or SQL conditions. Backed originally by Accel and Battery Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/styra.png
layout: provider
mcp_servers:
- description: ''
  name: Styra MCP Server
  slug: styra-mcp-server
modified: '2026-07-21'
name: Styra
nav: Providers
network: true
overview: 'Styra publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Compile API, Data API, and 2 more. Tagged areas include Company, Cybersecurity, Authorization, Policy as Code, and Open Policy Agent.


  Styra''s developer surface includes documentation, API reference, authentication, CLI, changelog, and 18 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 45.0
    developer_ergonomics: 54.2
    discoverability: 64.8
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Styra Authentication
  slug: styra-authentication
  summary_line: http · 1 scheme
slug: styra
tags:
- Company
- Cybersecurity
- Authorization
- Policy as Code
- Open Policy Agent
- Access Control
- Cloud-Native
- API Security
website: https://www.openpolicyagent.org
---
