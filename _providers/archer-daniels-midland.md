---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Archer Daniels Midland Agentic Access
  operation_count: 4
  slug: archer-daniels-midland-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: Agricultural commodity pricing and market data
  name: Archer Daniels Midland Commodities API
  slug: archer-daniels-midland-commodities-api
- description: ADM global facility and processing plant locations
  name: Archer Daniels Midland Locations API
  slug: archer-daniels-midland-locations-api
- description: ADM food ingredients and product catalog
  name: Archer Daniels Midland Products API
  slug: archer-daniels-midland-products-api
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Archer Daniels Midland Commodity Data Commodities API
  slug: open-archer-daniels-midland-commodities-api
- collection_type: open
  name: Archer Daniels Midland Commodity Data API
  slug: open-archer-daniels-midland-commodity-data-api
- collection_type: open
  name: Archer Daniels Midland Commodity Data Commodities Locations API
  slug: open-archer-daniels-midland-locations-api
- collection_type: open
  name: Archer Daniels Midland Commodity Data Commodities Products API
  slug: open-archer-daniels-midland-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/archer-daniels-midland-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archer-daniels-midland-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/archer-daniels-midland-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/archer-daniels-midland
- group: start
  title: ''
  type: Portal
  url: https://www.adm.com/en-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/rules/archer-daniels-midland-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/vocabulary/archer-daniels-midland-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/json-ld/archer-daniels-midland-commodity-data-api-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.adm.com/en-us/news/adm-stories/
created: '2026-03-23'
description: Archer Daniels Midland (ADM) is a Fortune 100 global leader in agricultural processing and food ingredient manufacturing, providing nutrition solutions for food, beverage, health, and industrial markets worldwide.
examples:
- key_count: 10
  name: Archer Daniels Midland Commodity Data Api Commodity Detail Example
  slug: archer-daniels-midland-commodity-data-api-commodity-detail-example
- key_count: 7
  name: Archer Daniels Midland Commodity Data Api Commodity Example
  slug: archer-daniels-midland-commodity-data-api-commodity-example
- key_count: 2
  name: Archer Daniels Midland Commodity Data Api Commodity List Example
  slug: archer-daniels-midland-commodity-data-api-commodity-list-example
- key_count: 2
  name: Archer Daniels Midland Commodity Data Api Error Response Example
  slug: archer-daniels-midland-commodity-data-api-error-response-example
- key_count: 8
  name: Archer Daniels Midland Commodity Data Api Location Example
  slug: archer-daniels-midland-commodity-data-api-location-example
- key_count: 2
  name: Archer Daniels Midland Commodity Data Api Location List Example
  slug: archer-daniels-midland-commodity-data-api-location-list-example
- key_count: 6
  name: Archer Daniels Midland Commodity Data Api Product Example
  slug: archer-daniels-midland-commodity-data-api-product-example
- key_count: 2
  name: Archer Daniels Midland Commodity Data Api Product List Example
  slug: archer-daniels-midland-commodity-data-api-product-list-example
features:
- description: Agricultural commodity pricing, market trends, and availability data for corn, soybeans, wheat, and other grains.
  name: Commodity Data
- description: API integrations for supply chain visibility, logistics, and sourcing of agricultural raw materials.
  name: Supply Chain Integration
- description: ADM processed food ingredients and agricultural product specifications, nutritional data, and documentation.
  name: Product Catalog
- description: Global network of processing facilities, grain elevators, and distribution centers.
  name: Facility Locations
- description: B2B API integrations for key customers and supply chain partners.
  name: Partner Integration
finops:
- name: Archer Daniels Midland Finops
  service_category: Industrial / Agriculture
  slug: archer-daniels-midland-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archer-daniels-midland.png
integrations:
- description: Integration with SAP ERP for procurement, supply chain, and financial management.
  name: SAP
- description: Oracle ERP integration for commodity trading and logistics management.
  name: Oracle
- description: Integration with commodity futures and options data from CME Group.
  name: CME Group
- description: Commodity market data integration with Bloomberg terminal services.
  name: Bloomberg
json_schemas:
- name: CommodityDetail
  property_count: 10
  slug: archer-daniels-midland-commodity-data-api-commodity-detail
- name: CommodityList
  property_count: 2
  slug: archer-daniels-midland-commodity-data-api-commodity-list
- name: Commodity
  property_count: 7
  slug: archer-daniels-midland-commodity-data-api-commodity
- name: ErrorResponse
  property_count: 2
  slug: archer-daniels-midland-commodity-data-api-error-response
- name: LocationList
  property_count: 2
  slug: archer-daniels-midland-commodity-data-api-location-list
- name: Location
  property_count: 8
  slug: archer-daniels-midland-commodity-data-api-location
