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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gracenote Agentic Access
  operation_count: 17
  slug: gracenote-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- description: The Gracenote OnConnect API delivers TV and video data including schedules, programs, celebrities, sports, images, and station lineups. Designed for mobile apps, connected TVs, EPGs, and streaming exp
  name: Gracenote OnConnect API
  slug: onconnect-api
- description: The Gracenote OnConnect Data API provides extended metadata for TV, movies, celebrities, and sports. It is designed for connected experiences and mobile applications that need rich entertainment data,
  name: Gracenote OnConnect Data API
  slug: onconnect-data-api
- baseURL: http://data.tmsapi.com/v1.1
  baseurl_source: spec
  description: The Celebrities API from Gracenote — 2 operation(s) for celebrities.
  name: Gracenote Celebrities API
  slug: gracenote-celebrities-api
- baseURL: http://data.tmsapi.com/v1.1
  baseurl_source: spec
  description: The Lineups API from Gracenote — 4 operation(s) for lineups.
  name: Gracenote Lineups API
  slug: gracenote-lineups-api
- baseURL: http://data.tmsapi.com/v1.1
  baseurl_source: spec
  description: The Movies API from Gracenote — 2 operation(s) for movies.
  name: Gracenote Movies API
  slug: gracenote-movies-api
- baseURL: http://data.tmsapi.com/v1.1
  baseurl_source: spec
  description: The Programs API from Gracenote — 2 operation(s) for programs.
  name: Gracenote Programs API
  slug: gracenote-programs-api
- baseURL: http://data.tmsapi.com/v1.1
  baseurl_source: spec
  description: The Series API from Gracenote — 2 operation(s) for series.
  name: Gracenote Series API
  slug: gracenote-series-api
- baseURL: http://data.tmsapi.com/v1.1
  baseurl_source: spec
  description: The Sports API from Gracenote — 2 operation(s) for sports.
  name: Gracenote Sports API
  slug: gracenote-sports-api
- baseURL: http://data.tmsapi.com/v1.1
  baseurl_source: spec
  description: The Stations API from Gracenote — 3 operation(s) for stations.
  name: Gracenote Stations API
  slug: gracenote-stations-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities API
  slug: open-gracenote-celebrities-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Lineups API
  slug: open-gracenote-lineups-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Movies API
  slug: open-gracenote-movies-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Programs API
  slug: open-gracenote-programs-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Series API
  slug: open-gracenote-series-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Sports API
  slug: open-gracenote-sports-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Stations API
  slug: open-gracenote-stations-api
- collection_type: open
  name: Gracenote OnConnect TMS API
  slug: open-gracenote
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gracenote-capability-edges.yml
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


  Gracenote''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 9 more developer resources.'
plans:
- name: Gracenote Plans Pricing
  plan_count: 3
  slug: gracenote-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Gracenote Rate Limits
  slug: gracenote-rate-limits
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
