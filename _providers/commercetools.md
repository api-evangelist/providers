---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Commercetools Agentic Access
  operation_count: 54
  slug: commercetools-agentic-access
  summary_line: 54 operations · 31 acting
api_count: 3
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
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Manage shopping carts with line items, discounts, shipping, and tax calculations.
  name: commercetools Carts API
  slug: commercetools-carts-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Organize products into hierarchical category structures.
  name: commercetools Categories API
  slug: commercetools-categories-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Manage customer accounts, addresses, authentication, and group assignments.
  name: commercetools Customers API
  slug: commercetools-customers-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Manage import containers that hold import requests before processing.
  name: commercetools ImportContainers API
  slug: commercetools-importcontainers-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Monitor the status of individual import operations.
  name: commercetools ImportOperations API
  slug: commercetools-importoperations-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Manage inventory entries tracking stock levels per channel and SKU.
  name: commercetools Inventory API
  slug: commercetools-inventory-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Create and manage orders resulting from cart checkouts or quotes.
  name: commercetools Orders API
  slug: commercetools-orders-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Track payment transactions and PSP interactions associated with orders.
  name: commercetools Payments API
  slug: commercetools-payments-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Manage product catalog entries including variants, images, prices, and attributes.
  name: commercetools Products API
  slug: commercetools-products-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Read and configure project-level settings including currencies, languages, and messages.
  name: commercetools Project API
  slug: commercetools-project-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Import standalone price resources into the project.
  name: commercetools StandalonePrices API
  slug: commercetools-standaloneprices-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: The Subscriptions API from commercetools — 2 operation(s) for subscriptions.
  name: commercetools Subscriptions API
  slug: commercetools-subscriptions-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Query the audit log of resource changes across the project.
  name: commercetools Change History API
  slug: commercetools-change-history-api
- baseURL: https://api.{region}.commercetools.com
  baseurl_source: declared
  description: Import product variant resources into the project.
  name: commercetools Product Variants API
  slug: commercetools-product-variants-api
artifact_total: 184
asyncapis:
- description: The commercetools Subscriptions system delivers real-time change notifications and domain messages to external message queue destinations when resources are created, updated, or deleted within a Compo
  name: commercetools Subscriptions Events
  slug: commercetools-subscriptions-asyncapi
collections:
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/commercetools/overview
- group: agent
  href: https://artifacts.apis.io/commercetools/well-known/commercetools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/commercetools-well-known.yml
- group: design
  href: https://artifacts.apis.io/commercetools/rules/commercetools-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/commercetools-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/commercetools/rules/commercetools-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/commercetools-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/commercetools/vocabulary/commercetools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/commercetools-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/commercetools/data-model/commercetools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/commercetools-data-model.yml
- group: design
  href: https://artifacts.apis.io/commercetools/conventions/commercetools-conventions.yml
  title: ''
  type: Conventions
  url: conventions/commercetools-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.commercetools.com/
- group: auth
  href: https://artifacts.apis.io/commercetools/scopes/commercetools-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/commercetools-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.commercetools.com/api/deprecations-and-removals
- group: design
  href: https://artifacts.apis.io/commercetools/lifecycle/commercetools-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/commercetools-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/commercetools/errors/commercetools-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/commercetools-error-codes.yml
- group: design
  href: https://artifacts.apis.io/commercetools/errors/commercetools-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/commercetools-problem-types.yml
- group: design
  href: https://artifacts.apis.io/commercetools/conformance/commercetools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/commercetools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/commercetools/llms/commercetools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/commercetools-llms.txt
- group: agent
  href: https://artifacts.apis.io/commercetools/mcp/commercetools-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/commercetools-mcp.yml
- group: other
  href: https://artifacts.apis.io/commercetools/hosts/commercetools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commercetools-hosts.yml
- group: other
  href: https://artifacts.apis.io/commercetools/vendors/commercetools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/commercetools-vendors.yml
- group: build
  href: https://artifacts.apis.io/commercetools/packages/commercetools-packages.yml
  title: ''
  type: SDKs
  url: packages/commercetools-packages.yml
