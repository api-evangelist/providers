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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Gumlet Agentic Access
  operation_count: 18
  slug: gumlet-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 6
apis:
- description: Query video and image analytics and insights.
  name: Gumlet Analytics API
  slug: gumlet-analytics-api
- description: Connect cloud storage to Gumlet image optimization.
  name: Gumlet Image Sources API
  slug: gumlet-image-sources-api
- description: Create and manage live streaming assets.
  name: Gumlet Live Streaming API
  slug: gumlet-live-streaming-api
- description: Direct and multipart uploads of local media.
  name: Gumlet Uploads API
  slug: gumlet-uploads-api
- description: Ingest, encode, and manage video-on-demand assets.
  name: Gumlet Video Assets API
  slug: gumlet-video-assets-api
- description: Manage video collections (sources) and organization.
  name: Gumlet Video Collections API
  slug: gumlet-video-collections-api
artifact_total: 14
collections:
- collection_type: open
  name: Gumlet API
  slug: open-gumlet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gumlet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gumlet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gumlet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gumlet-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gumlet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gumlet
- group: company
  title: ''
  type: Website
  url: https://www.gumlet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gumlet.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/gumlet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gumlet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gumlet-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gumlet.com/blog/rss/
created: '2026-07-01'
description: Gumlet is a video hosting, streaming, and image optimization platform. Its video APIs cover on-demand and live streaming, per-title encoding, DRM, subtitles, and analytics, while its image APIs provide real-time resize, compression, and CDN delivery from cloud storage sources. All surfaces run under a single REST API at api.gumlet.com/v1 authenticated with a bearer API key.
finops:
- name: Gumlet Finops
  service_category: Media and Content Delivery
  slug: gumlet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gumlet.png
layout: provider
modified: '2026-07-01'
name: Gumlet
nav: Providers
network: true
overview: 'Gumlet publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Image Sources API, Live Streaming API, and 3 more. Tagged areas include Video, Streaming, Image Optimization, CDN, and Encoding.


  Gumlet''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Gumlet Plans Pricing
  plan_count: 6
  slug: gumlet-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Gumlet Rate Limits
  slug: gumlet-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Gumlet Authentication
  slug: gumlet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gumlet Domain Security
  slug: gumlet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gumlet Vulnerability Disclosure
  slug: gumlet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gumlet
tags:
- Video
- Streaming
- Image Optimization
- CDN
- Encoding
- Analytics
website: https://www.gumlet.com/
---
