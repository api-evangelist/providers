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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Doordash Agentic Access
  operation_count: 42
  slug: doordash-agentic-access
  summary_line: 42 operations · 30 acting
api_count: 5
apis:
- description: Get address auto-completion suggestions based on partial input.
  name: doordash Addresses API
  slug: doordash-addresses-api
- description: Manage business entities that represent legal entities or owners.
  name: doordash Businesses API
  slug: doordash-businesses-api
- description: Manage the item catalog including adding new items and updating existing item information such as names, descriptions, images, and attributes.
  name: doordash Catalog API
  slug: doordash-catalog-api
- description: Create, retrieve, update, cancel, and estimate deliveries using the classic API endpoints.
  name: doordash Deliveries API
  slug: doordash-deliveries-api
- description: Manage store-level inventory, pricing, and other in-store attributes for items on the DoorDash platform.
  name: doordash Inventory API
  slug: doordash-inventory-api
- description: Manage item availability and 86ing (marking items as unavailable) in real time.
  name: doordash Items API
  slug: doordash-items-api
- description: Create, update, and manage menus for stores on the DoorDash marketplace.
  name: doordash Menus API
  slug: doordash-menus-api
- description: Receive, confirm, update, and manage orders placed through the DoorDash marketplace.
  name: doordash Orders API
  slug: doordash-orders-api
- description: Manage item-level promotions at the store level, including adding and updating promotional pricing.
  name: doordash Promotions API
  slug: doordash-promotions-api
- description: Validate delivery serviceability and get pricing quotes before creating a delivery.
  name: doordash Quotes API
  slug: doordash-quotes-api
- description: Create report requests and retrieve report download links for financial, operations, menu, and feedback data.
  name: doordash Reports API
  slug: doordash-reports-api
- description: Manage store locations associated with businesses.
  name: doordash Stores API
  slug: doordash-stores-api
artifact_total: 234
asyncapis:
- description: 'DoorDash Drive sends webhook notifications for delivery status updates, enabling near-real-time information flow from DoorDash and Dashers to partner applications. Webhooks support scenarios like map '
  name: DoorDash Drive Delivery Webhooks
  slug: doordash-drive-webhooks-asyncapi
- description: DoorDash Marketplace sends webhook notifications for order events, menu processing status, delivery status updates, and store onboarding events. Each environment (Sandbox and Production) supports only
  name: DoorDash Marketplace Webhooks
  slug: doordash-marketplace-webhooks-asyncapi
- description: DoorDash Reporting API sends webhook notifications when report generation is complete and the report is ready for download. Partners configure a webhook endpoint to receive these notifications instead
  name: DoorDash Reporting Webhooks
  slug: doordash-reporting-webhooks-asyncapi
collections:
- collection_type: postman
  name: DoorDash Drive Classic Addresses API
  slug: postman-doordash-addresses-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Businesses API
  slug: postman-doordash-businesses-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Catalog API
  slug: postman-doordash-catalog-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Deliveries API
  slug: postman-doordash-deliveries-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Inventory API
  slug: postman-doordash-inventory-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Items API
  slug: postman-doordash-items-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Menus API
  slug: postman-doordash-menus-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Orders API
  slug: postman-doordash-orders-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Promotions API
  slug: postman-doordash-promotions-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Quotes API
  slug: postman-doordash-quotes-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Reports API
  slug: postman-doordash-reports-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Stores API
  slug: postman-doordash-stores-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DoorDash Drive Classic Addresses API
  slug: open-doordash-addresses-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Businesses API
  slug: open-doordash-businesses-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Catalog API
  slug: open-doordash-catalog-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Deliveries API
  slug: open-doordash-deliveries-api
- collection_type: open
  name: DoorDash Drive Classic API
  slug: open-doordash-drive-classic
- collection_type: open
  name: DoorDash Drive API
  slug: open-doordash-drive
- collection_type: open
  name: DoorDash Drive Classic Addresses Inventory API
  slug: open-doordash-inventory-api
- collection_type: open
  name: DoorDash Item Management API
  slug: open-doordash-item-management
- collection_type: open
  name: DoorDash Drive Classic Addresses Items API
  slug: open-doordash-items-api
