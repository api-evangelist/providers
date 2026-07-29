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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 237
  human_in_the_loop: 11
  name: Fabric Com Agentic Access
  operation_count: 306
  slug: fabric-com-agentic-access
  summary_line: 306 operations · 237 acting · 11 human-in-the-loop
api_count: 61
apis:
- description: This endpoint helps perform additional operations for inventory management.
  name: fabric Actions Endpoints API
  slug: fabric-com-actions-endpoints-api
- description: Address endpoints are used to add add, update and remove addresses from the Cart.
  name: fabric Addresses API
  slug: fabric-com-addresses-api
- description: These endpoints help create appeasement requests.
  name: fabric Appeasements API
  slug: fabric-com-appeasements-api
- description: Item attributes are the objective and factual descriptions of items that shoppers see when they browse through your site. Attributes may be technical specifications like size, weight, etc., design spe
  name: fabric Attributes API
  slug: fabric-com-attributes-api
- description: These endpoints allow apps to authenticate themselves or their end users using fabric Identity. The main objective of these endpoints is to provide access tokens to applications, allowing them to invo
  name: fabric Authentication Endpoints API
  slug: fabric-com-authentication-endpoints-api
- description: Set of endpoints to help bulk import of items, bundles, categories and attributes through CSV files
  name: fabric Bulk Import API
  slug: fabric-com-bulk-import-api
- description: These endpoints check eligibility of order cancellation requests and if eligible, processes order cancellation.
  name: fabric Cancellations API
  slug: fabric-com-cancellations-api
- description: The Cart Actions API from fabric — 3 operation(s) for cart actions.
  name: fabric Cart Actions API
  slug: fabric-com-cart-actions-api
- description: Cart adjustment endpoints are used to add, update and remove adjustments at the Cart level.
  name: fabric Cart Adjustments API
  slug: fabric-com-cart-adjustments-api
- description: Cart endpoints are used to do basic cart operations, such as create a cart, add item to the corresponding cart, update items, remove items, delete cart, update status of the cart, and more.
  name: fabric Cart API
  slug: fabric-com-cart-api
- description: Cart fee endpoints are used to add, update and remove fees at the Cart level.
  name: fabric Cart Fees API
  slug: fabric-com-cart-fees-api
- description: CartPayments endpoints are used to authorize or void payments that are located within the shopping cart.
  name: fabric CartPayments API
  slug: fabric-com-cartpayments-api
- description: Cart endpoints are used to perform basic cart operations, such as create, update, delete and more.
  name: fabric Carts API
  slug: fabric-com-carts-api
- description: Retrieve an import template, import a file to the Catalog Connector, view import and export status, and download a previously processed file.
  name: fabric Catalog Connector Files API
  slug: fabric-com-catalog-connector-files-api
- description: Export data from the Catalog Connector and retrieve the status of previously processed files.
  name: fabric Catalog Connector Jobs API
  slug: fabric-com-catalog-connector-jobs-api
- description: Supports product operations based on Item ID.
  name: fabric Catalog Connector Operations by Item ID API
  slug: fabric-com-catalog-connector-operations-by-item-id-api
- description: Supports product operations based on Product ID.
  name: fabric Catalog Connector Operations by Product ID API
  slug: fabric-com-catalog-connector-operations-by-product-id-api
- description: Supports product operations based on SKU.
  name: fabric Catalog Connector Operations by SKU API
  slug: fabric-com-catalog-connector-operations-by-sku-api
- description: The Categories API from fabric — 2 operation(s) for categories.
  name: fabric Categories API
  slug: fabric-com-categories-api
- description: Categories (also called hierarchies or nodes) are hierarchical structures to organize items and services into intuitive groups. Organizing items in this way simplifies item discovery and lifecycle man
  name: fabric Category API
  slug: fabric-com-category-api
- description: The Checkout Session endpoint lets you create and complete a checkout session, and place an order for the cart items.
  name: fabric Checkout Session API
  slug: fabric-com-checkout-session-api
