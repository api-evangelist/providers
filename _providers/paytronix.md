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
- acting_count: 17
  human_in_the_loop: 0
  name: Paytronix Agentic Access
  operation_count: 30
  slug: paytronix-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 12
apis:
- description: Check-based point accrual, reward computation, and posting.
  name: Paytronix Check API
  slug: paytronix-check-api
- description: Card creation, activation, registration, and demographic editing.
  name: Paytronix Enrollment API
  slug: paytronix-enrollment-api
- description: Gift card sale, reload, balance, redeem, and exchange.
  name: Paytronix Gift API
  slug: paytronix-gift-api
- description: Guest account and user information lookup and management.
  name: Paytronix Guest API
  slug: paytronix-guest-api
- description: Menu item retrieval.
  name: Paytronix Menu Items API
  slug: paytronix-menu-items-api
- description: Guest authentication and token issuance.
  name: Paytronix OAuth API
  slug: paytronix-oauth-api
- description: Order creation, retrieval, and submission.
  name: Paytronix Orders API
  slug: paytronix-orders-api
- description: Stored-value recharge, saved payment methods, and auto recharge.
  name: Paytronix Payment API
  slug: paytronix-payment-api
- description: Restaurant and location discovery.
  name: Paytronix Restaurants API
  slug: paytronix-restaurants-api
- description: Geospatial and full-text search across restaurants and menu items.
  name: Paytronix Search API
  slug: paytronix-search-api
- description: Store and location lookup and management.
  name: Paytronix Store API
  slug: paytronix-store-api
- description: Loyalty and stored-value transaction processing at the POS.
  name: Paytronix Transaction API
  slug: paytronix-transaction-api
artifact_total: 174
collections:
- collection_type: open
  name: Paytronix Online Ordering API
  slug: open-paytronix-online-ordering-api
- collection_type: open
  name: Paytronix Server API
  slug: open-paytronix-server-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paytronix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paytronix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paytronix-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.paytronix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.paytronix.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.paytronix.com/pxs_api_reference/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paytronix.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.paytronix.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.paytronix.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paytronix-systems
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paytronix
- group: design
  title: ''
  type: SpectralRules
  url: rules/paytronix-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/paytronix-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paytronix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paytronix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paytronix-finops.yml
created: '2026-06-02'
description: Paytronix is a cloud-based digital guest engagement platform for restaurants and convenience stores, providing loyalty programs, gift and stored-value cards, online ordering, branded mobile apps, messaging, and analytics to more than 1,800 brands. Paytronix publishes extensive public integration documentation describing a REST-based Server API with 40-plus services spanning guests, enrollment, transactions, checks, payments, gift, messaging, campaigns, stores, and mobile wallet passes. Authentication supports OAuth, client credentials (integration identifier and secret via HTTP Basic), and B2B flows. A separate Online Ordering API is documented for ordering integrations, making Paytronix a developer-friendly guest engagement provider.
examples:
- key_count: 2
  name: Online Ordering Api Coordinates Example
  slug: online-ordering-api-coordinates-example
- key_count: 4
  name: Online Ordering Api Customer Example
  slug: online-ordering-api-customer-example
- key_count: 5
  name: Online Ordering Api Delivery Address Example
  slug: online-ordering-api-delivery-address-example
- key_count: 0
  name: Online Ordering Api Facets Example
  slug: online-ordering-api-facets-example
- key_count: 6
  name: Online Ordering Api Menu Item Example
  slug: online-ordering-api-menu-item-example
- key_count: 3
  name: Online Ordering Api Menu Item Search Results Example
  slug: online-ordering-api-menu-item-search-results-example
- key_count: 10
  name: Online Ordering Api Order Example
  slug: online-ordering-api-order-example
- key_count: 6
  name: Online Ordering Api Order Input Example
  slug: online-ordering-api-order-input-example
- key_count: 5
  name: Online Ordering Api Order Item Example
  slug: online-ordering-api-order-item-example
- key_count: 13
  name: Online Ordering Api Restaurant Example
  slug: online-ordering-api-restaurant-example
