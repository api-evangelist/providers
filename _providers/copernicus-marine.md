---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Copernicus Marine Toolbox provides the officially supported programmatic interface to the Copernicus Marine Data Store, available as both a Python library and CLI. Core operations include describe
  name: Copernicus Marine Toolbox API
  slug: copernicus-marine-toolbox-api
- description: The Copernicus Marine Web Map Tile Service (WMTS) is an OGC-compliant REST API for visualizing ocean data as raster map tiles. It supports GetCapabilities to discover available datasets and layers, Ge
  name: Copernicus Marine WMTS API
  slug: copernicus-marine-wmts-api
- description: The Copernicus Marine Catalogue Service for the Web (CSW) provides OGC-compliant metadata discovery over the full product catalogue. It supports GetCapabilities, DescribeRecord, GetRecords (search and
  name: Copernicus Marine CSW Catalogue API
  slug: copernicus-marine-csw-catalogue-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/copernicus-marine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marine.copernicus.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://help.marine.copernicus.eu/
- group: other
  title: ''
  type: DataStore
  url: https://data.marine.copernicus.eu/products
- group: other
  title: ''
  type: Registration
  url: https://data.marine.copernicus.eu/register
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/mercator-ocean
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/copernicus-marine-service
- group: company
  title: ''
  type: Blog
  url: https://marine.copernicus.eu/news
- group: commercial
  title: ''
  type: Pricing
  url: https://marine.copernicus.eu/access-data/
- group: commercial
  title: ''
  type: Plans
  url: plans/copernicus-marine-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/copernicus-marine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/copernicus-marine-finops.yml
created: '2026-06-13'
description: The EU Copernicus Marine Environment Monitoring Service (CMEMS), operated by Mercator Ocean International, provides free and open access to authoritative information on the state of the global ocean and European regional seas. The service delivers ocean physical and biogeochemical data through multiple APIs covering temperature, salinity, sea level, currents, sea ice, and marine ecosystem variables from satellite observations, in situ measurements, and numerical model reanalysis and forecast products. Data can be accessed programmatically via the Copernicus Marine Toolbox (Python API and CLI), the OGC-compliant Web Map Tile Service (WMTS) for visualization, and the Catalogue Service for the Web (CSW) for product discovery. All services require a free Copernicus Marine account, except the CSW which is fully open, and there are no data volume quotas or download limits.
finops:
- name: Copernicus Marine Finops
  service_category: ''
  slug: copernicus-marine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/copernicus-marine.png
jsonld:
- class_count: 0
  name: Copernicus Marine Context
  property_count: 0
  slug: copernicus-marine
layout: provider
modified: '2026-06-13'
name: Copernicus Marine
nav: Providers
network: true
overview: 'Copernicus Marine publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Ocean, Marine, Oceanography, Sea Level, and Temperature.


  The Copernicus Marine catalog on APIs.io includes 1 JSON-LD context.


  Copernicus Marine''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Copernicus Marine Plans
  plan_count: 1
  slug: copernicus-marine-plans
random_paper: 70
rate_limits:
- limit_count: 0
  name: Copernicus Marine Rate Limits
  slug: copernicus-marine-rate-limits
score:
  band: emerging
  composite: 20.2
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/copernicus-marine/refs/heads/main/screenshots/copernicus-marine-2026-06-20T175018.png
security:
- kind: domain-security
  name: Copernicus Marine Domain Security
  slug: copernicus-marine-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: copernicus-marine
tags:
- Ocean
- Marine
- Oceanography
- Sea Level
- Temperature
- Salinity
- Currents
- Biogeochemistry
- Climate
- Environment
- Satellite
- Forecast
- Reanalysis
- Open Data
- EU
website: https://marine.copernicus.eu/
---
