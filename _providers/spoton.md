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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Spoton Agentic Access
  operation_count: 26
  slug: spoton-agentic-access
  summary_line: 26 operations · 2 acting
api_count: 15
apis:
- description: Available reservation times and wait-time lookups.
  name: SpotOn Availability API
  slug: spoton-availability-api
- description: Cash deposit records recorded at a location.
  name: SpotOn Cash Deposits API
  slug: spoton-cash-deposits-api
- description: Employee records and their job positions for a location.
  name: SpotOn Employees API
  slug: spoton-employees-api
- description: Job position definitions for a location.
  name: SpotOn Job Positions API
  slug: spoton-job-positions-api
- description: Location details for the SpotOn POS organization.
  name: SpotOn Locations API
  slug: spoton-locations-api
- description: Menu item catalog for a location.
  name: SpotOn Menu Items API
  slug: spoton-menu-items-api
- description: Order type definitions for a location, such as Dine In or Takeout.
  name: SpotOn Order Types API
  slug: spoton-order-types-api
- description: Order and check data export, including items, modifiers, payments, and taxes.
  name: SpotOn Orders API
  slug: spoton-orders-api
- description: Cash paid in and paid out records for a location.
  name: SpotOn Paid In Outs API
  slug: spoton-paid-in-outs-api
- description: Payment methods configured at a location.
  name: SpotOn Payment Options API
  slug: spoton-payment-options-api
- description: Hierarchical report categories used to group menu items.
  name: SpotOn Report Categories API
  slug: spoton-report-categories-api
- description: Create and manage guest reservations.
  name: SpotOn Reservations API
  slug: spoton-reservations-api
- description: Restaurants accessible with the API key.
  name: SpotOn Restaurants API
  slug: spoton-restaurants-api
- description: Employee shift clock-in and clock-out records.
  name: SpotOn Time Clock Entries API
  slug: spoton-time-clock-entries-api
- description: Add guests to a restaurant waitlist.
  name: SpotOn Waitlist API
  slug: spoton-waitlist-api
artifact_total: 150
collections:
- collection_type: postman
  name: SpotOn Reserve Availability API
  slug: postman-spoton-availability-api
- collection_type: postman
  name: SpotOn Reserve Availability Cash Deposits API
  slug: postman-spoton-cash-deposits-api
- collection_type: postman
  name: SpotOn Reserve Availability Employees API
  slug: postman-spoton-employees-api
- collection_type: postman
  name: SpotOn Reserve Availability Job Positions API
  slug: postman-spoton-job-positions-api
- collection_type: postman
  name: SpotOn Reserve Availability Locations API
  slug: postman-spoton-locations-api
- collection_type: postman
  name: SpotOn Reserve Availability Menu Items API
  slug: postman-spoton-menu-items-api
- collection_type: postman
  name: SpotOn Reserve Availability Order Types API
  slug: postman-spoton-order-types-api
- collection_type: postman
  name: SpotOn Reserve Availability Orders API
  slug: postman-spoton-orders-api
- collection_type: postman
  name: SpotOn Reserve Availability Paid In Outs API
  slug: postman-spoton-paid-in-outs-api
- collection_type: postman
  name: SpotOn Reserve Availability Payment Options API
  slug: postman-spoton-payment-options-api
- collection_type: postman
  name: SpotOn Reserve Availability Report Categories API
  slug: postman-spoton-report-categories-api
- collection_type: postman
  name: SpotOn Reserve Availability Reservations API
  slug: postman-spoton-reservations-api
- collection_type: postman
  name: SpotOn Reserve Availability Restaurants API
  slug: postman-spoton-restaurants-api
- collection_type: postman
  name: SpotOn Reserve Availability Time Clock Entries API
  slug: postman-spoton-time-clock-entries-api
- collection_type: postman
  name: SpotOn Reserve Availability Waitlist API
  slug: postman-spoton-waitlist-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spoton/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spoton-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spoton-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spoton-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spoton-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.spoton.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.spoton.com/restaurant/docs/introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.spoton.com/developer-center/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spoton.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpotOnInc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seatninja.com/
- group: operate
  title: ''
  type: Support
  url: https://help.spoton.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spoton
- group: other
  title: ''
  type: X
  url: https://twitter.com/spoton
- group: design
  title: ''
  type: SpectralRules
  url: rules/spoton-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spoton-vocabulary.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/spoton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spoton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spoton-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.spoton.com/blog/rss/
