---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Skywatch Agentic Access
  operation_count: 26
  slug: skywatch-agentic-access
  summary_line: 26 operations · 14 acting
api_count: 7
apis:
- description: Query historical imagery and retrieve matching search results.
  name: SkyWatch Archive Search API
  slug: skywatch-archive-search-api
- description: Estimate the cost of locations, intervals, and pipelines.
  name: SkyWatch Cost Estimation API
  slug: skywatch-cost-estimation-api
- description: Results and delivery URLs produced by pipeline intervals.
  name: SkyWatch Interval Results API
  slug: skywatch-interval-results-api
- description: Reusable server-side areas of interest from KML or GeoJSON.
  name: SkyWatch Locations API
  slug: skywatch-locations-api
- description: Reusable output configurations - format, bands, and mosaicking.
  name: SkyWatch Outputs API
  slug: skywatch-outputs-api
- description: Standing orders that monitor an AOI and deliver imagery on a schedule.
  name: SkyWatch Pipelines API
  slug: skywatch-pipelines-api
- description: Callback-based subscriptions to EarthCache platform events.
  name: SkyWatch Subscriptions API
  slug: skywatch-subscriptions-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SkyWatch EarthCache Archive Search API
  slug: open-skywatch-archive-search-api
- collection_type: open
  name: SkyWatch EarthCache Archive Search Cost Estimation API
  slug: open-skywatch-cost-estimation-api
- collection_type: open
  name: SkyWatch EarthCache Archive Search Interval Results API
  slug: open-skywatch-interval-results-api
- collection_type: open
  name: SkyWatch EarthCache Archive Search Locations API
  slug: open-skywatch-locations-api
- collection_type: open
  name: SkyWatch EarthCache Archive Search Outputs API
  slug: open-skywatch-outputs-api
- collection_type: open
  name: SkyWatch EarthCache Archive Search Pipelines API
  slug: open-skywatch-pipelines-api
- collection_type: open
  name: SkyWatch EarthCache Archive Search Subscriptions API
  slug: open-skywatch-subscriptions-api
- collection_type: open
  name: SkyWatch EarthCache API
  slug: open-skywatch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/skywatch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skywatch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skywatch-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skywatch-apps
- group: company
  title: ''
  type: Website
  url: https://skywatch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.earthcache.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/skywatch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skywatch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/skywatch-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://skywatch.com/blog/
created: '2026-07-04'
description: SkyWatch Space Applications is an Earth observation company whose EarthCache platform gives developers a single API to discover, price, order, and deliver commercial satellite imagery and geospatial data from many providers - Pleiades, SPOT, PlanetScope, SkySat, Sentinel-1, Sentinel-2, TripleSat, Kompsat, and more. The EarthCache API (base https://api.skywatch.co/earthcache, x-api-key auth) exposes Archive Search over historical imagery, Pipelines that monitor an area of interest and deliver imagery on a schedule, interval results with analytics and metadata download URLs, cost estimation, reusable output configurations (format, bands, mosaicking), saved locations, and callback-based subscriptions for platform events. Imagery is billed per square kilometre with resolution-based minimums.
finops:
- name: Skywatch Finops
  service_category: Geospatial and Earth Observation Data
  slug: skywatch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skywatch.png
layout: provider
modified: '2026-07-04'
name: SkyWatch
nav: Providers
network: true
overview: 'SkyWatch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Archive Search API, Cost Estimation API, Interval Results API, and 4 more. Tagged areas include Satellite Imagery, Earth Observation, Geospatial, Remote Sensing, and EarthCache.


  SkyWatch''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Skywatch Plans Pricing
  plan_count: 3
  slug: skywatch-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Skywatch Rate Limits
  slug: skywatch-rate-limits
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.0
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Skywatch Authentication
  slug: skywatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Skywatch Domain Security
  slug: skywatch-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: skywatch
tags:
- Satellite Imagery
- Earth Observation
- Geospatial
- Remote Sensing
- EarthCache
- Imagery
website: https://skywatch.com/
---
