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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Tamara Agentic Access
  operation_count: 23
  slug: tamara-agentic-access
  summary_line: 23 operations · 17 acting
api_count: 11
apis:
- description: Authorize, capture, cancel, retrieve, and update orders created via Tamara checkout sessions. Mirrors the online checkout lifecycle (new → approved → authorised → captured → refunded) and is the merch
  name: Tamara Orders API
  slug: tamara-orders-api
- description: Generate Tamara checkout sessions for brick-and-mortar stores through SMS payment links or QR codes that customers scan with the Tamara consumer app to complete the BNPL purchase in-aisle. Includes th
  name: Tamara In-Store Checkout API
  slug: tamara-in-store-checkout-api
- description: Register and manage HTTPS webhook endpoints that receive order and dispute lifecycle events from Tamara (order_approved, order_authorised, order_captured, order_refunded, order_canceled, order_expired
  name: Tamara Webhooks API
  slug: tamara-webhooks-api
- description: Query, filter, and update merchant disputes raised against Tamara orders. Supports listing disputes by order id, dispute id, order status, or dispute status; and appending comments and proof attachmen
  name: Tamara Disputes API
  slug: tamara-disputes-api
- description: Check whether Tamara considers a customer eligible for a BNPL purchase before exposing Tamara as a payment method on the merchant's checkout page. The endpoint accepts an order amount/currency and a c
  name: Tamara Pre-Checkout Eligibility API
  slug: tamara-eligibility-api
- description: The Captures API from Tamara — 1 operation(s) for captures.
  name: Tamara Captures API
  slug: tamara-captures-api
- description: The Channel Partner Webhooks API from Tamara — 2 operation(s) for channel partner webhooks.
  name: Tamara Channel Partner Webhooks API
  slug: tamara-channel-partner-webhooks-api
- description: Create and manage hosted-checkout sessions.
  name: Tamara Checkout Sessions API
  slug: tamara-checkout-sessions-api
- description: The Merchant API Keys API from Tamara — 1 operation(s) for merchant api keys.
  name: Tamara Merchant API Keys API
  slug: tamara-merchant-api-keys-api
- description: The Merchant Onboarding API from Tamara — 2 operation(s) for merchant onboarding.
  name: Tamara Merchant Onboarding API
  slug: tamara-merchant-onboarding-api
- description: The Refunds API from Tamara — 2 operation(s) for refunds.
  name: Tamara Refunds API
  slug: tamara-refunds-api
arazzos:
- description: Inspect an order, authorise it when approved, then capture funds on fulfilment.
  name: Tamara Authorise and Capture Order
  slug: tamara-authorise-and-capture-order-workflow
- description: Run the full post-checkout money lifecycle — authorise, capture, then refund.
  name: Tamara Authorise, Capture and Refund Order
  slug: tamara-authorise-capture-refund-order-workflow
- description: Capture an authorised order, then refund against the returned capture id.
  name: Tamara Capture and Legacy Refund
  slug: tamara-capture-and-legacy-refund-workflow
- description: Capture funds against an authorised order, then issue a simplified refund.
  name: Tamara Capture and Refund Order
  slug: tamara-capture-and-refund-order-workflow
- description: Create a checkout session, poll the resulting order, and authorise it once approved.
  name: Tamara Create and Authorise Order
  slug: tamara-create-and-authorise-order-workflow
- description: Check pre-checkout eligibility, then create a checkout session only when eligible.
  name: Tamara Eligibility-Gated Checkout
  slug: tamara-eligibility-gated-checkout-workflow
- description: Create a checkout session, confirm approval, authorise, and capture in one flow.
  name: Tamara Full BNPL Lifecycle
  slug: tamara-full-bnpl-lifecycle-workflow
- description: Read an order's status and cancel it only when it is still cancellable.
  name: Tamara Order Status Cancel
  slug: tamara-order-status-cancel-workflow
- description: Read an order's status and refund it only when funds have been captured.
  name: Tamara Order Status Refund
  slug: tamara-order-status-refund-workflow
artifact_total: 57
collections:
- collection_type: postman
  name: Tamara Channel Partners API
  slug: postman-tamara-channel-partners-api
- collection_type: postman
  name: Tamara Checkout API
  slug: postman-tamara-checkout-api
- collection_type: postman
  name: Tamara Disputes API
  slug: postman-tamara-disputes-api
- collection_type: postman
  name: Tamara Pre-Checkout Eligibility API
  slug: postman-tamara-eligibility-api
- collection_type: postman
  name: Tamara In-Store Checkout API
  slug: postman-tamara-in-store-checkout-api
- collection_type: postman
  name: Tamara Orders API
  slug: postman-tamara-orders-api
- collection_type: postman
  name: Tamara Payments API
  slug: postman-tamara-payments-api
- collection_type: postman
  name: Tamara Webhooks API
  slug: postman-tamara-webhooks-api
- collection_type: open
  name: Tamara Channel Partners API
  slug: open-tamara-channel-partners-api
- collection_type: open
  name: Tamara Checkout API
  slug: open-tamara-checkout-api
- collection_type: open
  name: Tamara Disputes API
  slug: open-tamara-disputes-api
- collection_type: open
  name: Tamara Pre-Checkout Eligibility API
  slug: open-tamara-eligibility-api
- collection_type: open
  name: Tamara In-Store Checkout API
  slug: open-tamara-in-store-checkout-api
- collection_type: open
  name: Tamara Orders API
  slug: open-tamara-orders-api
- collection_type: open
  name: Tamara Payments API
  slug: open-tamara-payments-api
- collection_type: open
  name: Tamara Webhooks API
  slug: open-tamara-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tamara-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tamara-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tamara-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tamara/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-authorise-and-capture-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-authorise-capture-refund-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-capture-and-legacy-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-capture-and-refund-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-create-and-authorise-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-eligibility-gated-checkout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-full-bnpl-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-order-status-cancel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tamara-order-status-refund-workflow.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tamara.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tamara.co/reference/tamara-api-reference-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tamara.co/docs/direct-quick-start-guide
- group: operate
  title: ''
  type: Status
  url: https://status.tamara.co/
- group: operate
  title: ''
  type: Support
  url: https://docs.tamara.co/
- group: start
  title: ''
  type: Signup
  url: https://partners.tamara.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tamara.co/en-SA/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tamara.co/en-SA/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://tamara.co/en-SA/business
- group: company
  title: ''
  type: Blog
  url: https://tamara.co/en-SA/blog
- group: operate
  title: ''
  type: ContactForm
  url: https://tamara.co/en-SA/contact-us
- group: build
  title: ''
  type: Github
  url: https://github.com/Tamara-Technology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tamara-co
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TamaraTech
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/tamara/
- group: commercial
  title: ''
  type: Plans
  url: plans/tamara-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tamara-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tamara-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tamara-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tamara-vocabulary.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tamara-Technology/php-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tamara-Technology/dotnet-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tamara-Technology/ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tamara-Technology/android-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tamara-Technology/flutter-sdk-example
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tamara-Technology/react-sdk-example
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Tamara-Technology/magento
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Tamara-Technology/wp-plugin-tamara-checkout
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Tamara-Technology/opencart
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Tamara-Technology/prestashop
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Tamara-Technology/salesforce
- group: build
  title: ''
  type: Plugin
  url: https://tamara.co/en-sa/plugins/shopify
created: '2026-05-24'
description: Tamara is the Saudi Arabia–headquartered MENA shopping and Buy-Now-Pay-Later platform offering Shariah-compliant split-payment and Pay-Now solutions across Saudi Arabia, the United Arab Emirates, Kuwait, Bahrain, and Oman. Founded in 2020 and licensed by SAMA (Saudi Central Bank), Tamara provides merchants with a hosted-checkout Direct API, in-store SMS and QR payment links, mobile SDKs for iOS, Android, Flutter, and React Native, plug-and-play e-commerce extensions for Shopify, Magento, OpenCart, PrestaShop, Salesforce Commerce Cloud and WooCommerce, webhooks for order and dispute lifecycle events, and a Channel Partners onboarding API for payment service providers and platforms that white-label Tamara. The company became the first homegrown Saudi fintech unicorn in December 2023 after raising a US$340M Series C led by SNB Capital and Sanabil Investments and is backed by debt facilities from Goldman Sachs, Citi, and Apollo for its Shariah-compliant funding base.
examples:
- key_count: 2
  name: Tamara Authorise Order Example
  slug: tamara-authorise-order-example
- key_count: 2
  name: Tamara Capture Order Example
  slug: tamara-capture-order-example
- key_count: 2
  name: Tamara Create Checkout Session Example
  slug: tamara-create-checkout-session-example
- key_count: 2
  name: Tamara Pre Checkout Eligibility Example
  slug: tamara-pre-checkout-eligibility-example
- key_count: 2
  name: Tamara Register Webhook Example
  slug: tamara-register-webhook-example
- key_count: 2
  name: Tamara Simplified Refund Example
  slug: tamara-simplified-refund-example
finops:
- name: Tamara Finops
  service_category: Payments
  slug: tamara-finops
image: https://tamara.co/favicon.ico
json_schemas:
- name: TamaraCapture
  property_count: 6
  slug: tamara-capture
- name: TamaraCheckoutSession
  property_count: 4
  slug: tamara-checkout-session
- name: TamaraDispute
  property_count: 9
  slug: tamara-dispute
- name: TamaraOrder
  property_count: 14
  slug: tamara-order
- name: TamaraRefund
  property_count: 8
  slug: tamara-refund
json_structures:
- name: Tamara Order Structure
  property_count: 8
  slug: tamara-order-structure
jsonld:
- class_count: 0
  name: Tamara Context
  property_count: 7
  slug: tamara-context
layout: provider
modified: '2026-05-24'
name: Tamara
nav: Providers
network: true
overview: 'Tamara publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Orders API, In-Store Checkout API, Webhooks API, and 8 more. Tagged areas include BNPL, Buy Now Pay Later, Fintech, Payments, and Checkout.


  The Tamara catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tamara''s developer surface includes authentication, documentation, API reference, getting-started guide, status page, support, signup flow, and 38 more developer resources.'
plans:
- name: Tamara Plans Pricing
  plan_count: 2
  slug: tamara-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 3
  name: Tamara Rate Limits
  slug: tamara-rate-limits
rules:
- name: Tamara API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tamara-jsonschema-spectral-rules
- name: Tamara API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: tamara-rules
score:
  band: strong
  composite: 58.4
  delta: -6.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.4
    developer_ergonomics: 63.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tamara/refs/heads/main/screenshots/tamara-2026-06-20T194914.png
security:
- kind: authentication
  name: Tamara Authentication
  slug: tamara-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tamara Domain Security
  slug: tamara-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tamara
tags:
- BNPL
- Buy Now Pay Later
- Fintech
- Payments
- Checkout
- Shariah Compliant
- MENA
- Saudi Arabia
- UAE
- Installments
- Pay Later
- Merchant Services
- Orders
- Refunds
- Captures
- Webhooks
- Disputes
- Channel Partners
- E-commerce
- POS
---
