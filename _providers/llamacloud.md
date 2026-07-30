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
- acting_count: 8
  human_in_the_loop: 1
  name: Llamacloud Agentic Access
  operation_count: 19
  slug: llamacloud-agentic-access
  summary_line: 19 operations · 8 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: Files and pipeline documents.
  name: LlamaCloud Documents API
  slug: llamacloud-documents-api
- description: LlamaExtract schema-driven structured extraction.
  name: LlamaCloud Extraction API
  slug: llamacloud-extraction-api
- description: LlamaParse document parsing jobs and results.
  name: LlamaCloud Parsing API
  slug: llamacloud-parsing-api
- description: Managed ingestion and indexing pipelines.
  name: LlamaCloud Pipelines API
  slug: llamacloud-pipelines-api
- description: Query a managed index for relevant chunks.
  name: LlamaCloud Retrieval API
  slug: llamacloud-retrieval-api
artifact_total: 12
collections:
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
overview: 'LlamaCloud publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Extraction API, Parsing API, and 2 more. Tagged areas include AI, Document Parsing, Extraction, Indexing, and Retrieval.


  LlamaCloud''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Llamacloud Plans Pricing
  plan_count: 5
  slug: llamacloud-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Llamacloud Rate Limits
  slug: llamacloud-rate-limits
score:
  band: thin
  composite: 38.5
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- AI
- Document Parsing
- Extraction
- Indexing
- Retrieval
- RAG
website: https://cloud.llamaindex.ai
---
