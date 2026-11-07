---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Assembly Payments Agentic Access
  operation_count: 141
  slug: assembly-payments-agentic-access
  summary_line: 141 operations · 60 acting
api_count: 7
apis:
- baseURL: https://au-0000.api.assemblypay.com
  baseurl_source: declared
  description: Configure and manage webhook subscriptions and delivery for Zai/Assembly platform events.
  name: Webhooks API
  slug: webhooks-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Addresses API from Assembly Payments — 1 operation(s) for addresses.
  name: Assembly Payments Addresses API
  slug: assembly-payments-addresses-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Authentication API from Assembly Payments — 1 operation(s) for authentication.
  name: Assembly Payments Authentication API
  slug: assembly-payments-authentication-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Bank Accounts API from Assembly Payments — 6 operation(s) for bank accounts.
  name: Assembly Payments Bank Accounts API
  slug: assembly-payments-bank-accounts-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Batch Transactions API from Assembly Payments — 2 operation(s) for batch transactions.
  name: Assembly Payments Batch Transactions API
  slug: assembly-payments-batch-transactions-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The BPay Accounts API from Assembly Payments — 3 operation(s) for bpay accounts.
  name: Assembly Payments BPay Accounts API
  slug: assembly-payments-bpay-accounts-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Callbacks API from Assembly Payments — 4 operation(s) for callbacks.
  name: Assembly Payments Callbacks API
  slug: assembly-payments-callbacks-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Card Accounts API from Assembly Payments — 4 operation(s) for card accounts.
  name: Assembly Payments Card Accounts API
  slug: assembly-payments-card-accounts-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Charges API from Assembly Payments — 4 operation(s) for charges.
  name: Assembly Payments Charges API
  slug: assembly-payments-charges-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Companies API from Assembly Payments — 2 operation(s) for companies.
  name: Assembly Payments Companies API
  slug: assembly-payments-companies-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Direct Debit Authorities API from Assembly Payments — 2 operation(s) for direct debit authorities.
  name: Assembly Payments Direct Debit Authorities API
  slug: assembly-payments-direct-debit-authorities-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Disbursements API from Assembly Payments — 7 operation(s) for disbursements.
  name: Assembly Payments Disbursements API
  slug: assembly-payments-disbursements-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Failed NPP Payment Details API from Assembly Payments — 1 operation(s) for failed npp payment details.
  name: Assembly Payments Failed NPP Payment Details API
  slug: assembly-payments-failed-npp-payment-details-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Fees API from Assembly Payments — 2 operation(s) for fees.
  name: Assembly Payments Fees API
  slug: assembly-payments-fees-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Item Actions API from Assembly Payments — 8 operation(s) for item actions.
  name: Assembly Payments Item Actions API
  slug: assembly-payments-item-actions-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Items API from Assembly Payments — 9 operation(s) for items.
  name: Assembly Payments Items API
  slug: assembly-payments-items-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Jobs API from Assembly Payments — 2 operation(s) for jobs.
  name: Assembly Payments Jobs API
  slug: assembly-payments-jobs-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Marketplaces API from Assembly Payments — 1 operation(s) for marketplaces.
  name: Assembly Payments Marketplaces API
  slug: assembly-payments-marketplaces-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The PayIDs API from Assembly Payments — 3 operation(s) for payids.
  name: Assembly Payments Pay IDs API
  slug: assembly-payments-payids-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: Agreement Management APIs
  name: Assembly Payments PayTo Agreements API
  slug: assembly-payments-payto-agreements-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: Payment Initiation APIs
  name: Assembly Payments PayTo Payments API
  slug: assembly-payments-payto-payments-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Requests API from Assembly Payments — 2 operation(s) for requests.
  name: Assembly Payments Requests API
  slug: assembly-payments-requests-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Status API from Assembly Payments — 1 operation(s) for status.
  name: Assembly Payments Status API
  slug: assembly-payments-status-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Sub-wallets API from Assembly Payments — 9 operation(s) for sub-wallets.
  name: Assembly Payments Sub Wallets API
  slug: assembly-payments-sub-wallets-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Token Auth API from Assembly Payments — 1 operation(s) for token auth.
  name: Assembly Payments Token Auth API
  slug: assembly-payments-token-auth-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Tools API from Assembly Payments — 1 operation(s) for tools.
  name: Assembly Payments Tools API
  slug: assembly-payments-tools-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Transaction supplementary data API from Assembly Payments — 1 operation(s) for transaction supplementary data.
  name: Assembly Payments Transaction supplementary data API
  slug: assembly-payments-transaction-supplementary-data-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Transactions API from Assembly Payments — 7 operation(s) for transactions.
  name: Assembly Payments Transactions API
  slug: assembly-payments-transactions-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Users API from Assembly Payments — 9 operation(s) for users.
  name: Assembly Payments Users API
  slug: assembly-payments-users-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Virtual Accounts API from Assembly Payments — 5 operation(s) for virtual accounts.
  name: Assembly Payments Virtual Accounts API
  slug: assembly-payments-virtual-accounts-api
