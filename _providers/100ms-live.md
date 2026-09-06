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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 34
  human_in_the_loop: 8
  name: 100Ms Live Agentic Access
  operation_count: 63
  slug: 100ms-live-agentic-access
  summary_line: 63 operations · 34 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: In-session control of running rooms and connected peers.
  name: 100ms Active Rooms API
  slug: 100ms-live-active-rooms-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Query webhook events, track events, recording events, errors, and peer quality.
  name: 100ms Analytics API
  slug: 100ms-live-analytics-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Push the room feed to YouTube / Twitch / Facebook via RTMP.
  name: 100ms External Streams API
  slug: 100ms-live-external-streams-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: HLS live streams driven from a 100ms room.
  name: 100ms Live Streams API
  slug: 100ms-live-live-streams-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Templates, roles, and recording configuration.
  name: 100ms Policy API
  slug: 100ms-live-policy-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Real-time polls and quizzes inside a room.
  name: 100ms Polls API
  slug: 100ms-live-polls-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Output assets (mp4, mp3, transcript, chat) produced by recordings.
  name: 100ms Recording Assets API
  slug: 100ms-live-recording-assets-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Composite and track-level recordings of sessions.
  name: 100ms Recordings API
  slug: 100ms-live-recordings-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Short codes used by client apps to join a room.
  name: 100ms Room Codes API
  slug: 100ms-live-room-codes-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Persistent containers for a live session.
  name: 100ms Rooms API
  slug: 100ms-live-rooms-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Historical sessions inside a room.
  name: 100ms Sessions API
  slug: 100ms-live-sessions-api
- baseURL: https://api.100ms.live/v2
  baseurl_source: declared
  description: Per-room RTMP ingest stream keys.
  name: 100ms Stream Keys API
  slug: 100ms-live-stream-keys-api
artifact_total: 57
collections:
- collection_type: postman
  name: 100ms Server-Side Active Rooms API
  slug: postman-100ms-live-active-rooms-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Analytics API
  slug: postman-100ms-live-analytics-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms External Streams API
  slug: postman-100ms-live-external-streams-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Live Streams API
  slug: postman-100ms-live-live-streams-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Policy API
  slug: postman-100ms-live-policy-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Polls API
  slug: postman-100ms-live-polls-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Recording Assets API
  slug: postman-100ms-live-recording-assets-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Recordings API
  slug: postman-100ms-live-recordings-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Room Codes API
  slug: postman-100ms-live-room-codes-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms API
  slug: postman-100ms-live-rooms-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Sessions API
  slug: postman-100ms-live-sessions-api
- collection_type: postman
  name: 100ms Server-Side Active Rooms Stream Keys API
  slug: postman-100ms-live-stream-keys-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 100ms Server-Side Active Rooms API
  slug: open-100ms-live-active-rooms-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Analytics API
  slug: open-100ms-live-analytics-api
- collection_type: open
  name: 100ms Server-Side Active Rooms External Streams API
  slug: open-100ms-live-external-streams-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Live Streams API
  slug: open-100ms-live-live-streams-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Policy API
  slug: open-100ms-live-policy-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Polls API
  slug: open-100ms-live-polls-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Recording Assets API
  slug: open-100ms-live-recording-assets-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Recordings API
  slug: open-100ms-live-recordings-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Room Codes API
  slug: open-100ms-live-room-codes-api
- collection_type: open
  name: 100ms Server-Side Active Rooms API
  slug: open-100ms-live-rooms-api
- collection_type: open
  name: 100ms Server-Side API
  slug: open-100ms-live-server-side-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Sessions API
  slug: open-100ms-live-sessions-api
- collection_type: open
  name: 100ms Server-Side Active Rooms Stream Keys API
  slug: open-100ms-live-stream-keys-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/100ms-live-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/100ms/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/100ms-live-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/100ms-live-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/100ms-live-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/100ms-live-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/100ms-live-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.100ms.live/
- group: docs
  title: ''
  type: Documentation
  url: https://www.100ms.live/docs/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.100ms.live/register
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.100ms.live/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.100ms.live/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/100mslive
- group: operate
  title: ''
  type: StatusPage
  url: https://status.100ms.live/
- group: company
  title: ''
  type: Blog
  url: https://www.100ms.live/blog
