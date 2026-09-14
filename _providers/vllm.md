---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Vllm Agentic Access
  operation_count: 12
  slug: vllm-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 1
apis:
- description: OpenAI-compatible REST API exposed by `vllm serve`. Endpoints include /v1/chat/completions, /v1/completions, /v1/embeddings, /v1/score, /v1/audio/transcriptions, /v1/audio/translations, /v1/realtime (
  name: vLLM OpenAI-Compatible Server
  slug: openai-compatible
- baseURL: http://localhost:8000/v1
  baseurl_source: declared
  description: OpenAI-compatible audio endpoints
  name: vLLM Audio API
  slug: vllm-audio-api
- baseURL: http://localhost:8000/v1
  baseurl_source: declared
  description: OpenAI-compatible chat completions
  name: vLLM Chat API
  slug: vllm-chat-api
- baseURL: http://localhost:8000/v1
  baseurl_source: declared
  description: OpenAI-compatible text completions
  name: vLLM Completions API
  slug: vllm-completions-api
- baseURL: http://localhost:8000/v1
  baseurl_source: declared
  description: OpenAI-compatible embeddings
  name: vLLM Embeddings API
  slug: vllm-embeddings-api
- baseURL: http://localhost:8000/v1
  baseurl_source: declared
  description: vLLM-specific scoring and reranking endpoints
  name: vLLM Scoring API
  slug: vllm-scoring-api
- baseURL: http://localhost:8000/v1
  baseurl_source: declared
  description: vLLM-specific tokenize/detokenize utilities
  name: vLLM Tokenize API
  slug: vllm-tokenize-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: vLLM OpenAI-Compatible Server Audio API
  slug: open-vllm-audio-api
- collection_type: open
  name: vLLM OpenAI-Compatible Server Audio Chat API
  slug: open-vllm-chat-api
- collection_type: open
  name: vLLM OpenAI-Compatible Server Audio Completions API
  slug: open-vllm-completions-api
- collection_type: open
  name: vLLM OpenAI-Compatible Server Audio Embeddings API
  slug: open-vllm-embeddings-api
- collection_type: open
  name: vLLM OpenAI-Compatible Server Audio Scoring API
  slug: open-vllm-scoring-api
- collection_type: open
  name: vLLM OpenAI-Compatible Server Audio Tokenize API
  slug: open-vllm-tokenize-api
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
overview: 'vLLM publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Completions API, and 3 more. Tagged areas include LLM, Inference, Open-Source, GPU, and OpenAI-Compatible.


  vLLM''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Vllm Plans Pricing
  plan_count: 1
  slug: vllm-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Vllm Rate Limits
  slug: vllm-rate-limits
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
- Open-Source
- GPU
- OpenAI-Compatible
- Self-Hosted
website: https://docs.vllm.ai/
---
