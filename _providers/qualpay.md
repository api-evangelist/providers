---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 78
  human_in_the_loop: 1
  name: Qualpay Agentic Access
  operation_count: 136
  slug: qualpay-agentic-access
  summary_line: 136 operations · 78 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: The Account Updater API from Qualpay — 10 operation(s) for account updater.
  name: Qualpay Account Updater API
  slug: qualpay-account-updater-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Application
  name: Qualpay Application Boarding API
  slug: qualpay-application-boarding-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Checkout
  name: Qualpay Checkout API
  slug: qualpay-checkout-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Customer Vault
  name: Qualpay Customer Vault API
  slug: qualpay-customer-vault-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Original dispute management operations.
  name: Qualpay Disputes v0.5 API
  slug: qualpay-disputes-v0-5-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: API to allow automation of dispute reporting and responses.
  name: Qualpay Disputes v1.0 API
  slug: qualpay-disputes-v1-0-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Embedded Fields
  name: Qualpay Embedded Fields API
  slug: qualpay-embedded-fields-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: The Integrator API from Qualpay — 3 operation(s) for integrator.
  name: Qualpay Integrator API
  slug: qualpay-integrator-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Invoicing
  name: Qualpay Invoicing API
  slug: qualpay-invoicing-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Payee Vault
  name: Qualpay Payee Vault API
  slug: qualpay-payee-vault-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: The Payment Gateway API from Qualpay — 16 operation(s) for payment gateway.
  name: Qualpay Payment Gateway API
  slug: qualpay-payment-gateway-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Recurring Billing
  name: Qualpay Recurring Billing API
  slug: qualpay-recurring-billing-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Reporting
  name: Qualpay Reporting API
  slug: qualpay-reporting-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: The Token API from Qualpay — 3 operation(s) for token.
  name: Qualpay Token API
  slug: qualpay-token-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: The Transaction API from Qualpay — 1 operation(s) for transaction.
  name: Qualpay Transaction API
  slug: qualpay-transaction-api
- baseURL: https://api-test.qualpay.com
  baseurl_source: declared
  description: Webhooks
  name: Qualpay Webhooks API
  slug: qualpay-webhooks-api
artifact_total: 82
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qualpay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qualpay.com/legal/terms-and-conditions-v2
- group: start
  title: ''
  type: GettingStarted
  url: https://help.qualpay.com/help/my-account
- group: agent
  href: https://artifacts.apis.io/qualpay/agentic-access/qualpay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/qualpay-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/qualpay/rules/qualpay-rules.yml
  title: ''
  type: Spectral
  url: rules/qualpay-rules.yml
- group: design
  href: https://artifacts.apis.io/qualpay/json-ld/qualpay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qualpay-context.jsonld
- group: design
  href: https://artifacts.apis.io/qualpay/vocabulary/qualpay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qualpay-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/qualpay/data-model/qualpay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qualpay-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.qualpay.com/security
- group: design
  href: https://artifacts.apis.io/qualpay/errors/qualpay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qualpay-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qualpay/conformance/qualpay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qualpay-conformance.yml
- group: agent
  href: https://artifacts.apis.io/qualpay/llms/qualpay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qualpay-llms.txt
- group: agent
  href: https://artifacts.apis.io/qualpay/well-known/qualpay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qualpay-well-known.yml
- group: other
  href: https://artifacts.apis.io/qualpay/hosts/qualpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qualpay-hosts.yml
- group: other
  href: https://artifacts.apis.io/qualpay/vendors/qualpay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qualpay-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app-test.qualpay.com/login/signup
- group: auth
  title: ''
  type: Security
  url: https://www.qualpay.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.qualpay.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qualpay
- group: auth
  href: https://artifacts.apis.io/qualpay/authentication/qualpay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qualpay-authentication.yml
- group: auth
  href: https://artifacts.apis.io/qualpay/security/qualpay-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/qualpay-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/qualpay/security/qualpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qualpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qualpay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.qualpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.qualpay.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.qualpay.com/reference