- group: build
  title: ''
  type: Postman
  url: https://www.100ms.live/docs/server-side/v2/how-to-guides/set-up-postman
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/100mslive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/100mslive/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/100mslive/web-sdks
- group: build
  title: ''
  type: SDKs
  url: https://github.com/100mslive/100ms-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/100mslive/100ms-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/100mslive/100ms-react-native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/100mslive/100ms-flutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/100mslive/server-sdks
- group: build
  title: ''
  type: Examples
  url: https://github.com/100mslive/100ms-examples
- group: commercial
  title: ''
  type: Plans
  url: plans/100ms-live-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/100ms-live-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/100ms-live-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/100ms-live-room-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/100ms-live-recording-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/100ms-live-webhook-event-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/100ms-live-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/100ms-live-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/100ms-live-rules.yml
created: '2026-05-25'
description: 100ms is a live video and audio infrastructure company headquartered in Bengaluru, India that provides developer SDKs and a REST control plane for embedding video conferencing, interactive live streaming (HLS), RTMP ingest/egress, recording, real-time chat/messaging, polls, whiteboard, and AI-powered transcription into applications. The company was acquired by Disney+ Hotstar (JioCinema/JioHotstar) in 2023 and continues to operate as an independent commercial SaaS — the same infrastructure powering some of the largest live cricket audiences in the world (IPL on JioCinema/Hotstar). The platform exposes a single Server-Side REST API at api.100ms.live/v2 plus client SDKs for Web (JavaScript/React), iOS (Swift), Android (Kotlin), React Native, Flutter, and a Node.js server SDK, with public OpenAPI specs generated from the docs and a Postman collection.
examples:
- key_count: 2
  name: 100Ms Live Create Room Example
  slug: 100ms-live-create-room-example
- key_count: 2
  name: 100Ms Live Start Live Stream Example
  slug: 100ms-live-start-live-stream-example
- key_count: 2
  name: 100Ms Live Webhook Session Open Example
  slug: 100ms-live-webhook-session-open-example
finops:
- name: 100Ms Live Finops
  service_category: Networking and Content Delivery
  slug: 100ms-live-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the 100ms live video and audio infrastructure platform. 100ms provides a REST API at `api.100ms.live/v2` for managing rooms, templates, roles, p
  name: 100ms Live GraphQL Schema
  slug: 100ms-live-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/100ms-live.png
json_schemas:
- name: 100ms Recording
  property_count: 11
  slug: 100ms-live-recording
- name: 100ms Room
  property_count: 16
  slug: 100ms-live-room
- name: 100ms Webhook Event
  property_count: 5
  slug: 100ms-live-webhook-event
json_structures:
- name: 100Ms Live Room Structure
  property_count: 0
  slug: 100ms-live-room-structure
jsonld:
- class_count: 45
  name: 100Ms Live Context
  property_count: 7
  slug: 100ms-live-context
layout: provider
modified: '2026-05-25'
name: 100ms
nav: Providers
network: true
overview: '100ms publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Active Rooms API, Analytics API, External Streams API, and 9 more. Tagged areas include Live Video, Live Streaming, Video Conferencing, WebRTC, and HLS.


  The 100ms catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  100ms'' developer surface includes authentication, developer portal, documentation, signup flow, pricing, GitHub presence, engineering blog, and 27 more developer resources.'
plans:
- name: 100Ms Live Plans Pricing
  plan_count: 3
  slug: 100ms-live-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: 100Ms Live Rate Limits
  slug: 100ms-live-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: 100ms API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: 100ms-live-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: 100ms API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: 100ms-live-rules
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 81.5
    catalog_earned_first_party: 0.0
    catalog_gap: 33.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 28.8
    contract_quality: 64.2
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/100ms-live/refs/heads/main/screenshots/100ms-live-2026-06-20T162232.png
security:
- kind: authentication
  name: 100Ms Live Authentication
  slug: 100ms-live-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 100Ms Live Domain Security
  slug: 100ms-live-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 100Ms Live Vulnerability Disclosure
  slug: 100ms-live-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: 100Ms Live Trust Center
  slug: 100ms-live-trust-center
  summary_line: SOC 2, HIPAA
slug: 100ms-live
tags:
- Live Video
- Live Streaming
- Video Conferencing
- WebRTC
- HLS
- RTMP
- Recording
- Real-Time Messaging
- Live Infrastructure
- India
website: https://www.100ms.live/
---
