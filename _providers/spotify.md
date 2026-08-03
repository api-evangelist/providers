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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Spotify Agentic Access
  operation_count: 96
  slug: spotify-agentic-access
  summary_line: 96 operations · 36 acting
api_count: 15
apis:
- description: The Albums API from Spotify — 7 operation(s) for albums.
  name: Spotify Albums API
  slug: spotify-albums-api
- description: The Artists API from Spotify — 7 operation(s) for artists.
  name: Spotify Artists API
  slug: spotify-artists-api
- description: The Audiobooks API from Spotify — 5 operation(s) for audiobooks.
  name: Spotify Audiobooks API
  slug: spotify-audiobooks-api
- description: The Categories API from Spotify — 3 operation(s) for categories.
  name: Spotify Categories API
  slug: spotify-categories-api
- description: The Chapters API from Spotify — 3 operation(s) for chapters.
  name: Spotify Chapters API
  slug: spotify-chapters-api
- description: The Episodes API from Spotify — 5 operation(s) for episodes.
  name: Spotify Episodes API
  slug: spotify-episodes-api
- description: The Genres API from Spotify — 1 operation(s) for genres.
  name: Spotify Genres API
  slug: spotify-genres-api
- description: The Library API from Spotify — 18 operation(s) for library.
  name: Spotify Library API
  slug: spotify-library-api
- description: The Markets API from Spotify — 1 operation(s) for markets.
  name: Spotify Markets API
  slug: spotify-markets-api
- description: The Player API from Spotify — 13 operation(s) for player.
  name: Spotify Player API
  slug: spotify-player-api
- description: The Playlists API from Spotify — 10 operation(s) for playlists.
  name: Spotify Playlists API
  slug: spotify-playlists-api
- description: The Search API from Spotify — 1 operation(s) for search.
  name: Spotify Search API
  slug: spotify-search-api
- description: The Shows API from Spotify — 5 operation(s) for shows.
  name: Spotify Shows API
  slug: spotify-shows-api
- description: The Tracks API from Spotify — 13 operation(s) for tracks.
  name: Spotify Tracks API
  slug: spotify-tracks-api
- description: The Users API from Spotify — 8 operation(s) for users.
  name: Spotify Users API
  slug: spotify-users-api
artifact_total: 47
collections:
- collection_type: postman
  name: Spotify Web Albums API
  slug: postman-spotify-albums-api
- collection_type: postman
  name: Spotify Web Albums Artists API
  slug: postman-spotify-artists-api
- collection_type: postman
  name: Spotify Web Albums Audiobooks API
  slug: postman-spotify-audiobooks-api
- collection_type: postman
  name: Spotify Web Albums Categories API
  slug: postman-spotify-categories-api
- collection_type: postman
  name: Spotify Web Albums Chapters API
  slug: postman-spotify-chapters-api
- collection_type: postman
  name: Spotify Web Albums Episodes API
  slug: postman-spotify-episodes-api
- collection_type: postman
  name: Spotify Web Albums Genres API
  slug: postman-spotify-genres-api
- collection_type: postman
  name: Spotify Web Albums Library API
  slug: postman-spotify-library-api
- collection_type: postman
  name: Spotify Web Albums Markets API
  slug: postman-spotify-markets-api
- collection_type: postman
  name: Spotify Web Albums Player API
  slug: postman-spotify-player-api
- collection_type: postman
  name: Spotify Web Albums Playlists API
  slug: postman-spotify-playlists-api
- collection_type: postman
  name: Spotify Web Albums Search API
  slug: postman-spotify-search-api
- collection_type: postman
  name: Spotify Web Albums Shows API
  slug: postman-spotify-shows-api
- collection_type: postman
  name: Spotify Web Albums Tracks API
  slug: postman-spotify-tracks-api
- collection_type: postman
  name: Spotify Web Albums Users API
  slug: postman-spotify-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spotify/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spotify-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spotify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spotify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spotify-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spotify-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spotify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spotify
- group: other
  title: ''
  type: Developer
  url: https://developer.spotify.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.spotify.com/documentation/web-api/tutorials/getting-started
- group: auth
  title: ''
  type: Authorization
  url: https://developer.spotify.com/documentation/web-api/concepts/authorization
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.spotify.com/documentation/web-api/concepts/rate-limits
- group: auth
  title: ''
  type: Scopes
  url: https://developer.spotify.com/documentation/web-api/concepts/scopes
- group: operate
  title: ''
  type: Community
  url: https://developer.spotify.com/community
- group: other
  title: ''
  type: Embeds
  url: https://developer.spotify.com/documentation/embeds
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.spotify.com/terms
- group: start
  title: ''
  type: Login
  url: https://accounts.spotify.com/en/login
- group: operate
  title: ''
  type: Forums
  url: https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.spotify.com/documentation/web-api/references/changes/february-2026
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.spotify.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://newsroom.spotify.com/feed/
created: '2023-11-15'
description: Spotify is the world's leading music streaming platform with 600M+ users and 100M+ tracks. The Spotify Web API enables developers to discover music and podcasts, manage Spotify libraries, control audio playback, access audio analysis, and build personalized music experiences. Authentication uses OAuth 2.0 with scopes for user-authorized access. The API underwent significant changes in February 2026 with new generic library endpoints and streamlined playlist management.
examples:
- key_count: 3
  name: Spotify Get Playback State Example
  slug: spotify-get-playback-state-example
- key_count: 3
  name: Spotify Search Tracks Example
  slug: spotify-search-tracks-example
finops:
- name: Spotify Finops
  service_category: API
  slug: spotify-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Spotify Web API. The Spotify Web API is a RESTful service, but this schema models its resources and relationships as GraphQL types to enable
  name: Spotify GraphQL Schema
  slug: spotify-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spotify.png
json_schemas:
- name: Spotify Playlist
  property_count: 14
  slug: spotify-playlist
- name: Spotify Track
  property_count: 18
  slug: spotify-track
json_structures:
- name: Spotify Track Structure
  property_count: 0
  slug: spotify-track-structure
jsonld:
- class_count: 54
  name: Spotify Context
  property_count: 1
  slug: spotify-context
layout: provider
modified: '2026-05-30'
name: Spotify
nav: Providers
network: true
overview: 'Spotify publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Albums API, Artists API, Audiobooks API, and 12 more. Tagged areas include Music, Audio, Streaming, Podcasts, and Playlists.


  The Spotify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spotify''s developer surface includes authentication, getting-started guide, changelog, engineering blog, and 17 more developer resources.'
plans:
- name: Spotify Plans Pricing
  plan_count: 3
  slug: spotify-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Spotify Rate Limits
  slug: spotify-rate-limits
rules:
- name: Spotify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spotify-jsonschema-spectral-rules
- name: Spotify API Rules
  rule_count: 14
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 4
  slug: spotify-rules
scopes:
- name: Spotify Scopes
  scope_count: 19
  slug: spotify-scopes
  summary_line: 19 scopes · authorizationCode
score:
  band: strong
  composite: 60.7
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 81.0
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spotify/refs/heads/main/screenshots/spotify-2026-06-20T194353.png
security:
- kind: authentication
  name: Spotify Authentication
  slug: spotify-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Spotify Domain Security
  slug: spotify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spotify Vulnerability Disclosure
  slug: spotify-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spotify
tags:
- Music
- Audio
- Streaming
- Podcasts
- Playlists
website: https://developer.spotify.com/
---
