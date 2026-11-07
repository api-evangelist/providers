---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Chroma Agentic Access
  operation_count: 25
  slug: chroma-agentic-access
  summary_line: 25 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Chroma Python Client is a first-party SDK for interacting with both self-hosted Chroma servers and Chroma Cloud. It provides a simple, developer-friendly interface with a core API of just four fun
  name: Chroma Python Client
  slug: python-client
- description: The Chroma JavaScript and TypeScript Client is a first-party SDK for interacting with Chroma from JavaScript or TypeScript applications. The v3 rewrite focused on reducing bundle size and improving de
  name: Chroma JavaScript Client
  slug: javascript-client
- baseURL: https://api.trychroma.com
  baseurl_source: declared
  description: System-level endpoints for health checks, version information, and server diagnostics.
  name: Chroma System API
  slug: chroma-system-api
- baseURL: https://api.trychroma.com
  baseurl_source: declared
  description: The Authentication API from Chroma — 1 operation(s) for authentication.
  name: Chroma Authentication API
  slug: chroma-authentication-api
- baseURL: https://api.trychroma.com
  baseurl_source: declared
  description: The Collection API from Chroma — 7 operation(s) for collection.
  name: Chroma Collection API
  slug: chroma-collection-api
- baseURL: https://api.trychroma.com
  baseurl_source: declared
  description: The Database API from Chroma — 3 operation(s) for database.
  name: Chroma Database API
  slug: chroma-database-api
- baseURL: https://api.trychroma.com
  baseurl_source: declared
  description: The Function API from Chroma — 4 operation(s) for function.
  name: Chroma Function API
  slug: chroma-function-api
- baseURL: https://api.trychroma.com
  baseurl_source: declared
  description: The Record API from Chroma — 11 operation(s) for record.
  name: Chroma Record API
  slug: chroma-record-api
- baseURL: https://api.trychroma.com
  baseurl_source: declared
  description: The Tenant API from Chroma — 2 operation(s) for tenant.
  name: Chroma Tenant API
  slug: chroma-tenant-api
artifact_total: 55
collections:
- collection_type: postman
  name: Chroma Cloud Collections API
  slug: postman-chroma-collections-api
- collection_type: postman
  name: Chroma Cloud Collections Databases API
  slug: postman-chroma-databases-api
- collection_type: postman
  name: Chroma Cloud Collections Records API
  slug: postman-chroma-records-api
- collection_type: postman
  name: Chroma Cloud Collections Search API
  slug: postman-chroma-search-api
- collection_type: postman
  name: Chroma Cloud Collections System API
  slug: postman-chroma-system-api
- collection_type: postman
  name: Chroma Cloud Collections Tenants API
  slug: postman-chroma-tenants-api
- collection_type: open
  name: Chroma Cloud API
  slug: open-chroma-cloud-api
- collection_type: open
  name: Chroma Cloud Collections API
  slug: open-chroma-collections-api
- collection_type: open
  name: Chroma Cloud Collections Databases API
  slug: open-chroma-databases-api
- collection_type: open
  name: Chroma Server API (v2)
  slug: open-chroma-db
- collection_type: open
  name: Chroma Cloud Collections Records API
  slug: open-chroma-records-api
- collection_type: open
  name: Chroma Cloud Collections Search API
  slug: open-chroma-search-api
- collection_type: open
  name: Chroma Server API
  slug: open-chroma-server-api
- collection_type: open
  name: Chroma Cloud Collections System API
  slug: open-chroma-system-api
- collection_type: open
  name: Chroma Cloud Collections Tenants API
  slug: open-chroma-tenants-api
common:
- group: other
  href: https://artifacts.apis.io/chroma/capabilities/chroma-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/chroma-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/chroma/rate-limits/chroma-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chroma-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chroma/finops/chroma-finops.yml
  title: ''
  type: FinOps
  url: finops/chroma-finops.yml
- group: commercial
  href: https://artifacts.apis.io/chroma/plans/chroma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chroma-plans-pricing.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/chroma-core/chroma/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/chroma-core/chroma/releases
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/chroma/overview
- group: agent
  href: https://artifacts.apis.io/chroma/agentic-access/chroma-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chroma-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/chroma/security/chroma-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chroma-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/chroma/security/chroma-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chroma-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chroma/security/chroma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chroma-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/chroma/authentication/chroma-authentication.yml
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
  href: https://artifacts.apis.io/chroma/json-ld/chroma-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/chroma-context.jsonld
- group: docs
  href: https://artifacts.apis.io/chroma/json-schema/chroma-collection-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/chroma-collection-schema.json
- group: docs
  href: https://artifacts.apis.io/chroma/json-schema/chroma-record-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/chroma-record-schema.json
- group: design
  href: https://artifacts.apis.io/chroma/spectral/chroma-spectral.yml
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
- has_sources: true
  method: derived
  name: Chroma Finops
  primary_unit: logical gib written
  service_category: ''
  slug: chroma-finops
  template: false
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
mcp_servers:
- description: Remote MCP server at mcp.trychroma.com over HTTP; 3 tools listed.
  name: Chroma MCP Server
  slug: chroma
modified: '2026-05-19'
name: Chroma
nav: Providers
network: true
overview: 'Chroma publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including System API, Authentication API, Collection API, and 6 more. Tagged areas include Artificial Intelligence, AI-native, Apache 2.0, Cloud, and Embeddings.


  The Chroma catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chroma''s developer surface includes authentication, documentation, developer portal, pricing, engineering blog, and 26 more developer resources.'
plans:
- name: Chroma Plans Pricing
  plan_count: 9
  slug: chroma-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Chroma Rate Limits
  slug: chroma-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Chroma — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: chroma-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.3
    catalog_earned_first_party: 12.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 75.0
    contract_governance: 9.8
    contract_quality: 53.5
    developer_ergonomics: 46.4
    discoverability: 66.7
    operational_transparency: 36.8
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 56.3
      derived: 0
      marker_coverage: 43.8
      total: 16
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 72.2
screenshot: https://apis.io/screenshots/chroma/chroma-2026-06-20T174327.png
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
  summary_line: no policy recorded
- kind: trust-center
  name: Chroma Trust Center
  slug: chroma-trust-center
  summary_line: SOC 2, ISO 27001
slug: chroma
tags:
- Artificial Intelligence
- AI-native
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
- Vector Search
- Database
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
