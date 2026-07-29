---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - finops
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
- acting_count: 7
  human_in_the_loop: 0
  name: Cellulant Agentic Access
  operation_count: 8
  slug: cellulant-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 6
apis:
- description: Acknowledge successful or partial payments back to the platform.
  name: Cellulant Acknowledgement API
  slug: cellulant-acknowledgement-api
- description: OAuth 2.0 access token issuance for Tingg API calls.
  name: Cellulant Authentication API
  slug: cellulant-authentication-api
- description: Host-to-host checkout flow for merchant-controlled UX.
  name: Cellulant Custom Checkout API
  slug: cellulant-custom-checkout-api
- description: Outbound SMS notifications and OTPs.
  name: Cellulant Engagement API
  slug: cellulant-engagement-api
- description: Create hosted checkout sessions returning short and long URLs.
  name: Cellulant Express Checkout API
  slug: cellulant-express-checkout-api
- description: Post payouts, queries, validations, balances, and refunds.
  name: Cellulant Payments API
  slug: cellulant-payments-api
arazzos:
- description: Initiate a custom checkout, send the customer an OTP by SMS, then push the charge request.
  name: Cellulant Charge with OTP Notification
  slug: cellulant-charge-with-otp-notification-workflow
- description: Read the float balance, then disburse a payout only when the platform authenticated the balance query.
  name: Cellulant Check Balance and Payout
  slug: cellulant-check-balance-and-payout-workflow
- description: Raise an Express Checkout, poll status until paid, then acknowledge delivery back to the platform.
  name: Cellulant Checkout, Poll, and Acknowledge
  slug: cellulant-checkout-poll-and-acknowledge-workflow
- description: Create an Express Checkout, then text the customer the short payment URL over Tingg Engage.
  name: Cellulant Checkout with SMS Notification
  slug: cellulant-checkout-with-sms-notification-workflow
- description: Host-to-host flow — authenticate, initiate a custom checkout, push the charge prompt, then poll until the payment resolves.
  name: Cellulant Custom Checkout, Charge, and Poll
  slug: cellulant-custom-checkout-charge-and-poll-workflow
- description: Authenticate, raise a Tingg Express Checkout, then poll the request status until the payment settles.
  name: Cellulant Express Checkout and Poll Status
  slug: cellulant-express-checkout-and-poll-status-workflow
- description: Fetch the outstanding bill for an account, then settle it with a Beep payout.
  name: Cellulant Get Bill and Pay
  slug: cellulant-get-bill-and-pay-workflow
- description: Disburse a payout, query its outcome, and reverse it with a refund when the payout did not succeed.
  name: Cellulant Payout, Query, and Refund
  slug: cellulant-payout-query-and-refund-workflow
- description: Disburse a payout, then poll the Beep platform with queryPayment until the payout reaches a terminal state.
  name: Cellulant Post Payout and Query Status
  slug: cellulant-post-payout-and-query-status-workflow
- description: Validate the destination account, then post a mobile money or bank payout through the Beep platform.
  name: Cellulant Validate and Post Payout
  slug: cellulant-validate-and-post-payout-workflow
artifact_total: 35
collections:
- collection_type: postman
  name: Cellulant Tingg Checkout API
  slug: postman-cellulant-checkout-api
- collection_type: postman
  name: Cellulant Tingg Engage API
  slug: postman-cellulant-engage-api
- collection_type: postman
  name: Cellulant Tingg Payouts API
  slug: postman-cellulant-payouts-api
- collection_type: open
  name: Cellulant Tingg Checkout API
  slug: open-cellulant-checkout-api
- collection_type: open
  name: Cellulant Tingg Engage API
  slug: open-cellulant-engage-api
- collection_type: open
  name: Cellulant Tingg Payouts API
  slug: open-cellulant-payouts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cellulant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cellulant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cellulant-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cellulant/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-charge-with-otp-notification-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-check-balance-and-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-checkout-poll-and-acknowledge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-checkout-with-sms-notification-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-custom-checkout-charge-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-express-checkout-and-poll-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-get-bill-and-pay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-payout-query-and-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-post-payout-and-query-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cellulant-validate-and-post-payout-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.cellulant.io
- group: other
  title: ''
  type: Product
  url: https://tingg.africa
- group: start
  title: ''
  type: Portal
  url: https://developer.tingg.africa
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tingg.africa
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tingg.africa/docs/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tingg.africa/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tingg.africa/docs/checkout-v3-getting-started
- group: start
  title: ''
  type: Sandbox
  url: https://app.sandbox.tingg.africa
- group: start
  title: ''
  type: Signup
  url: https://app.sandbox.tingg.africa
- group: commercial
  title: ''
  type: Pricing
  url: https://tingg.africa/pricing/
- group: other
  title: ''
  type: Checkout
  url: https://tingg.africa/checkout/
- group: other
  title: ''
  type: Payouts
  url: https://tingg.africa/payouts/
