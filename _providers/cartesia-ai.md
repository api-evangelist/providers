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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Cartesia Ai Agentic Access
  operation_count: 86
  slug: cartesia-ai-agentic-access
  summary_line: 86 operations · 48 acting
api_count: 21
apis:
- description: 'Bidirectional, multiplexed WebSocket at wss://api.cartesia.ai/tts/websocket for realtime speech generation. Clients send JSON generation requests keyed by a context_id (continuing a context preserves '
  name: Cartesia TTS WebSocket API
  slug: cartesia-ai-tts-websocket-api
- description: Realtime transcription over WebSocket at wss://api.cartesia.ai/stt/websocket. Clients stream raw binary audio in 100ms chunks and issue finalize/close text commands; the server returns incremental and
  name: Cartesia STT WebSocket API
  slug: cartesia-ai-stt-websocket-api
- description: Voice agent configuration and public templates.
  name: Cartesia Agents API
  slug: cartesia-ai-agents-api
- description: Standard API key metadata.
  name: Cartesia API Keys API
  slug: cartesia-ai-api-keys-api
- description: Short-lived, scoped access token generation.
  name: Cartesia Auth API
  slug: cartesia-ai-auth-api
- description: Outbound call placement, batching, and history.
  name: Cartesia Calls API
  slug: cartesia-ai-calls-api
- description: Audio/text collections used to build custom fine-tunes and voices.
  name: Cartesia Datasets API
  slug: cartesia-ai-datasets-api
- description: Agent deployment inspection.
  name: Cartesia Deployments API
  slug: cartesia-ai-deployments-api
- description: Generate audio that smoothly connects two existing audio segments.
  name: Cartesia Infill API
  slug: cartesia-ai-infill-api
- description: Documents and folders used by agents.
  name: Cartesia Knowledge Base API
  slug: cartesia-ai-knowledge-base-api
- description: LLM-as-a-judge quality metrics for agents.
  name: Cartesia Metrics API
  slug: cartesia-ai-metrics-api
- description: Telephony number provisioning and import.
  name: Cartesia Phone Numbers API
  slug: cartesia-ai-phone-numbers-api
- description: Custom pronunciation overrides referenced by TTS requests.
  name: Cartesia Pronunciation Dictionaries API
  slug: cartesia-ai-pronunciation-dictionaries-api
- description: Linked telephony provider accounts.
  name: Cartesia Providers API
  slug: cartesia-ai-providers-api
- description: Batch transcription of an audio file of any length.
  name: Cartesia Speech-to-Text API
  slug: cartesia-ai-speech-to-text-api
- description: API health and version.
  name: Cartesia Status API
  slug: cartesia-ai-status-api
- description: Single-shot and streamed speech generation over plain HTTP.
  name: Cartesia Text-to-Speech API
  slug: cartesia-ai-text-to-speech-api
- description: Credit and agent usage reporting.
  name: Cartesia Usage API
  slug: cartesia-ai-usage-api
- description: Transform speech into a different target voice.
  name: Cartesia Voice Changer API
  slug: cartesia-ai-voice-changer-api
- description: Voice catalog management and voice cloning.
  name: Cartesia Voices API
  slug: cartesia-ai-voices-api
- description: Webhook endpoint registration.
  name: Cartesia Webhooks API
  slug: cartesia-ai-webhooks-api
artifact_total: 30
asyncapis:
- description: 'AsyncAPI 2.6 description of Cartesia''s **documented public WebSocket API**. Unlike most providers in this catalog, Cartesia publishes a real, bidirectional WebSocket protocol - not Server-Sent Events '
  name: Cartesia Realtime WebSocket API (TTS + STT)
  slug: cartesia-ai-asyncapi
collections:
- collection_type: open
  name: Cartesia API
  slug: open-cartesia-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cartesia-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cartesia-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cartesia-ai-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://cartesia.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cartesia-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cartesia-ai
- group: company
  title: ''
  type: Website
  url: https://cartesia.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cartesia.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/cartesia-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cartesia-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cartesia-ai-finops.yml
created: '2026-07-02'
description: Cartesia builds real-time voice AI - the Sonic family of text-to-speech models, Ink speech-to-text models, and a Voice Agents platform for building and deploying telephone and web voice agents. The core generation surface is exposed both as REST (bytes and Server-Sent Events) and as a low-latency, bidirectional WebSocket protocol at wss://api.cartesia.ai for streaming TTS and STT with multiplexed contexts, word/phoneme timestamps, and mid-stream flush and cancel.
finops:
- name: Cartesia Ai Finops
  service_category: AI and Machine Learning
  slug: cartesia-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cartesia-ai.png
layout: provider
modified: '2026-07-02'
name: Cartesia
nav: Providers
network: true
overview: 'Cartesia publishes 21 APIs on the [APIs.io](https://apis.io/) network, including TTS WebSocket API, STT WebSocket API, Agents API, and 18 more. Tagged areas include AI, Voice AI, Text to Speech, Speech to Text, and Realtime.


  The Cartesia catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cartesia''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Cartesia Ai Plans Pricing
  plan_count: 6
  slug: cartesia-ai-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 15
  name: Cartesia Ai Rate Limits
  slug: cartesia-ai-rate-limits
rules:
- name: Cartesia API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: cartesia-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.6
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.8
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cartesia-ai/refs/heads/main/screenshots/cartesia-ai-2026-07-25T204650.png
security:
- kind: authentication
  name: Cartesia Ai Authentication
  slug: cartesia-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cartesia Ai Domain Security
  slug: cartesia-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cartesia-ai
tags:
- AI
- Voice AI
- Text to Speech
- Speech to Text
- Realtime
- WebSocket
- Voice Cloning
- Voice Agents
website: https://cartesia.ai/
---
