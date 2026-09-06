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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hailuo Ai Agentic Access
  operation_count: 6
  slug: hailuo-ai-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.minimax.io/v1
  baseurl_source: declared
  description: OpenAI-compatible LLM chat completions.
  name: Hailuo AI / MiniMax Chat Completions API
  slug: hailuo-ai-chat-completions-api
- baseURL: https://api.minimax.io/v1
  baseurl_source: declared
  description: Retrieve generated assets by file_id.
  name: Hailuo AI / MiniMax Files API
  slug: hailuo-ai-files-api
- baseURL: https://api.minimax.io/v1
  baseurl_source: declared
  description: Vocal music generation from prompt and lyrics.
  name: Hailuo AI / MiniMax Music Generation API
  slug: hailuo-ai-music-generation-api
- baseURL: https://api.minimax.io/v1
  baseurl_source: declared
  description: Speech synthesis (T2A v2).
  name: Hailuo AI / MiniMax Text to Speech API
  slug: hailuo-ai-text-to-speech-api
- baseURL: https://api.minimax.io/v1
  baseurl_source: declared
  description: Asynchronous AI video generation with the Hailuo models.
  name: Hailuo AI / MiniMax Video Generation API
  slug: hailuo-ai-video-generation-api
artifact_total: 19
asyncapis:
- description: 'MiniMax publishes a documented real-time text-to-speech WebSocket API. A client opens a WebSocket connection to wss://api.minimax.io/ws/v1/t2a_v2 (US West: wss://api-uw.minimax.io/ws/v1/t2a_v2), authe'
  name: MiniMax Text-to-Speech (T2A) WebSocket API
  slug: hailuo-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hailuo AI / MiniMax Chat Completions API
  slug: open-hailuo-ai-chat-completions-api
- collection_type: open
  name: Hailuo AI / MiniMax Chat Completions Files API
  slug: open-hailuo-ai-files-api
- collection_type: open
  name: Hailuo AI / MiniMax Chat Completions Music Generation API
  slug: open-hailuo-ai-music-generation-api
- collection_type: open
  name: Hailuo AI / MiniMax Chat Completions Text to Speech API
  slug: open-hailuo-ai-text-to-speech-api
- collection_type: open
  name: Hailuo AI / MiniMax Chat Completions Video Generation API
  slug: open-hailuo-ai-video-generation-api
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
random_paper: 7
rate_limits:
- limit_count: 5
  name: Hailuo Ai Rate Limits
  slug: hailuo-ai-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Hailuo AI / MiniMax API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: hailuo-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 67.8
    catalog_earned_first_party: 0.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 11.4
    contract_quality: 63.1
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 31.6
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Text-to-Speech
- LLM
- Foundation Models
website: https://www.minimax.io/
---
