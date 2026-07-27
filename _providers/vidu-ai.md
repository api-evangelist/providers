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
    asyncapi_events: false
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
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Vidu Ai Agentic Access
  operation_count: 6
  slug: vidu-ai-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 2
apis:
- description: Create asynchronous video-generation tasks.
  name: Vidu Generation API
  slug: vidu-ai-generation-api
- description: Poll, list, and cancel generation tasks.
  name: Vidu Tasks API
  slug: vidu-ai-tasks-api
artifact_total: 8
collections:
- collection_type: open
  name: Vidu API
  slug: open-vidu-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vidu-ai-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vidu-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shengshu-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shengshu-technology
- group: company
  title: ''
  type: Website
  url: https://www.vidu.com
- group: docs
  title: ''
  type: Documentation
  url: https://platform.vidu.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/vidu-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vidu-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vidu-ai-finops.yml
created: '2026-07-11'
description: Vidu is a generative video AI platform from Shengshu Technology (ShengShu / 生数科技), built on the company's U-ViT diffusion-transformer architecture. The Vidu API turns text prompts, still images, and reference subjects into short video clips with features like text-to-video, image-to-video, reference-to-video (multi-entity / character consistency), start-and-end frame interpolation, and video upscaling. The API is a REST create-then-poll service - callers submit an asynchronous generation task, then poll the task status endpoint (or receive a callback) for the finished video URL. Access is open to individual developers and businesses on a prepaid, credit-based model with no application required.
finops:
- name: Vidu Ai Finops
  service_category: AI and Machine Learning
  slug: vidu-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vidu-ai.png
layout: provider
modified: '2026-07-11'
name: Vidu
nav: Providers
network: true
overview: 'Vidu publishes 2 APIs on the [APIs.io](https://apis.io/) network: Generation API and Tasks API. Tagged areas include Video Generation, AI Video, Generative AI, Text-to-Video, and Image-to-Video.


  Vidu''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Vidu Ai Plans Pricing
  plan_count: 2
  slug: vidu-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Vidu Ai Rate Limits
  slug: vidu-ai-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 3.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.6
    developer_ergonomics: 19.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Vidu Ai Authentication
  slug: vidu-ai-authentication
  summary_line: apiKey · 1 scheme
slug: vidu-ai
tags:
- Video Generation
- AI Video
- Generative AI
- Text-to-Video
- Image-to-Video
- Reference-to-Video
- U-ViT
- Diffusion
website: https://www.vidu.com
---
