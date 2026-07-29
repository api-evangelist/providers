---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
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
random_paper: 72
score:
  band: emerging
  composite: 16.4
  delta: -1.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 17.7
  schema_version: 0.6
  scored_at: '2026-07-28'
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
