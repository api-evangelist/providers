---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Zendit Agentic Access
  operation_count: 29
  slug: zendit-agentic-access
  summary_line: 29 operations · 5 acting
api_count: 8
apis:
- description: Wallet balance and account information
  name: Zendit Account API
  slug: zendit-account-api
- description: Brand catalog
  name: Zendit Brands API
  slug: zendit-brands-api
- description: eSIM plans and activation
  name: Zendit eSIM API
  slug: zendit-esim-api
- description: Mobile credit top-ups, bundles, and data plans
  name: Zendit Mobile Top-Up API
  slug: zendit-mobile-top-up-api
- description: Transaction reporting
  name: Zendit Reports API
  slug: zendit-reports-api
- description: Utility endpoints
  name: Zendit Tools API
  slug: zendit-tools-api
- description: Cross-product transaction queries
  name: Zendit Transactions API
  slug: zendit-transactions-api
- description: Digital gift cards and utility bill payments
  name: Zendit Vouchers API
  slug: zendit-vouchers-api
artifact_total: 104
collections:
- collection_type: postman
  name: Zendit Account API
  slug: postman-zendit-account-api
- collection_type: postman
  name: Zendit Account Brands API
  slug: postman-zendit-brands-api
- collection_type: postman
  name: Zendit Account eSIM API
  slug: postman-zendit-esim-api
- collection_type: postman
  name: Zendit Account Mobile Top-Up API
  slug: postman-zendit-mobile-top-up-api
- collection_type: postman
  name: Zendit Account Reports API
  slug: postman-zendit-reports-api
- collection_type: postman
  name: Zendit Account Tools API
  slug: postman-zendit-tools-api
- collection_type: postman
  name: Zendit Account Transactions API
  slug: postman-zendit-transactions-api
- collection_type: postman
  name: Zendit Account Vouchers API
  slug: postman-zendit-vouchers-api
- collection_type: open
  name: Zendit API
  slug: open-zendit-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zendit/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zendit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zendit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zendit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenditplatform
- group: company
  title: ''
  type: Website
  url: https://zendit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://zendit.io/user-guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://zendit.io/user-guide/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.zendit.io/api/
- group: start
  title: ''
  type: Login
  url: https://console.zendit.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://zendit.io/zendit-new-features/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenditplatform
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/rules/zendit-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/vocabulary/zendit-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://zendit.io/blog/
created: '2025-02-08'
description: Zendit is a cloud-based Prepay-as-a-Service platform that provides API access to a global prepaid ecosystem. The API enables businesses to offer mobile top-ups, data packages, digital gift cards, prepaid utility bill payments, and eSIM products through a single integration.
examples:
- key_count: 3
  name: Zendit Api Balance Example
  slug: zendit-api-balance-example
- key_count: 5
  name: Zendit Api Brand Example
  slug: zendit-api-brand-example
- key_count: 4
  name: Zendit Api Brand List Example
  slug: zendit-api-brand-list-example
- key_count: 5
  name: Zendit Api Esim Plan Example
  slug: zendit-api-esim-plan-example
- key_count: 2
  name: Zendit Api Esim Plan List Example
  slug: zendit-api-esim-plan-list-example
- key_count: 3
  name: Zendit Api Esim Purchase Request Example
  slug: zendit-api-esim-purchase-request-example
- key_count: 9
  name: Zendit Api Offer Example
  slug: zendit-api-offer-example
- key_count: 4
  name: Zendit Api Offer List Example
  slug: zendit-api-offer-list-example
- key_count: 5
  name: Zendit Api Phone Lookup Example
  slug: zendit-api-phone-lookup-example
- key_count: 2
  name: Zendit Api Price Example
  slug: zendit-api-price-example
- key_count: 8
  name: Zendit Api Purchase Example
  slug: zendit-api-purchase-example
- key_count: 4
  name: Zendit Api Purchase List Example
  slug: zendit-api-purchase-list-example
