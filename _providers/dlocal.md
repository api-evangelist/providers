---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 29.8
  scored_at: '2026-09-07'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Dlocal Agentic Access
  operation_count: 34
  slug: dlocal-agentic-access
  summary_line: 34 operations · 18 acting
api_count: 4
apis:
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Distribute funds globally with multi-currency support and local compliance across 60+ emerging market countries. Includes payout submission and retrieval, balance checking, quote generation for curren
  name: dLocal Payouts API
  slug: dlocal-payouts-api
- description: Complete solution for marketplaces and platforms with automated account onboarding, KYC information handling, bank account management, transfer operations, and account status and balance queries.
  name: dLocal Platforms API
  slug: dlocal-platforms-api
- description: Identity verification and document management API supporting verification creation and retrieval, document management, and status updates for compliance workflows across emerging markets.
  name: dLocal Verification API
  slug: dlocal-verification-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Platform sub-account management
  name: dLocal Accounts API
  slug: dlocal-accounts-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Query account balances
  name: dLocal Balance API
  slug: dlocal-balance-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Bank account registration and management
  name: dLocal Bank Accounts API
  slug: dlocal-bank-accounts-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Manage chargeback disputes
  name: dLocal Chargebacks API
  slug: dlocal-chargebacks-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Foreign exchange rate queries
  name: dLocal Currency API
  slug: dlocal-currency-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Document upload and management
  name: dLocal Documents API
  slug: dlocal-documents-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Know Your Customer verification
  name: dLocal KYC API
  slug: dlocal-kyc-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Query available local payment methods
  name: dLocal Payment Methods API
  slug: dlocal-payment-methods-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Create and manage payment transactions
  name: dLocal Payments API
  slug: dlocal-payments-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Submit and manage disbursements
  name: dLocal Payouts API
  slug: dlocal-payouts-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Reverse payment transactions
  name: dLocal Refunds API
  slug: dlocal-refunds-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Card tokenization operations
  name: dLocal Tokens API
  slug: dlocal-tokens-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Fund transfers between accounts
  name: dLocal Transfers API
  slug: dlocal-transfers-api
- baseURL: https://api.dlocal.com
  baseurl_source: declared
  description: Identity verification requests
  name: dLocal Verifications API
  slug: dlocal-verifications-api
arazzos:
- description: Authorize a card transaction, confirm the authorization, then capture the funds.
  name: dLocal Authorize and Capture Payment
  slug: dlocal-authorize-and-capture-payment-workflow
- description: Create an alternative payment, check its status, and cancel it while it is still PENDING.
  name: dLocal Cancel Pending Payment
  slug: dlocal-cancel-pending-payment-workflow
- description: Create a KYC verification, confirm it persisted, then branch on its status to update state or list documents.
  name: dLocal Create and Resolve KYC Verification
  slug: dlocal-create-and-resolve-kyc-verification-workflow
- description: Discover a supported payment method, create a payment, then poll its status until it settles.
  name: dLocal Create Payment and Confirm Status
  slug: dlocal-create-payment-and-confirm-status-workflow
- description: Enroll a payer for Pix Automatico, confirm the enrollment is ACTIVE, then place the first recurring charge.
  name: dLocal Enroll and Charge Recurring
  slug: dlocal-enroll-and-charge-recurring-workflow
- description: Preview the exchange rate for a corridor, then create a payment in the local currency.
  name: dLocal FX Preview and Pay
  slug: dlocal-fx-preview-and-pay-workflow
- description: Request a payout on hold, review it, then release or cancel based on the review.
  name: dLocal Hold and Release Payout
  slug: dlocal-hold-and-release-payout-workflow
- description: Confirm a payment, list all refunds raised against it, then retrieve one refund in detail.
  name: dLocal List and Inspect Payment Refunds
  slug: dlocal-list-payment-refunds-workflow
