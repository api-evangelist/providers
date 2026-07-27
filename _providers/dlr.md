---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dlr Agentic Access
  operation_count: 13
  slug: dlr-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 10
apis:
- description: OGC Web Map Service providing visualization layers for DLR Earth observation imagery products including optical satellite data, hyperspectral imagery, and derived remote sensing products.
  name: EOC Imagery Web Map Service (WMS)
  slug: eoc-imagery-web-map-service-wms
- description: OGC Web Coverage Service providing direct download and extraction of coverage data for DLR Earth observation imagery products, supporting data subsetting and retrieval in scientific formats.
  name: EOC Imagery Web Coverage Service (WCS)
  slug: eoc-imagery-web-coverage-service-wcs
- description: OGC Web Map Service providing basemap and core geospatial reference layers from DLR including global mosaics and topographic reference data derived from DLR satellite missions.
  name: EOC Basemap Web Map Service (WMS)
  slug: eoc-basemap-web-map-service-wms
- description: OGC Web Coverage Service for DLR basemap and reference datasets including the SRTM X-SAR global digital elevation model mosaic, providing programmatic access to raw coverage data.
  name: EOC Basemap Web Coverage Service (WCS)
  slug: eoc-basemap-web-coverage-service-wcs
- description: OGC Web Map Service providing land cover and land use visualization layers from DLR research, including World Settlement Footprint, crop type mapping, forest structure, CORINE land cover, and urbaniza
  name: EOC Land Web Map Service (WMS)
  slug: eoc-land-web-map-service-wms
- description: OGC Web Map Service providing atmospheric data visualization layers from DLR including Sentinel-5P TROPOMI products for ozone, nitrogen dioxide, sulfur dioxide, formaldehyde, and cloud fraction.
  name: EOC Atmosphere Web Map Service (WMS)
  slug: eoc-atmosphere-web-map-service-wms
- description: 'Multi-mission web portal API for interactive access to the DLR Earth observation data holdings including browse-and-download features, time-series data access, OGC WMS/WFS/WMTS/TMS browsing services, '
  name: EOWEB GeoPortal API
  slug: eoweb-geoportal-api
- description: essential characteristics of this API
  name: DLR Capabilities API
  slug: dlr-capabilities-api
- description: access to data (features)
  name: DLR Data API
  slug: dlr-data-api
- description: The STAC API from DLR — 1 operation(s) for stac.
  name: DLR STAC API
  slug: dlr-stac-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dlr-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dlr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dlr-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://geoservice.dlr.de/web/
- group: other
  title: ''
  type: DataCatalog
  url: https://geoservice.dlr.de/data-assets/
- group: other
  title: ''
  type: DataAccess
  url: https://www.dlr.de/en/eoc/research-transfer/topics/satellite-data/data-access
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dlr-eoc
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/dlr/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/dlr/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/dlr/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eoweb.dlr.de/egp/resources/context/Login
- group: operate
  title: ''
  type: Contact
  url: https://www.dlr.de/en/eoc/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dlr.de/en/privacy-policy
created: '2026-06-13'
description: The German Aerospace Center (DLR) Earth Observation Center (EOC) provides public APIs for accessing Earth observation satellite data, remote sensing products, and scientific datasets from German aerospace research missions. Services include OGC-compliant WMS, WCS, CSW, STAC, and WMTS endpoints covering atmospheric trace gases, digital elevation models, land cover, hyperspectral imagery, water resources, and more from missions such as TanDEM-X, TerraSAR-X, EnMAP, DESIS, and Sentinel series.
examples:
- key_count: 3
  name: Stac Collection Response
  slug: stac-collection-response
- key_count: 6
  name: Stac Search Request
  slug: stac-search-request
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.dlr.de/favicon.ico
json_schemas:
- name: DLR EOC STAC API Schema
  property_count: 3
  slug: eoc-stac-api
jsonld:
- class_count: 20
  name: Eoc Stac Api Context
  property_count: 17
  slug: eoc-stac-api
layout: provider
modified: '2026-06-13'
name: DLR
nav: Providers
network: true
overview: 'DLR publishes 3 APIs on the [APIs.io](https://apis.io/) network: Capabilities API, Data API, and STAC API. Tagged areas include Earth Observation, Remote Sensing, Satellite Data, Geospatial, and Aerospace.


  The DLR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DLR''s developer surface includes developer portal, GitHub presence, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 50
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: DLR API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: dlr-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.5
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 49.8
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dlr/refs/heads/main/screenshots/dlr-2026-06-20T180058.png
security:
- kind: domain-security
  name: Dlr Domain Security
  slug: dlr-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dlr Vulnerability Disclosure
  slug: dlr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dlr
tags:
- Earth Observation
- Remote Sensing
- Satellite Data
- Geospatial
- Aerospace
- Open Data
- OGC
- STAC
- Atmospheric Science
- Digital Elevation Models
website: https://geoservice.dlr.de/web/
---
