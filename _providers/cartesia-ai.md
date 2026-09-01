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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Cartesia Ai Agentic Access
  operation_count: 86
  slug: cartesia-ai-agentic-access
  summary_line: 86 operations · 48 acting
api_count: 1
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
- description: The STT API from Cartesia — 1 operation(s) for stt.
  name: Cartesia STT API
  slug: cartesia-ai-stt-api
- description: The TTS API from Cartesia — 2 operation(s) for tts.
  name: Cartesia TTS API
  slug: cartesia-ai-tts-api
artifact_total: 56
asyncapis:
- description: 'AsyncAPI 2.6 description of Cartesia''s **documented public WebSocket API**. Unlike most providers in this catalog, Cartesia publishes a real, bidirectional WebSocket protocol - not Server-Sent Events '
  name: Cartesia Realtime WebSocket API (TTS + STT)
  slug: cartesia-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cartesia Agents API
  slug: open-cartesia-ai-agents-api
- collection_type: open
  name: Cartesia Agents API Keys API
  slug: open-cartesia-ai-api-keys-api
- collection_type: open
  name: Cartesia Agents Auth API
  slug: open-cartesia-ai-auth-api
- collection_type: open
  name: Cartesia Agents Calls API
  slug: open-cartesia-ai-calls-api
- collection_type: open
  name: Cartesia Agents Datasets API
  slug: open-cartesia-ai-datasets-api
- collection_type: open
  name: Cartesia Agents Deployments API
  slug: open-cartesia-ai-deployments-api
- collection_type: open
  name: Cartesia Agents Infill API
  slug: open-cartesia-ai-infill-api
- collection_type: open
  name: Cartesia Agents Knowledge Base API
  slug: open-cartesia-ai-knowledge-base-api
- collection_type: open
  name: Cartesia Agents Metrics API
  slug: open-cartesia-ai-metrics-api
- collection_type: open
  name: Cartesia Agents Phone Numbers API
  slug: open-cartesia-ai-phone-numbers-api
- collection_type: open
  name: Cartesia Agents Pronunciation Dictionaries API
  slug: open-cartesia-ai-pronunciation-dictionaries-api
- collection_type: open
  name: Cartesia Agents Providers API
  slug: open-cartesia-ai-providers-api
- collection_type: open
  name: Cartesia Agents Speech-to-Text API
  slug: open-cartesia-ai-speech-to-text-api
- collection_type: open
  name: Cartesia Agents Status API
  slug: open-cartesia-ai-status-api
- collection_type: open
  name: Cartesia Auth STT API
  slug: open-cartesia-ai-stt-api
- collection_type: open
  name: Cartesia Agents Text-to-Speech API
  slug: open-cartesia-ai-text-to-speech-api
- collection_type: open
  name: Cartesia Auth TTS API
  slug: open-cartesia-ai-tts-api
- collection_type: open
  name: Cartesia Agents Usage API
  slug: open-cartesia-ai-usage-api
- collection_type: open
  name: Cartesia Agents Voice Changer API
  slug: open-cartesia-ai-voice-changer-api
- collection_type: open
  name: Cartesia Agents Voices API
  slug: open-cartesia-ai-voices-api
- collection_type: open
  name: Cartesia Agents Webhooks API
  slug: open-cartesia-ai-webhooks-api
- collection_type: open
  name: Cartesia API
  slug: open-cartesia-ai
- collection_type: open
  name: Cartesia API
  slug: open-cartesia
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
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cartesia.ai/llms.txt
created: '2026-07-02'
description: Cartesia builds real-time voice AI - the Sonic family of text-to-speech models, Ink speech-to-text models, and a Voice Agents platform for building and deploying telephone and web voice agents. The core generation surface is exposed both as REST (bytes and Server-Sent Events) and as a low-latency, bidirectional WebSocket protocol at wss://api.cartesia.ai for streaming TTS and STT with multiplexed contexts, word/phoneme timestamps, and mid-stream flush and cancel.
finops:
- name: Cartesia Ai Finops
  service_category: AI and Machine Learning
  slug: cartesia-ai-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Cartesia real-time text-to-speech and voice cloning API. Cartesia's native interfaces are REST, server-sent events, and WebSocket; this sche
  name: Cartesia GraphQL Schema
  slug: cartesia-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cartesia-ai.png
layout: provider
modified: '2026-08-08'
name: Cartesia
nav: Providers
network: true
overview: 'Cartesia publishes 23 APIs on the [APIs.io](https://apis.io/) network, including TTS WebSocket API, STT WebSocket API, Agents API, and 20 more. Tagged areas include Artificial Intelligence, Voice AI, Text-to-Speech, Speech-to-Text, and Real-Time.


  The Cartesia catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cartesia''s developer surface includes authentication, engineering blog, documentation, pricing, and 13 more developer resources.'
plans:
- name: Cartesia Ai Plans Pricing
  plan_count: 6
  slug: cartesia-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 15
  name: Cartesia Ai Rate Limits
  slug: cartesia-ai-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Cartesia API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: cartesia-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 11.4
    contract_quality: 62.5
    developer_ergonomics: 35.7
    discoverability: 70.4
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Artificial Intelligence
- Voice AI
- Text-to-Speech
- Speech-to-Text
- Real-Time
- WebSocket
- Voice Cloning
- Voice Agents
website: https://cartesia.ai/
---
