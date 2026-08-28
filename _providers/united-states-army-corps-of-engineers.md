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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: United States Army Corps Of Engineers Agentic Access
  operation_count: 20
  slug: united-states-army-corps-of-engineers-agentic-access
  summary_line: 20 operations · 3 acting
api_count: 10
apis:
- description: River basin information
  name: United States Army Corps of Engineers Basins API
  slug: united-states-army-corps-of-engineers-basins-api
- description: Browse available data in the CWMS catalog
  name: United States Army Corps of Engineers Catalog API
  slug: united-states-army-corps-of-engineers-catalog-api
- description: Forecast instances and specifications
  name: United States Army Corps of Engineers Forecasts API
  slug: united-states-army-corps-of-engineers-forecasts-api
- description: Location levels and stage-discharge relationships
  name: United States Army Corps of Engineers Levels API
  slug: united-states-army-corps-of-engineers-levels-api
- description: USACE location data including dams, reservoirs, streamgages, and sites
  name: United States Army Corps of Engineers Locations API
  slug: united-states-army-corps-of-engineers-locations-api
- description: Physical parameters and units
  name: United States Army Corps of Engineers Parameters API
  slug: united-states-army-corps-of-engineers-parameters-api
- description: USACE project management including locks, gates, turbines, and outlets
  name: United States Army Corps of Engineers Projects API
  slug: united-states-army-corps-of-engineers-projects-api
- description: Rating tables for converting between measured values
  name: United States Army Corps of Engineers Ratings API
  slug: united-states-army-corps-of-engineers-ratings-api
- description: Time series data retrieval and management
  name: United States Army Corps of Engineers Time Series API
  slug: united-states-army-corps-of-engineers-time-series-api
- description: API version information
  name: United States Army Corps of Engineers Version API
  slug: united-states-army-corps-of-engineers-version-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CWMS Data API
  slug: open-cwms-data-api
- collection_type: open
  name: CWMS Data Basins API
  slug: open-united-states-army-corps-of-engineers-basins-api
- collection_type: open
  name: CWMS Data Basins Catalog API
  slug: open-united-states-army-corps-of-engineers-catalog-api
- collection_type: open
  name: CWMS Data Basins Forecasts API
  slug: open-united-states-army-corps-of-engineers-forecasts-api
- collection_type: open
  name: CWMS Data Basins Levels API
  slug: open-united-states-army-corps-of-engineers-levels-api
- collection_type: open
  name: CWMS Data Basins Locations API
  slug: open-united-states-army-corps-of-engineers-locations-api
- collection_type: open
  name: CWMS Data Basins Parameters API
  slug: open-united-states-army-corps-of-engineers-parameters-api
- collection_type: open
  name: CWMS Data Basins Projects API
  slug: open-united-states-army-corps-of-engineers-projects-api
- collection_type: open
  name: CWMS Data Basins Ratings API
  slug: open-united-states-army-corps-of-engineers-ratings-api
- collection_type: open
  name: CWMS Data Basins Time Series API
  slug: open-united-states-army-corps-of-engineers-time-series-api
- collection_type: open
  name: CWMS Data Basins Version API
  slug: open-united-states-army-corps-of-engineers-version-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/USACE/cwms-data-api/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-states-army-corps-of-engineers-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-states-army-corps-of-engineers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-states-army-corps-of-engineers-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-army-corps-of-engineers
- group: company
  title: ''
  type: Website
  url: https://www.usace.army.mil/
- group: other
  title: ''
  type: OpenData
  url: https://www.usace.army.mil/open/
- group: other
  title: ''
  type: GeospatialData
  url: https://geospatial-usace.opendata.arcgis.com/
- group: other
  title: ''
  type: WaterData
  url: https://water.usace.army.mil/data
- group: build
  title: ''
  type: DigitalLibrary
  url: https://usace.contentdm.oclc.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/USACE
- group: other
  title: ''
  type: PermitsData
  url: https://permits.ops.usace.army.mil/
created: '2024-12-25'
description: The U.S. Army Corps of Engineers (USACE) provides engineering and construction services for the nation, managing water resources, infrastructure, and environmental projects. USACE operates the Corps Water Management System (CWMS) Data API, a RESTful service for accessing real-time and historical water management data including time series measurements, location information, ratings, forecasts, and project data for USACE-managed water resources across the United States.
examples:
- key_count: 2
  name: Cwms Data Api Getcatalog Example
  slug: cwms-data-api-getCatalog-example
- key_count: 2
  name: Cwms Data Api Getlocations Example
  slug: cwms-data-api-getLocations-example
- key_count: 2
  name: Cwms Data Api Gettimeseries Example
  slug: cwms-data-api-getTimeSeries-example
finops:
- name: United States Army Corps Of Engineers Finops
  service_category: API
  slug: united-states-army-corps-of-engineers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-states-army-corps-of-engineers.png
json_schemas:
- name: CWMS Location
  property_count: 18
  slug: cwms-data-api-location
- name: CWMS Time Series
  property_count: 10
  slug: cwms-data-api-timeseries
json_structures:
- name: Cwms Data Api Location Structure
  property_count: 0
  slug: cwms-data-api-location-structure
- name: Cwms Data Api Timeseries Structure
  property_count: 0
  slug: cwms-data-api-timeseries-structure
jsonld:
- class_count: 4
  name: United States Army Corps Of Engineers Context
  property_count: 24
  slug: united-states-army-corps-of-engineers-context
layout: provider
modified: '2026-05-19'
name: United States Army Corps of Engineers
nav: Providers
network: true
overview: 'United States Army Corps of Engineers publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Basins API, Catalog API, Forecasts API, and 7 more. Tagged areas include Engineering, Federal-Government, Water Resources, Hydrology, and Civil Engineering.


  The United States Army Corps of Engineers catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United States Army Corps of Engineers'' developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: United States Army Corps Of Engineers Plans Pricing
  plan_count: 3
  slug: united-states-army-corps-of-engineers-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: United States Army Corps Of Engineers Rate Limits
  slug: united-states-army-corps-of-engineers-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: United States Army Corps of Engineers API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: cwms-data-api-rules
- effective_rule_count: 5
  extends: []
  name: United States Army Corps of Engineers API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-army-corps-of-engineers-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.1
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 54.5
    contract_quality: 62.2
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 54.5
    operational_transparency: 13.2
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-states-army-corps-of-engineers/refs/heads/main/screenshots/united-states-army-corps-of-engineers-2026-06-20T200046.png
security:
- kind: authentication
  name: United States Army Corps Of Engineers Authentication
  slug: united-states-army-corps-of-engineers-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: United States Army Corps Of Engineers Domain Security
  slug: united-states-army-corps-of-engineers-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: united-states-army-corps-of-engineers
tags:
- Engineering
- Federal-Government
- Water Resources
- Hydrology
- Civil Engineering
website: https://www.usace.army.mil/
---
