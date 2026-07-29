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
- acting_count: 0
  human_in_the_loop: 0
  name: United States Department Of Agriculture Agentic Access
  operation_count: 15
  slug: united-states-department-of-agriculture-agentic-access
  summary_line: 15 operations
api_count: 8
apis:
- description: Station data retrieval
  name: United States Department of Agriculture Data API
  slug: united-states-department-of-agriculture-data-api
- description: Food search and retrieval operations
  name: United States Department of Agriculture Foods API
  slug: united-states-department-of-agriculture-foods-api
- description: Water supply forecasts
  name: United States Department of Agriculture Forecasts API
  slug: united-states-department-of-agriculture-forecasts-api
- description: Available years, states, reports, and variables
  name: United States Department of Agriculture Metadata API
  slug: united-states-department-of-agriculture-metadata-api
- description: Nutrient data and lists
  name: United States Department of Agriculture Nutrients API
  slug: united-states-department-of-agriculture-nutrients-api
- description: Monitoring station metadata and discovery
  name: United States Department of Agriculture Stations API
  slug: united-states-department-of-agriculture-stations-api
- description: Agricultural statistics query and retrieval
  name: United States Department of Agriculture Statistics API
  slug: united-states-department-of-agriculture-statistics-api
- description: Farm survey data retrieval
  name: United States Department of Agriculture Survey Data API
  slug: united-states-department-of-agriculture-survey-data-api
artifact_total: 27
collections:
- collection_type: open
  name: USDA ERS ARMS Data API
  slug: open-usda-ers-arms
- collection_type: open
  name: USDA FoodData Central API
  slug: open-usda-fooddata-central
- collection_type: open
  name: USDA NASS Quick Stats API
  slug: open-usda-nass-quickstats
- collection_type: open
  name: USDA NRCS AWDB Water and Climate REST API
  slug: open-usda-nrcs-awdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-states-department-of-agriculture-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-states-department-of-agriculture-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-states-department-of-agriculture-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usda
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda
created: '2024-11-14'
description: The United States Department of Agriculture (USDA) is a federal agency responsible for developing and executing policies related to farming, agriculture, forestry, and food. The USDA works to ensure the sustainability and safety of America's food supply, while also supporting rural development and promoting economic growth in rural communities. USDA provides multiple public APIs including FoodData Central for nutrient data, NASS Quick Stats for agricultural statistics, ERS ARMS for farm economics, and NRCS AWDB for water and climate monitoring data.
examples:
- key_count: 3
  name: Usda Awdb Get Station Data Example
  slug: usda-awdb-get-station-data-example
- key_count: 3
  name: Usda Fdc Search Foods Example
  slug: usda-fdc-search-foods-example
- key_count: 3
  name: Usda Nass Get Statistics Example
  slug: usda-nass-get-statistics-example
finops:
- name: United States Department Of Agriculture Finops
  service_category: API
  slug: united-states-department-of-agriculture-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-states-department-of-agriculture.png
json_schemas:
- name: USDA FoodData Central Food Item
  property_count: 10
  slug: usda-fdc-food-item
- name: USDA NASS Agricultural Statistics Record
  property_count: 16
  slug: usda-nass-stat-record
json_structures:
- name: Usda Fdc Food Item Structure
  property_count: 0
  slug: usda-fdc-food-item-structure
jsonld:
- class_count: 4
  name: United States Department Of Agriculture Context
  property_count: 14
  slug: united-states-department-of-agriculture-context
layout: provider
modified: '2026-05-19'
name: United States Department of Agriculture
nav: Providers
network: true
overview: 'United States Department of Agriculture publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Data API, Foods API, Forecasts API, and 5 more. Tagged areas include Federal Government, Agriculture, Food Safety, Nutrition, and Rural Development.


  The United States Department of Agriculture catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United States Department of Agriculture''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: United States Department Of Agriculture Plans Pricing
  plan_count: 3
  slug: united-states-department-of-agriculture-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: United States Department Of Agriculture Rate Limits
  slug: united-states-department-of-agriculture-rate-limits
rules:
- name: United States Department of Agriculture API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-department-of-agriculture-jsonschema-spectral-rules
- name: United States Department of Agriculture API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: usda-fooddata-central-rules
score:
  band: developing
  composite: 45.5
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/screenshots/united-states-department-of-agriculture-2026-06-20T200058.png
security:
- kind: authentication
  name: United States Department Of Agriculture Authentication
  slug: united-states-department-of-agriculture-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: United States Department Of Agriculture Domain Security
  slug: united-states-department-of-agriculture-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: united-states-department-of-agriculture
tags:
- Federal Government
- Agriculture
- Food Safety
- Nutrition
- Rural Development
- Climate
---
