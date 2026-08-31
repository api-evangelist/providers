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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Deezer Agentic Access
  operation_count: 41
  slug: deezer-agentic-access
  summary_line: 41 operations · 3 acting
api_count: 1
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
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Deezer Public Album API
  slug: open-deezer-album-api
- collection_type: open
  name: Deezer Public Album Artist API
  slug: open-deezer-artist-api
- collection_type: open
  name: Deezer Public Album Chart API
  slug: open-deezer-chart-api
- collection_type: open
  name: Deezer Public Album Editorial API
  slug: open-deezer-editorial-api
- collection_type: open
  name: Deezer Public Album Genre API
  slug: open-deezer-genre-api
- collection_type: open
  name: Deezer Public Album Infos API
  slug: open-deezer-infos-api
- collection_type: open
  name: Deezer Public Album Playlist API
  slug: open-deezer-playlist-api
- collection_type: open
  name: Deezer Public Album Radio API
  slug: open-deezer-radio-api
- collection_type: open
  name: Deezer Public Album Search API
  slug: open-deezer-search-api
- collection_type: open
  name: Deezer Public Album Track API
  slug: open-deezer-track-api
- collection_type: open
  name: Deezer Public Album User API
  slug: open-deezer-user-api
- collection_type: open
  name: Deezer Public API
  slug: open-deezer
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/deezer-capability-edges.yml
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
overview: 'Deezer publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Chart API, and 8 more. Tagged areas include Music, Streaming, Audio, Authentication, and Catalog.


  Deezer''s developer surface includes authentication and 12 more developer resources.'
plans:
- name: Deezer Plans Pricing
  plan_count: 2
  slug: deezer-plans-pricing
random_paper: 9
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
  composite: 30.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
- Authentication
- Catalog
- Playlists
website: https://www.deezer.com/
---
