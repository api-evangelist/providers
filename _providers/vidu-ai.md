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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Vidu Ai Agentic Access
  operation_count: 6
  slug: vidu-ai-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- description: Create asynchronous video-generation tasks.
  name: Vidu Generation API
  slug: vidu-ai-generation-api
- description: Poll, list, and cancel generation tasks.
  name: Vidu Tasks API
  slug: vidu-ai-tasks-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vidu Generation API
  slug: open-vidu-ai-generation-api
- collection_type: open
  name: Vidu Generation Tasks API
  slug: open-vidu-ai-tasks-api
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
random_paper: 15
rate_limits:
- limit_count: 3
  name: Vidu Ai Rate Limits
  slug: vidu-ai-rate-limits
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 33.8
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 50.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
