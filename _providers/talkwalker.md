---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Search and export a subset of documents from a Talkwalker project, including brand mentions and social data across supported channels. Results are metered at 1 credit per result plus a minimum of 10 c
  name: Talkwalker Search API
  slug: search-api
- description: Real-time streaming API (v3) for monitoring keyword-based streams and project or topic-level data feeds. Charged at 1 credit per streamed result with no per-call minimum.
  name: Talkwalker Streaming API
  slug: streaming-api
- description: Reproduce Talkwalker dashboard widgets programmatically by fetching histogram data. Charged at 10 credits per call.
  name: Talkwalker Histogram API
  slug: histogram-api
- description: Manage and retrieve project resources including topics, filters, pages, events, panels, and datasets. Also exposes tag and view (dashboard, report, alert) management endpoints. Free to call — no credi
  name: Talkwalker Resources API
  slug: resources-api
- description: Import custom documents and modify existing documents within Talkwalker projects. Supports custom metrics creation for imported content. Document imports are free — no credit cost.
  name: Talkwalker Document API
  slug: document-api
- description: Detect features and entities within images using Talkwalker's image detection capabilities, enabling logo detection and visual content analytics.
  name: Talkwalker Image API
  slug: image-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talkwalker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.talkwalker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.talkwalker.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/talkwalker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talkwalker
- group: company
  title: ''
  type: Blog
  url: https://www.talkwalker.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talkwalker.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/Talkwalker
- group: commercial
  title: ''
  type: Plans
  url: plans/talkwalker-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/talkwalker-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/talkwalker-finops.yml
created: '2026-06-13'
description: Talkwalker is a social media analytics and listening platform that provides REST APIs for tracking brand mentions, analyzing sentiment, measuring campaign performance, and monitoring competitors across 150 million websites and 10+ social networks. The API suite covers search, streaming, histograms, document management, image detection, topic management, and custom metrics.
finops:
- name: Talkwalker Finops
  service_category: ''
  slug: talkwalker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talkwalker.png
layout: provider
modified: '2026-06-13'
name: Talkwalker
nav: Providers
network: true
overview: 'Talkwalker publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media Analytics, Social Listening, Brand Monitoring, Sentiment Analysis, and Media Monitoring.


  Talkwalker''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Talkwalker Plans Pricing
  plan_count: 3
  slug: talkwalker-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 9
  name: Talkwalker Rate Limits
  slug: talkwalker-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: -2.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 27.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/talkwalker/refs/heads/main/screenshots/talkwalker-2026-06-20T194908.png
security:
- kind: domain-security
  name: Talkwalker Domain Security
  slug: talkwalker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: talkwalker
tags:
- Social Media Analytics
- Social Listening
- Brand Monitoring
- Sentiment Analysis
- Media Monitoring
- Campaign Analytics
website: https://www.talkwalker.com/
---
