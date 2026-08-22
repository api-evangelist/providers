---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Marginedge Agentic Access
  operation_count: 10
  slug: marginedge-agentic-access
  summary_line: 10 operations
api_count: 5
apis:
- description: Accounting categories
  name: MarginEdge Categories API
  slug: marginedge-categories-api
- description: Invoices/orders processed in MarginEdge
  name: MarginEdge Orders API
  slug: marginedge-orders-api
- description: Products tracked in a restaurant
  name: MarginEdge Products API
  slug: marginedge-products-api
- description: Restaurants, groups, and group categories you can access
  name: MarginEdge Restaurant Units API
  slug: marginedge-restaurant-units-api
- description: Vendors and their items and packaging
  name: MarginEdge Vendors API
  slug: marginedge-vendors-api
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MarginEdge Public Categories API
  slug: open-marginedge-categories-api
- collection_type: open
  name: MarginEdge Public Categories Orders API
  slug: open-marginedge-orders-api
- collection_type: open
  name: MarginEdge Public Categories Products API
  slug: open-marginedge-products-api
- collection_type: open
  name: MarginEdge Public Categories Restaurant Units API
  slug: open-marginedge-restaurant-units-api
- collection_type: open
  name: MarginEdge Public Categories Vendors API
  slug: open-marginedge-vendors-api
- collection_type: open
  name: MarginEdge Public API
  slug: open-marginedge
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marginedge-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/marginedge-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marginedge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marginedge-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.marginedge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.marginedge.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marginedge.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://help.marginedge.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.marginedge.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marginedge
- group: design
  title: ''
  type: SpectralRules
  url: rules/marginedge-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/marginedge-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/marginedge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marginedge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/marginedge-finops.yml
created: '2026-06-02'
description: MarginEdge is a restaurant back-office platform that automates invoice processing, inventory, recipe costing, and bill payment, syncing daily food cost and sales data into a restaurant's accounting system. Founded in 2015, it serves over 7,000 restaurants across all 50 states. For developers, MarginEdge publishes a public API through a dedicated developer portal that lets authorized parties programmatically retrieve invoice and product data from the restaurants they are permitted to access. Typical consumers include multi-unit operators building custom reporting, accounting groups, and business intelligence providers contracting with MarginEdge customers to deliver data services.
examples:
- key_count: 1
  name: Public Api Get Available Restaurant Units Response Model Example
  slug: public-api-get-available-restaurant-units-response-model-example
- key_count: 2
  name: Public Api Get Categories Response Model Example
  slug: public-api-get-categories-response-model-example
- key_count: 1
  name: Public Api Get Group Categories Response Model Example
  slug: public-api-get-group-categories-response-model-example
- key_count: 1
  name: Public Api Get Groups Response Model Example
  slug: public-api-get-groups-response-model-example
- key_count: 19
  name: Public Api Get Order Detail Response Model Example
  slug: public-api-get-order-detail-response-model-example
- key_count: 2
  name: Public Api Get Orders Response Model Example
  slug: public-api-get-orders-response-model-example
- key_count: 2
  name: Public Api Get Products Response Model Example
  slug: public-api-get-products-response-model-example
- key_count: 2
  name: Public Api Get Vendor Items Packaging Response Model Example
  slug: public-api-get-vendor-items-packaging-response-model-example
- key_count: 2
  name: Public Api Get Vendor Items Response Model Example
  slug: public-api-get-vendor-items-response-model-example
- key_count: 2
  name: Public Api Get Vendors Response Model Example
  slug: public-api-get-vendors-response-model-example
finops:
- name: Marginedge Finops
  service_category: Restaurant Back-Office Management
  slug: marginedge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marginedge.png
json_schemas:
- name: GetAvailableRestaurantUnitsResponseModel
  property_count: 1
  slug: public-api-get-available-restaurant-units-response-model
- name: GetCategoriesResponseModel
  property_count: 2
  slug: public-api-get-categories-response-model
- name: GetGroupCategoriesResponseModel
  property_count: 1
  slug: public-api-get-group-categories-response-model
- name: GetGroupsResponseModel
  property_count: 1
  slug: public-api-get-groups-response-model
- name: GetOrderDetailResponseModel
  property_count: 19
  slug: public-api-get-order-detail-response-model
- name: GetOrdersResponseModel
  property_count: 2
  slug: public-api-get-orders-response-model
- name: GetProductsResponseModel
  property_count: 2
  slug: public-api-get-products-response-model
- name: GetVendorItemsPackagingResponseModel
  property_count: 2
  slug: public-api-get-vendor-items-packaging-response-model
- name: GetVendorItemsResponseModel
  property_count: 2
  slug: public-api-get-vendor-items-response-model
- name: GetVendorsResponseModel
  property_count: 2
  slug: public-api-get-vendors-response-model
json_structures:
- name: Public Api Get Available Restaurant Units Response Model Structure
  property_count: 1
  slug: public-api-get-available-restaurant-units-response-model-structure
- name: Public Api Get Categories Response Model Structure
  property_count: 2
  slug: public-api-get-categories-response-model-structure
- name: Public Api Get Group Categories Response Model Structure
  property_count: 1
  slug: public-api-get-group-categories-response-model-structure
- name: Public Api Get Groups Response Model Structure
  property_count: 1
  slug: public-api-get-groups-response-model-structure
- name: Public Api Get Order Detail Response Model Structure
  property_count: 19
  slug: public-api-get-order-detail-response-model-structure
- name: Public Api Get Orders Response Model Structure
  property_count: 2
  slug: public-api-get-orders-response-model-structure
- name: Public Api Get Products Response Model Structure
  property_count: 2
  slug: public-api-get-products-response-model-structure
- name: Public Api Get Vendor Items Packaging Response Model Structure
  property_count: 2
  slug: public-api-get-vendor-items-packaging-response-model-structure
- name: Public Api Get Vendor Items Response Model Structure
  property_count: 2
  slug: public-api-get-vendor-items-response-model-structure
- name: Public Api Get Vendors Response Model Structure
  property_count: 2
  slug: public-api-get-vendors-response-model-structure
jsonld:
- class_count: 10
  name: Marginedge Context
  property_count: 67
  slug: marginedge-context
layout: provider
modified: '2026-06-02'
name: MarginEdge
nav: Providers
network: true
overview: 'MarginEdge publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Orders API, Products API, and 2 more. Tagged areas include Restaurant, Back Office, Invoices, Inventory, and Accounting.


  The MarginEdge catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  MarginEdge''s developer surface includes authentication, documentation, pricing, support, engineering blog, and 10 more developer resources.'
plans:
- name: Marginedge Plans Pricing
  plan_count: 3
  slug: marginedge-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Marginedge Rate Limits
  slug: marginedge-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: MarginEdge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: marginedge-jsonschema-spectral-rules
- effective_rule_count: 84
  extends:
  - spectral:oas
  name: MarginEdge API Rules
  rule_count: 43
  severity_counts:
    error: 10
    hint: 0
    info: 11
    warn: 22
  slug: marginedge-spectral-rules
score:
  band: developing
  composite: 47.4
  delta: -5.9
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 67.8
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 21.1
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/marginedge/refs/heads/main/screenshots/marginedge-2026-06-20T184941.png
security:
- kind: authentication
  name: Marginedge Authentication
  slug: marginedge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marginedge Domain Security
  slug: marginedge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Marginedge Trust Center
  slug: marginedge-trust-center
  summary_line: SOC 2, PCI DSS
slug: marginedge
tags:
- Restaurant
- Back Office
- Invoices
- Inventory
- Accounting
- Reporting
website: https://www.marginedge.com/
---