- description: Counter refers to inventory positions such as, available, in-transit, on-hand, or other custom positions. These endpoints let you read, update, and create custom counters that suit your business use c
  name: fabric Counters API
  slug: fabric-com-counters-api
- description: Coupon endpoints are used to add and remove coupons from the Cart
  name: fabric Coupons API
  slug: fabric-com-coupons-api
- description: Credits are refunds to customers, often in the form of gift cards or credit notes, when customers have made payments with cash or a card that has subsequently expired. Credits are provided during orde
  name: fabric Credits API
  slug: fabric-com-credits-api
- description: These endpoints provide the features for store admins to create and manage customers' addresses.
  name: fabric Customer Address API
  slug: fabric-com-customer-address-api
- description: Customer endpoints are used do basic customer operations, such as update a customer, add attributes and more.
  name: fabric Customer API
  slug: fabric-com-customer-api
- description: These endpoints provide the features for store admins to create and manage customers' details.
  name: fabric Customer Profile API
  slug: fabric-com-customer-profile-api
- description: These endpoints provide the feature for customers or shoppers to independently manage their details in the storefront.
  name: fabric Customer Self API
  slug: fabric-com-customer-self-api
- description: These endpoints deal with potential fraud orders.
  name: fabric Frauds API
  slug: fabric-com-frauds-api
- description: Fulfillment adjustments endpoints are used to add, update and remove adjustments at the Fulfillment level.
  name: fabric Fulfillment Adjustments API
  slug: fabric-com-fulfillment-adjustments-api
- description: Fulfillment fees endpoints are used to add, update and remove fees at the Fulfillment level.
  name: fabric Fulfillment Fees API
  slug: fabric-com-fulfillment-fees-api
- description: Fulfillment endpoints are used to add add, update and remove fulfillments from the Cart.
  name: fabric Fulfillments API
  slug: fabric-com-fulfillments-api
- description: Search for products based on the specified filter conditions.
  name: fabric General Catalog Connector Operations API
  slug: fabric-com-general-catalog-connector-operations-api
- description: XM Global Components API allows you to fetch all the live global component data
  name: fabric Global Components API
  slug: fabric-com-global-components-api
- description: fabric **Inventory** API lets organizations use *Inventory* as a standalone service, which functions as the repository of product availability for order fulfillment. Typically, Storefront Websites uti
  name: fabric Inventory API
  slug: fabric-com-inventory-api
- description: These endpoints help in performing inventory import file config operations
  name: fabric Inventory Import Configs API
  slug: fabric-com-inventory-import-configs-api
- description: Inventory Imports endpoints let you upload and download inventory details, in bulk, using a CSV file to and from AWS (Amazon Web Service) server presigned S3 URL that is generated from the Order servi
  name: fabric Inventory Imports API
  slug: fabric-com-inventory-imports-api
- description: fabric **Invoices** API helps in generating invoices that can be used by any third party system for order fulfillment operation.
  name: fabric Invoices API
  slug: fabric-com-invoices-api
- description: The Item Actions API from fabric — 3 operation(s) for item actions.
  name: fabric Item Actions API
  slug: fabric-com-item-actions-api
- description: Item adjustments endpoints are used to add, update and remove adjustments at the Item level.
  name: fabric Item Adjustments API
  slug: fabric-com-item-adjustments-api
- description: Item fee endpoints are used to add, update and remove fees at the Item level.
  name: fabric Item Fees API
  slug: fabric-com-item-fees-api
- description: Item endpoints are used to add, update and remove items from the Cart.
  name: fabric Items API
  slug: fabric-com-items-api
- description: LineItem endpoints are used to performbasic lineItem operations, such as create, update, delete and more.
  name: fabric LineItems API
  slug: fabric-com-lineitems-api
- description: XM Menu API allows you to fetch menus and their items
  name: fabric Menu API
  slug: fabric-com-menu-api
- description: Network refers to a group of locations having a group of SKUs in each location. These endpoints let you read, create, and manage an inventory-network by location, brand, or any other custom attributes
  name: fabric Networks API
  slug: fabric-com-networks-api
