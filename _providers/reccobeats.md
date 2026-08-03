---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Reccobeats Agentic Access
  operation_count: 14
  slug: reccobeats-agentic-access
  summary_line: 14 operations · 1 acting
api_count: 6
apis:
- description: Album metadata and tracklists.
  name: ReccoBeats Album API
  slug: reccobeats-album-api
- description: Artist metadata and discography.
  name: ReccoBeats Artist API
  slug: reccobeats-artist-api
- description: Extract audio features directly from an uploaded audio file.
  name: ReccoBeats Audio Analysis API
  slug: reccobeats-audio-analysis-api
- description: Spotify-style audio features for a catalog track.
  name: ReccoBeats Audio Features API
  slug: reccobeats-audio-features-api
- description: Track recommendations generated from seeds.
  name: ReccoBeats Recommendation API
  slug: reccobeats-recommendation-api
- description: Track metadata lookup by ReccoBeats or Spotify ID.
  name: ReccoBeats Track API
  slug: reccobeats-track-api
artifact_total: 12
collections:
- collection_type: open
  name: ReccoBeats API
  slug: open-reccobeats
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reccobeats-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reccobeats-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://reccobeats.com/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://reccobeats.com
- group: docs
  title: ''
  type: Documentation
  url: https://reccobeats.com/docs/documentation/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/reccobeats-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reccobeats-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reccobeats-finops.yml
created: '2026-07-03'
description: ReccoBeats is a free music recommendation and database API service. It exposes a REST API over a database of millions of tracks, artists, and albums, and a machine-learning recommendation engine that suggests tracks from seed tracks, artists, or albums. ReccoBeats also extracts Spotify-style audio features - acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, and valence - either for a catalog track by ID or directly from an uploaded audio file. Resources can be addressed by ReccoBeats UUID or by Spotify ID, and the API requires no API key or authentication.
finops:
- name: Reccobeats Finops
  service_category: Machine Learning and Media
  slug: reccobeats-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reccobeats.png
layout: provider
modified: '2026-07-03'
name: ReccoBeats
nav: Providers
network: true
overview: 'ReccoBeats publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Audio Analysis API, and 3 more. Tagged areas include Music, Recommendations, Audio Features, Audio Analysis, and Music Database.


  ReccoBeats'' developer surface includes engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Reccobeats Plans Pricing
  plan_count: 1
  slug: reccobeats-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Reccobeats Rate Limits
  slug: reccobeats-rate-limits
score:
  band: thin
  composite: 34.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Reccobeats Domain Security
  slug: reccobeats-domain-security
  summary_line: TLSv1.3
slug: reccobeats
tags:
- Music
- Recommendations
- Audio Features
- Audio Analysis
- Music Database
- Spotify Alternative
website: https://reccobeats.com
---
