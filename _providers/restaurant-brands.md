---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Restaurant Brands Agentic Access
  operation_count: 12
  slug: restaurant-brands-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 4
apis:
- description: The Loyalty API from Restaurant Brands International — 1 operation(s) for loyalty.
  name: Restaurant Brands International Loyalty API
  slug: restaurant-brands-loyalty-api
- description: The Menus API from Restaurant Brands International — 3 operation(s) for menus.
  name: Restaurant Brands International Menus API
  slug: restaurant-brands-menus-api
- description: The Orders API from Restaurant Brands International — 5 operation(s) for orders.
  name: Restaurant Brands International Orders API
  slug: restaurant-brands-orders-api
- description: The Stores API from Restaurant Brands International — 3 operation(s) for stores.
  name: Restaurant Brands International Stores API
  slug: restaurant-brands-stores-api
artifact_total: 298
collections:
- collection_type: open
  name: Burger King's Partners API
  slug: open-channel
- collection_type: open
  name: Burger King's Partners API v2
  slug: open-menu-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/restaurant-brands-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restaurant-brands-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/restaurant-brands-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rbictg.atlassian.net/wiki/spaces/RDP/overview
- group: design
  title: ''
  type: SpectralRules
  url: rules/restaurant-brands-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/restaurant-brands-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/restaurant-brands-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/restaurant-brands-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/restaurant-brands-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.rbi.com
- group: company
  title: ''
  type: About
  url: https://www.rbi.com/English/about-us/default.aspx
- group: company
  title: ''
  type: Investors
  url: https://www.rbi.com/English/investors/default.aspx
- group: company
  title: ''
  type: News
  url: https://www.rbi.com/English/news/default.aspx
- group: other
  title: ''
  type: Sustainability
  url: https://www.rbi.com/English/sustainability/default.aspx
- group: company
  title: ''
  type: Careers
  url: https://careers.rbi.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/restaurant-brands-international
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rbilabs
- group: other
  title: ''
  type: SEC Filings
  url: https://www.rbi.com/English/investors/sec-filings/default.aspx
- group: other
  title: ''
  type: Burger King
  url: https://www.bk.com
- group: other
  title: ''
  type: Tim Hortons
  url: https://www.timhortons.com
- group: other
  title: ''
  type: Popeyes
  url: https://www.popeyes.com
- group: other
  title: ''
  type: Firehouse Subs
  url: https://www.firehousesubs.com
- group: other
  title: ''
  type: Carrols Acquisition
  url: https://www.rbi.com/English/news/news-details/2024/Restaurant-Brands-International-Inc.-Completes-Acquisition-of-Carrols-Restaurant-Group/default.aspx
created: '2026-05-23'
description: 'Restaurant Brands International (RBI, NYSE: QSR) is one of the world''s largest quick service restaurant companies, with nearly $45 billion in annual system-wide sales and over 32,000 restaurants in more than 120 countries and territories. RBI operates four iconic brands — Tim Hortons, Burger King, Popeyes Louisiana Kitchen, and Firehouse Subs — and in May 2024 closed its $1B acquisition of Carrols Restaurant Group, Burger King''s largest U.S. franchisee. RBI Tech Group (rbictg.com) publishes a partner developer portal (the RBI Developer Portal on Confluence) documenting the Partners API — a set of partner-onboarding REST APIs for third-party food ordering marketplaces and POS/kiosk vendors integrating into RBI''s fulfillment platform. The documented surface includes ordering (price / commit / fire / place), menu and store retrieval, store-status and order/menu webhooks (Burger King''s Partners API v1 "Channel" and v2 "Menu"), loyalty identification and transaction validation,
  and payment capture / refund endpoints. Access is bilateral: partners request a Staging environment and are issued environment-, country-, and brand-scoped credentials (a bearer JWT for the Partners API; x-region / x-api-key / x-user-datetime headers for the Loyalty middleware). There is no public self-service signup, pricing, or rate card. The public GitHub presence (github.com/rbilabs) is limited to internal tooling forks and an archived hackathon repo.'
examples:
- key_count: 11
  name: Channel Address Example
  slug: channel-address-example
- key_count: 2
  name: Channel Allergen Example
  slug: channel-allergen-example
- key_count: 2
  name: Channel Available Example
  slug: channel-available-example
- key_count: 2
  name: Channel Balance Example
  slug: channel-balance-example
- key_count: 4
  name: Channel Calories Example
  slug: channel-calories-example
