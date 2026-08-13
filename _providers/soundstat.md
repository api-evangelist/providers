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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Soundstat Agentic Access
  operation_count: 20
  slug: soundstat-agentic-access
  summary_line: 20 operations · 15 acting
api_count: 5
apis:
- description: The Genres API from SoundStat — 1 operation(s) for genres.
  name: SoundStat Genres API
  slug: soundstat-genres-api
- description: The Recommendations API from SoundStat — 15 operation(s) for recommendations.
  name: SoundStat Recommendations API
  slug: soundstat-recommendations-api
- description: The Stats API from SoundStat — 1 operation(s) for stats.
  name: SoundStat Stats API
  slug: soundstat-stats-api
- description: The Track API from SoundStat — 2 operation(s) for track.
  name: SoundStat Track API
  slug: soundstat-track-api
- description: The Tracks API from SoundStat — 1 operation(s) for tracks.
  name: SoundStat Tracks API
  slug: soundstat-tracks-api
artifact_total: 12
collections:
- collection_type: open
  name: SoundStat API
  slug: open-soundstat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soundstat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundstat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soundstat-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://soundstat.info
- group: docs
  title: ''
  type: Documentation
  url: https://soundstat.info/api/v1/docs
- group: start
  title: ''
  type: SignUp
  url: https://soundstat.info/auth.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soundstat.info/terms.html
- group: commercial
  title: ''
  type: Plans
  url: plans/soundstat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soundstat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/soundstat-finops.yml
created: '2026-07-03'
description: SoundStat is an independent audio analysis API that returns detailed per-track features - tempo (BPM), key, mode, energy, danceability, valence, instrumentalness, acousticness, loudness, plus segment and beat structure - for music tracks referenced by Spotify track ID. Launched in early 2025 as an alternative after Spotify deprecated its public audio-features and recommendations endpoints, SoundStat has analyzed several million tracks and layers a rich recommendation engine (similar, feature-target, mixed-seed, mood, activity, time-of-day, cross-genre, DJ-compatible, contrast, hidden-gems, and more) plus genre-and-feature search on top of its analysis corpus. The REST API is authenticated with an x-api-key header and billed per unique track analyzed.
finops:
- name: Soundstat Finops
  service_category: Analytics and Media Intelligence
  slug: soundstat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundstat.png
layout: provider
modified: '2026-07-03'
name: SoundStat
nav: Providers
network: true
overview: 'SoundStat publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Genres API, Recommendations API, Stats API, and 2 more. Tagged areas include Music, Audio Analysis, Audio Features, Recommendations, and Track Analysis.


  SoundStat''s developer surface includes authentication, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Soundstat Plans Pricing
  plan_count: 5
  slug: soundstat-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 3
  name: Soundstat Rate Limits
  slug: soundstat-rate-limits
score:
  band: developing
  composite: 43.0
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 59.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.0
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
security:
- kind: authentication
  name: Soundstat Authentication
  slug: soundstat-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Soundstat Domain Security
  slug: soundstat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: soundstat
tags:
- Music
- Audio Analysis
- Audio Features
- Recommendations
- Track Analysis
- Spotify Alternative
website: https://soundstat.info
---
