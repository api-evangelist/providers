---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
- acting_count: 24
  human_in_the_loop: 4
  name: Vonage Video Agentic Access
  operation_count: 33
  slug: vonage-video-agentic-access
  summary_line: 33 operations · 24 acting · 4 human-in-the-loop
api_count: 9
apis:
- description: Record sessions as composed or individual-stream archives.
  name: Vonage Video API Archives API
  slug: vonage-video-archives-api
- description: Live stream sessions to HLS and RTMP destinations.
  name: Vonage Video API Broadcasts API
  slug: vonage-video-broadcasts-api
- description: Start and stop real-time live captions.
  name: Vonage Video API Captions API
  slug: vonage-video-captions-api
- description: Force-disconnect and mute participants.
  name: Vonage Video API Moderation API
  slug: vonage-video-moderation-api
- description: Experience Composer render service.
  name: Vonage Video API Render API
  slug: vonage-video-render-api
- description: Create sessions and manage connections.
  name: Vonage Video API Sessions API
  slug: vonage-video-sessions-api
- description: Send server-side signals into a session.
  name: Vonage Video API Signaling API
  slug: vonage-video-signaling-api
- description: Dial SIP/PSTN endpoints into a session and play DTMF.
  name: Vonage Video API SIP API
  slug: vonage-video-sip-api
- description: Inspect streams and change stream layout classes.
  name: Vonage Video API Streams API
  slug: vonage-video-streams-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vonage Video Archives API
  slug: open-vonage-video-archives-api
- collection_type: open
  name: Vonage Video Archives Broadcasts API
  slug: open-vonage-video-broadcasts-api
- collection_type: open
  name: Vonage Video Archives Captions API
  slug: open-vonage-video-captions-api
- collection_type: open
  name: Vonage Video Archives Moderation API
  slug: open-vonage-video-moderation-api
- collection_type: open
  name: Vonage Video Archives Render API
  slug: open-vonage-video-render-api
- collection_type: open
  name: Vonage Video Archives Sessions API
  slug: open-vonage-video-sessions-api
- collection_type: open
  name: Vonage Video Archives Signaling API
  slug: open-vonage-video-signaling-api
- collection_type: open
  name: Vonage Video Archives SIP API
  slug: open-vonage-video-sip-api
- collection_type: open
  name: Vonage Video Archives Streams API
  slug: open-vonage-video-streams-api
- collection_type: open
  name: Vonage Video API
  slug: open-vonage-video
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vonage-video-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vonage-video-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vonage-video-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vonage
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vonage
- group: company
  title: ''
  type: Website
  url: https://www.vonage.com/communications-apis/video/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vonage.com/en/video/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/vonage-video-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vonage-video-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vonage-video-finops.yml
created: '2026-06-20'
description: Vonage Video API (formerly OpenTok / TokBox) is a programmable live video platform for building real-time interactive video, voice, and messaging into apps. Its REST API on the Vonage Video Cloud creates sessions and drives advanced server-side features - recording (archives), live streaming broadcasts, signaling, SIP interconnect, and the Experience Composer render service - authenticated with JWT Bearer tokens.
finops:
- name: Vonage Video Finops
  service_category: Communications and Media
  slug: vonage-video-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vonage-video.png
layout: provider
modified: '2026-06-20'
name: Vonage Video API
nav: Providers
network: true
overview: 'Vonage Video API publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Archives API, Broadcasts API, Captions API, and 6 more. Tagged areas include Video, WebRTC, Live Streaming, Real-Time Communications, and CPaaS.


  Vonage Video API''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Vonage Video Plans Pricing
  plan_count: 3
  slug: vonage-video-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 7
  name: Vonage Video Rate Limits
  slug: vonage-video-rate-limits
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vonage-video/refs/heads/main/screenshots/vonage-video-2026-06-20T201136.png
security:
- kind: authentication
  name: Vonage Video Authentication
  slug: vonage-video-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vonage Video Domain Security
  slug: vonage-video-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vonage-video
tags:
- Video
- WebRTC
- Live Streaming
- Real-Time Communications
- CPaaS
website: https://www.vonage.com/communications-apis/video/
---