- key_count: 1
  name: Channel Cart Example
  slug: channel-cart-example
- key_count: 2
  name: Channel Cart Priced Example
  slug: channel-cart-priced-example
- key_count: 5
  name: Channel Charges Example
  slug: channel-charges-example
- key_count: 5
  name: Channel Commit Order Example
  slug: channel-commit-order-example
- key_count: 0
  name: Channel Config Offer Entry Example
  slug: channel-config-offer-entry-example
- key_count: 6
  name: Channel Customer Example
  slug: channel-customer-example
- key_count: 4
  name: Channel Day Part Example
  slug: channel-day-part-example
- key_count: 2
  name: Channel Discount Example
  slug: channel-discount-example
- key_count: 13
  name: Channel Entry Example
  slug: channel-entry-example
- key_count: 2
  name: Channel Entry Ref Example
  slug: channel-entry-ref-example
- key_count: 2
  name: Channel Fee Example
  slug: channel-fee-example
- key_count: 3
  name: Channel Feedback Example
  slug: channel-feedback-example
- key_count: 2
  name: Channel Geo Point Example
  slug: channel-geo-point-example
- key_count: 3
  name: Channel Identify Loyalty Example
  slug: channel-identify-loyalty-example
- key_count: 3
  name: Channel Identify Request Details Example
  slug: channel-identify-request-details-example
- key_count: 5
  name: Channel Identify Request Example
  slug: channel-identify-request-example
- key_count: 5
  name: Channel Identify Response Example
  slug: channel-identify-response-example
- key_count: 2
  name: Channel Image Example
  slug: channel-image-example
- key_count: 8
  name: Channel Location Example
  slug: channel-location-example
- key_count: 11
  name: Channel Loyalty Base Entry Example
  slug: channel-loyalty-base-entry-example
- key_count: 2
  name: Channel Loyalty Example
  slug: channel-loyalty-example
- key_count: 7
  name: Channel Menu Example
  slug: channel-menu-example
- key_count: 6
  name: Channel Menu Selection Example
  slug: channel-menu-selection-example
- key_count: 0
  name: Channel Menu Selection Priced Example
  slug: channel-menu-selection-priced-example
- key_count: 2
  name: Channel Mftaxes Example
  slug: channel-mftaxes-example
- key_count: 2
  name: Channel Money Example
  slug: channel-money-example
- key_count: 3
  name: Channel Nutrient Example
  slug: channel-nutrient-example
- key_count: 3
  name: Channel Nutrition Example
  slug: channel-nutrition-example
- key_count: 5
  name: Channel Order Error Example
  slug: channel-order-error-example
- key_count: 19
  name: Channel Order Example
  slug: channel-order-example
- key_count: 3
  name: Channel Order Placed Example
  slug: channel-order-placed-example
- key_count: 1
  name: Channel Payment Example
  slug: channel-payment-example
- key_count: 11
  name: Channel Place Order Example
  slug: channel-place-order-example
- key_count: 2
  name: Channel Posorder Error Example
  slug: channel-posorder-error-example
- key_count: 9
  name: Channel Price Order Example
  slug: channel-price-order-example
- key_count: 3
  name: Channel Price Range Example
  slug: channel-price-range-example
- key_count: 3
  name: Channel Quantity Constraints Example
  slug: channel-quantity-constraints-example
- key_count: 0
  name: Channel Reward Entry Example
  slug: channel-reward-entry-example
- key_count: 3
  name: Channel Service Hour Example
  slug: channel-service-hour-example
- key_count: 8
  name: Channel Store Example
  slug: channel-store-example
- key_count: 4
  name: Channel Store Status Changed Example
  slug: channel-store-status-changed-example
- key_count: 0
  name: Channel System Wide Offer Entry Example
  slug: channel-system-wide-offer-entry-example
- key_count: 4
  name: Channel Time Slot Example
  slug: channel-time-slot-example
- key_count: 1
  name: Channel Weekday Hours Example
  slug: channel-weekday-hours-example
- key_count: 14
  name: Menu V2 Allergen Example
  slug: menu-v2-allergen-example
- key_count: 2
  name: Menu V2 Availability Example
  slug: menu-v2-availability-example
- key_count: 3
  name: Menu V2 Calories Example
  slug: menu-v2-calories-example
- key_count: 0
  name: Menu V2 Config Offer Entry Example
  slug: menu-v2-config-offer-entry-example
