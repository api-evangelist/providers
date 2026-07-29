---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
- acting_count: 4
  human_in_the_loop: 0
  name: Targon Agentic Access
  operation_count: 6
  slug: targon-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 5
apis:
- description: OpenAI-compatible chat completions.
  name: Targon Chat API
  slug: targon-chat-api
- description: OpenAI-compatible legacy text completions.
  name: Targon Completions API
  slug: targon-completions-api
- description: Image generation from a text prompt.
  name: Targon Images API
  slug: targon-images-api
- description: List models available on Targon.
  name: Targon Models API
  slug: targon-models-api
- description: Query-based search/retrieval.
  name: Targon Search API
  slug: targon-search-api
artifact_total: 14
asyncapis:
- description: AsyncAPI 2.6 description of Targon's **chat completion streaming** surface. Targon is a decentralized AI inference platform operated as Bittensor Subnet 4 by Manifold Labs. It does not publish a WebSo
  name: Targon Chat Completions Streaming (HTTP + SSE)
  slug: targon-asyncapi
collections:
- collection_type: open
  name: Targon API
  slug: open-targon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/targon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/targon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/targon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/manifold-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manifold-labs
- group: company
  title: ''
  type: Website
  url: https://targon.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.targon.com
- group: commercial
  title: ''
  type: Plans
  url: plans/targon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/targon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/targon-finops.yml
created: '2026-06-21'
description: Targon is a decentralized AI inference platform operated as Bittensor Subnet 4 by Manifold Labs. It serves popular open models through an OpenAI-compatible REST API at https://api.targon.com/v1, where a marketplace of miners runs the inference and validators verify responses, giving developers chat, completions, image, and search endpoints over confidential, decentralized compute.
finops:
- name: Targon Finops
  service_category: AI and Machine Learning
  slug: targon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/targon.png
layout: provider
modified: '2026-06-21'
name: Targon
nav: Providers
network: true
overview: 'Targon publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Images API, and 2 more. Tagged areas include AI, LLM, Inference, Decentralized, and Bittensor.


  The Targon catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Targon''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Targon Plans Pricing
  plan_count: 2
  slug: targon-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Targon Rate Limits
  slug: targon-rate-limits
rules:
- name: Targon API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: targon-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.0
  delta: -3.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Targon Authentication
  slug: targon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Targon Domain Security
  slug: targon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: targon
tags:
- AI
- LLM
- Inference
- Decentralized
- Bittensor
website: https://targon.com
---