- collection_type: open
  name: DoorDash Marketplace API
  slug: open-doordash-marketplace
- collection_type: open
  name: DoorDash Drive Classic Addresses Menus API
  slug: open-doordash-menus-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Orders API
  slug: open-doordash-orders-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Promotions API
  slug: open-doordash-promotions-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Quotes API
  slug: open-doordash-quotes-api
- collection_type: open
  name: DoorDash Reporting API
  slug: open-doordash-reporting
- collection_type: open
  name: DoorDash Drive Classic Addresses Reports API
  slug: open-doordash-reports-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Stores API
  slug: open-doordash-stores-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/doordash-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/doordash/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doordash-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/doordash-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doordash-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doordash-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.doordash.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.doordash.com/en-US/
- group: company
  title: ''
  type: Website
  url: https://www.doordash.com/
- group: company
  title: ''
  type: Blog
  url: https://doordash.engineering/
- group: start
  title: ''
  type: Login
  url: https://developer.doordash.com/en-US/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doordash.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doordash.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://help.doordash.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doordash
- group: build
  title: DoorDash Open Source
  type: GitHubOrganization
  url: https://github.com/doordash-oss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/doordash
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://www.npmjs.com/package/@doordash/sdk
- group: build
  title: OpenAPI Go Codegen (oapi-codegen-dd)
  type: Tools
  url: https://github.com/doordash-oss/oapi-codegen-dd
- group: design
  title: ''
  type: JSONLD
  url: json-ld/doordash-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/doordash-delivery-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/doordash-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/doordash-menu-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/doordash-report-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/doordash-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/doordash-spectral-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/doordash-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doordash-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doordash-finops.yml
description: DoorDash is an on-demand local commerce platform whose developer program exposes its logistics and marketplace network through public APIs. The Drive and Drive Classic APIs let businesses request on-demand deliveries fulfilled by DoorDash's Dasher fleet, while the Marketplace, Item Management, and Reporting APIs let merchants and retailers receive orders, synchronize menus and catalogs, and access financial and operational reporting. All APIs use JWT-based authentication and are documented at developer.doordash.com.
examples:
- key_count: 1
  name: Doordash Accept Quote Request Example
  slug: doordash-accept-quote-request-example
- key_count: 6
  name: Doordash Address Suggestion Example
  slug: doordash-address-suggestion-example
- key_count: 3
  name: Doordash Business Example
  slug: doordash-business-example
- key_count: 3
  name: Doordash Business Request Example
  slug: doordash-business-request-example
- key_count: 2
  name: Doordash Cancelled Item Example
  slug: doordash-cancelled-item-example
- key_count: 11
  name: Doordash Catalog Item Example
  slug: doordash-catalog-item-example
- key_count: 1
  name: Doordash Catalog Items Request Example
  slug: doordash-catalog-items-request-example
- key_count: 3
  name: Doordash Catalog Items Response Example
  slug: doordash-catalog-items-response-example
- key_count: 2
  name: Doordash Checkout Audit Signal Example
  slug: doordash-checkout-audit-signal-example
- key_count: 16
  name: Doordash Classic Delivery Example
  slug: doordash-classic-delivery-example
- key_count: 18
  name: Doordash Classic Delivery Request Example
  slug: doordash-classic-delivery-request-example
- key_count: 3
  name: Doordash Classic Delivery Update Request Example
  slug: doordash-classic-delivery-update-request-example
- key_count: 3
  name: Doordash Customer Example
  slug: doordash-customer-example
- key_count: 29
  name: Doordash Delivery Example
  slug: doordash-delivery-example
- key_count: 5
  name: Doordash Delivery Item Example
  slug: doordash-delivery-item-example
- key_count: 21
  name: Doordash Delivery Request Example
  slug: doordash-delivery-request-example
- key_count: 3
  name: Doordash Delivery Update Request Example
  slug: doordash-delivery-update-request-example
- key_count: 27
  name: Doordash Delivery Webhook Payload Example
  slug: doordash-delivery-webhook-payload-example
- key_count: 5
  name: Doordash Estimate Example
  slug: doordash-estimate-example
- key_count: 4
  name: Doordash Estimate Request Example
  slug: doordash-estimate-request-example
- key_count: 4
  name: Doordash Item Option Example
  slug: doordash-item-option-example
