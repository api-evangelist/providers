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
  name: Apple Music Agentic Access
  operation_count: 24
  slug: apple-music-agentic-access
  summary_line: 24 operations · 1 acting
api_count: 6
apis:
- description: 'REST API for Apple Music: catalog (songs, albums, artists, music videos, playlists, stations), search, charts, recommendations, and the authenticated user''s library, playlists, and ratings.'
  name: Apple Music API
  slug: catalog-library
- description: Apple Music catalog resources
  name: Apple Music Catalog API
  slug: apple-music-catalog-api
- description: The Charts API from Apple Music — 1 operation(s) for charts.
  name: Apple Music Charts API
  slug: apple-music-charts-api
- description: Authenticated user library resources
  name: Apple Music Library API
  slug: apple-music-library-api
- description: The Search API from Apple Music — 2 operation(s) for search.
  name: Apple Music Search API
  slug: apple-music-search-api
- description: The Storefronts API from Apple Music — 3 operation(s) for storefronts.
  name: Apple Music Storefronts API
  slug: apple-music-storefronts-api
artifact_total: 15
collections:
- collection_type: open
  name: Apple Music API
  slug: open-apple-music
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apple-music-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apple-music-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apple-music-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apple-music-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://developer.apple.com/apple-music/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apple.com/documentation/applemusicapi
- group: commercial
  title: ''
  type: Plans
  url: plans/apple-music-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apple-music-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apple-music-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-05-08'
description: Apple Music is Apple's streaming music service. The Apple Music API and MusicKit framework give developers access to the Apple Music catalog, user library, charts, recommendations, search, and playback control. Authentication is via Apple Developer Program JWT tokens; user library access requires a MusicKit Music User Token.
finops:
- name: Apple Music Finops
  service_category: Music Streaming
  slug: apple-music-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Apple Music API (MusicKit API). The Apple Music API is a REST API provided by Apple through the Apple Developer Program. This schema represents the resource
  name: Apple Music GraphQL Schema
  slug: apple-music-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apple-music.png
layout: provider
modified: '2026-05-30'
name: Apple Music
nav: Providers
network: true
overview: 'Apple Music publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Charts API, Library API, and 2 more. Tagged areas include Music, Streaming, Apple, MusicKit, and Catalog.


  Apple Music''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Apple Music Plans Pricing
  plan_count: 2
  slug: apple-music-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 2
  name: Apple Music Rate Limits
  slug: apple-music-rate-limits
score:
  band: thin
  composite: 33.4
  delta: -1.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apple-music/refs/heads/main/screenshots/apple-music-2026-06-20T172322.png
security:
- kind: authentication
  name: Apple Music Authentication
  slug: apple-music-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Apple Music Domain Security
  slug: apple-music-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apple Music Vulnerability Disclosure
  slug: apple-music-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apple-music
tags:
- Music
- Streaming
- Apple
- MusicKit
- Catalog
- Library
website: https://developer.apple.com/apple-music/
---
