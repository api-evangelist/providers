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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Usda Agricultural Research Service Ars  Agentic Access
  operation_count: 12
  slug: usda-agricultural-research-service-ars--agentic-access
  summary_line: 12 operations · 3 acting
api_count: 3
apis:
- description: Dataset metadata search and retrieval
  name: USDA Agricultural Research Service (ARS) Datasets API
  slug: usda-agricultural-research-service-ars--datasets-api
- description: Search foods by keywords or other criteria
  name: USDA Agricultural Research Service (ARS) Food Search API
  slug: usda-agricultural-research-service-ars--food-search-api
- description: Retrieve food records by FDC ID
  name: USDA Agricultural Research Service (ARS) Foods API
  slug: usda-agricultural-research-service-ars--foods-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USDA Ag Data Commons CKAN Datasets API
  slug: open-usda-agricultural-research-service-ars--datasets-api
- collection_type: open
  name: USDA Ag Data Commons CKAN Datasets Food Search API
  slug: open-usda-agricultural-research-service-ars--food-search-api
- collection_type: open
  name: USDA Ag Data Commons CKAN Datasets Foods API
  slug: open-usda-agricultural-research-service-ars--foods-api
- collection_type: open
  name: USDA Ag Data Commons CKAN API
  slug: open-usda-ars-ag-data-commons
- collection_type: open
  name: USDA FoodData Central API
  slug: open-usda-ars-fooddata-central
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usda-agricultural-research-service-ars--agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usda-agricultural-research-service-ars--domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usda-agricultural-research-service-ars--authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-ars
- group: company
  title: ''
  type: Blog
  url: http://www.ars.usda.gov/rss
created: '2024-11-21'
description: The USDA Agricultural Research Service (ARS) is the principal in-house research agency of the US Department of Agriculture. ARS conducts research to develop and implement solutions to agricultural problems that affect Americans every day. Research areas include crop protection, animal health, food safety, natural resource management, sustainable agriculture, and nutrition. ARS provides public data access through FoodData Central (nutrition data) and the Ag Data Commons (agricultural research datasets repository with CKAN/DKAN API).
examples:
- key_count: 2
  name: Usda Ars Search Datasets Example
  slug: usda-ars-search-datasets-example
- key_count: 2
  name: Usda Ars Search Foods Example
  slug: usda-ars-search-foods-example
finops:
- name: Usda Agricultural Research Service Ars  Finops
  service_category: API
  slug: usda-agricultural-research-service-ars--finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usda-agricultural-research-service-ars-.png
json_schemas:
- name: USDA FoodData Central Food Item
  property_count: 11
  slug: usda-ars-food-item
json_structures:
- name: Usda Ars Food Item Structure
  property_count: 0
  slug: usda-ars-food-item-structure
jsonld:
- class_count: 3
  name: Usda Agricultural Research Service Ars Context
  property_count: 17
  slug: usda-agricultural-research-service-ars--context
layout: provider
modified: '2026-05-19'
name: USDA Agricultural Research Service (ARS)
nav: Providers
network: true
overview: 'USDA Agricultural Research Service (ARS) publishes 3 APIs on the [APIs.io](https://apis.io/) network: Datasets API, Food Search API, and Foods API. Tagged areas include Federal-Government, Agriculture, Food Safety, Nutrition, and Open Data.


  The USDA Agricultural Research Service (ARS) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  USDA Agricultural Research Service (ARS)''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Usda Agricultural Research Service Ars  Plans Pricing
  plan_count: 3
  slug: usda-agricultural-research-service-ars--plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Usda Agricultural Research Service Ars  Rate Limits
  slug: usda-agricultural-research-service-ars--rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: USDA Agricultural Research Service (ARS) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: usda-agricultural-research-service-ars--jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: USDA Agricultural Research Service (ARS) API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: usda-agricultural-research-service-ars--rules
score:
  band: thin
  composite: 34.0
  delta: 3.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 54.1
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usda-agricultural-research-service-ars-/refs/heads/main/screenshots/usda-agricultural-research-service-ars--2026-06-20T200650.png
security:
- kind: authentication
  name: Usda Agricultural Research Service Ars  Authentication
  slug: usda-agricultural-research-service-ars--authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Usda Agricultural Research Service Ars  Domain Security
  slug: usda-agricultural-research-service-ars--domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: usda-agricultural-research-service-ars-
tags:
- Federal-Government
- Agriculture
- Food Safety
- Nutrition
- Open Data
- Research
---