- key_count: 1
  name: Doordash Item Status Update Example
  slug: doordash-item-status-update-example
- key_count: 2
  name: Doordash Location Example
  slug: doordash-location-example
- key_count: 8
  name: Doordash Marketplace Delivery Webhook Payload Example
  slug: doordash-marketplace-delivery-webhook-payload-example
- key_count: 5
  name: Doordash Menu Category Example
  slug: doordash-menu-category-example
- key_count: 3
  name: Doordash Menu Details Example
  slug: doordash-menu-details-example
- key_count: 8
  name: Doordash Menu Item Example
  slug: doordash-menu-item-example
- key_count: 4
  name: Doordash Menu Option Example
  slug: doordash-menu-option-example
- key_count: 2
  name: Doordash Menu Request Example
  slug: doordash-menu-request-example
- key_count: 2
  name: Doordash Menu Response Example
  slug: doordash-menu-response-example
- key_count: 6
  name: Doordash Menu Webhook Payload Example
  slug: doordash-menu-webhook-payload-example
- key_count: 5
  name: Doordash Onboarding Webhook Payload Example
  slug: doordash-onboarding-webhook-payload-example
- key_count: 5
  name: Doordash Option Group Example
  slug: doordash-option-group-example
- key_count: 14
  name: Doordash Order Example
  slug: doordash-order-example
- key_count: 6
  name: Doordash Order Item Example
  slug: doordash-order-item-example
- key_count: 4
  name: Doordash Order Item Option Example
  slug: doordash-order-item-option-example
- key_count: 3
  name: Doordash Order Update Example
  slug: doordash-order-update-example
- key_count: 13
  name: Doordash Order Webhook Payload Example
  slug: doordash-order-webhook-payload-example
- key_count: 5
  name: Doordash Promotion Example
  slug: doordash-promotion-example
- key_count: 1
  name: Doordash Promotions Request Example
  slug: doordash-promotions-request-example
- key_count: 3
  name: Doordash Promotions Response Example
  slug: doordash-promotions-response-example
- key_count: 6
  name: Doordash Quote Example
  slug: doordash-quote-example
- key_count: 10
  name: Doordash Quote Request Example
  slug: doordash-quote-request-example
- key_count: 6
  name: Doordash Report Link Response Example
  slug: doordash-report-link-response-example
- key_count: 7
  name: Doordash Report Ready Payload Example
  slug: doordash-report-ready-payload-example
- key_count: 4
  name: Doordash Report Request Example
  slug: doordash-report-request-example
- key_count: 2
  name: Doordash Report Request Response Example
  slug: doordash-report-request-response-example
- key_count: 6
  name: Doordash Store Details Example
  slug: doordash-store-details-example
- key_count: 5
  name: Doordash Store Example
  slug: doordash-store-example
- key_count: 6
  name: Doordash Store Item Example
  slug: doordash-store-item-example
- key_count: 1
  name: Doordash Store Items Request Example
  slug: doordash-store-items-request-example
- key_count: 3
  name: Doordash Store Items Response Example
  slug: doordash-store-items-response-example
- key_count: 4
  name: Doordash Store Request Example
  slug: doordash-store-request-example
- key_count: 2
  name: Doordash Store Status Update Example
  slug: doordash-store-status-update-example
- key_count: 4
  name: Doordash Substitution Example
  slug: doordash-substitution-example
finops:
- name: Doordash Finops
  service_category: Last-Mile Delivery
  slug: doordash-finops
graphqls:
- description: 'This conceptual GraphQL schema models the DoorDash platform''s core domains: on-demand delivery logistics (Drive API), marketplace order management, menu and catalog operations, and reporting. DoorDash'
  name: DoorDash GraphQL Schema
  slug: doordash-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doordash.png
json_schemas:
- name: AcceptQuoteRequest
  property_count: 1
  slug: doordash-accept-quote-request
- name: AddressSuggestion
  property_count: 6
  slug: doordash-address-suggestion
- name: BusinessRequest
  property_count: 3
  slug: doordash-business-request
- name: Business
  property_count: 3
  slug: doordash-business
- name: CancelledItem
  property_count: 2
  slug: doordash-cancelled-item
