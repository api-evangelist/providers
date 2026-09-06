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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 40
  human_in_the_loop: 6
  name: Ant Media Agentic Access
  operation_count: 72
  slug: ant-media-agentic-access
  summary_line: 72 operations · 40 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: The Ant Media Server REST API provides programmatic access to all streaming server management functions including stream management, broadcast configuration, recording control, token authentication, c
  name: Ant Media Server REST API
  slug: ant-media-server-rest-api
- baseURL: https://{ant-media-server}:5443/{application}/rest/v2/
  baseurl_source: declared
  description: The Broadcasts API from Ant Media — 45 operation(s) for broadcasts.
  name: Ant Media Broadcasts API
  slug: ant-media-broadcasts-api
- baseURL: https://{ant-media-server}:5443/{application}/rest/v2/
  baseurl_source: declared
  description: The Filters API from Ant Media — 7 operation(s) for filters.
  name: Ant Media Filters API
  slug: ant-media-filters-api
- baseURL: https://{ant-media-server}:5443/{application}/rest/v2/
  baseurl_source: declared
  description: The Push Notification API from Ant Media — 3 operation(s) for push notification.
  name: Ant Media Push Notification API
  slug: ant-media-push-notification-api
- baseURL: https://{ant-media-server}:5443/{application}/rest/v2/
  baseurl_source: declared
  description: The Version API from Ant Media — 1 operation(s) for version.
  name: Ant Media Version API
  slug: ant-media-version-api
- baseURL: https://{ant-media-server}:5443/{application}/rest/v2/
  baseurl_source: declared
  description: The Vods API from Ant Media — 8 operation(s) for vods.
  name: Ant Media Vods API
  slug: ant-media-vods-api
- baseURL: https://{ant-media-server}:5443/rest/v2/
  baseurl_source: declared
  description: 'The Ant Media Server Management Panel REST API — 50 operations for non-application-specific administration: creating and deleting applications, managing operator accounts, reading and writing server a'
  name: Ant Media Management API
  slug: ant-media-management-api
- baseURL: https://{ant-media-server}:5443/rest/v2/
  baseurl_source: declared
  description: The cluster surface of the Ant Media Server management panel REST API — 9 operations for listing cluster nodes with offset/size paging, counting them, annotating a node with a note, and removing a nod
  name: Ant Media Cluster API
  slug: ant-media-cluster-api
artifact_total: 38
asyncapis:
- description: ''
  name: Ant Media Webhooks
  slug: ant-media-webhooks
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
- group: company
  title: ''
  type: Website
  url: https://antmedia.io/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ant-media-capability-edges.yml
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
  url: https://docs.antmedia.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.antmedia.io/quick-start/
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
- group: build
  title: ''
  type: Packages
  url: packages/ant-media-packages.yml
- group: build
  title: First-party Ant Media SDK packages
  type: SDKs
  url: packages/ant-media-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ant-media-llms.txt
- group: agent
  title: Derived candidate tool surface — Ant Media publishes no MCP server
  type: X-MCPServerCandidate
  url: mcp/ant-media-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ant-media-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ant-media-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ant-media-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ant-media-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ant-media-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.antmedia.io/status/home
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ant-media-changelog.yml
- group: operate
  title: Product release notes
  type: ChangeLog
  url: https://github.com/ant-media/Ant-Media-Server/releases
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ant-media-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/ant-media-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ant-media-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ant-media-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ant-media-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ant-media-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://antmedia.io/rest/
- group: start
  title: ''
  type: SignUp
  url: https://antmedia.io/ant-media-free-trial/
- group: operate
  title: ''
  type: HelpCenter
  url: https://antmedia.io/frequently-asked-questions/
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
modified: '2026-09-02'
name: Ant Media
nav: Providers
network: true
overview: 'Ant Media publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Broadcasts API, Filters API, Push Notification API, and 4 more. Tagged areas include Broadcasting, Live Streaming, Media, Streaming, and Video.


  The Ant Media catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ant Media''s developer surface includes developer portal, documentation, getting-started guide, pricing, engineering blog, support, authentication, and 35 more developer resources.'
plans:
- name: Ant Media Plans Pricing
  plan_count: 8
  slug: ant-media-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
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
  band: strong
  composite: 60.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.3
    catalog_earned_first_party: 12.0
    catalog_gap: 46.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 29.5
    contract_quality: 49.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 29.5
    operational_transparency: 42.1
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ant-media/refs/heads/main/screenshots/ant-media-2026-06-20T172022.png
security:
- kind: authentication
  name: Ant Media Authentication
  slug: ant-media-authentication
  summary_line: 4 schemes
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
website: https://antmedia.io/
---
