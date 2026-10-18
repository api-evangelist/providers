---
access_model:
  confidence: medium
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Airbus Agentic Access
  operation_count: 2
  slug: airbus-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
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
- baseURL: https://authenticate.foundation.api.oneatlas.airbus.com
  baseurl_source: spec
  description: The Authentication API from Airbus — 1 operation(s) for authentication.
  name: Airbus Authentication API
  slug: airbus-authentication-api
- baseURL: https://authenticate.foundation.api.oneatlas.airbus.com
  baseurl_source: spec
  description: The Catalog API from Airbus — 1 operation(s) for catalog.
  name: Airbus Catalog API
  slug: airbus-catalog-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Airbus OneAtlas API () Authentication API
  slug: open-airbus-authentication-api
- collection_type: open
  name: Airbus OneAtlas API () Authentication Catalog API
  slug: open-airbus-catalog-api
- collection_type: open
  name: Airbus OneAtlas API (Authentication)
  slug: open-airbus
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airbus/refs/heads/main/plans/airbus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airbus-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airbus/refs/heads/main/rate-limits/airbus-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airbus-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airbus/refs/heads/main/finops/airbus-finops.yml
  title: ''
  type: FinOps
  url: finops/airbus-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.airbus.com/en/rss.xml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airbus/refs/heads/main/agentic-access/airbus-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airbus-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airbus/refs/heads/main/security/airbus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/airbus-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airbus/refs/heads/main/security/airbus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airbus-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airbus/refs/heads/main/authentication/airbus-authentication.yml
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
- has_sources: true
  method: generated
  name: Airbus Finops
  primary_unit: ''
  service_category: Earth Observation / Satellite Imagery
  slug: airbus-finops
  template: false
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
modified: '2026-10-06'
name: Airbus
nav: Providers
network: true
overview: 'Airbus publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Catalog API, and 5 more. Tagged areas include Aerospace, Defense, Manufacturing, Aviation, and Earth Observation.


  Airbus'' developer surface includes authentication, developer portal, and 12 more developer resources.'
plans:
- name: Airbus Plans Pricing
  plan_count: 4
  slug: airbus-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Airbus Rate Limits
  slug: airbus-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.2
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 26.3
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
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
- Remote Sensing
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