- name: CatalogItem
  property_count: 11
  slug: doordash-catalog-item
- name: CatalogItemsRequest
  property_count: 1
  slug: doordash-catalog-items-request
- name: CatalogItemsResponse
  property_count: 3
  slug: doordash-catalog-items-response
- name: CheckoutAuditSignal
  property_count: 2
  slug: doordash-checkout-audit-signal
- name: ClassicDeliveryRequest
  property_count: 18
  slug: doordash-classic-delivery-request
- name: ClassicDelivery
  property_count: 16
  slug: doordash-classic-delivery
- name: ClassicDeliveryUpdateRequest
  property_count: 3
  slug: doordash-classic-delivery-update-request
- name: Customer
  property_count: 3
  slug: doordash-customer
- name: DeliveryItem
  property_count: 5
  slug: doordash-delivery-item
- name: DeliveryRequest
  property_count: 21
  slug: doordash-delivery-request
- name: Delivery
  property_count: 29
  slug: doordash-delivery
- name: DeliveryUpdateRequest
  property_count: 3
  slug: doordash-delivery-update-request
- name: DeliveryWebhookPayload
  property_count: 27
  slug: doordash-delivery-webhook-payload
- name: Error
  property_count: 3
  slug: doordash-error
- name: EstimateRequest
  property_count: 4
  slug: doordash-estimate-request
- name: Estimate
  property_count: 5
  slug: doordash-estimate
- name: ItemOption
  property_count: 4
  slug: doordash-item-option
- name: ItemStatusUpdate
  property_count: 1
  slug: doordash-item-status-update
- name: ItemError
  property_count: 3
  slug: doordash-itemerror
- name: Location
  property_count: 2
  slug: doordash-location
- name: MarketplaceDeliveryWebhookPayload
  property_count: 8
  slug: doordash-marketplace-delivery-webhook-payload
- name: MenuCategory
  property_count: 5
  slug: doordash-menu-category
- name: MenuDetails
  property_count: 3
  slug: doordash-menu-details
- name: MenuItem
  property_count: 8
  slug: doordash-menu-item
- name: MenuOption
  property_count: 4
  slug: doordash-menu-option
- name: MenuRequest
  property_count: 2
  slug: doordash-menu-request
- name: MenuResponse
  property_count: 2
  slug: doordash-menu-response
- name: DoorDash Menu
  property_count: 4
  slug: doordash-menu
- name: MenuWebhookPayload
  property_count: 6
  slug: doordash-menu-webhook-payload
- name: OnboardingWebhookPayload
  property_count: 5
  slug: doordash-onboarding-webhook-payload
- name: OptionGroup
  property_count: 5
  slug: doordash-option-group
- name: OrderItemOption
  property_count: 4
  slug: doordash-order-item-option
- name: OrderItem
  property_count: 6
  slug: doordash-order-item
- name: Order
  property_count: 14
  slug: doordash-order
- name: OrderUpdate
  property_count: 3
  slug: doordash-order-update
- name: OrderWebhookPayload
  property_count: 13
  slug: doordash-order-webhook-payload
- name: Promotion
  property_count: 5
  slug: doordash-promotion
- name: PromotionsRequest
  property_count: 1
  slug: doordash-promotions-request
- name: PromotionsResponse
  property_count: 3
  slug: doordash-promotions-response
- name: QuoteRequest
  property_count: 10
  slug: doordash-quote-request
- name: Quote
  property_count: 6
  slug: doordash-quote
- name: ReportLinkResponse
  property_count: 6
  slug: doordash-report-link-response
- name: ReportReadyPayload
  property_count: 7
  slug: doordash-report-ready-payload
- name: ReportRequestResponse
  property_count: 2
  slug: doordash-report-request-response
- name: ReportRequest
  property_count: 4
  slug: doordash-report-request
- name: DoorDash Report
  property_count: 9
  slug: doordash-report
- name: StoreDetails
  property_count: 6
  slug: doordash-store-details
- name: StoreItem
  property_count: 6
  slug: doordash-store-item
- name: StoreItemsRequest
  property_count: 1
  slug: doordash-store-items-request
- name: StoreItemsResponse
  property_count: 3
  slug: doordash-store-items-response