- key_count: 3
  name: Online Ordering Api Restaurant Search Results Example
  slug: online-ordering-api-restaurant-search-results-example
- key_count: 10
  name: Server Api Account Information Reply Example
  slug: server-api-account-information-reply-example
- key_count: 2
  name: Server Api Account Query Reply Example
  slug: server-api-account-query-reply-example
- key_count: 3
  name: Server Api Account Query Request Example
  slug: server-api-account-query-request-example
- key_count: 5
  name: Server Api Activate And Register Request Example
  slug: server-api-activate-and-register-request-example
- key_count: 3
  name: Server Api Add Redeem Reply Example
  slug: server-api-add-redeem-reply-example
- key_count: 4
  name: Server Api Add Redeem Request Example
  slug: server-api-add-redeem-request-example
- key_count: 6
  name: Server Api Address Example
  slug: server-api-address-example
- key_count: 3
  name: Server Api Card Info Example
  slug: server-api-card-info-example
- key_count: 3
  name: Server Api Change Card Status Request Example
  slug: server-api-change-card-status-request-example
- key_count: 6
  name: Server Api Charge Response Example
  slug: server-api-charge-response-example
- key_count: 4
  name: Server Api Check Example
  slug: server-api-check-example
- key_count: 8
  name: Server Api Compute Rewards Reply Example
  slug: server-api-compute-rewards-reply-example
- key_count: 7
  name: Server Api Compute Rewards Request Example
  slug: server-api-compute-rewards-request-example
- key_count: 7
  name: Server Api Create And Register Request Example
  slug: server-api-create-and-register-request-example
- key_count: 2
  name: Server Api Enrollment Config Reply Example
  slug: server-api-enrollment-config-reply-example
- key_count: 6
  name: Server Api Enrollment Reply Example
  slug: server-api-enrollment-reply-example
- key_count: 3
  name: Server Api Gift Balance Request Example
  slug: server-api-gift-balance-request-example
- key_count: 9
  name: Server Api Gift Redeem Request Example
  slug: server-api-gift-redeem-request-example
- key_count: 6
  name: Server Api Gift Reply Example
  slug: server-api-gift-reply-example
- key_count: 8
  name: Server Api Gift Request Example
  slug: server-api-gift-request-example
- key_count: 6
  name: Server Api Guest Token Request Example
  slug: server-api-guest-token-request-example
- key_count: 6
  name: Server Api Guest Token Response Example
  slug: server-api-guest-token-response-example
- key_count: 6
  name: Server Api Header Info Example
  slug: server-api-header-info-example
- key_count: 8
  name: Server Api Location Example
  slug: server-api-location-example
- key_count: 2
  name: Server Api Locations Reply Example
  slug: server-api-locations-reply-example
- key_count: 8
  name: Server Api Post And Accrue Request Example
  slug: server-api-post-and-accrue-request-example
- key_count: 5
  name: Server Api Recharge Request Example
  slug: server-api-recharge-request-example
- key_count: 2
  name: Server Api Saved Payment Methods Reply Example
  slug: server-api-saved-payment-methods-reply-example
- key_count: 3
  name: Server Api Transaction History Reply Example
  slug: server-api-transaction-history-reply-example
- key_count: 5
  name: Server Api Transaction Reply Example
  slug: server-api-transaction-reply-example
- key_count: 3
  name: Server Api Transaction Request Example
  slug: server-api-transaction-request-example
- key_count: 4
  name: Server Api User Information Reply Example
  slug: server-api-user-information-reply-example
- key_count: 3
  name: Server Api Wallet Balance Example
  slug: server-api-wallet-balance-example
- key_count: 3
  name: Server Api Wallet Content Example
  slug: server-api-wallet-content-example
features:
- description: Points, tiers, rewards, challenges, and referrals managed through the Server API Guest, Transaction, and Check services.
  name: Loyalty Programs
- description: Sell, reload, redeem, balance, and exchange gift and stored-value cards via the Gift and Transaction services.
  name: Gift And Stored Value
- description: Restaurant and menu discovery, search, and order creation and submission across six order methods via the Online Ordering API.
  name: Online Ordering
