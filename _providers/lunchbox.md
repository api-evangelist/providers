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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 55
  human_in_the_loop: 1
  name: Lunchbox Agentic Access
  operation_count: 102
  slug: lunchbox-agentic-access
  summary_line: 102 operations · 55 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Guest account registration, authentication, and profile management.
  name: Lunchbox Customer API
  slug: lunchbox-customer-api
- description: Reference data such as contact, countries, and states.
  name: Lunchbox Misc API
  slug: lunchbox-misc-api
- description: Order creation, item management, discounts, payments, and group orders.
  name: Lunchbox Orders API
  slug: lunchbox-orders-api
- description: Configure store service types.
  name: Lunchbox Service Types API
  slug: lunchbox-service-types-api
- description: Store configuration, hours, menus, and discounts.
  name: Lunchbox Stores API
  slug: lunchbox-stores-api
- description: Create, search, retrieve, update, validate, confirm, refund, and adjust loyalty user wallets.
  name: Lunchbox User Wallet API
  slug: lunchbox-user-wallet-api
artifact_total: 121
collections:
- collection_type: open
  name: Lunchbox Core API
  slug: open-lunchbox-core
- collection_type: open
  name: Lunchbox Loyalty API
  slug: open-lunchbox-loyalty
- collection_type: open
  name: Lunchbox Management API
  slug: open-lunchbox-management
- collection_type: open
  name: Lunchbox POS API
  slug: open-lunchbox-pos
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lunchbox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lunchbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lunchbox-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lunchbox.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lunchbox.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lunchbox.io/
- group: operate
  title: ''
  type: Support
  url: https://support.lunchbox.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lunchboxinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lunchboxtechnologies
- group: commercial
  title: ''
  type: Pricing
  url: https://lunchbox.io/service-fees
- group: operate
  title: ''
  type: StatusPage
  url: https://lunchbox.instatus.com
- group: commercial
  title: ''
  type: Plans
  url: plans/lunchbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lunchbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lunchbox-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lunchbox-vocabulary.yml
- group: design
  title: ''
  type: Spectral
  url: rules/lunchbox-spectral-rules.yml
created: '2026-06-02'
description: Lunchbox is a digital ordering and guest engagement platform for enterprise restaurant chains and ghost kitchens, offering online ordering, catering, loyalty, marketing CRM, order aggregation, and call center tooling across thousands of locations. For technology partners, Lunchbox provides an Open API that connects a restaurant's tech stack to its ecosystem, exposing location and menu data, guest account management, and order injection into the POS. The Open API supports last-mile delivery webhooks, menu consumption for digital boards and kiosks, and third-party marketplace integrations, and is documented on a dedicated developer portal at docs.lunchbox.io.
examples:
- key_count: 2
  name: Core Add Items Request Example
  slug: core-add-items-request-example
- key_count: 11
  name: Core Address Example
  slug: core-address-example
- key_count: 2
  name: Core Auth Session Example
  slug: core-auth-session-example
- key_count: 6
  name: Core Charges Example
  slug: core-charges-example
- key_count: 12
  name: Core Customer Example
  slug: core-customer-example
- key_count: 2
  name: Core Login Request Example
  slug: core-login-request-example
- key_count: 3
  name: Core Menu Example
  slug: core-menu-example
- key_count: 7
  name: Core Menu Item Example
  slug: core-menu-item-example
- key_count: 4
  name: Core New Order Request Example
  slug: core-new-order-request-example
- key_count: 7
  name: Core Order Child Item Example
  slug: core-order-child-item-example
- key_count: 10
  name: Core Order Example
  slug: core-order-example
- key_count: 8
  name: Core Order Item Example
  slug: core-order-item-example
- key_count: 8
  name: Core Registration Request Example
  slug: core-registration-request-example
- key_count: 11
  name: Core Store Example
  slug: core-store-example
- key_count: 5
  name: Loyalty User Wallet Create Example
  slug: loyalty-user-wallet-create-example
- key_count: 15
  name: Loyalty User Wallet Example
  slug: loyalty-user-wallet-example
- key_count: 4
  name: Loyalty User Wallet Update Example
  slug: loyalty-user-wallet-update-example
- key_count: 1
  name: Loyalty Wallet Reward Example
  slug: loyalty-wallet-reward-example
- key_count: 8
  name: Management Managed Order Summary Example
  slug: management-managed-order-summary-example
