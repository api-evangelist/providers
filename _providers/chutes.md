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
- acting_count: 8
  human_in_the_loop: 0
  name: Chutes Agentic Access
  operation_count: 17
  slug: chutes-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 4
apis:
- description: OpenAI-compatible chat completions.
  name: Chutes Chat API
  slug: chutes-chat-api
- description: Deploy, list, retrieve, update, and delete chutes.
  name: Chutes Chutes API
  slug: chutes-chutes-api
- description: Build, list, retrieve, and delete container images.
  name: Chutes Images API
  slug: chutes-images-api
- description: List models available on the Chutes network.
  name: Chutes Models API
  slug: chutes-models-api
artifact_total: 13
asyncapis:
- description: AsyncAPI 2.6 description of Chutes' **chat completion streaming** surface. Chutes does not publish a public WebSocket API. The only asynchronous / event-style transport documented at https://chutes.ai
  name: Chutes Chat Completions Streaming (HTTP + SSE)
  slug: chutes-asyncapi
collections:
- collection_type: open
  name: Chutes API
  slug: open-chutes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chutes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chutes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chutes-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rayonlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chutesai
- group: company
  title: ''
  type: Website
  url: https://chutes.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://chutes.ai/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/chutes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chutes-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chutes-finops.yml
created: '2026-06-21'
description: Chutes is a permissionless, serverless AI compute platform that lets developers deploy and run any model as an autoscaling "chute" on decentralized GPU capacity (Bittensor Subnet 64). It exposes a single OpenAI-compatible inference endpoint at llm.chutes.ai/v1 for hundreds of open-source LLMs, plus a management REST API at api.chutes.ai for building images and deploying, listing, and operating chutes.
finops:
- name: Chutes Finops
  service_category: AI and Machine Learning
  slug: chutes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chutes.png
layout: provider
modified: '2026-06-21'
name: Chutes
nav: Providers
network: true
overview: 'Chutes publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Chutes API, Images API, and 1 more. Tagged areas include AI, LLM, Inference, Serverless, and GPU.


  The Chutes catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Chutes'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Chutes Plans Pricing
  plan_count: 5
  slug: chutes-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Chutes Rate Limits
  slug: chutes-rate-limits
rules:
- name: Chutes API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: chutes-asyncapi-spectral-rules
score:
  band: developing
  composite: 46.2
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 50.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/chutes/refs/heads/main/screenshots/chutes-2026-07-25T205333.png
security:
- kind: authentication
  name: Chutes Authentication
  slug: chutes-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chutes Domain Security
  slug: chutes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chutes
tags:
- AI
- LLM
- Inference
- Serverless
- GPU
- Bittensor
website: https://chutes.ai/
---