- key_count: 3
  name: Zendit Api Redemption Instructions Example
  slug: zendit-api-redemption-instructions-example
- key_count: 5
  name: Zendit Api Refund Example
  slug: zendit-api-refund-example
- key_count: 4
  name: Zendit Api Report Example
  slug: zendit-api-report-example
- key_count: 3
  name: Zendit Api Report Request Example
  slug: zendit-api-report-request-example
- key_count: 4
  name: Zendit Api Topup Purchase Request Example
  slug: zendit-api-topup-purchase-request-example
- key_count: 5
  name: Zendit Api Transaction Example
  slug: zendit-api-transaction-example
- key_count: 4
  name: Zendit Api Transaction List Example
  slug: zendit-api-transaction-list-example
- key_count: 4
  name: Zendit Api Voucher Purchase Request Example
  slug: zendit-api-voucher-purchase-request-example
features:
- description: Recharge prepaid mobile credit globally across thousands of carriers.
  name: Mobile Top-Ups
- description: Sell mobile data packages to subscribers worldwide.
  name: Data Bundles
- description: Offer eSIM plans for global travelers with QR-code activation.
  name: eSIM Products
- description: Distribute prepaid gift cards across major brands.
  name: Digital Gift Cards
- description: Process prepaid utility payments for electricity, water, and gas.
  name: Utility Bill Payments
- description: Identify carrier from phone number in E.164 format.
  name: Phone Number Lookup
- description: Receive event notifications for transaction completions.
  name: Webhooks
- description: Generate transaction reports as CSV files asynchronously.
  name: Async Reports
finops:
- name: Zendit Finops
  service_category: API
  slug: zendit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zendit.png
integrations:
- description: Inbound webhook endpoints for transaction event notifications.
  name: Webhooks
- description: Bearer-token authenticated REST API over HTTPS.
  name: REST API
json_schemas:
- name: Balance
  property_count: 3
  slug: zendit-api-balance
- name: BrandList
  property_count: 4
  slug: zendit-api-brand-list
- name: Brand
  property_count: 5
  slug: zendit-api-brand
- name: EsimPlanList
  property_count: 2
  slug: zendit-api-esim-plan-list
- name: EsimPlan
  property_count: 5
  slug: zendit-api-esim-plan
- name: EsimPurchaseRequest
  property_count: 3
  slug: zendit-api-esim-purchase-request
- name: OfferList
  property_count: 4
  slug: zendit-api-offer-list
- name: Offer
  property_count: 9
  slug: zendit-api-offer
- name: PhoneLookup
  property_count: 5
  slug: zendit-api-phone-lookup
- name: Price
  property_count: 2
  slug: zendit-api-price
- name: PurchaseList
  property_count: 4
  slug: zendit-api-purchase-list
- name: Purchase
  property_count: 8
  slug: zendit-api-purchase
- name: RedemptionInstructions
  property_count: 3
  slug: zendit-api-redemption-instructions
- name: Refund
  property_count: 5
  slug: zendit-api-refund
- name: ReportRequest
  property_count: 3
  slug: zendit-api-report-request
- name: Report
  property_count: 4
  slug: zendit-api-report
- name: TopupPurchaseRequest
  property_count: 4
  slug: zendit-api-topup-purchase-request
- name: TransactionList
  property_count: 4
  slug: zendit-api-transaction-list
- name: Transaction
  property_count: 5
  slug: zendit-api-transaction
- name: VoucherPurchaseRequest
  property_count: 4
  slug: zendit-api-voucher-purchase-request
json_structures:
- name: Zendit Api Balance Structure
  property_count: 3
  slug: zendit-api-balance-structure
- name: Zendit Api Brand List Structure
  property_count: 4
  slug: zendit-api-brand-list-structure
- name: Zendit Api Brand Structure
  property_count: 5
  slug: zendit-api-brand-structure
