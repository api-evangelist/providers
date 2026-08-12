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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Bolt Agentic Access
  operation_count: 16
  slug: bolt-agentic-access
  summary_line: 16 operations · 14 acting
api_count: 13
apis:
- description: 'Core Bolt REST API for generating order tokens, managing transactions, pulling financial statements, and integrating one-click checkout into merchant storefronts. Supports both sandbox and production '
  name: Bolt API
  slug: bolt-api
- description: API for configuring and embedding Bolt's checkout experience and shopper account management directly into merchant storefronts, including login modals, account creation, passwordless authentication, a
  name: Embeddable Checkout v3 API
  slug: embeddable-checkout-v3-api
- description: API enabling merchant backends to respond to Bolt checkout events including discount application, cart creation and updates, shipping and tax calculations, and transaction status updates.
  name: Merchant Callback API
  slug: merchant-callback-api
- description: API for creating and managing Bolt Subscriptions, enabling recurring billing and subscription commerce on top of the Bolt checkout platform.
  name: Subscriptions API
  slug: subscriptions-api
- description: API for implementing custom back-office integrations including direct payment processing and card tokenization for merchant-side payment workflows.
  name: Tokenizer API
  slug: tokenizer-api
- description: API for platforms to complete connected merchant onboarding to Bolt, enabling platform partners to programmatically onboard new merchants.
  name: Bolt Connect Merchant Onboarding API
  slug: bolt-connect-api
- description: Beta API enabling Bolt checkout links and checkout experiences across any surface, including social commerce, email, and other off-site channels.
  name: Checkout Everywhere API
  slug: checkout-everywhere-api
- description: Use the Accounts API to access shoppers' accounts to empower your checkout and facilitate shoppers' choices.
  name: Bolt Account API
  slug: bolt-account-api
- description: Implement Callback endpoints on your servers to power Bolt experiences. Different Bolt packages require different callbacks to be implemented. Consult your relevant product documentation for a list of
  name: Bolt Callbacks API
  slug: bolt-callbacks-api
- description: Use the OAuth API to enable your ecommerce server to make API calls on behalf of a Bolt logged-in shopper.
  name: Bolt OAuth API
  slug: bolt-oauth-api
- description: Use the Orders API to create and manage orders, including orders that have been placed outside the Bolt ecosystem.
  name: Bolt Orders API
  slug: bolt-orders-api
- description: Use the Payments API to process credit card and alternative payment methods with Bolt.
  name: Bolt Payments API
  slug: bolt-payments-api
- description: Use the Testing API to generate and retrieve test data to verify a subset of flows in non-production environments.
  name: Bolt Testing API
  slug: bolt-testing-api
artifact_total: 110
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bolt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bolt-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bolt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bolt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bolt-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.bolt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.bolt.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/BoltApp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bolt-com
- group: company
  title: ''
  type: Blog
  url: https://www.bolt.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://help.bolt.com/dashboard/billing/fees/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bolt.com/
- group: other
  title: ''
  type: X
  url: https://x.com/bolt
- group: commercial
  title: ''
  type: Plans
  url: plans/bolt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bolt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bolt-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: https://help.bolt.com/developers/tools/api-keys/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.bolt.com/releases/
- group: operate
  title: ''
  type: Support
  url: https://support.bolt.com
- group: other
  title: ''
  type: MerchantDashboard
  url: https://merchant.bolt.com
created: '2026-06-13'
description: Bolt is a checkout experience platform that provides a REST API for one-click checkout, managing shopper accounts, processing payments, and accessing shopper network data across merchants. Bolt enables mid-market and enterprise eCommerce merchants to integrate optimized, frictionless checkout across platforms including Adobe Commerce, BigCommerce, Shopify, WooCommerce, and Salesforce Commerce Cloud. The Bolt Shopper Network allows returning shoppers to complete purchases with stored credentials across all Bolt-powered merchants.
examples:
- key_count: 4
  name: Accountaddpaymentmethod Request
  slug: accountAddPaymentMethod-request
