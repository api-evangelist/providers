---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: Read-write REST API for programmatically managing your JWP media library, players, playlists, live streams, advertising configurations, DRM policies, transformations, and webhooks. Authenticated via B
  name: JW Player Management API v2
  slug: jw-player-management-api-v2
- description: High-availability CDN-backed API for content embedding, playback metadata retrieval, poster images, streaming manifests, and server-side ad insertion (SSAI) configuration. Optimized for global scale w
  name: JW Player Delivery API
  slug: jw-player-delivery-api
- description: Client-side JavaScript API for controlling the JW Player embedded in web pages. Exposes methods and events for playback control, configuration, playlist management, advertising, and analytics integrat
  name: JW Player JavaScript Player API
  slug: jw-player-javascript-player-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/jwplayer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jwplayer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jwplayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jwplayer.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jwplayer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jwplayer
- group: company
  title: ''
  type: Blog
  url: https://jwx.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://jwx.com/video-management-delivery-pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jwplayer.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/jwdevelopers
- group: commercial
  title: ''
  type: Plans
  url: plans/jwplayer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jwplayer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jwplayer-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://jwx.com/blog/rss.xml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jwplayer-context.jsonld
created: '2026-06-12'
description: JW Player is a video player and streaming platform offering REST APIs for media management, playlist creation, player configuration, analytics, and live stream orchestration. The Management API v2 provides programmatic control over your media library, players, advertising, DRM, webhooks, and live broadcasts. The Delivery API enables high-availability content embedding, playback metadata, streaming manifests, and SSAI configuration via CDN.
finops:
- name: Jwplayer Finops
  service_category: ''
  slug: jwplayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jwplayer.png
jsonld:
- class_count: 67
  name: Jwplayer Context
  property_count: 14
  slug: jwplayer-context
layout: provider
modified: '2026-06-12'
name: JW Player
nav: Providers
network: true
overview: 'JW Player publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Streaming, Media Management, Live Streaming, and OTT.


  The JW Player catalog on APIs.io includes 1 JSON-LD context.


  JW Player''s developer surface includes documentation, GitHub presence, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Jwplayer Plans Pricing
  plan_count: 3
  slug: jwplayer-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Jwplayer Rate Limits
  slug: jwplayer-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 41.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 2.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 28.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jwplayer/refs/heads/main/screenshots/jwplayer-2026-06-20T183847.png
security:
- kind: domain-security
  name: Jwplayer Domain Security
  slug: jwplayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Jwplayer Trust Center
  slug: jwplayer-trust-center
  summary_line: PCI DSS, GDPR
slug: jwplayer
tags:
- Video
- Streaming
- Media Management
- Live Streaming
- OTT
- Playlists
- Analytics
- DRM
- Advertising
- Webhook
- Player
website: https://jwplayer.com
---
