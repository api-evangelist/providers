---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
- acting_count: 12
  human_in_the_loop: 0
  name: Vllm Agentic Access
  operation_count: 12
  slug: vllm-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 7
apis:
- description: OpenAI-compatible REST API exposed by `vllm serve`. Endpoints include /v1/chat/completions, /v1/completions, /v1/embeddings, /v1/score, /v1/audio/transcriptions, /v1/audio/translations, /v1/realtime (
  name: vLLM OpenAI-Compatible Server
  slug: openai-compatible
- description: OpenAI-compatible audio endpoints
  name: vLLM Audio API
  slug: vllm-audio-api
- description: OpenAI-compatible chat completions
  name: vLLM Chat API
  slug: vllm-chat-api
- description: OpenAI-compatible text completions
  name: vLLM Completions API
  slug: vllm-completions-api
- description: OpenAI-compatible embeddings
  name: vLLM Embeddings API
  slug: vllm-embeddings-api
- description: vLLM-specific scoring and reranking endpoints
  name: vLLM Scoring API
  slug: vllm-scoring-api
- description: vLLM-specific tokenize/detokenize utilities
  name: vLLM Tokenize API
  slug: vllm-tokenize-api
artifact_total: 14
collections:
- collection_type: open
  name: vLLM OpenAI-Compatible Server
  slug: open-vllm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vllm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vllm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vllm-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vllm-project
- group: company
  title: ''
  type: Website
  url: https://docs.vllm.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vllm.ai/
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/vllm-project/vllm
- group: commercial
  title: ''
  type: Plans
  url: plans/vllm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vllm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vllm-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://vllm.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://vllm.ai/blog/rss.xml
created: '2026-05-08'
description: vLLM is a high-throughput, memory-efficient open-source inference and serving engine for LLMs. It provides an OpenAI-compatible REST server (vllm serve) plus a Python API. vLLM is Apache 2.0 and run on your own GPU infrastructure; there is no hosted vLLM SaaS from the project itself.
finops:
- name: Vllm Finops
  service_category: LLM Inference
  slug: vllm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vllm.png
layout: provider
modified: '2026-05-08'
name: vLLM
nav: Providers
network: true
overview: 'vLLM publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Completions API, and 3 more. Tagged areas include LLM, Inference, Open Source, GPU, and OpenAI Compatible.


  vLLM''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Vllm Plans Pricing
  plan_count: 1
  slug: vllm-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 2
  name: Vllm Rate Limits
  slug: vllm-rate-limits
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.3
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vllm/refs/heads/main/screenshots/vllm-2026-06-20T201117.png
security:
- kind: authentication
  name: Vllm Authentication
  slug: vllm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vllm Domain Security
  slug: vllm-domain-security
  summary_line: TLSv1.3
slug: vllm
tags:
- LLM
- Inference
- Open Source
- GPU
- OpenAI Compatible
- Self-Hosted
website: https://docs.vllm.ai/
---