created: '2026-06-02'
description: SpotOn is an all-in-one restaurant point-of-sale and management platform that combines POS, online ordering, reservations, payments, labor, and reporting for restaurants and hospitality businesses. For developers and integration partners, SpotOn offers the Restaurant POS Export API, a location-centric REST API that delivers close-to-realtime data export from the SpotOn Restaurant POS System. It exposes resources such as orders, menu items, modifiers, employees, taxes, surcharges, payment options, labor reports, and time clock entries. Authentication uses an API key supplied via the x-api-key request header, with access granted on a per-location basis. SpotOn also publishes the Reserve API (powered by SeatNinja) for its reservations and waitlist product.
examples:
- key_count: 4
  name: Reserve Availability Response Example
  slug: reserve-availability-response-example
- key_count: 2
  name: Reserve Availability Slot Example
  slug: reserve-availability-slot-example
- key_count: 8
  name: Reserve Customer Information Example
  slug: reserve-customer-information-example
- key_count: 7
  name: Reserve Reservation Example
  slug: reserve-reservation-example
- key_count: 5
  name: Reserve Reservation Request Example
  slug: reserve-reservation-request-example
- key_count: 3
  name: Reserve Restaurant Example
  slug: reserve-restaurant-example
- key_count: 3
  name: Reserve Wait Time Response Example
  slug: reserve-wait-time-response-example
- key_count: 6
  name: Reserve Waitlist Entry Example
  slug: reserve-waitlist-entry-example
- key_count: 4
  name: Reserve Waitlist Request Example
  slug: reserve-waitlist-request-example
- key_count: 6
  name: Restaurant Pos Export Address Example
  slug: restaurant-pos-export-address-example
- key_count: 4
  name: Restaurant Pos Export Break Example
  slug: restaurant-pos-export-break-example
- key_count: 10
  name: Restaurant Pos Export Cash Deposit Example
  slug: restaurant-pos-export-cash-deposit-example
- key_count: 17
  name: Restaurant Pos Export Employee Example
  slug: restaurant-pos-export-employee-example
- key_count: 4
  name: Restaurant Pos Export Job Position Example
  slug: restaurant-pos-export-job-position-example
- key_count: 6
  name: Restaurant Pos Export Location Example
  slug: restaurant-pos-export-location-example
- key_count: 9
  name: Restaurant Pos Export Menu Item Catalog Example
  slug: restaurant-pos-export-menu-item-catalog-example
- key_count: 10
  name: Restaurant Pos Export Order Check Example
  slug: restaurant-pos-export-order-check-example
- key_count: 5
  name: Restaurant Pos Export Order Discount Example
  slug: restaurant-pos-export-order-discount-example
- key_count: 19
  name: Restaurant Pos Export Order Example
  slug: restaurant-pos-export-order-example
- key_count: 3
  name: Restaurant Pos Export Order Guest Example
  slug: restaurant-pos-export-order-guest-example
- key_count: 14
  name: Restaurant Pos Export Order Menu Item Example
  slug: restaurant-pos-export-order-menu-item-example
- key_count: 10
  name: Restaurant Pos Export Order Modifier Example
  slug: restaurant-pos-export-order-modifier-example
- key_count: 14
  name: Restaurant Pos Export Order Payment Example
  slug: restaurant-pos-export-order-payment-example
- key_count: 6
  name: Restaurant Pos Export Order Surcharge Example
  slug: restaurant-pos-export-order-surcharge-example
- key_count: 4
  name: Restaurant Pos Export Order Tax Example
  slug: restaurant-pos-export-order-tax-example
- key_count: 6
  name: Restaurant Pos Export Order Type Example
  slug: restaurant-pos-export-order-type-example
- key_count: 3
  name: Restaurant Pos Export Owner Info Example
  slug: restaurant-pos-export-owner-info-example
- key_count: 12
  name: Restaurant Pos Export Paid In Out Example
  slug: restaurant-pos-export-paid-in-out-example
- key_count: 6
  name: Restaurant Pos Export Payment Option Example
  slug: restaurant-pos-export-payment-option-example
- key_count: 5
  name: Restaurant Pos Export Report Category Example
  slug: restaurant-pos-export-report-category-example
- key_count: 13
  name: Restaurant Pos Export Time Clock Entry Example
  slug: restaurant-pos-export-time-clock-entry-example
features:
- description: All-in-one point-of-sale for counter-service and full-service restaurants.
  name: Restaurant POS
- description: Branded online ordering integrated with the POS.
  name: Online Ordering
- description: SpotOn Reserve manages reservations, waitlists, and guest communication.
  name: Reservations and Waitlist
- description: Integrated card processing with per-transaction take rates.
  name: Payments
- description: Employees, job positions, time clock entries, and labor reporting.
  name: Labor Management
- description: Sales, cash, and labor reporting with close-to-realtime data export.
  name: Reporting
- description: Location-centric REST API exporting orders, menu, payments, and labor data.
  name: Data Export API
