---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Replica API v2 (OpenAPI 3.0.0) — REST API for AI text-to-speech, speech-to-speech, and voice-library operations. Historical; the service was sunset on 2025-06-30.
  name: Replica API
  slug: replica-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://replicastudios.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.replicastudios.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.replicastudios.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.replicastudios.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.replicastudios.com/
- group: operate
  title: ''
  type: Support
  url: https://help.replicastudios.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/replica-studios-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/replica-studios-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replica-studios-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replica-studios-llms.txt
created: '2026-07-17'
description: Replica Studios (operated by Replica Media Pty Ltd) built AI voice, text-to-speech (TTS) and speech-to-speech (STS) technology for creators, game developers, and software teams. Its platform offered an AI Voice Library of 40+ expressive voices, Voice Lab for blending up to five voices into a custom character, and Voice Director for generating voice overs and dialogue. Developers integrated these capabilities through the Replica API v2 (OpenAPI 3.0.0) — a REST API supporting text-to-speech, speech-to-speech, and voice-listing operations, authenticated with API keys or Bearer JWTs minted at the /v2/auth endpoint. Replica Studios was a Techstars portfolio company. The company ceased operations on 2025-06-30; the marketing site now shows a farewell page and the api.replicastudios.com host no longer resolves, so this profile is a historical/discovery record captured from public documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replica-studios.png
layout: provider
modified: '2026-07-20'
name: Replica Studios
nav: Providers
network: true
overview: 'Replica Studios publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Voice, Text to Speech, Speech to Speech, and AI.


  Replica Studios'' developer surface includes documentation, API reference, getting-started guide, support, authentication, and 5 more developer resources.'
random_paper: 40
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Replica Studios Authentication
  slug: replica-studios-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Replica Studios Domain Security
  slug: replica-studios-domain-security
  summary_line: TLSv1.3
slug: replica-studios
tags:
- Company
- Voice
- Text to Speech
- Speech to Speech
- AI
- Audio
- Voice AI
- Generative AI
website: https://replicastudios.com/
---
