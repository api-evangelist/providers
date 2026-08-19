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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Block Agentic Access
  operation_count: 8
  slug: block-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 5
apis:
- description: Manage product catalog
  name: Block Catalog API
  slug: block-catalog-api
- description: Customer management and engagement
  name: Block Customers API
  slug: block-customers-api
- description: Merchant and location data
  name: Block Merchants API
  slug: block-merchants-api
- description: Create and manage orders
  name: Block Orders API
  slug: block-orders-api
- description: Process and manage payments
  name: Block Payments API
  slug: block-payments-api
arazzos:
- description: Browse catalog items, open an order, and branch on whether the order is OPEN.
  name: Block Square Catalog Browse And Order Verify
  slug: block-catalog-browse-and-order-verify-workflow
- description: Browse the catalog, build an order from a selected item, and capture payment.
  name: Block Square Catalog Driven Order
  slug: block-catalog-driven-order-workflow
- description: Browse the catalog, create a customer, and open an order for them.
  name: Block Square Catalog To Customer Order
  slug: block-catalog-to-customer-order-workflow
- description: Create an order, branch on its state, and only take payment when it is OPEN.
  name: Block Square Customer Order Then Pay
  slug: block-customer-order-then-pay-workflow
- description: Pull a customer roster, list payments for a location, and detail the latest one.
  name: Block Square Customer Payment Audit
  slug: block-customer-payment-audit-workflow
- description: Resolve a location, create a customer, place an order, take payment, and verify it.
  name: Block Square Full Commerce Flow
  slug: block-full-commerce-flow-workflow
- description: Resolve the active seller location, open an order there, and take payment.
  name: Block Square Location First Sale
  slug: block-location-first-sale-workflow
- description: Resolve a location, list its recent payments, and detail the most recent one.
  name: Block Square Location Payment Reconciliation
  slug: block-location-payment-reconciliation-workflow
- description: Create a customer, place an order for them, then capture payment for that order.
  name: Block Square New Customer Checkout
  slug: block-new-customer-checkout-workflow
- description: Resolve a location, create a customer, and charge a direct payment to them.
  name: Block Square Onboard Customer And Charge
  slug: block-onboard-customer-and-charge-workflow
- description: List recent payments for a location and pull full detail on the most recent one.
  name: Block Square Reconcile Payment
  slug: block-reconcile-payment-workflow
- description: Find an existing customer or create one, then place and pay for their order.
  name: Block Square Returning Customer Checkout
  slug: block-returning-customer-checkout-workflow
- description: Take a card payment and immediately re-read it to confirm the final status.
  name: Block Square Take Payment And Verify
  slug: block-take-payment-and-verify-workflow
artifact_total: 64
collections:
- collection_type: postman
  name: Square API
  slug: postman-block-square-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Square Catalog API
  slug: open-block-catalog-api
- collection_type: open
  name: Square Catalog Customers API
  slug: open-block-customers-api
- collection_type: open
  name: Square Catalog Merchants API
  slug: open-block-merchants-api
- collection_type: open
  name: Square Catalog Orders API
  slug: open-block-orders-api
- collection_type: open
  name: Square Catalog Payments API
  slug: open-block-payments-api
common:
- group: other
  title: ''
  type: Subsidiary
  url: https://cash.app/
- group: company
  title: ''
  type: Blog
  url: https://block.xyz/news
- group: design
  title: ''
  type: Webhooks
  url: https://developer.squareup.com/docs/webhooks/overview
- group: start
  title: ''
  type: Sandbox
  url: https://developer.squareup.com/explorer
- group: agent
  title: ''
  type: MCPServer
  url: https://developer.squareup.com/docs/mcp
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.squareup.com/docs/release-notes
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/block-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/block-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/block-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/block-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/block/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-catalog-browse-and-order-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-catalog-driven-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-catalog-to-customer-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-customer-order-then-pay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-customer-payment-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-full-commerce-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-location-first-sale-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-location-payment-reconciliation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-new-customer-checkout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-onboard-customer-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-reconcile-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-returning-customer-checkout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/block-take-payment-and-verify-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/joinblock
- group: company
  title: ''
  type: Website
  url: https://www.block.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://developer.squareup.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.squareup.com/docs/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://squareup.com/us/en/payments/our-rates
- group: operate
  title: ''
  type: StatusPage
  url: https://www.issquareup.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.squareup.com/forums
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/square
- group: commercial
  title: ''
  type: TermsOfService
  url: https://squareup.com/us/en/legal/developer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://squareup.com/us/en/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://developer.squareup.com/apps
- group: build
  title: Square SDKs
  type: SDKs
  url: https://developer.squareup.com/docs/sdks
- group: design
  title: ''
  type: SpectralRules
  url: rules/block-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/block-vocabulary.yaml
