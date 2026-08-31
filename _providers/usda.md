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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Usda Agentic Access
  operation_count: 9
  slug: usda-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Food Data Central FDC API
  slug: open-usda-fdc-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/USDA-REE-ERS/ARMS-Data-API/issues
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


  USDA''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Usda Plans Pricing
  plan_count: 3
  slug: usda-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Usda Rate Limits
  slug: usda-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: USDA API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: usda-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 60.5
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  open_source:
    applies: true
    score: 0.0
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Federal-Government
website: https://www.usda.gov/
---
