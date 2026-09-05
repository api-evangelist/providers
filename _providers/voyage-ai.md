---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 18.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Reranking endpoint that scores a list of candidate documents against a query and returns relevance scores. Powered by the voyage-rerank-2 model family, used downstream of vector search to improve retr
  name: Voyage AI Rerank API
  slug: rerank
- description: Multimodal embeddings endpoint backed by voyage-multimodal-3 that accepts interleaved text and images in a single request and returns embeddings in a shared vector space, enabling cross-modal retrieva
  name: Voyage AI Multimodal Embeddings API
  slug: multimodal-embeddings
- description: Endpoint that embeds chunks while conditioning on surrounding document context, improving recall for long-document RAG workflows where chunk embeddings would otherwise lose document-level signal.
  name: Voyage AI Contextualized Embeddings API
  slug: contextualized-embeddings
- description: Official Python client (voyageai) wrapping the embeddings, multimodal, contextualized, and reranking endpoints with batching, retries, and async support.
  name: Voyage AI Python SDK
  slug: python-sdk
- description: Official TypeScript / JavaScript client for the Voyage AI REST API.
  name: Voyage AI TypeScript SDK
  slug: typescript-sdk
- baseURL: https://api.voyageai.com/v1
  baseurl_source: declared
  description: Embed chunks conditioned on surrounding document context.
  name: Voyage AI Contextualized API
  slug: voyage-ai-contextualized-api
- baseURL: https://api.voyageai.com/v1
  baseurl_source: declared
  description: Dense text embeddings.
  name: Voyage AI Embeddings API
  slug: voyage-ai-embeddings-api
- baseURL: https://api.voyageai.com/v1
  baseurl_source: declared
  description: Embed interleaved text and images in a shared vector space.
  name: Voyage AI Multimodal API
  slug: voyage-ai-multimodal-api
- baseURL: https://api.voyageai.com/v1
  baseurl_source: declared
  description: Cross-encoder reranking of candidate documents.
  name: Voyage AI Rerank API
  slug: voyage-ai-rerank-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Voyage AI Contextualized API
  slug: open-voyage-ai-contextualized-api
- collection_type: open
  name: Voyage AI Embeddings API
  slug: open-voyage-ai-embeddings-api
- collection_type: open
  name: Voyage AI Multimodal API
  slug: open-voyage-ai-multimodal-api
- collection_type: open
  name: Voyage AI Rerank API
  slug: open-voyage-ai-rerank-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/voyage-ai/voyageai-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/voyage-ai/voyageai-python/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/voyage-ai/voyageai-python/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voyage-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voyage-ai
- group: company
  title: ''
  type: Website
  url: https://www.voyageai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.voyageai.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/voyage-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.voyageai.com/docs/pricing
- group: other
  title: ''
  type: Parent
  url: https://www.mongodb.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/voyage-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voyage-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/voyage-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.voyageai.com/feed
created: '2026-05-23'
description: Voyage AI builds state-of-the-art embedding and reranker models for retrieval-augmented generation (RAG) and semantic search. The platform exposes an OpenAI-style REST API at api.voyageai.com/v1 for text embeddings, multimodal embeddings, contextualized embeddings, and reranking, with Python and TypeScript SDKs. Model families include voyage-3.x and voyage-4.x text embeddings, voyage-code-3, domain-specialised models (voyage-finance-2, voyage-law-2), voyage-multimodal-3, and the voyage-rerank-2 reranker family. Voyage AI was acquired by MongoDB in February 2024 and is integrated into MongoDB Atlas Vector Search; models are also distributed via AWS Marketplace, Azure Marketplace, and Snowflake.
finops:
- name: Voyage Ai Finops
  service_category: API
  slug: voyage-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voyage-ai.png
layout: provider
modified: '2026-05-23'
name: Voyage AI
nav: Providers
network: true
overview: 'Voyage AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Contextualized API, Embeddings API, Multimodal API, and 1 more. Tagged areas include Embeddings, Rerankers, RAG, Semantic Search, and AI Models.


  Voyage AI''s developer surface includes documentation, GitHub presence, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Voyage Ai Plans Pricing
  plan_count: 1
  slug: voyage-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Voyage Ai Rate Limits
  slug: voyage-ai-rate-limits
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 33.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voyage-ai/refs/heads/main/screenshots/voyage-ai-2026-06-20T201141.png
security:
- kind: domain-security
  name: Voyage Ai Domain Security
  slug: voyage-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voyage-ai
tags:
- Embeddings
- Rerankers
- RAG
- Semantic Search
- AI Models
- Vector Search
- Multi-Modal
website: https://www.voyageai.com/
---
