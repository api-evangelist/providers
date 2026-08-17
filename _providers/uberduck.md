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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Uberduck Agentic Access
  operation_count: 5
  slug: uberduck-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 4
apis:
- description: Mint LiveKit tokens for real-time conversational AI voice calls.
  name: Uberduck Conversational API
  slug: uberduck-conversational-api
- description: List available text-to-speech models by provider.
  name: Uberduck Models API
  slug: uberduck-models-api
- description: Synthesize speech from text using a chosen voice and model.
  name: Uberduck Text-to-Speech API
  slug: uberduck-text-to-speech-api
- description: List, filter, and clone voices.
  name: Uberduck Voices API
  slug: uberduck-voices-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Uberduck Text To Speech Conversational API
  slug: open-uberduck-conversational-api
- collection_type: open
  name: Uberduck Text To Speech Conversational Models API
  slug: open-uberduck-models-api
- collection_type: open
  name: Uberduck Text To Speech Conversational Text-to-Speech API
  slug: open-uberduck-text-to-speech-api
- collection_type: open
  name: Uberduck Text To Speech Conversational Voices API
  slug: open-uberduck-voices-api
- collection_type: open
  name: Uberduck Text To Speech API
  slug: open-uberduck
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uberduck-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uberduck-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uberduck-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uberduck-ai
- group: company
  title: ''
  type: Website
  url: https://uberduck.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uberduck.ai
- group: docs
  title: ''
  type: APIReference
  url: https://api.uberduck.ai/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/uberduck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uberduck-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uberduck-finops.yml
created: '2026-07-11'
description: Uberduck is an AI voice platform whose public REST API converts text into natural-sounding speech across a catalog of voices and provider-backed models (AWS Polly, Google Cloud, Azure), lists and filters those voices, creates instant zero-shot voice clones from reference audio, and mints LiveKit tokens for real-time conversational AI voice calls. The API is HTTPS request/response with Bearer API-key authentication. It is self-serve but gated behind a paid plan - API access is a feature of the Creator plan and above. Uberduck's earlier AI music / rap-vocals API surface is no longer part of the published API; the current documented product (OpenAPI version 0.1.0) is focused on text-to-speech, voices, and conversational voice.
finops:
- name: Uberduck Finops
  service_category: AI and Machine Learning
  slug: uberduck-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uberduck.png
layout: provider
modified: '2026-07-11'
name: Uberduck
nav: Providers
network: true
overview: 'Uberduck publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Conversational API, Models API, Text-to-Speech API, and 1 more. Tagged areas include AI, Text to Speech, TTS, Voice, and Voice Cloning.


  Uberduck''s developer surface includes authentication, documentation, API reference, and 7 more developer resources.'
plans:
- name: Uberduck Plans Pricing
  plan_count: 4
  slug: uberduck-plans-pricing
random_paper: 108
rate_limits:
- limit_count: 6
  name: Uberduck Rate Limits
  slug: uberduck-rate-limits
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Uberduck Authentication
  slug: uberduck-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uberduck Domain Security
  slug: uberduck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uberduck
tags:
- AI
- Text to Speech
- TTS
- Voice
- Voice Cloning
- Speech Synthesis
- Conversational AI
website: https://uberduck.ai
---
