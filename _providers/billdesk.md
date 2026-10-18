---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Billdesk Agentic Access
  operation_count: 31
  slug: billdesk-agentic-access
  summary_line: 31 operations · 21 acting
api_count: 14
apis:
- description: Pre-built hosted checkout solution for one-time and recurring online payments. Merchants redirect customers to BillDesk-hosted pages, minimizing PCI DSS scope.
  name: BillDesk Neo Full Redirect API
  slug: neo-payments-api
- description: SDK-based payment integration for Android, iOS, Flutter, and web. Provides embedded payment experiences with BillDesk handling payment orchestration.
  name: BillDesk Ace SDK API
  slug: ace-sdk-api
- description: Direct REST API access for advanced payment processing, giving merchants full control over checkout UX. Supports transactions, mandates, refunds, card tokenization, invoices, payment links, and settle
  name: BillDesk CX+ Deep API
  slug: cx-plus-deep-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Authentication API from BillDesk — 3 operation(s) for authentication.
  name: BillDesk Authentication API
  slug: billdesk-authentication-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Card Account API from BillDesk — 4 operation(s) for card account.
  name: BillDesk Card Account API
  slug: billdesk-card-account-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Guest Checkout (AltID) API from BillDesk — 1 operation(s) for guest checkout (altid).
  name: BillDesk Guest Checkout (AltID) API
  slug: billdesk-guest-checkout-altid-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Invoice API from BillDesk — 2 operation(s) for invoice.
  name: BillDesk Invoice API
  slug: billdesk-invoice-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Mandate API from BillDesk — 6 operation(s) for mandate.
  name: BillDesk Mandate API
  slug: billdesk-mandate-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Order API from BillDesk — 3 operation(s) for order.
  name: BillDesk Order API
  slug: billdesk-order-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Payment Links API from BillDesk — 4 operation(s) for payment links.
  name: BillDesk Payment Links API
  slug: billdesk-payment-links-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Penny Drop API from BillDesk — 1 operation(s) for penny drop.
  name: BillDesk Penny Drop API
  slug: billdesk-penny-drop-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Refund API from BillDesk — 2 operation(s) for refund.
  name: BillDesk Refund API
  slug: billdesk-refund-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Settlement API from BillDesk — 1 operation(s) for settlement.
  name: BillDesk Settlement API
  slug: billdesk-settlement-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Transaction API from BillDesk — 3 operation(s) for transaction.
  name: BillDesk Transaction API
  slug: billdesk-transaction-api
- baseURL: https://api.billdesk.com/payments/ve1_2
  baseurl_source: declared
  description: The Validate VPA API from BillDesk — 1 operation(s) for validate vpa.
  name: BillDesk Validate VPA API
  slug: billdesk-validate-vpa-api
artifact_total: 51
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/agentic-access/billdesk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/billdesk-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/rules/billdesk-rules.yml
  title: ''
  type: Spectral
  url: rules/billdesk-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/json-ld/billdesk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/billdesk-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/vocabulary/billdesk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/billdesk-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/data-model/billdesk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/billdesk-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/errors/billdesk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/billdesk-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/conformance/billdesk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billdesk-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/well-known/billdesk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/billdesk-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/hosts/billdesk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billdesk-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/vendors/billdesk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billdesk-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/security/billdesk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billdesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billdesk.com/web/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billdesk.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/billdesk
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/billdesk
- group: company
  title: ''
  type: Blog
  url: https://www.billdesk.com/web/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.billdesk.com/web/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.com/billdesk.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/billdesk
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/plans/billdesk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/billdesk-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/rate-limits/billdesk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/billdesk-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/finops/billdesk-finops.yml
  title: ''
  type: FinOps
  url: finops/billdesk-finops.yml
