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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Uber Agentic Access
  operation_count: 57
  slug: uber-agentic-access
  summary_line: 57 operations · 27 acting
api_count: 20
apis:
- description: The Uber Guest Rides API enables businesses to allow their users to request rides from Uber without requiring an Uber account. Uses OAuth 2.0 with the guest.rides scope for authentication.
  name: Uber Guest Rides API
  slug: uber-guest-rides
- description: Voucher code generation and distribution
  name: Uber Codes API
  slug: uber-codes-api
- description: Delivery creation and management
  name: Uber Deliveries API
  slug: uber-deliveries-api
- description: Price and time estimates for rides
  name: Uber Estimates API
  slug: uber-estimates-api
- description: Business location management
  name: Uber Locations API
  slug: uber-locations-api
- description: Menu items, modifiers, and pricing
  name: Uber Menus API
  slug: uber-menus-api
- description: Eats order receipts
  name: Uber Orders API
  slug: uber-orders-api
- description: Organization and account management
  name: Uber Organizations API
  slug: uber-organizations-api
- description: Driver partner profile and activity data
  name: Uber Partners API
  slug: uber-partners-api
- description: Saved rider locations
  name: Uber Places API
  slug: uber-places-api
- description: Uber product types available at a location
  name: Uber Products API
  slug: uber-products-api
- description: Voucher program management
  name: Uber Programs API
  slug: uber-programs-api
- description: Voucher code redemption
  name: Uber Redemption API
  slug: uber-redemption-api
- description: Delivery refund processing
  name: Uber Refunds API
  slug: uber-refunds-api
- description: Analytics and performance metrics
  name: Uber Reporting API
  slug: uber-reporting-api
- description: Ride request management
  name: Uber Requests API
  slug: uber-requests-api
- description: Rider profile and history
  name: Uber Riders API
  slug: uber-riders-api
- description: Store management and operational status
  name: Uber Stores API
  slug: uber-stores-api
- description: Voucher program templates
  name: Uber Templates API
  slug: uber-templates-api
- description: Business trip receipts and invoices
  name: Uber Trips API
  slug: uber-trips-api
artifact_total: 112
collections:
- collection_type: postman
  name: Uber for Business Codes API
  slug: postman-uber-codes-api
- collection_type: postman
  name: Uber for Business Codes Deliveries API
  slug: postman-uber-deliveries-api
- collection_type: postman
  name: Uber for Business Codes Estimates API
  slug: postman-uber-estimates-api
- collection_type: postman
  name: Uber for Business Codes Locations API
  slug: postman-uber-locations-api
- collection_type: postman
  name: Uber for Business Codes Menus API
  slug: postman-uber-menus-api
- collection_type: postman
  name: Uber for Business Codes Orders API
  slug: postman-uber-orders-api
- collection_type: postman
  name: Uber for Business Codes Organizations API
  slug: postman-uber-organizations-api
- collection_type: postman
  name: Uber for Business Codes Partners API
  slug: postman-uber-partners-api
- collection_type: postman
  name: Uber for Business Codes Places API
  slug: postman-uber-places-api
- collection_type: postman
  name: Uber for Business Codes Products API
  slug: postman-uber-products-api
- collection_type: postman
  name: Uber for Business Codes Programs API
  slug: postman-uber-programs-api
- collection_type: postman
  name: Uber for Business Codes Redemption API
  slug: postman-uber-redemption-api
- collection_type: postman
  name: Uber for Business Codes Refunds API
  slug: postman-uber-refunds-api
- collection_type: postman
  name: Uber for Business Codes Reporting API
  slug: postman-uber-reporting-api
- collection_type: postman
  name: Uber for Business Codes Requests API
  slug: postman-uber-requests-api
- collection_type: postman
  name: Uber for Business Codes Riders API
  slug: postman-uber-riders-api
- collection_type: postman
  name: Uber for Business Codes Stores API
  slug: postman-uber-stores-api
- collection_type: postman
  name: Uber for Business Codes Templates API
  slug: postman-uber-templates-api
- collection_type: postman
  name: Uber for Business Codes Trips API
  slug: postman-uber-trips-api
- collection_type: open
  name: Uber for Business API
  slug: open-uber-businesses
- collection_type: open
  name: Uber Direct API
  slug: open-uber-direct
- collection_type: open
  name: Uber Drivers API
  slug: open-uber-drivers
