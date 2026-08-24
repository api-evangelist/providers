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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
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
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gumlet Analytics API
  slug: open-gumlet-analytics-api
- collection_type: open
  name: Gumlet Analytics Image Sources API
  slug: open-gumlet-image-sources-api
- collection_type: open
  name: Gumlet Analytics Live Streaming API
  slug: open-gumlet-live-streaming-api
- collection_type: open
  name: Gumlet Analytics Uploads API
  slug: open-gumlet-uploads-api
- collection_type: open
  name: Gumlet Analytics Video Assets API
  slug: open-gumlet-video-assets-api
- collection_type: open
  name: Gumlet Analytics Video Collections API
  slug: open-gumlet-video-collections-api
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
random_paper: 3
rate_limits:
- limit_count: 3
  name: Gumlet Rate Limits
  slug: gumlet-rate-limits
score:
  band: developing
  composite: 39.4
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gumlet/refs/heads/main/screenshots/gumlet-2026-07-25T220430.png
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
