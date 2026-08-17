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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Commercetools Agentic Access
  operation_count: 54
  slug: commercetools-agentic-access
  summary_line: 54 operations · 31 acting
api_count: 19
apis:
- description: The commercetools GraphQL API provides a flexible, network-efficient alternative to the HTTP API for querying and mutating Composable Commerce resources. It exposes a single endpoint and allows client
  name: Commercetools GraphQL API
  slug: graphql-api
- description: The commercetools TypeScript SDK is the official client library for interacting with the Composable Commerce HTTP API, Import API, and GraphQL API from JavaScript and TypeScript applications. It provi
  name: Commercetools TypeScript SDK
  slug: typescript-sdk
- description: The commercetools Java SDK is the official client library for accessing the Composable Commerce APIs from Java applications. It provides strongly typed request builders, automatic OAuth 2.0 token mana
  name: Commercetools Java SDK
  slug: java-sdk
- description: The commercetools Checkout API provides programmatic control over Checkout application configurations within Composable Commerce. The Checkout Applications API allows developers to create, update, and
  name: Commercetools Checkout API
  slug: checkout-api
- description: The commercetools Merchant Center Customizations API provides the programmatic interface for building custom applications and UI extensions within the Merchant Center. It exposes proxy endpoints to un
  name: Commercetools Merchant Center Customizations API
  slug: merchant-center-customizations-api
- description: Manage shopping carts with line items, discounts, shipping, and tax calculations.
  name: commercetools Carts API
  slug: commercetools-carts-api
- description: Organize products into hierarchical category structures.
  name: commercetools Categories API
  slug: commercetools-categories-api
- description: Query the audit log of resource changes across the project.
  name: commercetools ChangeHistory API
  slug: commercetools-changehistory-api
- description: Manage customer accounts, addresses, authentication, and group assignments.
  name: commercetools Customers API
  slug: commercetools-customers-api
- description: Manage import containers that hold import requests before processing.
  name: commercetools ImportContainers API
  slug: commercetools-importcontainers-api
- description: Monitor the status of individual import operations.
  name: commercetools ImportOperations API
  slug: commercetools-importoperations-api
- description: Manage inventory entries tracking stock levels per channel and SKU.
  name: commercetools Inventory API
  slug: commercetools-inventory-api
- description: Create and manage orders resulting from cart checkouts or quotes.
  name: commercetools Orders API
  slug: commercetools-orders-api
- description: Track payment transactions and PSP interactions associated with orders.
  name: commercetools Payments API
  slug: commercetools-payments-api
- description: Manage product catalog entries including variants, images, prices, and attributes.
  name: commercetools Products API
  slug: commercetools-products-api
- description: Import product variant resources into the project.
  name: commercetools ProductVariants API
  slug: commercetools-productvariants-api
- description: Read and configure project-level settings including currencies, languages, and messages.
  name: commercetools Project API
  slug: commercetools-project-api
- description: Import standalone price resources into the project.
  name: commercetools StandalonePrices API
  slug: commercetools-standaloneprices-api
- description: The Subscriptions API from commercetools — 2 operation(s) for subscriptions.
  name: commercetools Subscriptions API
  slug: commercetools-subscriptions-api
artifact_total: 144
asyncapis:
- description: The commercetools Subscriptions system delivers real-time change notifications and domain messages to external message queue destinations when resources are created, updated, or deleted within a Compo
  name: commercetools Subscriptions Events
  slug: commercetools-subscriptions-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: commercetools Change History Carts API
  slug: open-commercetools-carts-api
- collection_type: open
  name: commercetools Change History Carts Categories API
  slug: open-commercetools-categories-api
- collection_type: open
  name: commercetools Change History API
  slug: open-commercetools-change-history-api
- collection_type: open
  name: commercetools Change History Carts ChangeHistory API
  slug: open-commercetools-changehistory-api
- collection_type: open
  name: commercetools Change History Carts Customers API
  slug: open-commercetools-customers-api
