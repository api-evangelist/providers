---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.6
  scored_at: '2026-11-06'
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
  description: Platform chart rankings and Chartmetric Score (cm-score).
  name: Chartmetric Charts API
  slug: chartmetric-charts-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Unified entity search.
  name: Chartmetric Search API
  slug: chartmetric-search-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Albums, EPs and singles as released on streaming platforms, identified by a Chartmetric album ID. Endpoints cover album metadata, cross-platform ID lookup, the tracklist, per-platform stats, chart app
  name: Chartmetric Album API
  slug: chartmetric-album-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Artists, the core entity in Chartmetric, identified by a Chartmetric artist ID. Endpoints cover metadata and platform URLs, cross-platform ID lookup, fan metrics and cached stat trends, artist rank an
  name: Chartmetric Artist API
  slug: chartmetric-artist-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Brands tracked for sponsorship and partnership research. Endpoints list brand names, filter brands by interest category, and return the details of a single brand.
  name: Chartmetric Brand API
  slug: chartmetric-brand-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Cities used for geographic breakdowns of audience and consumption data. Endpoints list the cities of a country and return the top artists or tracks in a city for a given platform.
  name: Chartmetric City API
  slug: chartmetric-city-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Country-level rankings. Endpoints return artist rankings for a country, broken down by area, ranking type and sub-area.
  name: Chartmetric Country API
  slug: chartmetric-country-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Playlist curators — the editorial and user accounts that own playlists on Spotify, Apple Music, Amazon, Deezer, YouTube and iTunes. Endpoints list curators per platform and return a curator's metadata
  name: Chartmetric Curator API
  slug: chartmetric-curator-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Live events tied to a venue. Endpoints return the events scheduled at a given venue.
  name: Chartmetric Event API
  slug: chartmetric-event-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Music festivals tracked by Chartmetric. Endpoints return the list of festivals.
  name: Chartmetric Festival API
  slug: chartmetric-festival-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Chartmetric's genre taxonomy, used to filter artists, tracks and charts. Endpoints list all genres and return a single genre by ID.
  name: Chartmetric Genre API
  slug: chartmetric-genre-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Playlists across Spotify, Apple Music, Amazon, Deezer, YouTube, iTunes and SoundCloud. Endpoints list playlists per platform and return playlist metadata, follower and position history, current or pas
  name: Chartmetric Playlist API
  slug: chartmetric-playlist-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Radio airplay data for artists and tracks. Endpoints return airplay time series, total airplay counts overall, by entity and by broadcast market, and the radio station list for a country.
  name: Chartmetric Radio API
  slug: chartmetric-radio-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Deep social data for the social accounts linked to Chartmetric entities. Endpoints return post-level performance, such as the top Instagram posts and reels of an artist.
  name: Chartmetric SNS API
  slug: chartmetric-sns-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Authentication. Exchange your refresh token for a short-lived access token, which must be sent as a bearer token on every other request.
  name: Chartmetric Token API
  slug: chartmetric-token-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Tracks (recordings), identified by a Chartmetric track ID or a platform ID such as an ISRC or Spotify ID. Endpoints cover track metadata, cross-platform ID lookup, per-platform stats, chart appearance
  name: Chartmetric Track API
  slug: chartmetric-track-api
- baseURL: https://api.chartmetric.com/api
  baseurl_source: declared
  description: Venues used for live-event and touring data. Endpoints return the list of venues.
  name: Chartmetric Venue API
  slug: chartmetric-venue-api
artifact_total: 33
collections:
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
  href: https://artifacts.apis.io/chartmetric/capabilities/chartmetric-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/chartmetric-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/chartmetric/agentic-access/chartmetric-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chartmetric-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/chartmetric/security/chartmetric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chartmetric-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/chartmetric/authentication/chartmetric-authentication.yml
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
  href: https://artifacts.apis.io/chartmetric/plans/chartmetric-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chartmetric-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chartmetric/rate-limits/chartmetric-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chartmetric-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chartmetric/finops/chartmetric-finops.yml
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
- has_sources: true
  method: generated
  name: Chartmetric Finops
  primary_unit: ''
  service_category: Analytics
  slug: chartmetric-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chartmetric.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.chartmetric.com over HTTP.
  name: Chartmetric MCP Server
  slug: chartmetric
modified: '2026-06-21'
name: Chartmetric
nav: Providers
network: true
overview: 'Chartmetric publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Charts API, Search API, Album API, and 14 more. Tagged areas include Music, Analytics, Artist Intelligence, Streaming, and Charts.


  The Chartmetric catalog on APIs.io includes 1 Spectral governance ruleset.


  Chartmetric''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Chartmetric Plans Pricing
  plan_count: 4
  slug: chartmetric-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Chartmetric Rate Limits
  slug: chartmetric-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Chartmetric API Rules
  rule_count: 62
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 7
  slug: chartmetric-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 52.0
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 10.5
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 68.0
      total: 25
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chartmetric/chartmetric-2026-07-25T205111.png
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
