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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Inworld Agentic Access
  operation_count: 19
  slug: inworld-agentic-access
  summary_line: 19 operations · 13 acting
api_count: 10
apis:
- description: TTS-2 and TTS-1.5 (Max/Mini) models for character voice synthesis. Priced per 1M characters with plan-tier discounts.
  name: Inworld Text-to-Speech API
  slug: tts
- description: Multi-provider transcription API priced at $0.35/hour standard rate.
  name: Inworld Speech-to-Text API
  slug: stt
- description: Low-latency speech-to-speech voice API for natural conversation experiences. Included with all plans.
  name: Inworld Realtime API
  slug: realtime
- description: Routing layer over 220+ LLM models, billed at provider cost via Inworld's unified API.
  name: Inworld LLM Router API
  slug: llm-router
- description: Available models
  name: Inworld AI Models API
  slug: inworld-models-api
- description: Realtime speech-to-speech
  name: Inworld AI Realtime API
  slug: inworld-realtime-api
- description: LLM Router configurations
  name: Inworld AI Router API
  slug: inworld-router-api
- description: Speech-to-Text transcription
  name: Inworld AI STT API
  slug: inworld-stt-api
- description: Text-to-Speech synthesis
  name: Inworld AI TTS API
  slug: inworld-tts-api
- description: Voice catalog and custom voice management
  name: Inworld AI Voices API
  slug: inworld-voices-api
artifact_total: 18
collections:
- collection_type: open
  name: Inworld AI API
  slug: open-inworld
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inworld-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/inworld-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inworld-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inworld-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inworld-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inworld-ai
- group: company
  title: ''
  type: Website
  url: https://inworld.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inworld.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/inworld-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inworld-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inworld-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.inworld.ai/llms.txt
created: '2026-05-08'
description: Inworld AI provides voice and conversational AI building blocks for games and interactive media. Public APIs cover Text-to-Speech, Speech-to-Text, a Realtime speech-to-speech API, and an LLM Router that fronts 220+ third-party models with unified billing.
finops:
- name: Inworld Finops
  service_category: AI
  slug: inworld-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inworld.png
layout: provider
modified: '2026-05-08'
name: Inworld AI
nav: Providers
network: true
overview: 'Inworld AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Models API, Realtime API, Router API, and 3 more. Tagged areas include AI, Voice, Characters, Games, and Conversational.


  Inworld AI''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Inworld Plans Pricing
  plan_count: 5
  slug: inworld-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Inworld Rate Limits
  slug: inworld-rate-limits
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 54.3
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inworld/refs/heads/main/screenshots/inworld-2026-06-20T183534.png
security:
- kind: authentication
  name: Inworld Authentication
  slug: inworld-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inworld Domain Security
  slug: inworld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Inworld Trust Center
  slug: inworld-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: inworld
tags:
- AI
- Voice
- Characters
- Games
- Conversational
website: https://inworld.ai/
---
