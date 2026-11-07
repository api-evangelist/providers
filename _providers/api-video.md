---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Api Video Agentic Access
  operation_count: 13
  slug: api-video-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 1
apis:
- description: The api.video Live Streaming API enables low-latency live video broadcasts with RTMP ingest, automatic recording, and global CDN delivery for audiences worldwide.
  name: api.video Live Streaming API
  slug: live-streaming
- description: The api.video Analytics API provides viewer engagement metrics, playback statistics, and performance data for both video on demand and live streaming content.
  name: api.video Analytics API
  slug: analytics
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Videos API from API.Video — 8 operation(s) for videos.
  name: API.Video Videos API
  slug: api-video-videos-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Advanced authentication API from API.Video — 2 operation(s) for advanced authentication.
  name: API.Video Advanced authentication API
  slug: api-video-advanced-authentication-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Analytics API from API.Video — 3 operation(s) for analytics.
  name: API.Video Analytics API
  slug: api-video-analytics-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Captions API from API.Video — 2 operation(s) for captions.
  name: API.Video Captions API
  slug: api-video-captions-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Chapters API from API.Video — 2 operation(s) for chapters.
  name: API.Video Chapters API
  slug: api-video-chapters-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Live Streams API from API.Video — 4 operation(s) for live streams.
  name: API.Video Live Streams API
  slug: api-video-live-streams-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Player Themes API from API.Video — 3 operation(s) for player themes.
  name: API.Video Player Themes API
  slug: api-video-player-themes-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Summaries API from API.Video — 3 operation(s) for summaries.
  name: API.Video Summaries API
  slug: api-video-summaries-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Tags API from API.Video — 1 operation(s) for tags.
  name: API.Video Tags API
  slug: api-video-tags-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Upload Tokens API from API.Video — 2 operation(s) for upload tokens.
  name: API.Video Upload Tokens API
  slug: api-video-upload-tokens-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Watermarks API from API.Video — 2 operation(s) for watermarks.
  name: API.Video Watermarks API
  slug: api-video-watermarks-api
- baseURL: https://ws.api.video
  baseurl_source: declared
  description: The Webhooks API from API.Video — 2 operation(s) for webhooks.
  name: API.Video Webhooks API
  slug: api-video-webhooks-api
artifact_total: 89
asyncapis:
- description: ''
  name: Api Video Webhooks
  slug: api-video-webhooks
collections:
- collection_type: open
  name: api.video Videos API
  slug: open-api-video-videos-api
- collection_type: open
  name: api.video API
  slug: open-api-video
common:
- group: design
  href: https://artifacts.apis.io/api-video/rules/api-video-rules.yml
  title: ''
  type: Spectral
  url: rules/api-video-rules.yml
- group: design
  href: https://artifacts.apis.io/api-video/json-ld/api-video-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/api-video-context.jsonld
- group: design
  href: https://artifacts.apis.io/api-video/vocabulary/api-video-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/api-video-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/api-video/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/api-video/asyncapi/api-video-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/api-video-webhooks.yml
- group: design
  href: https://artifacts.apis.io/api-video/data-model/api-video-data-model.yml
  title: ''
  type: DataModel
  url: data-model/api-video-data-model.yml
- group: design
  href: https://artifacts.apis.io/api-video/components/api-video-components.yml
  title: ''
  type: Components
  url: components/api-video-components.yml
- group: operate
  href: https://artifacts.apis.io/api-video/changelog/api-video-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/api-video-changelog.yml
- group: design
  href: https://artifacts.apis.io/api-video/conventions/api-video-conventions.yml
  title: ''
  type: Conventions
  url: conventions/api-video-conventions.yml
- group: start
  href: https://artifacts.apis.io/api-video/sandbox/api-video-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/api-video-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/api-video/lifecycle/api-video-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/api-video-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/api-video/lifecycle/api-video-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/api-video-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/api-video/errors/api-video-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/api-video-problem-types.yml
- group: design
  href: https://artifacts.apis.io/api-video/conformance/api-video-conformance.yml
  title: ''
  type: Conformance
  url: conformance/api-video-conformance.yml
- group: auth
  href: https://artifacts.apis.io/api-video/well-known/api-video-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/api-video-status-security.txt
- group: agent
  href: https://artifacts.apis.io/api-video/well-known/api-video-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/api-video-well-known.yml
- group: other
  href: https://artifacts.apis.io/api-video/hosts/api-video-hosts.yml
  title: ''
  type: Hosts
  url: hosts/api-video-hosts.yml
- group: build
  href: https://artifacts.apis.io/api-video/integrations/api-video-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/api-video-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/api-video/vendors/api-video-vendors.yml
  title: ''
  type: Vendors
  url: vendors/api-video-vendors.yml
- group: build
  href: https://artifacts.apis.io/api-video/packages/api-video-packages.yml
  title: ''
  type: SDKs
  url: packages/api-video-packages.yml
