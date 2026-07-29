---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The VNPAY-QR payment gateway (vpcpay) processes card, QR, ATM/bank-account and international-card payments via a browser redirect plus server-to-server IPN callback. Requests carry vnp_ parameters sig
  name: VNPAY Payment Gateway
  slug: vnpay-payment-gateway
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vnlife-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sandbox.vnpayment.vn/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://sandbox.vnpayment.vn/apis/docs/gioi-thieu/gioi-thieu.html
- group: docs
  title: ''
  type: APIReference
  url: https://sandbox.vnpayment.vn/apis/docs/thanh-toan-pay/pay.html
- group: company
  title: ''
  type: Website
  url: https://vnpay.vn
- group: operate
  title: ''
  type: Support
  url: https://vnpay.vn/lien-he
- group: company
  title: ''
  type: Blog
  url: https://vnpay.vn/tin-tuc
- group: start
  title: ''
  type: GettingStarted
  url: https://sandbox.vnpayment.vn/apis/docs/huong-dan-tich-hop/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vnlife-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vnlife-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vnlife-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vnlife-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vnlife-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/vnlife-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vnlife-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vnlife-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sandbox.vnpayment.vn/apis/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vnlife-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vnlife-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vnlife-llms.txt
created: '2026-07-17'
description: VNLIFE is the Vietnamese technology and financial-services holding group whose flagship business is VNPAY (Vietnam Payment Solution Joint Stock Company), the leading electronic-payment provider in Vietnam. VNLIFE operates a payments and lifestyle ecosystem spanning the VNPAY-QR payment gateway (integrated across 40+ banks and 15+ e-wallets), SmartPOS/PhonePOS acceptance hardware, the VNPAY super-app, VnShop e-commerce, taxi booking, e-invoicing, and B2B payment platforms serving 350,000+ merchants, 450,000+ acceptance points, and 60M+ users. The VNPAY payment gateway is exposed as a documented redirect/IPN HTTP API (VNPAY-QR / vpcpay) secured with HMAC-SHA512 checksums. VNLIFE is backed by investors including SoftBank Vision Fund and GIC.
image: https://vnpay.vn/assets/images/logo-vnpay-qr.png
layout: provider
mcp_servers:
- description: ''
  name: vnlife-mcp.yml
  slug: vnlife-mcpyml
modified: '2026-07-21'
name: VNLIFE
nav: Providers
network: true
overview: 'VNLIFE publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Payment Gateway, and QR Payments.


  VNLIFE''s developer surface includes documentation, API reference, support, engineering blog, getting-started guide, sandbox, authentication, and 13 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 27.3
  delta: -2.3
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 29.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Vnlife Authentication
  slug: vnlife-authentication
  summary_line: checksum-signature/merchant-credential · 2 schemes
- kind: domain-security
  name: Vnlife Domain Security
  slug: vnlife-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vnlife
tags:
- Company
- Fintech
- Payments
- Payment Gateway
- QR Payments
- E-Commerce
- Vietnam
- Financial Services
website: https://vnpay.vn
---
