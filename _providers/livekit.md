---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
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
  score: 24.8
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Server-side Twirp API for managing rooms, participants, tracks, mute/unmute, and metadata.
  name: LiveKit RoomService API
  slug: room-service-api
- description: Record rooms or stream them to RTMP / HLS endpoints; output to S3, GCS, Azure Blob.
  name: LiveKit Egress API
  slug: egress-api
- description: Pull RTMP, SRT, or WHIP streams into LiveKit rooms.
  name: LiveKit Ingress API
  slug: ingress-api
- description: SIP integration for inbound and outbound PSTN calls bridged into LiveKit rooms.
  name: LiveKit SIP (Telephony) API
  slug: sip-api
- description: Bi-directional WebSocket signaling protocol used by LiveKit clients to coordinate WebRTC sessions with the SFU. Clients send `SignalRequest` protobuf messages and receive `SignalResponse` protobuf mes
  name: LiveKit Signaling Protocol (WebSocket)
  slug: signaling-api
- description: Framework and runtime for voice / multimodal AI agents that join LiveKit rooms; integrates with LLM, STT, and TTS providers.
  name: LiveKit Agents API
  slug: agents-api
artifact_total: 14
asyncapis:
- description: AsyncAPI description of LiveKit's signaling WebSocket protocol. LiveKit clients connect to a LiveKit server (Cloud or self-hosted) over a WebSocket at the `/rtc` endpoint. Once connected, the client a
  name: LiveKit Signaling Protocol
  slug: livekit-asyncapi
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/livekit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/livekit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livekit-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/livekitco
- group: start
  title: ''
  type: Portal
  url: https://livekit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.livekit.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://livekit.io/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/livekit
- group: commercial
  title: ''
  type: License
  url: https://github.com/livekit/livekit/blob/master/LICENSE
- group: commercial
  title: ''
  type: Plans
  url: plans/livekit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/livekit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/livekit-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.livekit.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://livekit.io/blog
created: '2026-05-08'
description: LiveKit is an open-source WebRTC platform with a managed Cloud offering. APIs cover Rooms, Participants, Tracks, Egress (recording, RTMP), Ingress (RTMP/SRT), SIP (telephony), and Agents (LLM voice agents). The server APIs use Twirp (HTTP+Protobuf); SDKs are available for major languages and frameworks. Authentication via JWT room tokens.
finops:
- name: Livekit Finops
  service_category: Realtime Infrastructure
  slug: livekit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/livekit.png
layout: provider
modified: '2026-05-29'
name: LiveKit
nav: Providers
network: true
overview: 'LiveKit publishes 1 API on the [APIs.io](https://apis.io/) network: Signaling Protocol (WebSocket). Tagged areas include Realtime, WebRTC, Audio, Video, and Open Source.


  The LiveKit catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LiveKit''s developer surface includes developer portal, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Livekit Plans Pricing
  plan_count: 4
  slug: livekit-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 3
  name: Livekit Rate Limits
  slug: livekit-rate-limits
rules:
- name: LiveKit API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: livekit-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.9
  delta: -0.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 51.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 43.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/livekit/refs/heads/main/screenshots/livekit-2026-06-20T184644.png
security:
- kind: domain-security
  name: Livekit Domain Security
  slug: livekit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Livekit Vulnerability Disclosure
  slug: livekit-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Livekit Trust Center
  slug: livekit-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, PCI DSS, HIPAA, GDPR
slug: livekit
tags:
- Realtime
- WebRTC
- Audio
- Video
- Open Source
- AI Agents
- Voice
- Cloud
website: https://livekit.io/
---
