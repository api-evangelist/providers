---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Noaa Gov Agentic Access
  operation_count: 66
  slug: noaa-gov-agentic-access
  summary_line: 66 operations
api_count: 24
apis:
- description: SWPC publishes solar wind, geomagnetic, X-ray flux, aurora forecast, radiation storm, and coronal mass ejection products through a static-file data service organised by format. JSON, text, and image f
  name: Space Weather Prediction Center (SWPC) Data Service
  slug: swpc-data-service
- description: The Center for Operational Oceanographic Products and Services (CO-OPS) Data API returns water-level observations, tide predictions, currents, meteorological observations, and operational forecast mod
  name: CO-OPS Data Retrieval API (Tides & Currents)
  slug: co-ops-data-api
- description: The CO-OPS Metadata API exposes station inventory, harmonic constituents, NOS PORTS station lists, flood thresholds, and high/low water station catalogs. Supports radius and bounding-box station disco
  name: CO-OPS Metadata API (MDAPI v1)
  slug: co-ops-metadata-api
- description: Derived products computed from historical CO-OPS water-level records — sea level trends, annual mean sea level reports, top-10 water levels, and extreme event summaries — exposed as a machine-readable
  name: CO-OPS Derived Product API (DPAPI v0.1)
  slug: co-ops-derived-product-api
- description: The National Centers for Environmental Information (NCEI) Access Data Service is the modern, token-free replacement for the legacy CDO web service. It exposes daily summaries (GHCND), hourly summaries
  name: NCEI Access Data Service (v1)
  slug: ncei-access-data-service
