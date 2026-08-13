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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Soundcloud Agentic Access
  operation_count: 19
  slug: soundcloud-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 6
apis:
- description: REST API for SoundCloud covering tracks (upload, metadata, stream), users (/me, profiles), playlists (CRUD), search (title/username/description), social (follow, like, comment), and audio playback. OA
  name: SoundCloud API
  slug: platform
- description: Playlist CRUD
  name: SoundCloud Playlists API
  slug: soundcloud-playlists-api
- description: Search and resolution
  name: SoundCloud Search API
  slug: soundcloud-search-api
- description: Follow and like actions
  name: SoundCloud Social API
  slug: soundcloud-social-api
- description: Track CRUD, streaming, and comments
  name: SoundCloud Tracks API
  slug: soundcloud-tracks-api
- description: Authenticated user and profile actions
  name: SoundCloud Users API
  slug: soundcloud-users-api
artifact_total: 16
collections:
- collection_type: open
  name: SoundCloud API
  slug: open-soundcloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soundcloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/soundcloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundcloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soundcloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/soundcloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soundcloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/soundcloud
- group: company
  title: ''
  type: Website
  url: https://soundcloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.soundcloud.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/soundcloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soundcloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/soundcloud-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://developers.soundcloud.com/blog/blog.rss
created: '2026-05-08'
description: SoundCloud is a music and audio streaming platform with a developer REST API for tracks, users, playlists, search, comments, likes, and uploads. Authentication is OAuth 2.1 with PKCE; access tokens expire approximately every hour.
finops:
- name: Soundcloud Finops
  service_category: Music Streaming
  slug: soundcloud-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the SoundCloud platform API. SoundCloud provides a REST API v2 for audio streaming and music discovery, covering tracks, users, playlists, socia
  name: SoundCloud GraphQL Schema
  slug: soundcloud-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundcloud.png
layout: provider
modified: '2026-05-30'
name: SoundCloud
nav: Providers
network: true
overview: 'SoundCloud publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Playlists API, Search API, Social API, and 2 more. Tagged areas include Music, Streaming, Audio, OAuth, and Tracks.


  SoundCloud''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Soundcloud Plans Pricing
  plan_count: 2
  slug: soundcloud-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Soundcloud Rate Limits
  slug: soundcloud-rate-limits
scopes:
- name: Soundcloud Scopes
  scope_count: 1
  slug: soundcloud-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 31.1
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 60.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soundcloud/refs/heads/main/screenshots/soundcloud-2026-06-20T194220.png
security:
- kind: authentication
  name: Soundcloud Authentication
  slug: soundcloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Soundcloud Domain Security
  slug: soundcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Soundcloud Vulnerability Disclosure
  slug: soundcloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: soundcloud
tags:
- Music
- Streaming
- Audio
- OAuth
- Tracks
- Playlists
website: https://soundcloud.com/
---