- collection_type: open
  name: commercetools HTTP API
  slug: open-commercetools-http-api
- collection_type: open
  name: commercetools Import API
  slug: open-commercetools-import-api
- collection_type: open
  name: commercetools Change History Carts ImportContainers API
  slug: open-commercetools-importcontainers-api
- collection_type: open
  name: commercetools Change History Carts ImportOperations API
  slug: open-commercetools-importoperations-api
- collection_type: open
  name: commercetools Change History Carts Inventory API
  slug: open-commercetools-inventory-api
- collection_type: open
  name: commercetools Change History Carts Orders API
  slug: open-commercetools-orders-api
- collection_type: open
  name: commercetools Change History Carts Payments API
  slug: open-commercetools-payments-api
- collection_type: open
  name: commercetools Change History Carts Products API
  slug: open-commercetools-products-api
- collection_type: open
  name: commercetools Change History Carts ProductVariants API
  slug: open-commercetools-productvariants-api
- collection_type: open
  name: commercetools Change History Carts Project API
  slug: open-commercetools-project-api
- collection_type: open
  name: commercetools Change History Carts StandalonePrices API
  slug: open-commercetools-standaloneprices-api
- collection_type: open
  name: commercetools Change History Carts Subscriptions API
  slug: open-commercetools-subscriptions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/commercetools-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/commercetools-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commercetools-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/commercetools-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commercetools
- group: company
  title: ''
  type: Website
  url: https://commercetools.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.commercetools.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://commercetools.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.commercetools.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/commercetools
- group: design
  title: ''
  type: JSONLD
  url: json-ld/commercetools-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/commercetools-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/commercetools-product-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/commercetools-subscription-message-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/commercetools-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://commercetools.com/blog
created: '2025-09-15'
description: commercetools is the leading composable, headless, API-first Commerce platform powering large-scale B2C, B2B, and marketplace digital commerce for enterprise brands. The platform exposes a broad API surface organized into the HTTP API (core REST interface), GraphQL API (flexible query and mutation alternative), Import API (bulk data ingestion), Change History API (audit log), Checkout API (managed checkout configuration), and Merchant Center Customizations API (custom UI extensions). It is complemented by official SDKs (TypeScript, Java, PHP, .NET, Python) and AsyncAPI-based subscriptions for event-driven integrations.
features:
- 'Core Commerce Edition: Composable Commerce APIs (custom price)'
- 'Foundry Edition: includes Frontend + Checkout + Blueprints + Expert Services'
- 'Premium Edition: unlimited SKUs, B2B APIs, Audit Log Premium'
- Headless / API-first commerce
- REST API at api.{region}.commercetools.com
- GraphQL API at api.{region}.commercetools.com/{project}/graphql
- 'REST API: 200 req/sec/project default'
- 'Search (Product Projection): 100 req/sec'
- 'Concurrent connections: 200/project'
- Cart, Order, Customer, Catalog, Discount, Inventory APIs
- OAuth 2.0 with scoped tokens
- Subscription messages for async event delivery
- Webhooks via HTTP destinations
- 'Multi-region: AWS US/EU/Australia, GCP US/EU/Australia'
- Custom Objects for extensibility
- Composable Frontend (B2C2B Foundry)
finops:
- name: Commercetools Finops
  service_category: Composable Commerce
  slug: commercetools-finops
graphqls:
- description: The commercetools GraphQL API provides a flexible, network-efficient alternative to the HTTP API for querying and mutating Composable Commerce resources. It exposes a single endpoint and allows client
  name: commercetools GraphQL API
  slug: commercetools-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commercetools.png
json_schemas:
- name: Address
  property_count: 12
  slug: commercetools-address
- name: Attribute
  property_count: 2
  slug: commercetools-attribute
- name: Cart
  property_count: 16
  slug: commercetools-cart
- name: CartDraft
  property_count: 10
  slug: commercetools-cartdraft
