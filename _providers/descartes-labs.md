---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-09-02'
api_count: 6
apis:
- description: The historical Descartes Labs Platform — a managed geospatial data refinery and analytics environment exposing imagery catalog, raster access, vector tables, compute functions, and authentication thro
  name: Descartes Labs Platform (Archived)
  slug: descartes-labs-platform
- description: The Catalog organised all imagery and derived data on the Platform. Products group Bands which group Images; Storage Blobs hold arbitrary file artefacts; Events emit notifications when new images, blo
  name: Descartes Labs Catalog API
  slug: catalog
- description: 'The Compute service ran user-supplied Python code as containerised Functions against the imagery archive at scale. Users defined a `Function` (CPUs, memory, environment, Docker image), submitted Jobs '
  name: Descartes Labs Compute API
  slug: compute
- description: 'The Vector service hosted tabular and geospatial feature data as Tables of typed columns with `uuid` identifiers and ipyleaflet visualisation. Supported property filtering (including `ilike` wildcard '
  name: Descartes Labs Vector API
  slug: vector
- description: Dynamic Compute was the Platform's lazy map-computation engine for interactive raster algebra and tile rendering in notebooks. Expressions over imagery products (band math, mosaicking, temporal compos
  name: Descartes Labs Dynamic Compute API
  slug: dynamic-compute
- description: The Auth module handled token-based authentication against app.descarteslabs.com — OAuth login flow, refresh tokens, and the user namespace claim that served as a global identifier for the authenticat
  name: Descartes Labs Auth API
  slug: auth
artifact_total: 22
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/dlarchives/descarteslabs-python/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/descartes-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.descarteslabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.descarteslabs.com
- group: operate
  title: ''
  type: Support
  url: https://support.descarteslabs.com
- group: start
  title: ''
  type: Login
  url: https://app.descarteslabs.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dlarchives
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlarchives/descarteslabs-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlarchives/descarteslabs-dynamic-compute
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlarchives/descarteslabs-vector
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dlarchives/tutorials
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dlarchives/example-notebooks
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dlarchives/workflows-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dlarchives/descarteslabs-ea-notebooks
- group: other
  title: ''
  type: Dataset
  url: https://github.com/dlarchives/DL-COVID-19
- group: other
  title: ''
  type: Research
  url: https://github.com/dlarchives/contrastive_sensor_fusion
- group: build
  title: ''
  type: PythonPackage
  url: https://pypi.org/project/descarteslabs/
- group: build
  title: ''
  type: PythonPackage
  url: https://pypi.org/project/descarteslabs-dynamic-compute/
- group: other
  title: ''
  type: Successor
  url: https://github.com/earthdaily/earthone-python
- group: other
  title: ''
  type: Successor
  url: https://earthdaily.com
- group: other
  title: ''
  type: Acquisition
  url: https://earthdaily.com/blog/descartes-labs-acquisition
- group: other
  title: ''
  type: Acquisition
  url: https://www.prnewswire.com/news-releases/earthdaily-analytics-announces-acquisition-of-descartes-labs-302276388.html
created: '2026-05-24'
description: Descartes Labs was a Santa Fe, New Mexico geospatial intelligence company founded in 2014 as a spin-out from Los Alamos National Laboratory. The company built the Descartes Labs Platform, a cloud-native geospatial data refinery and analytics environment combining a petabyte-scale satellite imagery archive (Landsat, Sentinel-1/2, MODIS, NAIP, PlanetScope, SkySat, commercial radar, NEXRAD weather radar, plus client-uploaded data) with a Python client library, JupyterHub-based workbench, and distributed compute for training and running deep learning and remote-sensing models at scale. Customers in agriculture, mining, energy, defense, insurance, and the U.S. government used the platform to build production geospatial machine learning pipelines covering crop forecasting, mineral exploration, infrastructure monitoring, methane detection, wildfire response, and ESG reporting. The Platform exposed a Catalog (imagery, bands, products, blobs, events), a Compute service (containerised
  functions, jobs, schedules), a Vector service (tabular and geospatial features), Dynamic Compute (lazy raster algebra and tiling), Auth, and a `descarteslabs` CLI. In October 2024, EarthDaily Analytics — backed by Antarctica Capital — acquired Descartes Labs and the Descartes Labs Government, Inc. subsidiary, folding the team, customers, and platform into the EarthDaily Constellation programme. The product was rebranded EarthOne in 2025; the `descarteslabs` Python package has been formally discontinued in favour of `earthdaily-earthone` (v5.x), the github.com/descarteslabs organisation has been renamed to `dlarchives`, www.descarteslabs.com is now a parked domain, and the docs.descarteslabs.com developer portal has been retired in favour of EarthDaily-hosted EarthOne documentation. This catalog entry preserves the historical Descartes Labs Platform surface as an archive — see the EarthDaily / EarthOne profile for the active product.
features:
- Cloud-native geospatial data refinery built on a petabyte-scale satellite imagery archive
- Native ingest and time-aligned access to Landsat, Sentinel-1, Sentinel-2, MODIS, NAIP, PlanetScope, SkySat, commercial radar, and NEXRAD
- Catalog service organising Products, Bands, Images, Storage Blobs, Events, and EventSchedules
- Event-driven processing — NewImage / NewStorage / NewVector / compute-function-completed subscriptions delivered to SQS or Compute Functions
- Compute service for containerised Python Functions, Jobs, and bulk `Function.map` submissions over the imagery archive
- Vector service for tabular and geospatial feature tables with property filtering, `ilike` wildcards, and ipyleaflet visualisation
- Dynamic Compute engine for lazy raster algebra and on-demand XYZ tile rendering in notebooks
- JupyterHub-based workbench on app.descarteslabs.com for in-browser notebook authoring
- Python client `descarteslabs` (PyPI) with auth, catalog, compute, config, core, geo, and vector subpackages
- '`descarteslabs` CLI for managing Products, Bands, Blobs, and sharing from the command line'
- Sharing model with owners / writers / readers and AuthCatalogObject permission helpers
- DL-COVID-19 mobility dataset and Contrastive Sensor Fusion research releases
- Enterprise customers across agriculture, mining, energy, defense, insurance, and U.S. government
- Descartes Labs Government, Inc. subsidiary for U.S. federal workloads
- Discontinued in 2025 and superseded by EarthDaily EarthOne (`earthdaily-earthone` 5.x) following the October 2024 acquisition
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/descartes-labs.png
layout: provider
modified: '2026-05-24'
name: Descartes Labs
nav: Providers
network: true
overview: 'Descartes Labs publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, Geospatial Intelligence, Earth Observation, Satellite Imagery, and Remote Sensing.


  Descartes Labs'' developer surface includes documentation, support, code examples, and 19 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/descartes-labs/refs/heads/main/screenshots/descartes-labs-2026-07-25T211750.png
security:
- kind: domain-security
  name: Descartes Labs Domain Security
  slug: descartes-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: descartes-labs
tags:
- Geospatial
- Geospatial Intelligence
- Earth Observation
- Satellite Imagery
- Remote Sensing
- Raster
- Vectors
- GIS
- Machine-Learning
- Geospatial Analytics
- Agriculture
- Mining
- Energy
- Defense
- Climate
- Acquired
- EarthOne
- EarthDaily
- Discontinued
website: https://www.descarteslabs.com
---
