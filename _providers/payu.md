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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Payu Agentic Access
  operation_count: 47
  slug: payu-agentic-access
  summary_line: 47 operations · 30 acting
api_count: 18
apis:
- description: REST API for payment processing in India. Supports hosted checkout, payment links, recurring payments, subscription management, save cards / vault, split settlements, wallet operations, cross-border p
  name: PayU India REST API
  slug: payu-india-rest-api
- description: REST API for payment processing across Latin America including Argentina, Brazil, Chile, Colombia, Mexico, and Peru. Supports payments, refunds, recurring charges, installment financing, and the Prici
  name: PayU Latam Payments API
  slug: payu-latam-payments-api
- description: Enterprise-grade payment orchestration API powered by PaymentsOS. Provides a single entry point for processing payments across multiple provider connections with dynamic routing. Supports charge, auth
  name: PayU Enterprise API (PaymentsOS)
  slug: payu-enterprise-api
- description: Authentication involves generating an OAuth token, which is used for further communication with PayU servers. To create a standard OAuth token, you will need <code>client_id</code> and <code>client_se
  name: PayU Authorize API
  slug: payu-authorize-api
- description: Retrieve available card installments options for specific card. For merchants operating on the Romanian market (Requires contact with a Payu representative first).
  name: PayU Card Installments API
  slug: payu-card-installments-api
- description: According to regulations in the European Union countries, payment service providers and parties providing currency conversion services at the point of sale are obliged to express the total currency co
  name: PayU FX-Reference API
  slug: payu-fx-reference-api
- description: In PayU, as a marketplace, you have the capability to manage various aspects of your submerchants.
  name: PayU Marketplace-Seller API
  slug: payu-marketplace-seller-api
- description: PayU is required by the Anti-Money Laundering Act to verify customers in this context. For this purpose, we provide a collection of endpoints to make it easier for you to verify sellers.
  name: PayU Marketplace-Verification API
  slug: payu-marketplace-verification-api
- description: We can convert your customers' payments to the currency of your shop set up with PayU.
  name: PayU MCP API
  slug: payu-mcp-api
- description: 'Order is the basic payment request for the standard integration with PayU. > If the response to the payment creation request is returned with an **HTTP 200** status and in HTML format, make sure that '
  name: PayU Order API
  slug: payu-order-api
- description: Below are the endpoints that enable you to create the necessary entities (Firm, Url, Shop, POS) for your partner.
  name: PayU Partner-Merchant-Registration API
  slug: payu-partner-merchant-registration-api
- description: Retrieving payment methods allows you to remove the threat of presenting a disabled payment method with white-label integration. It also gives you the ability to retrieve stored tokens and customer ca
  name: PayU Payment-Methods API
  slug: payu-payment-methods-api
- description: To widthraw funds from the PayU account you need to create a payout.
  name: PayU Payout API
  slug: payu-payout-api
- description: Payment Facilitator (PF) is an advanced form of partnership where PayU cedes much of its own responsibilities, like e.g. Know Your Customer (KYC) and verification, customer support and settlement (pay
  name: PayU PF-Submerchant-Registration API
  slug: payu-pf-submerchant-registration-api
- description: The PayU system fully supports refunds for the processed payments, the balance of which is transferred directly to the buyer's account.
  name: PayU Refund API
  slug: payu-refund-api
- description: Shop is the main entity in the management panel. It is the place where you can manage incoming transactions processed by PayU.
  name: PayU Shop API
  slug: payu-shop-api
- description: Statements in PayU are comprehensive reports that provide a detailed summary of completed purchase transactions, refunds, and payouts.
  name: PayU Statements API
  slug: payu-statements-api
- description: With tokenization, we are confident that your customers' card data is protected from third parties.
  name: PayU Token API
  slug: payu-token-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payu-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/payu-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/payu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payu-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://corporate.payu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://corporate.payu.com/developer-documentation/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/PayU
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/payu/
- group: company
  title: ''
  type: Blog
  url: https://corporate.payu.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://corporate.payu.com/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paymentsos.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/PayUindia
- group: commercial
  title: ''
  type: Plans
  url: plans/payu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/payu-finops.yml
created: '2026-06-13'
description: PayU is a global payment platform operating in 50+ emerging markets across Central & Eastern Europe, Latin America, the Middle East, and Africa. It provides REST APIs for payment processing, order management, refunds, payouts, subscriptions, fraud detection, checkout optimization, marketplace operations, tokenization, and financial services. PayU processes 4 million transactions daily for 450,000+ merchants through 450+ local payment methods.
finops:
- name: Payu Finops
  service_category: ''
  slug: payu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payu.png
json_schemas:
- name: PayU GPO Europe REST API - JSON Schemas
  property_count: 0
  slug: payu-europe-rest-api
jsonld:
- class_count: 0
  name: Payu Europe Rest Api Context
  property_count: 0
  slug: payu-europe-rest-api
layout: provider
modified: '2026-06-13'
name: PayU
nav: Providers
network: true
overview: 'PayU publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Authorize API, Card Installments API, FX-Reference API, and 12 more. Tagged areas include Payments, Payment Processing, Fintech, Financial Services, and Subscriptions.


  The PayU catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PayU''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Payu Plans Pricing
  plan_count: 3
  slug: payu-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 0
  name: Payu Rate Limits
  slug: payu-rate-limits
rules:
- name: PayU API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: payu-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.2
  delta: -6.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 68.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Payu Authentication
  slug: payu-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Payu Domain Security
  slug: payu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Payu Vulnerability Disclosure
  slug: payu-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Payu Trust Center
  slug: payu-trust-center
  summary_line: PCI DSS
slug: payu
tags:
- Payments
- Payment Processing
- Fintech
- Financial Services
- Subscriptions
- Fraud Detection
- Checkout
- Marketplace
- Tokenization
- Emerging Markets
website: https://corporate.payu.com/
---