- key_count: 4
  name: Management Managed Store Example
  slug: management-managed-store-example
- key_count: 12
  name: Management Managed Store Summary Example
  slug: management-managed-store-summary-example
- key_count: 4
  name: Management Order Page Example
  slug: management-order-page-example
- key_count: 10
  name: Management Service Type Config Example
  slug: management-service-type-config-example
- key_count: 4
  name: Management Store Page Example
  slug: management-store-page-example
- key_count: 3
  name: Pos Order Update Event Example
  slug: pos-order-update-event-example
- key_count: 11
  name: Pos Pos Contact Example
  slug: pos-pos-contact-example
- key_count: 3
  name: Pos Pos Hours Example
  slug: pos-pos-hours-example
- key_count: 1
  name: Pos Pos Location Example
  slug: pos-pos-location-example
- key_count: 3
  name: Pos Pos Order Ack Example
  slug: pos-pos-order-ack-example
- key_count: 9
  name: Pos Pos Order Example
  slug: pos-pos-order-example
- key_count: 10
  name: Pos Pos Order Location Example
  slug: pos-pos-order-location-example
- key_count: 5
  name: Pos Pos Store Example
  slug: pos-pos-store-example
- key_count: 2
  name: Pos Store Update Event Example
  slug: pos-store-update-event-example
finops:
- name: Lunchbox Finops
  service_category: Restaurant Commerce
  slug: lunchbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lunchbox.png
json_schemas:
- name: AddItemsRequest
  property_count: 2
  slug: core-add-items-request
- name: Address
  property_count: 11
  slug: core-address
- name: AuthSession
  property_count: 2
  slug: core-auth-session
- name: Charges
  property_count: 6
  slug: core-charges
- name: Customer
  property_count: 12
  slug: core-customer
- name: LoginRequest
  property_count: 2
  slug: core-login-request
- name: MenuItem
  property_count: 7
  slug: core-menu-item
- name: Menu
  property_count: 3
  slug: core-menu
- name: NewOrderRequest
  property_count: 4
  slug: core-new-order-request
- name: OrderChildItem
  property_count: 7
  slug: core-order-child-item
- name: OrderItem
  property_count: 8
  slug: core-order-item
- name: Order
  property_count: 10
  slug: core-order
- name: RegistrationRequest
  property_count: 8
  slug: core-registration-request
- name: Store
  property_count: 11
  slug: core-store
- name: UserWalletCreate
  property_count: 5
  slug: loyalty-user-wallet-create
- name: UserWallet
  property_count: 15
  slug: loyalty-user-wallet
- name: UserWalletUpdate
  property_count: 4
  slug: loyalty-user-wallet-update
- name: WalletReward
  property_count: 1
  slug: loyalty-wallet-reward
- name: ManagedOrderSummary
  property_count: 8
  slug: management-managed-order-summary
- name: ManagedStore
  property_count: 4
  slug: management-managed-store
- name: ManagedStoreSummary
  property_count: 12
  slug: management-managed-store-summary
- name: OrderPage
  property_count: 4
  slug: management-order-page
- name: ServiceTypeConfig
  property_count: 10
  slug: management-service-type-config
- name: StorePage
  property_count: 4
  slug: management-store-page
- name: OrderUpdateEvent
  property_count: 3
  slug: pos-order-update-event
- name: PosContact
  property_count: 11
  slug: pos-pos-contact
- name: PosHours
  property_count: 3
  slug: pos-pos-hours
- name: PosLocation
  property_count: 1
  slug: pos-pos-location
- name: PosOrderAck
  property_count: 3
  slug: pos-pos-order-ack
- name: PosOrderLocation
  property_count: 10
  slug: pos-pos-order-location
- name: PosOrder
  property_count: 9
  slug: pos-pos-order
- name: PosStore
  property_count: 5
  slug: pos-pos-store
- name: StoreUpdateEvent
  property_count: 2
  slug: pos-store-update-event
json_structures:
- name: Core Add Items Request Structure
  property_count: 2
  slug: core-add-items-request-structure
- name: Core Address Structure
  property_count: 11
  slug: core-address-structure
- name: Core Auth Session Structure
  property_count: 2
  slug: core-auth-session-structure
- name: Core Charges Structure
  property_count: 6
  slug: core-charges-structure
- name: Core Customer Structure
  property_count: 12
  slug: core-customer-structure
- name: Core Login Request Structure
  property_count: 2
  slug: core-login-request-structure
