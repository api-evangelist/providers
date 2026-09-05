---
access_model:
  confidence: medium
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apple Music Agentic Access
  operation_count: 24
  slug: apple-music-agentic-access
  summary_line: 24 operations · 1 acting
api_count: 1
apis:
- description: 'REST API for Apple Music: catalog (songs, albums, artists, music videos, playlists, stations), search, charts, recommendations, and the authenticated user''s library, playlists, and ratings.'
  name: Apple Music API
  slug: catalog-library
- baseURL: https://api.music.apple.com/v1
  baseurl_source: declared
  description: Apple Music catalog resources
  name: Apple Music Catalog API
  slug: apple-music-catalog-api
- baseURL: https://api.music.apple.com/v1
  baseurl_source: declared
  description: The Charts API from Apple Music — 1 operation(s) for charts.
  name: Apple Music Charts API
  slug: apple-music-charts-api
- baseURL: https://api.music.apple.com/v1
  baseurl_source: declared
  description: Authenticated user library resources
  name: Apple Music Library API
  slug: apple-music-library-api
- baseURL: https://api.music.apple.com/v1
  baseurl_source: declared
  description: The Search API from Apple Music — 2 operation(s) for search.
  name: Apple Music Search API
  slug: apple-music-search-api
- baseURL: https://api.music.apple.com/v1
  baseurl_source: declared
  description: The Storefronts API from Apple Music — 3 operation(s) for storefronts.
  name: Apple Music Storefronts API
  slug: apple-music-storefronts-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apple Music Catalog API
  slug: open-apple-music-catalog-api
- collection_type: open
  name: Apple Music Catalog Charts API
  slug: open-apple-music-charts-api
- collection_type: open
  name: Apple Music Catalog Library API
  slug: open-apple-music-library-api
- collection_type: open
  name: Apple Music Catalog Search API
  slug: open-apple-music-search-api
- collection_type: open
  name: Apple Music Catalog Storefronts API
  slug: open-apple-music-storefronts-api
- collection_type: open
  name: Apple Music API
  slug: open-apple-music
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/apple-music-capability-edges.yml
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


  Apple Music''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Apple Music Plans Pricing
  plan_count: 2
  slug: apple-music-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Apple Music Rate Limits
  slug: apple-music-rate-limits
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 51.2
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 33.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
