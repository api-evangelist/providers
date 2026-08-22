---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: Toast Agentic Access
  operation_count: 46
  slug: toast-agentic-access
  summary_line: 46 operations · 26 acting · 1 human-in-the-loop
api_count: 23
apis:
- description: The Toast Configuration API returns information about the configuration of a restaurant and its menus, such as menu items and alternate payment types, plus physical configuration including cash drawer
  name: Toast Configuration API
  slug: toast-configuration
- description: The Toast Analytics API provides an enterprise reporting and analytics service with operations that retrieve data for all or a subset of restaurants in a management group, create requests for reportin
  name: Toast Analytics API
  slug: toast-analytics
- description: The Toast Cash Management API provides information about cash operations that add cash to or remove cash from a restaurant cash drawer, separately from cash transaction payments.
  name: Toast Cash Management API
  slug: toast-cash-management
- description: The Toast Kitchen API returns information about kitchen operations for a restaurant, supporting kitchen display and fulfillment workflow integrations.
  name: Toast Kitchen API
  slug: toast-kitchen
- description: The Toast Credit Cards API is a simple, single-request, synchronous API to authorize credit card transactions associated with a Toast Orders API order.
  name: Toast Credit Cards API
  slug: toast-credit-cards
- description: The Toast Menus V3 API is the next-generation menu retrieval API, returning structured menu, item, modifier, and pricing data for a restaurant in an updated catalog-oriented model alongside the existi
  name: Toast Menus V3 API
  slug: toast-menus-v3
