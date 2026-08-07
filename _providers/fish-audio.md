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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fish Audio Agentic Access
  operation_count: 10
  slug: fish-audio-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 5
apis:
- description: The Fish Audio API provides RESTful access to text-to-speech, speech-to-text, voice cloning, and voice management capabilities backed by the Fish Audio S2-Pro model. Endpoints support streaming low-la
  name: Fish Audio API
  slug: fish-audio-api
- description: The Asr API from Fish Audio — 1 operation(s) for asr.
  name: Fish Audio Asr API
  slug: fish-audio-asr-api
- description: The Model API from Fish Audio — 2 operation(s) for model.
  name: Fish Audio Model API
  slug: fish-audio-model-api
- description: The Tts API from Fish Audio — 2 operation(s) for tts.
  name: Fish Audio Tts API
  slug: fish-audio-tts-api
- description: The Wallet API from Fish Audio — 2 operation(s) for wallet.
  name: Fish Audio Wallet API
  slug: fish-audio-wallet-api
artifact_total: 12
collections:
- collection_type: open
  name: Fish Audio API
  slug: open-fish-audio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fish-audio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fish-audio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fish-audio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fish.audio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fish.audio
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fish.audio/go-api
- group: other
  title: ''
  type: Playground
  url: https://fish.audio/discovery
- group: commercial
  title: ''
  type: Pricing
  url: https://fish.audio/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fishaudio
- group: other
  title: ''
  type: OpenSourceModel
  url: https://github.com/fishaudio/fish-speech
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/Es5qTB9BcN
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/FishAudio
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.fish.audio/llms.txt
created: '2026-05-23'
description: Fish Audio is an AI voice platform offering text-to-speech, voice cloning, speech-to-text, voice changing, and audio storytelling capabilities. The platform hosts a library of over two million voices across 30+ languages and is built around the Fish Speech open-source TTS model and the proprietary Fish Audio S2-Pro model. Fish Audio exposes a public REST API at api.fish.audio with first-party Python, Go, and TypeScript SDKs and supports voice cloning from as little as fifteen seconds of reference audio. The developer surface emphasizes ultra-low latency streaming, emotion control, and pay-as-you-go pricing for both prototype and production workloads.
finops:
- name: Fish Audio Finops
  service_category: API
  slug: fish-audio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fish-audio.png
layout: provider
modified: '2026-05-23'
name: Fish Audio
nav: Providers
network: true
overview: 'Fish Audio publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Asr API, Model API, Tts API, and 1 more. Tagged areas include Voice, Text to Speech, Speech to Text, Voice Cloning, and Audio.


  Fish Audio''s developer surface includes authentication, documentation, pricing, and 10 more developer resources.'
plans:
- name: Fish Audio Plans Pricing
  plan_count: 1
  slug: fish-audio-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 2
  name: Fish Audio Rate Limits
  slug: fish-audio-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.4
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fish-audio/refs/heads/main/screenshots/fish-audio-2026-06-20T181249.png
security:
- kind: authentication
  name: Fish Audio Authentication
  slug: fish-audio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fish Audio Domain Security
  slug: fish-audio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fish-audio
tags:
- Voice
- Text to Speech
- Speech to Text
- Voice Cloning
- Audio
- Generative AI
- Multilingual
- Streaming
- SDK
- Open Source
website: https://fish.audio
---
