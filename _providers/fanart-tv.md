---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/fanart-tv/hosts/fanart-tv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fanart-tv-hosts.yml
- group: other
  href: https://artifacts.apis.io/fanart-tv/vendors/fanart-tv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fanart-tv-vendors.yml
- group: build
  href: https://artifacts.apis.io/fanart-tv/packages/fanart-tv-packages.yml
  title: ''
  type: SDKs
  url: packages/fanart-tv-packages.yml
- group: build
  href: https://artifacts.apis.io/fanart-tv/packages/fanart-tv-packages.yml
  title: ''
  type: Packages
  url: packages/fanart-tv-packages.yml
- group: auth
  href: https://artifacts.apis.io/fanart-tv/security/fanart-tv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fanart-tv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fanart.tv/
- group: docs
  title: ''
  type: Documentation
  url: https://fanarttv.docs.apiary.io/
- group: docs
  title: ''
  type: APIReference
  url: https://fanarttv.docs.apiary.io/api-description-document
- group: start
  title: ''
  type: GettingStarted
  url: https://fanart.tv/2015/01/personal-api-keys/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/r9VufRkt
created: '2026-10-28'
description: Fanart.tv provides a community-driven API delivering high‑quality fan artwork, posters, and logos for movies, TV shows, and music. The service aggregates user‑contributed images, offering endpoints to retrieve artwork by TMDB or IMDb identifiers. Documentation is hosted on Apiary, with API servers at webservice.fanart.tv. Developers can use personal client keys alongside project keys for access, and the API returns JSON metadata and image URLs for integration into media applications.
layout: provider
modified: '2026-10-28'
name: Fanart.tv
nav: Providers
network: true
overview: 'Fanart.tv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Image, Movies, and TV.


  Fanart.tv''s developer surface includes documentation, API reference, getting-started guide, support, and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 11.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fanart Tv Domain Security
  slug: fanart-tv-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fanart-tv
tags:
- Company
- Media
- Image
- Movies
- TV
website: https://fanart.tv/
---
