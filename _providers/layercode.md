---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Layercode Agentic Access
  operation_count: 8
  slug: layercode-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 5
apis:
- description: Bidirectional realtime WebSocket transport that streams base64 PCM microphone audio from the browser to Layercode and streams synthesized speech, transcripts, and structured data back, authorized with
  name: Layercode Realtime Voice API
  slug: layercode-realtime-voice-api
- description: 'HMAC-signed webhook Layercode POSTs to your backend with session and transcript events (session.start, message, data, session.update, session.end); your backend streams response.tts / response.data / '
  name: Layercode Webhooks API
  slug: layercode-webhooks-api
- description: The Agents API from Layercode — 2 operation(s) for agents.
  name: Layercode Agents API
  slug: layercode-agents-api
- description: The Calls API from Layercode — 1 operation(s) for calls.
  name: Layercode Calls API
  slug: layercode-calls-api
- description: The Sessions API from Layercode — 3 operation(s) for sessions.
  name: Layercode Sessions API
  slug: layercode-sessions-api
artifact_total: 14
asyncapis:
- description: AsyncAPI 2.6 description of Layercode's **realtime voice transport**, a genuine bidirectional WebSocket documented at https://docs.layercode.com/api-reference/frontend-ws-api. Unlike one-way HTTP SSE,
  name: Layercode Realtime Voice WebSocket API
  slug: layercode-asyncapi
collections:
- collection_type: open
  name: Layercode REST API
  slug: open-layercode
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/layercode-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/layercode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/layercode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/layercodedev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/layercode
- group: company
  title: ''
  type: Website
  url: https://layercode.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.layercode.com
- group: commercial
  title: ''
  type: Plans
  url: plans/layercode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/layercode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/layercode-finops.yml
created: '2026-06-21'
description: Layercode provides voice-AI agent infrastructure - low-latency voice pipelines that turn any LLM or text-based agent into a conversational voice agent for web, mobile, and phone. A REST API manages agents, sessions, and outbound calls, while a realtime WebSocket transport streams audio to the browser and a signed webhook delivers transcripts to your backend, which streams text-to-speech responses back over Server-Sent Events.
finops:
- name: Layercode Finops
  service_category: AI and Machine Learning
  slug: layercode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/layercode.png
layout: provider
modified: '2026-06-21'
name: Layercode
nav: Providers
network: true
overview: 'Layercode publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Realtime Voice API, Webhooks API, Agents API, and 2 more. Tagged areas include AI, Voice, Voice Agents, Realtime, and Low Latency.


  The Layercode catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Layercode''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Layercode Plans Pricing
  plan_count: 1
  slug: layercode-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 3
  name: Layercode Rate Limits
  slug: layercode-rate-limits
rules:
- name: Layercode API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: layercode-asyncapi-spectral-rules
score:
  band: thin
  composite: 42.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.4
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 36.8
  previous_composite: 42.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Layercode Authentication
  slug: layercode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Layercode Domain Security
  slug: layercode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: layercode
tags:
- AI
- Voice
- Voice Agents
- Realtime
- Low Latency
website: https://layercode.com
---
