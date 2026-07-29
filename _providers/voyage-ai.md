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
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: OpenAI-compatible REST endpoint that returns dense vector embeddings for input text. Supports model selection (voyage-3.5, voyage-3-large, voyage-code-3, voyage-finance-2, voyage-law-2, voyage-4 famil
  name: Voyage AI Embeddings API
  slug: embeddings
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
artifact_total: 10
common:
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
overview: 'Voyage AI publishes 1 API on the [APIs.io](https://apis.io/) network: Embeddings API. Tagged areas include Embeddings, Rerankers, RAG, Semantic Search, and AI Models.


  Voyage AI''s developer surface includes documentation, GitHub presence, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Voyage Ai Plans Pricing
  plan_count: 1
  slug: voyage-ai-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 2
  name: Voyage Ai Rate Limits
  slug: voyage-ai-rate-limits
score:
  band: thin
  composite: 31.0
  delta: -1.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 40.3
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Multimodal
website: https://www.voyageai.com/
---