- group: build
  href: https://artifacts.apis.io/commercetools/packages/commercetools-packages.yml
  title: ''
  type: Packages
  url: packages/commercetools-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.commercetools.com/
- group: start
  title: ''
  type: SignUp
  url: https://commercetools.com/register-opportunity
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commercetools.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://commercetools.com/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.commercetools.com/api/releases/2026-10-02-reduced-category-tree-lock-contention
- group: commercial
  href: https://artifacts.apis.io/commercetools/plans/commercetools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/commercetools-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/commercetools/rate-limits/commercetools-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/commercetools-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/commercetools/finops/commercetools-finops.yml
  title: ''
  type: FinOps
  url: finops/commercetools-finops.yml
- group: other
  href: https://artifacts.apis.io/commercetools/capabilities/commercetools-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/commercetools-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/commercetools/agentic-access/commercetools-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/commercetools-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/commercetools/security/commercetools-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/commercetools-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/commercetools/security/commercetools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commercetools-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/commercetools/authentication/commercetools-authentication.yml
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
  href: https://artifacts.apis.io/commercetools/json-ld/commercetools-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/commercetools-context.jsonld
- group: docs
  href: https://artifacts.apis.io/commercetools/json-schema/commercetools-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/commercetools-order-schema.json
- group: docs
  href: https://artifacts.apis.io/commercetools/json-schema/commercetools-product-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/commercetools-product-schema.json
- group: docs
  href: https://artifacts.apis.io/commercetools/json-schema/commercetools-subscription-message-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/commercetools-subscription-message-schema.json
- group: design
  href: https://artifacts.apis.io/commercetools/rules/commercetools-rules.yml
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
- has_sources: true
  method: derived
  name: Commercetools Finops
  primary_unit: ''
  service_category: ''
  slug: commercetools-finops
  template: true
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
- name: CartDraft
  property_count: 10
  slug: commercetools-cart-draft
- name: CartPagedQueryResponse
  property_count: 5
  slug: commercetools-cart-paged-query-response
- name: Cart
  property_count: 16
  slug: commercetools-cart
- name: CartUpdate
  property_count: 2
  slug: commercetools-cart-update
- name: CartDraft
  property_count: 10
  slug: commercetools-cartdraft
- name: CartPagedQueryResponse
  property_count: 5
  slug: commercetools-cartpagedqueryresponse
- name: CartUpdate
  property_count: 2
  slug: commercetools-cartupdate
- name: CategoryDraft
  property_count: 8
  slug: commercetools-category-draft
- name: CategoryImportRequest
  property_count: 2
  slug: commercetools-category-import-request
- name: CategoryPagedQueryResponse
  property_count: 5
  slug: commercetools-category-paged-query-response
- name: Category
  property_count: 13
  slug: commercetools-category
- name: CategoryUpdate
  property_count: 2
  slug: commercetools-category-update
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
- name: CustomerDraft
  property_count: 8
  slug: commercetools-customer-draft
- name: CustomerImportRequest
  property_count: 2
  slug: commercetools-customer-import-request
- name: CustomerPagedQueryResponse
  property_count: 5
  slug: commercetools-customer-paged-query-response
- name: Customer
  property_count: 12
  slug: commercetools-customer
- name: CustomerUpdate
  property_count: 2
  slug: commercetools-customer-update
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
- name: ImportContainerDraft
  property_count: 2
  slug: commercetools-import-container-draft
- name: ImportContainerPagedQueryResponse
  property_count: 5
  slug: commercetools-import-container-paged-query-response
- name: ImportContainer
  property_count: 5
  slug: commercetools-import-container
- name: ImportOperationPagedQueryResponse
  property_count: 5
  slug: commercetools-import-operation-paged-query-response
- name: ImportOperation
  property_count: 9
  slug: commercetools-import-operation
- name: ImportResponse
  property_count: 1
  slug: commercetools-import-response
- name: ImportSummary
  property_count: 2
  slug: commercetools-import-summary
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
- name: InventoryEntryDraft
  property_count: 6
  slug: commercetools-inventory-entry-draft
- name: InventoryEntry
  property_count: 9
  slug: commercetools-inventory-entry
