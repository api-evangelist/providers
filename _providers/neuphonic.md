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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Neuphonic Agentic Access
  operation_count: 12
  slug: neuphonic-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 7
apis:
- description: WebSocket endpoint for continuous, low-latency text-to-speech streaming. Enables real-time voice synthesis with sub-25ms latency, supporting multiple text chunks over a single persistent connection. I
  name: Neuphonic TTS WebSocket API
  slug: neuphonic-tts-websocket-api
- description: REST API for creating and managing cloned voices. Accepts audio samples (MP3 or WAV, minimum 6 seconds, under 10MB) and generates a custom voice model. Supports creating, retrieving, updating, listing
  name: Neuphonic Voice Cloning API
  slug: neuphonic-voice-cloning-api
- description: REST API for creating and managing conversational AI voice agents. Agents combine Neuphonic TTS with GPT-4o for interactive voice applications and support Model Context Protocol (MCP) server integrati
  name: Neuphonic Agent API
  slug: neuphonic-agent-api
- description: The Agents API from Neuphonic — 3 operation(s) for agents.
  name: Neuphonic Agents API
  slug: neuphonic-agents-api
- description: The Ping API from Neuphonic — 1 operation(s) for ping.
  name: Neuphonic Ping API
  slug: neuphonic-ping-api
- description: The Sse API from Neuphonic — 2 operation(s) for sse.
  name: Neuphonic Sse API
  slug: neuphonic-sse-api
- description: The Voices API from Neuphonic — 2 operation(s) for voices.
  name: Neuphonic Voices API
  slug: neuphonic-voices-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Neuphonic Agents API
  slug: open-neuphonic-agents-api
- collection_type: open
  name: Neuphonic Agents Ping API
  slug: open-neuphonic-ping-api
- collection_type: open
  name: Neuphonic Agents Sse API
  slug: open-neuphonic-sse-api
- collection_type: open
  name: Neuphonic Agents Voices API
  slug: open-neuphonic-voices-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/neuphonic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neuphonic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neuphonic-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.neuphonic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.neuphonic.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neuphonic
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/neuphonic
- group: other
  title: ''
  type: X
  url: https://twitter.com/neuphonicspeech
- group: operate
  title: ''
  type: StatusPage
  url: https://status.neuphonic.com/
- group: other
  title: ''
  type: Playground
  url: https://app.neuphonic.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/neuphonic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neuphonic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/neuphonic-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/neuphonic-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/neuphonic-context.jsonld
created: 2026-06-12
description: Neuphonic is an ultra-low-latency voice AI platform specializing in real-time text-to-speech synthesis with sub-25ms latency, making it suitable for conversational AI and live applications. The platform provides both a cloud-hosted API with WebSocket streaming and Server-Sent Events (SSE), as well as open-source on-device models (NeuTTS Air, NeuTTS Nano) that run without a GPU. Neuphonic supports nine languages including English, Spanish, German, French, Urdu, Japanese, Korean, Chinese, and Portuguese, and offers instant voice cloning from short audio samples. Developers can also build conversational AI agents via the Agent API, which integrates with GPT-4o and supports Model Context Protocol (MCP) servers. Authentication uses API keys passed via the X-API-KEY header for SSE and as a query parameter for WebSocket connections.
examples:
- key_count: 5
  name: Clone Voice
  slug: clone-voice
- key_count: 4
  name: Create Agent
  slug: create-agent
- key_count: 4
  name: List Voices
  slug: list-voices
- key_count: 4
  name: Sse Speak
  slug: sse-speak
finops:
- name: Neuphonic Finops
  service_category: ''
  slug: neuphonic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neuphonic.png
json_schemas:
- name: Agent
  property_count: 7
  slug: neuphonic-agent
- name: SSE TTS Request
  property_count: 4
  slug: neuphonic-sse-request
- name: Voice
  property_count: 5
  slug: neuphonic-voice
jsonld:
- class_count: 5
  name: Neuphonic Context
  property_count: 29
  slug: neuphonic-context
layout: provider
modified: 2026-06-12
name: Neuphonic
nav: Providers
network: true
overview: 'Neuphonic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including TTS WebSocket API, Agents API, Ping API, and 2 more. Tagged areas include Text-to-Speech, Voice AI, Audio, Streaming, and WebSocket.


  The Neuphonic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Neuphonic''s developer surface includes authentication, documentation, and 13 more developer resources.'
plans:
- name: Neuphonic Plans Pricing
  plan_count: 3
  slug: neuphonic-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 4
  name: Neuphonic Rate Limits
  slug: neuphonic-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Neuphonic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: neuphonic-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.3
  delta: -6.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 74.1
    developer_ergonomics: 25.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/neuphonic/refs/heads/main/screenshots/neuphonic-2026-06-20T190223.png
security:
- kind: authentication
  name: Neuphonic Authentication
  slug: neuphonic-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Neuphonic Domain Security
  slug: neuphonic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neuphonic
tags:
- Text-to-Speech
- Voice AI
- Audio
- Streaming
- WebSocket
- Voice Cloning
- Conversational AI
- Real-Time
- Multilingual
- On-Device AI
website: https://www.neuphonic.com/
---
