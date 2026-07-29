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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Golden Agentic Access
  operation_count: 8
  slug: golden-agentic-access
  summary_line: 8 operations
api_count: 3
apis:
- description: The Entity API API from Golden — 2 operation(s) for entity api.
  name: Golden Entity API API
  slug: golden-entity-api-api
- description: The Query API API from Golden — 2 operation(s) for query api.
  name: Golden Query API API
  slug: golden-query-api-api
- description: The Schema API API from Golden — 4 operation(s) for schema api.
  name: Golden Schema API API
  slug: golden-schema-api-api
artifact_total: 7
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.golden.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.golden.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.golden.com
- group: start
  title: ''
  type: GettingStarted
  url: https://goldenhq.notion.site/goldenhq/Golden-Guide-1eef7518f3ca43da8d6ee4d54307801b
- group: operate
  title: ''
  type: Support
  url: https://golden.com/contact
- group: company
  title: ''
  type: Blog
  url: https://golden.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://golden.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://golden.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://golden.com/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://golden.com/about/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/golden-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/golden-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/golden-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/golden-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/golden-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/golden-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/golden-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/golden-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/golden-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/golden-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/golden-domain-security.yml
created: '2026-07-17'
description: 'Golden is a company-data and knowledge-graph platform that builds a continuously updated, citation-backed map of companies, technologies, people, and the relationships between them. The Golden Public API v2 gives developers programmatic, read access to that knowledge graph: retrieve entities and their properties, resolve the schema of entity types and predicates, and run natural-language Queries that return curated, source-cited lists of entities (for example, "companies in the artificial intelligence industry"). Authentication is via an API key passed in the `apikey` header, responses are cursor-paginated, and the API is documented with an OpenAPI 3.1 specification. Golden is backed by a16z and DCVC.'
image: https://golden.com/static/images/38d57130206f78fb48c9.png
layout: provider
mcp_servers:
- description: ''
  name: golden-mcp.yml
  slug: golden-mcpyml
modified: '2026-07-19'
name: Golden
nav: Providers
network: true
overview: 'Golden publishes 3 APIs on the [APIs.io](https://apis.io/) network: Entity API API, Query API API, and Schema API API. Tagged areas include Company, Knowledge Graph, Company Data, Data, and Entities.


  Golden''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 73
score:
  band: developing
  composite: 45.0
  delta: -1.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.8
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/golden/refs/heads/main/screenshots/golden-2026-07-25T220025.png
security:
- kind: authentication
  name: Golden Authentication
  slug: golden-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Golden Domain Security
  slug: golden-domain-security
  summary_line: TLSv1.3 · DMARC
slug: golden
tags:
- Company
- Knowledge Graph
- Company Data
- Data
- Entities
- Artificial Intelligence
- Search
- Business Intelligence
website: https://docs.golden.com
---