- description: The legacy Climate Data Online v2 REST API exposes datasets, datatypes, stations, locations, data categories, and observation records. Requires a free token from ncei.noaa.gov/cdo-web/token in the `to
  name: NCEI Climate Data Online (CDO) v2 API
  slug: ncei-cdo-v2-api
- description: NDBC publishes real-time meteorological and oceanographic observations (the last 45 days) and historical archives from a global network of over 900 moored buoys, drifting buoys, C-MAN coastal stations
  name: National Data Buoy Center (NDBC) Web Data Service
  slug: ndbc-data-service
- description: ERDDAP (Environmental Research Division Data Access Program) is a NOAA-funded, open-source server that unifies access to gridded (`griddap`) and tabular (`tabledap`) scientific datasets across OPeNDAP
  name: NOAA CoastWatch ERDDAP Server
  slug: erddap-coastwatch
- description: NODD is NOAA's bulk-data dissemination program, providing free, low-latency public access to tens of terabytes per day of forecast model output, satellite imagery, radar, and observation archives thro
  name: NOAA Open Data Dissemination (NODD)
  slug: nodd-open-data
- description: The Fisheries One Stop Shop (FOSS) Operational Data Store, hosted on Oracle REST Data Services (ORDS), exposes US commercial fisheries landings, foreign trade, fishing gear, and species reference data
  name: NOAA Fisheries One Stop Shop (FOSS) ODS / ORDS
  slug: foss-landings-api
- description: InPort is the authoritative metadata repository for NOAA Fisheries and the National Ocean Service and the NOAA-wide platform for data management plans. Catalog records describe data products, services
  name: NOAA InPort Metadata Catalog
  slug: inport-metadata-api
- description: The Alerts API from NOAA — National Oceanic and Atmospheric Administration — 8 operation(s) for alerts.
  name: NOAA — National Oceanic and Atmospheric Administration Alerts API
  slug: noaa-gov-alerts-api
- description: The Aviation API from NOAA — National Oceanic and Atmospheric Administration — 7 operation(s) for aviation.
  name: NOAA — National Oceanic and Atmospheric Administration Aviation API
  slug: noaa-gov-aviation-api
- description: The Glossary API from NOAA — National Oceanic and Atmospheric Administration — 1 operation(s) for glossary.
  name: NOAA — National Oceanic and Atmospheric Administration Glossary API
  slug: noaa-gov-glossary-api
- description: The Gridpoints API from NOAA — National Oceanic and Atmospheric Administration — 4 operation(s) for gridpoints.
  name: NOAA — National Oceanic and Atmospheric Administration Gridpoints API
  slug: noaa-gov-gridpoints-api
- description: The Icons API from NOAA — National Oceanic and Atmospheric Administration — 3 operation(s) for icons.
  name: NOAA — National Oceanic and Atmospheric Administration Icons API
  slug: noaa-gov-icons-api
- description: The Offices API from NOAA — National Oceanic and Atmospheric Administration — 8 operation(s) for offices.
  name: NOAA — National Oceanic and Atmospheric Administration Offices API
  slug: noaa-gov-offices-api
- description: The Points API from NOAA — National Oceanic and Atmospheric Administration — 3 operation(s) for points.
  name: NOAA — National Oceanic and Atmospheric Administration Points API
  slug: noaa-gov-points-api
- description: The Products API from NOAA — National Oceanic and Atmospheric Administration — 9 operation(s) for products.
  name: NOAA — National Oceanic and Atmospheric Administration Products API
  slug: noaa-gov-products-api
- description: The Radar API from NOAA — National Oceanic and Atmospheric Administration — 8 operation(s) for radar.
  name: NOAA — National Oceanic and Atmospheric Administration Radar API
  slug: noaa-gov-radar-api
- description: The Radio API from NOAA — National Oceanic and Atmospheric Administration — 1 operation(s) for radio.
  name: NOAA — National Oceanic and Atmospheric Administration Radio API
  slug: noaa-gov-radio-api
- description: The Stations API from NOAA — National Oceanic and Atmospheric Administration — 7 operation(s) for stations.
  name: NOAA — National Oceanic and Atmospheric Administration Stations API
  slug: noaa-gov-stations-api
- description: The Thumbnails API from NOAA — National Oceanic and Atmospheric Administration — 1 operation(s) for thumbnails.
  name: NOAA — National Oceanic and Atmospheric Administration Thumbnails API
  slug: noaa-gov-thumbnails-api
- description: The Zones API from NOAA — National Oceanic and Atmospheric Administration — 6 operation(s) for zones.
  name: NOAA — National Oceanic and Atmospheric Administration Zones API
  slug: noaa-gov-zones-api
artifact_total: 46
collections:
- collection_type: open
  name: weather.gov API
  slug: open-weather-gov-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/noaa-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noaa-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/noaa-gov-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.noaa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.noaa.gov/organization
- group: docs
  title: ''
  type: Documentation
  url: https://www.noaa.gov/information-technology/open-data-dissemination
- group: docs
  title: ''
  type: Documentation
  url: https://catalog.data.gov/organization/noaa-gov
- group: start
  title: ''
  type: Portal
  url: https://data.noaa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.noaa.gov/foia
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.noaa.gov/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.noaa.gov/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.noaa.gov/news
- group: company
  title: ''
  type: Blog
  url: https://www.weather.gov/news
- group: company
  title: ''
  type: Blog
  url: https://www.swpc.noaa.gov/news
- group: operate
  title: ''
  type: Support
  url: https://www.weather.gov/contact
- group: operate
  title: ''
  type: Support
  url: https://www.ncei.noaa.gov/contact
- group: docs
  title: ''
  type: Documentation
  url: https://www.noaa.gov/jobs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAA-EMC
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAA-GFDL
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAA-GSL
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAA-OWP
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAA-PSL
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAA-PMEL
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAAGFDL
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weather-gov
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/weather-gov/api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/weather-gov/weather.gov
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/NOAA-EMC/global-workflow
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/NOAA-GSL/Rocoto
- group: docs
  title: ''
  type: Documentation
  url: https://www.weather.gov/sti/
- group: docs
  title: ''
  type: Documentation
  url: https://www.weather.gov/about/who-we-are
- group: start
  title: ''
  type: Portal
  url: https://www.nesdis.noaa.gov/
- group: start
  title: ''
  type: Portal
  url: https://oceanservice.noaa.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.fisheries.noaa.gov/
- group: start
  title: ''
  type: Portal
  url: https://research.noaa.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.omao.noaa.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.ncei.noaa.gov/
- group: other
  title: ''
  type: BaseURL
  url: https://www.ncei.noaa.gov/erddap/
- group: design
  title: ''
  type: JSONLD
  url: https://json-ld/noaa-gov-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://vocabulary/noaa-gov-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://rate-limits/noaa-gov-rate-limits.yml
created: '2026-05-25'
description: The National Oceanic and Atmospheric Administration (NOAA) is the United States scientific and regulatory agency within the Department of Commerce charged with monitoring oceanic and atmospheric conditions, charting the seas, conducting deep-sea exploration, managing fishing and protection of marine mammals, and providing weather, climate, space weather, and ecosystem forecasts and warnings. NOAA's developer surface spans six line offices — the National Weather Service (NWS), the National Environmental Satellite, Data, and Information Service (NESDIS) including the National Centers for Environmental Information (NCEI), the National Ocean Service (NOS) including Tides & Currents (CO-OPS), the National Marine Fisheries Service (NMFS / NOAA Fisheries), the Office of Oceanic and Atmospheric Research (OAR), and the Office of Marine and Aviation Operations (OMAO). NOAA exposes free, open APIs at api.weather.gov, services.swpc.noaa.gov, api.tidesandcurrents.noaa.gov, ncei.noaa.gov/access,
  ERDDAP servers across line offices, the National Data Buoy Center (NDBC), and bulk forecast model output (GFS, GEFS, HRRR, GOES) through the NOAA Open Data Dissemination (NODD) program on AWS, GCP, and Azure.
features:
- Free and open weather, climate, ocean, fisheries, and space-weather APIs — no payment required and most endpoints require no API key
- National Weather Service api.weather.gov — alerts (CAP), gridded forecasts, observations, aviation (SIGMETs/AIRMETs/TAFs), radar, zones, points, glossary — 66 documented endpoints in OpenAPI 3.9.2
- GeoJSON, JSON-LD, CAP, ATOM, and DWML response formats via content negotiation on NWS API
- Space Weather Prediction Center JSON, text, and image feeds for solar wind, geomagnetic, X-ray flux, aurora, and CME products at services.swpc.noaa.gov
- CO-OPS Tides & Currents — data, metadata, and derived-product APIs covering 200+ coastal, Great Lakes, and territorial stations with selectable datums and units
- NCEI Access Data Service v1 — token-free climate data access (GHCND, hourly/monthly summaries, normals, SST archives) in CSV, JSON, NetCDF
- NCEI CDO v2 — token-based legacy climate API with 5 req/sec, 10k req/day rate limits
- National Data Buoy Center (NDBC) — 900+ buoys and coastal stations with real-time + historical oceanographic and meteorological observations via HTTP, THREDDS, and OGC API Features
- ERDDAP servers across CoastWatch, NCEI, IOOS, and line offices — unified gridded/tabular access via griddap and tabledap REST endpoints
- NOAA Open Data Dissemination (NODD) — GFS, GEFS, HRRR, RAP, NAM, RRFS, GraphCast, GOES, NEXRAD on AWS, GCP, and Azure (S3/GCS/Azure Blob)
- NOAA Fisheries FOSS Landings — Oracle REST Data Services exposing commercial landings, foreign trade, gear, and species data
- InPort metadata catalog — authoritative data inventory for NOAA Fisheries and NOS, beta API for machine-to-machine catalog access
- User-Agent header required on api.weather.gov for identification and security contact
- Hundreds of NOAA GitHub orgs (NOAA-EMC, NOAA-GFDL, NOAA-GSL, NOAA-OWP, NOAA-PMEL, NOAA-PSL, weather-gov) publishing forecast model code, workflow systems, scientific libraries, and tools
image: https://www.noaa.gov/themes/custom/noaa_components/logo.svg
json_schemas:
- name: NWS Alert
  property_count: 4
  slug: noaa-gov-alert
jsonld:
- class_count: 51
  name: Noaa Gov Context
  property_count: 3
  slug: noaa-gov-context
layout: provider
modified: '2026-05-25'
name: NOAA — National Oceanic and Atmospheric Administration
nav: Providers
network: true
overview: 'NOAA — National Oceanic and Atmospheric Administration publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Aviation API, Glossary API, and 10 more. Tagged areas include Weather, Climate, Ocean, Space Weather, and Government.


  The NOAA — National Oceanic and Atmospheric Administration catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NOAA — National Oceanic and Atmospheric Administration''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 36 more developer resources.'
random_paper: 96
rate_limits:
- limit_count: 0
  name: Noaa Gov Rate Limits
  slug: noaa-gov-rate-limits
rules:
- name: NOAA — National Oceanic and Atmospheric Administration API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: noaa-gov-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.6
  delta: -0.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 57.6
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Noaa Gov Authentication
  slug: noaa-gov-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Noaa Gov Domain Security
  slug: noaa-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: noaa-gov
tags:
- Weather
- Climate
- Ocean
- Space Weather
- Government
- Open Data
- Forecast
- Marine
- Atmospheric
- Hydrology
- Satellite
- Fisheries
- Aviation
- Emergency Management
website: https://www.noaa.gov/
---
