---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Minimax Ai Agentic Access
  operation_count: 18
  slug: minimax-ai-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.minimax.io
  baseurl_source: declared
  description: The Files API from MiniMax — 5 operation(s) for files.
  name: MiniMax Files API
  slug: minimax-ai-files-api
- baseURL: https://api.minimax.io
  baseurl_source: declared
  description: The Image API from MiniMax — 1 operation(s) for image.
  name: MiniMax Image API
  slug: minimax-ai-image-api
- baseURL: https://api.minimax.io
  baseurl_source: declared
  description: The Music API from MiniMax — 1 operation(s) for music.
  name: MiniMax Music API
  slug: minimax-ai-music-api
- baseURL: https://api.minimax.io
  baseurl_source: declared
  description: The Text Generation API from MiniMax — 1 operation(s) for text generation.
  name: MiniMax Text Generation API
  slug: minimax-ai-text-generation-api
- baseURL: https://api.minimax.io
  baseurl_source: declared
  description: The Text to Audio API from MiniMax — 3 operation(s) for text to audio.
  name: MiniMax Text to Audio API
  slug: minimax-ai-text-to-audio-api
- baseURL: https://api.minimax.io
  baseurl_source: declared
  description: The Video API from MiniMax — 3 operation(s) for video.
  name: MiniMax Video API
  slug: minimax-ai-video-api
- baseURL: https://api.minimax.io
  baseurl_source: declared
  description: The Voice API from MiniMax — 4 operation(s) for voice.
  name: MiniMax Voice API
  slug: minimax-ai-voice-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MiniMax Files API
  slug: open-minimax-ai-files-api
- collection_type: open
  name: MiniMax Files Image API
  slug: open-minimax-ai-image-api
- collection_type: open
  name: MiniMax Files Music API
  slug: open-minimax-ai-music-api
- collection_type: open
  name: MiniMax Files Text Generation API
  slug: open-minimax-ai-text-generation-api
- collection_type: open
  name: MiniMax Files Text to Audio API
  slug: open-minimax-ai-text-to-audio-api
- collection_type: open
  name: MiniMax Files Video API
  slug: open-minimax-ai-video-api
- collection_type: open
  name: MiniMax Files Voice API
  slug: open-minimax-ai-voice-api
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
overview: 'MiniMax publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Files API, Image API, Music API, and 4 more. Tagged areas include Artificial Intelligence, LLM, Inference, Multi-Modal, and Voice.


  MiniMax''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Minimax Ai Plans Pricing
  plan_count: 4
  slug: minimax-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 8
  name: Minimax Ai Rate Limits
  slug: minimax-ai-rate-limits
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
- Artificial Intelligence
- LLM
- Inference
- Multi-Modal
- Voice
- Video
- Music
- Image
website: https://www.minimax.io/
---