- collection_type: open
  name: Uber Eats API
  slug: open-uber-eats
- collection_type: open
  name: Uber Riders API
  slug: open-uber-riders
- collection_type: open
  name: Uber Vouchers API
  slug: open-uber-vouchers
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/uber/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uber-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uber-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uber-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uber
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uber-com
- group: start
  title: ''
  type: Portal
  url: https://developer.uber.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uber.com/docs
- group: start
  title: ''
  type: Console
  url: https://developer.uber.com/dashboard
- group: start
  title: ''
  type: Signup
  url: https://developer.uber.com/dashboard
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uber.com/docs/riders/getting-started/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://developer.uber.com/docs/riders/guides/authentication/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uber.com/us/en/business/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.uber.com/docs/riders/policies/license-and-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uber.com/legal/en/document/?name=privacy-notice
- group: company
  title: ''
  type: Blog
  url: https://www.uber.com/blog/engineering/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/uber/uber-direct-sdk
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/uber-structure.json
- group: commercial
  title: ''
  type: Plans
  url: plans/uber-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uber-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uber-finops.yml
created: '2025-02-06'
description: Uber is a global technology platform offering transportation, food delivery, and logistics services. Its developer platform provides APIs for integrating ride requests, food ordering, on-demand delivery, voucher programs, and business travel management into third-party applications. APIs use OAuth 2.0 authentication with scope-based access controls and support both production and sandbox environments.
examples:
- key_count: 2
  name: Uber Direct Create Delivery Example
  slug: uber-direct-create-delivery-example
- key_count: 2
  name: Uber Eats Get Order Example
  slug: uber-eats-get-order-example
- key_count: 2
  name: Uber Riders Create Ride Request Example
  slug: uber-riders-create-ride-request-example
- key_count: 2
  name: Uber Riders List Products Example
  slug: uber-riders-list-products-example
features:
- description: All Uber developer APIs authenticate with OAuth 2.0 bearer tokens using scope-based access controls for both client-credentials (server-to-server) and authorization-code (on behalf of a user) flows.
  name: OAuth 2.0 Authorization
- description: Most APIs offer a sandbox for simulating rides, deliveries, and orders without dispatching real couriers or charging real payment methods.
  name: Sandbox Environment
- description: Uber Direct and Uber Eats publish real-time event webhooks for delivery status, courier updates, shopping progress, refunds, and order lifecycle changes.
  name: Webhooks
- description: Uber Direct exposes Uber's on-demand courier network so merchants can quote, create, track, and manage last-mile deliveries from their own storefronts.
  name: Courier Delivery Network
- description: Uber Eats Marketplace APIs let restaurants and POS partners synchronize stores, menus, and orders with the Uber Eats consumer marketplace in real time.
  name: Marketplace Integration
finops:
- name: Uber Finops
  service_category: Mobility / Logistics
  slug: uber-finops
graphqls:
- description: This conceptual GraphQL schema covers the full breadth of the Uber developer platform, spanning ride-sharing (Riders API, Drivers API, Guest Rides), food delivery (Uber Eats), on-demand courier logist
  name: Uber GraphQL Schema
  slug: uber-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uber.png
integrations:
- description: Uber Eats integrates with restaurant POS platforms for automated order injection and menu management.
  name: Point Of Sale Systems
- description: Uber Direct integrates with online ordering and e-commerce checkout flows to add same-day local delivery.
  name: E-Commerce And Ordering Platforms
- description: Uber for Business integrates with expense management and corporate travel platforms via receipts and invoices.
  name: Expense And Travel Management
json_schemas:
- name: Activities
  property_count: 4
  slug: uber-activities
- name: BusinessLocation
  property_count: 4
  slug: uber-businesslocation
- name: BusinessLocationRequest
  property_count: 4
  slug: uber-businesslocationrequest
- name: Uber Direct Delivery
  property_count: 11
  slug: uber-delivery
- name: DeliveryQuote
  property_count: 6
  slug: uber-deliveryquote
- name: DeliveryRequest
  property_count: 9
  slug: uber-deliveryrequest
- name: DriverProfile
  property_count: 8
  slug: uber-driverprofile
- name: DriverTrip
  property_count: 7
  slug: uber-drivertrip
- name: Menu
  property_count: 1
  slug: uber-menu
- name: MenuCategory
  property_count: 3
  slug: uber-menucategory
