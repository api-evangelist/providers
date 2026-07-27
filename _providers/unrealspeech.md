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
- acting_count: 3
  human_in_the_loop: 0
  name: Unrealspeech Agentic Access
  operation_count: 4
  slug: unrealspeech-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 3
apis:
- description: Synchronous text-to-speech returning an MP3 and timestamp URLs.
  name: Unreal Speech Speech API
  slug: unrealspeech-speech-api
- description: Low-latency HTTP streaming synthesis returning audio bytes.
  name: Unreal Speech Stream API
  slug: unrealspeech-stream-api
- description: Asynchronous synthesis for long-form audio via submit-and-poll.
  name: Unreal Speech Synthesis Tasks API
  slug: unrealspeech-synthesis-tasks-api
artifact_total: 10
collections:
- collection_type: open
  name: Unreal Speech API
  slug: open-unrealspeech
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unrealspeech-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unrealspeech-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unrealspeech-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unrealspeech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unrealspeech
- group: company
  title: ''
  type: Website
  url: https://unrealspeech.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unrealspeech.com
- group: commercial
  title: ''
  type: Plans
  url: plans/unrealspeech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unrealspeech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unrealspeech-finops.yml
created: '2026-07-11'
description: Unreal Speech is a low-cost, high-scale text-to-speech (TTS) API for turning text into natural-sounding speech. It exposes a small REST surface - a low-latency HTTP streaming endpoint, a synchronous speech endpoint that returns an MP3 plus per-word or per-sentence timestamps, and an asynchronous synthesis tasks endpoint for long-form audio up to 500,000 characters. Requests are authenticated with a Bearer API key issued from the dashboard, and pricing is metered per character with a free monthly allowance.
finops:
- name: Unrealspeech Finops
  service_category: AI and Machine Learning
  slug: unrealspeech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unrealspeech.png
layout: provider
modified: '2026-07-11'
name: Unreal Speech
nav: Providers
network: true
overview: 'Unreal Speech publishes 3 APIs on the [APIs.io](https://apis.io/) network: Speech API, Stream API, and Synthesis Tasks API. Tagged areas include Text to Speech, TTS, Speech Synthesis, Audio, and Voice.


  Unreal Speech''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Unrealspeech Plans Pricing
  plan_count: 6
  slug: unrealspeech-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 7
  name: Unrealspeech Rate Limits
  slug: unrealspeech-rate-limits
score:
  band: thin
  composite: 42.1
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Unrealspeech Authentication
  slug: unrealspeech-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unrealspeech Domain Security
  slug: unrealspeech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unrealspeech
tags:
- Text to Speech
- TTS
- Speech Synthesis
- Audio
- Voice
- AI
website: https://unrealspeech.com
---