- group: other
  title: ''
  type: PaymentGateway
  url: https://tingg.africa/payment-gateway/
- group: other
  title: ''
  type: PaymentPages
  url: https://tingg.africa/payment-pages/
- group: other
  title: ''
  type: PaymentInfrastructure
  url: https://www.cellulant.io/business-offerings/payment-infrastructure/
- group: company
  title: ''
  type: Blog
  url: https://www.cellulant.io/category/blog/
- group: company
  title: ''
  type: Blog
  url: https://tingg.africa/blog/
- group: company
  title: ''
  type: Press
  url: https://www.cellulant.io/category/press-release/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CellulantCorp
- group: build
  title: ''
  type: SDKs
  url: https://packagist.org/packages/tingg/checkout
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/Tingg/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tingg-sdk/checkout
- group: build
  title: ''
  type: SDKs
  url: https://www.nuget.org/packages/Tingg.Checkout.Net
- group: build
  title: ''
  type: SDKs
  url: https://cdn.cellulant.africa/js/tingg-checkout-library.js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CellulantCorp/Express-Checkout-PHP-Client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CellulantCorp/express-checkout-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CellulantCorp/express-checkout-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CellulantCorp/express-checkout-c-sharp
- group: build
  title: ''
  type: Plugin
  url: https://github.com/CellulantCorp/cellulant-tingg-payment-gateway
- group: build
  title: ''
  type: Plugin
  url: https://wordpress.org/plugins/cellulant-tingg-checkout/
- group: build
  title: ''
  type: Plugin
  url: https://github.com/CellulantCorp/mula-wordpress-plugin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cellulant-corporation
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cellulant
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@CellulantCorp
- group: company
  title: ''
  type: Careers
  url: https://www.cellulant.io/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.cellulant.io/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cellulant.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cellulant.io/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/cellulant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cellulant-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cellulant-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cellulant-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/cellulant-rules.yml
created: '2026-05-24'
description: 'Cellulant is a pan-African payments platform headquartered in Nairobi, Kenya, operating across 35 African countries. Its flagship product Tingg is a single API that lets businesses collect online and offline payments, disburse to mobile money wallets and bank accounts, vend airtime and data, pay bills, and engage customers by SMS — interoperably across 350+ banks, mobile network operators, and card networks. Cellulant processes more than 4.5 million transactions per day for over 2,000 enterprise merchants and powers payments for ~220 million consumers. The Tingg platform exposes three primary developer-facing surfaces: Tingg Checkout 3.0 (Express, Custom and Direct Card), Tingg Payouts (the Beep global JSON endpoint), and Tingg Engage (transactional SMS). Cellulant ships official SDKs for PHP, Python, Node.js, .NET, JavaScript, plus a WooCommerce plugin.'
examples:
- key_count: 2
  name: Cellulant Create Express Checkout Example
  slug: cellulant-create-express-checkout-example
- key_count: 2
  name: Cellulant Post Payment Example
  slug: cellulant-post-payment-example
- key_count: 2
  name: Cellulant Send Engagement Example
  slug: cellulant-send-engagement-example
finops:
- name: Cellulant Finops
  service_category: Financial Services — Payments
  slug: cellulant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cellulant.png
json_schemas:
- name: Tingg Express Checkout Request
  property_count: 17
  slug: cellulant-checkout-request
- name: Tingg Payout Packet
  property_count: 14
  slug: cellulant-payout-packet
jsonld:
- class_count: 0
  name: Cellulant Context
  property_count: 4
  slug: cellulant-context
layout: provider
modified: '2026-05-24'
name: Cellulant
nav: Providers
network: true
overview: 'Cellulant publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Acknowledgement API, Authentication API, Custom Checkout API, and 3 more. Tagged areas include Payments, Mobile Money, Checkout, Payouts, and Disbursement.


  The Cellulant catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cellulant''s developer surface includes authentication, developer portal, documentation, getting-started guide, sandbox, signup flow, pricing, and 50 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 4
  name: Cellulant Rate Limits
  slug: cellulant-rate-limits
rules:
- name: Cellulant API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cellulant-jsonschema-spectral-rules
- name: Cellulant API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 4
  slug: cellulant-rules
score:
  band: strong
  composite: 57.1
  delta: -5.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 77.4
    developer_ergonomics: 67.4
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 63.0
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
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cellulant/refs/heads/main/screenshots/cellulant-2026-06-20T174113.png
security:
- kind: authentication
  name: Cellulant Authentication
  slug: cellulant-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Cellulant Domain Security
  slug: cellulant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cellulant
tags:
- Payments
- Mobile Money
- Checkout
- Payouts
- Disbursement
- Africa
- Pan-African
- Fintech
- Bank Transfer
- Cards
- Airtime
- Bill Payment
- SMS
- OTP
- Tingg
website: https://www.cellulant.io
---
