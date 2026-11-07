---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Oracle Retail Agentic Access
  operation_count: 16
  slug: oracle-retail-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 2
apis:
- description: Oracle Retail Pricing Cloud Service provides REST APIs for regular price management, promotional pricing, competitive pricing, and clearance pricing across retail operations.
  name: Oracle Retail Pricing Cloud Service API
  slug: oracle-retail-pricing-cloud-service-api
- description: Oracle Retail Integration Cloud Service (RIB and BDI) provides messaging and bulk data integration APIs connecting Oracle Retail applications to third-party systems using enterprise messaging patterns
  name: Oracle Retail Integration Cloud Service API
  slug: oracle-retail-integration-cloud-service-api
- description: Oracle Retail Xstore Point of Service provides APIs for store operations including transactions, inventory lookup, customer management, and omnichannel fulfillment from retail store systems.
  name: Oracle Retail Xstore Point of Service API
  slug: oracle-retail-xstore-point-of-service-api
- baseURL: https://{host}/MerchServices/MerchRes/v1
  baseurl_source: declared
  description: Fulfillment and sourcing operations
  name: Oracle Retail Fulfillment API
  slug: oracle-retail-fulfillment-api
- baseURL: https://{host}/MerchServices/MerchRes/v1
  baseurl_source: declared
  description: Inventory and stock on hand
  name: Oracle Retail Inventory API
  slug: oracle-retail-inventory-api
- baseURL: https://{host}/MerchServices/MerchRes/v1
  baseurl_source: declared
  description: Item setup and attributes
  name: Oracle Retail Items API
  slug: oracle-retail-items-api
- baseURL: https://{host}/MerchServices/MerchRes/v1
  baseurl_source: declared
  description: Customer order management
  name: Oracle Retail Orders API
  slug: oracle-retail-orders-api
- baseURL: https://{host}/MerchServices/MerchRes/v1
  baseurl_source: declared
  description: Returns and refunds management
  name: Oracle Retail Returns API
  slug: oracle-retail-returns-api
- baseURL: https://{host}/MerchServices/MerchRes/v1
  baseurl_source: declared
  description: Supplier management
  name: Oracle Retail Suppliers API
  slug: oracle-retail-suppliers-api
- baseURL: https://{host}/MerchServices/MerchRes/v1
  baseurl_source: declared
  description: Purchase order management
  name: Oracle Retail Purchase Orders API
  slug: oracle-retail-purchase-orders-api
artifact_total: 57
collections:
- collection_type: postman
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment API
  slug: postman-oracle-retail-fulfillment-api
- collection_type: postman
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Inventory API
  slug: postman-oracle-retail-inventory-api
- collection_type: postman
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Items API
  slug: postman-oracle-retail-items-api
- collection_type: postman
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Orders API
  slug: postman-oracle-retail-orders-api
- collection_type: postman
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment PurchaseOrders API
  slug: postman-oracle-retail-purchaseorders-api
- collection_type: postman
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Returns API
  slug: postman-oracle-retail-returns-api
- collection_type: postman
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Suppliers API
  slug: postman-oracle-retail-suppliers-api
- collection_type: open
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment API
  slug: open-oracle-retail-fulfillment-api
- collection_type: open
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Inventory API
  slug: open-oracle-retail-inventory-api
- collection_type: open
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Items API
  slug: open-oracle-retail-items-api
- collection_type: open
  name: Oracle Retail Merchandising Foundation Cloud Service API
  slug: open-oracle-retail-merchandising
- collection_type: open
  name: Oracle Retail Order Management Suite Cloud Service API
  slug: open-oracle-retail-order-management
- collection_type: open
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Orders API
  slug: open-oracle-retail-orders-api
- collection_type: open
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment PurchaseOrders API
  slug: open-oracle-retail-purchaseorders-api
- collection_type: open
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Returns API
  slug: open-oracle-retail-returns-api
- collection_type: open
  name: Oracle Retail Merchandising Foundation Cloud Service Fulfillment Suppliers API
  slug: open-oracle-retail-suppliers-api
common:
- group: commercial
  href: https://artifacts.apis.io/oracle-retail/finops/oracle-retail-finops.yml
  title: ''
  type: FinOps
  url: finops/oracle-retail-finops.yml
- group: operate
  href: https://artifacts.apis.io/oracle-retail/rate-limits/oracle-retail-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/oracle-retail-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/industries/payg-services-price-list/
- group: commercial
  href: https://artifacts.apis.io/oracle-retail/plans/oracle-retail-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oracle-retail-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/oracle-retail/capabilities/oracle-retail-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-retail-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-retail/overview
- group: agent
  href: https://artifacts.apis.io/oracle-retail/agentic-access/oracle-retail-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-retail-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/oracle-retail/security/oracle-retail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oracle-retail-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/oracle-retail/authentication/oracle-retail-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oracle-retail-authentication.yml
- group: auth
  href: https://artifacts.apis.io/oracle-retail/scopes/oracle-retail-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/oracle-retail-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/oracle-retail
