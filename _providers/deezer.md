---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Deezer Agentic Access
  operation_count: 41
  slug: deezer-agentic-access
  summary_line: 41 operations · 3 acting
api_count: 12
apis:
- description: Public REST API covering /track, /album, /artist, /playlist, /chart, /search, /genre, /radio, /user, and /editorial. Public endpoints (catalog, search) are unauthenticated and return JSON; user-scoped
  name: Deezer API
  slug: platform
- description: The Album API from Deezer — 2 operation(s) for album.
  name: Deezer Album API
  slug: deezer-album-api
- description: The Artist API from Deezer — 6 operation(s) for artist.
  name: Deezer Artist API
  slug: deezer-artist-api
- description: The Chart API from Deezer — 5 operation(s) for chart.
  name: Deezer Chart API
  slug: deezer-chart-api
- description: The Editorial API from Deezer — 3 operation(s) for editorial.
  name: Deezer Editorial API
  slug: deezer-editorial-api
- description: The Genre API from Deezer — 3 operation(s) for genre.
  name: Deezer Genre API
  slug: deezer-genre-api
- description: The Infos API from Deezer — 1 operation(s) for infos.
  name: Deezer Infos API
  slug: deezer-infos-api
- description: The Playlist API from Deezer — 2 operation(s) for playlist.
  name: Deezer Playlist API
  slug: deezer-playlist-api
- description: The Radio API from Deezer — 3 operation(s) for radio.
  name: Deezer Radio API
  slug: deezer-radio-api
- description: The Search API from Deezer — 5 operation(s) for search.
  name: Deezer Search API
  slug: deezer-search-api
- description: The Track API from Deezer — 1 operation(s) for track.
  name: Deezer Track API
  slug: deezer-track-api
- description: The User API from Deezer — 7 operation(s) for user.
  name: Deezer User API
  slug: deezer-user-api
artifact_total: 22
collections:
- collection_type: open
  name: Deezer Public API
  slug: open-deezer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deezer-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deezer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deezer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deezer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deezer-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deezer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deezer
- group: company
  title: ''
  type: Website
  url: https://www.deezer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.deezer.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/deezer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deezer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deezer-finops.yml
created: '2026-05-08'
description: Deezer is a global music streaming service. The Deezer API is a public REST API for tracks, albums, artists, playlists, charts, search, and authenticated user library. It uses OAuth 2.0 for user- scoped operations and is free to use within published rate limits.
finops:
- name: Deezer Finops
  service_category: Music Streaming
  slug: deezer-finops
graphqls:
- description: Deezer is a music streaming service. The API covers track search, artist and album lookups, playlist management, user library, editorial playlists, radio, podcast episode data, and music recommendatio
  name: Deezer GraphQL API
  slug: deezer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deezer.png
layout: provider
modified: '2026-05-08'
name: Deezer
nav: Providers
network: true
overview: 'Deezer publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Chart API, and 8 more. Tagged areas include Music, Streaming, Audio, OAuth, and Catalog.


  Deezer''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Deezer Plans Pricing
  plan_count: 2
  slug: deezer-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 1
  name: Deezer Rate Limits
  slug: deezer-rate-limits
scopes:
- name: Deezer Scopes
  scope_count: 7
  slug: deezer-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 28.8
  delta: -5.7
  facets:
    commercial_clarity: 13.2
    contract_quality: 54.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/deezer/refs/heads/main/screenshots/deezer-2026-06-20T175819.png
security:
- kind: authentication
  name: Deezer Authentication
  slug: deezer-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Deezer Domain Security
  slug: deezer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deezer Vulnerability Disclosure
  slug: deezer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deezer
tags:
- Music
- Streaming
- Audio
- OAuth
- Catalog
- Playlists
website: https://www.deezer.com/
---
