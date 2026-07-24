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
- acting_count: 4
  human_in_the_loop: 0
  name: Nscale Agentic Access
  operation_count: 6
  slug: nscale-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 5
apis:
- description: OpenAI-compatible chat completions.
  name: Nscale Chat API
  slug: nscale-chat-api
- description: OpenAI-compatible legacy text completions.
  name: Nscale Completions API
  slug: nscale-completions-api
- description: Vector embeddings of text input.
  name: Nscale Embeddings API
  slug: nscale-embeddings-api
- description: Text-to-image generation.
  name: Nscale Images API
  slug: nscale-images-api
- description: Model catalog discovery.
  name: Nscale Models API
  slug: nscale-models-api
artifact_total: 14
asyncapis:
- description: 'AsyncAPI 2.6 description of Nscale''s **chat completion streaming** surface. Nscale does not publish a WebSocket API. The only asynchronous / event-style transport documented for the OpenAI-compatible '
  name: Nscale Chat Completions Streaming (HTTP + SSE)
  slug: nscale-asyncapi
collections:
- collection_type: open
  name: Nscale Serverless Inference API
  slug: open-nscale
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nscale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nscale-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nscale.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nscale
- group: company
  title: ''
  type: Website
  url: https://www.nscale.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nscale.com
- group: commercial
  title: ''
  type: Plans
  url: plans/nscale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nscale-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nscale-finops.yml
created: '2026-06-21'
description: Nscale is an AI/GPU cloud that pairs serverless, OpenAI-compatible inference with on-demand GPU compute. The Serverless Inference API serves open models (Llama, Qwen, DeepSeek, GPT OSS, Mistral, Flux) at https://inference.api.nscale.com/v1 with pay-per-token billing, while the platform API provisions GPU clusters, compute instances, networks, and storage.
finops:
- name: Nscale Finops
  service_category: AI and Machine Learning
  slug: nscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nscale.png
layout: provider
modified: '2026-06-21'
name: Nscale
nav: Providers
network: true
overview: 'Nscale publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Embeddings API, and 2 more. Tagged areas include AI, GPU, Inference, Serverless, and Cloud Compute.


  The Nscale catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Nscale''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Nscale Plans Pricing
  plan_count: 3
  slug: nscale-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Nscale Rate Limits
  slug: nscale-rate-limits
rules:
- name: Nscale API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: nscale-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.9
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 31.6
  previous_composite: 47.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Nscale Authentication
  slug: nscale-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nscale Domain Security
  slug: nscale-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nscale
tags:
- AI
- GPU
- Inference
- Serverless
- Cloud Compute
website: https://www.nscale.com
---