- description: Add a bank account to a sub-merchant, list the account's bank accounts, retrieve one, then disable it.
  name: dLocal Manage Account Bank Accounts
  slug: dlocal-manage-account-bank-accounts-workflow
- description: Create a platform sub-merchant account, attach a bank account, then confirm KYC and balance.
  name: dLocal Onboard Sub-Merchant Account
  slug: dlocal-onboard-submerchant-account-workflow
- description: Check balance, lock an FX quote, request a payout against the quote, then confirm its status.
  name: dLocal Quote and Request Payout
  slug: dlocal-quote-and-request-payout-workflow
- description: Confirm a payment is PAID, issue a refund against it, then verify the refund status.
  name: dLocal Refund Payment and Confirm
  slug: dlocal-refund-payment-and-confirm-workflow
- description: Check the source account balance, transfer funds to another account, then confirm the transfer.
  name: dLocal Settle Transfer Between Accounts
  slug: dlocal-settle-transfer-between-accounts-workflow
- description: Create a payment, simulate a chargeback against it in sandbox, then inspect the chargeback and its status.
  name: dLocal Simulate and Inspect Chargeback
  slug: dlocal-simulate-and-inspect-chargeback-workflow
- description: Tokenize a card, verify the stored token, then charge it in a card payment.
  name: dLocal Tokenize Card and Charge
  slug: dlocal-tokenize-card-and-charge-workflow
artifact_total: 60
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: dLocal Payins Accounts API
  slug: open-dlocal-accounts-api
- collection_type: open
  name: dLocal Payins Accounts Balance API
  slug: open-dlocal-balance-api
- collection_type: open
  name: dLocal Payins Accounts Bank Accounts API
  slug: open-dlocal-bank-accounts-api
- collection_type: open
  name: dLocal Payins Accounts Chargebacks API
  slug: open-dlocal-chargebacks-api
- collection_type: open
  name: dLocal Payins Accounts Currency API
  slug: open-dlocal-currency-api
- collection_type: open
  name: dLocal Payins Accounts Documents API
  slug: open-dlocal-documents-api
- collection_type: open
  name: dLocal Payins Accounts KYC API
  slug: open-dlocal-kyc-api
- collection_type: open
  name: dLocal Payins Accounts Payment Methods API
  slug: open-dlocal-payment-methods-api
- collection_type: open
  name: dLocal Payins Accounts Payments API
  slug: open-dlocal-payments-api
- collection_type: open
  name: dLocal Payins Accounts Payouts API
  slug: open-dlocal-payouts-api
- collection_type: open
  name: dLocal Payins Accounts Refunds API
  slug: open-dlocal-refunds-api
- collection_type: open
  name: dLocal Payins Accounts Tokens API
  slug: open-dlocal-tokens-api
- collection_type: open
  name: dLocal Payins Accounts Transfers API
  slug: open-dlocal-transfers-api
- collection_type: open
  name: dLocal Payins Accounts Verifications API
  slug: open-dlocal-verifications-api
common:
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-authorize-and-capture-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-cancel-pending-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-create-and-resolve-kyc-verification-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-create-payment-and-confirm-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-enroll-and-charge-recurring-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-fx-preview-and-pay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-hold-and-release-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-list-payment-refunds-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-manage-account-bank-accounts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-onboard-submerchant-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-quote-and-request-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-refund-payment-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-settle-transfer-between-accounts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-simulate-and-inspect-chargeback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dlocal-tokenize-card-and-charge-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://dlocal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dlocal.com/reference/api
- group: auth
  title: ''
  type: Compliance
  url: https://docs.dlocal.com/docs/pci-compliance
- group: build
  title: ''
  type: SDKs
  url: https://docs.dlocal.com/reference/postman-api-collection
- group: start
  title: ''
  type: Signup
  url: https://dlocal.com/contact-sales/
- group: other
  title: ''
  type: Resources
  url: https://dlocal.com/careers/
