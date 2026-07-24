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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Sezzle Agentic Access
  operation_count: 27
  slug: sezzle-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 8
apis:
- description: The legacy Sezzle v1 API for merchants. Supports checkout creation and order completion via redirect-based flow. Deprecated in favor of v2; existing integrations are encouraged to migrate to v2.
  name: Sezzle API v1
  slug: sezzle-api-v1
- description: The Bearer Authentication API from Sezzle — 1 operation(s) for bearer authentication.
  name: Sezzle Bearer Authentication API
  slug: sezzle-bearer-authentication-api
- description: The Customer API from Sezzle — 4 operation(s) for customer.
  name: Sezzle Customer API
  slug: sezzle-customer-api
- description: The Order API from Sezzle — 7 operation(s) for order.
  name: Sezzle Order API
  slug: sezzle-order-api
- description: The Reports API from Sezzle — 4 operation(s) for reports.
  name: Sezzle Reports API
  slug: sezzle-reports-api
- description: The Session API from Sezzle — 2 operation(s) for session.
  name: Sezzle Session API
  slug: sezzle-session-api
- description: The Token API from Sezzle — 2 operation(s) for token.
  name: Sezzle Token API
  slug: sezzle-token-api
- description: The Webhooks API from Sezzle — 3 operation(s) for webhooks.
  name: Sezzle Webhooks API
  slug: sezzle-webhooks-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sezzle-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sezzle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sezzle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sezzle-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.sezzle.com/
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.sezzle.com/merchant
- group: operate
  title: ''
  type: MerchantSupport
  url: https://merchant-help.sezzle.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sezzle
- group: build
  title: ''
  type: SDKNode
  url: https://github.com/sezzle/sezzle-node
- group: build
  title: ''
  type: SDKAndroid
  url: https://github.com/sezzle/sezzle-merchant-sdk-android
- group: build
  title: ''
  type: SDKiOS
  url: https://github.com/sezzle/sezzle-merchant-sdk-ios
- group: build
  title: ''
  type: IntegrationMagento2
  url: https://github.com/sezzle/sezzle-magento2
- group: build
  title: ''
  type: IntegrationWooCommerce
  url: https://docs.sezzle.com/
- group: build
  title: ''
  type: IntegrationShopify
  url: https://apps.shopify.com/sezzle-payments
- group: commercial
  title: ''
  type: Pricing
  url: https://sezzle.com/pricing
- group: commercial
  title: ''
  type: Terms
  url: https://sezzle.com/terms-of-service
- group: commercial
  title: ''
  type: Privacy
  url: https://sezzle.com/privacy-policy
created: '2026-06-13'
description: Sezzle is a buy-now-pay-later platform that enables merchants to offer installment payment options at checkout. Its REST APIs support merchant checkout integration, order management, shopper authentication, customer tokenization, and payment installment processing — allowing shoppers to split purchases into four interest-free payments over six weeks.
examples:
- key_count: 2
  name: Authentication Request
  slug: authentication-request
- key_count: 3
  name: Authentication Response
  slug: authentication-response
- key_count: 1
  name: Capture Request
  slug: capture-request
- key_count: 2
  name: Refund Request
  slug: refund-request
- key_count: 4
  name: Session Request
  slug: session-request
- key_count: 4
  name: Session Response
  slug: session-response
- key_count: 2
  name: Webhook Create Request
  slug: webhook-create-request
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sezzle.png
json_schemas:
- name: Address
  property_count: 8
  slug: address
- name: Customer
  property_count: 8
  slug: customer
- name: Discount
  property_count: 2
  slug: discount
- name: LineItem
  property_count: 4
  slug: line-item
- name: Order
  property_count: 9
  slug: order
- name: Payout
  property_count: 0
  slug: payout
- name: Price
  property_count: 2
  slug: price
- name: Webhook
  property_count: 2
  slug: webhook
jsonld:
- class_count: 12
  name: Sezzle Context
  property_count: 60
  slug: sezzle-context
layout: provider
modified: '2026-06-13'
name: Sezzle
nav: Providers
network: true
overview: 'Sezzle publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bearer Authentication API, Customer API, Order API, and 4 more. Tagged areas include Buy Now Pay Later, BNPL, Payments, Installments, and Fintech.


  The Sezzle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sezzle''s developer surface includes authentication, developer portal, GitHub presence, pricing, terms of service, privacy policy, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Sezzle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sezzle-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.7
  delta: 1.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.7
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 48.1
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sezzle/refs/heads/main/screenshots/sezzle-2026-06-20T193742.png
security:
- kind: authentication
  name: Sezzle Authentication
  slug: sezzle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sezzle Domain Security
  slug: sezzle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sezzle Vulnerability Disclosure
  slug: sezzle-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sezzle
tags:
- Buy Now Pay Later
- BNPL
- Payments
- Installments
- Fintech
- Merchant Integration
- Checkout
website: https://docs.sezzle.com/
---
