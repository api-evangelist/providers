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
  name: Akool Agentic Access
  operation_count: 13
  slug: akool-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 7
apis:
- description: Mint a Bearer token from a clientId / clientSecret pair.
  name: Akool Authentication API
  slug: akool-authentication-api
- description: Swap a source face onto a target image or video.
  name: Akool Face Swap API
  slug: akool-face-swap-api
- description: Text-to-image and image-to-image generation.
  name: Akool Image Generation API
  slug: akool-image-generation-api
- description: Real-time streaming avatar sessions over WebRTC (Agora / LiveKit / TRTC).
  name: Akool Live Avatar API
  slug: akool-live-avatar-api
- description: Generate a speaking avatar video from text or audio.
  name: Akool Talking Avatar API
  slug: akool-talking-avatar-api
- description: Animate a still portrait into a talking video.
  name: Akool Talking Photo API
  slug: akool-talking-photo-api
- description: Translate a video into other languages with optional lip-sync.
  name: Akool Video Translation API
  slug: akool-video-translation-api
artifact_total: 13
collections:
- collection_type: open
  name: Akool OpenAPI
  slug: open-akool
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akool-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akool-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AKOOL-Official
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akoolai
- group: company
  title: ''
  type: Website
  url: https://akool.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akool.com
- group: commercial
  title: ''
  type: Plans
  url: plans/akool-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/akool-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/akool-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://akool.com/blog
created: '2026-07-11'
description: Akool is a generative AI platform for video and imagery - talking avatars, talking photos, face swap, video translation with lip-sync, background change, image generation, and a real-time streaming (live) avatar product. The Akool OpenAPI exposes these tools as an HTTPS REST API under https://openapi.akool.com, authenticated with a Bearer token minted from a clientId / clientSecret pair (or a direct x-api-key). Generation is asynchronous - callers create a task, then poll by id or receive an encrypted webhook callback when the task completes. The Live Avatar product opens a real-time session whose media is carried over a third-party WebRTC transport (Agora, LiveKit, or TRTC).
finops:
- name: Akool Finops
  service_category: AI and Machine Learning
  slug: akool-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akool.png
layout: provider
modified: '2026-07-11'
name: Akool
nav: Providers
network: true
overview: 'Akool publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Face Swap API, Image Generation API, and 4 more. Tagged areas include AI Avatars, Video Generation, AI Video, Face Swap, and Generative AI.


  Akool''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Akool Plans Pricing
  plan_count: 5
  slug: akool-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 4
  name: Akool Rate Limits
  slug: akool-rate-limits
score:
  band: thin
  composite: 35.5
  delta: -5.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 44.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/akool/refs/heads/main/screenshots/akool-2026-07-25T195517.png
security:
- kind: authentication
  name: Akool Authentication
  slug: akool-authentication
  summary_line: http/apiKey · 2 schemes
slug: akool
tags:
- AI Avatars
- Video Generation
- AI Video
- Face Swap
- Generative AI
- Talking Avatar
- Video Translation
- Live Avatar
website: https://akool.com
---
