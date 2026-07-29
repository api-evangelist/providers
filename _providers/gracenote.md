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
- acting_count: 0
  human_in_the_loop: 0
  name: Gracenote Agentic Access
  operation_count: 17
  slug: gracenote-agentic-access
  summary_line: 17 operations
api_count: 9
apis:
- description: The Gracenote OnConnect API delivers TV and video data including schedules, programs, celebrities, sports, images, and station lineups. Designed for mobile apps, connected TVs, EPGs, and streaming exp
  name: Gracenote OnConnect API
  slug: onconnect-api
- description: The Gracenote OnConnect Data API provides extended metadata for TV, movies, celebrities, and sports. It is designed for connected experiences and mobile applications that need rich entertainment data,
  name: Gracenote OnConnect Data API
  slug: onconnect-data-api
- description: The Celebrities API from Gracenote — 2 operation(s) for celebrities.
  name: Gracenote Celebrities API
  slug: gracenote-celebrities-api
- description: The Lineups API from Gracenote — 4 operation(s) for lineups.
  name: Gracenote Lineups API
  slug: gracenote-lineups-api
- description: The Movies API from Gracenote — 2 operation(s) for movies.
  name: Gracenote Movies API
  slug: gracenote-movies-api
- description: The Programs API from Gracenote — 2 operation(s) for programs.
  name: Gracenote Programs API
  slug: gracenote-programs-api
- description: The Series API from Gracenote — 2 operation(s) for series.
  name: Gracenote Series API
  slug: gracenote-series-api
- description: The Sports API from Gracenote — 2 operation(s) for sports.
  name: Gracenote Sports API
  slug: gracenote-sports-api
- description: The Stations API from Gracenote — 3 operation(s) for stations.
  name: Gracenote Stations API
  slug: gracenote-stations-api
artifact_total: 16
collections:
- collection_type: open
  name: Gracenote OnConnect TMS API
  slug: open-gracenote
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gracenote-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gracenote-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gracenote-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gracenote
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gracenote
- group: company
  title: ''
  type: Website
  url: https://www.gracenote.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.tmsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tmsapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tmsapi.com/Getting_Started
- group: operate
  title: ''
  type: Support
  url: https://www.gracenote.com/support/
- group: other
  title: ''
  type: Products
  url: https://www.gracenote.com/products/
- group: other
  title: ''
  type: Parent
  url: https://www.nielsen.com/
- group: company
  title: ''
  type: Blog
  url: https://gracenote.com/insights/
created: '2026-03-16'
description: Gracenote, a Nielsen company, provides entertainment metadata, content recognition technology, and developer APIs for TV, video, music, sports, and automotive industries. Gracenote enables content discovery, search, and personalization across linear and streaming services worldwide.
finops:
- name: Gracenote Finops
  service_category: API
  slug: gracenote-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gracenote.png
layout: provider
modified: '2026-04-28'
name: Gracenote
nav: Providers
network: true
overview: 'Gracenote publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Celebrities API, Lineups API, Movies API, and 4 more. Tagged areas include Automotive, Content Metadata, Entertainment, Music, and Nielsen.


  Gracenote''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Gracenote Plans Pricing
  plan_count: 3
  slug: gracenote-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Gracenote Rate Limits
  slug: gracenote-rate-limits
score:
  band: thin
  composite: 39.1
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.0
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/screenshots/gracenote-2026-06-20T182312.png
security:
- kind: authentication
  name: Gracenote Authentication
  slug: gracenote-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gracenote Domain Security
  slug: gracenote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gracenote
tags:
- Automotive
- Content Metadata
- Entertainment
- Music
- Nielsen
- Sports
- Streaming
- Television
- Video
website: https://www.gracenote.com/
---
