---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
- acting_count: 2
  human_in_the_loop: 0
  name: Martian Ai Agentic Access
  operation_count: 3
  slug: martian-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: The Chat Completions API from Martian — 1 operation(s) for chat completions.
  name: Martian Chat Completions API
  slug: martian-ai-chat-completions-api
- description: The Messages API from Martian — 1 operation(s) for messages.
  name: Martian Messages API
  slug: martian-ai-messages-api
- description: The Models API from Martian — 1 operation(s) for models.
  name: Martian Models API
  slug: martian-ai-models-api
artifact_total: 12
asyncapis:
- description: AsyncAPI 2.6 description of the Martian Gateway's **chat completion streaming** surface. Martian does not publish a WebSocket API. The Martian Gateway is an OpenAI-compatible model router; its only as
  name: Martian Gateway Chat Completions Streaming (HTTP + SSE)
  slug: martian-ai-asyncapi
collections:
- collection_type: open
  name: Martian Gateway API
  slug: open-martian-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/martian-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/martian-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/martian-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withmartian
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/withmartian
- group: company
  title: ''
  type: Website
  url: https://www.withmartian.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withmartian.com
- group: commercial
  title: ''
  type: Plans
  url: plans/martian-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/martian-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/martian-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.withmartian.com/blog
created: '2026-06-20'
description: Martian operates an LLM model router and gateway that dynamically routes each request to the best underlying model across providers for the optimal balance of quality, latency, and cost. The Martian Gateway exposes a drop-in, OpenAI-compatible REST API (and an Anthropic Messages-compatible surface) so applications can route across a large catalog of models by changing only the base URL.
finops:
- name: Martian Ai Finops
  service_category: AI and Machine Learning
  slug: martian-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/martian-ai.png
layout: provider
modified: '2026-06-20'
name: Martian
nav: Providers
network: true
overview: 'Martian publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chat Completions API, Messages API, and Models API. Tagged areas include AI, LLM, Model Router, Gateway, and Cost Optimization.


  The Martian catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Martian''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Martian Ai Plans Pricing
  plan_count: 3
  slug: martian-ai-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 4
  name: Martian Ai Rate Limits
  slug: martian-ai-rate-limits
rules:
- name: Martian API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: martian-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.5
  delta: -3.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/screenshots/martian-ai-2026-06-20T185007.png
security:
- kind: authentication
  name: Martian Ai Authentication
  slug: martian-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Martian Ai Domain Security
  slug: martian-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: martian-ai
tags:
- AI
- LLM
- Model Router
- Gateway
- Cost Optimization
website: https://www.withmartian.com
---
