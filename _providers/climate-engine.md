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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Climate Engine Agentic Access
  operation_count: 23
  slug: climate-engine-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 6
apis:
- description: Key validation, expiration, and user quotas.
  name: Climate Engine Home API
  slug: climate-engine-home-api
- description: Dataset dates, variables, county names, and raster classifications.
  name: Climate Engine Metadata API
  slug: climate-engine-metadata-api
- description: Earth Engine map IDs and asynchronous raster exports.
  name: Climate Engine Raster API
  slug: climate-engine-raster-api
- description: Pre-built drought, vegetation, and site characterization reports.
  name: Climate Engine Reports API
  slug: climate-engine-reports-api
- description: Native, interannual, standard-index, and regression time series.
  name: Climate Engine Timeseries API
  slug: climate-engine-timeseries-api
- description: Statistics reduced over coordinates and feature collections.
  name: Climate Engine Zonal Statistics API
  slug: climate-engine-zonal-statistics-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/climate-engine-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/climate-engine-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/climate-engine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/climate-engine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/climate-engine-finops.yml
created: '2026-06-20'
description: Climate Engine is a geospatial climate and remote-sensing data platform that runs on Google Earth Engine. Its commercial REST API (api.climateengine.org) provides on-demand processing of satellite and gridded climate datasets - Landsat, Sentinel, MODIS, GRIDMET, ERA5, CHIRPS and more - returning timeseries, map tiles, zonal statistics, and pre-built reports over points, polygons, and feature collections.
finops:
- name: Climate Engine Finops
  service_category: Analytics
  slug: climate-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/climate-engine.png
layout: provider
modified: '2026-06-20'
name: Climate Engine
nav: Providers
network: true
overview: 'Climate Engine publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Home API, Metadata API, Raster API, and 3 more. Tagged areas include Climate, Geospatial, Remote Sensing, Satellite, and Earth Observation.


  Climate Engine''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Climate Engine Plans Pricing
  plan_count: 2
  slug: climate-engine-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Climate Engine Rate Limits
  slug: climate-engine-rate-limits
score:
  band: thin
  composite: 33.2
  delta: -1.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/climate-engine/refs/heads/main/screenshots/climate-engine-2026-06-20T174522.png
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