- name: StoreRequest
  property_count: 4
  slug: doordash-store-request
- name: Store
  property_count: 5
  slug: doordash-store
- name: StoreStatusUpdate
  property_count: 2
  slug: doordash-store-status-update
- name: Substitution
  property_count: 4
  slug: doordash-substitution
json_structures:
- name: Doordash Accept Quote Request Structure
  property_count: 1
  slug: doordash-accept-quote-request-structure
- name: Doordash Address Suggestion Structure
  property_count: 6
  slug: doordash-address-suggestion-structure
- name: Doordash Business Request Structure
  property_count: 3
  slug: doordash-business-request-structure
- name: Doordash Business Structure
  property_count: 3
  slug: doordash-business-structure
- name: Doordash Cancelled Item Structure
  property_count: 2
  slug: doordash-cancelled-item-structure
- name: Doordash Catalog Item Structure
  property_count: 11
  slug: doordash-catalog-item-structure
- name: Doordash Catalog Items Request Structure
  property_count: 1
  slug: doordash-catalog-items-request-structure
- name: Doordash Catalog Items Response Structure
  property_count: 3
  slug: doordash-catalog-items-response-structure
- name: Doordash Checkout Audit Signal Structure
  property_count: 2
  slug: doordash-checkout-audit-signal-structure
- name: Doordash Classic Delivery Request Structure
  property_count: 18
  slug: doordash-classic-delivery-request-structure
- name: Doordash Classic Delivery Structure
  property_count: 16
  slug: doordash-classic-delivery-structure
- name: Doordash Classic Delivery Update Request Structure
  property_count: 3
  slug: doordash-classic-delivery-update-request-structure
- name: Doordash Customer Structure
  property_count: 3
  slug: doordash-customer-structure
- name: Doordash Delivery Item Structure
  property_count: 5
  slug: doordash-delivery-item-structure
- name: Doordash Delivery Request Structure
  property_count: 21
  slug: doordash-delivery-request-structure
- name: Doordash Delivery Structure
  property_count: 29
  slug: doordash-delivery-structure
- name: Doordash Delivery Update Request Structure
  property_count: 3
  slug: doordash-delivery-update-request-structure
- name: Doordash Delivery Webhook Payload Structure
  property_count: 27
  slug: doordash-delivery-webhook-payload-structure
- name: Doordash Estimate Request Structure
  property_count: 4
  slug: doordash-estimate-request-structure
- name: Doordash Estimate Structure
  property_count: 5
  slug: doordash-estimate-structure
- name: Doordash Item Option Structure
  property_count: 4
  slug: doordash-item-option-structure
- name: Doordash Item Status Update Structure
  property_count: 1
  slug: doordash-item-status-update-structure
- name: Doordash Location Structure
  property_count: 2
  slug: doordash-location-structure
- name: Doordash Marketplace Delivery Webhook Payload Structure
  property_count: 8
  slug: doordash-marketplace-delivery-webhook-payload-structure
- name: Doordash Menu Category Structure
  property_count: 5
  slug: doordash-menu-category-structure
- name: Doordash Menu Details Structure
  property_count: 3
  slug: doordash-menu-details-structure
- name: Doordash Menu Item Structure
  property_count: 8
  slug: doordash-menu-item-structure
- name: Doordash Menu Option Structure
  property_count: 4
  slug: doordash-menu-option-structure
- name: Doordash Menu Request Structure
  property_count: 2
  slug: doordash-menu-request-structure
- name: Doordash Menu Response Structure
  property_count: 2
  slug: doordash-menu-response-structure
- name: Doordash Menu Webhook Payload Structure
  property_count: 6
  slug: doordash-menu-webhook-payload-structure
- name: Doordash Onboarding Webhook Payload Structure
  property_count: 5
  slug: doordash-onboarding-webhook-payload-structure
- name: Doordash Option Group Structure
  property_count: 5
  slug: doordash-option-group-structure
- name: Doordash Order Item Option Structure
  property_count: 4
  slug: doordash-order-item-option-structure
- name: Doordash Order Item Structure
  property_count: 6
  slug: doordash-order-item-structure
- name: Doordash Order Structure
  property_count: 14
  slug: doordash-order-structure
