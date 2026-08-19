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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Wellsaid Labs Agentic Access
  operation_count: 16
  slug: wellsaid-labs-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 4
apis:
- description: Asynchronous clip creation, retrieval, and combination.
  name: WellSaid Labs Clips API
  slug: wellsaid-labs-clips-api
- description: Replacement libraries and respelling suggestions for pronunciation control.
  name: WellSaid Labs Pronunciation API
  slug: wellsaid-labs-pronunciation-api
- description: Render text to speech, with streaming audio and word timing.
  name: WellSaid Labs Text-to-Speech API
  slug: wellsaid-labs-text-to-speech-api
- description: Catalog of available AI voice avatars and their metadata.
  name: WellSaid Labs Voice Avatars API
  slug: wellsaid-labs-voice-avatars-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WellSaid Labs Clips API
  slug: open-wellsaid-labs-clips-api
- collection_type: open
  name: WellSaid Labs Clips Pronunciation API
  slug: open-wellsaid-labs-pronunciation-api
- collection_type: open
  name: WellSaid Labs Clips Text-to-Speech API
  slug: open-wellsaid-labs-text-to-speech-api
- collection_type: open
  name: WellSaid Labs Clips Voice Avatars API
  slug: open-wellsaid-labs-voice-avatars-api
- collection_type: open
  name: WellSaid Labs API
  slug: open-wellsaid-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wellsaid-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wellsaid-labs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellsaid-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellsaid-labs-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wellsaid-labs
- group: company
  title: ''
  type: Website
  url: https://wellsaidlabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wellsaidlabs.com/docs/getting-started
- group: commercial
  title: ''
  type: Plans
  url: plans/wellsaid-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellsaid-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wellsaid-labs-finops.yml
created: '2026-07-11'
description: WellSaid Labs is an AI text-to-speech (TTS) platform that turns text into studio-quality synthetic voiceover using a library of 200+ AI voice avatars across many styles, languages, and accents. Beyond the AI Voice Studio web app, WellSaid exposes a documented REST API (base https://api.wellsaidlabs.com/v1) that renders text to speech, streams audio for low time-to-first-byte playback, returns word-level timing and subtitles, manages asynchronous clips, lists voice avatars, and lets teams control pronunciation with replacement libraries and respelling suggestions. The API authenticates with an X-Api-Key header and is gated behind a trial API key and a business plan.
finops:
- name: Wellsaid Labs Finops
  service_category: AI and Machine Learning
  slug: wellsaid-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wellsaid-labs.png
layout: provider
modified: '2026-07-11'
name: WellSaid Labs
nav: Providers
network: true
overview: 'WellSaid Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Clips API, Pronunciation API, Text-to-Speech API, and 1 more. Tagged areas include AI, Text to Speech, TTS, Voice, and Voiceover.


  WellSaid Labs'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Wellsaid Labs Plans Pricing
  plan_count: 5
  slug: wellsaid-labs-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 3
  name: Wellsaid Labs Rate Limits
  slug: wellsaid-labs-rate-limits
score:
  band: developing
  composite: 39.6
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 57.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Wellsaid Labs Authentication
  slug: wellsaid-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wellsaid Labs Domain Security
  slug: wellsaid-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wellsaid Labs Trust Center
  slug: wellsaid-labs-trust-center
  summary_line: SOC 2, GDPR
slug: wellsaid-labs
tags:
- AI
- Text to Speech
- TTS
- Voice
- Voiceover
- Speech Synthesis
- Audio
website: https://wellsaidlabs.com
---
