---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: United States Census Bureau Agentic Access
  operation_count: 10
  slug: united-states-census-bureau-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: The TIGERweb GeoServices REST API provides access to Census Bureau geographic data including boundaries for states, counties, census tracts, block groups, and other geographic entities. Supports stand
  name: TIGERweb GeoServices REST API
  slug: tigerweb-rest-api
- description: The Census Geocoding Services convert addresses to geographic coordinates and census geography identifiers. Supports both single-address lookups and batch geocoding for large address lists.
  name: Census Geocoding Services
  slug: geocoding-api
- description: ACS demographic, economic, social, and housing characteristics
  name: United States Census Bureau American Community Survey API
  slug: united-states-census-bureau-american-community-survey-api
- description: Business establishment and employment data
  name: United States Census Bureau County Business Patterns API
  slug: united-states-census-bureau-county-business-patterns-api
- description: Decennial Census population and housing counts
  name: United States Census Bureau Decennial Census API
  slug: united-states-census-bureau-decennial-census-api
- description: Economic activity by industry and geography
  name: United States Census Bureau Economic Census API
  slug: united-states-census-bureau-economic-census-api
- description: Geocoding and geographic boundary services
  name: United States Census Bureau Geographic Services API
  slug: united-states-census-bureau-geographic-services-api
- description: International demographic and trade data
  name: United States Census Bureau International API
  slug: united-states-census-bureau-international-api
- description: Annual population estimates and projections
  name: United States Census Bureau Population Estimates API
  slug: united-states-census-bureau-population-estimates-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Census Data API
  slug: open-census-data-api
- collection_type: open
  name: Census Data American Community Survey API
  slug: open-united-states-census-bureau-american-community-survey-api
- collection_type: open
  name: Census Data American Community Survey County Business Patterns API
  slug: open-united-states-census-bureau-county-business-patterns-api
- collection_type: open
  name: Census Data American Community Survey Decennial Census API
  slug: open-united-states-census-bureau-decennial-census-api
- collection_type: open
  name: Census Data American Community Survey Economic Census API
  slug: open-united-states-census-bureau-economic-census-api
- collection_type: open
  name: Census Data American Community Survey Geographic Services API
  slug: open-united-states-census-bureau-geographic-services-api
- collection_type: open
  name: Census Data American Community Survey International API
  slug: open-united-states-census-bureau-international-api
- collection_type: open
  name: Census Data American Community Survey Population Estimates API
  slug: open-united-states-census-bureau-population-estimates-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-states-census-bureau-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-states-census-bureau-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-census-bureau
- group: company
  title: ''
  type: Website
  url: https://www.census.gov/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.census.gov/data/developers.html
- group: start
  title: ''
  type: APIKeySignup
  url: https://api.census.gov/data/key_signup.html
- group: other
  title: ''
  type: DataExplorer
  url: https://data.census.gov/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uscensusbureau
- group: operate
  title: ''
  type: Forums
  url: https://apiforum.uscensusbureau.com/
- group: company
  title: ''
  type: Newsletter
  url: https://public.govdelivery.com/accounts/USCENSUS/subscriber/new?topic_id=USCENSUS_11933
- group: agent
  title: ''
  type: LlmsText
  url: https://api.census.gov/llms.txt
created: '2024-01-01'
description: The U.S. Census Bureau is the nation's leading provider of quality data about its people and economy. The Census Bureau has been rolling out datasets via APIs, providing programmatic access to demographic, economic, housing, and social statistics. The Census Data API supports queries across datasets including the American Community Survey, Decennial Census, Population Estimates, County Business Patterns, Economic Census, and International Trade, with data available at national, state, county, tract, and block group geographic levels.
examples:
- key_count: 3
  name: Census Data Api Geocodeaddress Example
  slug: census-data-api-geocodeAddress-example
- key_count: 3
  name: Census Data Api Getacs5Year Example
  slug: census-data-api-getACS5Year-example
- key_count: 3
  name: Census Data Api Getcountybusinesspatterns Example
  slug: census-data-api-getCountyBusinessPatterns-example
finops:
- name: United States Census Bureau Finops
  service_category: API
  slug: united-states-census-bureau-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-states-census-bureau.png
json_schemas:
- name: Census Geocoder Response
  property_count: 1
  slug: census-data-api-geocode
- name: Census Data API Response
  property_count: 0
  slug: census-data-api-response
json_structures:
- name: Census Data Api Response Structure
  property_count: 0
  slug: census-data-api-response-structure
jsonld:
- class_count: 4
  name: United States Census Bureau Context
  property_count: 21
  slug: united-states-census-bureau-context
layout: provider
modified: '2026-05-19'
name: United States Census Bureau
nav: Providers
network: true
overview: 'United States Census Bureau publishes 7 APIs on the [APIs.io](https://apis.io/) network, including American Community Survey API, County Business Patterns API, Decennial Census API, and 4 more. Tagged areas include Demographics, Federal-Government, Open Data, Statistics, and Economics.


  The United States Census Bureau catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United States Census Bureau''s developer surface includes GitHub presence and 10 more developer resources.'
plans:
- name: United States Census Bureau Plans Pricing
  plan_count: 3
  slug: united-states-census-bureau-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: United States Census Bureau Rate Limits
  slug: united-states-census-bureau-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: United States Census Bureau API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: census-data-api-rules
- effective_rule_count: 5
  extends: []
  name: United States Census Bureau API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-census-bureau-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 34.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 54.5
    contract_quality: 57.8
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 54.5
    operational_transparency: 13.2
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-states-census-bureau/refs/heads/main/screenshots/united-states-census-bureau-2026-06-20T200100.png
security:
- kind: domain-security
  name: United States Census Bureau Domain Security
  slug: united-states-census-bureau-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: united-states-census-bureau
tags:
- Demographics
- Federal-Government
- Open Data
- Statistics
- Economics
- Population
website: https://www.census.gov/
---