- description: Stored-value recharge, saved payment methods, auto recharge, and Stripe/Apple Pay/Spreedly integration via the Payment service.
  name: Payments
- description: Create, activate, and register virtual and physical cards with configurable enrollment fields via the Enrollment service.
  name: Guest Enrollment
- description: Guest messaging, campaign feedback, and message-frequency preferences managed through the messaging services.
  name: Messaging And Campaigns
finops:
- name: Paytronix Finops
  service_category: Guest Engagement + Loyalty
  slug: paytronix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paytronix.png
integrations:
- description: Payment processing via checkout sessions and payment intents in the Payment service.
  name: Stripe
- description: Apple Pay merchant validation and domain registration in the Payment service.
  name: Apple Pay
- description: Card tokenization via Spreedly iframe parameters in the Payment service.
  name: Spreedly
- description: Mobile wallet passes via the Apple Passbook service.
  name: Apple Wallet
- description: Mobile wallet passes via the Google Wallet (Android Pay) service.
  name: Google Wallet
json_schemas:
- name: Coordinates
  property_count: 2
  slug: online-ordering-api-coordinates
- name: Customer
  property_count: 4
  slug: online-ordering-api-customer
- name: DeliveryAddress
  property_count: 5
  slug: online-ordering-api-delivery-address
- name: Facets
  property_count: 0
  slug: online-ordering-api-facets
- name: MenuItem
  property_count: 6
  slug: online-ordering-api-menu-item
- name: MenuItemSearchResults
  property_count: 3
  slug: online-ordering-api-menu-item-search-results
- name: OrderInput
  property_count: 6
  slug: online-ordering-api-order-input
- name: OrderItem
  property_count: 5
  slug: online-ordering-api-order-item
- name: Order
  property_count: 10
  slug: online-ordering-api-order
- name: Restaurant
  property_count: 13
  slug: online-ordering-api-restaurant
- name: RestaurantSearchResults
  property_count: 3
  slug: online-ordering-api-restaurant-search-results
- name: AccountInformationReply
  property_count: 10
  slug: server-api-account-information-reply
- name: AccountQueryReply
  property_count: 2
  slug: server-api-account-query-reply
- name: AccountQueryRequest
  property_count: 3
  slug: server-api-account-query-request
- name: ActivateAndRegisterRequest
  property_count: 5
  slug: server-api-activate-and-register-request
- name: AddRedeemReply
  property_count: 3
  slug: server-api-add-redeem-reply
- name: AddRedeemRequest
  property_count: 4
  slug: server-api-add-redeem-request
- name: Address
  property_count: 6
  slug: server-api-address
- name: CardInfo
  property_count: 3
  slug: server-api-card-info
- name: ChangeCardStatusRequest
  property_count: 3
  slug: server-api-change-card-status-request
- name: ChargeResponse
  property_count: 6
  slug: server-api-charge-response
- name: Check
  property_count: 4
  slug: server-api-check
- name: ComputeRewardsReply
  property_count: 8
  slug: server-api-compute-rewards-reply
- name: ComputeRewardsRequest
  property_count: 7
  slug: server-api-compute-rewards-request
- name: CreateAndRegisterRequest
  property_count: 7
  slug: server-api-create-and-register-request
- name: EnrollmentConfigReply
  property_count: 2
  slug: server-api-enrollment-config-reply
- name: EnrollmentReply
  property_count: 6
  slug: server-api-enrollment-reply
- name: GiftBalanceRequest
  property_count: 3
  slug: server-api-gift-balance-request
- name: GiftRedeemRequest
  property_count: 0
  slug: server-api-gift-redeem-request
- name: GiftReply
  property_count: 6
  slug: server-api-gift-reply
- name: GiftRequest
  property_count: 8
  slug: server-api-gift-request
- name: GuestTokenRequest
  property_count: 6
  slug: server-api-guest-token-request
- name: GuestTokenResponse
  property_count: 6
  slug: server-api-guest-token-response
- name: HeaderInfo
  property_count: 6
  slug: server-api-header-info
- name: Location
  property_count: 8
  slug: server-api-location