- name: ProductList
  property_count: 2
  slug: archer-daniels-midland-commodity-data-api-product-list
- name: Product
  property_count: 6
  slug: archer-daniels-midland-commodity-data-api-product
json_structures:
- name: Archer Daniels Midland Commodity Data Api Commodity Detail Structure
  property_count: 10
  slug: archer-daniels-midland-commodity-data-api-commodity-detail-structure
- name: Archer Daniels Midland Commodity Data Api Commodity List Structure
  property_count: 2
  slug: archer-daniels-midland-commodity-data-api-commodity-list-structure
- name: Archer Daniels Midland Commodity Data Api Commodity Structure
  property_count: 7
  slug: archer-daniels-midland-commodity-data-api-commodity-structure
- name: Archer Daniels Midland Commodity Data Api Error Response Structure
  property_count: 2
  slug: archer-daniels-midland-commodity-data-api-error-response-structure
- name: Archer Daniels Midland Commodity Data Api Location List Structure
  property_count: 2
  slug: archer-daniels-midland-commodity-data-api-location-list-structure
- name: Archer Daniels Midland Commodity Data Api Location Structure
  property_count: 8
  slug: archer-daniels-midland-commodity-data-api-location-structure
- name: Archer Daniels Midland Commodity Data Api Product List Structure
  property_count: 2
  slug: archer-daniels-midland-commodity-data-api-product-list-structure
- name: Archer Daniels Midland Commodity Data Api Product Structure
  property_count: 6
  slug: archer-daniels-midland-commodity-data-api-product-structure
jsonld:
- class_count: 7
  name: Archer Daniels Midland Commodity Data Api Context
  property_count: 22
  slug: archer-daniels-midland-commodity-data-api-context
layout: provider
modified: '2026-04-19'
name: Archer Daniels Midland
nav: Providers
network: true
overview: 'Archer Daniels Midland publishes 3 APIs on the [APIs.io](https://apis.io/) network: Commodities API, Locations API, and Products API. Tagged areas include Agriculture, Food Processing, Commodities, Supply Chain, and Fortune 100.


  The Archer Daniels Midland catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Archer Daniels Midland''s developer surface includes authentication, developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: Archer Daniels Midland Plans Pricing
  plan_count: 1
  slug: archer-daniels-midland-plans-pricing
press:
- date: '2026-05-25'
  title: ADM settles accounting scandal—can AI help prevent the ...
  url: https://finance.yahoo.com/news/adm-settles-accounting-scandal-ai-125235091.html
- date: '2026-05-25'
  title: 21st-century neural value chains
  url: https://www.tcs.com/what-we-do/industries/manufacturing/white-paper/digital-capabilities-21st-century-value-chains
- date: '2026-05-25'
  title: How ADM and Brightseed are using AI to expand ...
  url: https://www.fooddive.com/news/adm-brightseed-gut-health-ai-artificial-intelligence-tech-plant-based-microbiome-immunity/647378/
- date: '2026-05-25'
  title: ADM Archer-Daniels-Midland Company Stock Price & ...
  url: https://seekingalpha.com/symbol/ADM
- date: '2026-05-25'
  title: AI could pose risk for food and ag companies
  url: https://www.agriculturedive.com/news/ai-could-create-risk-for-food-and-ag-companies-ADM-Coca-Cola/724981/
random_paper: 0
rate_limits:
- limit_count: 1
  name: Archer Daniels Midland Rate Limits
  slug: archer-daniels-midland-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Archer Daniels Midland API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: archer-daniels-midland-jsonschema-spectral-rules
- effective_rule_count: 62
  extends:
  - spectral:oas
  name: Archer Daniels Midland API Rules
  rule_count: 21
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 11
  slug: archer-daniels-midland-spectral-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 21.6
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/screenshots/archer-daniels-midland-2026-06-20T172404.png
security:
- kind: authentication
  name: Archer Daniels Midland Authentication
  slug: archer-daniels-midland-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Archer Daniels Midland Domain Security
  slug: archer-daniels-midland-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: archer-daniels-midland
tags:
- Agriculture
- Food Processing
- Commodities
- Supply Chain
- Fortune 100
- Nutrition
use_cases:
- description: Automate commodity price tracking and procurement workflows for food manufacturers.
  name: Commodity Procurement
- description: Integrate ADM supply chain data with enterprise ERP and logistics systems.
  name: Supply Chain Visibility
- description: Search and source ADM processed food ingredients for product development.
  name: Food Ingredient Sourcing
- description: Access commodity pricing and market trend data for agricultural commodity risk management.
  name: Risk Management
website: https://www.adm.com/en-us/
---