- group: start
  title: ''
  type: Portal
  url: https://docs.oracle.com/en/industries/retail/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/industries/retail/
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/retail/
- group: operate
  title: ''
  type: Support
  url: https://community.oracle.com/gbu/rgbu/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/retail/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.oracle.com/developer/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: docs
  href: https://artifacts.apis.io/oracle-retail/openapi/_original/oracle-retail-merchandising-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-retail-merchandising-openapi.yml
- group: docs
  href: https://artifacts.apis.io/oracle-retail/openapi/_original/oracle-retail-order-management-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-retail-order-management-openapi.yml
- group: docs
  href: https://artifacts.apis.io/oracle-retail/json-schema/oracle-retail-item-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/oracle-retail-item-schema.json
- group: docs
  href: https://artifacts.apis.io/oracle-retail/json-schema/oracle-retail-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/oracle-retail-order-schema.json
- group: design
  href: https://artifacts.apis.io/oracle-retail/json-ld/oracle-retail-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/oracle-retail-context.jsonld
created: '2024-01-01'
description: Oracle Retail is a suite of cloud and on-premises applications for retailers spanning merchandising, pricing, supply chain, omnichannel order management, point of service, and store operations. Oracle Retail APIs provide REST, messaging, and integration services for managing the full retail lifecycle across digital and physical channels.
finops:
- has_sources: true
  method: derived
  name: Oracle Retail Finops
  primary_unit: processed payment amount
  service_category: ''
  slug: oracle-retail-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-retail.png
json_schemas:
- name: Address
  property_count: 10
  slug: oracle-retail-address
- name: Error
  property_count: 3
  slug: oracle-retail-error
- name: InventoryPosition
  property_count: 9
  slug: oracle-retail-inventoryposition
- name: Oracle Retail Item
  property_count: 19
  slug: oracle-retail-item
- name: ItemCreate
  property_count: 8
  slug: oracle-retail-itemcreate
- name: ItemUpdate
  property_count: 3
  slug: oracle-retail-itemupdate
- name: Oracle Retail Order
  property_count: 17
  slug: oracle-retail-order
- name: OrderCreate
  property_count: 6
  slug: oracle-retail-ordercreate
- name: OrderDetail
  property_count: 1
  slug: oracle-retail-orderdetail
- name: OrderLine
  property_count: 8
  slug: oracle-retail-orderline
- name: OrderLineCreate
  property_count: 4
  slug: oracle-retail-orderlinecreate
- name: OrderUpdate
  property_count: 3
  slug: oracle-retail-orderupdate
- name: PurchaseOrder
  property_count: 13
  slug: oracle-retail-purchaseorder
- name: PurchaseOrderCreate
  property_count: 7
  slug: oracle-retail-purchaseordercreate
- name: PurchaseOrderDetail
  property_count: 1
  slug: oracle-retail-purchaseorderdetail
- name: PurchaseOrderLine
  property_count: 10
  slug: oracle-retail-purchaseorderline
- name: Return
  property_count: 5
  slug: oracle-retail-return
- name: ReturnCreate
  property_count: 2
  slug: oracle-retail-returncreate
- name: ShipmentRequest
  property_count: 6
  slug: oracle-retail-shipmentrequest
- name: Supplier
  property_count: 15
  slug: oracle-retail-supplier
json_structures:
- name: Oracle Retail Structure
  property_count: 0
  slug: oracle-retail-structure
jsonld:
- class_count: 0
  name: Oracle Retail Context
  property_count: 30
  slug: oracle-retail-context
layout: provider
modified: '2026-08-21'
name: Oracle Retail
nav: Providers
network: true
overview: 'Oracle Retail publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Fulfillment API, Inventory API, Items API, and 7 more. Tagged areas include Retail, Merchandising, Order Management, Pricing, and Inventory.


  The Oracle Retail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle Retail''s developer surface includes pricing, authentication, developer portal, documentation, support, engineering blog, and 21 more developer resources.'
plans:
- name: Oracle Retail Plans Pricing
  plan_count: 10
  slug: oracle-retail-plans-pricing
- name: Oracle Retail Price Estimates
  plan_count: 0
  slug: oracle-retail-price-estimates
random_paper: 20
rate_limits:
- limit_count: 0
  name: Oracle Retail Rate Limits
  slug: oracle-retail-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Oracle Retail — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oracle-retail-jsonschema-spectral-rules
scopes:
- name: Oracle Retail Scopes
  scope_count: 4
  slug: oracle-retail-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 58.3
    catalog_earned_first_party: 12.0
    catalog_gap: 56.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 65.8
    contract_governance: 9.8
    contract_quality: 54.3
    developer_ergonomics: 44.0
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/oracle-retail/oracle-retail-2026-06-20T191144.png
security:
- kind: authentication
  name: Oracle Retail Authentication
  slug: oracle-retail-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Oracle Retail Domain Security
  slug: oracle-retail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-retail
tags:
- Retail
- Merchandising
- Order Management
- Pricing
- Inventory
- Point-of-Sale
- Omnichannel
- Oracle
website: https://www.oracle.com/retail/
---