- key_count: 2
  name: Menu V2 Day Part Example
  slug: menu-v2-day-part-example
- key_count: 14
  name: Menu V2 Day Part Schedule Example
  slug: menu-v2-day-part-schedule-example
- key_count: 4
  name: Menu V2 Entry Options Example
  slug: menu-v2-entry-options-example
- key_count: 2
  name: Menu V2 Entry Price Example
  slug: menu-v2-entry-price-example
- key_count: 2
  name: Menu V2 Image Example
  slug: menu-v2-image-example
- key_count: 2
  name: Menu V2 Localized String Example
  slug: menu-v2-localized-string-example
- key_count: 13
  name: Menu V2 Loyalty Entry Example
  slug: menu-v2-loyalty-entry-example
- key_count: 13
  name: Menu V2 Menu Entry Example
  slug: menu-v2-menu-entry-example
- key_count: 8
  name: Menu V2 Menu Example
  slug: menu-v2-menu-example
- key_count: 2
  name: Menu V2 Meta Example
  slug: menu-v2-meta-example
- key_count: 12
  name: Menu V2 Nutrient Example
  slug: menu-v2-nutrient-example
- key_count: 3
  name: Menu V2 Nutrition Example
  slug: menu-v2-nutrition-example
- key_count: 3
  name: Menu V2 Option Example
  slug: menu-v2-option-example
- key_count: 0
  name: Menu V2 Paper Coupon Entry Example
  slug: menu-v2-paper-coupon-entry-example
- key_count: 3
  name: Menu V2 Quantity Example
  slug: menu-v2-quantity-example
- key_count: 0
  name: Menu V2 Reward Entry Example
  slug: menu-v2-reward-entry-example
- key_count: 0
  name: Menu V2 System Wide Offer Entry Example
  slug: menu-v2-system-wide-offer-entry-example
finops:
- name: Restaurant Brands Finops
  service_category: Quick Service Restaurant Platform
  slug: restaurant-brands-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restaurant-brands.png
json_schemas:
- name: Address
  property_count: 11
  slug: channel-address
- name: Allergen
  property_count: 2
  slug: channel-allergen
- name: Available
  property_count: 2
  slug: channel-available
- name: Balance
  property_count: 2
  slug: channel-balance
- name: Brand
  property_count: 0
  slug: channel-brand
- name: Calories
  property_count: 4
  slug: channel-calories
- name: CartPriced
  property_count: 2
  slug: channel-cart-priced
- name: Cart
  property_count: 1
  slug: channel-cart
- name: Charges
  property_count: 5
  slug: channel-charges
- name: CommitOrder
  property_count: 5
  slug: channel-commit-order
- name: ConfigOfferEntry
  property_count: 0
  slug: channel-config-offer-entry
- name: Currency
  property_count: 0
  slug: channel-currency
- name: cursor
  property_count: 0
  slug: channel-cursor
- name: Customer
  property_count: 6
  slug: channel-customer
- name: DateTime
  property_count: 0
  slug: channel-date-time
- name: DayPartId
  property_count: 0
  slug: channel-day-part-id
- name: DayPart
  property_count: 4
  slug: channel-day-part
- name: Discount
  property_count: 2
  slug: channel-discount
- name: Discounts
  property_count: 0
  slug: channel-discounts
- name: EntryId
  property_count: 0
  slug: channel-entry-id
- name: EntryRef
  property_count: 2
  slug: channel-entry-ref
- name: Entry
  property_count: 13
  slug: channel-entry
- name: ExternalReferenceId
  property_count: 0
  slug: channel-external-reference-id
- name: Fee
  property_count: 2
  slug: channel-fee
- name: Feedback
  property_count: 3
  slug: channel-feedback
- name: Feedbacks
  property_count: 0
  slug: channel-feedbacks
- name: Fees
  property_count: 0
  slug: channel-fees
- name: FireOrderInSeconds
  property_count: 0
  slug: channel-fire-order-in-seconds
- name: GeoPoint
  property_count: 2
  slug: channel-geo-point
- name: Identifier
  property_count: 0
  slug: channel-identifier
- name: IdentifierType
  property_count: 0
  slug: channel-identifier-type
- name: IdentifyLoyalty
  property_count: 3
  slug: channel-identify-loyalty
- name: IdentifyRequestDetails
  property_count: 3
  slug: channel-identify-request-details
