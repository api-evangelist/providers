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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Last Fm Agentic Access
  operation_count: 2
  slug: last-fm-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Methods for retrieving album metadata and managing album tags
  name: Last.fm Album API
  slug: last-fm-album-api
artifact_total: 30
collections:
- collection_type: postman
  name: Last.fm Album API
  slug: postman-last-fm-album-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lastfm/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/last-fm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/last-fm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/last-fm-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.last.fm/
- group: docs
  title: ''
  type: Documentation
  url: https://www.last.fm/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.last.fm/api/intro
- group: auth
  title: ''
  type: Authentication
  url: https://www.last.fm/api/authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.last.fm/api/tos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lastfm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/last-fm
- group: company
  title: ''
  type: Blog
  url: https://www.last.fm/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.last.fm/pro
- group: other
  title: ''
  type: X
  url: https://x.com/lastfm
- group: operate
  title: ''
  type: StatusPage
  url: https://x.com/lastfmstatus
- group: commercial
  title: ''
  type: Plans
  url: plans/last-fm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/last-fm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/last-fm-finops.yml
created: '2026-06-13'
description: Last.fm is a music discovery and social listening platform that tracks users' listening habits across devices and services via scrobbling. The Last.fm API provides access to a rich music metadata database covering artist information, album data, track details, user listening history, personalized charts, and music recommendations. Developers can integrate scrobbling, retrieve top charts by geography or tag, explore similar artists and tracks, and access user profile data.
examples:
- key_count: 1
  name: Artist Getinfo Response
  slug: artist-getInfo-response
- key_count: 14
  name: Track Scrobble Request
  slug: track-scrobble-request
- key_count: 1
  name: User Getrecenttracks Response
  slug: user-getRecentTracks-response
features:
- description: Comprehensive metadata for artists, albums, and tracks including biographies, images, tags, and similar items
  name: Music Metadata
- description: Track submission API (Scrobbling 2.0) for recording listening history from any client or device
  name: Scrobbling
- description: Access recent tracks, loved tracks, top artists, albums, and tracks for any user
  name: User Listening History
- description: Global and geographic top artists and tracks, plus tag-based and weekly user charts
  name: Music Charts
- description: Similar artist and track recommendations powered by Last.fm's social listening data
  name: Music Discovery
- description: Full-text search across the Last.fm music catalog for artists, albums, and tracks
  name: Artist and Track Search
- description: Browse music by community-applied tags to discover themed playlists and artists
  name: Tag Exploration
- description: Access user friends, listening comparisons, and shared music taste data
  name: User Social Data
finops:
- name: Last Fm Finops
  service_category: ''
  slug: last-fm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/last-fm.png
json_schemas:
- name: Artist
  property_count: 10
  slug: artist
- name: Scrobble
  property_count: 10
  slug: scrobble
- name: Track
  property_count: 13
  slug: track
jsonld:
- class_count: 32
  name: Last Fm Context
  property_count: 1
  slug: last-fm-context
layout: provider
modified: '2026-06-13'
name: Last.fm
nav: Providers
network: true
overview: 'Last.fm publishes 1 API on the [APIs.io](https://apis.io/) network: Album API. Tagged areas include Music, Music Metadata, Scrobbling, Music Discovery, and Streaming.


  The Last.fm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Last.fm''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Last Fm Plans Pricing
  plan_count: 3
  slug: last-fm-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 3
  name: Last Fm Rate Limits
  slug: last-fm-rate-limits
rules:
- name: Last.fm API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: last-fm-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.2
  delta: -3.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 72.0
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 61.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/last-fm/refs/heads/main/screenshots/last-fm-2026-06-20T184321.png
security:
- kind: authentication
  name: Last Fm Authentication
  slug: last-fm-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Last Fm Domain Security
  slug: last-fm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: last-fm
tags:
- Music
- Music Metadata
- Scrobbling
- Music Discovery
- Streaming
use_cases:
- description: Record tracks played in music apps to Last.fm user profiles for history and recommendations
  name: Music Player Scrobbling
- description: Augment music catalogs with artist bios, album art, tags, and similar artist data
  name: Music Metadata Enrichment
- description: Display weekly, monthly, or all-time listening charts for users in applications
  name: Personalized Charts
- description: Power recommendation engines with similar artist and track data from Last.fm
  name: Music Discovery Features
- description: Show what friends are listening to and compare music tastes between users
  name: Social Listening
- description: Display top artists and tracks by country or region for localized music features
  name: Geographic Music Trends
website: https://www.last.fm/
---
