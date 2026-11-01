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
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-10-31'
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
  baseurl_source: spec
  description: The Videos API from API.Video — 8 operation(s) for videos.
  name: API.Video Videos API
  slug: api-video-videos-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Advanced authentication API from API.Video — 2 operation(s) for advanced authentication.
  name: API.Video Advanced authentication API
  slug: api-video-advanced-authentication-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Analytics API from API.Video — 3 operation(s) for analytics.
  name: API.Video Analytics API
  slug: api-video-analytics-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Captions API from API.Video — 2 operation(s) for captions.
  name: API.Video Captions API
  slug: api-video-captions-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Chapters API from API.Video — 2 operation(s) for chapters.
  name: API.Video Chapters API
  slug: api-video-chapters-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Live Streams API from API.Video — 4 operation(s) for live streams.
  name: API.Video Live Streams API
  slug: api-video-live-streams-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Player Themes API from API.Video — 3 operation(s) for player themes.
  name: API.Video Player Themes API
  slug: api-video-player-themes-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Summaries API from API.Video — 3 operation(s) for summaries.
  name: API.Video Summaries API
  slug: api-video-summaries-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Tags API from API.Video — 1 operation(s) for tags.
  name: API.Video Tags API
  slug: api-video-tags-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Upload Tokens API from API.Video — 2 operation(s) for upload tokens.
  name: API.Video Upload Tokens API
  slug: api-video-upload-tokens-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Watermarks API from API.Video — 2 operation(s) for watermarks.
  name: API.Video Watermarks API
  slug: api-video-watermarks-api
- baseURL: https://ws.api.video
  baseurl_source: spec
  description: The Webhooks API from API.Video — 2 operation(s) for webhooks.
  name: API.Video Webhooks API
  slug: api-video-webhooks-api
artifact_total: 37
collections:
- collection_type: open
  name: api.video Videos API
  slug: open-api-video-videos-api
- collection_type: open
  name: api.video API
  slug: open-api-video
common:
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
created: '2025-03-01'
description: api.video is a video infrastructure platform offering APIs for video on demand, live streaming, analytics, and AI-powered features including transcription and summarization. It provides lightning-fast encoding, 99.999% uptime, 140+ global points of presence, and SDKs in 20+ languages for integrating video into websites, apps, and software.
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
layout: provider
modified: '2026-05-19'
name: API.Video
nav: Providers
network: true
overview: 'API.Video publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Videos API, Advanced authentication API, Analytics API, and 11 more. Tagged areas include Artificial Intelligence, Analytics, CDN, Encoding, and Live Streaming.


  API.Video''s developer surface includes documentation, getting-started guide, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Api Video Plans Pricing
  plan_count: 3
  slug: api-video-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Api Video Rate Limits
  slug: api-video-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 51.3
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 28.9
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/api-video/api-video-2026-06-20T172221.png
security:
- kind: domain-security
  name: Api Video Domain Security
  slug: api-video-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