- name: CartPagedQueryResponse
  property_count: 5
  slug: commercetools-cartpagedqueryresponse
- name: CartUpdate
  property_count: 2
  slug: commercetools-cartupdate
- name: Category
  property_count: 13
  slug: commercetools-category
- name: CategoryDraft
  property_count: 8
  slug: commercetools-categorydraft
- name: CategoryImport
  property_count: 6
  slug: commercetools-categoryimport
- name: CategoryImportRequest
  property_count: 2
  slug: commercetools-categoryimportrequest
- name: CategoryPagedQueryResponse
  property_count: 5
  slug: commercetools-categorypagedqueryresponse
- name: CategoryUpdate
  property_count: 2
  slug: commercetools-categoryupdate
- name: Change
  property_count: 4
  slug: commercetools-change
- name: Customer
  property_count: 12
  slug: commercetools-customer
- name: CustomerDraft
  property_count: 8
  slug: commercetools-customerdraft
- name: CustomerImport
  property_count: 7
  slug: commercetools-customerimport
- name: CustomerImportRequest
  property_count: 2
  slug: commercetools-customerimportrequest
- name: CustomerPagedQueryResponse
  property_count: 5
  slug: commercetools-customerpagedqueryresponse
- name: CustomerSignInResult
  property_count: 2
  slug: commercetools-customersigninresult
- name: CustomerUpdate
  property_count: 2
  slug: commercetools-customerupdate
- name: ErrorObject
  property_count: 2
  slug: commercetools-errorobject
- name: Image
  property_count: 3
  slug: commercetools-image
- name: ImportContainer
  property_count: 5
  slug: commercetools-importcontainer
- name: ImportContainerDraft
  property_count: 2
  slug: commercetools-importcontainerdraft
- name: ImportContainerPagedQueryResponse
  property_count: 5
  slug: commercetools-importcontainerpagedqueryresponse
- name: ImportOperation
  property_count: 9
  slug: commercetools-importoperation
- name: ImportOperationPagedQueryResponse
  property_count: 5
  slug: commercetools-importoperationpagedqueryresponse
- name: ImportOperationStatus
  property_count: 3
  slug: commercetools-importoperationstatus
- name: ImportResponse
  property_count: 1
  slug: commercetools-importresponse
- name: ImportSummary
  property_count: 2
  slug: commercetools-importsummary
- name: InventoryEntry
  property_count: 9
  slug: commercetools-inventoryentry
- name: InventoryEntryDraft
  property_count: 6
  slug: commercetools-inventoryentrydraft
- name: InventoryImport
  property_count: 5
  slug: commercetools-inventoryimport
- name: InventoryImportRequest
  property_count: 2
  slug: commercetools-inventoryimportrequest
- name: InventoryPagedQueryResponse
  property_count: 5
  slug: commercetools-inventorypagedqueryresponse
- name: LineItem
  property_count: 9
  slug: commercetools-lineitem
- name: LocalizedString
  property_count: 0
  slug: commercetools-localizedstring
- name: ModifiedBy
  property_count: 6
  slug: commercetools-modifiedby
- name: Money
  property_count: 3
  slug: commercetools-money
- name: commercetools Order
  property_count: 36
  slug: commercetools-order
- name: OrderFromCartDraft
  property_count: 5
  slug: commercetools-orderfromcartdraft
- name: OrderImport
  property_count: 8
  slug: commercetools-orderimport
- name: OrderImportRequest
  property_count: 2
  slug: commercetools-orderimportrequest
- name: OrderPagedQueryResponse
  property_count: 5
  slug: commercetools-orderpagedqueryresponse
- name: OrderUpdate
  property_count: 2
  slug: commercetools-orderupdate
- name: Payment
  property_count: 11
  slug: commercetools-payment
- name: PaymentDraft
  property_count: 6
  slug: commercetools-paymentdraft
- name: PaymentMethodInfo
  property_count: 3
  slug: commercetools-paymentmethodinfo
