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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agricultural Statistics Service Agentic Access
  operation_count: 3
  slug: agricultural-statistics-service-agentic-access
  summary_line: 3 operations
api_count: 5
apis:
- description: The CroplandCROS API provides access to the Cropland Data Layer (CDL), a crop-specific land cover data layer with 30-meter spatial resolution covering the continental United States. Historical CDL dat
  name: USDA NASS CroplandCROS API
  slug: cropland-cros-api
- description: The VegScape API delivers vegetation condition indices at 250-meter spatial resolution covering the continental United States. Data includes daily and weekly vegetation index composites available sinc
  name: USDA NASS VegScape API
  slug: vegscape-api
- description: The Crop CASMA API provides programmatic access to crop vegetation and soil moisture conditions using NASA SMAP and MODIS satellite data for agricultural drought monitoring and crop condition analysis
  name: USDA NASS Crop CASMA API
  slug: crop-casma-api
- description: Parameter value discovery for query building
  name: Agricultural Statistics Service Parameters API
  slug: agricultural-statistics-service-parameters-api
- description: Agricultural statistics data retrieval and filtering
  name: Agricultural Statistics Service Statistics API
  slug: agricultural-statistics-service-statistics-api
artifact_total: 50
collections:
- collection_type: postman
  name: USDA NASS QuickStats Parameters API
  slug: postman-agricultural-statistics-service-parameters-api
- collection_type: postman
  name: USDA NASS QuickStats Parameters Statistics API
  slug: postman-agricultural-statistics-service-statistics-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USDA NASS QuickStats Parameters API
  slug: open-agricultural-statistics-service-parameters-api
- collection_type: open
  name: USDA NASS QuickStats Parameters Statistics API
  slug: open-agricultural-statistics-service-statistics-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/agricultural-statistics-service/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agricultural-statistics-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agricultural-statistics-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agricultural-statistics-service-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nass.usda.gov/rss/news.xml
- group: company
  title: ''
  type: Website
  url: https://www.nass.usda.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.nass.usda.gov/developer/index.php
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usda
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usda.gov/policies-and-links
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usda.gov/privacy-policy
- group: design
  title: ''
  type: SpectralRules
  url: rules/agricultural-statistics-service-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agricultural-statistics-service-vocabulary.yaml
created: '2024-12-03'
description: The National Agricultural Statistics Service (NASS) is an agency of the United States Department of Agriculture (USDA) whose mission is to support the United States, its agricultural sector, and rural communities by providing accurate, objective, and meaningful statistical information and services. NASS operates the QuickStats API for programmatic access to agricultural survey and census data, as well as geospatial APIs for cropland data, vegetation conditions, and crop moisture monitoring covering the continental United States.
examples:
- key_count: 1
  name: Quickstats Api Count Response Example
  slug: quickstats-api-count-response-example
- key_count: 2
  name: Quickstats Api Error Response Example
  slug: quickstats-api-error-response-example
- key_count: 1
  name: Quickstats Api Param Values Response Example
  slug: quickstats-api-param-values-response-example
- key_count: 18
  name: Quickstats Api Statistics Record Example
  slug: quickstats-api-statistics-record-example
- key_count: 1
  name: Quickstats Api Statistics Response Example
  slug: quickstats-api-statistics-response-example
features:
- description: All API access requires registration and an API key obtained by agreeing to NASS Terms of Service.
  name: API Key Authentication
- description: The QuickStats API supports JSON, XML, and CSV response formats with optional JSONP callback support.
  name: Multiple Output Formats
- description: Support for comparison operators including GE, LE, GT, LT, NE, LIKE, and NOT_LIKE for flexible data filtering.
  name: Rich Query Operators
- description: Access to the complete Census of Agriculture and annual survey estimates covering all major commodity types.
  name: Agricultural Census Data
- description: Geospatial APIs provide 30-meter and 250-meter resolution data layers covering the entire continental United States.
  name: Geospatial Data Coverage
- description: Access to historical agricultural statistics and cropland data extending back to 1997 for select states.
  name: Historical Time Series
