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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Api Video Agentic Access
  operation_count: 13
  slug: api-video-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 3
apis:
- description: The api.video Live Streaming API enables low-latency live video broadcasts with RTMP ingest, automatic recording, and global CDN delivery for audiences worldwide.
  name: api.video Live Streaming API
  slug: live-streaming
- description: The api.video Analytics API provides viewer engagement metrics, playback statistics, and performance data for both video on demand and live streaming content.
  name: api.video Analytics API
  slug: analytics
- description: The Videos API from API.Video — 8 operation(s) for videos.
  name: API.Video Videos API
  slug: api-video-videos-api
artifact_total: 25
collections:
- collection_type: open
  name: api.video API
  slug: open-api-video
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/api-video-agentic-access.yml
- group: auth
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
- name: Api Video Finops
  service_category: API
  slug: api-video-finops
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
overview: 'API.Video publishes 1 API on the [APIs.io](https://apis.io/) network: Videos API. Tagged areas include AI, Analytics, CDN, Encoding, and Live Streaming.


  API.Video''s developer surface includes documentation, getting-started guide, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Api Video Plans Pricing
  plan_count: 3
  slug: api-video-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Api Video Rate Limits
  slug: api-video-rate-limits
score:
  band: thin
  composite: 38.7
  delta: -1.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 44.1
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-video/refs/heads/main/screenshots/api-video-2026-06-20T172221.png
security:
- kind: domain-security
  name: Api Video Domain Security
  slug: api-video-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: api-video
tags:
- AI
- Analytics
- CDN
- Encoding
- Live Streaming
- Transcription
- Video
- Video on Demand
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
