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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Chroma Db Agentic Access
  operation_count: 24
  slug: chroma-db-agentic-access
  summary_line: 24 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Named vector stores holding embeddings and metadata.
  name: Chroma Collections API
  slug: chroma-db-collections-api
- description: Logical grouping of collections within a tenant.
  name: Chroma Databases API
  slug: chroma-db-databases-api
- description: Nearest-neighbor vector similarity search over a collection.
  name: Chroma Query API
  slug: chroma-db-query-api
- description: Embeddings (with documents, metadata, URIs) inside a collection.
  name: Chroma Records API
  slug: chroma-db-records-api
- description: Server health, version, and pre-flight operational endpoints.
  name: Chroma System API
  slug: chroma-db-system-api
- description: Top-level isolation boundary that owns databases.
  name: Chroma Tenants API
  slug: chroma-db-tenants-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chroma Server API (v2) Collections API
  slug: open-chroma-db-collections-api
- collection_type: open
  name: Chroma Server API (v2) Collections Databases API
  slug: open-chroma-db-databases-api
- collection_type: open
  name: Chroma Server API (v2) Collections Query API
  slug: open-chroma-db-query-api
- collection_type: open
  name: Chroma Server API (v2) Collections Records API
  slug: open-chroma-db-records-api
- collection_type: open
  name: Chroma Server API (v2) Collections System API
  slug: open-chroma-db-system-api
- collection_type: open
  name: Chroma Server API (v2) Collections Tenants API
  slug: open-chroma-db-tenants-api
- collection_type: open
  name: Chroma Server API (v2)
  slug: open-chroma-db
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chroma-db-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chroma-db-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chroma-db-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chroma-core
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trychroma
- group: company
  title: ''
  type: Website
  url: https://www.trychroma.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trychroma.com
- group: commercial
  title: ''
  type: Plans
  url: plans/chroma-db-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chroma-db-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chroma-db-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.trychroma.com/blog
created: '2026-07-12'
description: Chroma (Chroma DB) is an open-source, AI-native vector database (embedding database) for building LLM, RAG, and semantic-search applications. It provides storage, indexing, and retrieval for vector embeddings with metadata filtering, full-text and regex search, and multi-modal retrieval across text, images, and audio. Chroma is Apache-2.0 licensed and self-hostable via a single server, and is also available as Chroma Cloud, a serverless, usage-based managed offering. Its HTTP/REST v2 API is organized around tenants, databases, collections, and the records (embeddings) inside each collection - add, upsert, update, get, query (similarity search), and delete - and is the same interface used by the Python, JavaScript/TypeScript, Rust, and other client libraries.
finops:
- name: Chroma Db Finops
  service_category: AI and Machine Learning
  slug: chroma-db-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chroma-db.png
layout: provider
modified: '2026-07-12'
name: Chroma
nav: Providers
network: true
overview: 'Chroma publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Databases API, Query API, and 3 more. Tagged areas include Vector Database, Vector Index, Vector Search, Vector Store, and Embeddings.


  Chroma''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Chroma Db Plans Pricing
  plan_count: 4
  slug: chroma-db-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Chroma Db Rate Limits
  slug: chroma-db-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chroma-db/refs/heads/main/screenshots/chroma-db-2026-07-25T205258.png
security:
- kind: authentication
  name: Chroma Db Authentication
  slug: chroma-db-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chroma Db Domain Security
  slug: chroma-db-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chroma-db
tags:
- Vector Database
- Vector Index
- Vector Search
- Vector Store
- Embeddings
- Similarity Search
- RAG
- Semantic Search
- Artificial Intelligence
- AI Inference
- Machine-Learning
- Open-Source
website: https://www.trychroma.com
---
