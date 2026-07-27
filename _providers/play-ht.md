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
- acting_count: 2
  human_in_the_loop: 0
  name: Play Ht Agentic Access
  operation_count: 6
  slug: play-ht-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 3
apis:
- description: REST API for PlayHT TTS, voice cloning, and PlayDialog conversational voice. v2.2 and v2.3 endpoints supported. WebSocket streaming for low-latency conversational use cases.
  name: PlayHT API
  slug: platform
- description: Text-to-speech generation jobs.
  name: PlayHT TTS API
  slug: play-ht-tts-api
- description: Prebuilt and cloned voice catalog.
  name: PlayHT Voices API
  slug: play-ht-voices-api
artifact_total: 10
collections:
- collection_type: open
  name: PlayHT API
  slug: open-play-ht
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/play-ht-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/play-ht-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/play-ht-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/playht
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/play-ht
- group: company
  title: ''
  type: Website
  url: https://play.ht/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.play.ht/
- group: commercial
  title: ''
  type: Plans
  url: plans/play-ht-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/play-ht-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/play-ht-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.play.ht/llms.txt
created: '2026-05-08'
description: PlayHT is an AI voice generation and TTS platform with hundreds of voices, voice cloning, and a realtime conversational voice API (Play 3.0 mini, PlayDialog). The PlayHT REST API exposes voice synthesis, voice cloning, streaming, and language translation. Documentation is at https://docs.play.ht/.
finops:
- name: Play Ht Finops
  service_category: AI
  slug: play-ht-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/play-ht.png
layout: provider
modified: '2026-05-08'
name: PlayHT
nav: Providers
network: true
overview: 'PlayHT publishes 2 APIs on the [APIs.io](https://apis.io/) network: TTS API and Voices API. Tagged areas include AI, Voice, TTS, Voice Cloning, and Audio.


  PlayHT''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Play Ht Plans Pricing
  plan_count: 4
  slug: play-ht-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 3
  name: Play Ht Rate Limits
  slug: play-ht-rate-limits
score:
  band: thin
  composite: 39.7
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.2
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/play-ht/refs/heads/main/screenshots/play-ht-2026-06-20T191803.png
security:
- kind: authentication
  name: Play Ht Authentication
  slug: play-ht-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Play Ht Domain Security
  slug: play-ht-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: play-ht
tags:
- AI
- Voice
- TTS
- Voice Cloning
- Audio
- Realtime
website: https://play.ht/
---