finops:
- name: Spoton Finops
  service_category: Restaurant Technology + Payments
  slug: spoton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spoton.png
integrations:
- description: Feed exported sales, cash, and tip data into accounting and bookkeeping platforms.
  name: Accounting Systems
- description: Use time clock and labor data to integrate with payroll services.
  name: Payroll Providers
- description: Load POS export data into analytics warehouses and BI tools.
  name: Data Warehouses
- description: Embed SpotOn Reserve booking and waitlist via the JavaScript SDK.
  name: Reservation Front-Ends
json_schemas:
- name: AvailabilityResponse
  property_count: 4
  slug: reserve-availability-response
- name: AvailabilitySlot
  property_count: 2
  slug: reserve-availability-slot
- name: CustomerInformation
  property_count: 8
  slug: reserve-customer-information
- name: ReservationRequest
  property_count: 5
  slug: reserve-reservation-request
- name: Reservation
  property_count: 7
  slug: reserve-reservation
- name: Restaurant
  property_count: 3
  slug: reserve-restaurant
- name: WaitTimeResponse
  property_count: 3
  slug: reserve-wait-time-response
- name: WaitlistEntry
  property_count: 6
  slug: reserve-waitlist-entry
- name: WaitlistRequest
  property_count: 4
  slug: reserve-waitlist-request
- name: Address
  property_count: 6
  slug: restaurant-pos-export-address
- name: Break
  property_count: 4
  slug: restaurant-pos-export-break
- name: CashDeposit
  property_count: 10
  slug: restaurant-pos-export-cash-deposit
- name: Employee
  property_count: 17
  slug: restaurant-pos-export-employee
- name: JobPosition
  property_count: 4
  slug: restaurant-pos-export-job-position
- name: Location
  property_count: 6
  slug: restaurant-pos-export-location
- name: MenuItemCatalog
  property_count: 9
  slug: restaurant-pos-export-menu-item-catalog
- name: OrderCheck
  property_count: 10
  slug: restaurant-pos-export-order-check
- name: OrderDiscount
  property_count: 5
  slug: restaurant-pos-export-order-discount
- name: OrderGuest
  property_count: 3
  slug: restaurant-pos-export-order-guest
- name: OrderMenuItem
  property_count: 14
  slug: restaurant-pos-export-order-menu-item
- name: OrderModifier
  property_count: 10
  slug: restaurant-pos-export-order-modifier
- name: OrderPayment
  property_count: 14
  slug: restaurant-pos-export-order-payment
- name: Order
  property_count: 19
  slug: restaurant-pos-export-order
- name: OrderSurcharge
  property_count: 6
  slug: restaurant-pos-export-order-surcharge
- name: OrderTax
  property_count: 4
  slug: restaurant-pos-export-order-tax
- name: OrderType
  property_count: 6
  slug: restaurant-pos-export-order-type
- name: OwnerInfo
  property_count: 3
  slug: restaurant-pos-export-owner-info
- name: PaidInOut
  property_count: 12
  slug: restaurant-pos-export-paid-in-out
- name: PaymentOption
  property_count: 6
  slug: restaurant-pos-export-payment-option
- name: ReportCategory
  property_count: 5
  slug: restaurant-pos-export-report-category
- name: TimeClockEntry
  property_count: 13
  slug: restaurant-pos-export-time-clock-entry
json_structures:
- name: Reserve Availability Response Structure
  property_count: 4
  slug: reserve-availability-response-structure
- name: Reserve Availability Slot Structure
  property_count: 2
  slug: reserve-availability-slot-structure
- name: Reserve Customer Information Structure
  property_count: 8
  slug: reserve-customer-information-structure
- name: Reserve Reservation Request Structure
  property_count: 5
  slug: reserve-reservation-request-structure
- name: Reserve Reservation Structure
  property_count: 7
  slug: reserve-reservation-structure
- name: Reserve Restaurant Structure
  property_count: 3
  slug: reserve-restaurant-structure
- name: Reserve Wait Time Response Structure
  property_count: 3
  slug: reserve-wait-time-response-structure
- name: Reserve Waitlist Entry Structure
  property_count: 6
  slug: reserve-waitlist-entry-structure
- name: Reserve Waitlist Request Structure
  property_count: 4
  slug: reserve-waitlist-request-structure
- name: Restaurant Pos Export Address Structure
  property_count: 6
  slug: restaurant-pos-export-address-structure
- name: Restaurant Pos Export Break Structure
  property_count: 4
  slug: restaurant-pos-export-break-structure
- name: Restaurant Pos Export Cash Deposit Structure
  property_count: 10
  slug: restaurant-pos-export-cash-deposit-structure
