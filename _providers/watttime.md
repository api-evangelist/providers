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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Watttime Agentic Access
  operation_count: 9
  slug: watttime-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 6
apis:
- description: Official Python SDK for the WattTime API providing simplified access to real-time, forecast, and historical emissions data.
  name: WattTime Python Client
  slug: watttime-python-client
- description: Account information and access management.
  name: WattTime Account API
  slug: watttime-account-api
- description: Register for an account and obtain access tokens.
  name: WattTime Authentication API
  slug: watttime-authentication-api
- description: Access real-time, historical, and forecast marginal emissions signals for electric grids.
  name: WattTime Emissions Data API
  slug: watttime-emissions-data-api
- description: Retrieve emissions forecasts and historical forecast data.
  name: WattTime Forecasts API
  slug: watttime-forecasts-api
- description: Discover and query grid balancing authorities and regions.
  name: WattTime Grid Regions API
  slug: watttime-grid-regions-api
artifact_total: 81
collections:
- collection_type: postman
  name: WattTime Account API
  slug: postman-watttime-account-api
- collection_type: postman
  name: WattTime Account Authentication API
  slug: postman-watttime-authentication-api
- collection_type: postman
  name: WattTime Account Emissions Data API
  slug: postman-watttime-emissions-data-api
- collection_type: postman
  name: WattTime Account Forecasts API
  slug: postman-watttime-forecasts-api
- collection_type: postman
  name: WattTime Account Grid Regions API
  slug: postman-watttime-grid-regions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WattTime Account API
  slug: open-watttime-account-api
- collection_type: open
  name: WattTime Account Authentication API
  slug: open-watttime-authentication-api
- collection_type: open
  name: WattTime Account Emissions Data API
  slug: open-watttime-emissions-data-api
- collection_type: open
  name: WattTime Account Forecasts API
  slug: open-watttime-forecasts-api
- collection_type: open
  name: WattTime Account Grid Regions API
  slug: open-watttime-grid-regions-api
- collection_type: open
  name: WattTime API
  slug: open-watttime
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/watttime/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/watttime-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/watttime-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/watttime-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/watttime
- group: start
  title: WattTime Website
  type: Portal
  url: https://watttime.org/
- group: docs
  title: API Documentation
  type: Documentation
  url: https://docs.watttime.org/
- group: operate
  title: API Release Notes
  type: ReleaseNotes
  url: https://watttime.org/data-science/release-notes/
- group: operate
  title: API Status Page
  type: StatusPage
  url: http://status.watttime.org/
- group: build
  title: WattTime GitHub Organization
  type: GitHubOrganization
  url: https://github.com/WattTime
- group: operate
  title: Support Email
  type: Support
  url: mailto:support@watttime.org
- group: design
  title: WattTime Spectral Rules
  type: SpectralRules
  url: rules/watttime-spectral-rules.yml
- group: design
  title: WattTime Vocabulary
  type: Vocabulary
  url: vocabulary/watttime-vocabulary.yml
- group: design
  title: WattTime JSON-LD Context
  type: JSONLD
  url: json-ld/watttime-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://watttime.org/feed/
created: '2025-05-02'
description: WattTime is a nonprofit organization that provides real-time, forecast, and historical data for electric grids around the world, enabling carbon-aware computing and clean energy procurement decisions. The WattTime API delivers marginal emissions data (CO2 MOER), health damage signals, average emissions rates, and renewable energy forecasts for 342 grid regions across 210 countries and territories. Developers and organizations use the API to schedule workloads during low-carbon windows, measure actual emissions reductions from clean energy procurement, and meet sustainability reporting requirements.
examples:
- key_count: 4
  name: Watttime Data Meta Example
  slug: watttime-data-meta-example
- key_count: 3
  name: Watttime Data Point Example
  slug: watttime-data-point-example
- key_count: 2
  name: Watttime Data Response Example
  slug: watttime-data-response-example
- key_count: 5
  name: Watttime Forecast Meta Example
  slug: watttime-forecast-meta-example
- key_count: 2
  name: Watttime Forecast Response Example
  slug: watttime-forecast-response-example
- key_count: 2
  name: Watttime Grid Maps Response Example
  slug: watttime-grid-maps-response-example
- key_count: 4
  name: Watttime Historical Download Response Example
  slug: watttime-historical-download-response-example
- key_count: 1
  name: Watttime Login Response Example
  slug: watttime-login-response-example
- key_count: 2
  name: Watttime My Access Response Example
  slug: watttime-my-access-response-example
- key_count: 6
  name: Watttime Region Access Example
  slug: watttime-region-access-example
- key_count: 3
  name: Watttime Region Response Example
  slug: watttime-region-response-example
- key_count: 4
  name: Watttime Register Request Example
  slug: watttime-register-request-example
- key_count: 2
  name: Watttime Register Response Example
  slug: watttime-register-response-example
features:
- description: CO2 MOER signal providing real-time marginal carbon intensity for local grid regions, updated every 5 minutes via the forecast endpoint.
  name: Real-Time Marginal Emissions
- description: 24-72 hour ahead emissions forecasts enabling applications to schedule energy-intensive workloads during low-carbon grid windows.
  name: Emissions Forecasting
- description: Historical MOER data available for up to 32 days via the data endpoint, and multi-year historical datasets downloadable as CSV files.
  name: Historical Data Access
- description: Estimates the damage to human life and health caused by emissions from electricity generation based on time and location of consumption.
  name: Health Damage Signal
