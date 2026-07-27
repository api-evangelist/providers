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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Magento Agentic Access
  operation_count: 38
  slug: magento-agentic-access
  summary_line: 38 operations · 22 acting
api_count: 16
apis:
- description: 'The Adobe Commerce GraphQL API offers a flexible, query-driven interface designed primarily for building headless storefronts and progressive web applications. It exposes a single endpoint and allows '
  name: Magento GraphQL API
  slug: graphql-api
- description: 'The Adobe Commerce SOAP API exposes the same service contracts as the REST API through a WSDL 1.2 interface compliant with WS-I 2.0 Basic Profile. It allows enterprise systems and legacy integrations '
  name: Magento SOAP API
  slug: soap-api
- description: Adobe Commerce Webhooks enable developers to configure synchronous HTTP callbacks that fire when specific events occur within a Commerce instance, allowing external systems to react in real time to st
  name: Adobe Commerce Webhooks
  slug: webhooks
- description: The Adobe Commerce Admin UI SDK enables App Builder developers to extend the Commerce Admin panel with custom menus, pages, and UI components built as out-of-process applications. Rather than modifyin
  name: Adobe Commerce Admin UI SDK
  slug: admin-ui-sdk
- description: Adobe Commerce Eventing provides an asynchronous event-driven integration framework that publishes Commerce business events to Adobe I/O Events, enabling App Builder applications and other Adobe Exper
  name: Adobe Commerce Eventing
  slug: events
- description: Endpoints for obtaining integration tokens for admin and customer users. Token-based authentication issues a Bearer token that must be included in the Authorization header of subsequent requests.
  name: magento Authentication API
  slug: magento-authentication-api
- description: Shopping cart and quote management for admin, customer, and guest users, including item management, coupon codes, shipping estimation, and payment information collection.
  name: magento Carts API
  slug: magento-carts-api
- description: Category tree management including creation, retrieval, update, and deletion of catalog categories and their product assignments.
  name: magento Categories API
  slug: magento-categories-api
- description: Customer account management including registration, profile updates, address management, authentication, and customer group assignment.
  name: magento Customers API
  slug: magento-customers-api
- description: Multi-source inventory management including sources, stocks, stock-source links, and source item quantity management.
  name: magento Inventory API
  slug: magento-inventory-api
- description: Invoice management for orders including invoice creation, retrieval, and payment capture operations.
  name: magento Invoices API
  slug: magento-invoices-api
- description: Sales order management including order retrieval, status updates, comment posting, cancellation, and order item management.
  name: magento Orders API
  slug: magento-orders-api
- description: Catalog product management including creation, retrieval, update, and deletion of simple, configurable, virtual, bundled, and grouped products. Supports product attributes, media, pricing rules, and c
  name: magento Products API
  slug: magento-products-api
- description: Shipment management for orders including shipment creation, retrieval, tracking number management, and shipment comments.
  name: magento Shipments API
  slug: magento-shipments-api
- description: Store configuration retrieval including store groups, store views, websites, and configuration settings.
  name: magento Stores API
  slug: magento-stores-api
- description: Tax configuration management including tax rates, tax rules, and tax classes used for order tax calculation.
  name: magento Tax API
  slug: magento-tax-api
artifact_total: 82
asyncapis:
- description: Adobe Commerce Eventing provides an asynchronous event-driven integration framework that publishes Commerce business events to Adobe I/O Events, enabling App Builder applications and other Adobe Exper
  name: Adobe Commerce Eventing
  slug: magento-events-asyncapi
- description: Adobe Commerce Webhooks enable developers to configure synchronous HTTP callbacks that fire when specific events occur within a Commerce instance, allowing external systems to react in real time to st
  name: Adobe Commerce Webhooks
  slug: magento-webhooks-asyncapi
collections:
- collection_type: open
  name: Magento REST API
  slug: open-magento-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magento-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/magento-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magento-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magento-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magento
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adobe-commerce
- group: design
  title: ''
  type: JSONLD
  url: json-ld/magento-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/magento-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/magento-product-schema.json
description: Overview of the Adobe Commerce and Magento Open Source REST API documentation.
features:
- 'Magento Open Source: free, self-hosted PHP commerce platform'
- 'Adobe Commerce: $22K-$125K+/year custom by AOV/GMV'
- 'Adobe Commerce Cloud: managed cloud with Fastly + AWS + New Relic'
- REST API and GraphQL API
- OAuth 2.0 + admin/customer/integration tokens
- Asynchronous and bulk APIs
- Webhooks for catalog, order, customer events
- B2B features (company accounts, quotes, requisitions)
- PWA Studio for headless storefronts
- Page Builder (drag-and-drop content)
- Adobe Sensei AI for product recommendations
- Multi-store, multi-warehouse, multi-currency
- Built-in Elasticsearch/OpenSearch
- Magento Marketplace for extensions
- Composer-based dependency management
- Cloud edition includes Fastly CDN, New Relic APM, AWS hosting
finops:
- name: Magento Finops
  service_category: E-Commerce Platform
  slug: magento-finops