- baseURL: https://secure.api.promisepay.com
  baseurl_source: declared
  description: The Wallet Accounts API from Assembly Payments — 7 operation(s) for wallet accounts.
  name: Assembly Payments Wallet Accounts API
  slug: assembly-payments-wallet-accounts-api
artifact_total: 75
common:
- group: auth
  href: https://artifacts.apis.io/assembly-payments/well-known/assembly-payments-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/assembly-payments-status-security.txt
- group: other
  href: https://artifacts.apis.io/assembly-payments/capabilities/assembly-payments-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/assembly-payments-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/assembly-payments/agentic-access/assembly-payments-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/assembly-payments-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/assembly-payments/rate-limits/assembly-payments-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/assembly-payments-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/assembly-payments/plans/assembly-payments-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/assembly-payments-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/assembly-payments/rules/assembly-payments-rules.yml
  title: ''
  type: Spectral
  url: rules/assembly-payments-rules.yml
- group: design
  href: https://artifacts.apis.io/assembly-payments/json-ld/assembly-payments-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/assembly-payments-context.jsonld
- group: design
  href: https://artifacts.apis.io/assembly-payments/vocabulary/assembly-payments-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/assembly-payments-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/assembly-payments/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/assembly-payments/data-model/assembly-payments-data-model.yml
  title: ''
  type: DataModel
  url: data-model/assembly-payments-data-model.yml
- group: design
  href: https://artifacts.apis.io/assembly-payments/components/assembly-payments-components.yml
  title: ''
  type: Components
  url: components/assembly-payments-components.yml
- group: design
  href: https://artifacts.apis.io/assembly-payments/conventions/assembly-payments-conventions.yml
  title: ''
  type: Conventions
  url: conventions/assembly-payments-conventions.yml
- group: start
  href: https://artifacts.apis.io/assembly-payments/sandbox/assembly-payments-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/assembly-payments-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/assembly-payments/lifecycle/assembly-payments-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/assembly-payments-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/assembly-payments/lifecycle/assembly-payments-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/assembly-payments-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/assembly-payments/errors/assembly-payments-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/assembly-payments-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/assembly-payments/errors/assembly-payments-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/assembly-payments-problem-types.yml
- group: design
  href: https://artifacts.apis.io/assembly-payments/conformance/assembly-payments-conformance.yml
  title: ''
  type: Conformance
  url: conformance/assembly-payments-conformance.yml
- group: other
  href: https://artifacts.apis.io/assembly-payments/overlays/assembly-payments-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/assembly-payments-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/assembly-payments/llms/assembly-payments-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assembly-payments-llms.txt
- group: agent
  href: https://artifacts.apis.io/assembly-payments/well-known/assembly-payments-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assembly-payments-well-known.yml
- group: other
  href: https://artifacts.apis.io/assembly-payments/hosts/assembly-payments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assembly-payments-hosts.yml
- group: build
  href: https://artifacts.apis.io/assembly-payments/integrations/assembly-payments-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/assembly-payments-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/assembly-payments/vendors/assembly-payments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assembly-payments-vendors.yml
- group: build
  href: https://artifacts.apis.io/assembly-payments/packages/assembly-payments-packages.yml
  title: ''
  type: SDKs
  url: packages/assembly-payments-packages.yml
- group: build
  href: https://artifacts.apis.io/assembly-payments/packages/assembly-payments-packages.yml
  title: ''
  type: Packages
  url: packages/assembly-payments-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hellozai.com/docs/onboarding-a-pay-in-user
- group: auth
  href: https://artifacts.apis.io/assembly-payments/authentication/assembly-payments-authentication.yml
  title: ''
  type: Authentication
  url: authentication/assembly-payments-authentication.yml
- group: auth
  href: https://artifacts.apis.io/assembly-payments/security/assembly-payments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assembly-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assemblypay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hellozai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hellozai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hellozai.com/reference
- group: company
  title: ''
  type: Blog
  url: https://www.hellozai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hellozai.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.hellozai.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.hellozai.com/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hellozai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellozai.com/company/policies/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellozai.com/company/policies/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.hellozai.com/company/leadership-team
- group: company
  title: ''
  type: Newsroom
  url: https://www.hellozai.com/news
- group: company
  title: ''
  type: About
  url: https://www.hellozai.com/about-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AssemblyPayments
created: '2026-10-22'
description: Assembly Payments was an Australian payments platform founded to give marketplaces, platforms and businesses embedded payment processing, digital wallets, escrow-style payment workflows and real-time payouts through an API. According to the company's own About page, Assembly Payments became the first non-bank to launch real-time payments in Australia and later merged with CurrencyFair to become Zai; assemblypay.com now redirects to hellozai.com, and the developer portal at developer.hellozai.com (still introduced as 'The Assembly Payments Developer Portal') documents the Zai payments API for payment processing, wallets, PayTo, payouts and workflow automation.
image: https://www.hellozai.com/hubfs/zai01/assets/Featured%20images/Homepage-featured-image.png
json_schemas:
- name: AgreementDetailsResponse
  property_count: 9
  slug: assembly-payments-agreement-details-response
