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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Bluecart Agentic Access
  operation_count: 22
  slug: bluecart-agentic-access
  summary_line: 22 operations · 13 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: Manage client-specific catalogs of products and pricing.
  name: BlueCart Catalogs API
  slug: bluecart-catalogs-api
- description: Manage buyer/client associations and their account details.
  name: BlueCart Clients API
  slug: bluecart-clients-api
- description: Search, retrieve, place, and modify wholesale orders.
  name: BlueCart Orders API
  slug: bluecart-orders-api
- description: Manage the product catalog including pricing and inventory.
  name: BlueCart Products API
  slug: bluecart-products-api
- description: Manage platform users and their roles and notifications.
  name: BlueCart Users API
  slug: bluecart-users-api
artifact_total: 78
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BlueCart Catalogs API
  slug: open-bluecart-catalogs-api
- collection_type: open
  name: BlueCart Catalogs Clients API
  slug: open-bluecart-clients-api
- collection_type: open
  name: BlueCart Catalogs Orders API
  slug: open-bluecart-orders-api
- collection_type: open
  name: BlueCart Catalogs Products API
  slug: open-bluecart-products-api
- collection_type: open
  name: BlueCart Catalogs Users API
  slug: open-bluecart-users-api
- collection_type: open
  name: BlueCart API
  slug: open-bluecart
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bluecart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluecart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluecart-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluecart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bluecart.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bluecart.com/endpoints
- group: auth
  title: ''
  type: Authentication
  url: https://docs.bluecart.com/authentication
- group: design
  title: ''
  type: Pagination
  url: https://docs.bluecart.com/pagination
- group: operate
  title: ''
  type: Support
  url: https://www.bluecart.com/contact
- group: start
  title: ''
  type: Signup
  url: https://www.bluecart.com/
- group: design
  title: ''
  type: Rules
  url: rules/bluecart-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bluecart-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bluecart-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/bluecart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bluecart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bluecart-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bluecart.com/blog
created: '2026-06-02'
description: BlueCart is an end-to-end eCommerce and procurement platform for the hospitality and food and beverage industries, connecting restaurants and buyers with wholesale distributors and suppliers. It streamlines wholesale ordering, order management, inventory, and payments for both sides of the supply chain. BlueCart exposes a public REST API that lets distributors and partners programmatically manage products, orders, customers, catalogs, and users, returning JSON responses and integrating BlueCart data with external accounting, eCommerce, and logistics systems used across foodservice operations.
examples:
- key_count: 3
  name: Bluecart Catalog Create Example
  slug: bluecart-catalog-create-example
- key_count: 5
  name: Bluecart Catalog Example
  slug: bluecart-catalog-example
- key_count: 2
  name: Bluecart Catalog List Example
  slug: bluecart-catalog-list-example
- key_count: 4
  name: Bluecart Catalog Update Example
  slug: bluecart-catalog-update-example
- key_count: 9
  name: Bluecart Client Create Example
  slug: bluecart-client-create-example
- key_count: 13
  name: Bluecart Client Example
  slug: bluecart-client-example
- key_count: 9
  name: Bluecart Client Update Example
  slug: bluecart-client-update-example
- key_count: 9
  name: Bluecart Order Create Example
  slug: bluecart-order-create-example
- key_count: 2
  name: Bluecart Order Create Result Example
  slug: bluecart-order-create-result-example
- key_count: 15
  name: Bluecart Order Example
  slug: bluecart-order-example
- key_count: 2
  name: Bluecart Order List Example
  slug: bluecart-order-list-example
- key_count: 5
  name: Bluecart Order Product Example
  slug: bluecart-order-product-example
- key_count: 10
  name: Bluecart Order Update Example
  slug: bluecart-order-update-example
- key_count: 9
  name: Bluecart Product Create Example
  slug: bluecart-product-create-example
- key_count: 12
  name: Bluecart Product Example
  slug: bluecart-product-example
- key_count: 2
  name: Bluecart Product List Example
  slug: bluecart-product-list-example
- key_count: 9
  name: Bluecart User Create Example
  slug: bluecart-user-create-example
- key_count: 12
  name: Bluecart User Example
  slug: bluecart-user-example
- key_count: 2
  name: Bluecart User List Example
  slug: bluecart-user-list-example
finops:
- name: Bluecart Finops
  service_category: Wholesale Commerce + Procurement
  slug: bluecart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluecart.png
json_schemas:
- name: CatalogCreate
  property_count: 3
  slug: bluecart-catalog-create
- name: CatalogList
  property_count: 2
  slug: bluecart-catalog-list
- name: Catalog
  property_count: 5
  slug: bluecart-catalog
