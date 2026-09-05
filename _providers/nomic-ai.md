---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Nomic Ai Agentic Access
  operation_count: 4
  slug: nomic-ai-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- description: REST API for the Nomic Atlas platform. Exposes endpoints for creating and managing datasets, building 2D semantic maps over text and image data, querying and updating points, and orchestrating long-ru
  name: Nomic Atlas API
  slug: atlas
- description: Hosted embedding endpoint backed by the Nomic Embed model family (nomic-embed-text-v1.5 and nomic-embed-vision-v1.5). Returns dense multilingual text and image vectors with Matryoshka-style configurab
  name: Nomic Embedding API
  slug: embeddings
- description: Upload, parse, and extract endpoints for ingesting PDFs and other documents into Atlas as structured text and tables prior to embedding and map building.
  name: Nomic Atlas File Parsing API
  slug: file-parsing
- description: Polling endpoint that returns the status of long-running Atlas jobs (map builds, embeddings, dataset operations).
  name: Nomic Atlas Task Status API
  slug: task-status
- description: Official Python client (nomic) for the Atlas platform, embedding API, and dataset/map workflows.
  name: Nomic Python SDK
  slug: python-sdk
- description: Official TypeScript / JavaScript client for the Nomic Atlas API.
  name: Nomic TypeScript SDK
  slug: typescript-sdk
- description: Open-source ecosystem for running large language models locally on consumer hardware. Ships a desktop chat client, a local OpenAI-compatible HTTP server, and Python and TypeScript bindings. MIT-licens
  name: GPT4All
  slug: gpt4all
- description: Open-weights multilingual text embedding model published on Hugging Face, Apache-2.0 licensed. Supports Matryoshka-style truncatable embeddings and task-type prefixes.
  name: nomic-embed-text-v1.5 (Open Weights)
  slug: embed-text-model
- description: Open-weights vision embedding model that shares an embedding space with nomic-embed-text-v1.5 to support cross-modal retrieval. Published on Hugging Face.
  name: nomic-embed-vision-v1.5 (Open Weights)
  slug: embed-vision-model
- baseURL: https://api-atlas.nomic.ai
  baseurl_source: declared
  description: The Embeddings API from Nomic AI — 1 operation(s) for embeddings.
  name: Nomic AI Embeddings API
  slug: nomic-ai-embeddings-api
- baseURL: https://api-atlas.nomic.ai
  baseurl_source: declared
  description: The Files API from Nomic AI — 2 operation(s) for files.
  name: Nomic AI Files API
  slug: nomic-ai-files-api
- baseURL: https://api-atlas.nomic.ai
  baseurl_source: declared
  description: The Tasks API from Nomic AI — 1 operation(s) for tasks.
  name: Nomic AI Tasks API
  slug: nomic-ai-tasks-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nomic Atlas Embeddings API
  slug: open-nomic-ai-embeddings-api
- collection_type: open
  name: Nomic Atlas Embeddings Files API
  slug: open-nomic-ai-files-api
- collection_type: open
  name: Nomic Atlas Embeddings Tasks API
  slug: open-nomic-ai-tasks-api
- collection_type: open
  name: Nomic Atlas API
  slug: open-nomic-ai
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/nomic-ai/nomic/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/nomic-ai/nomic/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nomic-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nomic-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nomic-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nomic-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nomic-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nomic-ai
- group: company
  title: ''
  type: Website
  url: https://www.nomic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nomic.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nomic-ai
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/nomic-ai
- group: commercial
  title: ''
  type: Plans
  url: plans/nomic-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nomic-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nomic-ai-finops.yml
created: '2026-05-23'
description: Nomic AI builds open and accessible AI infrastructure. The company is known for the open-source Nomic Embed family (nomic-embed-text-v1.5, nomic-embed-vision-v1.5) of multilingual text and vision embedding models, the Nomic Atlas platform for exploring, labelling, and operationalising unstructured data via interactive 2D maps, and the GPT4All open-source ecosystem for running large language models locally on consumer CPUs and GPUs. The Nomic Atlas REST API at api-atlas.nomic.ai exposes endpoints for datasets, maps, embeddings, file parsing, and task status, with official Python and TypeScript SDKs.
finops:
- name: Nomic Ai Finops
  service_category: API
  slug: nomic-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nomic-ai.png
layout: provider
modified: '2026-05-23'
name: Nomic AI
nav: Providers
network: true
overview: 'Nomic AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Embeddings API, Files API, and Tasks API. Tagged areas include Embeddings, Vector Database, Data Exploration, LLM, and Open-Source.


  Nomic AI''s developer surface includes authentication, documentation, GitHub presence, and 12 more developer resources.'
plans:
- name: Nomic Ai Plans Pricing
  plan_count: 1
  slug: nomic-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Nomic Ai Rate Limits
  slug: nomic-ai-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 58.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nomic-ai/refs/heads/main/screenshots/nomic-ai-2026-06-20T190456.png
security:
- kind: authentication
  name: Nomic Ai Authentication
  slug: nomic-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nomic Ai Domain Security
  slug: nomic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nomic Ai Vulnerability Disclosure
  slug: nomic-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nomic Ai Trust Center
  slug: nomic-ai-trust-center
  summary_line: SOC 2
slug: nomic-ai
tags:
- Embeddings
- Vector Database
- Data Exploration
- LLM
- Open-Source
- RAG
- Atlas
website: https://www.nomic.ai/
---
