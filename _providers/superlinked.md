---
access_model:
  confidence: medium
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Superlinked Agentic Access
  operation_count: 4
  slug: superlinked-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- description: The open-source Apache-2.0 Python framework (pip install superlinked) used to declare Schema, Space, Index, Query, Source, and Executor objects. The same definitions run in-memory for prototyping or p
  name: Superlinked Framework (Python)
  slug: superlinked-framework
- description: Managed, production-scale hosting of Superlinked-powered apps, available in early access via a sales-led demo. Runs the same schema-generated REST surface as the self-hosted Superlinked Server without
  name: Superlinked Cloud
  slug: superlinked-cloud
- baseURL: http://localhost:8080/api/v1
  baseurl_source: declared
  description: Endpoints to trigger and monitor configured batch data loaders.
  name: Superlinked Data Loader API
  slug: superlinked-data-loader-api
- baseURL: http://localhost:8080/api/v1
  baseurl_source: declared
  description: Schema-generated endpoints that accept records and write embeddings to the connected vector database.
  name: Superlinked Ingestion API
  slug: superlinked-ingestion-api
- baseURL: http://localhost:8080/api/v1
  baseurl_source: declared
  description: Schema-generated endpoints that run registered queries against the connected vector database.
  name: Superlinked Query API
  slug: superlinked-query-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Superlinked Server Data Loader API
  slug: open-superlinked-data-loader-api
- collection_type: open
  name: Superlinked Server Data Loader Ingestion API
  slug: open-superlinked-ingestion-api
- collection_type: open
  name: Superlinked Server Data Loader Query API
  slug: open-superlinked-query-api
- collection_type: open
  name: Superlinked Server API
  slug: open-superlinked
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/superlinked-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/superlinked-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superlinked-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superlinked-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://superlinked.com/blog
created: '2026-06-20'
description: Superlinked is an open-source Python framework for building vector-compute pipelines that encode structured and unstructured data into multi-modal embeddings for retrieval, recommendations, RAG, and analytics. When deployed via the Superlinked Server, the framework auto-generates a REST API - ingestion and query endpoints derived directly from your schema, index, and query definitions - and connects to external vector databases. A managed Superlinked Cloud is available in early access.
finops:
- name: Superlinked Finops
  service_category: AI and Machine Learning
  slug: superlinked-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superlinked.png
layout: provider
modified: '2026-06-20'
name: Superlinked
nav: Providers
network: true
overview: 'Superlinked publishes 3 APIs on the [APIs.io](https://apis.io/) network: Data Loader API, Ingestion API, and Query API. Tagged areas include Vectors, Embeddings, Vector Search, Retrieval, and Recommendations.


  Superlinked''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Superlinked Plans Pricing
  plan_count: 2
  slug: superlinked-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Superlinked Rate Limits
  slug: superlinked-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 47.4
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superlinked/refs/heads/main/screenshots/superlinked-2026-06-20T194718.png
security:
- kind: authentication
  name: Superlinked Authentication
  slug: superlinked-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Superlinked Domain Security
  slug: superlinked-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Superlinked Vulnerability Disclosure
  slug: superlinked-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: superlinked
tags:
- Vectors
- Embeddings
- Vector Search
- Retrieval
- Recommendations
- RAG
---