- group: company
  title: ''
  type: Newsletter
  url: https://dlocal.com/press-releases/
- group: other
  title: ''
  type: Resources
  url: https://investor.dlocal.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dlocal.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dlocal.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: http://intercom.help/end-user-team-faqs/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dlocal
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/dlocal-direct-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/dlocal-direct-android-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/mobile-checkout-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/mobile-checkout-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/web-drop-in-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/data-collector-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/data-collector-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/dlocal-data-collector-capacitor-plugin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/dlocal-direct-js-native-integration
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dlocal/smart-fields-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dlocal/Starter-Code-Examples
- group: build
  title: ''
  type: SDKs
  url: https://docs.dlocal.com/reference/including-dlocaljs
- group: other
  title: ''
  type: Troubleshooting
  url: https://docs.dlocal.com/reference/troubleshooting-integration
- group: other
  title: ''
  type: Troubleshooting
  url: https://docs.dlocal.com/reference/troubleshooting-signature
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.dlocal.com/reference/http-errors-payments
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.dlocal.com/reference/http-errors-refunds
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.dlocal.com/reference/http-errors-cards
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.dlocal.com/reference/error-codes-payouts-v3
- group: design
  title: ''
  type: SpectralRules
  url: rules/dlocal-rules.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dlocal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dlocal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dlocal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dlocal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dlocal.com/docs/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.dlocal.com/reference/payins-security
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dlocal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dlocal
- group: company
  title: ''
  type: Blog
  url: https://www.dlocal.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dlocal.com/faqs/faqs-solutions/
- group: operate
  title: ''
  type: StatusPage
  url: https://dlocal.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/dLocalPayments
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/dlocal-dev
- group: commercial
  title: ''
  type: Plans
  url: plans/dlocal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dlocal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dlocal-finops.yml
created: 2026-06-13
description: dLocal is an emerging markets payment platform that enables global merchants to accept and disburse local payment methods and currencies through a single REST API. The platform covers 60+ countries across Africa, Asia, and Latin America, providing payins, payouts, and platform-as-a-service capabilities with 1,000+ local payment methods including cards, cash, bank transfers, mobile money, and eWallets.
examples:
- key_count: 4
  name: Create Payment
  slug: create-payment
- key_count: 4
  name: Create Payout
  slug: create-payout
finops:
- name: Dlocal Finops
  service_category: ''
  slug: dlocal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dlocal.png
json_schemas:
- name: dLocal Payment
  property_count: 16
  slug: payment
- name: dLocal Payout
  property_count: 13
  slug: payout
jsonld:
- class_count: 2
  name: Dlocal Context
  property_count: 56
  slug: dlocal-context
layout: provider
modified: 2026-06-13
name: dLocal
nav: Providers
network: true
overview: 'dLocal publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Payouts API, Accounts API, Balance API, and 12 more. Tagged areas include Payments, Emerging Markets, Payins, Payouts, and Fintech.


  The dLocal catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  dLocal''s developer surface includes developer portal, API reference, signup flow, support, code examples, authentication, documentation, and 56 more developer resources.'
plans:
- name: Dlocal Plans Pricing
  plan_count: 1
  slug: dlocal-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Dlocal Rate Limits
  slug: dlocal-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: dLocal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: dlocal-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: dLocal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 2
    info: 0
    warn: 4
  slug: dlocal-rules
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 62.9
    developer_ergonomics: 61.9
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
    - latin-america
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/dlocal/refs/heads/main/screenshots/dlocal-2026-06-20T180058.png
security:
- kind: authentication
  name: Dlocal Authentication
  slug: dlocal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dlocal Domain Security
  slug: dlocal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dlocal
tags:
- Payments
- Emerging Markets
- Payins
- Payouts
- Fintech
- Latin America
- Africa
- Asia
- Local Payment Methods
- Payment Processing
website: https://www.dlocal.com/
---
