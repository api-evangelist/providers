---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Historical public REST API for the 8tracks internet-radio platform. Exposes mix discovery and search, per-session play tokens, playback control (play/next/skip/report), similar-mix recommendation, and
  name: 8tracks API v3
  slug: 8tracks-api-v3
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://8tracks.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://8tracks.com/developers/includes
- group: docs
  title: ''
  type: APIReference
  url: https://8tracks.com/developers/api_v3
- group: company
  title: ''
  type: Blog
  url: https://blog.8tracks.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/8tracks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/8tracks-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/8tracks-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/8tracks-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/8tracks-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/8tracks-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/8tracks-well-known.yml
created: '2026-07-17'
description: 8tracks was a San Francisco-based internet radio and social music-streaming service that let people create and share handcrafted playlists ("mixes") of at least eight tracks, discover mixes by mood, activity, genre, and tag, and play them back through the web, iOS, and Android apps. Founded in 2008, it grew to more than eight million monthly listeners by 2014 before declining. 8tracks published a public REST API (v2/v3) that exposed mix discovery, playback token sessions, track skip/report events, and user likes/favorites, but stopped issuing new API keys in February 2015. The company ceased operations on December 31, 2019, briefly relaunched under BackBeat Inc. in April 2020, and the service has been inactive since. This profile documents the historical API surface and web properties.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/8tracks.png
layout: provider
modified: '2026-07-17'
name: 8Tracks
nav: Providers
network: true
overview: '8Tracks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Streaming, Radio, and Playlists.


  8Tracks'' developer surface includes documentation, API reference, engineering blog, authentication, and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: 8Tracks Authentication
  slug: 8tracks-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: 8Tracks Domain Security
  slug: 8tracks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 8tracks
tags:
- Company
- Music
- Streaming
- Radio
- Playlists
- Audio
- Media
- Entertainment
website: https://8tracks.com/developers
---