- name: IdentifyRequest
  property_count: 5
  slug: channel-identify-request
- name: IdentifyResponse
  property_count: 5
  slug: channel-identify-response
- name: Image
  property_count: 2
  slug: channel-image
- name: limit
  property_count: 0
  slug: channel-limit
- name: Locale
  property_count: 0
  slug: channel-locale
- name: LocalizedText
  property_count: 0
  slug: channel-localized-text
- name: Location
  property_count: 8
  slug: channel-location
- name: LoyaltyBaseEntry
  property_count: 11
  slug: channel-loyalty-base-entry
- name: LoyaltyId
  property_count: 0
  slug: channel-loyalty-id
- name: Loyalty
  property_count: 2
  slug: channel-loyalty
- name: LoyaltyTransactionId
  property_count: 0
  slug: channel-loyalty-transaction-id
- name: Menu
  property_count: 7
  slug: channel-menu
- name: MenuSelectionPriced
  property_count: 0
  slug: channel-menu-selection-priced
- name: MenuSelection
  property_count: 6
  slug: channel-menu-selection
- name: MFTaxes
  property_count: 2
  slug: channel-mftaxes
- name: Money
  property_count: 2
  slug: channel-money
- name: MpfOrderId
  property_count: 0
  slug: channel-mpf-order-id
- name: Nutrient
  property_count: 3
  slug: channel-nutrient
- name: Nutrition
  property_count: 3
  slug: channel-nutrition
- name: Operator
  property_count: 0
  slug: channel-operator
- name: OrderError
  property_count: 5
  slug: channel-order-error
- name: OrderId
  property_count: 0
  slug: channel-order-id
- name: OrderPlaced
  property_count: 3
  slug: channel-order-placed
- name: Order
  property_count: 19
  slug: channel-order
- name: OrderStatus
  property_count: 0
  slug: channel-order-status
- name: PaymentMethod
  property_count: 0
  slug: channel-payment-method
- name: Payment
  property_count: 1
  slug: channel-payment
- name: Phone
  property_count: 0
  slug: channel-phone
- name: PlaceOrder
  property_count: 11
  slug: channel-place-order
- name: PosVendor
  property_count: 0
  slug: channel-pos-vendor
- name: POSOrderError
  property_count: 2
  slug: channel-posorder-error
- name: PriceOrder
  property_count: 9
  slug: channel-price-order
- name: PriceRange
  property_count: 3
  slug: channel-price-range
- name: QuantityConstraints
  property_count: 3
  slug: channel-quantity-constraints
- name: ReadyInSeconds
  property_count: 0
  slug: channel-ready-in-seconds
- name: Reason
  property_count: 0
  slug: channel-reason
- name: Region
  property_count: 0
  slug: channel-region
- name: RewardEntry
  property_count: 0
  slug: channel-reward-entry
- name: ServiceHour
  property_count: 3
  slug: channel-service-hour
- name: ServiceMode
  property_count: 0
  slug: channel-service-mode
- name: StoreId
  property_count: 0
  slug: channel-store-id
- name: Store
  property_count: 8
  slug: channel-store
- name: StoreStatusChanged
  property_count: 4
  slug: channel-store-status-changed
- name: StoreStatus
  property_count: 0
  slug: channel-store-status
- name: SystemWideOfferEntry
  property_count: 0
  slug: channel-system-wide-offer-entry
- name: Terminal
  property_count: 0
  slug: channel-terminal
- name: TimeSlot
  property_count: 4
  slug: channel-time-slot
- name: Timezone
  property_count: 0
  slug: channel-timezone
- name: TransactionId
  property_count: 0
  slug: channel-transaction-id
- name: WeekdayHours
  property_count: 1
  slug: channel-weekday-hours
- name: Allergen
  property_count: 14
  slug: menu-v2-allergen
- name: Availability
  property_count: 2
  slug: menu-v2-availability
- name: Calories
  property_count: 3
  slug: menu-v2-calories
- name: ConfigOfferEntry
  property_count: 0
  slug: menu-v2-config-offer-entry
- name: DayPartSchedule
  property_count: 14
  slug: menu-v2-day-part-schedule
- name: DayPart
  property_count: 2
  slug: menu-v2-day-part
- name: EntryOptions
  property_count: 4
  slug: menu-v2-entry-options
- name: EntryPrice
  property_count: 2
  slug: menu-v2-entry-price
- name: Image
  property_count: 2
  slug: menu-v2-image