- name: CatalogUpdate
  property_count: 4
  slug: bluecart-catalog-update
- name: ClientCreate
  property_count: 9
  slug: bluecart-client-create
- name: Client
  property_count: 13
  slug: bluecart-client
- name: ClientUpdate
  property_count: 9
  slug: bluecart-client-update
- name: OrderCreateResult
  property_count: 2
  slug: bluecart-order-create-result
- name: OrderCreate
  property_count: 9
  slug: bluecart-order-create
- name: OrderList
  property_count: 2
  slug: bluecart-order-list
- name: OrderProduct
  property_count: 5
  slug: bluecart-order-product
- name: Order
  property_count: 15
  slug: bluecart-order
- name: OrderUpdate
  property_count: 10
  slug: bluecart-order-update
- name: ProductCreate
  property_count: 9
  slug: bluecart-product-create
- name: ProductList
  property_count: 2
  slug: bluecart-product-list
- name: Product
  property_count: 12
  slug: bluecart-product
- name: UserCreate
  property_count: 9
  slug: bluecart-user-create
- name: UserList
  property_count: 2
  slug: bluecart-user-list
- name: User
  property_count: 12
  slug: bluecart-user
json_structures:
- name: Bluecart Catalog Create Structure
  property_count: 3
  slug: bluecart-catalog-create-structure
- name: Bluecart Catalog List Structure
  property_count: 2
  slug: bluecart-catalog-list-structure
- name: Bluecart Catalog Structure
  property_count: 5
  slug: bluecart-catalog-structure
- name: Bluecart Catalog Update Structure
  property_count: 4
  slug: bluecart-catalog-update-structure
- name: Bluecart Client Create Structure
  property_count: 9
  slug: bluecart-client-create-structure
- name: Bluecart Client Structure
  property_count: 13
  slug: bluecart-client-structure
- name: Bluecart Client Update Structure
  property_count: 9
  slug: bluecart-client-update-structure
- name: Bluecart Order Create Result Structure
  property_count: 2
  slug: bluecart-order-create-result-structure
- name: Bluecart Order Create Structure
  property_count: 9
  slug: bluecart-order-create-structure
- name: Bluecart Order List Structure
  property_count: 2
  slug: bluecart-order-list-structure
- name: Bluecart Order Product Structure
  property_count: 5
  slug: bluecart-order-product-structure
- name: Bluecart Order Structure
  property_count: 15
  slug: bluecart-order-structure
- name: Bluecart Order Update Structure
  property_count: 10
  slug: bluecart-order-update-structure
- name: Bluecart Product Create Structure
  property_count: 9
  slug: bluecart-product-create-structure
- name: Bluecart Product List Structure
  property_count: 2
  slug: bluecart-product-list-structure
- name: Bluecart Product Structure
  property_count: 12
  slug: bluecart-product-structure
- name: Bluecart User Create Structure
  property_count: 9
  slug: bluecart-user-create-structure
- name: Bluecart User List Structure
  property_count: 2
  slug: bluecart-user-list-structure
- name: Bluecart User Structure
  property_count: 12
  slug: bluecart-user-structure
jsonld:
- class_count: 19
  name: Bluecart Context
  property_count: 60
  slug: bluecart-context
layout: provider
modified: '2026-06-02'
name: BlueCart
nav: Providers
network: true
overview: 'BlueCart publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalogs API, Clients API, Orders API, and 2 more. Tagged areas include Restaurant, Procurement, Wholesale, Ordering, and Food Distribution.


  The BlueCart catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BlueCart''s developer surface includes authentication, documentation, API reference, support, signup flow, engineering blog, and 11 more developer resources.'
plans:
- name: Bluecart Plans Pricing
  plan_count: 3
  slug: bluecart-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Bluecart Rate Limits
  slug: bluecart-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BlueCart API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bluecart-jsonschema-spectral-rules
- effective_rule_count: 85
  extends:
  - spectral:oas
  name: BlueCart API Rules
  rule_count: 44
  severity_counts:
    error: 8
    hint: 0
    info: 14
    warn: 22
  slug: bluecart-spectral-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 32.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 28.8
    contract_quality: 25.2
    developer_ergonomics: 47.6
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 31.6
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluecart/refs/heads/main/screenshots/bluecart-2026-06-20T173530.png
security:
- kind: authentication
  name: Bluecart Authentication
  slug: bluecart-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bluecart Domain Security
  slug: bluecart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluecart
tags:
- Restaurant
- Procurement
- Wholesale
- Ordering
- Food Distribution
- Hospitality
- E-Commerce
website: https://www.bluecart.com/
---