finops:
- name: Agricultural Statistics Service Finops
  service_category: API
  slug: agricultural-statistics-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agricultural-statistics-service.png
integrations:
- description: Open-source R package for accessing NASS QuickStats API data directly within R statistical computing environments.
  name: R Package rnassqs
- description: Python package providing programmatic access to the USDA NASS QuickStats API for data analysis workflows.
  name: Python Package usdarnass
- description: NASS Quick Stats datasets are cataloged on catalog.data.gov for broader federal data discovery.
  name: data.gov Catalog
- description: Crop CASMA integrates NASA SMAP satellite data for soil moisture monitoring.
  name: NASA SMAP
json_schemas:
- name: Count Response
  property_count: 1
  slug: quickstats-api-count-response
- name: Error Response
  property_count: 2
  slug: quickstats-api-error-response
- name: Parameter Values Response
  property_count: 1
  slug: quickstats-api-param-values-response
- name: Statistics Record
  property_count: 18
  slug: quickstats-api-statistics-record
- name: Statistics Response
  property_count: 1
  slug: quickstats-api-statistics-response
json_structures:
- name: Quickstats Api Count Response Structure
  property_count: 1
  slug: quickstats-api-count-response-structure
- name: Quickstats Api Error Response Structure
  property_count: 2
  slug: quickstats-api-error-response-structure
- name: Quickstats Api Param Values Response Structure
  property_count: 1
  slug: quickstats-api-param-values-response-structure
- name: Quickstats Api Statistics Record Structure
  property_count: 18
  slug: quickstats-api-statistics-record-structure
- name: Quickstats Api Statistics Response Structure
  property_count: 1
  slug: quickstats-api-statistics-response-structure
jsonld:
- class_count: 5
  name: Agricultural Statistics Service Quickstats Api Context
  property_count: 23
  slug: agricultural-statistics-service-quickstats-api-context
layout: provider
modified: '2026-05-19'
name: Agricultural Statistics Service
nav: Providers
network: true
overview: 'Agricultural Statistics Service publishes 2 APIs on the [APIs.io](https://apis.io/) network: Parameters API and Statistics API. Tagged areas include Agriculture, Federal-Government, Statistics, Open Data, and Geospatial.


  The Agricultural Statistics Service catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Agricultural Statistics Service''s developer surface includes authentication, engineering blog, developer portal, and 9 more developer resources.'
plans:
- name: Agricultural Statistics Service Plans Pricing
  plan_count: 3
  slug: agricultural-statistics-service-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Agricultural Statistics Service Rate Limits
  slug: agricultural-statistics-service-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agricultural Statistics Service API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agricultural-statistics-service-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Agricultural Statistics Service API Rules
  rule_count: 27
  severity_counts:
    error: 11
    hint: 0
    info: 0
    warn: 16
  slug: agricultural-statistics-service-spectral-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 28.7
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agricultural-statistics-service/refs/heads/main/screenshots/agricultural-statistics-service-2026-06-20T170425.png
security:
- kind: authentication
  name: Agricultural Statistics Service Authentication
  slug: agricultural-statistics-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Agricultural Statistics Service Domain Security
  slug: agricultural-statistics-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agricultural-statistics-service
tags:
- Agriculture
- Federal-Government
- Statistics
- Open Data
- Geospatial
use_cases:
- description: Query crop production estimates by commodity, year, and location for market analysis and supply forecasting.
  name: Crop Production Analysis
- description: Access livestock inventory and production statistics at state and county levels for supply chain planning.
  name: Livestock Population Monitoring
- description: Use the CroplandCROS API to integrate 30-meter resolution cropland data into GIS applications and land use analysis.
  name: Geospatial Cropland Mapping
- description: Monitor crop condition and soil moisture via the Crop CASMA API to assess drought impacts on agricultural production.
  name: Agricultural Drought Monitoring
- description: Access the full Quick Stats database for academic research on agricultural trends, productivity, and policy analysis.
  name: Agricultural Research
- description: Combine crop production, livestock, and vegetation data to assess regional and national food security conditions.
  name: Food Security Assessment
website: https://www.nass.usda.gov/
---