- name: Core Menu Item Structure
  property_count: 7
  slug: core-menu-item-structure
- name: Core Menu Structure
  property_count: 3
  slug: core-menu-structure
- name: Core New Order Request Structure
  property_count: 4
  slug: core-new-order-request-structure
- name: Core Order Child Item Structure
  property_count: 7
  slug: core-order-child-item-structure
- name: Core Order Item Structure
  property_count: 8
  slug: core-order-item-structure
- name: Core Order Structure
  property_count: 10
  slug: core-order-structure
- name: Core Registration Request Structure
  property_count: 8
  slug: core-registration-request-structure
- name: Core Store Structure
  property_count: 11
  slug: core-store-structure
- name: Loyalty User Wallet Create Structure
  property_count: 5
  slug: loyalty-user-wallet-create-structure
- name: Loyalty User Wallet Structure
  property_count: 15
  slug: loyalty-user-wallet-structure
- name: Loyalty User Wallet Update Structure
  property_count: 4
  slug: loyalty-user-wallet-update-structure
- name: Loyalty Wallet Reward Structure
  property_count: 1
  slug: loyalty-wallet-reward-structure
- name: Management Managed Order Summary Structure
  property_count: 8
  slug: management-managed-order-summary-structure
- name: Management Managed Store Structure
  property_count: 4
  slug: management-managed-store-structure
- name: Management Managed Store Summary Structure
  property_count: 12
  slug: management-managed-store-summary-structure
- name: Management Order Page Structure
  property_count: 4
  slug: management-order-page-structure
- name: Management Service Type Config Structure
  property_count: 10
  slug: management-service-type-config-structure
- name: Management Store Page Structure
  property_count: 4
  slug: management-store-page-structure
- name: Pos Order Update Event Structure
  property_count: 3
  slug: pos-order-update-event-structure
- name: Pos Pos Contact Structure
  property_count: 11
  slug: pos-pos-contact-structure
- name: Pos Pos Hours Structure
  property_count: 3
  slug: pos-pos-hours-structure
- name: Pos Pos Location Structure
  property_count: 1
  slug: pos-pos-location-structure
- name: Pos Pos Order Ack Structure
  property_count: 3
  slug: pos-pos-order-ack-structure
- name: Pos Pos Order Location Structure
  property_count: 10
  slug: pos-pos-order-location-structure
- name: Pos Pos Order Structure
  property_count: 9
  slug: pos-pos-order-structure
- name: Pos Pos Store Structure
  property_count: 5
  slug: pos-pos-store-structure
- name: Pos Store Update Event Structure
  property_count: 2
  slug: pos-store-update-event-structure
jsonld:
- class_count: 17
  name: Lunchbox Core Context
  property_count: 64
  slug: lunchbox-core-context
- class_count: 5
  name: Lunchbox Loyalty Context
  property_count: 14
  slug: lunchbox-loyalty-context
- class_count: 6
  name: Lunchbox Management Context
  property_count: 38
  slug: lunchbox-management-context
- class_count: 11
  name: Lunchbox Pos Context
  property_count: 45
  slug: lunchbox-pos-context
layout: provider
modified: '2026-06-02'
name: Lunchbox
nav: Providers
network: true
overview: 'Lunchbox publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Customer API, Misc API, Orders API, and 3 more. Tagged areas include Restaurant, Online Ordering, Guest Engagement, Catering, and Menus.


  The Lunchbox catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Lunchbox''s developer surface includes authentication, documentation, API reference, support, pricing, and 11 more developer resources.'
plans:
- name: Lunchbox Plans Pricing
  plan_count: 2
  slug: lunchbox-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Lunchbox Rate Limits
  slug: lunchbox-rate-limits
rules:
- name: Lunchbox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lunchbox-jsonschema-spectral-rules
- name: Lunchbox API Rules
  rule_count: 37
  severity_counts:
    error: 8
    hint: 0
    info: 8
    warn: 21
  slug: lunchbox-spectral-rules
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.0
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lunchbox/refs/heads/main/screenshots/lunchbox-2026-06-20T184805.png
security:
- kind: authentication
  name: Lunchbox Authentication
  slug: lunchbox-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lunchbox Domain Security
  slug: lunchbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lunchbox
tags:
- Restaurant
- Online Ordering
- Guest Engagement
- Catering
- Menus
- Orders
- Loyalty
- Enterprise
website: https://lunchbox.io/
---
