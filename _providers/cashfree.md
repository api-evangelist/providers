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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Cashfree Agentic Access
  operation_count: 40
  slug: cashfree-agentic-access
  summary_line: 40 operations · 22 acting · 1 human-in-the-loop
api_count: 23
apis:
- description: API for creating and managing recurring payment mandates using UPI AutoPay and eNACH, including subscription plans, customer mandates, and automated billing cycles.
  name: Cashfree Subscriptions API
  slug: subscriptions
- description: API for marketplace and SaaS platform operators to onboard sub-merchants, split payments, manage settlements to multiple vendors, and operate escrow arrangements.
  name: Cashfree Platforms API
  slug: platforms
- description: The Authorize API from Cashfree Payments — 1 operation(s) for authorize.
  name: Cashfree Payments Authorize API
  slug: cashfree-authorize-api
- description: The Beneficiary v2 API from Cashfree Payments — 1 operation(s) for beneficiary v2.
  name: Cashfree Payments Beneficiary v2 API
  slug: cashfree-beneficiary-v2-api
- description: The CreateCashgram API from Cashfree Payments — 1 operation(s) for createcashgram.
  name: Cashfree Payments CreateCashgram API
  slug: cashfree-createcashgram-api
- description: The Deactivate Static KYC Link API from Cashfree Payments — 1 operation(s) for deactivate static kyc link.
  name: Cashfree Payments Deactivate Static KYC Link API
  slug: cashfree-deactivate-static-kyc-link-api
- description: The DeactivateCashgram API from Cashfree Payments — 1 operation(s) for deactivatecashgram.
  name: Cashfree Payments DeactivateCashgram API
  slug: cashfree-deactivatecashgram-api
- description: Collection of APIs to handle disputes.
  name: Cashfree Payments Disputes API
  slug: cashfree-disputes-api
- description: Collection of APIs to handle Easy-Split.
  name: Cashfree Payments Easy-Split API
  slug: cashfree-easy-split-api
- description: Collection of APIs to check eligible entities - payment methods, offers, affordability
  name: Cashfree Payments Eligibility API
  slug: cashfree-eligibility-api
- description: The Generate KYC Link API from Cashfree Payments — 1 operation(s) for generate kyc link.
  name: Cashfree Payments Generate KYC Link API
  slug: cashfree-generate-kyc-link-api
- description: The Generate Static KYC Link API from Cashfree Payments — 1 operation(s) for generate static kyc link.
  name: Cashfree Payments Generate Static KYC Link API
  slug: cashfree-generate-static-kyc-link-api
- description: The Get KYC Link Status API from Cashfree Payments — 1 operation(s) for get kyc link status.
  name: Cashfree Payments Get KYC Link Status API
  slug: cashfree-get-kyc-link-status-api
- description: The GetCashgramStatus API from Cashfree Payments — 1 operation(s) for getcashgramstatus.
  name: Cashfree Payments GetCashgramStatus API
  slug: cashfree-getcashgramstatus-api
- description: Operation related to Name Match verification.
  name: Cashfree Payments Name Match API
  slug: cashfree-name-match-api
- description: Collection of APIs to handle orders.
  name: Cashfree Payments Orders API
  slug: cashfree-orders-api
- description: Collection of APIs to handle payment links.
  name: Cashfree Payments Payment Links API
  slug: cashfree-payment-links-api
- description: Collection of APIs to handle payments.
  name: Cashfree Payments Payments API
  slug: cashfree-payments-api
- description: Collection of APIs to handle refunds.
  name: Cashfree Payments Refunds API
  slug: cashfree-refunds-api
- description: Collection of APIs to handle settlements
  name: Cashfree Payments Settlement Reconciliation API
  slug: cashfree-settlement-reconciliation-api
- description: Collection of APIs to handle settlements.
  name: Cashfree Payments Settlements API
  slug: cashfree-settlements-api
