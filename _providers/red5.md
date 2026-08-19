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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Red5 Agentic Access
  operation_count: 35
  slug: red5-agentic-access
  summary_line: 35 operations · 18 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: The Red5 Pro Server API is an HTTP-based REST API for gathering server, application, client, and stream statistics from a running Red5 Pro instance. It exposes endpoints for server health checks, appl
  name: Red5 Pro Server API
  slug: server-api
- description: The Red5 Pro WebRTC SDK is a JavaScript library for integrating low-latency live streaming publish and subscribe capabilities into web applications. It supports WHIP for WebRTC publishing and WHEP for
  name: Red5 Pro WebRTC SDK
  slug: webrtc-sdk
- description: 'The Red5 Core SDK is a native client library for building real-time streaming applications on Linux, Windows, and macOS desktop platforms. It offers interfaces for server connection management, media '
  name: Red5 Core SDK
  slug: core-sdk
- description: The Red5 Pro iOS Streaming SDK is a native iOS library for integrating real-time live streaming publish and subscribe capabilities into iOS applications. It supports H.264 video and AAC/Opus audio enc
  name: Red5 Pro iOS Streaming SDK
  slug: ios-sdk
- description: The Red5 Pro Android Streaming SDK is a native Android library for integrating real-time live streaming publish and subscribe capabilities into Android applications. It supports H.264/H.265 video enco
  name: Red5 Pro Android Streaming SDK
  slug: android-sdk
- description: Node metrics, system info, and autoscaling management
  name: Red5 Admin API
  slug: red5-admin-api
- description: Application scope statistics and management
  name: Red5 Applications API
  slug: red5-applications-api
- description: Restream recorded FLV or MP4 files as pseudo-live streams
  name: Red5 File Restreamer API
  slug: red5-file-restreamer-api
- description: Image overlay management for mixer sessions
  name: Red5 Images API
  slug: red5-images-api
- description: Input stream management for mixer sessions
  name: Red5 Inputs API
  slug: red5-inputs-api
- description: Server log access endpoints
  name: Red5 Logs API
  slug: red5-logs-api
- description: Mixer session lifecycle management
  name: Red5 Mixers API
  slug: red5-mixers-api
- description: Stream provisioning, authentication, and configuration
  name: Red5 Provision API
  slug: red5-provision-api
- description: WHIP, WHEP, and WebSocket proxy endpoints
  name: Red5 Proxy API
  slug: red5-proxy-api
- description: Configure RTMP and RTMPS push/pull restreaming
  name: Red5 RTMP Restreamer API
  slug: red5-rtmp-restreamer-api
- description: Server-level restreamer plugin configuration
  name: Red5 Servlet Configuration API
  slug: red5-servlet-configuration-api
- description: Live stream enumeration, statistics, and control
  name: Red5 Streams API
  slug: red5-streams-api
artifact_total: 50
asyncapis:
- description: AsyncAPI specification for the Red5 Pro WebRTC streaming event system, covering WebSocket signaling messages exchanged during publish and subscribe sessions. Red5 Pro WebRTC uses WebSocket connections
  name: Red5 Pro WebRTC Streaming Events
  slug: red5-webrtc-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Red5 Pro Brew Mixer Admin API
  slug: open-red5-admin-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Applications API
  slug: open-red5-applications-api
- collection_type: open
  name: Red5 Pro Brew Mixer API
  slug: open-red5-brew-mixer-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin File Restreamer API
  slug: open-red5-file-restreamer-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Images API
  slug: open-red5-images-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Inputs API
  slug: open-red5-inputs-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Logs API
  slug: open-red5-logs-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Mixers API
  slug: open-red5-mixers-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Provision API
  slug: open-red5-provision-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Proxy API
  slug: open-red5-proxy-api
- collection_type: open
  name: Red5 Pro Restreamer API
  slug: open-red5-restreamer-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin RTMP Restreamer API
  slug: open-red5-rtmp-restreamer-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Server API
  slug: open-red5-server-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Servlet Configuration API
  slug: open-red5-servlet-configuration-api
- collection_type: open
  name: Red5 Pro Stream Manager 2.0 API
  slug: open-red5-stream-manager-2
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Streams API
  slug: open-red5-streams-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/red5-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red5-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/red5-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/red5pro
- group: company
  title: ''
  type: Website
  url: https://www.red5.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.red5.net/docs/red5-pro/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/red5pro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Red5
- group: build
  title: ''
  type: SDKs
  url: https://www.red5.net/live-streaming-sdks/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.red5.net/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.red5.net/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.red5.net/contact/
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/red5-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red5-stream-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red5-restream-provision-schema.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red5-server-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/red5-stream-manager-2-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/red5-brew-mixer-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/red5-restreamer-api-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/red5-webrtc-streaming-asyncapi.yml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/red5-stream-structure.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/red5-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/red5-vocabulary.yml
created: '2026-03-01'
description: Red5 provides real-time streaming infrastructure for live video and audio delivery at scale. The Red5 Pro platform includes a media server, Stream Manager 2.0 for autoscaling cloud deployments, the Brew Mixer for composite stream production, a Restreamer for pushing live streams to social media and RTMP destinations, and WebRTC and native SDKs for browser and mobile integration. Red5 APIs enable programmatic management of streams, mixers, restreaming, cluster orchestration, and node monitoring. Use cases include live events, sports broadcasting, interactive video, gaming, surveillance, and enterprise communications requiring ultra-low latency streaming.
examples:
- key_count: 2
  name: Red5 Server Api List Streams Example
  slug: red5-server-api-list-streams-example
- key_count: 2
  name: Red5 Stream Manager Create Provision Example
  slug: red5-stream-manager-create-provision-example
finops:
- name: Red5 Finops
  service_category: Streaming Media
  slug: red5-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/red5.png
json_schemas:
- name: Red5 Pro Restream Provision
  property_count: 8
  slug: red5-restream-provision
- name: Red5 Pro Stream
  property_count: 12
  slug: red5-stream
json_structures:
- name: Red5 Stream Structure
  property_count: 0
  slug: red5-stream-structure
jsonld:
- class_count: 0
  name: Red5 Context
  property_count: 9
  slug: red5-context
layout: provider
modified: '2026-05-19'
name: Red5
nav: Providers
network: true
overview: 'Red5 publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Pro Server API, Pro WebRTC SDK, Admin API, and 11 more. Tagged areas include Live Streaming, Media, Real-Time, RTMP, and Streaming.


  The Red5 catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Red5''s developer surface includes authentication, documentation, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Red5 Plans Pricing
  plan_count: 2
  slug: red5-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 2
  name: Red5 Rate Limits
  slug: red5-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Red5 API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: red5-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Red5 API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: red5-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Red5 API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 8
  slug: red5-rules
score:
  band: thin
  composite: 37.4
  delta: -4.2
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 61.9
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red5/refs/heads/main/screenshots/red5-2026-06-20T192724.png
security:
- kind: authentication
  name: Red5 Authentication
  slug: red5-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Red5 Domain Security
  slug: red5-domain-security
  summary_line: TLSv1.3 · DMARC
slug: red5
tags:
- Live Streaming
- Media
- Real-Time
- RTMP
- Streaming
- Video
- WebRTC
website: https://www.red5.net/
---
