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
- acting_count: 8
  human_in_the_loop: 1
  name: Llamacloud Agentic Access
  operation_count: 19
  slug: llamacloud-agentic-access
  summary_line: 19 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.cloud.llamaindex.ai/api/v1
  baseurl_source: declared
  description: Files and pipeline documents.
  name: LlamaCloud Documents API
  slug: llamacloud-documents-api
- baseURL: https://api.cloud.llamaindex.ai/api/v1
  baseurl_source: declared
  description: LlamaExtract schema-driven structured extraction.
  name: LlamaCloud Extraction API
  slug: llamacloud-extraction-api
- baseURL: https://api.cloud.llamaindex.ai/api/v1
  baseurl_source: declared
  description: LlamaParse document parsing jobs and results.
  name: LlamaCloud Parsing API
  slug: llamacloud-parsing-api
- baseURL: https://api.cloud.llamaindex.ai/api/v1
  baseurl_source: declared
  description: Managed ingestion and indexing pipelines.
  name: LlamaCloud Pipelines API
  slug: llamacloud-pipelines-api
- baseURL: https://api.cloud.llamaindex.ai/api/v1
  baseurl_source: declared
  description: Query a managed index for relevant chunks.
  name: LlamaCloud Retrieval API
  slug: llamacloud-retrieval-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LlamaCloud Documents API
  slug: open-llamacloud-documents-api
- collection_type: open
  name: LlamaCloud Documents Extraction API
  slug: open-llamacloud-extraction-api
- collection_type: open
  name: LlamaCloud Documents Parsing API
  slug: open-llamacloud-parsing-api
- collection_type: open
  name: LlamaCloud Documents Pipelines API
  slug: open-llamacloud-pipelines-api
- collection_type: open
  name: LlamaCloud Documents Retrieval API
  slug: open-llamacloud-retrieval-api
- collection_type: open
  name: LlamaCloud API
  slug: open-llamacloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/llamacloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/llamacloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/llamacloud-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/run-llama
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/llamaindex
- group: company
  title: ''
  type: Website
  url: https://cloud.llamaindex.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.llamaindex.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/llamacloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/llamacloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/llamacloud-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.llamaindex.ai/blog
created: '2026-06-20'
description: LlamaCloud is the managed document parsing, extraction, indexing, and retrieval platform from LlamaIndex. It exposes REST APIs at https://api.cloud.llamaindex.ai for LlamaParse (document parsing to Markdown/JSON), managed ingestion pipelines and indexes, document management, retrieval, and LlamaExtract (schema-driven structured extraction), all secured with a Bearer API key. This is the hosted cloud platform, distinct from the open-source LlamaIndex framework.
finops:
- name: Llamacloud Finops
  service_category: AI and Machine Learning
  slug: llamacloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/llamacloud.png
layout: provider
modified: '2026-06-20'
name: LlamaCloud
nav: Providers
network: true
overview: 'LlamaCloud publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Extraction API, Parsing API, and 2 more. Tagged areas include Artificial Intelligence, Document Parsing, Extraction, Indexing, and Retrieval.


  LlamaCloud''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Llamacloud Plans Pricing
  plan_count: 5
  slug: llamacloud-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Llamacloud Rate Limits
  slug: llamacloud-rate-limits
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.9
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/llamacloud/refs/heads/main/screenshots/llamacloud-2026-06-20T184622.png
security:
- kind: authentication
  name: Llamacloud Authentication
  slug: llamacloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Llamacloud Domain Security
  slug: llamacloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: llamacloud
tags:
- Artificial Intelligence
- Document Parsing
- Extraction
- Indexing
- Retrieval
- RAG
website: https://cloud.llamaindex.ai
---
