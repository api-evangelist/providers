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
- acting_count: 47
  human_in_the_loop: 0
  name: Lancedb Agentic Access
  operation_count: 50
  slug: lancedb-agentic-access
  summary_line: 50 operations · 47 acting
api_count: 16
apis:
- description: Distributed, multi-tenant multimodal lakehouse. Adds curation and deduplication, Python UDF feature engineering, materialized views, GPU-accelerated index build via cuVS, distributed query, and direct
  name: LanceDB Enterprise
  slug: enterprise
- description: Apache 2.0 open lakehouse format for multimodal AI. Columnar Parquet replacement offering 100x faster random access, zero-copy reads, vector indexes, and automatic data versioning. Convertible from Pa
  name: Lance Format
  slug: lance-format
- description: Primary client library. First-class Arrow, Pandas, Polars, and Pydantic integration; pluggable embedding functions covering OpenAI, Cohere, Jina, Hugging Face, Ollama, Bedrock, Sentence Transformers a
  name: LanceDB Python SDK
  slug: python-sdk
- description: Node.js / TypeScript / JavaScript client library for LanceDB OSS, Cloud, and Enterprise. Bundles native bindings via napi-rs.
  name: LanceDB TypeScript SDK
  slug: typescript-sdk
- description: Native Rust client library; the LanceDB core and storage layer are written in Rust.
  name: LanceDB Rust SDK
  slug: rust-sdk
- description: Official Go client library for LanceDB OSS, Cloud, and Enterprise.
  name: LanceDB Go SDK
  slug: go-sdk
- description: C ABI bindings for LanceDB enabling embedding into C, C++, and other FFI-capable hosts.
  name: LanceDB C Bindings
  slug: c-sdk
- description: Model Context Protocol (MCP) server exposing LanceDB tables as retrieval tools for MCP-aware agents and IDEs.
  name: LanceDB MCP Server
  slug: mcp-server
- description: Operations that interact with object data and might be computationally intensive
  name: LanceDB Data API
  slug: lancedb-data-api
- description: Operations that are related to an index
  name: LanceDB Index API
  slug: lancedb-index-api
- description: The MaterializedView API from LanceDB — 2 operation(s) for materializedview.
  name: LanceDB MaterializedView API
  slug: lancedb-materializedview-api
- description: Operations that only interact with object metadata and should be computationally lightweight
  name: LanceDB Metadata API
  slug: lancedb-metadata-api
- description: Operations that are related to a namespace
  name: LanceDB Namespace API
  slug: lancedb-namespace-api
- description: Operations that are related to a table
  name: LanceDB Table API
  slug: lancedb-table-api
- description: Operations that are related to tags
  name: LanceDB Tag API
  slug: lancedb-tag-api
- description: Operations that are related to a transaction
  name: LanceDB Transaction API
  slug: lancedb-transaction-api
artifact_total: 36
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lancedb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lancedb-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lancedb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lancedb-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lancedb-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://lancedb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lancedb.com/
- group: company
  title: ''
  type: Blog
  url: https://lancedb.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lancedb
- group: build
  title: ''
  type: GitHubFormat
  url: https://github.com/lance-format
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/G5DcmnZWKB
- group: auth
  title: ''
  type: Trust
  url: https://trust.lancedb.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@lancedb.com
- group: operate
  title: ''
  type: Contact
  url: https://lancedb.com/contact
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lancedb.com/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/lancedb/main/openapi/lance-namespace-openapi.yaml
- group: other
  title: ''
  type: Capabilities
  url: https://raw.githubusercontent.com/api-evangelist/lancedb/main/capabilities/multimodal-retrieval.yaml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/lancedb/main/vocabulary/lancedb-vocabulary.yml
created: '2026-05-23'
description: LanceDB is the AI-Native multimodal lakehouse built on the open-source Lance columnar storage format. It pairs an Apache 2.0 licensed embedded retrieval library (Python, TypeScript, Rust, Go, C, Java SDKs) with a managed cloud service (LanceDB Cloud) and an enterprise lakehouse (LanceDB Enterprise) that unify vector, full-text, hybrid, and SQL search across billions of multimodal records. The REST surface is governed by the open Lance Namespace specification (OpenAPI 3.1) covering namespace, table, index, tag, and transaction operations with first-class support for materialized views, schema evolution, and time-travel versioning. LanceDB is used in production by Midjourney, Runway, World Labs, Netflix, Character.AI, Uber, NVIDIA, ByteDance, Databricks, and others for RAG, agent memory, training data curation, feature engineering, and large-scale retrieval.
examples:
- key_count: 4
  name: Lancedb Create Table Example
  slug: lancedb-create-table-example
- key_count: 3
  name: Lancedb Create Tag Example
  slug: lancedb-create-tag-example
- key_count: 8
  name: Lancedb Create Vector Index Example
  slug: lancedb-create-vector-index-example
- key_count: 13
  name: Lancedb Hybrid Query Example
  slug: lancedb-hybrid-query-example
- key_count: 5
  name: Lancedb Merge Insert Example
  slug: lancedb-merge-insert-example
finops:
- name: Lancedb Finops
  service_category: ''
  slug: lancedb-finops
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-network/lancedb/lancedb-logo.png
json_schemas:
- name: Lance Namespace
  property_count: 5
  slug: lancedb-namespace
- name: LanceDB Query Request
  property_count: 13
  slug: lancedb-query
- name: LanceDB Table
  property_count: 9
  slug: lancedb-table
json_structures:
- name: Lancedb Table Structure
  property_count: 10
  slug: lancedb-table-structure
jsonld:
- class_count: 26
  name: Lancedb Context
  property_count: 5
  slug: lancedb-context
layout: provider
modified: '2026-05-25'
name: LanceDB
nav: Providers
network: true
overview: 'LanceDB publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Data API, Index API, MaterializedView API, and 5 more. Tagged areas include Vector Database, Multimodal, Lance Format, Lakehouse, and RAG.


  The LanceDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  LanceDB''s developer surface includes authentication, documentation, engineering blog, GitHub presence, support, and 13 more developer resources.'
plans:
- name: Lancedb Plans Pricing
  plan_count: 4
  slug: lancedb-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 0
  name: Lancedb Rate Limits
  slug: lancedb-rate-limits
rules:
- name: LanceDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lancedb-jsonschema-spectral-rules
- name: LanceDB API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: lancedb-rules
scopes:
- name: Lancedb Scopes
  scope_count: 0
  slug: lancedb-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.2
  delta: -6.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.5
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lancedb/refs/heads/main/screenshots/lancedb-2026-06-20T184404.png
security:
- kind: authentication
  name: Lancedb Authentication
  slug: lancedb-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Lancedb Domain Security
  slug: lancedb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lancedb Trust Center
  slug: lancedb-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: lancedb
tags:
- Vector Database
- Multimodal
- Lance Format
- Lakehouse
- RAG
- Agent Memory
- Open Source
- Embeddings
- Full-Text Search
- Hybrid Search
- Columnar Storage
- Arrow
- AI Infrastructure
website: https://lancedb.com/
---