- name: LocationsReply
  property_count: 2
  slug: server-api-locations-reply
- name: PostAndAccrueRequest
  property_count: 8
  slug: server-api-post-and-accrue-request
- name: RechargeRequest
  property_count: 5
  slug: server-api-recharge-request
- name: SavedPaymentMethodsReply
  property_count: 2
  slug: server-api-saved-payment-methods-reply
- name: TransactionHistoryReply
  property_count: 3
  slug: server-api-transaction-history-reply
- name: TransactionReply
  property_count: 5
  slug: server-api-transaction-reply
- name: TransactionRequest
  property_count: 3
  slug: server-api-transaction-request
- name: UserInformationReply
  property_count: 4
  slug: server-api-user-information-reply
- name: WalletBalance
  property_count: 3
  slug: server-api-wallet-balance
- name: WalletContent
  property_count: 3
  slug: server-api-wallet-content
json_structures:
- name: Online Ordering Api Coordinates Structure
  property_count: 2
  slug: online-ordering-api-coordinates-structure
- name: Online Ordering Api Customer Structure
  property_count: 4
  slug: online-ordering-api-customer-structure
- name: Online Ordering Api Delivery Address Structure
  property_count: 5
  slug: online-ordering-api-delivery-address-structure
- name: Online Ordering Api Facets Structure
  property_count: 0
  slug: online-ordering-api-facets-structure
- name: Online Ordering Api Menu Item Search Results Structure
  property_count: 3
  slug: online-ordering-api-menu-item-search-results-structure
- name: Online Ordering Api Menu Item Structure
  property_count: 6
  slug: online-ordering-api-menu-item-structure
- name: Online Ordering Api Order Input Structure
  property_count: 6
  slug: online-ordering-api-order-input-structure
- name: Online Ordering Api Order Item Structure
  property_count: 5
  slug: online-ordering-api-order-item-structure
- name: Online Ordering Api Order Structure
  property_count: 10
  slug: online-ordering-api-order-structure
- name: Online Ordering Api Restaurant Search Results Structure
  property_count: 3
  slug: online-ordering-api-restaurant-search-results-structure
- name: Online Ordering Api Restaurant Structure
  property_count: 13
  slug: online-ordering-api-restaurant-structure
- name: Server Api Account Information Reply Structure
  property_count: 10
  slug: server-api-account-information-reply-structure
- name: Server Api Account Query Reply Structure
  property_count: 2
  slug: server-api-account-query-reply-structure
- name: Server Api Account Query Request Structure
  property_count: 3
  slug: server-api-account-query-request-structure
- name: Server Api Activate And Register Request Structure
  property_count: 5
  slug: server-api-activate-and-register-request-structure
- name: Server Api Add Redeem Reply Structure
  property_count: 3
  slug: server-api-add-redeem-reply-structure
- name: Server Api Add Redeem Request Structure
  property_count: 4
  slug: server-api-add-redeem-request-structure
- name: Server Api Address Structure
  property_count: 6
  slug: server-api-address-structure
- name: Server Api Card Info Structure
  property_count: 3
  slug: server-api-card-info-structure
- name: Server Api Change Card Status Request Structure
  property_count: 3
  slug: server-api-change-card-status-request-structure
- name: Server Api Charge Response Structure
  property_count: 6
  slug: server-api-charge-response-structure
- name: Server Api Check Structure
  property_count: 4
  slug: server-api-check-structure
- name: Server Api Compute Rewards Reply Structure
  property_count: 8
  slug: server-api-compute-rewards-reply-structure
- name: Server Api Compute Rewards Request Structure
  property_count: 7
  slug: server-api-compute-rewards-request-structure
- name: Server Api Create And Register Request Structure
  property_count: 7
  slug: server-api-create-and-register-request-structure
- name: Server Api Enrollment Config Reply Structure
  property_count: 2
  slug: server-api-enrollment-config-reply-structure
- name: Server Api Enrollment Reply Structure
  property_count: 6
  slug: server-api-enrollment-reply-structure
- name: Server Api Gift Balance Request Structure
  property_count: 3
  slug: server-api-gift-balance-request-structure
