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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 37
  human_in_the_loop: 5
  name: Livepeer Agentic Access
  operation_count: 64
  slug: livepeer-agentic-access
  summary_line: 64 operations · 37 acting · 5 human-in-the-loop
api_count: 28
apis:
- description: Primary REST API for the Livepeer Studio gateway. Resource-oriented JSON endpoints for live streams, on-demand assets, multistream targets, transcoding jobs, sessions, playback, signing keys, webhooks
  name: Livepeer Studio REST API
  slug: studio
- description: Endpoints for creating and managing live streams, ingest RTMP/WHIP URLs, profiles for adaptive bitrate transcoding, recording, and stream keys.
  name: Livepeer Streams API
  slug: streams
- description: Endpoints for uploading, importing, transcoding, and serving on-demand video assets, including direct upload, URL import, and IPFS storage.
  name: Livepeer Assets API
  slug: assets
- description: Endpoints for registering and managing multistream destinations that forward an active live stream to additional RTMP/RTMPS endpoints such as YouTube, Twitch, or X.
  name: Livepeer Multistream Targets API
  slug: multistream
- description: Webhook management endpoints plus outbound event notifications for stream lifecycle events (stream.started, stream.idle, recording.ready, asset.ready, playback.access_control). Signed payloads deliver
  name: Livepeer Webhooks API
  slug: webhooks
- description: Endpoints for one-off transcoding jobs against source files in object storage, returning a job handle and transcoded renditions.
  name: Livepeer Transcode API
  slug: transcode
- description: Endpoints for retrieving completed live session recordings and metadata for past live streams.
  name: Livepeer Sessions API
  slug: sessions
- description: Playback info endpoint returning HLS/WebRTC playback URLs and metadata for a stream or asset, plus access-control gating.
  name: Livepeer Playback API
  slug: playback
- description: Endpoints for managing JWT signing keys used for playback access control and webhook signature verification.
  name: Livepeer Signing Keys API
  slug: signing-keys
- description: AI video and image generation endpoints (text-to-image, image-to-image, image-to-video, upscale, audio-to-text) routed through the Livepeer AI subnet of GPU orchestrators.
  name: Livepeer AI Generate API
  slug: ai-generate
- description: Official TypeScript/JavaScript SDK (@livepeer/ai or livepeer) for the Livepeer Studio REST API and AI endpoints.
  name: Livepeer JavaScript/TypeScript SDK
  slug: js-sdk
- description: Official Python SDK for the Livepeer Studio REST API.
  name: Livepeer Python SDK
  slug: python-sdk
- description: Official Go SDK for the Livepeer Studio REST API.
  name: Livepeer Go SDK
  slug: go-sdk
- description: Official Ruby SDK for the Livepeer Studio REST API.
  name: Livepeer Ruby SDK
  slug: ruby-sdk
- description: React video player component for HLS/WebRTC playback of Livepeer streams and assets, with customisable controls and access-control integration.
  name: Livepeer React Player Component
  slug: react-player
- description: React component for in-browser WebRTC broadcasting to a Livepeer live stream, with device selection and settings controls.
  name: Livepeer React Broadcast Component
  slug: react-broadcast
- description: Operations related to access control/signing keys api
  name: Livepeer accessControl API
  slug: livepeer-accesscontrol-api
- description: Operations related to asset/vod api
  name: Livepeer asset API
  slug: livepeer-asset-api
- description: Operations related to AI generate api
  name: Livepeer generate API
  slug: livepeer-generate-api
- description: Operations related to metrics api
  name: Livepeer metrics API
  slug: livepeer-metrics-api
- description: Operations related to multistream api
  name: Livepeer multistream API
  slug: livepeer-multistream-api
- description: Operations related to playback api
  name: Livepeer playback API
  slug: livepeer-playback-api
- description: Operations related to rooms api
  name: Livepeer room API
  slug: livepeer-room-api
- description: Operations related to session api
  name: Livepeer session API
  slug: livepeer-session-api
- description: Operations related to livestream api
  name: Livepeer stream API
  slug: livepeer-stream-api
- description: Operations related to tasks api
  name: Livepeer task API
  slug: livepeer-task-api
- description: Operations related to transcode api
  name: Livepeer transcode API
  slug: livepeer-transcode-api
- description: Operations related to webhook api
  name: Livepeer webhook API
  slug: livepeer-webhook-api
artifact_total: 35
collections:
- collection_type: open
  name: Livepeer API Reference
  slug: open-livepeer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/livepeer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livepeer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/livepeer-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/livepeer
- group: company
  title: ''
  type: Website
  url: https://livepeer.org/
- group: other
  title: ''
  type: Studio
  url: https://livepeer.studio/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.livepeer.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/livepeer
- group: operate
  title: ''
  type: Status
  url: https://status.livepeer.studio/
- group: commercial
  title: ''
  type: Plans
  url: plans/livepeer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/livepeer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/livepeer-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.livepeer.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://livepeer.org/blog
created: '2026-05-23'
description: Livepeer is a decentralized video infrastructure network. Independent orchestrators run GPU hardware to provide live and on-demand video transcoding services, paid for in ETH/LPT on the Livepeer protocol. Livepeer Studio is the managed gateway and developer platform sitting on top of the network, exposing a REST API at livepeer.studio/api for live streams, on- demand assets, multistream targets, transcoding jobs, sessions, playback, signing keys, AI generation (text-to-image, image-to-image, image-to-video, upscale, audio-to-text), and webhooks. Official SDKs are published for JavaScript/TypeScript, Python, Go, and Ruby, with React Player and React Broadcast components for client-side playback and ingest.
finops:
- name: Livepeer Finops
  service_category: API
  slug: livepeer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/livepeer.png
layout: provider
modified: '2026-05-23'
name: Livepeer
nav: Providers
network: true
overview: 'Livepeer publishes 12 APIs on the [APIs.io](https://apis.io/) network, including accessControl API, asset API, generate API, and 9 more. Tagged areas include Video, Streaming, Transcoding, Decentralized, and Web3.


  Livepeer''s developer surface includes authentication, documentation, GitHub presence, status page, engineering blog, and 9 more developer resources.'
plans:
- name: Livepeer Plans Pricing
  plan_count: 1
  slug: livepeer-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 2
  name: Livepeer Rate Limits
  slug: livepeer-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 3.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.8
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/livepeer/refs/heads/main/screenshots/livepeer-2026-06-20T184613.png
security:
- kind: authentication
  name: Livepeer Authentication
  slug: livepeer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Livepeer Domain Security
  slug: livepeer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: livepeer
tags:
- Video
- Streaming
- Transcoding
- Decentralized
- Web3
- Live Video
- AI Video
website: https://livepeer.org/
---
