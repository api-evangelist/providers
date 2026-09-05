---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Payfast Agentic Access
  operation_count: 16
  slug: payfast-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: REST API for managing recurring billing subscriptions, including fetching subscription details, pausing, unpausing, cancelling, updating subscription parameters, and processing adhoc charges against e
  name: PayFast Subscriptions API
  slug: payfast-subscriptions-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: REST API for managing tokenized recurring card payment agreements, allowing merchants to charge customers at future dates and amounts without storing card details directly. Supports adhoc charges on s
  name: PayFast Tokenization API
  slug: payfast-tokenization-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: REST API for querying merchant transaction history with support for date range queries, daily summaries, weekly aggregations, and monthly aggregations, enabling merchants to reconcile payments program
  name: PayFast Transaction History API
  slug: payfast-transaction-history-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: REST API for querying individual credit card transaction details by transaction ID, giving merchants programmatic access to card payment records.
  name: PayFast Credit Card Transactions API
  slug: payfast-credit-card-transactions-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: REST API for merchants to initiate and track refunds on completed transactions, specifying refund amount, reason, and account type for disbursement back to the customer.
  name: PayFast Refunds API
  slug: payfast-refunds-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: Query individual credit card transaction details
  name: PayFast Credit Card Transactions API
  slug: payfast-credit-card-transactions-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: Validate ITN (Instant Transaction Notification) webhooks
  name: PayFast Notifications API
  slug: payfast-notifications-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: Generate payment identifiers for embedded (onsite) checkout flows
  name: PayFast Onsite Checkout API
  slug: payfast-onsite-checkout-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: Standard redirect-based payment form integration
  name: PayFast Payment Form API
  slug: payfast-payment-form-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: Initiate and track refunds on completed transactions
  name: PayFast Refunds API
  slug: payfast-refunds-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: Manage recurring billing subscription agreements
  name: PayFast Subscriptions API
  slug: payfast-subscriptions-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: Manage tokenized card payment agreements (adhoc charges)
  name: PayFast Tokenization API
  slug: payfast-tokenization-api
- baseURL: https://api.payfast.co.za
  baseurl_source: declared
  description: Query merchant transaction history with date range and aggregations
  name: PayFast Transaction History API
  slug: payfast-transaction-history-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PayFast Credit Card Transactions API
  slug: open-payfast-credit-card-transactions-api
- collection_type: open
  name: PayFast Credit Card Transactions Notifications API
  slug: open-payfast-notifications-api
- collection_type: open
  name: PayFast Credit Card Transactions Onsite Checkout API
  slug: open-payfast-onsite-checkout-api
- collection_type: open
  name: PayFast Credit Card Transactions Payment Form API
  slug: open-payfast-payment-form-api
- collection_type: open
  name: PayFast Credit Card Transactions Refunds API
  slug: open-payfast-refunds-api
- collection_type: open
  name: PayFast Credit Card Transactions Subscriptions API
  slug: open-payfast-subscriptions-api
- collection_type: open
  name: PayFast Credit Card Transactions Tokenization API
  slug: open-payfast-tokenization-api
- collection_type: open
  name: PayFast Credit Card Transactions Transaction History API
  slug: open-payfast-transaction-history-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payfast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payfast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payfast-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://payfast.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.payfast.co.za/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Payfast
- group: commercial
  title: ''
  type: Pricing
  url: https://payfast.io/fees
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payfast.io
- group: company
  title: ''
  type: Blog
  url: https://payfast.io/resources
- group: operate
  title: ''
  type: Support
  url: https://support.payfast.help
- group: commercial
  title: ''
  type: Plans
  url: plans/payfast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payfast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/payfast-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: https://developers.payfast.co.za/documentation
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.payfast.co.za
created: '2026-06-13'
description: South African payment gateway providing REST APIs for online payment processing, subscription billing, tokenized recurring card payments, onsite checkout, QR code payments, instant EFT bank transfers, and merchant refunds. Trusted by 80,000+ South African businesses and certified PCI-DSS Level 1.
examples:
- key_count: 4
  name: Adhoc Charge
  slug: adhoc-charge
- key_count: 4
  name: Create Refund
  slug: create-refund
- key_count: 4
  name: Fetch Subscription
  slug: fetch-subscription
- key_count: 4
  name: Initiate Payment
  slug: initiate-payment
- key_count: 3
  name: Subscription Recurring Billing
  slug: subscription-recurring-billing
- key_count: 4
  name: Transaction History Range
  slug: transaction-history-range
finops:
- name: Payfast Finops
  service_category: ''
  slug: payfast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payfast.png
json_schemas:
- name: PayFast Payment Form Request
  property_count: 36
  slug: payfast-payment-form
- name: PayFast Refund Request
  property_count: 4
  slug: payfast-refund-request
- name: PayFast Subscription Update Request
  property_count: 4
  slug: payfast-subscription-update
jsonld:
- class_count: 0
  name: Payfast Context
  property_count: 0
  slug: payfast
layout: provider
modified: '2026-06-13'
name: PayFast
nav: Providers
network: true
overview: 'PayFast publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Subscriptions API, Tokenization API, Transaction History API, and 10 more. Tagged areas include Payments, Payment Gateway, South Africa, Subscription, and Recurring Billing.


  The PayFast catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PayFast''s developer surface includes authentication, documentation, pricing, engineering blog, support, sandbox, and 9 more developer resources.'
plans:
- name: Payfast Plans Pricing
  plan_count: 2
  slug: payfast-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Payfast Rate Limits
  slug: payfast-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: PayFast API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: payfast-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 56.3
    catalog_earned_first_party: 0.0
    catalog_gap: 58.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 60.8
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payfast/refs/heads/main/screenshots/payfast-2026-06-20T191452.png
security:
- kind: authentication
  name: Payfast Authentication
  slug: payfast-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Payfast Domain Security
  slug: payfast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payfast
tags:
- Payments
- Payment Gateway
- South Africa
- Subscription
- Recurring Billing
- Tokenization
- Instant EFT
- QR Code Payments
- Refunds
- Fintech
website: https://payfast.io
---