- key_count: 4
  name: Accountaddresscreate Request
  slug: accountAddressCreate-request
- key_count: 4
  name: Accountaddressedit Request
  slug: accountAddressEdit-request
- key_count: 4
  name: Guestpaymentsinitialize Request
  slug: guestPaymentsInitialize-request
- key_count: 5
  name: Guestpaymentsinitialize Response 200
  slug: guestPaymentsInitialize-response-200
- key_count: 4
  name: Oauthgettoken Request
  slug: oauthGetToken-request
- key_count: 4
  name: Orderscreate Request
  slug: ordersCreate-request
- key_count: 5
  name: Orderscreate Response 200
  slug: ordersCreate-response-200
- key_count: 5
  name: Paymentsaction Response 200
  slug: paymentsAction-response-200
- key_count: 4
  name: Paymentsinitialize Request
  slug: paymentsInitialize-request
- key_count: 5
  name: Paymentsinitialize Response 200
  slug: paymentsInitialize-response-200
finops:
- name: Bolt Finops
  service_category: ''
  slug: bolt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bolt.png
json_schemas:
- name: account-test-creation-data
  property_count: 9
  slug: account-test-creation-data
- name: account-test-phone-data
  property_count: 1
  slug: account-test-phone-data
- name: account
  property_count: 3
  slug: account
- name: address-listing
  property_count: 13
  slug: address-listing
- name: Explicit Address Reference
  property_count: 13
  slug: address-reference-explicit
- name: Address ID Reference
  property_count: 2
  slug: address-reference-id
- name: Partial Address Reference
  property_count: 2
  slug: address-reference-partial
- name: address-reference
  property_count: 0
  slug: address-reference
- name: amount
  property_count: 2
  slug: amount
- name: authorization-code-request
  property_count: 6
  slug: authorization-code-request
- name: base-oauth-token-response
  property_count: 6
  slug: base-oauth-token-response
- name: cart-2
  property_count: 6
  slug: cart-2
- name: cart-discount
  property_count: 3
  slug: cart-discount
- name: cart-error
  property_count: 2
  slug: cart-error
- name: cart-item
  property_count: 9
  slug: cart-item
- name: cart-shipment
  property_count: 3
  slug: cart-shipment
- name: cart-updated-event-data
  property_count: 1
  slug: cart-updated-event-data
- name: cart
  property_count: 8
  slug: cart
- name: country-code
  property_count: 0
  slug: country-code
- name: create-full-account
  property_count: 2
  slug: create-full-account
- name: credit-card-error
  property_count: 2
  slug: credit-card-error
- name: credit-card-network
  property_count: 0
  slug: credit-card-network
- name: credit-card
  property_count: 7
  slug: credit-card
- name: error
  property_count: 2
  slug: error
- name: event
  property_count: 6
  slug: event
- name: events-request
  property_count: 0
  slug: events-request
- name: events-response
  property_count: 1
  slug: events-response
- name: failed-event
  property_count: 3
  slug: failed-event
- name: field-error
  property_count: 3
  slug: field-error
- name: get-access-token-response
  property_count: 0
  slug: get-access-token-response
- name: guest-payment-initialize-request
  property_count: 7
  slug: guest-payment-initialize-request
- name: item
  property_count: 7
  slug: item
- name: marketplace-commission-fee
  property_count: 3
  slug: marketplace-commission-fee
- name: order-response
  property_count: 2
  slug: order-response
- name: order
  property_count: 2
  slug: order
- name: page-view-event-data
  property_count: 2
  slug: page-view-event-data
- name: page-viewed-event-data
  property_count: 2
  slug: page-viewed-event-data
- name: payment-action-request
  property_count: 2
  slug: payment-action-request
- name: payment-completed-event-data
  property_count: 2
  slug: payment-completed-event-data
- name: payment-event-data
  property_count: 2
  slug: payment-event-data
- name: payment-incremental-authorization-request
  property_count: 5
  slug: payment-incremental-authorization-request
- name: payment-initialize-request
  property_count: 6
  slug: payment-initialize-request
