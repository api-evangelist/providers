---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Soundcharts Agentic Access
  operation_count: 32
  slug: soundcharts-agentic-access
  summary_line: 32 operations · 1 acting
api_count: 9
apis:
- description: The Album API from Soundcharts — 4 operation(s) for album.
  name: Soundcharts Album API
  slug: soundcharts-album-api
- description: The Artist API from Soundcharts — 7 operation(s) for artist.
  name: Soundcharts Artist API
  slug: soundcharts-artist-api
- description: The Chart API from Soundcharts — 5 operation(s) for chart.
  name: Soundcharts Chart API
  slug: soundcharts-chart-api
- description: The Metrics API from Soundcharts — 4 operation(s) for metrics.
  name: Soundcharts Metrics API
  slug: soundcharts-metrics-api
- description: The Playlist API from Soundcharts — 3 operation(s) for playlist.
  name: Soundcharts Playlist API
  slug: soundcharts-playlist-api
- description: The Radio API from Soundcharts — 3 operation(s) for radio.
  name: Soundcharts Radio API
  slug: soundcharts-radio-api
- description: The Referential API from Soundcharts — 1 operation(s) for referential.
  name: Soundcharts Referential API
  slug: soundcharts-referential-api
- description: The Search API from Soundcharts — 1 operation(s) for search.
  name: Soundcharts Search API
  slug: soundcharts-search-api
- description: The Song API from Soundcharts — 4 operation(s) for song.
  name: Soundcharts Song API
  slug: soundcharts-song-api
artifact_total: 16
collections:
- collection_type: open
  name: Soundcharts API
  slug: open-soundcharts
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soundcharts-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundcharts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soundcharts-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soundcharts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/soundcharts
- group: company
  title: ''
  type: Website
  url: https://soundcharts.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soundcharts.com/api/v2/doc
- group: commercial
  title: ''
  type: Plans
  url: plans/soundcharts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soundcharts-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/soundcharts-finops.yml
created: '2026-06-21'
description: Soundcharts is a global music-market intelligence platform that aggregates standardized metadata and real-time performance data for artists, songs, albums, and playlists across streaming, social, chart, and radio sources. The Soundcharts API exposes this catalog and analytics layer over a REST interface at https://customer.api.soundcharts.com, authenticated with x-app-id and x-api-key headers.
finops:
- name: Soundcharts Finops
  service_category: Analytics
  slug: soundcharts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundcharts.png
layout: provider
modified: '2026-06-21'
name: Soundcharts
nav: Providers
network: true
overview: 'Soundcharts publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Chart API, and 6 more. Tagged areas include Music, Analytics, Market Intelligence, Metadata, and Streaming.


  Soundcharts'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Soundcharts Plans Pricing
  plan_count: 4
  slug: soundcharts-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 3
  name: Soundcharts Rate Limits
  slug: soundcharts-rate-limits
score:
  band: thin
  composite: 39.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Soundcharts Authentication
  slug: soundcharts-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Soundcharts Domain Security
  slug: soundcharts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soundcharts
tags:
- Music
- Analytics
- Market Intelligence
- Metadata
- Streaming
- Charts
website: https://soundcharts.com/
---
