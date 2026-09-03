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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 18
  human_in_the_loop: 5
  name: Videosdk Agentic Access
  operation_count: 36
  slug: videosdk-agentic-access
  summary_line: 36 operations · 18 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.videosdk.live
  baseurl_source: declared
  description: HLS live streaming and playback management.
  name: VideoSDK HLS Streaming API
  slug: videosdk-hls-streaming-api
- baseURL: https://api.videosdk.live
  baseurl_source: declared
  description: Per-participant recording management.
  name: VideoSDK Participant Recordings API
  slug: videosdk-participant-recordings-api
- baseURL: https://api.videosdk.live
  baseurl_source: declared
  description: Start, stop, and manage meeting recordings.
  name: VideoSDK Recordings API
  slug: videosdk-recordings-api
- baseURL: https://api.videosdk.live
  baseurl_source: declared
  description: Manage meeting rooms.
  name: VideoSDK Rooms API
  slug: videosdk-rooms-api
- baseURL: https://api.videosdk.live
  baseurl_source: declared
  description: RTMP live streaming to external platforms.
  name: VideoSDK RTMP Streaming API
  slug: videosdk-rtmp-streaming-api
- baseURL: https://api.videosdk.live
  baseurl_source: declared
  description: Manage and query meeting sessions and participants.
  name: VideoSDK Sessions API
  slug: videosdk-sessions-api
- baseURL: https://api.videosdk.live
  baseurl_source: declared
  description: Per-track and composite recording management.
  name: VideoSDK Track Recordings API
  slug: videosdk-track-recordings-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VideoSDK Real-Time Communication HLS Streaming API
  slug: open-videosdk-hls-streaming-api
- collection_type: open
  name: VideoSDK Real-Time Communication HLS Streaming Participant Recordings API
  slug: open-videosdk-participant-recordings-api
- collection_type: open
  name: VideoSDK Real-Time Communication HLS Streaming Recordings API
  slug: open-videosdk-recordings-api
- collection_type: open
  name: VideoSDK Real-Time Communication HLS Streaming Rooms API
  slug: open-videosdk-rooms-api
- collection_type: open
  name: VideoSDK Real-Time Communication HLS Streaming RTMP Streaming API
  slug: open-videosdk-rtmp-streaming-api
- collection_type: open
  name: VideoSDK Real-Time Communication HLS Streaming Sessions API
  slug: open-videosdk-sessions-api
- collection_type: open
  name: VideoSDK Real-Time Communication HLS Streaming Track Recordings API
  slug: open-videosdk-track-recordings-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/videosdk-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/videosdk-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/videosdk-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/videosdk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/videosdk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/videosdk-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.videosdk.live
- group: docs
  title: ''
  type: Documentation
  url: https://docs.videosdk.live
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/videosdk-live
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/video-sdk
- group: other
  title: ''
  type: X
  url: https://x.com/video_sdk
- group: company
  title: ''
  type: Blog
  url: https://www.videosdk.live/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.videosdk.live/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/videosdk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/videosdk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/videosdk-finops.yml
created: '2026-06-13'
description: Real-time voice, video, and AI agent platform for developers. VideoSDK provides REST and WebSocket APIs for building video conferencing, live streaming, interactive broadcast applications, and real-time AI agent integrations with SDKs for JavaScript, React, Flutter, React Native, Android, and iOS.
examples:
- key_count: 4
  name: Create Room
  slug: create-room
- key_count: 4
  name: Fetch Sessions
  slug: fetch-sessions
- key_count: 4
  name: Start Hls Stream
  slug: start-hls-stream
- key_count: 4
  name: Start Recording
  slug: start-recording
- key_count: 4
  name: Start Rtmp Livestream
  slug: start-rtmp-livestream
finops:
- name: Videosdk Finops
  service_category: ''
  slug: videosdk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/videosdk.png
json_schemas:
- name: HlsStream
  property_count: 8
  slug: hls-stream
- name: Participant
  property_count: 3
  slug: participant
- name: Recording
  property_count: 8
  slug: recording
- name: Room
  property_count: 8
  slug: room
- name: Session
  property_count: 7
  slug: session
jsonld:
- class_count: 7
  name: Videosdk Context
  property_count: 50
  slug: videosdk-context
layout: provider
modified: '2026-06-13'
name: VideoSDK
nav: Providers
network: true
overview: 'VideoSDK publishes 7 APIs on the [APIs.io](https://apis.io/) network, including HLS Streaming API, Participant Recordings API, Recordings API, and 4 more. Tagged areas include Video, Audio, WebRTC, Real-Time Communication, and Live Streaming.


  The VideoSDK catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  VideoSDK''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Videosdk Plans Pricing
  plan_count: 3
  slug: videosdk-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Videosdk Rate Limits
  slug: videosdk-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: VideoSDK API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: videosdk-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 63.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/videosdk/refs/heads/main/screenshots/videosdk-2026-06-20T201124.png
security:
- kind: authentication
  name: Videosdk Authentication
  slug: videosdk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Videosdk Domain Security
  slug: videosdk-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Videosdk Vulnerability Disclosure
  slug: videosdk-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Videosdk Trust Center
  slug: videosdk-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: videosdk
tags:
- Video
- Audio
- WebRTC
- Real-Time Communication
- Live Streaming
- HLS
- RTMP
- AI Agents
- Video Conferencing
- WebSocket
website: https://www.videosdk.live
---