- name: Affirm Payment Method
  property_count: 2
  slug: payment-method-affirm
- name: Afterpay Payment Method
  property_count: 2
  slug: payment-method-afterpay
- name: ApplePay Payment Method
  property_count: 0
  slug: payment-method-applepay
- name: Credit Card Payment Method
  property_count: 0
  slug: payment-method-credit-card
- name: payment-method-extended
  property_count: 0
  slug: payment-method-extended
- name: Googlepay Payment Method
  property_count: 0
  slug: payment-method-googlepay
- name: Klarna Account Payment Method
  property_count: 2
  slug: payment-method-klarna-account
- name: Klarna Pay Now Payment Method
  property_count: 2
  slug: payment-method-klarna-paynow
- name: Klarna Payment Method
  property_count: 2
  slug: payment-method-klarna
- name: PayPal Payment Method
  property_count: 3
  slug: payment-method-paypal
- name: Payment by reference Method
  property_count: 2
  slug: payment-method-reference
- name: payment-method
  property_count: 0
  slug: payment-method
- name: payment-response-finalized
  property_count: 4
  slug: payment-response-finalized
- name: payment-response-pending
  property_count: 5
  slug: payment-response-pending
- name: payment-response-three-ds-required
  property_count: 4
  slug: payment-response-three-ds-required
- name: payment-response
  property_count: 0
  slug: payment-response
- name: payment-update-request
  property_count: 2
  slug: payment-update-request
- name: processor-response
  property_count: 3
  slug: processor-response
- name: profile-creation-data
  property_count: 0
  slug: profile-creation-data
- name: profile
  property_count: 4
  slug: profile
- name: recognition-event-data
  property_count: 3
  slug: recognition-event-data
- name: refresh-token-request
  property_count: 6
  slug: refresh-token-request
- name: seller-info
  property_count: 1
  slug: seller-info
- name: seller-split-amounts
  property_count: 5
  slug: seller-split-amounts
- name: seller-split
  property_count: 3
  slug: seller-split
- name: shopper-recognized-event-data
  property_count: 3
  slug: shopper-recognized-event-data
- name: test-credit-card
  property_count: 5
  slug: test-credit-card
- name: three-ds-error
  property_count: 2
  slug: three-ds-error
- name: transaction-authorization
  property_count: 2
  slug: transaction-authorization
- name: transaction-capture
  property_count: 2
  slug: transaction-capture
- name: transaction-refund
  property_count: 1
  slug: transaction-refund
- name: transaction-void
  property_count: 1
  slug: transaction-void
- name: transaction
  property_count: 2
  slug: transaction
- name: update-cart-event-data
  property_count: 1
  slug: update-cart-event-data
jsonld:
- class_count: 0
  name: Bolt Api Context
  property_count: 0
  slug: bolt-api
layout: provider
modified: '2026-06-13'
name: Bolt
nav: Providers
network: true
overview: 'Bolt publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Callbacks API, OAuth API, and 3 more. Tagged areas include Checkout, Payments, eCommerce, One-Click Checkout, and Shopper Network.


  The Bolt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bolt''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, support, and 14 more developer resources.'
plans:
- name: Bolt Plans Pricing
  plan_count: 1
  slug: bolt-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 0
  name: Bolt Rate Limits
  slug: bolt-rate-limits
rules:
- name: Bolt API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bolt-jsonschema-spectral-rules
scopes:
- name: Bolt Scopes
  scope_count: 3
  slug: bolt-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  delta: -0.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 66.0
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bolt/refs/heads/main/screenshots/bolt-2026-06-20T173600.png
security:
- kind: authentication
  name: Bolt Authentication
  slug: bolt-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Bolt Domain Security
  slug: bolt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bolt Trust Center
  slug: bolt-trust-center
  summary_line: SOC 2, ISO 27001
slug: bolt
tags:
- Checkout
- Payments
- eCommerce
- One-Click Checkout
- Shopper Network
- Fraud Protection
website: https://www.bolt.com/
---
