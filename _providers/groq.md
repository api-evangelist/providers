---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Groq Agentic Access
  operation_count: 23
  slug: groq-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 9
apis:
- description: The Audio API from Groq — 3 operation(s) for audio.
  name: Groq Audio API
  slug: groq-audio-api
- description: The Batch API from Groq — 3 operation(s) for batch.
  name: Groq Batch API
  slug: groq-batch-api
- description: The Chat API from Groq — 1 operation(s) for chat.
  name: Groq Chat API
  slug: groq-chat-api
- description: The Embeddings API from Groq — 1 operation(s) for embeddings.
  name: Groq Embeddings API
  slug: groq-embeddings-api
- description: The Files API from Groq — 3 operation(s) for files.
  name: Groq Files API
  slug: groq-files-api
- description: The Fine Tuning API from Groq — 2 operation(s) for fine tuning.
  name: Groq Fine Tuning API
  slug: groq-fine-tuning-api
- description: The Models API from Groq — 2 operation(s) for models.
  name: Groq Models API
  slug: groq-models-api
- description: The Reranking API from Groq — 1 operation(s) for reranking.
  name: Groq Reranking API
  slug: groq-reranking-api
- description: The Responses API from Groq — 1 operation(s) for responses.
  name: Groq Responses API
  slug: groq-responses-api
artifact_total: 21
asyncapis:
- description: AsyncAPI 2.6 description of Groq's **chat completion streaming** surface. Groq does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://console.groq.com/do
  name: Groq Chat Completions Streaming (HTTP + SSE)
  slug: groq-asyncapi
collections:
- collection_type: open
  name: GroqCloud API
  slug: open-groq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/groq-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/groq-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/groq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/groq-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/groq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/groq
- group: company
  title: ''
  type: Website
  url: https://groq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://console.groq.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/groq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/groq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/groq-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://groq.com/blog
created: '2026-05-08'
description: Groq builds custom Language Processing Unit (LPU) silicon optimized for low-latency LLM inference. The GroqCloud API serves popular open models (Llama, GPT OSS, Whisper, Orpheus) at industry-leading tokens-per-second with an OpenAI-compatible interface.
finops:
- name: Groq Finops
  service_category: AI and Machine Learning
  slug: groq-finops
graphqls:
- description: Groq provides ultra-fast LLM inference via their Language Processing Unit (LPU) hardware. The API is OpenAI-compatible and covers chat completions, audio transcription, and batch processing with model
  name: Groq GraphQL API
  slug: groq-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-05-29'
name: Groq
nav: Providers
network: true
overview: 'Groq publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Batch API, Chat API, and 6 more. Tagged areas include AI, LLM, Inference, LPU, and Low Latency.


  The Groq catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Groq''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Groq Plans Pricing
  plan_count: 4
  slug: groq-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 6
  name: Groq Rate Limits
  slug: groq-rate-limits
rules:
- name: Groq API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: groq-asyncapi-spectral-rules
score:
  band: developing
  composite: 46.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 61.0
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 36.8
  previous_composite: 46.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groq/refs/heads/main/screenshots/groq-2026-06-20T182414.png
security:
- kind: authentication
  name: Groq Authentication
  slug: groq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Groq Domain Security
  slug: groq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Groq Vulnerability Disclosure
  slug: groq-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Groq Trust Center
  slug: groq-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: groq
tags:
- AI
- LLM
- Inference
- LPU
- Low Latency
website: https://groq.com/
---
