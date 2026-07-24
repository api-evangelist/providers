---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Usda Agentic Access
  operation_count: 9
  slug: usda-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 7
apis:
- description: Programmatic access to official US agricultural statistics from the National Agricultural Statistics Service, including crop production estimates, livestock data, and Census of Agriculture results fro
  name: USDA NASS Quick Stats API
  slug: usda-nass-quick-stats-api
- description: Economic Research Service API providing access to data from the Agriculture Resource Management Survey (ARMS), covering farm finances, production practices, and resource use. Returns data in JSON form
  name: USDA ERS ARMS Data API
  slug: usda-ers-arms-data-api
- description: Market Analysis Reporting System (MARS) API providing programmatic access to USDA Agricultural Marketing Service commodity price and market news data including livestock, dairy, fruits, vegetables, an
  name: USDA AMS MyMarketNews MARS API
  slug: usda-ams-mymarketnews-mars-api
- description: Geospatial API serving Cropland Data Layer (CDL) and related geospatial data at 30-meter resolution covering the continental US from 2008 onward, with historical data for select states back to 1997.
  name: USDA NASS CroplandCROS API
  slug: usda-nass-croplandcros-api
- description: ArcGIS Server REST API providing access to USDA Forest Service nationwide geospatial datasets including forest boundaries, land status, fire occurrence, and ecological data layers.
  name: USDA Forest Service Geospatial REST API
  slug: usda-forest-service-geospatial-rest-api
- description: Food Safety and Inspection Service API providing real-time access to the Meat, Poultry and Egg Product Inspection Directory, including establishment location, size, species processed, and inspection s
  name: USDA FSIS MPI Directory API
  slug: usda-fsis-mpi-directory-api
- description: endpoints to retrieve nutrient data
  name: USDA FDC API
  slug: usda-fdc-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usda-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usda-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.usda.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ers.usda.gov/developer/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/USDA
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/USDA-REE-ERS
- group: company
  title: ''
  type: Blog
  url: https://www.usda.gov/media/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://api.data.gov/docs/developer-manual/
- group: operate
  title: ''
  type: StatusPage
  url: https://api.data.gov/status/
- group: other
  title: ''
  type: X
  url: https://twitter.com/USDA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda
- group: commercial
  title: ''
  type: Plans
  url: plans/usda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usda-finops.yml
created: '2026-06-13'
description: The US Department of Agriculture provides a suite of free public REST APIs covering agricultural statistics, food and nutrition data, market news, food safety inspection records, crop and vegetation monitoring, and geospatial services. APIs are accessed through api.data.gov and agency-specific portals, all requiring a free API key.
examples:
- key_count: 3
  name: Usda Fooddata Central Food Item Example
  slug: usda-fooddata-central-food-item-example
- key_count: 3
  name: Usda Fooddata Central Food Search Example
  slug: usda-fooddata-central-food-search-example
finops:
- name: Usda Finops
  service_category: ''
  slug: usda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usda.png
json_schemas:
- name: FoodData Central Food Item
  property_count: 0
  slug: usda-fooddata-central-food-item
jsonld:
- class_count: 7
  name: Usda Context
  property_count: 54
  slug: usda-context
layout: provider
modified: '2026-06-13'
name: USDA
nav: Providers
network: true
overview: 'USDA publishes 1 API on the [APIs.io](https://apis.io/) network: FDC API. Tagged areas include Agriculture, Food Safety, Nutrition, Statistics, and Geospatial.


  The USDA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  USDA''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Usda Plans Pricing
  plan_count: 3
  slug: usda-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Usda Rate Limits
  slug: usda-rate-limits
rules:
- name: USDA API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: usda-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 51.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usda/refs/heads/main/screenshots/usda-2026-06-20T200646.png
security:
- kind: authentication
  name: Usda Authentication
  slug: usda-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Usda Domain Security
  slug: usda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: usda
tags:
- Agriculture
- Food Safety
- Nutrition
- Statistics
- Geospatial
- Market News
- Federal Government
website: https://www.usda.gov/
---