- name: PaymentPagedQueryResponse
  property_count: 5
  slug: commercetools-paymentpagedqueryresponse
- name: PaymentStatus
  property_count: 3
  slug: commercetools-paymentstatus
- name: PaymentUpdate
  property_count: 2
  slug: commercetools-paymentupdate
- name: Price
  property_count: 7
  slug: commercetools-price
- name: PriceDraft
  property_count: 6
  slug: commercetools-pricedraft
- name: commercetools Product
  property_count: 11
  slug: commercetools-product
- name: ProductCatalogData
  property_count: 4
  slug: commercetools-productcatalogdata
- name: ProductData
  property_count: 8
  slug: commercetools-productdata
- name: ProductDraft
  property_count: 10
  slug: commercetools-productdraft
- name: ProductImport
  property_count: 7
  slug: commercetools-productimport
- name: ProductImportRequest
  property_count: 2
  slug: commercetools-productimportrequest
- name: ProductPagedQueryResponse
  property_count: 5
  slug: commercetools-productpagedqueryresponse
- name: ProductUpdate
  property_count: 2
  slug: commercetools-productupdate
- name: ProductVariant
  property_count: 6
  slug: commercetools-productvariant
- name: ProductVariantDraft
  property_count: 5
  slug: commercetools-productvariantdraft
- name: ProductVariantImport
  property_count: 7
  slug: commercetools-productvariantimport
- name: ProductVariantImportRequest
  property_count: 2
  slug: commercetools-productvariantimportrequest
- name: Project
  property_count: 6
  slug: commercetools-project
- name: Record
  property_count: 10
  slug: commercetools-record
- name: RecordPagedQueryResponse
  property_count: 5
  slug: commercetools-recordpagedqueryresponse
- name: Reference
  property_count: 2
  slug: commercetools-reference
- name: StandalonePriceImport
  property_count: 8
  slug: commercetools-standalonepriceimport
- name: StandalonePriceImportRequest
  property_count: 2
  slug: commercetools-standalonepriceimportrequest
- name: commercetools Subscription Message
  property_count: 11
  slug: commercetools-subscription-message
- name: Subscription
  property_count: 10
  slug: commercetools-subscription
- name: SubscriptionDraft
  property_count: 5
  slug: commercetools-subscriptiondraft
- name: SubscriptionPagedQueryResponse
  property_count: 5
  slug: commercetools-subscriptionpagedqueryresponse
- name: SubscriptionUpdate
  property_count: 2
  slug: commercetools-subscriptionupdate
- name: Transaction
  property_count: 6
  slug: commercetools-transaction
json_structures:
- name: Commercetools Structure
  property_count: 0
  slug: commercetools-structure
jsonld:
- class_count: 0
  name: Commercetools Context
  property_count: 13
  slug: commercetools-context
layout: provider
modified: '2026-05-19'
name: commercetools
nav: Providers
network: true
overview: 'commercetools publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Carts API, Categories API, ChangeHistory API, and 11 more. Tagged areas include Commerce, Composable Commerce, E-Commerce, GraphQL, and REST.


  The commercetools catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  commercetools'' developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Commercetools Plans Pricing
  plan_count: 3
  slug: commercetools-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 4
  name: Commercetools Rate Limits
  slug: commercetools-rate-limits
rules:
- name: commercetools API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: commercetools-asyncapi-spectral-rules
- name: commercetools API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: commercetools-jsonschema-spectral-rules
- name: commercetools API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: commercetools-rules
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 77.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 28.9
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commercetools/refs/heads/main/screenshots/commercetools-2026-06-20T174814.png
security:
- kind: authentication
  name: Commercetools Authentication
  slug: commercetools-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Commercetools Domain Security
  slug: commercetools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Commercetools Trust Center
  slug: commercetools-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, CSA STAR
slug: commercetools
tags:
- Commerce
- Composable Commerce
- E-Commerce
- GraphQL
- REST
- SDK
website: https://commercetools.com/
---