- group: operate
  title: ''
  type: Support
  url: https://www.qualpay.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.qualpay.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qualpay.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/qualpay/workspace/qualpay-api
coverage:
  checked: '2026-10-26'
  detail: Qualpay provides markdown documentation via llms.txt but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://developer.qualpay.com/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Qualpay provides a comprehensive payments platform offering embedded finance services, customizable checkout, recurring billing, virtual terminal, ACH/eCheck processing, and industry‑specific solutions for nonprofits, utilities, energy, waste management, propane, e‑commerce, B2B and home services. Their developer hub offers hosted APIs, webhooks, sandbox testing, detailed documentation, and sample code to integrate payment processing quickly and securely.
json_schemas:
- name: AddAppRequest-2
  property_count: 3
  slug: qualpay-add-app-request-2
- name: AddBillingCardRequest
  property_count: 22
  slug: qualpay-add-billing-card-request
- name: AddCustomerRequest
  property_count: 13
  slug: qualpay-add-customer-request
- name: AddPayeeRequest
  property_count: 7
  slug: qualpay-add-payee-request
- name: AddRecurringPlanRequest
  property_count: 20
  slug: qualpay-add-recurring-plan-request
- name: AddShippingAddressRequest
  property_count: 13
  slug: qualpay-add-shipping-address-request
- name: AddSubscriptionRequest
  property_count: 21
  slug: qualpay-add-subscription-request
- name: AusCancelResponse
  property_count: 3
  slug: qualpay-aus-cancel-response
- name: AusHoldRequest
  property_count: 3
  slug: qualpay-aus-hold-request
- name: AusListDetailResponse
  property_count: 5
  slug: qualpay-aus-list-detail-response
- name: AusListSummaryResponse
  property_count: 5
  slug: qualpay-aus-list-summary-response
- name: AusReleaseRequest
  property_count: 3
  slug: qualpay-aus-release-request
- name: AusUpdatedResponse
  property_count: 5
  slug: qualpay-aus-updated-response
- name: BrowseAppsResult-2
  property_count: 5
  slug: qualpay-browse-apps-result-2
- name: BrowseSalesRepsResult-2
  property_count: 5
  slug: qualpay-browse-sales-reps-result-2
- name: CancelCheckoutResponse
  property_count: 2
  slug: qualpay-cancel-checkout-response
- name: CheckoutLinkResponse
  property_count: 3
  slug: qualpay-checkout-link-response
- name: CheckoutRequest
  property_count: 19
  slug: qualpay-checkout-request
- name: CheckoutResponse
  property_count: 3
  slug: qualpay-checkout-response
- name: CorrespondingTransactionResponse
  property_count: 5
  slug: qualpay-corresponding-transaction-response
- name: CreateInvoiceRequest
  property_count: 17
  slug: qualpay-create-invoice-request
- name: DisputeDetail
  property_count: 5
  slug: qualpay-dispute-detail
- name: DisputeResponse
  property_count: 5
  slug: qualpay-dispute-response
- name: EmailAppRequest
  property_count: 2
  slug: qualpay-email-app-request
- name: EmbeddedKeyResponse
  property_count: 3
  slug: qualpay-embedded-key-response
- name: GetAppResult-2
  property_count: 3
  slug: qualpay-get-app-result-2
- name: InvoiceBouncedResponse
  property_count: 5
  slug: qualpay-invoice-bounced-response
- name: InvoiceListResponse
  property_count: 5
  slug: qualpay-invoice-list-response
- name: InvoicePaymentListResponse
  property_count: 5
  slug: qualpay-invoice-payment-list-response
- name: InvoicePaymentRequest
  property_count: 5
  slug: qualpay-invoice-payment-request
- name: MerchantSettingsResponse
  property_count: 3
  slug: qualpay-merchant-settings-response
- name: NewAccountRequest
  property_count: 5
  slug: qualpay-new-account-request
- name: PayeeAccountResponse
  property_count: 5
  slug: qualpay-payee-account-response
