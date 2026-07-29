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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Reka Ai Agentic Access
  operation_count: 11
  slug: reka-ai-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 6
apis:
- description: 'Multimodal API surface from Reka AI: Chat (text + vision multimodal), Vision (video upload, search, Q&A, clip generation), Research (web search with reasoning and citations), and Speech (audio transcr'
  name: Reka AI Platform API
  slug: platform
- description: Chat completions over Reka multimodal models.
  name: Reka AI Chat API
  slug: reka-ai-chat-api
- description: List available Reka models.
  name: Reka AI Models API
  slug: reka-ai-models-api
- description: OpenAI-compatible chat with optional web search and citations.
  name: Reka AI Research API
  slug: reka-ai-research-api
- description: Audio transcription and translation.
  name: Reka AI Speech API
  slug: reka-ai-speech-api
- description: Video and image management, search, Q&A, and clips.
  name: Reka AI Vision API
  slug: reka-ai-vision-api
artifact_total: 14
collections:
- collection_type: open
  name: Reka AI Platform API
  slug: open-reka-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reka-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/reka-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reka-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reka-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reka-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reka-ai
- group: company
  title: ''
  type: Website
  url: https://www.reka.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reka.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/reka-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reka-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reka-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.reka.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://reka.ai/news
created: '2026-05-08'
description: Reka AI is a multimodal foundation model company offering Reka Core, Flash, Edge, and Vision models that natively process text, images, video, and audio. The Reka platform exposes Chat, Vision, Research, and Speech APIs.
finops:
- name: Reka Ai Finops
  service_category: AI
  slug: reka-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reka-ai.png
layout: provider
modified: '2026-05-08'
name: Reka AI
nav: Providers
network: true
overview: 'Reka AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Models API, Research API, and 2 more. Tagged areas include AI, LLM, Inference, Multimodal, and Foundation Models.


  Reka AI''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Reka Ai Plans Pricing
  plan_count: 1
  slug: reka-ai-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 1
  name: Reka Ai Rate Limits
  slug: reka-ai-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -2.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 55.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/reka-ai/refs/heads/main/screenshots/reka-ai-2026-06-20T192937.png
security:
- kind: authentication
  name: Reka Ai Authentication
  slug: reka-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Reka Ai Domain Security
  slug: reka-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reka Ai Trust Center
  slug: reka-ai-trust-center
  summary_line: SOC 2
slug: reka-ai
tags:
- AI
- LLM
- Inference
- Multimodal
- Foundation Models
- Vision
website: https://www.reka.ai/
---
