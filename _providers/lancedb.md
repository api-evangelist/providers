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
    auth_clarity: negotiable
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 47
  human_in_the_loop: 0
  name: Lancedb Agentic Access
  operation_count: 50
  slug: lancedb-agentic-access
  summary_line: 50 operations · 47 acting
api_count: 1
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
- baseURL: https://github.com/lancedb/lancedb
  baseurl_source: declared
  description: The MaterializedView API from LanceDB — 2 operation(s) for materializedview.
  name: LanceDB MaterializedView API
  slug: lancedb-materializedview-api
- baseURL: https://github.com/lancedb/lancedb
  baseurl_source: declared
  description: Operations that are related to a namespace
  name: LanceDB Namespace API
  slug: lancedb-namespace-api
- baseURL: https://github.com/lancedb/lancedb
  baseurl_source: declared
  description: Operations that are related to a table
  name: LanceDB Table API
  slug: lancedb-table-api
- baseURL: https://github.com/lancedb/lancedb
  baseurl_source: declared
  description: Operations that are related to a transaction
  name: LanceDB Transaction API
  slug: lancedb-transaction-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lance Namespace Specification Data API
  slug: open-lancedb-data-api
- collection_type: open
  name: Lance Namespace Specification Data Index API
  slug: open-lancedb-index-api
- collection_type: open
  name: Lance Namespace Specification Data MaterializedView API
  slug: open-lancedb-materializedview-api
- collection_type: open
  name: Lance Namespace Specification Data Metadata API
  slug: open-lancedb-metadata-api
- collection_type: open
  name: Lance Specification Data Namespace API
  slug: open-lancedb-namespace-api
- collection_type: open
  name: Lance Namespace Specification Data Table API
  slug: open-lancedb-table-api
- collection_type: open
  name: Lance Namespace Specification Data Tag API
  slug: open-lancedb-tag-api
- collection_type: open
  name: Lance Namespace Specification Data Transaction API
  slug: open-lancedb-transaction-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/lance-format/lance/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/lance-format/lance/blob/main/CONTRIBUTING.md
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
overview: 'LanceDB publishes 4 APIs on the [APIs.io](https://apis.io/) network, including MaterializedView API, Namespace API, Table API, and 1 more. Tagged areas include Vector Database, Multi-Modal, Lance Format, Lakehouse, and RAG.


  The LanceDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  LanceDB''s developer surface includes authentication, documentation, engineering blog, GitHub presence, support, and 15 more developer resources.'
plans:
- name: Lancedb Plans Pricing
  plan_count: 4
  slug: lancedb-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Lancedb Rate Limits
  slug: lancedb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: LanceDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lancedb-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: LanceDB API Rules
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
  composite: 48.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 37.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 55.8
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 50.0
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
- Multi-Modal
- Lance Format
- Lakehouse
- RAG
- Agent Memory
- Open-Source
- Embeddings
- Full-Text Search
- Hybrid Search
- Columnar Storage
- Arrow
- AI Infrastructure
website: https://lancedb.com/
---