- name: InventoryImportRequest
  property_count: 2
  slug: commercetools-inventory-import-request
- name: InventoryPagedQueryResponse
  property_count: 5
  slug: commercetools-inventory-paged-query-response
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
- name: OrderFromCartDraft
  property_count: 5
  slug: commercetools-order-from-cart-draft
- name: OrderImportRequest
  property_count: 2
  slug: commercetools-order-import-request
- name: OrderPagedQueryResponse
  property_count: 5
  slug: commercetools-order-paged-query-response
- name: commercetools Order
  property_count: 36
  slug: commercetools-order
- name: OrderUpdate
  property_count: 2
  slug: commercetools-order-update
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
- name: PaymentDraft
  property_count: 6
  slug: commercetools-payment-draft
- name: PaymentPagedQueryResponse
  property_count: 5
  slug: commercetools-payment-paged-query-response
- name: Payment
  property_count: 11
  slug: commercetools-payment
- name: PaymentUpdate
  property_count: 2
  slug: commercetools-payment-update
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
- name: ProductDraft
  property_count: 10
  slug: commercetools-product-draft
- name: ProductImportRequest
  property_count: 2
  slug: commercetools-product-import-request
- name: ProductPagedQueryResponse
  property_count: 5
  slug: commercetools-product-paged-query-response
- name: commercetools Product
  property_count: 11
  slug: commercetools-product
- name: ProductUpdate
  property_count: 2
  slug: commercetools-product-update
- name: ProductVariantImportRequest
  property_count: 2
  slug: commercetools-product-variant-import-request
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
- name: RecordPagedQueryResponse
  property_count: 5
  slug: commercetools-record-paged-query-response
- name: Record
  property_count: 10
  slug: commercetools-record
- name: RecordPagedQueryResponse
  property_count: 5
  slug: commercetools-recordpagedqueryresponse
- name: Reference
  property_count: 2
  slug: commercetools-reference
- name: StandalonePriceImportRequest
  property_count: 2
  slug: commercetools-standalone-price-import-request
- name: StandalonePriceImport
  property_count: 8
  slug: commercetools-standalonepriceimport
- name: StandalonePriceImportRequest
  property_count: 2
  slug: commercetools-standalonepriceimportrequest
- name: SubscriptionDraft
  property_count: 5
  slug: commercetools-subscription-draft
- name: commercetools Subscription Message
  property_count: 11
  slug: commercetools-subscription-message
- name: SubscriptionPagedQueryResponse
  property_count: 5
  slug: commercetools-subscription-paged-query-response
- name: Subscription
  property_count: 10
  slug: commercetools-subscription
- name: SubscriptionUpdate
  property_count: 2
  slug: commercetools-subscription-update
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
mcp_servers:
- description: Remote MCP server at docs.commercetools.com; 127 tools listed.
  name: commercetools MCP (Knowledge MCP + Commerce MCP)
  slug: commercetools-mcp-knowledge-mcp-commerce-mcp
modified: '2026-05-19'
name: commercetools
nav: Providers
network: true
overview: 'commercetools publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Carts API, Categories API, Customers API, and 16 more. Tagged areas include Commerce, Composable Commerce, E-Commerce, GraphQL, and REST.


  The commercetools catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  commercetools'' developer surface includes support, signup flow, getting-started guide, changelog, authentication, documentation, pricing, and 38 more developer resources.'
plans:
- name: Commercetools Plans Pricing
  plan_count: 1
  slug: commercetools-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Commercetools Rate Limits
  slug: commercetools-rate-limits
rules:
- authorship: generated
  effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: commercetools — asyncapi rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: commercetools-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: commercetools — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: commercetools-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: commercetools API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: commercetools-rules
scopes:
- name: Commercetools Scopes
  scope_count: 87
  slug: commercetools-scopes
  summary_line: 87 scopes
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 35
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 71.5
    developer_ergonomics: 40.5
    discoverability: 80.0
    operational_transparency: 53.9
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/commercetools/commercetools-2026-06-20T174814.png
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
- Agentic Commerce
website: https://commercetools.com/
---