- group: build
  href: https://artifacts.apis.io/api-video/packages/api-video-packages.yml
  title: ''
  type: Packages
  url: packages/api-video-packages.yml
- group: auth
  href: https://artifacts.apis.io/api-video/authentication/api-video-authentication.yml
  title: ''
  type: Authentication
  url: authentication/api-video-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/api-video/plans/api-video-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/api-video-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/api-video/rate-limits/api-video-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/api-video-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/api-video/finops/api-video-finops.yml
  title: ''
  type: FinOps
  url: finops/api-video-finops.yml
- group: other
  href: https://artifacts.apis.io/api-video/capabilities/api-video-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/api-video-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/api-video/agentic-access/api-video-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/api-video-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/api-video/security/api-video-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/api-video-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/api-video
- group: company
  title: ''
  type: Website
  url: https://api.video/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.video/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.video/get-started/start-building
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.video
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ApiVideo
- group: commercial
  title: ''
  type: Pricing
  url: https://api.video/pricing
- group: company
  title: ''
  type: Blog
  url: https://api.video/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.video/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.video/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.video/changelog/
- group: operate
  title: ''
  type: Support
  url: https://chat.api.video/hc/help-center
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.api.video/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.api.video/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.video/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.video/privacy-policy/
- group: design
  title: ''
  type: Webhooks
  url: https://docs.api.video/reference/create-and-manage-webhooks