- name: Restaurant Pos Export Employee Structure
  property_count: 17
  slug: restaurant-pos-export-employee-structure
- name: Restaurant Pos Export Job Position Structure
  property_count: 4
  slug: restaurant-pos-export-job-position-structure
- name: Restaurant Pos Export Location Structure
  property_count: 6
  slug: restaurant-pos-export-location-structure
- name: Restaurant Pos Export Menu Item Catalog Structure
  property_count: 9
  slug: restaurant-pos-export-menu-item-catalog-structure
- name: Restaurant Pos Export Order Check Structure
  property_count: 10
  slug: restaurant-pos-export-order-check-structure
- name: Restaurant Pos Export Order Discount Structure
  property_count: 5
  slug: restaurant-pos-export-order-discount-structure
- name: Restaurant Pos Export Order Guest Structure
  property_count: 3
  slug: restaurant-pos-export-order-guest-structure
- name: Restaurant Pos Export Order Menu Item Structure
  property_count: 14
  slug: restaurant-pos-export-order-menu-item-structure
- name: Restaurant Pos Export Order Modifier Structure
  property_count: 10
  slug: restaurant-pos-export-order-modifier-structure
- name: Restaurant Pos Export Order Payment Structure
  property_count: 14
  slug: restaurant-pos-export-order-payment-structure
- name: Restaurant Pos Export Order Structure
  property_count: 19
  slug: restaurant-pos-export-order-structure
- name: Restaurant Pos Export Order Surcharge Structure
  property_count: 6
  slug: restaurant-pos-export-order-surcharge-structure
- name: Restaurant Pos Export Order Tax Structure
  property_count: 4
  slug: restaurant-pos-export-order-tax-structure
- name: Restaurant Pos Export Order Type Structure
  property_count: 6
  slug: restaurant-pos-export-order-type-structure
- name: Restaurant Pos Export Owner Info Structure
  property_count: 3
  slug: restaurant-pos-export-owner-info-structure
- name: Restaurant Pos Export Paid In Out Structure
  property_count: 12
  slug: restaurant-pos-export-paid-in-out-structure
- name: Restaurant Pos Export Payment Option Structure
  property_count: 6
  slug: restaurant-pos-export-payment-option-structure
- name: Restaurant Pos Export Report Category Structure
  property_count: 5
  slug: restaurant-pos-export-report-category-structure
- name: Restaurant Pos Export Time Clock Entry Structure
  property_count: 13
  slug: restaurant-pos-export-time-clock-entry-structure
jsonld:
- class_count: 9
  name: Spoton Reserve Context
  property_count: 23
  slug: spoton-reserve-context
- class_count: 22
  name: Spoton Restaurant Pos Export Context
  property_count: 110
  slug: spoton-restaurant-pos-export-context
layout: provider
modified: '2026-06-03'
name: SpotOn
nav: Providers
network: true
overview: 'SpotOn publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Cash Deposits API, Employees API, and 12 more. Tagged areas include Restaurant, Point of Sale, Payments, Online Ordering, and Reservations.


  The SpotOn catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  SpotOn''s developer surface includes authentication, documentation, pricing, support, engineering blog, and 15 more developer resources.'
plans:
- name: Spoton Plans Pricing
  plan_count: 3
  slug: spoton-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 3
  name: Spoton Rate Limits
  slug: spoton-rate-limits
rules:
- name: SpotOn API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spoton-jsonschema-spectral-rules
- name: SpotOn API Rules
  rule_count: 35
  severity_counts:
    error: 10
    hint: 0
    info: 5
    warn: 20
  slug: spoton-rules
score:
  band: developing
  composite: 54.9
  delta: -7.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 68.6
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 15
      marker_coverage: 100.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/spoton/refs/heads/main/screenshots/spoton-2026-06-20T194358.png
security:
- kind: authentication
  name: Spoton Authentication
  slug: spoton-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spoton Domain Security
  slug: spoton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Spoton Trust Center
  slug: spoton-trust-center
  summary_line: SOC 2, PCI DSS
slug: spoton
tags:
- Restaurant
- Point of Sale
- Payments
- Online Ordering
- Reservations
- Reporting
use_cases:
- description: Export orders, payments, and cash deposits to reconcile against statements and accounting systems.
  name: Accounting and Reconciliation
- description: Pull POS sales and labor data into a warehouse for analytics and dashboards.
  name: Business Intelligence
- description: Export time clock entries and pay rates to drive payroll processing.
  name: Payroll Integration
- description: Keep third-party ordering and inventory systems in sync with the POS menu catalog.
  name: Menu Synchronization
- description: Build reservation and waitlist flows using the Reserve API and its JavaScript SDK.
  name: Guest Booking Experiences
website: https://www.spoton.com
---
