---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Turbopuffer Agentic Access
  operation_count: 14
  slug: turbopuffer-agentic-access
  summary_line: 14 operations · 10 acting
api_count: 11
apis:
- description: Endpoints for upserting, patching, and deleting documents within a namespace. Writes are batched into a per-namespace write-ahead log and become queryable once committed to object storage. Supports bo
  name: turbopuffer Write API
  slug: write
- description: Unified query endpoint that runs vector ANN, full-text BM25, and hybrid queries against a namespace, with attribute filters, top-k, aggregation groups, and ranking controls. Supports multi-query (up t
  name: turbopuffer Query API
  slug: query
- description: Namespace lifecycle and metadata endpoints — list namespaces, read schema / dimensions / row count, warm the cache, export contents, branch_from (copy-on-write clones in constant time), copy_from, and
  name: turbopuffer Namespaces API
  slug: namespaces
- description: Official Python client library for the turbopuffer REST API, Stainless-generated from the public OpenAPI spec.
  name: turbopuffer Python SDK
  slug: python-sdk
- description: Official TypeScript / JavaScript client library for the turbopuffer REST API, Stainless-generated and published to npm.
  name: turbopuffer TypeScript SDK
  slug: typescript-sdk
- description: Official Go client library for the turbopuffer REST API, Stainless-generated from the public OpenAPI spec.
  name: turbopuffer Go SDK
  slug: go-sdk
- description: Official Java / Kotlin client library for the turbopuffer REST API, Stainless-generated from the public OpenAPI spec.
  name: turbopuffer Java SDK
  slug: java-sdk
- description: Official Ruby client library for the turbopuffer REST API, Stainless-generated from the public OpenAPI spec.
  name: turbopuffer Ruby SDK
  slug: ruby-sdk
- description: Official C# / .NET client library for the turbopuffer REST API, Stainless-generated from the public OpenAPI spec.
  name: turbopuffer C# SDK
  slug: csharp-sdk
- description: Open-source general-purpose benchmarking tool for turbopuffer deployments. Useful for validating recall, latency, and throughput on a given workload.
  name: tpuf-benchmark
  slug: benchmark
- description: The Namespaces API from turbopuffer — 12 operation(s) for namespaces.
  name: turbopuffer Namespaces API
  slug: turbopuffer-namespaces-api
artifact_total: 18
collections:
- collection_type: open
  name: turbopuffer API
  slug: open-turbopuffer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/turbopuffer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turbopuffer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turbopuffer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://turbopuffer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://turbopuffer.com/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/turbopuffer
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/turbopuffer/turbopuffer-openapi
- group: commercial
  title: ''
  type: Pricing
  url: https://turbopuffer.com/pricing
- group: other
  title: ''
  type: Architecture
  url: https://turbopuffer.com/docs/architecture
- group: other
  title: ''
  type: Regions
  url: https://turbopuffer.com/docs/regions
- group: other
  title: ''
  type: Limits
  url: https://turbopuffer.com/docs/limits
- group: company
  title: ''
  type: Blog
  url: https://turbopuffer.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://turbopuffer.com/llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://turbopuffer.com/terms-of-service
- group: other
  title: ''
  type: Customers
  url: https://turbopuffer.com/customers
created: '2026-05-23'
description: turbopuffer is a serverless search engine that combines vector and full-text (BM25) search built from first principles directly on object storage. It exposes a single REST API organized around namespaces — each namespace stores documents with vector embeddings, attributes, and full-text indexes — and supports approximate nearest neighbor, full-text BM25, and hybrid query patterns with attribute filtering, ranking, and aggregation. The platform is used in production by Anthropic, Cursor, Notion, Linear, Superhuman, Pylon, Readwise, and Telus, and handles 4T+ documents, 10M+ writes/s, and 25k+ queries/s across customer fleets. Official client libraries ship for Python, TypeScript, Go, Java, Ruby, and C#, generated from a public OpenAPI 3.1 specification via Stainless. Pricing is tiered (Launch, Scale, Enterprise) with usage-based metering on storage, writes, and queries on top of monthly minimums.
finops:
- name: Turbopuffer Finops
  service_category: API
  slug: turbopuffer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turbopuffer.png
layout: provider
modified: '2026-05-25'
name: turbopuffer
nav: Providers
network: true
overview: 'turbopuffer publishes 1 API on the [APIs.io](https://apis.io/) network: Namespaces API. Tagged areas include Vector Search, Full-Text Search, Hybrid Search, BM25, and Serverless.


  turbopuffer''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Turbopuffer Plans Pricing
  plan_count: 3
  slug: turbopuffer-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 3
  name: Turbopuffer Rate Limits
  slug: turbopuffer-rate-limits
score:
  band: thin
  composite: 39.4
  delta: -2.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 43.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turbopuffer/refs/heads/main/screenshots/turbopuffer-2026-06-20T195831.png
security:
- kind: authentication
  name: Turbopuffer Authentication
  slug: turbopuffer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Turbopuffer Domain Security
  slug: turbopuffer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: turbopuffer
tags:
- Vector Search
- Full-Text Search
- Hybrid Search
- BM25
- Serverless
- Object Storage
- RAG
- Semantic Search
- AI Infrastructure
- Embeddings
website: https://turbopuffer.com/
---