created: '2025-03-01'
description: api.video is a video infrastructure platform - part of OVHcloud (its terms are contracted with OVHcloud OCT1, Roubaix, France) - offering a REST API at ws.api.video for video on demand, live streaming (RTMPS/SRT ingest, restreaming, DVR), a hosted player and player SDKs, viewer analytics, webhooks, and AI transcription and summarization. It publishes an OpenAPI 3.0 document (59 operations), eight generated API clients (Node, Python, PHP, Go, C#, Java, Swift, Android), uploader, recorder and live-stream SDKs for web and mobile, a free sandbox environment, and WordPress, Contentful, Strapi, Bubble and Zapier plugins. Encoding is free; hosting and delivery are billed per minute of video.
features:
- description: Video encoding with 0.02s playback speed using global infrastructure.
  name: Lightning-Fast Video Encoding
- description: Enterprise-grade reliability with 99.999% uptime guarantee backed by SLA.
  name: 99.999% Uptime SLA
- description: Global CDN with 140+ PoPs and 1 Petabyte monthly traffic capacity for worldwide delivery.
  name: 140+ Global Points of Presence
- description: Automatic video transcription powered by AI for searchable captions and accessibility.
  name: AI Transcription
- description: AI-generated video summaries to help viewers navigate long-form content.
  name: AI Video Summarization
- description: Official SDKs for iOS, Android, Flutter, Java, Python, Node.js, PHP, C#, React Native, and more.
  name: 20+ SDKs
- description: Flexible usage-based pricing with volume discounts scaling with consumption.
  name: Usage-Based Pricing
- description: Reliable large file uploads with resumable upload support for videos of any size.
  name: Resumable Uploads
finops:
- has_sources: false
  method: generated
  name: Api Video Finops
  primary_unit: request
  service_category: API
  slug: api-video-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-video.png
integrations:
- description: WordPress plugin for embedding and managing api.video content in WordPress sites.
  name: WordPress
- description: Integration with Contentful CMS for video asset management in headless content workflows.
  name: Contentful
- description: No-code integration with Bubble for adding video capabilities to Bubble applications.
  name: Bubble
json_schemas:
- name: AccessToken
  property_count: 4
  slug: api-video-access-token
- name: Analytics response for aggregated metrics
  property_count: 2
  slug: api-video-analytics-aggregated-metrics-response
- name: Analytics response for metrics breakdown by dimension
  property_count: 3
  slug: api-video-analytics-metrics-breakdown-response
- name: Analytics response for metrics over time
  property_count: 3
  slug: api-video-analytics-metrics-over-time-response
- name: ApiKey
  property_count: 1
  slug: api-video-authenticate-payload
- name: Caption
  property_count: 5
  slug: api-video-caption
- name: VideoCaptions
  property_count: 2
  slug: api-video-captions-list-response
- name: CaptionsUpdatePayload
  property_count: 1
  slug: api-video-captions-update-payload
- name: CaptionsUploadPayload
  property_count: 1
  slug: api-video-captions-upload-payload
- name: Chapter
  property_count: 3
  slug: api-video-chapter
- name: VideoChapters
  property_count: 2
  slug: api-video-chapters-list-response
- name: ChaptersUpdatePayload
  property_count: 1
  slug: api-video-chapters-update-payload
- name: Tags
  property_count: 2
  slug: api-video-list-tags-response
- name: LiveStreamCreationPayload
  property_count: 4
  slug: api-video-live-stream-creation-payload
- name: LiveStreams
  property_count: 2
  slug: api-video-live-stream-list-response
- name: LiveStream
  property_count: 10
  slug: api-video-live-stream
- name: LiveStreamThumbnailUploadPayload
  property_count: 1
  slug: api-video-live-stream-thumbnail-upload-payload
- name: LiveStreamUpdatePayload
  property_count: 4
  slug: api-video-live-stream-update-payload
- name: PlayerThemeCreationPayload
  property_count: 16
  slug: api-video-player-theme-creation-payload
- name: PlayerTheme
  property_count: 20
  slug: api-video-player-theme
- name: PlayerThemeUpdatePayload
  property_count: 16
  slug: api-video-player-theme-update-payload
- name: PlayerThemeUploadLogoPayload
  property_count: 2
  slug: api-video-player-theme-upload-logo-payload
- name: PlayerThemes
  property_count: 2
  slug: api-video-player-themes-list-response
- name: RefreshToken
  property_count: 1
  slug: api-video-refresh-token-payload
- name: Summaries
  property_count: 2
  slug: api-video-summaries-list-response
- name: summary-creation-payload
  property_count: 3
  slug: api-video-summary-creation-payload
- name: summary
  property_count: 6
  slug: api-video-summary
- name: summary-source
  property_count: 2
  slug: api-video-summary-source
- name: summary-update-payload
  property_count: 2
  slug: api-video-summary-update-payload
- name: TokenCreationPayload
  property_count: 1
  slug: api-video-token-creation-payload
- name: UploadTokens
  property_count: 2
  slug: api-video-token-list-response
- name: tokenUploadPayload
  property_count: 2
  slug: api-video-token-upload-payload
- name: UploadToken
  property_count: 4
  slug: api-video-upload-token
- name: VideoCreationPayload
  property_count: 15
  slug: api-video-video-creation-payload
- name: Video
  property_count: 19
  slug: api-video-video
- name: VideoStatus
  property_count: 2
  slug: api-video-video-status
- name: ThumbnailPickPayload
  property_count: 1
  slug: api-video-video-thumbnail-pick-payload
- name: VideoUpdatePayload
  property_count: 12
  slug: api-video-video-update-payload
- name: Watermark
  property_count: 2
  slug: api-video-watermark
- name: WatermarkUploadPayload
  property_count: 1
  slug: api-video-watermark-upload-payload
- name: Watermarks
  property_count: 2
  slug: api-video-watermarks-list-response
- name: Webhook
  property_count: 5
  slug: api-video-webhook
- name: WebhooksCreationPayload
  property_count: 2
  slug: api-video-webhooks-creation-payload
- name: Webhooks
  property_count: 2
  slug: api-video-webhooks-list-response
jsonld:
- class_count: 69
  name: Api Video Context
  property_count: 113
  slug: api-video-context
layout: provider
modified: '2026-11-05'
name: API.Video
nav: Providers
network: true
overview: 'API.Video publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Videos API, Advanced authentication API, Analytics API, and 11 more. Tagged areas include Artificial Intelligence, Analytics, CDN, Encoding, and Live Streaming.


  The API.Video catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  API.Video''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, pricing, engineering blog, and 38 more developer resources.'
plans:
- name: Api Video Plans Pricing
  plan_count: 2
  slug: api-video-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Api Video Rate Limits
  slug: api-video-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: API.Video API Rules
  rule_count: 63
  severity_counts:
    error: 42
    hint: 0
    info: 7
    warn: 14
  slug: api-video-rules
score:
  band: exemplar
  composite: 69.3
  coverage:
    artifact_dirs: 36
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 38.8
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 79.2
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 92.1
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 84.6
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/api-video/api-video-2026-06-20T172221.png
security:
- kind: authentication
  name: Api Video Authentication
  slug: api-video-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Api Video Domain Security
  slug: api-video-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: api-video-delegated-upload-token
  slug: api-video-delegated-upload-token
- name: api-video-run-a-live-stream
  slug: api-video-run-a-live-stream
- name: api-video-subscribe-and-verify-webhooks
  slug: api-video-subscribe-and-verify-webhooks
- name: api-video-upload-and-publish-video
  slug: api-video-upload-and-publish-video
slug: api-video
tags:
- Artificial Intelligence
- Analytics
- CDN
- Encoding
- Live Streaming
- Transcription
- Video
- Video-on-Demand
use_cases:
- description: Host and deliver training videos with analytics to track learner engagement and completion.
  name: Online Learning and Corporate Training
- description: Build TikTok-style or short-form video applications with fast encoding and global delivery.
  name: Short-Form Video Platforms
- description: Add product videos and live shopping streams to e-commerce and marketplace applications.
  name: E-Commerce Video
- description: Integrate video messaging and user-generated content into communication platforms.
  name: Communication Tools
- description: Host and stream AI-generated video content at scale with reliable infrastructure.
  name: Generative AI Video Hosting
website: https://api.video/
---
