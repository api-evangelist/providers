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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Moonshot Ai Agentic Access
  operation_count: 13
  slug: moonshot-ai-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 6
apis:
- description: The Batch API from Moonshot AI — 3 operation(s) for batch.
  name: Moonshot AI Batch API
  slug: moonshot-ai-batch-api
- description: The Billing API from Moonshot AI — 1 operation(s) for billing.
  name: Moonshot AI Billing API
  slug: moonshot-ai-billing-api
- description: The Chat API from Moonshot AI — 1 operation(s) for chat.
  name: Moonshot AI Chat API
  slug: moonshot-ai-chat-api
- description: The Files API from Moonshot AI — 3 operation(s) for files.
  name: Moonshot AI Files API
  slug: moonshot-ai-files-api
- description: The Models API from Moonshot AI — 1 operation(s) for models.
  name: Moonshot AI Models API
  slug: moonshot-ai-models-api
- description: The Utilities API from Moonshot AI — 1 operation(s) for utilities.
  name: Moonshot AI Utilities API
  slug: moonshot-ai-utilities-api
artifact_total: 15
asyncapis:
- description: 'AsyncAPI 2.6 description of the Moonshot AI streaming chat completions surface. Moonshot''s `/v1/chat/completions` endpoint is OpenAI-compatible and, when invoked with `stream: true`, delivers incremen'
  name: Moonshot AI Chat Completions Streaming API
  slug: moonshot-ai-chat-completions-asyncapi
collections:
- collection_type: open
  name: Moonshot AI API
  slug: open-moonshot-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moonshot-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moonshot-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moonshot-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MoonshotAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moonshot-ai-linkedin
- group: company
  title: ''
  type: Website
  url: https://www.moonshot.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.kimi.ai/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/moonshot-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moonshot-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moonshot-ai-finops.yml
created: '2026-05-08'
description: Moonshot AI is a Chinese foundation model company best known for Kimi, an LLM with industry-leading long-context capabilities. The Moonshot platform exposes OpenAI-compatible chat completion, files, batch, models, balance, and token-estimation APIs.
finops:
- name: Moonshot Ai Finops
  service_category: AI and Machine Learning
  slug: moonshot-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moonshot-ai.png
layout: provider
modified: '2026-05-30'
name: Moonshot AI
nav: Providers
network: true
overview: 'Moonshot AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Billing API, Chat API, and 3 more. Tagged areas include AI, LLM, Inference, Long Context, and Kimi.


  The Moonshot AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Moonshot AI''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Moonshot Ai Plans Pricing
  plan_count: 2
  slug: moonshot-ai-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Moonshot Ai Rate Limits
  slug: moonshot-ai-rate-limits
rules:
- name: Moonshot AI API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: moonshot-ai-asyncapi-spectral-rules
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 66.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 13.2
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moonshot-ai/refs/heads/main/screenshots/moonshot-ai-2026-06-20T185801.png
security:
- kind: authentication
  name: Moonshot Ai Authentication
  slug: moonshot-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Moonshot Ai Domain Security
  slug: moonshot-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moonshot-ai
tags:
- AI
- LLM
- Inference
- Long Context
- Kimi
website: https://www.moonshot.ai/
---
