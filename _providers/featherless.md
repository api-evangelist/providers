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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Featherless Agentic Access
  operation_count: 4
  slug: featherless-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 4
apis:
- description: OpenAI-compatible chat completions.
  name: Featherless AI Chat API
  slug: featherless-chat-api
- description: OpenAI-compatible legacy text completions.
  name: Featherless AI Completions API
  slug: featherless-completions-api
- description: OpenAI-compatible text embeddings.
  name: Featherless AI Embeddings API
  slug: featherless-embeddings-api
- description: Model catalog discovery.
  name: Featherless AI Models API
  slug: featherless-models-api
artifact_total: 13
asyncapis:
- description: AsyncAPI 2.6 description of Featherless AI's **chat completion streaming** surface. Featherless AI's core inference API is OpenAI-compatible and does not publish a WebSocket API for chat. The asynchro
  name: Featherless AI Chat Completions Streaming (HTTP + SSE)
  slug: featherless-asyncapi
collections:
- collection_type: open
  name: Featherless AI API
  slug: open-featherless
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/featherless-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/featherless-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/featherless-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/featherless-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/featherless-ai
- group: company
  title: ''
  type: Website
  url: https://featherless.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://featherless.ai/docs/quickstart-guide
- group: commercial
  title: ''
  type: Plans
  url: plans/featherless-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/featherless-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/featherless-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://featherless.ai/blog
created: '2026-06-21'
description: Featherless AI is a serverless LLM inference platform that serves thousands of open-weight models from the Hugging Face catalog behind a single OpenAI-compatible REST API. It uses flat monthly subscription pricing with unlimited tokens rather than per-token billing, exposing chat completions, text completions, an embeddings endpoint, and a large models catalog.
finops:
- name: Featherless Finops
  service_category: AI and Machine Learning
  slug: featherless-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/featherless.png
layout: provider
modified: '2026-06-21'
name: Featherless AI
nav: Providers
network: true
overview: 'Featherless AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Embeddings API, and 1 more. Tagged areas include AI, LLM, Inference, Serverless, and Open Models.


  The Featherless AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Featherless AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Featherless Plans Pricing
  plan_count: 4
  slug: featherless-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Featherless Rate Limits
  slug: featherless-rate-limits
rules:
- name: Featherless AI API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: featherless-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.0
  delta: -3.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/featherless/refs/heads/main/screenshots/featherless-2026-07-25T214310.png
security:
- kind: authentication
  name: Featherless Authentication
  slug: featherless-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Featherless Domain Security
  slug: featherless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: featherless
tags:
- AI
- LLM
- Inference
- Serverless
- Open Models
website: https://featherless.ai/
---
