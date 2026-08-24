---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 35
  human_in_the_loop: 2
  name: Dolby Io Agentic Access
  operation_count: 85
  slug: dolby-io-agentic-access
  summary_line: 85 operations · 35 acting · 2 human-in-the-loop
api_count: 18
apis:
- description: Legacy Dolby.io Media APIs for cloud-based audio and video processing. Includes Enhance (noise reduction, leveling, dialog isolation), Analyze (loudness, speech metrics, diagnostics), Transcode (web/m
  name: Dolby.io Media API
  slug: dolby-io-media-api
- description: Legacy Communications APIs for high-quality WebRTC voice and video conferencing with spatial audio, music mode, noise suppression, and dial-in/dial-out. Includes Client Access Token, Conference, Recor
  name: Dolby.io Communications API
  slug: dolby-io-communications-api
- description: Server-Guided Ad Insertion (SGAI) for live streaming. The Signaling Service enriches origin manifests with advanced ad-break markers and integrates with Google Ad Manager for ad decisioning; the Ad En
  name: Dolby OptiView Ads API
  slug: dolby-optiview-ads-api
- description: Cross-platform video player (formerly THEOplayer) with SDKs for Web, Android, iOS & tvOS, React Native, Flutter, Chromecast, and Roku. Supports HLS, MPEG-DASH, DRM, advertising integration, low-latenc
  name: Dolby OptiView Player SDK (THEOplayer)
  slug: dolby-optiview-player-sdk
- description: The ABR Ladders API from Dolby.io — 1 operation(s) for abr ladders.
  name: Dolby.io ABR Ladders API
  slug: dolby-io-abr-ladders-api
- description: Account-level usage, tracking, and advanced reporting.
  name: Dolby.io Analytics API
  slug: dolby-io-analytics-api
- description: The Channels API from Dolby.io — 20 operation(s) for channels.
  name: Dolby.io Channels API
  slug: dolby-io-channels-api
- description: Cluster discovery for region-specific publish/subscribe URLs.
  name: Dolby.io Cluster API
  slug: dolby-io-cluster-api
- description: The Custom Endpoint Providers API from Dolby.io — 1 operation(s) for custom endpoint providers.
  name: Dolby.io Custom Endpoint Providers API
  slug: dolby-io-custom-endpoint-providers-api
- description: The Custom Endpoints API from Dolby.io — 2 operation(s) for custom endpoints.
  name: Dolby.io Custom Endpoints API
  slug: dolby-io-custom-endpoints-api
- description: The Distributions API from Dolby.io — 13 operation(s) for distributions.
  name: Dolby.io Distributions API
  slug: dolby-io-distributions-api
- description: The Engines API from Dolby.io — 6 operation(s) for engines.
  name: Dolby.io Engines API
  slug: dolby-io-engines-api
- description: The Ingests API from Dolby.io — 3 operation(s) for ingests.
  name: Dolby.io Ingests API
  slug: dolby-io-ingests-api
- description: Create and manage publish (broadcaster) tokens.
  name: Dolby.io PublishToken API
  slug: dolby-io-publishtoken-api
- description: The Regions API from Dolby.io — 1 operation(s) for regions.
  name: Dolby.io Regions API
  slug: dolby-io-regions-api
- description: Create and manage subscribe (viewer) tokens.
  name: Dolby.io SubscribeToken API
  slug: dolby-io-subscribetoken-api
- description: Register and manage event-driven webhooks for feeds, recordings, thumbnails, transcoders, and viewer connections.
  name: Dolby.io Webhook API
  slug: dolby-io-webhook-api
- description: The Webhooks API from Dolby.io — 4 operation(s) for webhooks.
  name: Dolby.io Webhooks API
  slug: dolby-io-webhooks-api
arazzos:
- description: Add an ingest and a transcoding engine to a channel, start it, and poll until playing.
  name: Dolby OptiView Attach Ingest and Engine then Go Live
  slug: dolby-io-attach-ingest-engine-and-go-live-workflow
- description: Resolve a channel, list its engine runs, and pull its transcoding-minutes analytics.
  name: Dolby OptiView Audit Channel Run History
  slug: dolby-io-audit-channel-run-history-workflow
- description: Register a recording webhook, then create a publish token that records its streams.
  name: Dolby OptiView Enable Recording Webhook and Token
  slug: dolby-io-enable-recording-webhook-and-token-workflow
- description: Pick an engine on a channel, fetch its most recent run, then list its full run history.
  name: Dolby OptiView Inspect an Engine's Last Run
  slug: dolby-io-inspect-engine-last-run-workflow
- description: Create a THEOlive channel, start it, and poll until it is live and playing.
  name: Dolby OptiView Provision and Start a Channel
  slug: dolby-io-provision-and-start-channel-workflow
- description: Discover the account cluster, create a publish token, then read it back to confirm.
  name: Dolby OptiView Provision a Broadcast Token with Cluster
  slug: dolby-io-provision-broadcast-token-with-cluster-workflow
- description: Create a geo-restricted subscribe token for a stream, then read it back to confirm.
  name: Dolby OptiView Provision a Viewer Token
  slug: dolby-io-provision-viewer-token-workflow
- description: Create a distribution for a channel and attach a token security key to protect playback.
  name: Dolby OptiView Publish a Secured Distribution
  slug: dolby-io-publish-distribution-with-security-workflow
- description: Select an engine on a channel, start it, and poll the engine until it is playing.
  name: Dolby OptiView Start a Single Engine and Confirm
  slug: dolby-io-start-single-engine-and-confirm-workflow
- description: Stop a running channel and poll until it has fully settled in the stopped state.
  name: Dolby OptiView Stop a Channel and Confirm Idle
  slug: dolby-io-stop-channel-and-confirm-idle-workflow
- description: Stop a channel, poll until it is fully stopped, then delete it.
  name: Dolby OptiView Tear Down a Channel
  slug: dolby-io-teardown-channel-workflow
artifact_total: 86
collections:
- collection_type: postman
  name: Dolby OptiView Real-time Streaming API
  slug: postman-dolby-io-realtime-streaming-api
- collection_type: postman
  name: Dolby OptiView THEOlive API
  slug: postman-dolby-io-theolive-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders API
  slug: open-dolby-io-abr-ladders-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Analytics API
  slug: open-dolby-io-analytics-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Channels API
  slug: open-dolby-io-channels-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Cluster API
  slug: open-dolby-io-cluster-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Custom Endpoint Providers API
  slug: open-dolby-io-custom-endpoint-providers-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Custom Endpoints API
  slug: open-dolby-io-custom-endpoints-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Distributions API
  slug: open-dolby-io-distributions-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Engines API
  slug: open-dolby-io-engines-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Ingests API
  slug: open-dolby-io-ingests-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders PublishToken API
  slug: open-dolby-io-publishtoken-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming API
  slug: open-dolby-io-realtime-streaming-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Regions API
  slug: open-dolby-io-regions-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders SubscribeToken API
  slug: open-dolby-io-subscribetoken-api
- collection_type: open
  name: Dolby OptiView THEOlive API
  slug: open-dolby-io-theolive-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Webhook API
  slug: open-dolby-io-webhook-api
- collection_type: open
  name: Dolby OptiView Real-time Streaming ABR Ladders Webhooks API
  slug: open-dolby-io-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dolby-io-realtime-streaming-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dolby-io-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/dolby-io-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dolby-io-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dolby-io-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dolby-io-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dolby-io-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/dolby-io-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dolby-io-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dolby-io-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/dolby-io-cli.yml
- group: design
  title: ''
  type: Components
  url: components/dolby-io-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dolby-io-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dolby-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dolby-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dolby-io-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dolbyio/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-attach-ingest-engine-and-go-live-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-audit-channel-run-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-enable-recording-webhook-and-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-inspect-engine-last-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-provision-and-start-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-provision-broadcast-token-with-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-provision-viewer-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-publish-distribution-with-security-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-start-single-engine-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-stop-channel-and-confirm-idle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dolby-io-teardown-channel-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://optiview.dolby.com
- group: start
  title: ''
  type: Portal
  url: https://dolby.io
- group: docs
  title: ''
  type: Documentation
  url: https://optiview.dolby.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dolby.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://optiview.dolby.com/docs/millicast/getting-started/
- group: start
  title: ''
  type: Signup
  url: https://streaming.dolby.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dolby.io
- group: commercial
  title: ''
  type: Pricing
  url: https://optiview.dolby.com/plans/
- group: commercial
  title: ''
  type: Plans
  url: plans/dolby-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dolby-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dolby-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dolby.io/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dolby.com/about/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dolby.com/about/legal/terms-of-service-for-dolby-io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.dolby.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dolbyio
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dolbyio-samples
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dolbyio/dolbyio-rest-apis-client-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dolbyio/dolbyio-rest-apis-client-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dolbyio/dolbyio-rest-apis-client-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dolbyio/rts-uikit-ios
- group: build
  title: ''
  type: Tools
  url: https://github.com/dolbyio/web-webrtc-stats
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dolbyio-samples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dolbyio-samples/streaming-WHIP-WHEP-node-sample
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dolbyio-samples/streaming-webhook-thumbnails
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dolbyio-samples/stream-app-web-viewer
- group: build
  title: ''
  type: Tools
  url: https://github.com/dolbyio/awesome-audio
- group: operate
  title: ''
  type: Forums
  url: https://github.com/orgs/dolbyio/discussions
- group: design
  title: ''
  type: Webhooks
  url: https://optiview.dolby.com/docs/millicast/webhooks/
- group: operate
  title: ''
  type: ChangeLog
  url: https://optiview.dolby.com/docs/release-notes/
created: '2026-05-25T00:00:00.000Z'
description: Dolby.io (now branded as Dolby OptiView) is Dolby Laboratories' developer platform for media, streaming, communications, and advertising APIs. Originally launched as a hub for Dolby's audio and video processing services (Media APIs, Communications APIs), the platform has consolidated around three OptiView pillars — Real-time Streaming (formerly Millicast), Live Streaming (formerly THEOlive), and Playback (formerly THEOplayer) — with an Advertising pillar built on Server-Guided Ad Insertion. The platform powers live sports streaming for the NFL, NASCAR, Paddy Power, and other large broadcasters, with sub-500ms WebRTC delivery, multi-format ingest (WHIP/WHEP, SRT, RTMP), and cross-platform playback SDKs.
examples:
- key_count: 2
  name: Dolby Io Create Publish Token Example
  slug: dolby-io-create-publish-token-example
- key_count: 2
  name: Dolby Io Create Subscribe Token Example
  slug: dolby-io-create-subscribe-token-example
- key_count: 3
  name: Dolby Io Create Webhook Example
  slug: dolby-io-create-webhook-example
features:
- OptiView Real-time Streaming (Millicast) — sub-500ms WebRTC streaming to 100k+ viewers
- WHIP and WHEP protocol support for standards-based publish and playback
- Multi-protocol ingest — WebRTC, SRT, RTMP, RTMPS
- Video codec support — H.264, H.265, VP8, VP9, AV1; Opus audio
- Publish and Subscribe token APIs with regex stream names, geo restrictions, IP binding
- Webhooks for feeds, recordings, thumbnails, transcoders, and viewer connections (HMAC-SHA1 signed)
- Account-level analytics — publish minutes, viewer minutes, bytes transferred
- OptiView Live (THEOlive) — live channels with low latency, Nielsen tracking, DRM, server-side ads
- Channels, Ingests, Engines, Distributions resource model with full REST and GraphQL surfaces
- Server-Guided Ad Insertion (SGAI) with Google Ad Manager integration
- OptiView Player SDKs — Web, Android, iOS/tvOS, React Native, Flutter, Chromecast, Roku
- Open Video UI component library for player customization
- Legacy Media APIs — Enhance, Analyze, Transcode, Diagnose, Music Mastering
- Legacy Communications APIs — WebRTC conferencing, spatial audio, recording, RTMP/HLS streaming
- Official REST API client SDKs for Node.js, Python, and .NET
- Real-time Streaming UI Kit for iOS (Swift)
- WebRTC statistics parser for browser-side diagnostics
- Region presence across US East/West, Europe, Asia-Pacific, and South America
- Bearer-token authentication via per-account API Secrets
- Status page tracking core services and regional infrastructure
finops:
- name: Dolby Io Finops
  service_category: Streaming and Media
  slug: dolby-io-finops
graphqls:
- description: ''
  name: Dolby.io GraphQL API
  slug: dolby-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dolby-io.png
json_schemas:
- name: Dolby OptiView Publish Token
  property_count: 0
  slug: dolby-io-publish-token
- name: Dolby OptiView Subscribe Token
  property_count: 0
  slug: dolby-io-subscribe-token
- name: Dolby OptiView Webhook
  property_count: 0
  slug: dolby-io-webhook
jsonld:
- class_count: 0
  name: Dolby Io Context
  property_count: 8
  slug: dolby-io-context
layout: provider
mcp_servers:
- description: ''
  name: Dolby.io MCP Server
  slug: dolbyio-mcp-server
modified: '2026-06-20'
name: Dolby.io
nav: Providers
network: true
overview: 'Dolby.io publishes 14 APIs on the [APIs.io](https://apis.io/) network, including ABR Ladders API, Analytics API, Channels API, and 11 more. Tagged areas include Media, Streaming, Real-Time Streaming, WebRTC, and Live Streaming.


  The Dolby.io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dolby.io''s developer surface includes CLI, authentication, developer portal, documentation, getting-started guide, signup flow, pricing, and 51 more developer resources.'
plans:
- name: Dolby Io Plans Pricing
  plan_count: 4
  slug: dolby-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Dolby Io Rate Limits
  slug: dolby-io-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Dolby.io API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: dolby-io-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Dolby.io API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: dolby-io-rules
score:
  band: strong
  composite: 65.3
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 30.3
    contract_quality: 66.5
    developer_ergonomics: 78.6
    discoverability: 83.3
    governance: 30.3
    operational_transparency: 57.9
  previous_composite: 65.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dolby-io/refs/heads/main/screenshots/dolby-io-2026-06-20T180134.png
security:
- kind: authentication
  name: Dolby Io Authentication
  slug: dolby-io-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dolby Io Domain Security
  slug: dolby-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dolby Io Vulnerability Disclosure
  slug: dolby-io-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: dolby-io
tags:
- Media
- Streaming
- Real-Time Streaming
- WebRTC
- Live Streaming
- Low Latency
- Video
- Audio
- Broadcast
- Player
- Advertising
- Dolby OptiView
- Millicast
- THEOlive
- THEOplayer
website: https://optiview.dolby.com
---
