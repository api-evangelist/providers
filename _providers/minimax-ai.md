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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Minimax Ai Agentic Access
  operation_count: 18
  slug: minimax-ai-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 7
apis:
- description: The Files API from MiniMax — 5 operation(s) for files.
  name: MiniMax Files API
  slug: minimax-ai-files-api
- description: The Image API from MiniMax — 1 operation(s) for image.
  name: MiniMax Image API
  slug: minimax-ai-image-api
- description: The Music API from MiniMax — 1 operation(s) for music.
  name: MiniMax Music API
  slug: minimax-ai-music-api
- description: The Text Generation API from MiniMax — 1 operation(s) for text generation.
  name: MiniMax Text Generation API
  slug: minimax-ai-text-generation-api
- description: The Text to Audio API from MiniMax — 3 operation(s) for text to audio.
  name: MiniMax Text to Audio API
  slug: minimax-ai-text-to-audio-api
- description: The Video API from MiniMax — 3 operation(s) for video.
  name: MiniMax Video API
  slug: minimax-ai-video-api
- description: The Voice API from MiniMax — 4 operation(s) for voice.
  name: MiniMax Voice API
  slug: minimax-ai-voice-api
artifact_total: 14
collections:
- collection_type: open
  name: MiniMax API
  slug: open-minimax-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/minimax-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minimax-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/minimax-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MiniMax-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/minimax-ai
- group: company
  title: ''
  type: Website
  url: https://www.minimax.io/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.minimax.io/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/minimax-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/minimax-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/minimax-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.minimax.io/blog
created: '2026-05-08'
description: 'MiniMax is a Chinese foundation model company offering full-stack multimodal APIs: text generation (M2.7, M2.5, M2.1, M2, M1, Text-01), speech synthesis (Speech 2.8/2.6/2.5), voice cloning, voice design, image generation (Image-01), video generation (Hailuo 2.3), and music generation (Music-2.6).'
finops:
- name: Minimax Ai Finops
  service_category: AI and Machine Learning
  slug: minimax-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/minimax-ai.png
layout: provider
modified: '2026-05-19'
name: MiniMax
nav: Providers
network: true
overview: 'MiniMax publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Files API, Image API, Music API, and 4 more. Tagged areas include AI, LLM, Inference, Multimodal, and Voice.


  MiniMax''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Minimax Ai Plans Pricing
  plan_count: 4
  slug: minimax-ai-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 8
  name: Minimax Ai Rate Limits
  slug: minimax-ai-rate-limits
score:
  band: thin
  composite: 35.7
  delta: -5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/minimax-ai/refs/heads/main/screenshots/minimax-ai-2026-06-20T185605.png
security:
- kind: authentication
  name: Minimax Ai Authentication
  slug: minimax-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Minimax Ai Domain Security
  slug: minimax-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: minimax-ai
tags:
- AI
- LLM
- Inference
- Multimodal
- Voice
- Video
- Music
- Image
website: https://www.minimax.io/
---
