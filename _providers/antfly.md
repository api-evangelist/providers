---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 218
  human_in_the_loop: 5
  name: Antfly Agentic Access
  operation_count: 338
  slug: antfly-agentic-access
  summary_line: 338 operations · 218 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: The Ai API from Antfly — 24 operation(s) for ai.
  name: Antfly AI API
  slug: antfly-ai-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: 'Monitor and manage your Antfly cluster''s health and status. ## Cluster Health The cluster health endpoint provides real-time status of all stores and shards: - **healthy**: All nodes and shards operat'
  name: Antfly Cluster Management API
  slug: antfly-cluster-management-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: 'Perform data operations including batch inserts/deletes, linear merge sync, backup/restore, and individual key lookups. ## Batch Operations Efficiently insert or delete multiple documents in a single '
  name: Antfly Data Operations API
  slug: antfly-data-operations-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: The Documents API from Antfly — 12 operation(s) for documents.
  name: Antfly Documents API
  slug: antfly-documents-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: 'Create and manage indexes for full-text search, vector similarity search, and multimodal content. ## Index Types Antfly supports two primary index types: ### `full_text` - Full-Text Search Index BM25-'
  name: Antfly Index Management API
  slug: antfly-index-management-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: The Inference API from Antfly — 1 operation(s) for inference.
  name: Antfly Inference API
  slug: antfly-inference-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: PostgreSQL-style installed extension lifecycle.
  name: Antfly Installed API
  slug: antfly-installed-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: Evidence-backed temporal agent memory
  name: Antfly Memory API
  slug: antfly-memory-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: The Ml API from Antfly — 3 operation(s) for ml.
  name: Antfly Ml API
  slug: antfly-ml-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: The Models API from Antfly — 2 operation(s) for models.
  name: Antfly Models API
  slug: antfly-models-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: Signed installable artifacts known to Antfly.
  name: Antfly Packages API
  slug: antfly-packages-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: Operations related to permissions
  name: Antfly Permission API
  slug: antfly-permission-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: The personal_connections API from Antfly — 5 operation(s) for personal_connections.
  name: Antfly Personal Connections API
  slug: antfly-personal-connections-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: 'Execute queries across tables using full-text search, vector similarity search, or hybrid approaches combining both with Reciprocal Rank Fusion (RRF). ## Query Types ### Full-Text Search Uses Antfly q'
  name: Antfly Query Operations API
  slug: antfly-query-operations-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: Durable resolver identity correction, suppression, review and replay.
  name: Antfly Resolver Curation API
  slug: antfly-resolver-curation-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: Operations related to Casbin role and group membership
  name: Antfly Role API
  slug: antfly-role-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: Operations related to row-level security filters
  name: Antfly Row Filter API
  slug: antfly-rowfilter-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: 'Manage tables in your Antfly cluster. Tables store your documents and support multiple indexes. ## Schema Schemas define the structure and types of data in your tables using **JSON Schema** with custo'
  name: Antfly Table Management API
  slug: antfly-table-management-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: Operations related to users
  name: Antfly User API
  slug: antfly-user-api
- baseURL: https://api.antfly.io
  baseurl_source: declared
  description: Operations related to API key management
  name: Antfly API Key API
  slug: antfly-api-key-api
artifact_total: 39
asyncapis:
- description: ''
  name: Antfly Webhooks
  slug: antfly-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/antfly/agentic-access/antfly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/antfly-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/antfly/plans/antfly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/antfly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/antfly/rules/antfly-rules.yml
  title: ''
  type: Spectral
  url: rules/antfly-rules.yml
- group: design
  href: https://artifacts.apis.io/antfly/json-ld/antfly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/antfly-context.jsonld
- group: design
  href: https://artifacts.apis.io/antfly/vocabulary/antfly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/antfly-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/antfly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/antfly/asyncapi/antfly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/antfly-webhooks.yml
- group: design
  href: https://artifacts.apis.io/antfly/data-model/antfly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/antfly-data-model.yml
- group: operate
  href: https://artifacts.apis.io/antfly/changelog/antfly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/antfly-changelog.yml
- group: design
  href: https://artifacts.apis.io/antfly/conventions/antfly-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/antfly-conventions.yml
- group: design
  href: https://artifacts.apis.io/antfly/conventions/antfly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/antfly-conventions.yml