- description: The Optimize API from fabric — 4 operation(s) for optimize.
  name: fabric Optimize API
  slug: fabric-com-optimize-api
- description: Order draft endpoints are used to create an order draft or get a generated order draft.
  name: fabric OrderDrafts API
  slug: fabric-com-orderdrafts-api
- description: These endpoints create orders, update pickup details (for BOPIS scenarios) and get order details.
  name: fabric Orders API
  slug: fabric-com-orders-api
- description: XM Pages API allows you to fetch all the live pages, or a live page by a specific URL
  name: fabric Pages API
  slug: fabric-com-pages-api
- description: Payments endpoints are used to add add, update and remove payments from the Cart.
  name: fabric Payments API
  slug: fabric-com-payments-api
- description: The Platform API from fabric — 1 operation(s) for platform.
  name: fabric Platform API
  slug: fabric-com-platform-api
- description: The Prices API from fabric — 4 operation(s) for prices.
  name: fabric Prices API
  slug: fabric-com-prices-api
- description: '**Product**, a subset of Product Catalog endpoints, aims at making item management more efficient. They create, update, and get items, which may be individual items or collection of items (called bund'
  name: fabric Product API
  slug: fabric-com-product-api
- description: The Promotions API from fabric — 5 operation(s) for promotions.
  name: fabric Promotions API
  slug: fabric-com-promotions-api
- description: The Real-time Pricing Engine API from fabric — 3 operation(s) for real-time pricing engine.
  name: fabric Real-time Pricing Engine API
  slug: fabric-com-real-time-pricing-engine-api
- description: These endpoints help in performing reserved network operations
  name: fabric ReservedNetwork Endpoints API
  slug: fabric-com-reservednetwork-endpoints-api
- description: These endpoints check eligibility of order return or exchanges requests and, if eligible, processes order return or exchanges.
  name: fabric Returns API
  slug: fabric-com-returns-api
- description: fabric **Shipments** API is a multi-tenant service that enables you to manage shipments for existing 'Allocations.' Shipments serve as records of the locations from which an order was fulfilled. Typic
  name: fabric Shipments API
  slug: fabric-com-shipments-api
- description: These endpoints track orders.
  name: fabric Tracking API
  slug: fabric-com-tracking-api
- description: The transfer-shipment-controller API from fabric — 9 operation(s) for transfer-shipment-controller.
  name: fabric transfer-shipment-controller API
  slug: fabric-com-transfer-shipment-controller-api
- description: Validation endpoints are used to pass in data from fabric and third-party services to perform business logic on the Cart
  name: fabric Validations API
  slug: fabric-com-validations-api
artifact_total: 96
collections:
- collection_type: open
  name: Cart API
  slug: open-fabric-cart
- collection_type: open
  name: Catalog - Connector
  slug: open-fabric-catalog
- collection_type: open
  name: Checkout
  slug: open-fabric-checkout
- collection_type: open
  name: Customers
  slug: open-fabric-customers
- collection_type: open
  name: Experiences v2 (XM v2)
  slug: open-fabric-experiences
- collection_type: open
  name: Authentication v3
  slug: open-fabric-identity
- collection_type: open
  name: fabric Inventory API
  slug: open-fabric-inventory
- collection_type: open
  name: Orders - Invoices API
  slug: open-fabric-invoices
- collection_type: open
  name: Offers - Prices
  slug: open-fabric-offers-prices
- collection_type: open
  name: Offers - Real-time Pricing Engine
  slug: open-fabric-offers-pricing
- collection_type: open
  name: Offers - Promotions
  slug: open-fabric-offers-promotions
- collection_type: open
  name: fabric Orders API
  slug: open-fabric-orders
- collection_type: open
  name: Product Catalog
  slug: open-fabric-pim
- collection_type: open
  name: fabric Orders API
  slug: open-fabric-product-agent
