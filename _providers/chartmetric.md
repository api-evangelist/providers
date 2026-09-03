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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Chartmetric Agentic Access
  operation_count: 26
  slug: chartmetric-agentic-access
  summary_line: 26 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Album metadata, tracks, followers, charts, and placements.
  name: Chartmetric Albums API
  slug: chartmetric-albums-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Artist metadata, stats, related artists, and placements.
  name: Chartmetric Artists API
  slug: chartmetric-artists-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Exchange a refresh token for a short-lived access token.
  name: Chartmetric Authentication API
  slug: chartmetric-authentication-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Platform chart rankings and Chartmetric Score (cm-score).
  name: Chartmetric Charts API
  slug: chartmetric-charts-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Playlist metadata, track listings, snapshots, and evolution.
  name: Chartmetric Playlists API
  slug: chartmetric-playlists-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Unified entity search.
  name: Chartmetric Search API
  slug: chartmetric-search-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Track metadata, stats, charts, and playlist placements.
  name: Chartmetric Tracks API
  slug: chartmetric-tracks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chartmetric Albums API
  slug: open-chartmetric-albums-api
- collection_type: open
  name: Chartmetric Albums Artists API
  slug: open-chartmetric-artists-api
- collection_type: open
  name: Chartmetric Albums Authentication API
  slug: open-chartmetric-authentication-api
- collection_type: open
  name: Chartmetric Albums Charts API
  slug: open-chartmetric-charts-api
- collection_type: open
  name: Chartmetric Albums Playlists API
  slug: open-chartmetric-playlists-api
- collection_type: open
  name: Chartmetric Albums Search API
  slug: open-chartmetric-search-api
- collection_type: open
  name: Chartmetric Albums Tracks API
  slug: open-chartmetric-tracks-api
- collection_type: open
  name: Chartmetric API
  slug: open-chartmetric
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/chartmetric-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chartmetric-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chartmetric-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chartmetric-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chartmetric
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chartmetric
- group: company
  title: ''
  type: Website
  url: https://www.chartmetric.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.chartmetric.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/chartmetric-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chartmetric-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chartmetric-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://hmc.chartmetric.com/feed
created: '2026-06-21'
description: Chartmetric is a music analytics and artist-intelligence platform. Its REST API exposes the company's catalog of artists, tracks, albums, playlists, and charts along with cross-platform streaming, social, and radio statistics across Spotify, Apple Music, YouTube, TikTok, Instagram, and more, plus a unified search endpoint.
finops:
- name: Chartmetric Finops
  service_category: Analytics
  slug: chartmetric-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chartmetric.png
layout: provider
modified: '2026-06-21'
name: Chartmetric
nav: Providers
network: true
overview: 'Chartmetric publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Albums API, Artists API, Authentication API, and 4 more. Tagged areas include Music, Analytics, Artist Intelligence, Streaming, and Charts.


  Chartmetric''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Chartmetric Plans Pricing
  plan_count: 4
  slug: chartmetric-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Chartmetric Rate Limits
  slug: chartmetric-rate-limits
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chartmetric/refs/heads/main/screenshots/chartmetric-2026-07-25T205111.png
security:
- kind: authentication
  name: Chartmetric Authentication
  slug: chartmetric-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chartmetric Domain Security
  slug: chartmetric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chartmetric
tags:
- Music
- Analytics
- Artist Intelligence
- Streaming
- Charts
website: https://www.chartmetric.com
---
