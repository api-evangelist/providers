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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Golden Recursion Agentic Access
  operation_count: 8
  slug: golden-recursion-agentic-access
  summary_line: 8 operations
api_count: 3
apis:
- description: The Entity API API from Golden Recursion — 2 operation(s) for entity api.
  name: Golden Recursion Entity API API
  slug: golden-recursion-entity-api-api
- description: The Query API API from Golden Recursion — 2 operation(s) for query api.
  name: Golden Recursion Query API API
  slug: golden-recursion-query-api-api
- description: The Schema API API from Golden Recursion — 4 operation(s) for schema api.
  name: Golden Recursion Schema API API
  slug: golden-recursion-schema-api-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Introspect the predicate schema, search entities by type, then retrieve the full cited entity.
  name: Golden — discover schema then enrich an entity
  slug: golden-recursion-enrich-entity
- description: Resolve a saved Golden query by its permalink and page through its entity results.
  name: Golden — run a saved query by permalink
  slug: golden-recursion-saved-query
artifact_total: 10
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://golden.com/product/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.golden.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.golden.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://golden.com/product/api
- group: operate
  title: ''
  type: Support
  url: https://golden.com/help
- group: company
  title: ''
  type: Blog
  url: https://golden.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goldenrecursion
- group: operate
  title: ''
  type: Roadmap
  url: https://golden.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://golden.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://golden.com/signup
- group: start
  title: ''
  type: Login
  url: https://golden.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://golden.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://golden.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/golden-recursion-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/golden-recursion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/golden-recursion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/golden-recursion-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/golden-recursion-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/golden-recursion-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/golden-recursion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/golden-recursion-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/golden-recursion-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/golden-recursion-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/golden-recursion-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/golden-recursion-enrich-entity.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/golden-recursion-saved-query.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/golden-recursion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/golden-recursion-domain-security.yml
created: '2026-07-17'
description: 'Golden Recursion Inc. builds Golden, a San Francisco company using machine intelligence to construct a self-building knowledge graph of millions of connected entities — companies, people, venture-capital firms and products — each described by structured, cited properties. The Golden API v2 gives developers read-only, programmatic access to the same data that powers the Golden Query Tool: retrieve entities and their cited properties, pull the results of saved queries by ID or permalink, and introspect the entity-type and predicate schema. Responses are structured JSON with underlying source citations so every value can be traced. Authentication is a simple apikey header. Golden also ships godel, an open-source Python SDK for its protocol GraphQL API. Backed by a16z.'
image: https://golden.com/static/images/38d57130206f78fb48c9.png
layout: provider
mcp_servers:
- description: ''
  name: golden-recursion-mcp.yml
  slug: golden-recursion-mcpyml
modified: '2026-07-19'
name: Golden Recursion
nav: Providers
network: true
overview: 'Golden Recursion publishes 3 APIs on the [APIs.io](https://apis.io/) network: Entity API API, Query API API, and Schema API API. Tagged areas include Company, Knowledge Graph, Data Enrichment, Entity Data, and Company Data.


  Golden Recursion''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 32
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.9
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 48.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/golden-recursion/refs/heads/main/screenshots/golden-recursion-2026-07-25T220029.png
security:
- kind: authentication
  name: Golden Recursion Authentication
  slug: golden-recursion-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Golden Recursion Domain Security
  slug: golden-recursion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: golden-recursion
tags:
- Company
- Knowledge Graph
- Data Enrichment
- Entity Data
- Company Data
- Artificial Intelligence
- Semantic Web
- Data
website: https://golden.com/product/api
---
