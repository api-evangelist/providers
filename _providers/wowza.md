---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 251
  human_in_the_loop: 10
  name: Wowza Agentic Access
  operation_count: 491
  slug: wowza-agentic-access
  summary_line: 491 operations · 251 acting · 10 human-in-the-loop
api_count: 2
apis:
- description: Native Java API for extending and customizing the Wowza Streaming Engine media server via server listeners, application modules, HTTP providers, and Media Reader/Writer plugins. The Java API is the fo
  name: Wowza Streaming Engine Java API
  slug: wowza-streaming-engine-java-api
- description: Commercial-grade HTML5 video player with iOS, tvOS, and Android SDKs, DRM (Widevine, FairPlay, PlayReady), ad insertion, real-time streaming at scale plugin support, and 30+ modular plugins. Ships sta
  name: Wowza Flowplayer
  slug: wowza-flowplayer
- description: Wowza GoCoder broadcasting SDK for iOS and Android — capture, encode, and stream live video and audio from mobile devices directly to Wowza Streaming Engine or Wowza Video. Official sample repositorie
  name: Wowza GoCoder SDK
  slug: wowza-gocoder-sdk
- description: WebRTC-based SDK for delivering sub-second-latency live streams at scale through the Wowza Real-Time Streaming service. Public documentation repo and WebRTC sample applications are hosted in the Wowza
  name: Wowza Real-Time Streaming SDK
  slug: wowza-real-time-streaming-sdk
- description: Operations related to using advanced token authentication, known in Wowza Video as a default playback token behavior option, with videos. Use token authentication when distributing valuable or sensiti
  name: Wowza advanced_token_authentication API
  slug: wowza-advanced-token-authentication-api
- description: Operations related to engagement analytics for a VOD stream.
  name: Wowza analytics_engagement API
  slug: wowza-analytics-engagement-api
- description: Operations related to ingest analytics for a live stream.
  name: Wowza analytics_ingest API
  slug: wowza-analytics-ingest-api
- description: Operations related to popularity analytics.
  name: Wowza analytics_popularity API
  slug: wowza-analytics-popularity-api
- description: Operations related to viewer analytics.
  name: Wowza analytics_viewers API
  slug: wowza-analytics-viewers-api
- description: The Applications API from Wowza — 69 operation(s) for applications.
  name: Wowza Applications API
  slug: wowza-applications-api