created: '2026-06-13'
description: BillDesk is an Indian integrated payment solutions platform founded in 2000, offering REST APIs for bill payments, recurring mandates, UPI payments, net banking, card payments, and enterprise payment gateway integrations. The platform provides three integration tiers (Neo full-redirect, Ace SDK, and CX+ deep API), supporting online payments, e-Mandate setup, invoicing, refunds, tokenization, and 150+ payment methods across web, mobile, and third-party e-commerce plugins.
finops:
- has_sources: false
  method: generated
  name: Billdesk Finops
  primary_unit: ''
  service_category: ''
  slug: billdesk-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/billdesk.png
json_schemas:
- name: Additional-Info
  property_count: 7
  slug: billdesk-additional-info
- name: Altid_card_request
  property_count: 5
  slug: billdesk-altid-card-request
- name: Bankaccount
  property_count: 7
  slug: billdesk-bankaccount
- name: bankid
  property_count: 0
  slug: billdesk-bankid
- name: Cardacc-network-issuer-token
  property_count: 5
  slug: billdesk-cardacc-network-issuer-token
- name: cardaccid auth data
  property_count: 7
  slug: billdesk-cardaccid-auth-data
- name: Cardaccount-in-txn-response
  property_count: 8
  slug: billdesk-cardaccount-in-txn-response
- name: currency
  property_count: 0
  slug: billdesk-currency
- name: customer-response
  property_count: 4
  slug: billdesk-customer-response
- name: customer
  property_count: 4
  slug: billdesk-customer
- name: Device object
  property_count: 4
  slug: billdesk-device-order
- name: Device
  property_count: 11
  slug: billdesk-device
- name: error_desc
  property_count: 0
  slug: billdesk-error-desc
- name: Mandate
  property_count: 12
  slug: billdesk-mandate
- name: mercid
  property_count: 0
  slug: billdesk-mercid
- name: Network-issuer-token
  property_count: 7
  slug: billdesk-network-issuer-token
- name: objectid
  property_count: 0
  slug: billdesk-objectid
- name: orderid
  property_count: 0
  slug: billdesk-orderid
- name: Pay using alt id token
  property_count: 4
  slug: billdesk-pay-using-altid
- name: Pay using card number - pan
  property_count: 7
  slug: billdesk-pay-using-card-number-pan
- name: Pay using issuer token
  property_count: 4
  slug: billdesk-pay-using-issuer-token
- name: Pay using network token
  property_count: 4
  slug: billdesk-pay-using-network-token
- name: payment_method_type
  property_count: 0
  slug: billdesk-payment-method-type
- name: payment-object-response
  property_count: 4
  slug: billdesk-payment-object-response
- name: payment-object
  property_count: 5
  slug: billdesk-payment-object
- name: Response-parameters
  property_count: 8
  slug: billdesk-response-parameters
- name: UDF
  property_count: 0
  slug: billdesk-udf
- name: upi-response
  property_count: 1
  slug: billdesk-upi-response
- name: Upi
  property_count: 1
  slug: billdesk-upi
jsonld:
- class_count: 60
  name: Billdesk Context
  property_count: 112
  slug: billdesk-context
layout: provider
modified: '2026-06-13'
name: BillDesk
nav: Providers
network: true
overview: 'BillDesk publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Card Account API, Guest Checkout (AltID) API, and 12 more. Tagged areas include Payments, India, Payment Gateway, UPI, and Recurring Payments.


  The BillDesk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BillDesk''s developer surface includes documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Billdesk Plans Pricing
  plan_count: 1
  slug: billdesk-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Billdesk Rate Limits
  slug: billdesk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: BillDesk API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: billdesk-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 0.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.9
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 66.0
    developer_ergonomics: 10.7
    discoverability: 71.4
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/screenshots/billdesk-2026-06-20T173307.png
security:
- kind: domain-security
  name: Billdesk Domain Security
  slug: billdesk-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: billdesk
tags:
- Payments
- India
- Payment Gateway
- UPI
- Recurring Payments
- Mandates
- Net Banking
- Bill Payments
- Fintech
website: https://www.billdesk.com/web/
---