- description: The Toast Gift Cards integration specification is an outbound API. The partner hosts an HTTPS endpoint that accepts POST requests from the Toast platform to process gift card transactions (balance inq
  name: Toast Gift Cards Integration API
  slug: toast-gift-cards-integration
- description: 'The Toast Loyalty integration specification is an outbound API. The partner hosts an HTTPS endpoint that accepts POST requests from the Toast platform to handle loyalty program transactions (accrual, '
  name: Toast Loyalty Integration API
  slug: toast-loyalty-integration
- description: The Toast Tender integration specification is an outbound API. The partner hosts an HTTPS endpoint that accepts POST requests from the Toast platform to receive tender transaction data for alternate o
  name: Toast Tender Integration API
  slug: toast-tender-integration
- description: The Authentication API from Toast — 1 operation(s) for authentication.
  name: Toast Authentication API
  slug: toast-authentication-api
- description: The ConnectedRestaurants API from Toast — 1 operation(s) for connectedrestaurants.
  name: Toast ConnectedRestaurants API
  slug: toast-connectedrestaurants-api
- description: Related to price reduction applied to restaurant orders. For example, a restaurant might apply a discount for a promotion.
  name: Toast Discounts API
  slug: toast-discounts-api
- description: The Employees API from Toast — 6 operation(s) for employees.
  name: Toast Employees API
  slug: toast-employees-api
- description: The Groups API from Toast — 1 operation(s) for groups.
  name: Toast Groups API
  slug: toast-groups-api
- description: The Jobs API from Toast — 3 operation(s) for jobs.
  name: Toast Jobs API
  slug: toast-jobs-api
- description: The Menus API from Toast — 1 operation(s) for menus.
  name: Toast Menus API
  slug: toast-menus-api
- description: The Metadata API from Toast — 1 operation(s) for metadata.
  name: Toast Metadata API
  slug: toast-metadata-api
- description: Related to orders made by restaurant guests. For example, a restaurant guest orders items from a menu. Toast platform orders include one or more guest check.
  name: Toast Orders API
  slug: toast-orders-api
- description: Related to guests' payments for restaurant orders. Toast platform payments apply to a check in an order.
  name: Toast Payments API
  slug: toast-payments-api
- description: The Restaurants API from Toast — 2 operation(s) for restaurants.
  name: Toast Restaurants API
  slug: toast-restaurants-api
- description: The Shifts API from Toast — 2 operation(s) for shifts.
  name: Toast Shifts API
  slug: toast-shifts-api
- description: The Stock API from Toast — 3 operation(s) for stock.
  name: Toast Stock API
  slug: toast-stock-api
- description: The Time entries API from Toast — 2 operation(s) for time entries.
  name: Toast Time entries API
  slug: toast-time-entries-api
artifact_total: 388
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Toast Authentication API
  slug: open-toast-authentication-api
- collection_type: open
  name: Toast Authentication ConnectedRestaurants API
  slug: open-toast-connectedrestaurants-api
- collection_type: open
  name: Toast Authentication Discounts API
  slug: open-toast-discounts-api
- collection_type: open
  name: Toast Authentication Employees API
  slug: open-toast-employees-api
- collection_type: open
  name: Toast Authentication Groups API
  slug: open-toast-groups-api
- collection_type: open
  name: Toast Authentication Jobs API
  slug: open-toast-jobs-api
- collection_type: open
  name: Toast Authentication Menus API
  slug: open-toast-menus-api
- collection_type: open
  name: Toast Authentication Metadata API
  slug: open-toast-metadata-api
- collection_type: open
  name: Toast Authentication Orders API
  slug: open-toast-orders-api
- collection_type: open
  name: Toast Authentication Payments API
  slug: open-toast-payments-api
- collection_type: open
  name: Toast Authentication Restaurants API
  slug: open-toast-restaurants-api
- collection_type: open
  name: Toast Authentication Shifts API
  slug: open-toast-shifts-api
- collection_type: open
  name: Toast Authentication Stock API
  slug: open-toast-stock-api
- collection_type: open
  name: Toast Authentication Time entries API
  slug: open-toast-time-entries-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/toast-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/toast-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toast-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/toast-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toast-inc
- group: company
  title: ''
  type: Website
  url: https://pos.toasttab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.toasttab.com/doc/devguide/index.html
- group: start
  title: ''
  type: Portal
  url: https://doc.toasttab.com/openapi/
- group: start
  title: ''
  type: Signup
  url: https://developers.toasttab.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/toasttab
- group: design
  title: ''
  type: SpectralRules
  url: rules/toast-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/toast-vocabulary.yaml
created: '2025-02-08'
description: Toast is a restaurant technology platform providing cloud-based point-of-sale, payment processing, and business management tools for the restaurant industry. The Toast platform exposes REST APIs enabling technology partners to build integrations for orders, menus, labor management, restaurant configuration, inventory/stock management, authentication, and partner ecosystem access. APIs use OAuth 2.0 client credentials authentication with GUIDs for resource identification. Toast serves 120,000+ restaurant locations and offers both partner integrations (requiring formal partnership) and custom integrations via the developer portal.
examples:
- key_count: 3
  name: Authentication Authentication Request Example
  slug: authentication-authentication-request-example
- key_count: 1
  name: Authentication Authentication Response Example
  slug: authentication-authentication-response-example
- key_count: 6
  name: Authentication Authentication Token Example
  slug: authentication-authentication-token-example
- key_count: 15
  name: Labor Employee Example
  slug: labor-employee-example
- key_count: 1
  name: Labor External Reference Example
  slug: labor-external-reference-example
- key_count: 10
  name: Labor Job Example
  slug: labor-job-example
- key_count: 1
  name: Labor Job Wage Override Example
  slug: labor-job-wage-override-example
- key_count: 5
  name: Labor Schedule Config Example
  slug: labor-schedule-config-example
- key_count: 6
  name: Labor Shift Example
  slug: labor-shift-example
- key_count: 7
  name: Labor Time Entry Break Example
  slug: labor-time-entry-break-example
- key_count: 17
  name: Labor Time Entry Example
  slug: labor-time-entry-example
- key_count: 2
  name: Labor Toast Reference Example
  slug: labor-toast-reference-example
- key_count: 1
  name: Menus Alcohol Example
  slug: menus-alcohol-example
- key_count: 5
  name: Menus Allergen Item Example
  slug: menus-allergen-item-example
- key_count: 2
  name: Menus Availability Example
  slug: menus-availability-example
- key_count: 6
  name: Menus Catalog Product Example
  slug: menus-catalog-product-example
- key_count: 4
  name: Menus Catalog Product Option Example
  slug: menus-catalog-product-option-example
- key_count: 3
  name: Menus Catalog Product Option Value Example
  slug: menus-catalog-product-option-value-example
- key_count: 4
  name: Menus Catalog Product Variant Example
  slug: menus-catalog-product-variant-example
- key_count: 3
  name: Menus Catalog Product Variant Option Example
  slug: menus-catalog-product-variant-option-example
- key_count: 2
  name: Menus Item Tag Example
  slug: menus-item-tag-example
- key_count: 6
  name: Menus Menu Example
  slug: menus-menu-example
- key_count: 6
  name: Menus Menu Group Example
  slug: menus-menu-group-example
- key_count: 12
  name: Menus Menu Item Example
  slug: menus-menu-item-example
- key_count: 2
  name: Menus Metadata Example
  slug: menus-metadata-example
- key_count: 13
  name: Menus Modifier Group Example
  slug: menus-modifier-group-example
- key_count: 11
  name: Menus Modifier Option Example
  slug: menus-modifier-option-example
- key_count: 2
  name: Menus Modifier Option Tax Info Example
  slug: menus-modifier-option-tax-info-example
- key_count: 4
  name: Menus Portion Example
  slug: menus-portion-example
- key_count: 7
  name: Menus Pre Modifier Example
  slug: menus-pre-modifier-example
- key_count: 3
  name: Menus Pre Modifier Group Example
  slug: menus-pre-modifier-group-example
- key_count: 3
  name: Menus Pricing Rules Example
  slug: menus-pricing-rules-example
- key_count: 7
  name: Menus Restaurant Example
  slug: menus-restaurant-example
- key_count: 2
  name: Menus Sales Category Example
  slug: menus-sales-category-example
- key_count: 2
  name: Menus Schedule Example
  slug: menus-schedule-example
- key_count: 2
  name: Menus Sequence Price Example
  slug: menus-sequence-price-example
- key_count: 3
  name: Menus Size Sequence Pricing Rule Example
  slug: menus-size-sequence-pricing-rule-example
- key_count: 2
  name: Menus Time Range Example
  slug: menus-time-range-example
- key_count: 3
  name: Menus Time Specific Price Example
  slug: menus-time-specific-price-example
- key_count: 2
  name: Orders Applicable Discount Example
  slug: orders-applicable-discount-example
- key_count: 1
  name: Orders Applicable Discounts Request Example
  slug: orders-applicable-discounts-request-example
- key_count: 9
  name: Orders Applied Discount Example
  slug: orders-applied-discount-example
- key_count: 3
  name: Orders Applied Discount Reason Example
  slug: orders-applied-discount-reason-example
- key_count: 1
  name: Orders Applied Discount Trigger Example
  slug: orders-applied-discount-trigger-example
- key_count: 5
  name: Orders Applied Loyalty Info Example
  slug: orders-applied-loyalty-info-example
- key_count: 1
  name: Orders Applied Packaging Info Example
  slug: orders-applied-packaging-info-example
- key_count: 4
  name: Orders Applied Packaging Item Example
  slug: orders-applied-packaging-item-example
- key_count: 12
  name: Orders Applied Service Charge Example
  slug: orders-applied-service-charge-example
- key_count: 9
  name: Orders Applied Tax Rate Example
  slug: orders-applied-tax-rate-example
- key_count: 18
  name: Orders Check Example
  slug: orders-check-example
- key_count: 2
  name: Orders Config Reference Example
  slug: orders-config-reference-example
- key_count: 3
  name: Orders Curbside Pickup Info Example
  slug: orders-curbside-pickup-info-example
- key_count: 5
  name: Orders Customer Example
  slug: orders-customer-example
- key_count: 13
  name: Orders Delivery Info Example
  slug: orders-delivery-info-example
- key_count: 6
  name: Orders Delivery Service Info Example
  slug: orders-delivery-service-info-example
- key_count: 1
  name: Orders Device Example
  slug: orders-device-example
- key_count: 1
  name: Orders External Reference Example
  slug: orders-external-reference-example
- key_count: 2
  name: Orders Fulfillment Example
  slug: orders-fulfillment-example
- key_count: 2
  name: Orders Gift Card Info Example
  slug: orders-gift-card-info-example
- key_count: 2
  name: Orders Loyalty Details Example
  slug: orders-loyalty-details-example
- key_count: 2
  name: Orders Marketplace Facilitator Tax Info Example
  slug: orders-marketplace-facilitator-tax-info-example
- key_count: 14
  name: Orders Order Example
  slug: orders-order-example
- key_count: 1
  name: Orders Order Response Example
  slug: orders-order-response-example
- key_count: 13
  name: Orders Payment Example
  slug: orders-payment-example
- key_count: 2
  name: Orders Refund Details Example
  slug: orders-refund-details-example
- key_count: 4
  name: Orders Refund Example
  slug: orders-refund-example
- key_count: 13
  name: Orders Selection Example
  slug: orders-selection-example
- key_count: 2
  name: Orders Toast Reference Example
  slug: orders-toast-reference-example
- key_count: 1
  name: Orders Update Payment Request Example
  slug: orders-update-payment-request-example
- key_count: 2
  name: Orders Void Information Example
  slug: orders-void-information-example
- key_count: 10
  name: Partners Paginated Response Example
  slug: partners-paginated-response-example
- key_count: 12
  name: Partners Partner Access External Rep Example
  slug: partners-partner-access-external-rep-example
- key_count: 4
  name: Restaurants Day Schedule Example
  slug: restaurants-day-schedule-example
- key_count: 3
  name: Restaurants Delivery Example
  slug: restaurants-delivery-example
- key_count: 3
  name: Restaurants Delivery Payment Options Example
  slug: restaurants-delivery-payment-options-example
- key_count: 10
  name: Restaurants General Example
  slug: restaurants-general-example
- key_count: 2
  name: Restaurants Hours Example
  slug: restaurants-hours-example
- key_count: 4
  name: Restaurants Image Example
  slug: restaurants-image-example
- key_count: 11
  name: Restaurants Location Example
  slug: restaurants-location-example
- key_count: 4
  name: Restaurants Online Ordering Example
  slug: restaurants-online-ordering-example
- key_count: 1
  name: Restaurants Payment Options Example
  slug: restaurants-payment-options-example
- key_count: 8
  name: Restaurants Prep Times Example
  slug: restaurants-prep-times-example
- key_count: 1
  name: Restaurants Restaurant Example
  slug: restaurants-restaurant-example
- key_count: 1
  name: Restaurants Restaurant Info Example
  slug: restaurants-restaurant-info-example
- key_count: 1
  name: Restaurants Schedules Example
  slug: restaurants-schedules-example
- key_count: 2
  name: Restaurants Service Example
  slug: restaurants-service-example
- key_count: 4
  name: Restaurants Takeout Payment Options Example
  slug: restaurants-takeout-payment-options-example
- key_count: 6
  name: Restaurants Ur Ls Example
  slug: restaurants-ur-ls-example
- key_count: 7
  name: Restaurants Week Schedule Example
  slug: restaurants-week-schedule-example
- key_count: 3
  name: Stock Inventory Search Request Example
  slug: stock-inventory-search-request-example
- key_count: 6
  name: Stock Menu Item Inventory Example
  slug: stock-menu-item-inventory-example
features:
- description: Retrieve restaurant orders, checks, and payment data by GUID or bulk date queries.
  name: Orders API
- description: Full menu data retrieval including items, modifiers, prices, and availability.
  name: Menus API
- description: Employee CRUD operations, shift management, and payroll integration support.
  name: Labor Management API
- description: Location settings, payment options, and management group restaurant discovery.
  name: Restaurant Configuration API
- description: Inventory management for menu items and modifiers with stock level tracking.
  name: Stock and Inventory API
- description: Client credentials OAuth flow with GUID-scoped tokens for secure API access.
  name: OAuth 2.0 Authentication
- description: Formal partner program enabling multi-restaurant access and ecosystem integrations.
  name: Partner Integration Program
- description: Outbound integration webhooks for real-time event delivery (gift cards, loyalty, tender).
  name: Webhook Support
finops:
- name: Toast Finops
  service_category: Restaurant POS & Payments
  slug: toast-finops
graphqls:
- description: This conceptual GraphQL schema represents the Toast restaurant technology platform API surface. Toast provides cloud-based point-of-sale, payment processing, and business management tools for the rest
  name: Toast GraphQL Schema
  slug: toast-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toast.png
integrations:
- description: Third-party delivery platform integrated with Toast for order injection.
  name: DoorDash
- description: Delivery platform integration for menu sync and order management.
  name: UberEats
- description: Accounting integration for restaurant financial data via Toast reporting APIs.
  name: QuickBooks
- description: Payroll platform integration using Toast Labor API data.
  name: ADP
- description: Reservation system integration with Toast for guest management.
  name: OpenTable
json_schemas:
- name: AuthenticationRequest
  property_count: 3
  slug: authentication-authentication-request
- name: AuthenticationResponse
  property_count: 2
  slug: authentication-authentication-response
- name: AuthenticationToken
  property_count: 6
  slug: authentication-authentication-token
- name: Employee
  property_count: 0
  slug: labor-employee
- name: ExternalReference
  property_count: 0
  slug: labor-external-reference
- name: Job
  property_count: 0
  slug: labor-job
- name: JobWageOverride
  property_count: 2
  slug: labor-job-wage-override
- name: ScheduleConfig
  property_count: 5
  slug: labor-schedule-config
- name: Shift
  property_count: 0
  slug: labor-shift
- name: TimeEntryBreak
  property_count: 8
  slug: labor-time-entry-break
- name: TimeEntry
  property_count: 0
  slug: labor-time-entry
- name: ToastReference
  property_count: 2
  slug: labor-toast-reference
- name: Alcohol
  property_count: 1
  slug: menus-alcohol
- name: AllergenItem
  property_count: 5
  slug: menus-allergen-item
- name: Availability
  property_count: 2
  slug: menus-availability
- name: CatalogProductInfo
  property_count: 2
  slug: menus-catalog-product-info
- name: CatalogProductOption
  property_count: 4
  slug: menus-catalog-product-option
- name: CatalogProductOptionValue
  property_count: 3
  slug: menus-catalog-product-option-value
- name: CatalogProduct
  property_count: 6
  slug: menus-catalog-product
- name: CatalogProductVariantOption
  property_count: 4
  slug: menus-catalog-product-variant-option
- name: CatalogProductVariant
  property_count: 4
  slug: menus-catalog-product-variant
- name: ContentAdvisories
  property_count: 1
  slug: menus-content-advisories
- name: DimensionUnitOfMeasure
  property_count: 0
  slug: menus-dimension-unit-of-measure
- name: GuestCount
  property_count: 0
  slug: menus-guest-count
- name: Height
  property_count: 0
  slug: menus-height
- name: Image
  property_count: 0
  slug: menus-image
- name: Images
  property_count: 0
  slug: menus-images
- name: ItemTag
  property_count: 2
  slug: menus-item-tag
- name: Length
  property_count: 0
  slug: menus-length
- name: MasterId
  property_count: 0
  slug: menus-master-id
- name: MenuGroup
  property_count: 13
  slug: menus-menu-group
- name: MenuItem
  property_count: 42
  slug: menus-menu-item
- name: Menu
  property_count: 13
  slug: menus-menu
- name: Metadata
  property_count: 2
  slug: menus-metadata
- name: ModifierGroup
  property_count: 19
  slug: menus-modifier-group
- name: ModifierOption
  property_count: 40
  slug: menus-modifier-option
- name: ModifierOptionTaxInfo
  property_count: 2
  slug: menus-modifier-option-tax-info
- name: MultiLocationId
  property_count: 0
  slug: menus-multi-location-id
- name: Portion
  property_count: 4
  slug: menus-portion
- name: PosButtonColorDark
  property_count: 0
  slug: menus-pos-button-color-dark
- name: PosButtonColorLight
  property_count: 0
  slug: menus-pos-button-color-light
- name: PosName
  property_count: 0
  slug: menus-pos-name
- name: PreModifierGroup
  property_count: 4
  slug: menus-pre-modifier-group
- name: PreModifier
  property_count: 11
  slug: menus-pre-modifier
- name: PricingRules
  property_count: 3
  slug: menus-pricing-rules
- name: Restaurant
  property_count: 7
  slug: menus-restaurant
- name: SalesCategory
  property_count: 2
  slug: menus-sales-category
- name: Schedule
  property_count: 2
  slug: menus-schedule
- name: SequencePrice
  property_count: 2
  slug: menus-sequence-price
- name: SizeSequencePricingRule
  property_count: 3
  slug: menus-size-sequence-pricing-rule
- name: TimeRange
  property_count: 2
  slug: menus-time-range
- name: TimeSpecificPrice
  property_count: 3
  slug: menus-time-specific-price
- name: Visibility
  property_count: 0
  slug: menus-visibility
- name: Weight
  property_count: 0
  slug: menus-weight
- name: WeightUnitOfMeasure
  property_count: 0
  slug: menus-weight-unit-of-measure
- name: Width
  property_count: 0
  slug: menus-width
- name: ApplicableDiscount
  property_count: 3
  slug: orders-applicable-discount
- name: ApplicableDiscountsRequest
  property_count: 2
  slug: orders-applicable-discounts-request
- name: AppliedDiscountReason
  property_count: 4
  slug: orders-applied-discount-reason
- name: AppliedDiscount
  property_count: 0
  slug: orders-applied-discount
- name: AppliedDiscountTrigger
  property_count: 2
  slug: orders-applied-discount-trigger
- name: AppliedLoyaltyInfo
  property_count: 0
  slug: orders-applied-loyalty-info
- name: AppliedPackagingInfo
  property_count: 0
  slug: orders-applied-packaging-info
- name: AppliedPackagingItem
  property_count: 0
  slug: orders-applied-packaging-item
- name: AppliedServiceCharge
  property_count: 0
  slug: orders-applied-service-charge
- name: AppliedTaxRate
  property_count: 0
  slug: orders-applied-tax-rate
- name: Check
  property_count: 0
  slug: orders-check
- name: ConfigReference
  property_count: 0
  slug: orders-config-reference
- name: CurbsidePickupInfo
  property_count: 0
  slug: orders-curbside-pickup-info
- name: Customer
  property_count: 0
  slug: orders-customer
- name: DeliveryInfo
  property_count: 14
  slug: orders-delivery-info
- name: DeliveryServiceInfo
  property_count: 0
  slug: orders-delivery-service-info
- name: Device
  property_count: 1
  slug: orders-device
- name: ExternalReference
  property_count: 0
  slug: orders-external-reference
- name: Fulfillment
  property_count: 2
  slug: orders-fulfillment
- name: GiftCardInfo
  property_count: 0
  slug: orders-gift-card-info
- name: LoyaltyDetails
  property_count: 2
  slug: orders-loyalty-details
- name: MarketplaceFacilitatorTaxInfo
  property_count: 2
  slug: orders-marketplace-facilitator-tax-info
- name: OrderResponse
  property_count: 1
  slug: orders-order-response
- name: Order
  property_count: 0
  slug: orders-order
- name: Payment
  property_count: 0
  slug: orders-payment
- name: RefundDetails
  property_count: 3
  slug: orders-refund-details
- name: Refund
  property_count: 5
  slug: orders-refund
- name: RefundTransaction
  property_count: 0
  slug: orders-refund-transaction
- name: Selection
  property_count: 0
  slug: orders-selection
- name: ToastReference
  property_count: 2
  slug: orders-toast-reference
- name: UpdatePaymentRequest
  property_count: 1
  slug: orders-update-payment-request
- name: VoidInformation
  property_count: 5
  slug: orders-void-information
- name: PaginatedResponse
  property_count: 10
  slug: partners-paginated-response
- name: PartnerAccessExternalRep
  property_count: 12
  slug: partners-partner-access-external-rep
- name: DaySchedule
  property_count: 4
  slug: restaurants-day-schedule
- name: DeliveryPaymentOptions
  property_count: 3
  slug: restaurants-delivery-payment-options
- name: Delivery
  property_count: 3
  slug: restaurants-delivery
- name: General
  property_count: 10
  slug: restaurants-general
- name: Hours
  property_count: 2
  slug: restaurants-hours
- name: Image
  property_count: 4
  slug: restaurants-image
- name: Location
  property_count: 11
  slug: restaurants-location
- name: OnlineOrdering
  property_count: 5
  slug: restaurants-online-ordering
- name: PaymentOptions
  property_count: 3
  slug: restaurants-payment-options
- name: PrepTimes
  property_count: 8
  slug: restaurants-prep-times
- name: RestaurantInfo
  property_count: 8
  slug: restaurants-restaurant-info
- name: Restaurant
  property_count: 1
  slug: restaurants-restaurant
- name: Schedules
  property_count: 2
  slug: restaurants-schedules
- name: Service
  property_count: 3
  slug: restaurants-service
- name: TakeoutPaymentOptions
  property_count: 4
  slug: restaurants-takeout-payment-options
- name: URLs
  property_count: 6
  slug: restaurants-ur-ls
- name: WeekSchedule
  property_count: 7
  slug: restaurants-week-schedule
- name: InventorySearchRequest
  property_count: 3
  slug: stock-inventory-search-request
- name: MenuItemInventory
  property_count: 6
  slug: stock-menu-item-inventory
- name: ErrorMessage
  property_count: 9
  slug: toast-errormessage
- name: InventorySearchRequest
  property_count: 3
  slug: toast-inventorysearchrequest
- name: MenuItemInventory
  property_count: 6
  slug: toast-menuiteminventory
json_structures:
- name: Authentication Authentication Request Structure
  property_count: 3
  slug: authentication-authentication-request-structure
- name: Authentication Authentication Response Structure
  property_count: 2
  slug: authentication-authentication-response-structure
- name: Authentication Authentication Token Structure
  property_count: 6
  slug: authentication-authentication-token-structure
- name: Labor Employee Structure
  property_count: 0
  slug: labor-employee-structure
- name: Labor External Reference Structure
  property_count: 0
  slug: labor-external-reference-structure
- name: Labor Job Structure
  property_count: 0
  slug: labor-job-structure
- name: Labor Job Wage Override Structure
  property_count: 2
  slug: labor-job-wage-override-structure
- name: Labor Schedule Config Structure
  property_count: 5
  slug: labor-schedule-config-structure
- name: Labor Shift Structure
  property_count: 0
  slug: labor-shift-structure
- name: Labor Time Entry Break Structure
  property_count: 8
  slug: labor-time-entry-break-structure
- name: Labor Time Entry Structure
  property_count: 0
  slug: labor-time-entry-structure
- name: Labor Toast Reference Structure
  property_count: 2
  slug: labor-toast-reference-structure
- name: Menus Alcohol Structure
  property_count: 1
  slug: menus-alcohol-structure
- name: Menus Allergen Item Structure
  property_count: 5
  slug: menus-allergen-item-structure
- name: Menus Availability Structure
  property_count: 2
  slug: menus-availability-structure
- name: Menus Catalog Product Info Structure
  property_count: 2
  slug: menus-catalog-product-info-structure
- name: Menus Catalog Product Option Structure
  property_count: 4
  slug: menus-catalog-product-option-structure
- name: Menus Catalog Product Option Value Structure
  property_count: 3
  slug: menus-catalog-product-option-value-structure
- name: Menus Catalog Product Structure
  property_count: 6
  slug: menus-catalog-product-structure
- name: Menus Catalog Product Variant Option Structure
  property_count: 4
  slug: menus-catalog-product-variant-option-structure
- name: Menus Catalog Product Variant Structure
  property_count: 4
  slug: menus-catalog-product-variant-structure
- name: Menus Content Advisories Structure
  property_count: 1
  slug: menus-content-advisories-structure
- name: Menus Dimension Unit Of Measure Structure
  property_count: 0
  slug: menus-dimension-unit-of-measure-structure
- name: Menus Guest Count Structure
  property_count: 0
  slug: menus-guest-count-structure
- name: Menus Height Structure
  property_count: 0
  slug: menus-height-structure
- name: Menus Image Structure
  property_count: 0
  slug: menus-image-structure
- name: Menus Images Structure
  property_count: 0
  slug: menus-images-structure
- name: Menus Item Tag Structure
  property_count: 2
  slug: menus-item-tag-structure
- name: Menus Length Structure
  property_count: 0
  slug: menus-length-structure
- name: Menus Master Id Structure
  property_count: 0
  slug: menus-master-id-structure
- name: Menus Menu Group Structure
  property_count: 13
  slug: menus-menu-group-structure
- name: Menus Menu Item Structure
  property_count: 42
  slug: menus-menu-item-structure
- name: Menus Menu Structure
  property_count: 13
  slug: menus-menu-structure
- name: Menus Metadata Structure
  property_count: 2
  slug: menus-metadata-structure
- name: Menus Modifier Group Structure
  property_count: 19
  slug: menus-modifier-group-structure
- name: Menus Modifier Option Structure
  property_count: 40
  slug: menus-modifier-option-structure
- name: Menus Modifier Option Tax Info Structure
  property_count: 2
  slug: menus-modifier-option-tax-info-structure
- name: Menus Multi Location Id Structure
  property_count: 0
  slug: menus-multi-location-id-structure
- name: Menus Portion Structure
  property_count: 4
  slug: menus-portion-structure
- name: Menus Pos Button Color Dark Structure
  property_count: 0
  slug: menus-pos-button-color-dark-structure
- name: Menus Pos Button Color Light Structure
  property_count: 0
  slug: menus-pos-button-color-light-structure
- name: Menus Pos Name Structure
  property_count: 0
  slug: menus-pos-name-structure
- name: Menus Pre Modifier Group Structure
  property_count: 4
  slug: menus-pre-modifier-group-structure
- name: Menus Pre Modifier Structure
  property_count: 11
  slug: menus-pre-modifier-structure
- name: Menus Pricing Rules Structure
  property_count: 3
  slug: menus-pricing-rules-structure
- name: Menus Restaurant Structure
  property_count: 7
  slug: menus-restaurant-structure
- name: Menus Sales Category Structure
  property_count: 2
  slug: menus-sales-category-structure
- name: Menus Schedule Structure
  property_count: 2
  slug: menus-schedule-structure
- name: Menus Sequence Price Structure
  property_count: 2
  slug: menus-sequence-price-structure
- name: Menus Size Sequence Pricing Rule Structure
  property_count: 3
  slug: menus-size-sequence-pricing-rule-structure
- name: Menus Time Range Structure
  property_count: 2
  slug: menus-time-range-structure
- name: Menus Time Specific Price Structure
  property_count: 3
  slug: menus-time-specific-price-structure
- name: Menus Visibility Structure
  property_count: 0
  slug: menus-visibility-structure
- name: Menus Weight Structure
  property_count: 0
  slug: menus-weight-structure
- name: Menus Weight Unit Of Measure Structure
  property_count: 0
  slug: menus-weight-unit-of-measure-structure
- name: Menus Width Structure
  property_count: 0
  slug: menus-width-structure
- name: Orders Applicable Discount Structure
  property_count: 3
  slug: orders-applicable-discount-structure
- name: Orders Applicable Discounts Request Structure
  property_count: 2
  slug: orders-applicable-discounts-request-structure
- name: Orders Applied Discount Reason Structure
  property_count: 4
  slug: orders-applied-discount-reason-structure
- name: Orders Applied Discount Structure
  property_count: 0
  slug: orders-applied-discount-structure
- name: Orders Applied Discount Trigger Structure
  property_count: 2
  slug: orders-applied-discount-trigger-structure
- name: Orders Applied Loyalty Info Structure
  property_count: 0
  slug: orders-applied-loyalty-info-structure
- name: Orders Applied Packaging Info Structure
  property_count: 0
  slug: orders-applied-packaging-info-structure
- name: Orders Applied Packaging Item Structure
  property_count: 0
  slug: orders-applied-packaging-item-structure
- name: Orders Applied Service Charge Structure
  property_count: 0
  slug: orders-applied-service-charge-structure
- name: Orders Applied Tax Rate Structure
  property_count: 0
  slug: orders-applied-tax-rate-structure
- name: Orders Check Structure
  property_count: 0
  slug: orders-check-structure
- name: Orders Config Reference Structure
  property_count: 0
  slug: orders-config-reference-structure
- name: Orders Curbside Pickup Info Structure
  property_count: 0
  slug: orders-curbside-pickup-info-structure
- name: Orders Customer Structure
  property_count: 0
  slug: orders-customer-structure
- name: Orders Delivery Info Structure
  property_count: 14
  slug: orders-delivery-info-structure
- name: Orders Delivery Service Info Structure
  property_count: 0
  slug: orders-delivery-service-info-structure
- name: Orders Device Structure
  property_count: 1
  slug: orders-device-structure
- name: Orders External Reference Structure
  property_count: 0
  slug: orders-external-reference-structure
- name: Orders Fulfillment Structure
  property_count: 2
  slug: orders-fulfillment-structure
- name: Orders Gift Card Info Structure
  property_count: 0
  slug: orders-gift-card-info-structure
- name: Orders Loyalty Details Structure
  property_count: 2
  slug: orders-loyalty-details-structure
- name: Orders Marketplace Facilitator Tax Info Structure
  property_count: 2
  slug: orders-marketplace-facilitator-tax-info-structure
- name: Orders Order Response Structure
  property_count: 1
  slug: orders-order-response-structure
- name: Orders Order Structure
  property_count: 0
  slug: orders-order-structure
- name: Orders Payment Structure
  property_count: 0
  slug: orders-payment-structure
- name: Orders Refund Details Structure
  property_count: 3
  slug: orders-refund-details-structure
- name: Orders Refund Structure
  property_count: 5
  slug: orders-refund-structure
- name: Orders Refund Transaction Structure
  property_count: 0
  slug: orders-refund-transaction-structure
- name: Orders Selection Structure
  property_count: 0
  slug: orders-selection-structure
- name: Orders Toast Reference Structure
  property_count: 2
  slug: orders-toast-reference-structure
- name: Orders Update Payment Request Structure
  property_count: 1
  slug: orders-update-payment-request-structure
- name: Orders Void Information Structure
  property_count: 5
  slug: orders-void-information-structure
- name: Partners Paginated Response Structure
  property_count: 10
  slug: partners-paginated-response-structure
- name: Partners Partner Access External Rep Structure
  property_count: 12
  slug: partners-partner-access-external-rep-structure
- name: Restaurants Day Schedule Structure
  property_count: 4
  slug: restaurants-day-schedule-structure
- name: Restaurants Delivery Payment Options Structure
  property_count: 3
  slug: restaurants-delivery-payment-options-structure
- name: Restaurants Delivery Structure
  property_count: 3
  slug: restaurants-delivery-structure
- name: Restaurants General Structure
  property_count: 10
  slug: restaurants-general-structure
- name: Restaurants Hours Structure
  property_count: 2
  slug: restaurants-hours-structure
- name: Restaurants Image Structure
  property_count: 4
  slug: restaurants-image-structure
- name: Restaurants Location Structure
  property_count: 11
  slug: restaurants-location-structure
- name: Restaurants Online Ordering Structure
  property_count: 5
  slug: restaurants-online-ordering-structure
- name: Restaurants Payment Options Structure
  property_count: 3
  slug: restaurants-payment-options-structure
- name: Restaurants Prep Times Structure
  property_count: 8
  slug: restaurants-prep-times-structure
- name: Restaurants Restaurant Info Structure
  property_count: 8
  slug: restaurants-restaurant-info-structure
- name: Restaurants Restaurant Structure
  property_count: 1
  slug: restaurants-restaurant-structure
- name: Restaurants Schedules Structure
  property_count: 2
  slug: restaurants-schedules-structure
- name: Restaurants Service Structure
  property_count: 3
  slug: restaurants-service-structure
- name: Restaurants Takeout Payment Options Structure
  property_count: 4
  slug: restaurants-takeout-payment-options-structure
- name: Restaurants Ur Ls Structure
  property_count: 6
  slug: restaurants-ur-ls-structure
- name: Restaurants Week Schedule Structure
  property_count: 7
  slug: restaurants-week-schedule-structure
- name: Stock Inventory Search Request Structure
  property_count: 3
  slug: stock-inventory-search-request-structure
- name: Stock Menu Item Inventory Structure
  property_count: 6
  slug: stock-menu-item-inventory-structure
- name: Toast Structure
  property_count: 0
  slug: toast-structure
jsonld:
- class_count: 3
  name: Toast Authentication Context
  property_count: 11
  slug: toast-authentication-context
- class_count: 9
  name: Toast Labor Context
  property_count: 15
  slug: toast-labor-context
- class_count: 29
  name: Toast Menus Context
  property_count: 100
  slug: toast-menus-context
- class_count: 31
  name: Toast Orders Context
  property_count: 46
  slug: toast-orders-context
- class_count: 2
  name: Toast Partners Context
  property_count: 22
  slug: toast-partners-context
- class_count: 17
  name: Toast Restaurants Context
  property_count: 77
  slug: toast-restaurants-context
- class_count: 2
  name: Toast Stock Context
  property_count: 9
  slug: toast-stock-context
layout: provider
modified: '2026-06-03'
name: Toast
nav: Providers
network: true
overview: 'Toast publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, ConnectedRestaurants API, Discounts API, and 11 more. Tagged areas include Food Service, Point of Sale, Restaurants, and Hospitality.


  The Toast catalog on APIs.io includes 7 JSON-LD contexts and 2 Spectral governance rulesets.


  Toast''s developer surface includes authentication, documentation, developer portal, signup flow, and 9 more developer resources.'
plans:
- name: Toast Plans Pricing
  plan_count: 1
  slug: toast-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Toast Rate Limits
  slug: toast-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Toast API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: toast-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Toast API Rules
  rule_count: 36
  severity_counts:
    error: 9
    hint: 0
    info: 14
    warn: 13
  slug: toast-spectral-rules
scopes:
- name: Toast Scopes
  scope_count: 22
  slug: toast-scopes
  summary_line: 22 scopes · clientCredentials
score:
  band: thin
  composite: 37.6
  delta: -5.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 66.3
    developer_ergonomics: 31.0
    discoverability: 55.6
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/toast/refs/heads/main/screenshots/toast-2026-06-20T195427.png
security:
- kind: authentication
  name: Toast Authentication
  slug: toast-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Toast Domain Security
  slug: toast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Toast Vulnerability Disclosure
  slug: toast-vulnerability-disclosure
  summary_line: disclosure policy published
slug: toast
tags:
- Food Service
- Point of Sale
- Restaurants
- Hospitality
use_cases:
- description: Connect third-party online ordering platforms to Toast POS for order injection and menu sync.
  name: Online Ordering Integration
- description: Sync Toast employee and shift data with payroll systems using the Labor API.
  name: Payroll and Labor Integration
- description: Pull order and payment data via bulk orders API for custom reporting and business intelligence.
  name: Reporting and Analytics
- description: Integrate restaurant inventory systems with Toast Stock API for real-time stock tracking.
  name: Inventory Management
- description: Build loyalty program and gift card integrations using Toast outbound webhook APIs.
  name: Loyalty and Gift Cards
- description: Partner integrations managing hundreds of restaurant locations via Partners API.
  name: Multi-Location Management
website: https://pos.toasttab.com/
---