- name: Zendit Api Esim Plan List Structure
  property_count: 2
  slug: zendit-api-esim-plan-list-structure
- name: Zendit Api Esim Plan Structure
  property_count: 5
  slug: zendit-api-esim-plan-structure
- name: Zendit Api Esim Purchase Request Structure
  property_count: 3
  slug: zendit-api-esim-purchase-request-structure
- name: Zendit Api Offer List Structure
  property_count: 4
  slug: zendit-api-offer-list-structure
- name: Zendit Api Offer Structure
  property_count: 9
  slug: zendit-api-offer-structure
- name: Zendit Api Phone Lookup Structure
  property_count: 5
  slug: zendit-api-phone-lookup-structure
- name: Zendit Api Price Structure
  property_count: 2
  slug: zendit-api-price-structure
- name: Zendit Api Purchase List Structure
  property_count: 4
  slug: zendit-api-purchase-list-structure
- name: Zendit Api Purchase Structure
  property_count: 8
  slug: zendit-api-purchase-structure
- name: Zendit Api Redemption Instructions Structure
  property_count: 3
  slug: zendit-api-redemption-instructions-structure
- name: Zendit Api Refund Structure
  property_count: 5
  slug: zendit-api-refund-structure
- name: Zendit Api Report Request Structure
  property_count: 3
  slug: zendit-api-report-request-structure
- name: Zendit Api Report Structure
  property_count: 4
  slug: zendit-api-report-structure
- name: Zendit Api Topup Purchase Request Structure
  property_count: 4
  slug: zendit-api-topup-purchase-request-structure
- name: Zendit Api Transaction List Structure
  property_count: 4
  slug: zendit-api-transaction-list-structure
- name: Zendit Api Transaction Structure
  property_count: 5
  slug: zendit-api-transaction-structure
- name: Zendit Api Voucher Purchase Request Structure
  property_count: 4
  slug: zendit-api-voucher-purchase-request-structure
jsonld:
- class_count: 17
  name: Zendit Api Context
  property_count: 38
  slug: zendit-api-context
- class_count: 2
  name: Zendit Api Esim Context
  property_count: 4
  slug: zendit-api-esim-context
- class_count: 1
  name: Zendit Api Topup Context
  property_count: 4
  slug: zendit-api-topup-context
- class_count: 2
  name: Zendit Api Voucher Context
  property_count: 6
  slug: zendit-api-voucher-context
layout: provider
modified: '2026-05-19'
name: Zendit
nav: Providers
network: true
overview: 'Zendit publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Brands API, eSIM API, and 5 more. Tagged areas include eSIM, Gift Cards, Mobile Top-Up, Payments, and Prepaid.


  The Zendit catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Zendit''s developer surface includes authentication, documentation, getting-started guide, API reference, changelog, engineering blog, and 9 more developer resources.'
plans:
- name: Zendit Plans Pricing
  plan_count: 3
  slug: zendit-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 5
  name: Zendit Rate Limits
  slug: zendit-rate-limits
rules:
- name: Zendit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zendit-jsonschema-spectral-rules
- name: Zendit API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 13
  slug: zendit-rules
score:
  band: developing
  composite: 45.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 29.2
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/screenshots/zendit-2026-06-20T201909.png
security:
- kind: authentication
  name: Zendit Authentication
  slug: zendit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zendit Domain Security
  slug: zendit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zendit
tags:
- eSIM
- Gift Cards
- Mobile Top-Up
- Payments
- Prepaid
use_cases:
- description: Power top-up and data plan sales for MVNOs and resellers.
  name: Telecom Resellers
- description: Embed eSIM purchases into travel booking flows.
  name: Travel Apps
- description: Aggregate digital gift card inventory across brands.
  name: Gift Card Marketplaces
- description: Enable bill payment and prepaid services within wallets.
  name: Fintech Apps
- description: Reward users with mobile top-ups, gift cards, or eSIM data.
  name: Loyalty Programs
website: https://zendit.io/
---
