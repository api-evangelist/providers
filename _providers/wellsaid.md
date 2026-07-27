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
- acting_count: 8
  human_in_the_loop: 0
  name: Wellsaid Agentic Access
  operation_count: 16
  slug: wellsaid-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 4
apis:
- description: Manage rendered clips.
  name: WellSaid Labs Clips API
  slug: wellsaid-clips-api
- description: Respelling suggestions and replacement libraries.
  name: WellSaid Labs Pronunciation API
  slug: wellsaid-pronunciation-api
- description: Render text to speech as clips or audio streams.
  name: WellSaid Labs Text-to-Speech API
  slug: wellsaid-text-to-speech-api
- description: Discover available voice avatars.
  name: WellSaid Labs Voices API
  slug: wellsaid-voices-api
artifact_total: 12
collections:
- collection_type: open
  name: WellSaid Labs API
  slug: open-wellsaid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wellsaid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wellsaid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellsaid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellsaid-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wellsaid-labs
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
  url: https://docs.wellsaidlabs.com
- group: commercial
  title: ''
  type: Plans
  url: plans/wellsaid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellsaid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wellsaid-finops.yml
created: '2026-06-21'
description: WellSaid Labs is an AI text-to-speech voice platform. Its REST API renders natural-sounding speech from text using studio-quality voice avatars, supporting synchronous clip creation, low-latency audio streaming, and word-level timing with subtitles, authenticated with an X-Api-Key header.
finops:
- name: Wellsaid Finops
  service_category: AI and Machine Learning
  slug: wellsaid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wellsaid.png
layout: provider
modified: '2026-06-21'
name: WellSaid Labs
nav: Providers
network: true
overview: 'WellSaid Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Clips API, Pronunciation API, Text-to-Speech API, and 1 more. Tagged areas include AI, Text to Speech, Voice, Audio, and TTS.


  WellSaid Labs'' developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Wellsaid Plans Pricing
  plan_count: 3
  slug: wellsaid-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 3
  name: Wellsaid Rate Limits
  slug: wellsaid-rate-limits
score:
  band: thin
  composite: 42.6
  delta: 3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 57.5
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Wellsaid Authentication
  slug: wellsaid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wellsaid Domain Security
  slug: wellsaid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wellsaid Trust Center
  slug: wellsaid-trust-center
  summary_line: SOC 2, GDPR
slug: wellsaid
tags:
- AI
- Text to Speech
- Voice
- Audio
- TTS
website: https://wellsaidlabs.com
---