graphqls:
- description: 'The Adobe Commerce GraphQL API offers a flexible, query-driven interface designed primarily for building headless storefronts and progressive web applications. It exposes a single endpoint and allows '
  name: magento GraphQL API
  slug: magento-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magento.png
json_schemas:
- name: Address
  property_count: 10
  slug: magento-address
- name: AdminTokenRequest
  property_count: 2
  slug: magento-admintokenrequest
- name: CartItem
  property_count: 7
  slug: magento-cartitem
- name: CartItemRequest
  property_count: 1
  slug: magento-cartitemrequest
- name: Category
  property_count: 12
  slug: magento-category
- name: CategoryRequest
  property_count: 1
  slug: magento-categoryrequest
- name: CategoryTree
  property_count: 0
  slug: magento-categorytree
- name: CustomAttribute
  property_count: 2
  slug: magento-customattribute
- name: Customer
  property_count: 11
  slug: magento-customer
- name: CustomerRequest
  property_count: 2
  slug: magento-customerrequest
- name: CustomerSearchResults
  property_count: 3
  slug: magento-customersearchresults
- name: CustomerTokenRequest
  property_count: 2
  slug: magento-customertokenrequest
- name: Error
  property_count: 2
  slug: magento-error
- name: InventorySource
  property_count: 11
  slug: magento-inventorysource
- name: InventorySourceRequest
  property_count: 1
  slug: magento-inventorysourcerequest
- name: InventorySourceSearchResults
  property_count: 2
  slug: magento-inventorysourcesearchresults
- name: Invoice
  property_count: 7
  slug: magento-invoice
- name: InvoiceRequest
  property_count: 3
  slug: magento-invoicerequest
- name: InvoiceSearchResults
  property_count: 2
  slug: magento-invoicesearchresults
- name: Magento Order
  property_count: 28
  slug: magento-order
- name: OrderCommentRequest
  property_count: 1
  slug: magento-ordercommentrequest
- name: OrderItem
  property_count: 10
  slug: magento-orderitem
- name: OrderRequest
  property_count: 1
  slug: magento-orderrequest
- name: OrderSearchResults
  property_count: 3
  slug: magento-ordersearchresults
- name: Magento Product
  property_count: 17
  slug: magento-product
- name: ProductRequest
  property_count: 2
  slug: magento-productrequest
- name: ProductSearchResults
  property_count: 3
  slug: magento-productsearchresults
- name: Shipment
  property_count: 5
  slug: magento-shipment
- name: ShipmentRequest
  property_count: 1
  slug: magento-shipmentrequest
- name: SourceItem
  property_count: 4
  slug: magento-sourceitem
- name: SourceItemSearchResults
  property_count: 2
  slug: magento-sourceitemsearchresults
- name: SourceItemUpdateRequest
  property_count: 1
  slug: magento-sourceitemupdaterequest
- name: StoreConfig
  property_count: 12
  slug: magento-storeconfig
- name: TaxRate
  property_count: 6
  slug: magento-taxrate
- name: TaxRateSearchResults
  property_count: 2
  slug: magento-taxratesearchresults
json_structures:
- name: Magento Structure
  property_count: 0
  slug: magento-structure
jsonld:
- class_count: 0
  name: Magento Context
  property_count: 8
  slug: magento-context
layout: provider
modified: '2026-05-19'
name: magento
nav: Providers
network: true
overview: 'magento publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Adobe Commerce Webhooks, Adobe Commerce Eventing, Authentication API, and 10 more.


  The magento catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  magento''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Magento Plans Pricing
  plan_count: 3
  slug: magento-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 3
  name: Magento Rate Limits
  slug: magento-rate-limits
rules:
- name: magento API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: magento-asyncapi-spectral-rules
- name: magento API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: magento-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.4
  delta: 2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.8
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 36.8
  previous_composite: 43.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magento/refs/heads/main/screenshots/magento-2026-06-20T184844.png
security:
- kind: authentication
  name: Magento Authentication
  slug: magento-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Magento Domain Security
  slug: magento-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Magento Vulnerability Disclosure
  slug: magento-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: magento
---
