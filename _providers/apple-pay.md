---
access_model:
  confidence: high
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Apple Pay Agentic Access
  operation_count: 6
  slug: apple-pay-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 5
apis:
- description: Native iOS, watchOS, and macOS framework for integrating Apple Pay into mobile and desktop applications. Provides PKPaymentRequest and PKPaymentAuthorizationViewController for in-app Apple Pay checkou
  name: PassKit Framework (Apple Pay)
  slug: passkit-framework-apple-pay
- description: Register and manage merchant domains for Apple Pay on the Web
  name: Apple Pay Merchant Registration API
  slug: apple-pay-merchant-registration-api
- description: Validate merchant identity and obtain payment sessions
  name: Apple Pay Merchant Validation API
  slug: apple-pay-merchant-validation-api
- description: Endpoints for receiving and processing Apple Pay payment tokens
  name: Apple Pay Payment Processing API
  slug: apple-pay-payment-processing-api
- description: Endpoints for checking payment transaction status
  name: Apple Pay Payment Status API
  slug: apple-pay-payment-status-api
artifact_total: 46
collections:
- collection_type: postman
  name: Apple Pay JS Merchant Registration API
  slug: postman-apple-pay-merchant-registration-api
- collection_type: postman
  name: Apple Pay JS Merchant Registration Merchant Validation API
  slug: postman-apple-pay-merchant-validation-api
- collection_type: postman
  name: Apple Pay JS Merchant Registration Payment Processing API
  slug: postman-apple-pay-payment-processing-api
- collection_type: postman
  name: Apple Pay JS Merchant Registration Payment Status API
  slug: postman-apple-pay-payment-status-api
- collection_type: open
  name: Apple Pay JS API
  slug: open-apple-pay-js
- collection_type: open
  name: Apple Pay Payment Token API
  slug: open-apple-pay-payment-token
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apple-pay/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apple-pay-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apple-pay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apple-pay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apple-pay-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.apple.com/account/
- group: operate
  title: ''
  type: Support
  url: https://developer.apple.com/support/apple-pay/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.apple.com/apple-pay/acceptable-use-guidelines/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.apple.com/apple-pay/get-started/
- group: other
  title: ''
  type: Branding
  url: https://developer.apple.com/apple-pay/marketing/
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.apple.com/system-status/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apple-pay-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/apple-pay-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apple-pay-vocabulary.yaml
created: '2024-01-01'
description: Apple Pay enables secure, frictionless payments in apps and on the web using the payment cards stored in users' Apple Wallet. It supports Touch ID, Face ID, and Apple Watch authentication for both in-person and online payments. Apple Pay is available on iOS, watchOS, macOS, and via Safari on the web through the Apple Pay JS API, with a PassKit native framework for iOS/watchOS app integration.
examples:
- key_count: 6
  name: Apple Pay Payment Request Example
  slug: apple-pay-payment-request-example
- key_count: 4
  name: Apple Pay Payment Token Example
  slug: apple-pay-payment-token-example
features:
- description: Users authorize payments using biometric authentication on Apple devices
  name: Touch ID and Face ID Authentication
- description: Native iOS and watchOS integration via PassKit framework
  name: In-App Payments
- description: Safari-based Apple Pay checkout via the ApplePaySession JavaScript API
  name: Web Payments
- description: Contactless payments from Apple Watch without needing iPhone
  name: Apple Watch Support
- description: Supports Visa, Mastercard, Amex, Discover, JCB, UnionPay, and more
  name: Multiple Card Networks
- description: Domain verification ensures only registered merchants can use Apple Pay
  name: Merchant Domain Verification
- description: Subscription and automatic payment support via automatic payment requests
  name: Recurring Payments
- description: Support for deferred billing like hotel deposits and pre-orders
  name: Deferred Payments
finops:
- name: Apple Pay Finops
  service_category: Payments / Digital Wallet
  slug: apple-pay-finops
image: https://developer.apple.com/assets/elements/icons/apple-pay/apple-pay-96x96.png
integrations:
- description: Stripe Elements and Stripe.js support Apple Pay via the Payment Request Button
  name: Stripe
- description: PayPal's Braintree SDK provides Apple Pay integration for iOS and web
  name: Braintree
- description: Square's iOS SDK supports Apple Pay for in-app and contactless payments
  name: Square
- description: Adyen payment platform supports Apple Pay for web and mobile checkout
  name: Adyen
- description: Shopify natively supports Apple Pay for accelerated checkout
  name: Shopify
- description: WooCommerce Stripe plugin enables Apple Pay on WordPress stores
  name: WooCommerce
json_schemas:
- name: Apple Pay Payment Request
  property_count: 16
  slug: apple-pay-payment-request
- name: Apple Pay Payment Token
  property_count: 3
  slug: apple-pay-payment-token
json_structures:
- name: Apple Pay Payment Request Structure
  property_count: 16
  slug: apple-pay-payment-request-structure
- name: Apple Pay Payment Token Structure
  property_count: 3
  slug: apple-pay-payment-token-structure
jsonld:
- class_count: 0
  name: Apple Pay Context
  property_count: 10
  slug: apple-pay-context
layout: provider
modified: '2026-05-19'
name: Apple Pay
nav: Providers
network: true
overview: 'Apple Pay publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Merchant Registration API, Merchant Validation API, Payment Processing API, and 1 more. Tagged areas include Apple, Contactless Payments, Digital Wallet, E-Commerce, and Mobile Payments.


  The Apple Pay catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apple Pay''s developer surface includes authentication, developer portal, support, getting-started guide, and 10 more developer resources.'
plans:
- name: Apple Pay Plans Pricing
  plan_count: 2
  slug: apple-pay-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Apple Pay Rate Limits
  slug: apple-pay-rate-limits
rules:
- name: Apple Pay API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: apple-pay-jsonschema-spectral-rules
- name: Apple Pay API Rules
  rule_count: 29
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 16
  slug: apple-pay-spectral-rules
score:
  band: developing
  composite: 55.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 79.1
    developer_ergonomics: 39.1
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 47.4
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apple-pay/refs/heads/main/screenshots/apple-pay-2026-06-20T172320.png
security:
- kind: authentication
  name: Apple Pay Authentication
  slug: apple-pay-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Apple Pay Domain Security
  slug: apple-pay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apple Pay Vulnerability Disclosure
  slug: apple-pay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apple-pay
tags:
- Apple
- Contactless Payments
- Digital Wallet
- E-Commerce
- Mobile Payments
- Payments
use_cases:
- description: One-tap checkout on web and mobile using saved payment cards
  name: E-Commerce Checkout
- description: Native iOS app purchases with Face ID or Touch ID authentication
  name: In-App Purchases
- description: Setting up recurring subscription payments authorized by the user
  name: Subscription Billing
- description: Tap-to-pay at point-of-sale terminals using iPhone or Apple Watch
  name: Contactless In-Store Payments
- description: Paying for transit and transportation with Express Mode
  name: Transit Payments
website: https://developer.apple.com/account/
---