- name: Doordash Order Update Structure
  property_count: 3
  slug: doordash-order-update-structure
- name: Doordash Order Webhook Payload Structure
  property_count: 13
  slug: doordash-order-webhook-payload-structure
- name: Doordash Promotion Structure
  property_count: 5
  slug: doordash-promotion-structure
- name: Doordash Promotions Request Structure
  property_count: 1
  slug: doordash-promotions-request-structure
- name: Doordash Promotions Response Structure
  property_count: 3
  slug: doordash-promotions-response-structure
- name: Doordash Quote Request Structure
  property_count: 10
  slug: doordash-quote-request-structure
- name: Doordash Quote Structure
  property_count: 6
  slug: doordash-quote-structure
- name: Doordash Report Link Response Structure
  property_count: 6
  slug: doordash-report-link-response-structure
- name: Doordash Report Ready Payload Structure
  property_count: 7
  slug: doordash-report-ready-payload-structure
- name: Doordash Report Request Response Structure
  property_count: 2
  slug: doordash-report-request-response-structure
- name: Doordash Report Request Structure
  property_count: 4
  slug: doordash-report-request-structure
- name: Doordash Store Details Structure
  property_count: 6
  slug: doordash-store-details-structure
- name: Doordash Store Item Structure
  property_count: 6
  slug: doordash-store-item-structure
- name: Doordash Store Items Request Structure
  property_count: 1
  slug: doordash-store-items-request-structure
- name: Doordash Store Items Response Structure
  property_count: 3
  slug: doordash-store-items-response-structure
- name: Doordash Store Request Structure
  property_count: 4
  slug: doordash-store-request-structure
- name: Doordash Store Status Update Structure
  property_count: 2
  slug: doordash-store-status-update-structure
- name: Doordash Store Structure
  property_count: 5
  slug: doordash-store-structure
- name: Doordash Substitution Structure
  property_count: 4
  slug: doordash-substitution-structure
jsonld:
- class_count: 0
  name: Doordash Context
  property_count: 7
  slug: doordash-context
- class_count: 13
  name: Doordash Drive Classic Context
  property_count: 31
  slug: doordash-drive-classic-context
- class_count: 14
  name: Doordash Drive Context
  property_count: 47
  slug: doordash-drive-context
- class_count: 3
  name: Doordash Drive Webhooks Context
  property_count: 25
  slug: doordash-drive-webhooks-context
- class_count: 11
  name: Doordash Item Management Context
  property_count: 23
  slug: doordash-item-management-context
- class_count: 20
  name: Doordash Marketplace Context
  property_count: 38
  slug: doordash-marketplace-context
- class_count: 7
  name: Doordash Marketplace Webhooks Context
  property_count: 26
  slug: doordash-marketplace-webhooks-context
- class_count: 4
  name: Doordash Reporting Context
  property_count: 8
  slug: doordash-reporting-context
- class_count: 2
  name: Doordash Reporting Webhooks Context
  property_count: 6
  slug: doordash-reporting-webhooks-context
layout: provider
modified: '2026-06-02'
name: doordash
nav: Providers
network: true
overview: 'doordash publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Businesses API, Catalog API, and 9 more.


  The doordash catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 9 JSON-LD contexts, and 3 Spectral governance rulesets.


  doordash''s developer surface includes authentication, documentation, engineering blog, support, tooling, and 24 more developer resources.'
plans:
- name: Doordash Plans Pricing
  plan_count: 3
  slug: doordash-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Doordash Rate Limits
  slug: doordash-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: doordash API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: doordash-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: doordash API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: doordash-jsonschema-spectral-rules
- effective_rule_count: 83
  extends:
  - spectral:oas
  name: doordash API Rules
  rule_count: 42
  severity_counts:
    error: 7
    hint: 0
    info: 8
    warn: 27
  slug: doordash-spectral-rules
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 28.8
    contract_quality: 81.9
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doordash/refs/heads/main/screenshots/doordash-2026-06-20T180204.png
security:
- kind: authentication
  name: Doordash Authentication
  slug: doordash-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Doordash Domain Security
  slug: doordash-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Doordash Trust Center
  slug: doordash-trust-center
  summary_line: SOC 2, PCI DSS
slug: doordash
website: https://www.doordash.com/
---