- name: LocalizedString
  property_count: 2
  slug: menu-v2-localized-string
- name: LoyaltyEntry
  property_count: 13
  slug: menu-v2-loyalty-entry
- name: MenuEntry
  property_count: 13
  slug: menu-v2-menu-entry
- name: Menu
  property_count: 8
  slug: menu-v2-menu
- name: Meta
  property_count: 2
  slug: menu-v2-meta
- name: Nutrient
  property_count: 12
  slug: menu-v2-nutrient
- name: Nutrition
  property_count: 3
  slug: menu-v2-nutrition
- name: Option
  property_count: 3
  slug: menu-v2-option
- name: PaperCouponEntry
  property_count: 0
  slug: menu-v2-paper-coupon-entry
- name: Quantity
  property_count: 3
  slug: menu-v2-quantity
- name: RewardEntry
  property_count: 0
  slug: menu-v2-reward-entry
- name: ServiceMode
  property_count: 0
  slug: menu-v2-service-mode
- name: StoreId
  property_count: 0
  slug: menu-v2-store-id
- name: SystemWideOfferEntry
  property_count: 0
  slug: menu-v2-system-wide-offer-entry
json_structures:
- name: Channel Address Structure
  property_count: 11
  slug: channel-address-structure
- name: Channel Allergen Structure
  property_count: 2
  slug: channel-allergen-structure
- name: Channel Available Structure
  property_count: 2
  slug: channel-available-structure
- name: Channel Balance Structure
  property_count: 2
  slug: channel-balance-structure
- name: Channel Brand Structure
  property_count: 0
  slug: channel-brand-structure
- name: Channel Calories Structure
  property_count: 4
  slug: channel-calories-structure
- name: Channel Cart Priced Structure
  property_count: 2
  slug: channel-cart-priced-structure
- name: Channel Cart Structure
  property_count: 1
  slug: channel-cart-structure
- name: Channel Charges Structure
  property_count: 5
  slug: channel-charges-structure
- name: Channel Commit Order Structure
  property_count: 5
  slug: channel-commit-order-structure
- name: Channel Config Offer Entry Structure
  property_count: 0
  slug: channel-config-offer-entry-structure
- name: Channel Currency Structure
  property_count: 0
  slug: channel-currency-structure
- name: Channel Cursor Structure
  property_count: 0
  slug: channel-cursor-structure
- name: Channel Customer Structure
  property_count: 6
  slug: channel-customer-structure
- name: Channel Date Time Structure
  property_count: 0
  slug: channel-date-time-structure
- name: Channel Day Part Id Structure
  property_count: 0
  slug: channel-day-part-id-structure
- name: Channel Day Part Structure
  property_count: 4
  slug: channel-day-part-structure
- name: Channel Discount Structure
  property_count: 2
  slug: channel-discount-structure
- name: Channel Discounts Structure
  property_count: 0
  slug: channel-discounts-structure
- name: Channel Entry Id Structure
  property_count: 0
  slug: channel-entry-id-structure
- name: Channel Entry Ref Structure
  property_count: 2
  slug: channel-entry-ref-structure
- name: Channel Entry Structure
  property_count: 13
  slug: channel-entry-structure
- name: Channel External Reference Id Structure
  property_count: 0
  slug: channel-external-reference-id-structure
- name: Channel Fee Structure
  property_count: 2
  slug: channel-fee-structure
- name: Channel Feedback Structure
  property_count: 3
  slug: channel-feedback-structure
- name: Channel Feedbacks Structure
  property_count: 0
  slug: channel-feedbacks-structure
- name: Channel Fees Structure
  property_count: 0
  slug: channel-fees-structure
- name: Channel Fire Order In Seconds Structure
  property_count: 0
  slug: channel-fire-order-in-seconds-structure
- name: Channel Geo Point Structure
  property_count: 2
  slug: channel-geo-point-structure
- name: Channel Identifier Structure
  property_count: 0
  slug: channel-identifier-structure
- name: Channel Identifier Type Structure
  property_count: 0
  slug: channel-identifier-type-structure
- name: Channel Identify Loyalty Structure
  property_count: 3
  slug: channel-identify-loyalty-structure
- name: Channel Identify Request Details Structure
  property_count: 3
  slug: channel-identify-request-details-structure
- name: Channel Identify Request Structure
  property_count: 5
  slug: channel-identify-request-structure
- name: Channel Identify Response Structure
  property_count: 5
  slug: channel-identify-response-structure
