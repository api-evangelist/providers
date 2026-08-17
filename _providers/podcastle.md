---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Podcastle Agentic Access
  operation_count: 5
  slug: podcastle-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 3
apis:
- description: Transcription and speech-to-text are Podcastle platform features (multi-language transcription with speaker identification) available in the product, console, and credit-based plans. A standalone tran
  name: Podcastle Transcription
  slug: transcription
- description: Synthesize speech from text in batch, streaming, or with word timestamps.
  name: Podcastle Text to Speech API
  slug: podcastle-text-to-speech-api
- description: Browse the voice library and create instant voice clones.
  name: Podcastle Voices API
  slug: podcastle-voices-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Async (Podcastle) Voice Text to Speech API
  slug: open-podcastle-text-to-speech-api
- collection_type: open
  name: Async (Podcastle) Voice Text to Speech Voices API
  slug: open-podcastle-voices-api
- collection_type: open
  name: Async (Podcastle) Voice API
  slug: open-podcastle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/podcastle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podcastle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podcastle-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://podcastle.ai/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podcastle-ai
- group: company
  title: ''
  type: Website
  url: https://podcastle.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.async.com
- group: commercial
  title: ''
  type: Plans
  url: plans/podcastle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/podcastle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/podcastle-finops.yml
created: '2026-06-21'
description: Podcastle is an AI audio and podcast creation platform whose developer engine, Async, exposes a low-latency Voice API for human-like text-to-speech, a browsable voice library, and instant voice cloning from a short audio sample. The API is served from https://api.async.com and authenticated with an x-api-key header plus a version header. Transcription is a Podcastle platform feature; no standalone transcription endpoint is documented in the public Voice API.
finops:
- name: Podcastle Finops
  service_category: AI and Machine Learning
  slug: podcastle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podcastle.png
layout: provider
modified: '2026-06-21'
name: Podcastle
nav: Providers
network: true
overview: 'Podcastle publishes 2 APIs on the [APIs.io](https://apis.io/) network: Text to Speech API and Voices API. Tagged areas include AI, Audio, Text to Speech, Voice Cloning, and Podcasting.


  Podcastle''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Podcastle Plans Pricing
  plan_count: 6
  slug: podcastle-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 3
  name: Podcastle Rate Limits
  slug: podcastle-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Podcastle Authentication
  slug: podcastle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Podcastle Domain Security
  slug: podcastle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: podcastle
tags:
- AI
- Audio
- Text to Speech
- Voice Cloning
- Podcasting
website: https://podcastle.ai
---