- name: PayeeListResponse
  property_count: 5
  slug: qualpay-payee-list-response
- name: PGApiBatchCloseRequest
  property_count: 10
  slug: qualpay-pgapi-batch-close-request
- name: PGApiTokenizeRequest
  property_count: 25
  slug: qualpay-pgapi-tokenize-request
- name: PGApiTransactionRequest
  property_count: 54
  slug: qualpay-pgapi-transaction-request
- name: PGApiTransactionResponse
  property_count: 12
  slug: qualpay-pgapi-transaction-response
- name: PGApiVerifyRequest
  property_count: 30
  slug: qualpay-pgapi-verify-request
- name: PGApiVerifyResponse
  property_count: 10
  slug: qualpay-pgapi-verify-response
- name: QPApiListResponse
  property_count: 5
  slug: qualpay-qpapi-list-response
- name: QPApiResponse
  property_count: 3
  slug: qualpay-qpapi-response
- name: RecurringPlanListResponse
  property_count: 5
  slug: qualpay-recurring-plan-list-response
- name: RotateKeyRequest
  property_count: 1
  slug: qualpay-rotate-key-request
- name: RotateKeyResponse
  property_count: 3
  slug: qualpay-rotate-key-response
- name: SettledTransactionResponse
  property_count: 5
  slug: qualpay-settled-transaction-response
- name: StatementDisputeResponse
  property_count: 5
  slug: qualpay-statement-dispute-response
- name: StatementReserveResponse
  property_count: 5
  slug: qualpay-statement-reserve-response
- name: StatementSettlementResponse
  property_count: 5
  slug: qualpay-statement-settlement-response
- name: SubscriptionLabelsListResponse
  property_count: 5
  slug: qualpay-subscription-labels-list-response
- name: TransactionRequestResponse
  property_count: 5
  slug: qualpay-transaction-request-response
- name: TransactionRequestResponse2
  property_count: 3
  slug: qualpay-transaction-request-response2
- name: UpdateBillingCardRequest
  property_count: 18
  slug: qualpay-update-billing-card-request
- name: UpdateCustomerRequest
  property_count: 10
  slug: qualpay-update-customer-request
- name: UpdateDraftRequest
  property_count: 13
  slug: qualpay-update-draft-request
- name: UpdatePayeeAccountRequest
  property_count: 5
  slug: qualpay-update-payee-account-request
- name: UpdatePayeeRequest
  property_count: 5
  slug: qualpay-update-payee-request
- name: UpdateRecurringPlanRequest
  property_count: 19
  slug: qualpay-update-recurring-plan-request
- name: UpdateShippingAddressRequest
  property_count: 14
  slug: qualpay-update-shipping-address-request
- name: UpdateSubscriptionRequest
  property_count: 8
  slug: qualpay-update-subscription-request
jsonld:
- class_count: 120
  name: Qualpay Context
  property_count: 268
  slug: qualpay-context
layout: provider
modified: '2026-10-26'
name: Qualpay
nav: Providers
network: true
overview: 'Qualpay publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Updater API, Application Boarding API, Checkout API, and 13 more. Tagged areas include Payments, Payment Processing, Merchant Services, B2B Payments, and Reporting.


  The Qualpay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qualpay''s developer surface includes getting-started guide, signup flow, authentication, documentation, API reference, support, engineering blog, and 23 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Qualpay API Rules
  rule_count: 66
  severity_counts:
    error: 50
    hint: 0
    info: 4
    warn: 12
  slug: qualpay-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 71.4
    developer_ergonomics: 36.9
    discoverability: 61.6
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/qualpay/qualpay-2026-11-03T141812.png
security:
- kind: authentication
  name: Qualpay Authentication
  slug: qualpay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qualpay Domain Security
  slug: qualpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Qualpay Trust Center
  slug: qualpay-trust-center
  summary_line: PCI DSS
slug: qualpay
tags:
- Payments
- Payment Processing
- Merchant Services
- B2B Payments
- Reporting
- Tokenization
website: https://www.qualpay.com/
---
