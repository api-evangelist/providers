---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
- acting_count: 1
  human_in_the_loop: 0
  name: Sutra Ai Agentic Access
  operation_count: 2
  slug: sutra-ai-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: OpenAI-compatible chat completions across SUTRA models.
  name: SUTRA (Two AI) Chat API
  slug: sutra-ai-chat-api
- description: List available SUTRA models.
  name: SUTRA (Two AI) Models API
  slug: sutra-ai-models-api
artifact_total: 11
asyncapis:
- description: AsyncAPI 2.6 description of SUTRA's **chat completion streaming** surface. Two AI (Numeric) does not publish a WebSocket API for SUTRA. The only asynchronous / event-style transport documented at http
  name: SUTRA Chat Completions Streaming (HTTP + SSE)
  slug: sutra-ai-asyncapi
collections:
- collection_type: open
  name: SUTRA API
  slug: open-sutra-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sutra-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sutra-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sutra-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sutra-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/two-ai
- group: company
  title: ''
  type: Website
  url: https://www.two.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.two.ai/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/sutra-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sutra-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sutra-ai-finops.yml
created: '2026-06-21'
description: SUTRA is a family of multilingual large language models from Two AI (Numeric), fluent in 50+ languages including Hindi, Gujarati, Tamil, Bengali, Korean, Arabic, and Japanese. The SUTRA API is OpenAI-compatible and serves the SUTRA-V2 instruction/conversation model and the SUTRA-R0 reasoning model through a single Bearer-authenticated REST interface.
finops:
- name: Sutra Ai Finops
  service_category: AI and Machine Learning
  slug: sutra-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sutra-ai.png
layout: provider
modified: '2026-06-21'
name: SUTRA (Two AI)
nav: Providers
network: true
overview: 'SUTRA (Two AI) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Models API. Tagged areas include AI, LLM, Multilingual, Inference, and Reasoning.


  The SUTRA (Two AI) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SUTRA (Two AI)''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Sutra Ai Plans Pricing
  plan_count: 3
  slug: sutra-ai-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 3
  name: Sutra Ai Rate Limits
  slug: sutra-ai-rate-limits
rules:
- name: SUTRA (Two AI) API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: sutra-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.6
    developer_ergonomics: 19.6
    discoverability: 60.0
    governance: 52.6
    operational_transparency: 36.8
  previous_composite: 47.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sutra Ai Authentication
  slug: sutra-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sutra Ai Domain Security
  slug: sutra-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sutra-ai
tags:
- AI
- LLM
- Multilingual
- Inference
- Reasoning
website: https://www.two.ai
---
