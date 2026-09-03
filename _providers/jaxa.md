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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 20.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Jaxa Agentic Access
  operation_count: 3
  slug: jaxa-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: 'Provides access to over 100 Earth observation satellite datasets from JAXA missions including ALOS, GCOM-C, and GCOM-W. Delivers data in Cloud Optimized GeoTIFF (COG) format through a STAC-compatible '
  name: JAXA Earth API
  slug: jaxa-earth-api
- description: OGC-compliant web services for searching and accessing JAXA Earth observation satellite products from missions including GCOM-W (AMSR2), GCOM-C (SGLI), and GSMaP precipitation products. Provides Catal
  name: G-Portal Web API
  slug: g-portal-web-api
- description: Provides global satellite-based precipitation estimates through the Global Satellite Mapping of Precipitation (GSMaP) product. Delivers near-real-time and archive rainfall rate data at 0.1-degree reso
  name: GSMaP Global Rainfall Watch API
  slug: gsmap-global-rainfall-watch-api
- description: Online search and ordering system for ALOS and ALOS-2 synthetic aperture radar and optical observation data. Authorized users can search observation archives, review observation plans, and order stand
  name: ALOS User Interface Gateway 2 (AUIG2)
  slug: alos-user-interface-gateway-2-auig2
- description: Provides near-real-time and archive access to Himawari geostationary meteorological satellite imagery and derived products. Data accessible via FTP from the P-Tree (Public ftp/http-based data TREe) se
  name: JAXA Himawari P-Tree Data Service
  slug: jaxa-himawari-p-tree-data-service
- baseURL: https://data.earth.jaxa.jp/
  baseurl_source: declared
  description: Catalog Services for the Web - search satellite observation collections and granules
  name: JAXA CSW API
  slug: jaxa-csw-api
- baseURL: https://data.earth.jaxa.jp/
  baseurl_source: declared
  description: Web Coverage Service - retrieve raw coverage/raster data from satellite datasets
  name: JAXA WCS API
  slug: jaxa-wcs-api
- baseURL: https://data.earth.jaxa.jp/
  baseurl_source: declared
  description: Web Map Service - retrieve map imagery from satellite datasets
  name: JAXA WMS API
  slug: jaxa-wms-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: G-Portal Web CSW API
  slug: open-jaxa-csw-api
- collection_type: open
  name: G-Portal Web CSW WCS API
  slug: open-jaxa-wcs-api
- collection_type: open
  name: G-Portal Web CSW WMS API
  slug: open-jaxa-wms-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jaxa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jaxa-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://earth.jaxa.jp/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jaxa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://global.jaxa.jp/policy.html
- group: other
  title: ''
  type: IntellectualProperty
  url: https://global.jaxa.jp/about/ip_policy/index_e.html
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/jaxa/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/jaxa/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/jaxa/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Japan Aerospace Exploration Agency (JAXA) provides public APIs and data services for satellite Earth observation data, including GCOM/ALOS satellite imagery, global precipitation mapping, greenhouse gas monitoring, and scientific mission data from Japanese space programs.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jaxa.png
layout: provider
modified: '2026-06-13'
name: JAXA
nav: Providers
network: true
overview: 'JAXA publishes 3 APIs on the [APIs.io](https://apis.io/) network: CSW API, WCS API, and WMS API. Tagged areas include Space, Satellite, Earth Observation, Remote Sensing, and Geospatial.


  JAXA''s developer surface includes developer portal, GitHub presence, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 0
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jaxa/refs/heads/main/screenshots/jaxa-2026-06-20T183708.png
security:
- kind: domain-security
  name: Jaxa Domain Security
  slug: jaxa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jaxa
tags:
- Space
- Satellite
- Earth Observation
- Remote Sensing
- Geospatial
- Climate
- Environment
- Precipitation
- Greenhouse Gas
- Japan
website: https://earth.jaxa.jp/en/
---