- description: Collection of APIs to handle simulation.
  name: Cashfree Payments Simulation API
  slug: cashfree-simulation-api
- description: The Transfers v2 API from Cashfree Payments — 2 operation(s) for transfers v2.
  name: Cashfree Payments Transfers v2 API
  slug: cashfree-transfers-v2-api
artifact_total: 40
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cashfree-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cashfree-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cashfree-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cashfree.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cashfree.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cashfree
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/cashfree
- group: company
  title: ''
  type: Blog
  url: https://www.cashfree.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cashfree.com/payment-gateway-charges/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cashfree.com/
- group: other
  title: ''
  type: X
  url: https://x.com/gocashfree
- group: start
  title: ''
  type: DevPortal
  url: https://www.cashfree.com/devstudio
- group: operate
  title: ''
  type: Support
  url: https://www.cashfree.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.cashfree.com/contact-us/
- group: commercial
  title: ''
  type: Plans
  url: plans/cashfree-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cashfree-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cashfree-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cashfree-vocabulary.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cashfree-payment-gateway-schemas.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cashfree-payouts-schemas.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cashfree-verification-schemas.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cashfree-provider.jsonld
created: '2026-06-13'
description: Cashfree Payments is an Indian payment gateway and banking platform providing REST APIs for payment links, subscriptions, payouts, refunds, QR codes, and banking payouts across UPI, credit and debit cards, net banking, and international payment methods. It serves over one million businesses with RBI authorisation as a Payment Aggregator and Prepaid Payment Instrument provider.
examples:
- key_count: 3
  name: Cashfree Payment Gateway Examples
  slug: cashfree-payment-gateway-examples
- key_count: 3
  name: Cashfree Payouts Examples
  slug: cashfree-payouts-examples
- key_count: 3
  name: Cashfree Verification Examples
  slug: cashfree-verification-examples
finops:
- name: Cashfree Finops
  service_category: ''
  slug: cashfree-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cashfree.png
json_schemas:
- name: Cashfree Cashfree Payment Gateway APIs Schemas
  property_count: 0
  slug: cashfree-payment-gateway-schemas
- name: Cashfree Cashfree Payout APIs Schemas
  property_count: 0
  slug: cashfree-payouts-schemas
- name: Cashfree Cashfree Verification API's. Schemas
  property_count: 0
  slug: cashfree-verification-schemas
jsonld:
- class_count: 224
  name: Cashfree Payment Gateway Context
  property_count: 0
  slug: cashfree-payment-gateway
- class_count: 19
  name: Cashfree Payouts Context
  property_count: 0
  slug: cashfree-payouts
- class_count: 0
  name: Cashfree Provider Context
  property_count: 0
  slug: cashfree-provider
- class_count: 149
  name: Cashfree Verification Context
  property_count: 0
  slug: cashfree-verification
layout: provider
modified: '2026-06-13'
name: Cashfree Payments
nav: Providers
network: true
overview: 'Cashfree Payments publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Authorize API, Beneficiary v2 API, CreateCashgram API, and 18 more. Tagged areas include Payments, Payouts, UPI, India, and Payment Gateway.


  The Cashfree Payments catalog on APIs.io includes 4 JSON-LD contexts and 1 Spectral governance ruleset.


  Cashfree Payments'' developer surface includes authentication, documentation, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Cashfree Plans Pricing
  plan_count: 3
  slug: cashfree-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Cashfree Rate Limits
  slug: cashfree-rate-limits
rules:
- name: Cashfree Payments API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cashfree-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.3
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cashfree/refs/heads/main/screenshots/cashfree-2026-06-20T174035.png
security:
- kind: authentication
  name: Cashfree Authentication
  slug: cashfree-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Cashfree Domain Security
  slug: cashfree-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cashfree
tags:
- Payments
- Payouts
- UPI
- India
- Payment Gateway
- Subscriptions
- Refunds
- QR Codes
- Net Banking
- Identity Verification
website: https://www.cashfree.com/
---