- name: Server Api Gift Redeem Request Structure
  property_count: 0
  slug: server-api-gift-redeem-request-structure
- name: Server Api Gift Reply Structure
  property_count: 6
  slug: server-api-gift-reply-structure
- name: Server Api Gift Request Structure
  property_count: 8
  slug: server-api-gift-request-structure
- name: Server Api Guest Token Request Structure
  property_count: 6
  slug: server-api-guest-token-request-structure
- name: Server Api Guest Token Response Structure
  property_count: 6
  slug: server-api-guest-token-response-structure
- name: Server Api Header Info Structure
  property_count: 6
  slug: server-api-header-info-structure
- name: Server Api Location Structure
  property_count: 8
  slug: server-api-location-structure
- name: Server Api Locations Reply Structure
  property_count: 2
  slug: server-api-locations-reply-structure
- name: Server Api Post And Accrue Request Structure
  property_count: 8
  slug: server-api-post-and-accrue-request-structure
- name: Server Api Recharge Request Structure
  property_count: 5
  slug: server-api-recharge-request-structure
- name: Server Api Saved Payment Methods Reply Structure
  property_count: 2
  slug: server-api-saved-payment-methods-reply-structure
- name: Server Api Transaction History Reply Structure
  property_count: 3
  slug: server-api-transaction-history-reply-structure
- name: Server Api Transaction Reply Structure
  property_count: 5
  slug: server-api-transaction-reply-structure
- name: Server Api Transaction Request Structure
  property_count: 3
  slug: server-api-transaction-request-structure
- name: Server Api User Information Reply Structure
  property_count: 4
  slug: server-api-user-information-reply-structure
- name: Server Api Wallet Balance Structure
  property_count: 3
  slug: server-api-wallet-balance-structure
- name: Server Api Wallet Content Structure
  property_count: 3
  slug: server-api-wallet-content-structure
jsonld:
- class_count: 11
  name: Paytronix Online Ordering Api Context
  property_count: 37
  slug: paytronix-online-ordering-api-context
- class_count: 33
  name: Paytronix Server Api Context
  property_count: 116
  slug: paytronix-server-api-context
layout: provider
modified: '2026-06-03'
name: Paytronix
nav: Providers
network: true
overview: 'Paytronix publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Check API, Enrollment API, Gift API, and 9 more. Tagged areas include Restaurant, Loyalty, Gift Cards, Online Ordering, and Guest Engagement.


  The Paytronix catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Paytronix''s developer surface includes authentication, documentation, API reference, pricing, support, engineering blog, and 10 more developer resources.'
plans:
- name: Paytronix Plans Pricing
  plan_count: 2
  slug: paytronix-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Paytronix Rate Limits
  slug: paytronix-rate-limits
rules:
- name: Paytronix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: paytronix-jsonschema-spectral-rules
- name: Paytronix API Rules
  rule_count: 39
  severity_counts:
    error: 5
    hint: 0
    info: 13
    warn: 21
  slug: paytronix-spectral-rules
score:
  band: developing
  composite: 44.7
  delta: -8.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.6
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/paytronix/refs/heads/main/screenshots/paytronix-2026-06-20T191510.png
security:
- kind: authentication
  name: Paytronix Authentication
  slug: paytronix-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Paytronix Domain Security
  slug: paytronix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paytronix
tags:
- Restaurant
- Loyalty
- Gift Cards
- Online Ordering
- Guest Engagement
- Payments
- Messaging
use_cases:
- description: Authenticate guests with the OAuth Service and surface balances, tiers, and transaction history from the Guest service.
  name: Branded Loyalty Mobile App
- description: Activate cards, accrue points, and redeem rewards at the register using the Transaction and Check services.
  name: Point-Of-Sale Loyalty Integration
- description: Sell and redeem gift cards online and in store with the Gift service and stored-value recharge via the Payment service.
  name: Gift Card Program
- description: Build ordering experiences with restaurant/menu search and order submission through the Online Ordering API.
  name: Online And Mobile Ordering
website: https://www.paytronix.com/
---