- group: design
  href: https://artifacts.apis.io/antfly/errors/antfly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/antfly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/antfly/conformance/antfly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/antfly-conformance.yml
- group: other
  href: https://artifacts.apis.io/antfly/hosts/antfly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antfly-hosts.yml
- group: other
  href: https://artifacts.apis.io/antfly/vendors/antfly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/antfly-vendors.yml
- group: build
  href: https://artifacts.apis.io/antfly/packages/antfly-packages.yml
  title: ''
  type: SDKs
  url: packages/antfly-packages.yml
- group: build
  href: https://artifacts.apis.io/antfly/packages/antfly-packages.yml
  title: ''
  type: Packages
  url: packages/antfly-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://antfly.io/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://antfly.io/releases
- group: auth
  href: https://artifacts.apis.io/antfly/authentication/antfly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/antfly-authentication.yml
- group: auth
  href: https://artifacts.apis.io/antfly/security/antfly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antfly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.antfly.io
- group: docs
  title: ''
  type: Documentation
  url: https://antfly.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://antfly.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://antfly.io/docs/guides/quickstart
- group: company
  title: ''
  type: Blog
  url: https://antfly.io/thoughts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/antflydb/antfly
- group: commercial
  title: ''
  type: Pricing
  url: https://antfly.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antfly.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antfly.io/privacy
created: '2026-10-29'
description: Antfly provides a self‑learning retrieval engine for AI agents, enabling hybrid search over user‑owned data sources such as PostgreSQL, S3, and file systems. It offers built‑in vector embeddings, reranking, multimodal support (text, images, audio, video), and a knowledge graph, all running locally or in the Antfly Cloud. The platform is open‑source, free for self‑hosted use, and includes managed growth and enterprise plans with RBAC, SSO, autoscaling, and unlimited queries.
image: https://antfly.io/af-logo.svg
json_schemas:
- name: InferenceGenerateRequest
  property_count: 33
  slug: antfly-inference-generate-request
- name: MemoryInspection
  property_count: 2
  slug: antfly-memory-inspection
- name: MemoryRecallResult
  property_count: 13
  slug: antfly-memory-recall-result
- name: MemoryRecordPage
  property_count: 4
  slug: antfly-memory-record-page
- name: MemoryRecord
  property_count: 16
  slug: antfly-memory-record
- name: MemoryRelationshipProposal
  property_count: 15
  slug: antfly-memory-relationship-proposal
- name: PostAiV1ChatCompletionsRequest
  property_count: 33
  slug: antfly-post-ai-v1-chat-completions-request
- name: PostAiV1GenerateBatchRequest
  property_count: 2
  slug: antfly-post-ai-v1-generate-batch-request
- name: PostAiV1GenerateContextCheckpointRequest
  property_count: 33
  slug: antfly-post-ai-v1-generate-context-checkpoint-request
- name: PostAiV1GenerateContextPrepareRequest
  property_count: 10
  slug: antfly-post-ai-v1-generate-context-prepare-request
- name: PostAiV1GenerateRequest
  property_count: 33
  slug: antfly-post-ai-v1-generate-request
- name: PostGenerateContextCheckpointRequest
  property_count: 28
  slug: antfly-post-generate-context-checkpoint-request
jsonld:
- class_count: 120
  name: Antfly Context
  property_count: 325
  slug: antfly-context
layout: provider
modified: '2026-10-29'
name: Antfly
nav: Providers
network: true
overview: 'Antfly publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API, Cluster Management API, Data Operations API, and 17 more. Tagged areas include Artificial Intelligence, Search, Retrieval, Vectors, and Hybrid.


  The Antfly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Antfly''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Antfly Plans Pricing
  plan_count: 3
  slug: antfly-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Antfly API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 5
  slug: antfly-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 41.0
    discoverability: 67.0
    operational_transparency: 18.4
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 16
      marker_coverage: 43.2
      total: 37
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/antfly/antfly-2026-11-03T120854.png
security:
- kind: authentication
  name: Antfly Authentication
  slug: antfly-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Antfly Domain Security
  slug: antfly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: antfly
tags:
- Artificial Intelligence
- Search
- Retrieval
- Vectors
- Hybrid
website: https://www.antfly.io
---
