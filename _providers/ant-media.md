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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 40
  human_in_the_loop: 6
  name: Ant Media Agentic Access
  operation_count: 72
  slug: ant-media-agentic-access
  summary_line: 72 operations · 40 acting · 6 human-in-the-loop
api_count: 6
apis:
- description: The Ant Media Server REST API provides programmatic access to all streaming server management functions including stream management, broadcast configuration, recording control, token authentication, c
  name: Ant Media Server REST API
  slug: ant-media-server-rest-api
- description: The Broadcasts API from Ant Media — 45 operation(s) for broadcasts.
  name: Ant Media Broadcasts API
  slug: ant-media-broadcasts-api
- description: The Filters API from Ant Media — 7 operation(s) for filters.
  name: Ant Media Filters API
  slug: ant-media-filters-api
- description: The Push Notification API from Ant Media — 3 operation(s) for push notification.
  name: Ant Media Push Notification API
  slug: ant-media-push-notification-api
- description: The Version API from Ant Media — 1 operation(s) for version.
  name: Ant Media Version API
  slug: ant-media-version-api
- description: The Vods API from Ant Media — 8 operation(s) for vods.
  name: Ant Media Vods API
  slug: ant-media-vods-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ant Media Server REST API Reference Broadcasts API
  slug: open-ant-media-broadcasts-api
- collection_type: open
  name: Ant Media Server REST API Reference Broadcasts Filters API
  slug: open-ant-media-filters-api
- collection_type: open
  name: Ant Media Server REST API Reference Broadcasts Push Notification API
  slug: open-ant-media-push-notification-api
- collection_type: open
  name: Ant Media Server REST API Reference Broadcasts Version API
  slug: open-ant-media-version-api
- collection_type: open
  name: Ant Media Server REST API Reference Broadcasts Vods API
  slug: open-ant-media-vods-api
- collection_type: open
  name: Ant Media Server REST API Reference
  slug: open-ant-media
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ant-media/Ant-Media-Server/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ant-media/Ant-Media-Server/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ant-media-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ant-media-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antmedia
- group: start
  title: ''
  type: Portal
  url: https://antmedia.io
- group: docs
  title: ''
  type: Documentation
  url: https://antmedia.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://antmedia.io/docs/guides/getting-started/quick-start/
- group: commercial
  title: ''
  type: Pricing
  url: https://antmedia.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://antmedia.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ant-media
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ant-media/Ant-Media-Server
- group: operate
  title: ''
  type: Support
  url: https://antmedia.io/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antmedia.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antmedia.io/privacy-policy/
- group: docs
  title: Broadcast Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ant-media/refs/heads/main/json-schema/ant-media-broadcast-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ant-media/refs/heads/main/vocabulary/ant-media-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://antmedia.io/llms.txt
created: '2025-03-01'
description: Ant Media Server is a scalable, open-source media server for ultra-low latency live streaming and WebRTC-based video applications. It supports WebRTC, RTMP, RTSP, SRT, HLS, and CMAF protocols, enabling developers to build real-time video applications with sub-second latency. Available in Community (open-source) and Enterprise editions with adaptive bitrate streaming, cloud auto-scaling, video recording, and REST API management.
examples:
- key_count: 19
  name: Ant Media Broadcast Example
  slug: ant-media-broadcast-example
features:
- description: Achieve sub-500ms latency with WebRTC-based publish and play, enabling real-time interactive video applications like auctions, gaming, and telehealth.
  name: Ultra-Low Latency WebRTC Streaming
- description: Ingest and deliver streams via RTMP, RTSP, SRT, WebRTC, HLS, CMAF, and LL-HLS, supporting a wide range of encoders and players.
  name: Multi-Protocol Support
- description: Automatically transcode streams to multiple bitrate/resolution ladders and deliver the optimal quality based on viewer bandwidth.
  name: Adaptive Bitrate Streaming
- description: Record live streams to MP4 or HLS on local disk or cloud storage, creating video-on-demand assets from live broadcasts automatically.
  name: Video Recording and VoD
- description: Deploy Ant Media Server in horizontal cluster mode with auto-scaling on AWS, Azure, GCP, and Alibaba Cloud for high-concurrency events.
  name: Cluster and Auto-Scaling
- description: Full programmatic control of streams, broadcasts, conferences, and server settings via a comprehensive REST API.
  name: REST API Management
finops:
- name: Ant Media Finops
  service_category: API
  slug: ant-media-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ant-media.png
json_schemas:
- name: Broadcast
  property_count: 21
  slug: ant-media-broadcast
json_structures:
- name: Ant Media Broadcast Structure
  property_count: 21
  slug: ant-media-broadcast-structure
jsonld:
- class_count: 3
  name: Ant Media Context
  property_count: 14
  slug: ant-media-context
layout: provider
modified: '2026-04-19'
name: Ant Media
nav: Providers
network: true
overview: 'Ant Media publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Broadcasts API, Filters API, Push Notification API, and 2 more. Tagged areas include Broadcasting, Live Streaming, Media, Streaming, and Video.


  The Ant Media catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ant Media''s developer surface includes developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Ant Media Plans Pricing
  plan_count: 3
  slug: ant-media-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Ant Media Rate Limits
  slug: ant-media-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ant Media API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ant-media-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 25.0
    contract_quality: 44.6
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ant-media/refs/heads/main/screenshots/ant-media-2026-06-20T172022.png
security:
- kind: domain-security
  name: Ant Media Domain Security
  slug: ant-media-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ant-media
tags:
- Broadcasting
- Live Streaming
- Media
- Streaming
- Video
- WebRTC
use_cases:
- description: Enable HIPAA-compliant real-time video consultations between patients and healthcare providers with sub-second latency.
  name: Telehealth and Remote Consultations
- description: Power interactive live shopping experiences and real-time bidding platforms with low-latency video and chat.
  name: Live E-Commerce and Auctions
- description: Deliver interactive live lectures, webinars, and virtual classrooms with two-way video and screen sharing.
  name: E-Learning and Virtual Classrooms
- description: Broadcast gaming sessions and esports events with RTMP ingest from OBS and HLS/WebRTC delivery to viewers at scale.
  name: Gaming and Esports Broadcasting
- description: Ingest RTSP streams from IP cameras and provide browser-based WebRTC viewing with recording and motion detection.
  name: Video Surveillance
website: https://antmedia.io
---