- name: Channel Image Structure
  property_count: 2
  slug: channel-image-structure
- name: Channel Limit Structure
  property_count: 0
  slug: channel-limit-structure
- name: Channel Locale Structure
  property_count: 0
  slug: channel-locale-structure
- name: Channel Localized Text Structure
  property_count: 0
  slug: channel-localized-text-structure
- name: Channel Location Structure
  property_count: 8
  slug: channel-location-structure
- name: Channel Loyalty Base Entry Structure
  property_count: 11
  slug: channel-loyalty-base-entry-structure
- name: Channel Loyalty Id Structure
  property_count: 0
  slug: channel-loyalty-id-structure
- name: Channel Loyalty Structure
  property_count: 2
  slug: channel-loyalty-structure
- name: Channel Loyalty Transaction Id Structure
  property_count: 0
  slug: channel-loyalty-transaction-id-structure
- name: Channel Menu Selection Priced Structure
  property_count: 0
  slug: channel-menu-selection-priced-structure
- name: Channel Menu Selection Structure
  property_count: 6
  slug: channel-menu-selection-structure
- name: Channel Menu Structure
  property_count: 7
  slug: channel-menu-structure
- name: Channel Mftaxes Structure
  property_count: 2
  slug: channel-mftaxes-structure
- name: Channel Money Structure
  property_count: 2
  slug: channel-money-structure
- name: Channel Mpf Order Id Structure
  property_count: 0
  slug: channel-mpf-order-id-structure
- name: Channel Nutrient Structure
  property_count: 3
  slug: channel-nutrient-structure
- name: Channel Nutrition Structure
  property_count: 3
  slug: channel-nutrition-structure
- name: Channel Operator Structure
  property_count: 0
  slug: channel-operator-structure
- name: Channel Order Error Structure
  property_count: 5
  slug: channel-order-error-structure
- name: Channel Order Id Structure
  property_count: 0
  slug: channel-order-id-structure
- name: Channel Order Placed Structure
  property_count: 3
  slug: channel-order-placed-structure
- name: Channel Order Status Structure
  property_count: 0
  slug: channel-order-status-structure
- name: Channel Order Structure
  property_count: 19
  slug: channel-order-structure
- name: Channel Payment Method Structure
  property_count: 0
  slug: channel-payment-method-structure
- name: Channel Payment Structure
  property_count: 1
  slug: channel-payment-structure
- name: Channel Phone Structure
  property_count: 0
  slug: channel-phone-structure
- name: Channel Place Order Structure
  property_count: 11
  slug: channel-place-order-structure
- name: Channel Pos Vendor Structure
  property_count: 0
  slug: channel-pos-vendor-structure
- name: Channel Posorder Error Structure
  property_count: 2
  slug: channel-posorder-error-structure
- name: Channel Price Order Structure
  property_count: 9
  slug: channel-price-order-structure
- name: Channel Price Range Structure
  property_count: 3
  slug: channel-price-range-structure
- name: Channel Quantity Constraints Structure
  property_count: 3
  slug: channel-quantity-constraints-structure
- name: Channel Ready In Seconds Structure
  property_count: 0
  slug: channel-ready-in-seconds-structure
- name: Channel Reason Structure
  property_count: 0
  slug: channel-reason-structure
- name: Channel Region Structure
  property_count: 0
  slug: channel-region-structure
- name: Channel Reward Entry Structure
  property_count: 0
  slug: channel-reward-entry-structure
- name: Channel Service Hour Structure
  property_count: 3
  slug: channel-service-hour-structure
- name: Channel Service Mode Structure
  property_count: 0
  slug: channel-service-mode-structure
- name: Channel Store Id Structure
  property_count: 0
  slug: channel-store-id-structure
- name: Channel Store Status Changed Structure
  property_count: 4
  slug: channel-store-status-changed-structure
- name: Channel Store Status Structure
  property_count: 0
  slug: channel-store-status-structure
- name: Channel Store Structure
  property_count: 8
  slug: channel-store-structure
- name: Channel System Wide Offer Entry Structure
  property_count: 0
  slug: channel-system-wide-offer-entry-structure
- name: Channel Terminal Structure
  property_count: 0
  slug: channel-terminal-structure
- name: Channel Time Slot Structure
  property_count: 4
  slug: channel-time-slot-structure
- name: Channel Timezone Structure
  property_count: 0
  slug: channel-timezone-structure