- description: Coverage across 342 grid regions in 210 countries and territories, including North America, Europe, and global expansion with synthetic demand proxy models.
  name: Global Grid Coverage
- description: Identify the relevant balancing authority for any geographic coordinates and retrieve the list of accessible grid regions.
  name: Grid Region Discovery
- description: Date-based model versioning (e.g., 2026-03-01) allowing unique versions per region and signal for reproducibility and comparison.
  name: Model Versioning
finops:
- name: Watttime Finops
  service_category: API
  slug: watttime-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/watttime.png
integrations:
- description: WattTime provides the carbon intensity data underlying the Green Software Foundation's Software Carbon Intensity (SCI) specification.
  name: Green Software Foundation
- description: WattTime contributes emissions data and modeling to the Climate TRACE global emissions inventory.
  name: Climate TRACE
- description: Official Green Software Foundation Impact Framework plugin available for integrating WattTime data into software sustainability measurements.
  name: Impact Framework
json_schemas:
- name: DataMeta
  property_count: 4
  slug: watttime-data-meta
- name: DataPoint
  property_count: 3
  slug: watttime-data-point
- name: DataResponse
  property_count: 2
  slug: watttime-data-response
- name: ForecastMeta
  property_count: 5
  slug: watttime-forecast-meta
- name: ForecastResponse
  property_count: 2
  slug: watttime-forecast-response
- name: GridMapsResponse
  property_count: 2
  slug: watttime-grid-maps-response
- name: HistoricalDownloadResponse
  property_count: 4
  slug: watttime-historical-download-response
- name: LoginResponse
  property_count: 1
  slug: watttime-login-response
- name: MyAccessResponse
  property_count: 2
  slug: watttime-my-access-response
- name: RegionAccess
  property_count: 6
  slug: watttime-region-access
- name: RegionResponse
  property_count: 3
  slug: watttime-region-response
- name: RegisterRequest
  property_count: 4
  slug: watttime-register-request
- name: RegisterResponse
  property_count: 2
  slug: watttime-register-response
json_structures:
- name: Watttime Data Meta Structure
  property_count: 4
  slug: watttime-data-meta-structure
- name: Watttime Data Point Structure
  property_count: 3
  slug: watttime-data-point-structure
- name: Watttime Data Response Structure
  property_count: 2
  slug: watttime-data-response-structure
- name: Watttime Forecast Meta Structure
  property_count: 5
  slug: watttime-forecast-meta-structure
- name: Watttime Forecast Response Structure
  property_count: 2
  slug: watttime-forecast-response-structure
- name: Watttime Grid Maps Response Structure
  property_count: 2
  slug: watttime-grid-maps-response-structure
- name: Watttime Historical Download Response Structure
  property_count: 4
  slug: watttime-historical-download-response-structure
- name: Watttime Login Response Structure
  property_count: 1
  slug: watttime-login-response-structure
- name: Watttime My Access Response Structure
  property_count: 2
  slug: watttime-my-access-response-structure
- name: Watttime Region Access Structure
  property_count: 6
  slug: watttime-region-access-structure
- name: Watttime Region Response Structure
  property_count: 3
  slug: watttime-region-response-structure
- name: Watttime Register Request Structure
  property_count: 4
  slug: watttime-register-request-structure
- name: Watttime Register Response Structure
  property_count: 2
  slug: watttime-register-response-structure
jsonld:
- class_count: 13
  name: Watttime Context
  property_count: 25
  slug: watttime-context
layout: provider
modified: '2026-05-19'
name: WattTime
nav: Providers
network: true
overview: 'WattTime publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Emissions Data API, and 2 more. Tagged areas include Emissions, Climate, Carbon, Energy, and Electricity Grid.


  The WattTime catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WattTime''s developer surface includes authentication, developer portal, documentation, release notes, support, engineering blog, and 9 more developer resources.'
plans:
- name: Watttime Plans Pricing
  plan_count: 3
  slug: watttime-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Watttime Rate Limits
  slug: watttime-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WattTime API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: watttime-jsonschema-spectral-rules
- effective_rule_count: 80
  extends:
  - spectral:oas
  name: WattTime API Rules
  rule_count: 39
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 25
  slug: watttime-spectral-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 32.1
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 42.1
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/watttime/refs/heads/main/screenshots/watttime-2026-06-20T201256.png
security:
- kind: authentication
  name: Watttime Authentication
  slug: watttime-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Watttime Domain Security
  slug: watttime-domain-security
  summary_line: TLSv1.3
slug: watttime
tags:
- Emissions
- Climate
- Carbon
- Energy
- Electricity Grid
- Sustainability
- Clean Energy
use_cases:
- description: Technology companies and cloud providers schedule compute workloads, data transfers, and batch jobs to run during periods of low marginal carbon intensity.
  name: Carbon-Aware Computing
- description: Organizations measure the actual emissions reductions from renewable energy procurement and power purchase agreements using marginal emissions data.
  name: Clean Energy Procurement
- description: Enterprises report Scope 2 emissions more accurately using marginal emissions rates rather than average grid emission factors.
  name: Sustainability Reporting
- description: Building energy management systems shift heating, cooling, and EV charging to low-emission grid windows to reduce carbon footprint.
  name: Smart Building Optimization
- description: Researchers, utilities, and policy makers analyze historical and forecast emissions data to study grid decarbonization trends.
  name: Grid Research and Analysis
website: https://watttime.org/
---