- collection_type: open
  name: Orders - Shipments API
  slug: open-fabric-shipments
- collection_type: open
  name: Cart Orchestrator API
  slug: open-fabric-shopperxp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fabric-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fabric-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fabric-com-authentication.yml
- group: start
  title: ''
  type: Signup
  url: https://fabric.inc/request-demo
- group: start
  title: ''
  type: Portal
  url: https://developer.fabric.inc/home
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fabric.inc/v3/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fabric.inc/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: https://developer.fabric.inc/v3/api-reference/identity
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.fabric.inc/release-notes
- group: company
  title: ''
  type: Blog
  url: https://fabric.inc/blog
- group: company
  title: ''
  type: About
  url: https://fabric.inc/company/about
- group: operate
  title: ''
  type: ContactUs
  url: https://fabric.inc/contact-us
- group: build
  title: ''
  type: GitHub
  url: https://github.com/FabricCommerce
- group: build
  title: ''
  type: Postman
  url: https://github.com/FabricCommerce/public-fabric-api-postman-collections
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fabricinc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/fabriccommerce
- group: company
  title: ''
  type: PressRoom
  url: https://fabric.inc/news
- group: commercial
  title: ''
  type: Plans
  url: plans/fabric-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fabric-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fabric-com-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fabric-com-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fabric-com-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/fabric-com-rules.yml
created: '2026-05-25'
examples:
- key_count: 2
  name: Fabric Create Cart Example
  slug: fabric-create-cart-example
- key_count: 2
  name: Fabric Evaluate Cart Pricing Example
  slug: fabric-evaluate-cart-pricing-example
- key_count: 2
  name: Fabric Toggle Promotion Example
  slug: fabric-toggle-promotion-example
- key_count: 2
  name: Fabric Update Order Status Example
  slug: fabric-update-order-status-example
finops:
- name: Fabric Com Finops
  service_category: ''
  slug: fabric-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fabric-com.png
json_schemas:
- name: fabric Cart
  property_count: 8
  slug: fabric-cart
- name: fabric Order
  property_count: 14
  slug: fabric-order
- name: fabric Product
  property_count: 10
  slug: fabric-product
- name: fabric Promotion
  property_count: 12
  slug: fabric-promotion
json_structures:
- name: Fabric Order Structure
  property_count: 0
  slug: fabric-order-structure
- name: Fabric Product Structure
  property_count: 0
  slug: fabric-product-structure
jsonld:
- class_count: 32
  name: Fabric Com Context
  property_count: 5
  slug: fabric-com-context
layout: provider
modified: '2026-05-25'
name: fabric
nav: Providers
network: true
overview: 'fabric publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Actions Endpoints API, Addresses API, Appeasements API, and 58 more. Tagged areas include Commerce, Composable Commerce, Headless Commerce, E-commerce, and Retail.


  The fabric catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  fabric''s developer surface includes authentication, signup flow, developer portal, documentation, changelog, engineering blog, GitHub presence, and 16 more developer resources.'
plans:
- name: Fabric Com Plans Pricing
  plan_count: 2
  slug: fabric-com-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 0
  name: Fabric Com Rate Limits
  slug: fabric-com-rate-limits
rules:
- name: fabric API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fabric-com-jsonschema-spectral-rules
- name: fabric API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: fabric-com-rules
score:
  band: thin
  composite: 41.8
  delta: -4.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.5
    developer_ergonomics: 34.8
    discoverability: 40.7
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 61
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fabric-com/refs/heads/main/screenshots/fabric-com-2026-06-20T181000.png
security:
- kind: authentication
  name: Fabric Com Authentication
  slug: fabric-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fabric Com Domain Security
  slug: fabric-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fabric-com
tags:
- Commerce
- Composable Commerce
- Headless Commerce
- E-commerce
- Retail
- Cart
- Catalog
- PIM
- OMS
- Inventory
- Offers
- Pricing
- Promotions
- Checkout
- Identity
- Experiences
- Agentic Commerce
website: https://developer.fabric.inc/home
---