created: '2024-09-27'
description: Block, Inc. is a global technology company building economic empowerment tools through a family of products including Square (commerce and payments), Cash App (personal finance and investing), Afterpay (buy now pay later), TIDAL (music streaming), and Spiral (open-source Bitcoin development). The Square API enables developers to build commerce applications with payment processing, order management, catalog, customer engagement, and business operations capabilities.
examples:
- key_count: 5
  name: Block Catalog Object Example
  slug: block-catalog-object-example
- key_count: 13
  name: Block Customer Example
  slug: block-customer-example
- key_count: 12
  name: Block Order Example
  slug: block-order-example
- key_count: 14
  name: Block Payment Example
  slug: block-payment-example
features:
- description: Accept card-present and card-not-present payments using Square hardware, web, or mobile SDKs with OAuth 2.0 or access token authentication.
  name: Payment Processing
- description: Create, update, and fulfill orders with line items, discounts, taxes, and service charges across online and in-person channels.
  name: Order Management
- description: Manage a unified product catalog with items, variations, modifiers, categories, taxes, and discounts synchronized across all locations.
  name: Catalog Management
- description: Build customer profiles, loyalty programs, gift cards, and marketing campaigns to drive repeat business and customer retention.
  name: Customer Engagement
- description: Manage multiple business locations with location-specific inventory, pricing, staff permissions, and reporting.
  name: Multi-Location Support
- description: Subscribe to real-time webhook events for payments, orders, inventory changes, customer activity, and subscription lifecycle events.
  name: Webhook Events
- description: Full sandbox environment with test card numbers, merchant accounts, and simulated hardware for development and testing.
  name: Sandbox Environment
finops:
- name: Block Finops
  service_category: API
  slug: block-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/block.png
integrations:
- description: Official Square extension for WooCommerce synchronizes inventory, products, and payments between WordPress stores and Square.
  name: WooCommerce
- description: Square integration for BigCommerce enables omnichannel selling with synchronized catalog and unified payment processing.
  name: BigCommerce
- description: Square-Xero integration automatically syncs sales transactions and payments to Xero accounting for reconciliation.
  name: Xero
- description: Square connector for QuickBooks Online syncs sales, refunds, and fees to QuickBooks for financial reporting.
  name: QuickBooks
json_schemas:
- name: CatalogObject
  property_count: 4
  slug: block-catalog-object
- name: Customer
  property_count: 7
  slug: block-customer
- name: Order
  property_count: 7
  slug: block-order
- name: Payment
  property_count: 8
  slug: block-payment
json_structures:
- name: Block Catalog Object Structure
  property_count: 0
  slug: block-catalog-object-structure
- name: Block Customer Structure
  property_count: 0
  slug: block-customer-structure
- name: Block Order Structure
  property_count: 0
  slug: block-order-structure
- name: Block Payment Structure
  property_count: 0
  slug: block-payment-structure
jsonld:
- class_count: 35
  name: Block Context
  property_count: 0
  slug: block-context
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
modified: '2026-05-19'
name: Block
nav: Providers
network: true
overview: 'Block publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Customers API, Merchants API, and 2 more. Tagged areas include Commerce, Cryptocurrency, eCommerce, Fintech, and Payments.


  The Block catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Block''s developer surface includes engineering blog, sandbox, changelog, authentication, documentation, getting-started guide, pricing, and 31 more developer resources.'
plans:
- name: Block Plans Pricing
  plan_count: 3
  slug: block-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Block Rate Limits
  slug: block-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Block API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: block-jsonschema-spectral-rules
- effective_rule_count: 75
  extends:
  - spectral:oas
  name: Block API Rules
  rule_count: 34
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 20
  slug: block-spectral-rules
scopes:
- name: Block Scopes
  scope_count: 6
  slug: block-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 42.6
  delta: -10.1
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 25.0
    contract_quality: 20.0
    developer_ergonomics: 59.5
    discoverability: 72.2
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/block/refs/heads/main/screenshots/block-2026-07-25T203345.png
security:
- kind: authentication
  name: Block Authentication
  slug: block-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Block Domain Security
  slug: block-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: block
tags:
- Commerce
- Cryptocurrency
- eCommerce
- Fintech
- Payments
- Point Of Sale
- Square
use_cases:
- description: Retailers and restaurants build custom POS applications using Square's payment, catalog, and order APIs.
  name: Point of Sale Integration
- description: Online stores integrate Square's Web Payments SDK and Orders API to accept payments and manage fulfillment.
  name: eCommerce Checkout
- description: Multi-seller marketplaces use Square Connect to route payments to sellers and manage fees through the Payouts API.
  name: Marketplace Payments
- description: SaaS and service businesses use Square Subscriptions API for automated recurring billing and invoice management.
  name: Subscription Billing
- description: Businesses implement custom loyalty programs using the Loyalty API to track points, tiers, and reward redemptions.
  name: Loyalty and Rewards
website: https://www.block.xyz
---
