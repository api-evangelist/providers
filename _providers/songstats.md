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
- acting_count: 10
  human_in_the_loop: 0
  name: Songstats Agentic Access
  operation_count: 41
  slug: songstats-agentic-access
  summary_line: 41 operations · 10 acting
api_count: 5
apis:
- description: The Artists API from Songstats — 12 operation(s) for artists.
  name: Songstats Artists API
  slug: songstats-artists-api
- description: The Collaborators API from Songstats — 5 operation(s) for collaborators.
  name: Songstats Collaborators API
  slug: songstats-collaborators-api
- description: The Info API from Songstats — 3 operation(s) for info.
  name: Songstats Info API
  slug: songstats-info-api
- description: The Labels API from Songstats — 9 operation(s) for labels.
  name: Songstats Labels API
  slug: songstats-labels-api
- description: The Tracks API from Songstats — 7 operation(s) for tracks.
  name: Songstats Tracks API
  slug: songstats-tracks-api
artifact_total: 20
collections:
- collection_type: open
  name: Songstats Enterprise API
  slug: open-songstats
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/songstats-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/songstats-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/songstats-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/songstats
- group: start
  title: ''
  type: Portal
  url: https://songstats.com/for/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.songstats.com/
- group: company
  title: ''
  type: Website
  url: https://songstats.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Songstats
- group: company
  title: ''
  type: Blog
  url: https://lab.songstats.com/
- group: start
  title: ''
  type: Signup
  url: https://songstats.com/for/developers
created: '2025-02-12'
description: Songstats provides music data analytics through its Enterprise API, enabling music industry professionals to access streaming statistics, audience data, chart positions, playlist placements, and catalog information for artists, tracks, record labels, and collaborators across all major streaming platforms including Spotify, Apple Music, Amazon Music, Deezer, TikTok, and more. Integrated with Radiostats for radio airplay data across 40,000+ stations.
examples:
- key_count: 3
  name: Songstats Get Artist Stats Example
  slug: songstats-get-artist-stats-example
- key_count: 3
  name: Songstats Get Track Historic Stats Example
  slug: songstats-get-track-historic-stats-example
finops:
- name: Songstats Finops
  service_category: API
  slug: songstats-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/songstats.png
json_schemas:
- name: Songstats Artist
  property_count: 6
  slug: songstats-artist
- name: Songstats Track
  property_count: 8
  slug: songstats-track
json_structures:
- name: Songstats Artist Structure
  property_count: 0
  slug: songstats-artist-structure
jsonld:
- class_count: 5
  name: Songstats Context
  property_count: 13
  slug: songstats-context
layout: provider
modified: '2026-05-19'
name: Songstats
nav: Providers
network: true
overview: 'Songstats publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Artists API, Collaborators API, Info API, and 2 more. Tagged areas include Analytics, Music, Streaming, Artists, and Tracks.


  The Songstats catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Songstats'' developer surface includes authentication, developer portal, documentation, GitHub presence, engineering blog, signup flow, and 4 more developer resources.'
plans:
- name: Songstats Plans Pricing
  plan_count: 3
  slug: songstats-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Songstats Rate Limits
  slug: songstats-rate-limits
rules:
- name: Songstats API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: songstats-jsonschema-spectral-rules
- name: Songstats API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: songstats-rules
score:
  band: developing
  composite: 51.6
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.9
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 55.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/songstats/refs/heads/main/screenshots/songstats-2026-06-20T194203.png
security:
- kind: authentication
  name: Songstats Authentication
  slug: songstats-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Songstats Domain Security
  slug: songstats-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: songstats
tags:
- Analytics
- Music
- Streaming
- Artists
- Tracks
- Labels
website: https://songstats.com/
---