- name: AmendAgreementDetailsRequest
  property_count: 4
  slug: assembly-payments-amend-agreement-details-request
- name: bank_account_requestBody_au
  property_count: 10
  slug: assembly-payments-bank-account-request-body-au
- name: callbacks
  property_count: 2
  slug: assembly-payments-callbacks
- name: charge_requestBody
  property_count: 14
  slug: assembly-payments-charge-request-body
- name: deregister_pay_id
  property_count: 3
  slug: assembly-payments-deregister-pay-id
- name: InitiatePaymentRequest
  property_count: 3
  slug: assembly-payments-initiate-payment-request
- name: InitiatePaymentResponse
  property_count: 7
  slug: assembly-payments-initiate-payment-response
- name: InitiatePaymentStatusResponse
  property_count: 13
  slug: assembly-payments-initiate-payment-status-response
- name: item_requestBody
  property_count: 13
  slug: assembly-payments-item-request-body
- name: Job
  property_count: 7
  slug: assembly-payments-job
- name: Jobs
  property_count: 2
  slug: assembly-payments-jobs
- name: make_payment_requestBody
  property_count: 5
  slug: assembly-payments-make-payment-request-body
- name: npp_last_domestic_leg_disbursement
  property_count: 22
  slug: assembly-payments-npp-last-domestic-leg-disbursement
- name: npp_last_domestic_leg_requestBody
  property_count: 6
  slug: assembly-payments-npp-last-domestic-leg-request-body
- name: pay_id_request
  property_count: 3
  slug: assembly-payments-pay-id-request
- name: pay_id
  property_count: 8
  slug: assembly-payments-pay-id
- name: paymentData
  property_count: 12
  slug: assembly-payments-payment-data
- name: single_item
  property_count: 1
  slug: assembly-payments-single-item
- name: status
  property_count: 4
  slug: assembly-payments-status
- name: supplementaryData
  property_count: 11
  slug: assembly-payments-supplementary-data
- name: update_user_requestBody
  property_count: 20
  slug: assembly-payments-update-user-request-body
- name: update_va_status_resp
  property_count: 3
  slug: assembly-payments-update-va-status-resp
- name: UpdateWebhookRequestBody
  property_count: 3
  slug: assembly-payments-update-webhook-request-body
- name: user_requestBody
  property_count: 22
  slug: assembly-payments-user-request-body
- name: ValidateAgreementRequest
  property_count: 4
  slug: assembly-payments-validate-agreement-request
- name: virtual_account
  property_count: 14
  slug: assembly-payments-virtual-account
- name: virtual_accounts_list
  property_count: 2
  slug: assembly-payments-virtual-accounts-list
- name: WebhookRequestBody
  property_count: 3
  slug: assembly-payments-webhook-request-body
- name: Webhook
  property_count: 9
  slug: assembly-payments-webhook
- name: Webhooks
  property_count: 2
  slug: assembly-payments-webhooks
jsonld:
- class_count: 120
  name: Assembly Payments Context
  property_count: 282
  slug: assembly-payments-context
layout: provider
modified: '2026-10-22'
name: Assembly Payments
nav: Providers
network: true
overview: 'Assembly Payments publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks API, Addresses API, Authentication API, and 28 more. Tagged areas include Company, Payments, Fintech, Marketplace, and Digital Wallet.


  The Assembly Payments catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Assembly Payments'' developer surface includes sandbox, getting-started guide, authentication, documentation, API reference, engineering blog, pricing, and 37 more developer resources.'
plans:
- name: Assembly Payments Plans Pricing
  plan_count: 2
  slug: assembly-payments-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Assembly Payments Rate Limits
  slug: assembly-payments-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Assembly Payments API Rules
  rule_count: 65
  severity_counts:
    error: 42
    hint: 0
    info: 6
    warn: 17
  slug: assembly-payments-rules
scopes:
- name: Assembly Payments Scopes
  scope_count: 0
  slug: assembly-payments-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 35
    catalog_earned: 81.8
    catalog_earned_first_party: 16.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 71.9
    developer_ergonomics: 62.5
    discoverability: 80.4
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 31
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/assembly-payments/assembly-payments-2026-11-03T121217.png
security:
- kind: authentication
  name: Assembly Payments Authentication
  slug: assembly-payments-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Assembly Payments Domain Security
  slug: assembly-payments-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 5
skills:
- name: assembly-payments-marketplace-payment
  slug: assembly-payments-marketplace-payment
- name: assembly-payments-payto-agreement
  slug: assembly-payments-payto-agreement
- name: assembly-payments-refund-or-cancel
  slug: assembly-payments-refund-or-cancel
- name: assembly-payments-wallet-payout
  slug: assembly-payments-wallet-payout
- name: assembly-payments-webhook-setup
  slug: assembly-payments-webhook-setup
slug: assembly-payments
tags:
- Company
- Payments
- Fintech
- Marketplace
- Digital Wallet
- Payouts
- Australia
- PayTo
website: https://assemblypay.com/
---
