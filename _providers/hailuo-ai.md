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
- acting_count: 4
  human_in_the_loop: 0
  name: Hailuo Ai Agentic Access
  operation_count: 6
  slug: hailuo-ai-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 5
apis:
- description: OpenAI-compatible LLM chat completions.
  name: Hailuo AI / MiniMax Chat Completions API
  slug: hailuo-ai-chat-completions-api
- description: Retrieve generated assets by file_id.
  name: Hailuo AI / MiniMax Files API
  slug: hailuo-ai-files-api
- description: Vocal music generation from prompt and lyrics.
  name: Hailuo AI / MiniMax Music Generation API
  slug: hailuo-ai-music-generation-api
- description: Speech synthesis (T2A v2).
  name: Hailuo AI / MiniMax Text to Speech API
  slug: hailuo-ai-text-to-speech-api
- description: Asynchronous AI video generation with the Hailuo models.
  name: Hailuo AI / MiniMax Video Generation API
  slug: hailuo-ai-video-generation-api
artifact_total: 13
asyncapis:
- description: 'MiniMax publishes a documented real-time text-to-speech WebSocket API. A client opens a WebSocket connection to wss://api.minimax.io/ws/v1/t2a_v2 (US West: wss://api-uw.minimax.io/ws/v1/t2a_v2), authe'
  name: MiniMax Text-to-Speech (T2A) WebSocket API
  slug: hailuo-ai-asyncapi
collections:
- collection_type: open
  name: Hailuo AI / MiniMax API
  slug: open-hailuo-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hailuo-ai-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hailuo-ai-authentication.yml
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
  url: plans/hailuo-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hailuo-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hailuo-ai-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://platform.minimax.io/login
- group: company
  title: ''
  type: Blog
  url: https://www.minimax.io/news
created: '2026-07-11'
description: Hailuo AI is MiniMax's generative video and audio platform. MiniMax is a Singapore- and China-based foundation-model company whose developer platform (platform.minimax.io / api.minimax.io, and intl.minimaxi.com for international users) exposes documented HTTP APIs for AI video generation (the Hailuo text-to-video and image-to-video models - MiniMax-Hailuo-2.3, MiniMax-Hailuo-02, Video-01, T2V-01, I2V-01, S2V-01), large language model chat completions (the MiniMax / abab family), text-to-speech (T2A) over both HTTP and a real-time WebSocket, music generation, and voice cloning. Video generation follows an asynchronous create-task-then-poll pattern; all APIs authenticate with a Bearer API key.
finops:
- name: Hailuo Ai Finops
  service_category: AI and Machine Learning
  slug: hailuo-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hailuo-ai.png
layout: provider
modified: '2026-07-11'
name: Hailuo AI / MiniMax
nav: Providers
network: true
overview: 'Hailuo AI / MiniMax publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat Completions API, Files API, Music Generation API, and 2 more. Tagged areas include Video Generation, AI Video, Generative AI, Text-to-Video, and Image-to-Video.


  The Hailuo AI / MiniMax catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hailuo AI / MiniMax''s developer surface includes authentication, documentation, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Hailuo Ai Plans Pricing
  plan_count: 4
  slug: hailuo-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Hailuo Ai Rate Limits
  slug: hailuo-ai-rate-limits
rules:
- name: Hailuo AI / MiniMax API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: hailuo-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 49.0
  delta: -4.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 70.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 31.6
  previous_composite: 53.4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/hailuo-ai/refs/heads/main/screenshots/hailuo-ai-2026-07-25T220530.png
security:
- kind: authentication
  name: Hailuo Ai Authentication
  slug: hailuo-ai-authentication
  summary_line: http · 1 scheme
slug: hailuo-ai
tags:
- Video Generation
- AI Video
- Generative AI
- Text-to-Video
- Image-to-Video
- Text to Speech
- LLM
- Foundation Models
website: https://www.minimax.io/
---