- name: Channel Transaction Id Structure
  property_count: 0
  slug: channel-transaction-id-structure
- name: Channel Weekday Hours Structure
  property_count: 1
  slug: channel-weekday-hours-structure
- name: Menu V2 Allergen Structure
  property_count: 14
  slug: menu-v2-allergen-structure
- name: Menu V2 Availability Structure
  property_count: 2
  slug: menu-v2-availability-structure
- name: Menu V2 Calories Structure
  property_count: 3
  slug: menu-v2-calories-structure
- name: Menu V2 Config Offer Entry Structure
  property_count: 0
  slug: menu-v2-config-offer-entry-structure
- name: Menu V2 Day Part Schedule Structure
  property_count: 14
  slug: menu-v2-day-part-schedule-structure
- name: Menu V2 Day Part Structure
  property_count: 2
  slug: menu-v2-day-part-structure
- name: Menu V2 Entry Options Structure
  property_count: 4
  slug: menu-v2-entry-options-structure
- name: Menu V2 Entry Price Structure
  property_count: 2
  slug: menu-v2-entry-price-structure
- name: Menu V2 Image Structure
  property_count: 2
  slug: menu-v2-image-structure
- name: Menu V2 Localized String Structure
  property_count: 2
  slug: menu-v2-localized-string-structure
- name: Menu V2 Loyalty Entry Structure
  property_count: 13
  slug: menu-v2-loyalty-entry-structure
- name: Menu V2 Menu Entry Structure
  property_count: 13
  slug: menu-v2-menu-entry-structure
- name: Menu V2 Menu Structure
  property_count: 8
  slug: menu-v2-menu-structure
- name: Menu V2 Meta Structure
  property_count: 2
  slug: menu-v2-meta-structure
- name: Menu V2 Nutrient Structure
  property_count: 12
  slug: menu-v2-nutrient-structure
- name: Menu V2 Nutrition Structure
  property_count: 3
  slug: menu-v2-nutrition-structure
- name: Menu V2 Option Structure
  property_count: 3
  slug: menu-v2-option-structure
- name: Menu V2 Paper Coupon Entry Structure
  property_count: 0
  slug: menu-v2-paper-coupon-entry-structure
- name: Menu V2 Quantity Structure
  property_count: 3
  slug: menu-v2-quantity-structure
- name: Menu V2 Reward Entry Structure
  property_count: 0
  slug: menu-v2-reward-entry-structure
- name: Menu V2 Service Mode Structure
  property_count: 0
  slug: menu-v2-service-mode-structure
- name: Menu V2 Store Id Structure
  property_count: 0
  slug: menu-v2-store-id-structure
- name: Menu V2 System Wide Offer Entry Structure
  property_count: 0
  slug: menu-v2-system-wide-offer-entry-structure
jsonld:
- class_count: 49
  name: Restaurant Brands Channel Context
  property_count: 127
  slug: restaurant-brands-channel-context
- class_count: 21
  name: Restaurant Brands Menu V2 Context
  property_count: 83
  slug: restaurant-brands-menu-v2-context
layout: provider
modified: '2026-06-03'
name: Restaurant Brands International
nav: Providers
network: true
overview: 'Restaurant Brands International publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Loyalty API, Menus API, Orders API, and 1 more. Tagged areas include Fortune 500, Franchising, Hospitality, NYSE QSR, and Quick Service Restaurants.


  The Restaurant Brands International catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Restaurant Brands International''s developer surface includes authentication, product news, GitHub presence, and 20 more developer resources.'
plans:
- name: Restaurant Brands Plans Pricing
  plan_count: 1
  slug: restaurant-brands-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Restaurant Brands Rate Limits
  slug: restaurant-brands-rate-limits
rules:
- name: Restaurant Brands International API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restaurant-brands-jsonschema-spectral-rules
- name: Restaurant Brands International API Rules
  rule_count: 33
  severity_counts:
    error: 6
    hint: 0
    info: 8
    warn: 19
  slug: restaurant-brands-spectral-rules
score:
  band: developing
  composite: 46.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 71.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Restaurant Brands Authentication
  slug: restaurant-brands-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Restaurant Brands Domain Security
  slug: restaurant-brands-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: restaurant-brands
tags:
- Fortune 500
- Franchising
- Hospitality
- NYSE QSR
- Quick Service Restaurants
- Restaurants
website: https://www.rbi.com
---
