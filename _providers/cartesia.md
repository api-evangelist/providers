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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Cartesia Agentic Access
  operation_count: 10
  slug: cartesia-agentic-access
  summary_line: 10 operations · 8 acting
api_count: 6
apis:
- description: The Sonic text-to-speech API converts text into ultra-low-latency, emotive speech with sub-100ms time-to-first-byte. It supports REST, server-sent events, and WebSocket streaming for real-time voice a
  name: Cartesia Sonic Text-to-Speech API
  slug: tts-api
- description: The Ink streaming speech-to-text API transcribes audio in real time with native turn detection tuned for voice agents and conversational systems.
  name: Cartesia Ink Speech-to-Text API
  slug: stt-api
- description: The Auth API from Cartesia — 1 operation(s) for auth.
  name: Cartesia Auth API
  slug: cartesia-auth-api
- description: The STT API from Cartesia — 1 operation(s) for stt.
  name: Cartesia STT API
  slug: cartesia-stt-api
- description: The TTS API from Cartesia — 2 operation(s) for tts.
  name: Cartesia TTS API
  slug: cartesia-tts-api
- description: The Voices API from Cartesia — 4 operation(s) for voices.
  name: Cartesia Voices API
  slug: cartesia-voices-api
artifact_total: 16
asyncapis:
- description: 'AsyncAPI description of Cartesia''s real-time WebSocket interfaces, derived strictly from the official Cartesia documentation at https://docs.cartesia.ai. Three WebSocket surfaces are covered: - Sonic '
  name: Cartesia Streaming WebSocket APIs
  slug: cartesia-asyncapi
collections:
- collection_type: open
  name: Cartesia API
  slug: open-cartesia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cartesia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cartesia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cartesia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cartesia.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cartesia.ai
- group: company
  title: ''
  type: Blog
  url: https://cartesia.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cartesia-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://cartesia.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cartesia.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cartesia.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/cartesia
- group: other
  title: ''
  type: X
  url: https://x.com/cartesia_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cartesia-ai
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cartesia.ai/llms.txt
created: '2026-05-23'
description: Cartesia is a real-time multimodal AI platform built around the Sonic family of ultra-low-latency text-to-speech models and the Ink streaming speech-to-text models. Sonic models deliver the first audio byte in as little as 90ms, support more than 40 languages, and can express laughter and emotion, making them well-suited to conversational AI, voice agents, dubbing, and avatar applications. Ink models add streaming transcription with native turn detection optimized for voice agents. Cartesia ships Python, JavaScript, and Go SDKs and exposes REST, server-sent events, and WebSocket interfaces for streaming audio. The platform is SOC 2 Type II, HIPAA, and PCI Level 1 aligned.
finops:
- name: Cartesia Finops
  service_category: API
  slug: cartesia-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Cartesia real-time text-to-speech and voice cloning API. Cartesia's native interfaces are REST, server-sent events, and WebSocket; this sche
  name: Cartesia GraphQL Schema
  slug: cartesia-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cartesia.png
layout: provider
modified: '2026-05-29'
name: Cartesia
nav: Providers
network: true
overview: 'Cartesia publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Sonic Text-to-Speech API, Ink Speech-to-Text API, Auth API, and 3 more. Tagged areas include Voice, TTS, Text to Speech, STT, and Speech to Text.


  The Cartesia catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cartesia''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Cartesia Plans Pricing
  plan_count: 1
  slug: cartesia-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 2
  name: Cartesia Rate Limits
  slug: cartesia-rate-limits
rules:
- name: Cartesia API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: cartesia-asyncapi-spectral-rules
score:
  band: developing
  composite: 52.5
  delta: 3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.5
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 52.6
    operational_transparency: 26.3
  previous_composite: 49.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cartesia/refs/heads/main/screenshots/cartesia-2026-06-20T174023.png
security:
- kind: authentication
  name: Cartesia Authentication
  slug: cartesia-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cartesia Domain Security
  slug: cartesia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cartesia
tags:
- Voice
- TTS
- Text to Speech
- STT
- Speech to Text
- Streaming
- WebSocket
- Voice Agents
- Voice Clone
- Sonic
- Ink
- Real-Time
website: https://cartesia.ai
---
