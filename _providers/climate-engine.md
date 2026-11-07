---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Climate Engine Agentic Access
  operation_count: 23
  slug: climate-engine-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.climateengine.org
  baseurl_source: declared
  description: Key validation, expiration, and user quotas.
  name: Climate Engine Home API
  slug: climate-engine-home-api
- baseURL: https://api.climateengine.org
  baseurl_source: declared
  description: Dataset dates, variables, county names, and raster classifications.
  name: Climate Engine Metadata API
  slug: climate-engine-metadata-api
- baseURL: https://api.climateengine.org
  baseurl_source: declared
  description: Pre-built drought, vegetation, and site characterization reports.
  name: Climate Engine Reports API
  slug: climate-engine-reports-api
- baseURL: https://api.climateengine.org
  baseurl_source: declared
  description: The raster/export API from Climate Engine — 27 operation(s) for raster/export.
  name: Climate Engine Raster/export API
  slug: climate-engine-raster-export-api
- baseURL: https://api.climateengine.org
  baseurl_source: declared
  description: The raster/mapid API from Climate Engine — 24 operation(s) for raster/mapid.
  name: Climate Engine Raster/mapid API
  slug: climate-engine-raster-mapid-api
- baseURL: https://api.climateengine.org
  baseurl_source: declared
  description: The zonal_stats API from Climate Engine — 12 operation(s) for zonal_stats.
  name: Climate Engine Zonal Stats API
  slug: climate-engine-zonal-stats-api
- baseURL: https://api.climateengine.org
  baseurl_source: declared
  description: The Time Series API from Climate Engine — 8 operation(s) for time series.
  name: Climate Engine Time Series API
  slug: climate-engine-time-series-api
artifact_total: 21
collections:
- collection_type: open
  name: 'Climate Engine API v1: climate-engine-pro Home API'
  slug: open-climate-engine-home-api
- collection_type: open
  name: 'Climate Engine API v1: climate-engine-pro Home Metadata API'
  slug: open-climate-engine-metadata-api
- collection_type: open
  name: 'Climate Engine API v1: climate-engine-pro Home Raster API'
  slug: open-climate-engine-raster-api
- collection_type: open
  name: 'Climate Engine API v1: climate-engine-pro Home Reports API'
  slug: open-climate-engine-reports-api
- collection_type: open
  name: 'Climate Engine API v1: climate-engine-pro Home Timeseries API'
  slug: open-climate-engine-timeseries-api
- collection_type: open
  name: 'Climate Engine API v1: climate-engine-pro Home Zonal Statistics API'
  slug: open-climate-engine-zonal-statistics-api
- collection_type: open
  name: 'Climate Engine API v1: climate-engine-pro'
  slug: open-climate-engine
common:
- group: agent
  href: https://artifacts.apis.io/climate-engine/agentic-access/climate-engine-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/climate-engine-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/climate-engine/security/climate-engine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/climate-engine-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/climate-engine/authentication/climate-engine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/climate-engine-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/climate-engine
- group: company
  title: ''
  type: Website
  url: https://www.climateengine.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.climateengine.org
- group: commercial
  href: https://artifacts.apis.io/climate-engine/plans/climate-engine-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/climate-engine-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/climate-engine/rate-limits/climate-engine-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/climate-engine-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/climate-engine/finops/climate-engine-finops.yml
  title: ''
  type: FinOps
  url: finops/climate-engine-finops.yml
created: '2026-06-20'
description: Climate Engine is a geospatial climate and remote-sensing data platform that runs on Google Earth Engine. Its commercial REST API (api.climateengine.org) provides on-demand processing of satellite and gridded climate datasets - Landsat, Sentinel, MODIS, GRIDMET, ERA5, CHIRPS and more - returning timeseries, map tiles, zonal statistics, and pre-built reports over points, polygons, and feature collections.
finops:
- has_sources: true
  method: generated
  name: Climate Engine Finops
  primary_unit: ''
  service_category: Analytics
  slug: climate-engine-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/climate-engine.png
layout: provider
modified: '2026-06-20'
name: Climate Engine
nav: Providers
network: true
overview: 'Climate Engine publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Home API, Metadata API, Reports API, and 4 more. Tagged areas include Climate, Geospatial, Remote Sensing, Satellite, and Earth Observation.


  The Climate Engine catalog on APIs.io includes 1 Spectral governance ruleset.


  Climate Engine''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Climate Engine Plans Pricing
  plan_count: 2
  slug: climate-engine-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Climate Engine Rate Limits
  slug: climate-engine-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Climate Engine API Rules
  rule_count: 52
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 8
  slug: climate-engine-rules
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 48.9
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 25.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 50.0
      total: 14
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/climate-engine/climate-engine-2026-06-20T174522.png
security:
- kind: authentication
  name: Climate Engine Authentication
  slug: climate-engine-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Climate Engine Domain Security
  slug: climate-engine-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: climate-engine
tags:
- Climate
- Geospatial
- Remote Sensing
- Satellite
- Earth Observation
website: https://www.climateengine.com
---