- description: <blockquote>The <strong>assets</strong> operations are deprecated in 2.0. Use the <strong>/videos</strong> endpoints instead.</blockquote> Operations related to assets, which are created through the `
  name: Wowza assets API
  slug: wowza-assets-api
- description: Operations related to categorizing videos.
  name: Wowza categories API
  slug: wowza-categories-api
- description: Operations related to clipping and stitching videos and live streams.
  name: Wowza clipping API
  slug: wowza-clipping-api
- description: Operations related to live streams. A live stream is a single, linear video broadcast. You broadcast a live stream by receiving encoded source video into the Wowza Video service and letting Wowza Vide
  name: Wowza live_streams API
  slug: wowza-live-streams-api
- description: The Machine Stats API from Wowza — 2 operation(s) for machine stats.
  name: Wowza Machine Stats API
  slug: wowza-machine-stats-api
- description: <blockquote>The <strong>player</strong> operations are deprecated in 2.0. Create and update player configurations in the user interface. Any values you send using the <strong>player</strong> operation
  name: Wowza players API
  slug: wowza-players-api
- description: Operations related to quality of experience metrics.
  name: Wowza quality_of_experience API
  slug: wowza-quality-of-experience-api
- description: Operations related to Real-Time Streaming at Scale. If your audience is fewer than 300 viewers or you want to deliver a stream in near real time alongside other delivery protocols, <a href="https://ww
  name: Wowza real_time API
  slug: wowza-real-time-api
- description: <blockquote>The <strong>recordings</strong> operations are deprecated in 2.0. Use the <strong>/videos</strong> endpoints instead.</blockquote> Operations related to recordings, which are created throu
  name: Wowza recordings API
  slug: wowza-recordings-api
- description: The REST information API from Wowza — 1 operation(s) for rest information.
  name: Wowza REST information API
  slug: wowza-rest-information-api
- description: Operations related to schedules. Schedules allow you to automatically start or stop a live stream or transcoder at a predetermined date and time. You can configure a schedule to start and/or stop a li
  name: Wowza schedules API
  slug: wowza-schedules-api
- description: The Server Licenses API from Wowza — 1 operation(s) for server licenses.
  name: Wowza Server Licenses API
  slug: wowza-server-licenses-api
- description: The Server Listeners API from Wowza — 1 operation(s) for server listeners.
  name: Wowza Server Listeners API
  slug: wowza-server-listeners-api
- description: The Server log4j system API from Wowza — 3 operation(s) for server log4j system.
  name: Wowza Server log4j system API
  slug: wowza-server-log4j-system-api
- description: The Server MediaCache API from Wowza — 8 operation(s) for server mediacache.
  name: Wowza Server MediaCache API
  slug: wowza-server-mediacache-api
- description: The Server MediaCache Version 3 API from Wowza — 6 operation(s) for server mediacache version 3.
  name: Wowza Server MediaCache Version 3 API
  slug: wowza-server-mediacache-version-3-api
- description: The Server MediaCasters API from Wowza — 2 operation(s) for server mediacasters.
  name: Wowza Server MediaCasters API
  slug: wowza-server-mediacasters-api
- description: The Server Monitoring API from Wowza — 2 operation(s) for server monitoring.
  name: Wowza Server Monitoring API
  slug: wowza-server-monitoring-api
- description: The Server Publishers API from Wowza — 2 operation(s) for server publishers.
  name: Wowza Server Publishers API
  slug: wowza-server-publishers-api
- description: The Server Publishers Version 3 API from Wowza — 2 operation(s) for server publishers version 3.
  name: Wowza Server Publishers Version 3 API
  slug: wowza-server-publishers-version-3-api
- description: The Server Status API from Wowza — 1 operation(s) for server status.
  name: Wowza Server Status API
  slug: wowza-server-status-api
- description: The Server Transcoder API from Wowza — 1 operation(s) for server transcoder.
  name: Wowza Server Transcoder API
  slug: wowza-server-transcoder-api
- description: The Server Tuning API from Wowza — 1 operation(s) for server tuning.
  name: Wowza Server Tuning API
  slug: wowza-server-tuning-api
- description: The Server Users API from Wowza — 2 operation(s) for server users.
  name: Wowza Server Users API
  slug: wowza-server-users-api
- description: The Servers Configuration API from Wowza — 12 operation(s) for servers configuration.
  name: Wowza Servers Configuration API
  slug: wowza-servers-configuration-api
- description: <blockquote>The <strong>storage</strong> operations are deprecated in 2.0. Operations related to peak and current storage for an account.
  name: Wowza storage API
  slug: wowza-storage-api
- description: 'Operations related to stream sources. You can create a Wowza stream source and associate it to a live stream or transcoder. ### Wowza Stream Sources When you set up a Wowza stream source with a live s'
  name: Wowza stream_sources API
  slug: wowza-stream-sources-api
- description: 'Operations related to stream targets. A stream target is a destination for a stream. Stream targets can be Wowza Video edge resources; custom, external destinations, target destinations. ### Wowza CDN'
  name: Wowza stream_targets API
  slug: wowza-stream-targets-api
- description: 'Operations related to transcoders, output renditions, and output stream targets. ### Transcoders Wowza Video transcoders allow you to customize transcoding processes by creating transcoders that are o'
  name: Wowza transcoders API
  slug: wowza-transcoders-api
- description: Operations related to stream analytics for an account.
  name: Wowza usage_account API
  slug: wowza-usage-account-api
- description: Operations related to stream target analytics, including CDN usage and viewer data.
  name: Wowza usage API
  slug: wowza-usage-api
- description: Operations related to real-time streams analytics.
  name: Wowza usage_real_time_streams API
  slug: wowza-usage-real-time-streams-api
- description: Operations related to transcoder analytics.
  name: Wowza usage_transcoders API
  slug: wowza-usage-transcoders-api
- description: <blockquote>The <strong>VOD stream</strong> operations are deprecated in 2.0. Operations related to video on demand (VOD) stream analytics.
  name: Wowza usage_vod_streams API
  slug: wowza-usage-vod-streams-api
- description: Operations related to uploading and categorizing videos.
  name: Wowza videos API
  slug: wowza-videos-api
- description: The Virtual Hosts API from Wowza — 42 operation(s) for virtual hosts.
  name: Wowza Virtual Hosts API
  slug: wowza-virtual-hosts-api
- description: <blockquote>The <strong>VOD stream</strong> operations are deprecated in 2.0. Use the <strong>/videos</strong> endpoints instead.</blockquote> Operations related to video on demand (VOD) streams, whic
  name: Wowza vod_streams API
  slug: wowza-vod-streams-api
- description: The Webhooks API from Wowza — 6 operation(s) for webhooks.
  name: Wowza Webhooks API
  slug: wowza-webhooks-api
artifact_total: 141
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication API
  slug: open-wowza-advanced-token-authentication-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication analytics_engagement API
  slug: open-wowza-analytics-engagement-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication analytics_ingest API
  slug: open-wowza-analytics-ingest-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication analytics_popularity API
  slug: open-wowza-analytics-popularity-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication analytics_viewers API
  slug: open-wowza-analytics-viewers-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Applications API
  slug: open-wowza-applications-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication assets API
  slug: open-wowza-assets-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication categories API
  slug: open-wowza-categories-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication clipping API
  slug: open-wowza-clipping-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication live_streams API
  slug: open-wowza-live-streams-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Machine Stats API
  slug: open-wowza-machine-stats-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication players API
  slug: open-wowza-players-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication quality_of_experience API
  slug: open-wowza-quality-of-experience-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication real_time API
  slug: open-wowza-real-time-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication recordings API
  slug: open-wowza-recordings-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication REST information API
  slug: open-wowza-rest-information-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication schedules API
  slug: open-wowza-schedules-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Licenses API
  slug: open-wowza-server-licenses-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Listeners API
  slug: open-wowza-server-listeners-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server log4j system API
  slug: open-wowza-server-log4j-system-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server MediaCache API
  slug: open-wowza-server-mediacache-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server MediaCache Version 3 API
  slug: open-wowza-server-mediacache-version-3-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server MediaCasters API
  slug: open-wowza-server-mediacasters-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Monitoring API
  slug: open-wowza-server-monitoring-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Publishers API
  slug: open-wowza-server-publishers-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Publishers Version 3 API
  slug: open-wowza-server-publishers-version-3-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Status API
  slug: open-wowza-server-status-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Transcoder API
  slug: open-wowza-server-transcoder-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Tuning API
  slug: open-wowza-server-tuning-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Server Users API
  slug: open-wowza-server-users-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Servers Configuration API
  slug: open-wowza-servers-configuration-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication storage API
  slug: open-wowza-storage-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication stream_sources API
  slug: open-wowza-stream-sources-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication stream_targets API
  slug: open-wowza-stream-targets-api
- collection_type: open
  name: Wowza Streaming Engine REST API
  slug: open-wowza-streaming-engine
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication transcoders API
  slug: open-wowza-transcoders-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication usage_account API
  slug: open-wowza-usage-account-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication usage API
  slug: open-wowza-usage-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication usage_real_time_streams API
  slug: open-wowza-usage-real-time-streams-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication usage_transcoders API
  slug: open-wowza-usage-transcoders-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication usage_vod_streams API
  slug: open-wowza-usage-vod-streams-api
- collection_type: open
  name: Wowza Video REST API Reference Documentation
  slug: open-wowza-video
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication videos API
  slug: open-wowza-videos-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Virtual Hosts API
  slug: open-wowza-virtual-hosts-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication vod_streams API
  slug: open-wowza-vod-streams-api
- collection_type: open
  name: Wowza Streaming Engine REST advanced_token_authentication Webhooks API
  slug: open-wowza-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wowza-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wowza-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wowza-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wowza-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.wowza.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wowza.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wowza.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.wowza.com/docs/wowza-developer-apis-and-sdks
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wowza.com/docs/wowza-video/api/video/openapi
- group: start
  title: ''
  type: Signup
  url: https://www.wowza.com/free-trial
- group: start
  title: ''
  type: Console
  url: https://cloud.wowza.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wowza.com/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wowza.com/pricing/video
- group: commercial
  title: ''
  type: Pricing
  url: https://store.wowza.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wowza.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wowza.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wowza.com
- group: operate
  title: ''
  type: Support
  url: https://support.wowza.com/hc
- group: operate
  title: ''
  type: Forums
  url: https://www.wowza.com/community/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.wowza.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.wowza.com/docs/wowza-video-release-notes
- group: company
  title: ''
  type: About
  url: https://www.wowza.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WowzaMediaSystems
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WowzaMediaSystems/wowza-video-api-demos-postman
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WowzaMediaSystems/wse-rest-library-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WowzaMediaSystems/wsc-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WowzaMediaSystems/wsc-sdk-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WowzaMediaSystems/wsc-api-examples-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WowzaMediaSystems/wowza-streaming-engine-mcp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WowzaMediaSystems/wowza-video-intelligence-framework
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WowzaMediaSystems/dev-guides
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wowza-media-systems
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/wowzamedia
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/WowzaMediaSystems
created: '2026-05-25'
description: Wowza is a Denver, Colorado-based video streaming infrastructure provider that has been simplifying live and on-demand streaming since 2007. The platform spans three flagship products — Wowza Streaming Engine (a self-hosted, on-prem/cloud/edge media server supporting RTMP, RTSP, SRT, WebRTC, HLS, and MPEG-DASH), Wowza Video (a fully managed, cloud-based streaming platform with a v2.0 REST API for live streams, transcoders, stream sources, stream targets, schedules, real-time streams, videos, categories, viewer analytics, ingest data, engagement, popularity, and quality-of-experience monitoring), and Wowza Flowplayer (a commercial-grade HTML5 video player with iOS, tvOS, and Android SDKs, DRM, ad insertion, and 30+ modular plugins). Wowza powers over 200,000 streaming instances across 140 countries, serving security and surveillance, law enforcement, government and defense, sports and live events, smart cities, industrial monitoring, healthcare, and OTT customers. Developer surface
  includes a public OpenAPI 3.0 specification for Wowza Video, a Swagger-derived OpenAPI 3.0 specification for Wowza Streaming Engine's REST API (default base http://localhost:8087), a Java API for extending Streaming Engine via plugins, a Wowza IDE, Postman collections, and a large public WowzaMediaSystems GitHub organization of plugins, modules, sample apps, and language SDKs.
features:
- description: Wowza Streaming Engine runs on prem, in the cloud, hybrid, or at the edge with full operator control.
  name: Self-Hosted Media Server
- description: Wowza Video is a fully managed live and VOD streaming platform with REST API control.
  name: Managed Cloud Streaming
- description: RTMP, RTSP, SRT, WebRTC, HLS, MPEG-DASH ingest and delivery across both Engine and Video products.
  name: Broad Protocol Support
- description: WebRTC-based Wowza Real-Time Streaming delivers sub-second latency at scale.
  name: Sub-Second Real-Time Streaming
- description: GPU-accelerated transcoding for ABR ladders, format conversion, and packaging into HLS and MPEG-DASH.
  name: Live and On-Demand Transcoding
- description: Restream to YouTube, Facebook, Twitch, Akamai, AWS Elemental MediaStore, custom CDNs, and SRT endpoints.
  name: Stream Targets and Push Publishing
- description: Commercial-grade HTML5 player with iOS, tvOS, and Android SDKs, DRM, ads, and 30+ plugins.
  name: Wowza Flowplayer HTML5 Player
- description: Live DVR window plus automatic live-to-VOD archiving for replays and clipping workflows.
  name: nDVR and Live-to-VOD
- description: First-class webhook events from both Wowza Streaming Engine and Wowza Video for stream lifecycle, transcoder, and analytics signals.
  name: Webhooks
- description: Wowza Video exposes ingest, engagement, popularity, viewer, and quality-of-experience analytics via REST.
  name: Viewer and QoE Analytics
- description: Streaming Engine Java API plus a Wowza IDE for building custom server listeners, application modules, HTTP providers, and media reader/writer plugins.
  name: Java Plugin Framework
- description: Wowza ships official Postman collections, a public OpenAPI 3.0 spec for Wowza Video, and a Swagger-derived OpenAPI 3.0 spec for the Streaming Engine REST API.
  name: Postman and Swagger Tooling
- description: Open-source MCP server enabling AI agents to control Wowza Streaming Engine via the Model Context Protocol.
  name: Wowza Streaming Engine MCP
- description: Plugin framework for integrating AI/ML inference (ASR, captions, object detection, ONVIF) into the streaming pipeline.
  name: Video Intelligence Framework
image: https://www.wowza.com/wp-content/themes/wowza/assets/img/wowza-favicon.svg
integrations:
- description: Push Publishing profiles, signed token validation, and HLS Akamai targets are first-class.
  name: Akamai
- description: Streaming Engine S3 upload plugin and AWS-region Wowza Video deployments.
  name: AWS S3
- description: Standard CDN target for Wowza Video and Streaming Engine output.
  name: Amazon CloudFront
- description: Native restreaming/push-publishing target.
  name: YouTube Live
- description: Native restreaming/push-publishing target.
  name: Facebook Live
- description: Native restreaming/push-publishing target.
  name: Twitch
- description: Official Postman collections for both Wowza Video and Streaming Engine REST APIs.
  name: Postman
- description: Official OpenAPI 3.0 specs published for Wowza Video and Wowza Streaming Engine.
  name: Swagger / OpenAPI
- description: First-class SRT ingest and egress support for low-latency contribution.
  name: SRT Alliance
- description: WSE plugin for ingesting ONVIF IP camera streams in surveillance deployments.
  name: ONVIF
- description: WSE caption handler plugins that generate captions via Azure Speech Services or OpenAI Whisper.
  name: Azure Speech and OpenAI Whisper
- description: Official Wowza Streaming Engine MCP server lets AI agents drive Engine via MCP.
  name: Model Context Protocol (MCP)
- description: WSE analytics plugin reports streaming statistics into Google Analytics.
  name: Google Analytics
layout: provider
modified: '2026-05-25'
name: Wowza
nav: Providers
network: true
overview: 'Wowza publishes 44 APIs on the [APIs.io](https://apis.io/) network, including advanced_token_authentication API, analytics_engagement API, analytics_ingest API, and 41 more. Tagged areas include Video, Streaming, Live Streaming, Video-on-Demand, and Transcoding.


  Wowza''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, developer console, pricing, and 27 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 56.3
    developer_ergonomics: 81.0
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 58.1
      derived: 0
      marker_coverage: 0.0
      total: 44
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wowza/refs/heads/main/screenshots/wowza-2026-06-20T201630.png
security:
- kind: authentication
  name: Wowza Authentication
  slug: wowza-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Wowza Domain Security
  slug: wowza-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wowza
solutions:
- description: Self-hosted media server licensed monthly, annually, or as a one-time perpetual purchase for on-prem, cloud, hybrid, and edge deployment.
  name: Wowza Streaming Engine
- description: Fully managed cloud streaming platform with REST API, hosted Flowplayer, transcoders, stream targets, real-time streaming, and analytics.
  name: Wowza Video
- description: Combined Wowza Streaming Engine and Wowza Video deployment for flexible hybrid topologies.
  name: Wowza Hybrid Cloud
- description: Standalone HTML5 video player with SDKs, DRM, ads, and plugins — bundled with Wowza Video or sold separately.
  name: Wowza Flowplayer
- description: WebRTC-based sub-second latency live streaming service for interactive applications.
  name: Wowza Real-Time Streaming
- description: Custom deployment, integration, and Wowza Streaming Engine plugin development engagements.
  name: Professional Services
tags:
- Video
- Streaming
- Live Streaming
- Video-on-Demand
- Transcoding
- Media Server
- RTMP
- RTSP
- SRT
- WebRTC
- HLS
- MPEG-DASH
- Real-Time Streaming
- Low Latency
- Video Player
- HTML5 Player
- DRM
- CDN
- Video Analytics
- QoE
- Webhook
- Edge
- Surveillance
- OTT
use_cases:
- description: 24/7 live monitoring for security operations, law enforcement, and physical security with RTSP ingest.
  name: Security and Video Surveillance
- description: Mission-critical streaming for defense, intelligence, and government agencies — including tactical and ISR workflows.
  name: Government and Defense
- description: Low-latency live event production and distribution, including auction, betting, and interactive sports use cases.
  name: Sports and Live Events
- description: VOD and live OTT services with ABR delivery, DRM, and analytics.
  name: OTT Streaming
- description: Edge-deployed media servers for traffic, infrastructure, and industrial IoT camera feeds.
  name: Smart Cities and Industrial Monitoring
- description: Secure live and recorded video for telemedicine, surgical observation, and medical education.
  name: Healthcare and Telemedicine
- description: WebRTC-powered sub-second video for auctions, gaming, fitness, and two-way interactive experiences.
  name: Interactive and Real-Time Apps
- description: SRT contribution feeds, contribution-to-CDN workflows, and live-to-VOD archiving for broadcasters.
  name: Broadcasting and Media
- description: Live lectures, recorded course content, and interactive classroom video.
  name: Education and E-Learning
- description: Multi-platform restreaming and on-prem capture for religious organizations.
  name: Houses of Worship
website: https://www.wowza.com
---
