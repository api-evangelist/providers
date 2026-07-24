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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: Chroma Agentic Access
  operation_count: 44
  slug: chroma-agentic-access
  summary_line: 44 operations · 26 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Chroma Python Client is a first-party SDK for interacting with both self-hosted Chroma servers and Chroma Cloud. It provides a simple, developer-friendly interface with a core API of just four fun
  name: Chroma Python Client
  slug: python-client
- description: The Chroma JavaScript and TypeScript Client is a first-party SDK for interacting with Chroma from JavaScript or TypeScript applications. The v3 rewrite focused on reducing bundle size and improving de
  name: Chroma JavaScript Client
  slug: javascript-client
- description: Collection management endpoints for creating, listing, retrieving, updating, and deleting collections within a database.
  name: Chroma Collections API
  slug: chroma-collections-api
- description: Database management endpoints for creating, listing, retrieving, and deleting databases within a tenant.
  name: Chroma Databases API
  slug: chroma-databases-api
- description: Record management endpoints for adding, getting, updating, upserting, deleting, and querying records within a collection.
  name: Chroma Records API
  slug: chroma-records-api
- description: Advanced search endpoints available exclusively in Chroma Cloud. Provides a unified interface for hybrid search operations combining vector similarity search with metadata filtering and custom ranking
  name: Chroma Search API
  slug: chroma-search-api
- description: System-level endpoints for health checks, version information, and server diagnostics.
  name: Chroma System API
  slug: chroma-system-api
- description: Tenant management endpoints for creating and retrieving tenants.
  name: Chroma Tenants API
  slug: chroma-tenants-api
artifact_total: 41
collections:
- collection_type: open
  name: Chroma Cloud API
  slug: open-chroma-cloud-api
- collection_type: open
  name: Chroma Server API
  slug: open-chroma-server-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chroma-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chroma-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chroma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chroma-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chroma-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trychroma
- group: company
  title: ''
  type: Website
  url: https://www.trychroma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trychroma.com/docs/overview/introduction
- group: start
  title: ''
  type: Portal
  url: https://docs.trychroma.com/
- group: start
  title: ''
  type: Login
  url: https://cloud.trychroma.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.trychroma.com/cloud/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.trychroma.com/blog
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/chroma-core
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/chroma-core/chroma
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/MMeYNTmh3x
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/trychroma
- group: commercial
  title: ''
  type: License
  url: https://github.com/chroma-core/chroma/blob/main/LICENSE
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trychroma.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trychroma.com/privacy
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/chroma-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chroma-collection-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chroma-record-schema.json
- group: design
  title: ''
  type: Spectral
  url: spectral/chroma-spectral.yml
- group: other
  title: ''
  type: EmbeddingProviders
  url: ''
- group: other
  title: ''
  type: Standards
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.trychroma.com/llms.txt
created: '2025-03-07'
description: Chroma (Chroma DB) is an open-source AI-native embedding database designed to make it easy to build LLM applications by providing storage, retrieval, and management for vector embeddings, full-text search, regex search, and multi-modal retrieval (text, image, audio). Distributed under the Apache 2.0 license, Chroma can be self-hosted (single-node Python or distributed Rust-based deployment) or consumed via Chroma Cloud, a managed serverless vector database service offering usage-based pricing. Chroma is the open-source data infrastructure for AI agents and RAG (Retrieval-Augmented Generation) applications, with first-party SDKs for Python and JavaScript/TypeScript and integrations with leading embedding providers (OpenAI, Cohere, Hugging Face, sentence-transformers).
features:
- name: Document and Metadata Storage
- name: Vector Similarity Search (Dense, Sparse, Hybrid)
- name: Full-Text and Regex Search
- name: Metadata Filtering
- name: Multi-Modal Retrieval (Text, Image, Audio)
- name: Automatic Tokenization and Embedding
- name: Collection Management
- name: Embedding Function Plugins
- name: Self-Hosted and Cloud Deployments
- name: Apache 2.0 Open Source License
finops:
- name: Chroma Finops
  service_category: AI Infrastructure / Vector Database
  slug: chroma-finops
graphqls:
- description: Chroma is an open-source embedding database for AI. The API covers collection management, document and embedding upsert, querying by embedding or text, metadata filtering, and multi-modal data storage
  name: Chroma GraphQL API
  slug: chroma-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chroma.png
json_schemas:
- name: Chroma Collection
  property_count: 5
  slug: chroma-collection
- name: Chroma Record
  property_count: 5
  slug: chroma-record
jsonld:
- class_count: 0
  name: Chroma Context
  property_count: 6
  slug: chroma-context
layout: provider
modified: '2026-05-19'
name: Chroma
nav: Providers
network: true
overview: 'Chroma publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Databases API, Records API, and 3 more. Tagged areas include AI, AI Native, Apache 2.0, Cloud, and Embeddings.


  The Chroma catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chroma''s developer surface includes authentication, documentation, developer portal, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Chroma Plans Pricing
  plan_count: 3
  slug: chroma-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Chroma Rate Limits
  slug: chroma-rate-limits
rules:
- name: Chroma API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: chroma-jsonschema-spectral-rules
score:
  band: developing
  composite: 59.4
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 63.4
    developer_ergonomics: 30.4
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 59.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chroma/refs/heads/main/screenshots/chroma-2026-06-20T174327.png
security:
- kind: authentication
  name: Chroma Authentication
  slug: chroma-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Chroma Domain Security
  slug: chroma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chroma Vulnerability Disclosure
  slug: chroma-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Chroma Trust Center
  slug: chroma-trust-center
  summary_line: SOC 2, ISO 27001
slug: chroma
tags:
- AI
- AI Native
- Apache 2.0
- Cloud
- Embeddings
- Hybrid Search
- JavaScript
- LLM
- Machine Learning
- Multi-Modal
- Open Source
- Python
- RAG
- Retrieval
- SDK
- Search
- Serverless
- TypeScript
- Vector Database
use_cases:
- name: RAG (Retrieval Augmented Generation)
- name: Semantic Search
- name: AI Agent Memory
- name: Code Search (AST-Aware Chunking)
- name: Recommendation Systems
- name: Multi-Modal Search (Text + Images)
- name: Question Answering Systems
- name: Knowledge Base Querying
website: https://www.trychroma.com/
---