- name: MenuItem
  property_count: 6
  slug: uber-menuitem
- name: Order
  property_count: 7
  slug: uber-order
- name: OrderReceipt
  property_count: 8
  slug: uber-orderreceipt
- name: Organization
  property_count: 3
  slug: uber-organization
- name: Payment
  property_count: 7
  slug: uber-payment
- name: PaymentsResponse
  property_count: 4
  slug: uber-paymentsresponse
- name: Place
  property_count: 1
  slug: uber-place
- name: PlaceUpdate
  property_count: 1
  slug: uber-placeupdate
- name: PriceEstimate
  property_count: 9
  slug: uber-priceestimate
- name: Product
  property_count: 5
  slug: uber-product
- name: Receipt
  property_count: 8
  slug: uber-receipt
- name: Refund
  property_count: 5
  slug: uber-refund
- name: RefundRequest
  property_count: 3
  slug: uber-refundrequest
- name: ReportRequest
  property_count: 3
  slug: uber-reportrequest
- name: Uber Ride Request
  property_count: 8
  slug: uber-ride-request
- name: RideDetails
  property_count: 6
  slug: uber-ridedetails
- name: RideEstimate
  property_count: 1
  slug: uber-rideestimate
- name: RideRequest
  property_count: 8
  slug: uber-riderequest
- name: RiderProfile
  property_count: 6
  slug: uber-riderprofile
- name: Store
  property_count: 5
  slug: uber-store
- name: StoreUpdate
  property_count: 2
  slug: uber-storeupdate
- name: TimeEstimate
  property_count: 3
  slug: uber-timeestimate
- name: TripReceipt
  property_count: 12
  slug: uber-tripreceipt
- name: TripsResponse
  property_count: 4
  slug: uber-tripsresponse
- name: VoucherCode
  property_count: 3
  slug: uber-vouchercode
- name: VoucherProgram
  property_count: 8
  slug: uber-voucherprogram
- name: VoucherProgramRequest
  property_count: 6
  slug: uber-voucherprogramrequest
- name: VoucherProgramUpdate
  property_count: 2
  slug: uber-voucherprogramupdate
- name: VoucherTemplate
  property_count: 4
  slug: uber-vouchertemplate
json_structures:
- name: Uber Riders Structure
  property_count: 0
  slug: uber-riders-structure
- name: Uber Structure
  property_count: 0
  slug: uber-structure
jsonld:
- class_count: 8
  name: Uber Context
  property_count: 30
  slug: uber-context
layout: provider
modified: '2026-06-03'
name: Uber
nav: Providers
network: true
overview: 'Uber publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Codes API, Deliveries API, Estimates API, and 16 more. Tagged areas include Ride-Sharing, Rides, Taxis, Transportation, and Food Delivery.


  The Uber catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Uber''s developer surface includes authentication, developer portal, documentation, developer console, signup flow, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Uber Plans Pricing
  plan_count: 1
  slug: uber-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 1
  name: Uber Rate Limits
  slug: uber-rate-limits
rules:
- name: Uber API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uber-jsonschema-spectral-rules
- name: Uber API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 9
  slug: uber-rules
score:
  band: strong
  composite: 59.4
  delta: -2.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 78.4
    developer_ergonomics: 52.2
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uber/refs/heads/main/screenshots/uber-2026-06-20T195925.png
security:
- kind: authentication
  name: Uber Authentication
  slug: uber-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uber Domain Security
  slug: uber-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uber
tags:
- Ride-Sharing
- Rides
- Taxis
- Transportation
- Food Delivery
- Delivery
- Logistics
use_cases:
- description: Restaurants and food brands use Uber Direct to dispatch couriers for delivery of orders placed on their own websites and apps, bypassing the Uber Eats marketplace fee structure.
  name: Restaurant Delivery Fulfillment
- description: POS and online-ordering platforms integrate Uber Eats APIs to keep store hours, menus, pricing, and order status in sync between their systems and the Uber Eats marketplace.
  name: Menu And Order Synchronization
- description: Enterprises use Uber for Business and Vouchers to provision rides and meals for employees and guests with centralized billing, expense reporting, and policy controls.
  name: Corporate Travel And Meals
- description: Healthcare, hospitality, and service businesses use Guest Rides to request trips on behalf of customers who do not have an Uber account.
  name: Guest Ride Provisioning
website: https://developer.uber.com/
---
