---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Dacast Agentic Access
  operation_count: 19
  slug: dacast-agentic-access
  summary_line: 19 operations · 11 acting
api_count: 1
apis:
- description: Viewer analytics and reporting.
  name: Dacast Analytics API
  slug: dacast-analytics-api
- description: Live streaming channels and simulcast.
  name: Dacast Live Channels API
  slug: dacast-live-channels-api
- description: Ordered collections of VOD and live content.
  name: Dacast Playlists API
  slug: dacast-playlists-api
- description: Video on demand upload and management.
  name: Dacast VOD API
  slug: dacast-vod-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dacast Analytics API
  slug: open-dacast-analytics-api
- collection_type: open
  name: Dacast Analytics Live Channels API
  slug: open-dacast-live-channels-api
- collection_type: open
  name: Dacast Analytics Playlists API
  slug: open-dacast-playlists-api
- collection_type: open
  name: Dacast Analytics VOD API
  slug: open-dacast-vod-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dacast-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dacast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dacast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dacast-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dacast
- group: company
  title: ''
  type: Website
  url: https://www.dacast.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dacast.com
- group: commercial
  title: ''
  type: Plans
  url: plans/dacast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dacast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dacast-finops.yml
created: '2026-07-11'
description: Dacast is a unified live streaming and video hosting (OTT) platform that lets businesses broadcast live channels, host and monetize video on demand (VOD), organize content into playlists, and embed a white-label HTML5 player. Dacast exposes a RESTful JSON API (base https://developer.dacast.com/v2) for programmatically creating live channels, uploading and managing VOD, building playlists, and reading viewer analytics. API requests authenticate with an X-Api-Key header. API access is gated to Scale and Custom plans (trial accounts can request temporary access from sales), so the endpoints below are grounded in Dacast's public developer docs but several exact paths beyond the confirmed /v2/channel, /v2/vod, and /v2/playlist are honestly modeled.
finops:
- name: Dacast Finops
  service_category: Media and Streaming
  slug: dacast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dacast.png
layout: provider
modified: '2026-07-11'
name: Dacast
nav: Providers
network: true
overview: 'Dacast publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Live Channels API, Playlists API, and 1 more. Tagged areas include Live Streaming, Video, VOD, OTT, and Video Hosting.


  Dacast''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Dacast Plans Pricing
  plan_count: 5
  slug: dacast-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Dacast Rate Limits
  slug: dacast-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dacast/refs/heads/main/screenshots/dacast-2026-07-25T211123.png
security:
- kind: authentication
  name: Dacast Authentication
  slug: dacast-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dacast Domain Security
  slug: dacast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dacast
tags:
- Live Streaming
- Video
- VOD
- OTT
- Video Hosting
- Media
- Analytics
website: https://www.dacast.com
---
