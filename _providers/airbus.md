---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Airbus Agentic Access
  operation_count: 2
  slug: airbus-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 7
apis:
- description: Subscription-based catalogue access to Airbus Living Library Pléiades, Pléiades Neo, and SPOT optical imagery for AOI search, preview, and streaming.
  name: OneAtlas Living Library API
  slug: oneatlas-living-library
- description: On-demand purchase of historical archive imagery from Airbus optical and radar constellations on a pay-per-order basis.
  name: OneAtlas Pay-Per-Order Archives API
  slug: oneatlas-pay-per-order-archives
- description: On-demand satellite tasking for new imagery acquisitions over a user-defined area of interest, with priority and acquisition-window options.
  name: OneAtlas Pay-Per-Order Tasking API
  slug: oneatlas-pay-per-order-tasking
- description: Global high-resolution basemap tile service derived from Airbus optical imagery, suitable for embedding in GIS and web mapping applications.
  name: OneAtlas Basemap API
  slug: oneatlas-basemap
- description: Access to Airbus radar (SAR) imagery and elevation products including WorldDEM, suitable for change detection, surveillance, and terrain analysis.
  name: OneAtlas Radar & Elevation API
  slug: oneatlas-radar-elevation
- description: The Authentication API from Airbus — 1 operation(s) for authentication.
  name: Airbus Authentication API
  slug: airbus-authentication-api
- description: The Catalog API from Airbus — 1 operation(s) for catalog.
  name: Airbus Catalog API
  slug: airbus-catalog-api
artifact_total: 30
collections:
- collection_type: open
  name: Airbus OneAtlas API (Authentication)
  slug: open-airbus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airbus-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airbus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airbus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airbus-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airbus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airbusgroup
- group: company
  title: ''
  type: Website
  url: https://www.airbus.com/
- group: start
  title: ''
  type: Portal
  url: https://api.oneatlas.airbus.com/
- group: other
  title: ''
  type: AccountManagement
  url: https://account.foundation.oneatlas.airbus.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.oneatlas.airbus.com/
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: A European multinational aerospace corporation designing, manufacturing, and selling commercial aircraft, helicopters, defense, and space products. Through its Space Solutions / OneAtlas division Airbus publishes a developer API portal for satellite imagery, mapping, and elevation data.
features:
- description: Access to Pléiades, Pléiades Neo, and SPOT optical imagery via the Living Library catalogue and archive ordering.
  name: Optical Imagery
- description: SAR imagery from the TerraSAR-X / TanDEM-X constellation and from the new Radar Constellation.
  name: Radar Imagery
- description: Pay-per-order tasking for new imagery acquisitions over a user-defined AOI.
  name: Satellite Tasking
- description: Global elevation models including WorldDEM derived from Airbus radar interferometry.
  name: Elevation Products
- description: High-resolution global basemap tile service for embedding in GIS and web maps.
  name: Basemap Tile Service
- description: Authentication via per-user API key issued by the OneAtlas account portal with OAuth 2.0 access-token exchange.
  name: API Key + OAuth 2.0
finops:
- name: Airbus Finops
  service_category: Earth Observation / Satellite Imagery
  slug: airbus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airbus.png
integrations:
- description: Esri ArcGIS integrations for streaming Airbus basemaps and imagery into the ArcGIS platform.
  name: ArcGIS
- description: QGIS plugins for connecting to Airbus tile and WMS / WMTS services.
  name: QGIS
- description: Airbus distributes selected imagery products through AWS Marketplace and Earth on AWS.
  name: AWS
- description: Aviation-data platform powered by Airbus and Palantir, exposed to airline operators via separate enterprise integration.
  name: Skywise
layout: provider
modified: '2026-05-16'
name: Airbus
nav: Providers
network: true
overview: 'Airbus publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Catalog API. Tagged areas include Aerospace, Defense, Manufacturing, Aviation, and Earth Observation.


  Airbus'' developer surface includes authentication, developer portal, and 8 more developer resources.'
plans:
- name: Airbus Plans Pricing
  plan_count: 4
  slug: airbus-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 3
  name: Airbus Rate Limits
  slug: airbus-rate-limits
score:
  band: thin
  composite: 41.8
  delta: -1.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airbus/refs/heads/main/screenshots/airbus-2026-06-20T171419.png
security:
- kind: authentication
  name: Airbus Authentication
  slug: airbus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airbus Domain Security
  slug: airbus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Airbus Vulnerability Disclosure
  slug: airbus-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: airbus
tags:
- Aerospace
- Defense
- Manufacturing
- Aviation
- Earth Observation
- Satellite Imagery
use_cases:
- description: Periodic optical imagery used to monitor land-use change, deforestation, agriculture, and urban expansion.
  name: Land-Use / Land-Cover Monitoring
- description: Tasking and archive ordering of high-resolution optical and SAR imagery for defense and intelligence customers.
  name: Defense & Intelligence
- description: Repeat radar acquisitions for monitoring pipelines, dams, mines, and other linear infrastructure.
  name: Infrastructure Monitoring
- description: Embedding the OneAtlas basemap into GIS workflows and web-mapping products.
  name: GIS Basemaps
- description: Rapid tasking and archive ordering after natural disasters to support response and recovery.
  name: Disaster Response
website: https://www.airbus.com/
---
