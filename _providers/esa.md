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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Esa Agentic Access
  operation_count: 18
  slug: esa-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 18
apis:
- description: 'OData-based catalogue interface for searching and downloading Copernicus Earth observation products from the Copernicus Data Space Ecosystem. Supports querying by spatial footprint, acquisition date, '
  name: Copernicus Data Space OData Catalogue API
  slug: copernicus-odata
- description: RESTful API interface providing access to various satellite imagery archives including raw data, rendered images, and statistical analysis without requiring local data downloads. Supports configurable
  name: Copernicus Sentinel Hub API
  slug: copernicus-sentinel-hub
- description: Standardised openEO interface enabling programmatic access and cloud processing of Earth observation datasets without local data management. Supports automatic scaling on cloud infrastructure. The fre
  name: Copernicus openEO API
  slug: copernicus-openeo
- description: OGC-compliant web services providing seamless satellite data access through standard GIS applications. Exposes WMS (Web Map Service), WMTS (Web Map Tile Service), WFS (Web Feature Service), and WCS (W
  name: Copernicus OGC API (WMS/WMTS/WFS/WCS)
  slug: copernicus-ogc
- description: Serverless computation service for generating higher-level products from archived lower-level Copernicus data using ESA processors. Supports single-item and batch processing workflows including CARD-B
  name: Copernicus On-Demand Processing (ODP) API
  slug: copernicus-on-demand-processing
- description: Heliophysics Application Programmer's Interface (HAPI) server providing access to ESA Space Weather Service Network data. Implements the COSPAR-recommended HAPI standard for streaming heliophysics tim
  name: ESA Space Weather HAPI Server
  slug: space-weather-hapi
- description: 'Table Access Protocol (TAP) service for the ESA Gaia stellar catalogue, the most precise astrometric survey of the Milky Way. Enables ADQL (Astronomical Data Query Language) queries against Gaia Data '
  name: ESA Gaia Archive TAP API
  slug: gaia-tap
- description: IVOA Table Access Protocol (TAP) service providing access to ESA legacy mission archives including Hipparcos (~118,000 stars with milliarcsecond accuracy, 42 data products across 59 tables), Cos-B gam
  name: ESASky Legacy TAP Service
  slug: esasky-legacy-tap
- description: GraphQL API for managing ESA Datalabs computational environments, data pipelines, data volumes, and user access controls. Provides 50+ query operations (datalab management, pipeline runs, user/role ma
  name: ESA Datalabs GraphQL API
  slug: datalabs-graphql
- description: Earth System Grid Federation (ESGF) RESTful API providing access to ESA Climate Change Initiative (CCI) observational products aligned with CMIP climate model data through the Obs4MIPs framework. Enab
  name: ESA CCI ESGF RESTful API
  slug: cci-esgf
- description: The Bulk Transaction Extension API from European Space Agency (ESA) — 1 operation(s) for bulk transaction extension.
  name: European Space Agency (ESA) Bulk Transaction Extension API
  slug: esa-bulk-transaction-extension-api
- description: The Collections API from European Space Agency (ESA) — 4 operation(s) for collections.
  name: European Space Agency (ESA) Collections API
  slug: esa-collections-api
- description: The Conformance API from European Space Agency (ESA) — 1 operation(s) for conformance.
  name: European Space Agency (ESA) Conformance API
  slug: esa-conformance-api
- description: The Copernicus Data Space Ecosystem (CDSE) Asset Level STAC Catalogue API from European Space Agency (ESA) — 1 operation(s) for copernicus data space ecosystem (cdse) asset level stac catalogue.
  name: European Space Agency (ESA) Copernicus Data Space Ecosystem (CDSE) Asset Level STAC Catalogue API
  slug: esa-copernicus-data-space-ecosystem-cdse-asset-level-stac-catalogue-api
- description: The Filter Extension API from European Space Agency (ESA) — 2 operation(s) for filter extension.
  name: European Space Agency (ESA) Filter Extension API
  slug: esa-filter-extension-api
- description: The Liveliness/Readiness API from European Space Agency (ESA) — 1 operation(s) for liveliness/readiness.
  name: European Space Agency (ESA) Liveliness/Readiness API
  slug: esa-liveliness-readiness-api
- description: The Search API from European Space Agency (ESA) — 1 operation(s) for search.
  name: European Space Agency (ESA) Search API
  slug: esa-search-api
- description: The Transaction Extension API from European Space Agency (ESA) — 4 operation(s) for transaction extension.
  name: European Space Agency (ESA) Transaction Extension API
  slug: esa-transaction-extension-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Copernicus Data Space Ecosystem (CDSE) asset-level STAC catalogue Bulk Transaction Extension API
  slug: open-esa-bulk-transaction-extension-api
- collection_type: open
  name: Copernicus Data Space Ecosystem (CDSE) asset-level STAC catalogue Bulk Transaction Extension Collections API
  slug: open-esa-collections-api
- collection_type: open
  name: Copernicus Data Space Ecosystem (CDSE) asset-level STAC catalogue Bulk Transaction Extension Conformance API
  slug: open-esa-conformance-api
- collection_type: open
  name: Copernicus Data Space Ecosystem (CDSE) asset-level STAC catalogue Bulk Transaction Extension Copernicus Data Space Ecosystem (CDSE) Asset Level STAC Catalogue API
  slug: open-esa-copernicus-data-space-ecosystem-cdse-asset-level-stac-catalogue-api
- collection_type: open
  name: Copernicus Data Space Ecosystem (CDSE) asset-level STAC catalogue Bulk Transaction Extension Filter Extension API
  slug: open-esa-filter-extension-api
- collection_type: open
  name: Copernicus Data Space Ecosystem (CDSE) asset-level STAC catalogue Bulk Transaction Extension Liveliness/Readiness API
  slug: open-esa-liveliness-readiness-api
- collection_type: open
  name: Copernicus Data Space Ecosystem (CDSE) asset-level STAC catalogue Bulk Transaction Extension Search API
  slug: open-esa-search-api
- collection_type: open
  name: Copernicus Data Space Ecosystem (CDSE) asset-level STAC catalogue Bulk Transaction Extension API
  slug: open-esa-transaction-extension-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/esa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/esa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.esa.int/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.dataspace.copernicus.eu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/esa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/european-space-agency
- group: commercial
  title: ''
  type: Plans
  url: plans/esa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/esa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/esa-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/esa-context.jsonld
- group: docs
  title: ''
  type: GraphQL
  url: graphql/esa-graphql.md
- group: company
  title: ''
  type: Blog
  url: https://www.esa.int/rssfeed/Our_Activities/Space_News
created: '2026-06-13'
description: The European Space Agency (ESA) provides public REST and standards-based APIs spanning Copernicus Earth observation (OData, STAC, Sentinel Hub, openEO, OGC, S3, On-Demand Processing), space weather monitoring (HAPI), astronomical mission archives (Gaia TAP, ESASky Legacy TAP), scientific data labs (Datalabs GraphQL), and climate change initiative datasets (ESGF, THREDDS, OpenSearch). Data includes Sentinel satellite imagery, solar and heliospheric time-series, gamma-ray and stellar catalogues, and multi-mission Earth observation products from European space programs.
finops:
- name: Esa Finops
  service_category: Earth Observation / Space Science
  slug: esa-finops
graphqls:
- description: European Space Agency (ESA) Datalabs GraphQL API
  name: ESA Datalabs GraphQL API
  slug: esa-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/esa.png
jsonld:
- class_count: 22
  name: Esa Context
  property_count: 0
  slug: esa-context
layout: provider
modified: '2026-06-13'
name: European Space Agency (ESA)
nav: Providers
network: true
overview: 'European Space Agency (ESA) publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bulk Transaction Extension API, Collections API, Conformance API, and 5 more. Tagged areas include Earth Observation, Copernicus, Sentinel, Space Weather, and Astronomy.


  The European Space Agency (ESA) catalog on APIs.io includes 1 JSON-LD context.


  European Space Agency (ESA)''s developer surface includes documentation, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Esa Plans Pricing
  plan_count: 2
  slug: esa-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 9
  name: Esa Rate Limits
  slug: esa-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 59.6
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/esa/refs/heads/main/screenshots/esa-2026-06-20T180819.png
security:
- kind: domain-security
  name: Esa Domain Security
  slug: esa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: esa
tags:
- Earth Observation
- Copernicus
- Sentinel
- Space Weather
- Astronomy
- Satellite Data
- Climate
- Geospatial
- STAC
- OData
website: https://www.esa.int/
---
