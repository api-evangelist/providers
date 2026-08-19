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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Oracle Retail Agentic Access
  operation_count: 16
  slug: oracle-retail-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 10
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
- description: Fulfillment and sourcing operations
  name: Oracle Retail Fulfillment API
  slug: oracle-retail-fulfillment-api
- description: Inventory and stock on hand
  name: Oracle Retail Inventory API
  slug: oracle-retail-inventory-api
- description: Item setup and attributes
  name: Oracle Retail Items API
  slug: oracle-retail-items-api
- description: Customer order management
  name: Oracle Retail Orders API
  slug: oracle-retail-orders-api
- description: Purchase order management
  name: Oracle Retail PurchaseOrders API
  slug: oracle-retail-purchaseorders-api
- description: Returns and refunds management
  name: Oracle Retail Returns API
  slug: oracle-retail-returns-api
- description: Supplier management
  name: Oracle Retail Suppliers API
  slug: oracle-retail-suppliers-api
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
  name: API Collection
  slug: open-.refine-report
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-retail/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-retail-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-retail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-retail-authentication.yml
- group: auth
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
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-retail-merchandising-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-retail-order-management-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/oracle-retail-item-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/oracle-retail-order-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/oracle-retail-context.jsonld
created: '2024-01-01'
description: Oracle Retail is a suite of cloud and on-premises applications for retailers spanning merchandising, pricing, supply chain, omnichannel order management, point of service, and store operations. Oracle Retail APIs provide REST, messaging, and integration services for managing the full retail lifecycle across digital and physical channels.
finops:
- name: Oracle Retail Finops
  service_category: Retail Applications
  slug: oracle-retail-finops
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
  property_count: 0
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
  property_count: 0
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
modified: '2026-05-19'
name: Oracle Retail
nav: Providers
network: true
overview: 'Oracle Retail publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Fulfillment API, Inventory API, Items API, and 4 more. Tagged areas include Retail, Merchandising, Order Management, Pricing, and Inventory.


  The Oracle Retail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle Retail''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 16 more developer resources.'
plans:
- name: Oracle Retail Plans Pricing
  plan_count: 3
  slug: oracle-retail-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 3
  name: Oracle Retail Rate Limits
  slug: oracle-retail-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Oracle Retail API Rules
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
  composite: 41.9
  delta: -6.7
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 61.4
    developer_ergonomics: 40.5
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-retail/refs/heads/main/screenshots/oracle-retail-2026-06-20T191144.png
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
- Point of Sale
- Omnichannel
- Oracle
website: https://www.oracle.com/retail/
---
