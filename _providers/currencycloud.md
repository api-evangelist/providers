---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Currencycloud Agentic Access
  operation_count: 111
  slug: currencycloud-agentic-access
  summary_line: 111 operations · 51 acting
api_count: 2
apis:
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Account Usage API from Currencycloud — 1 operation(s) for account usage.
  name: Currencycloud Account Usage API
  slug: currencycloud-account-usage-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create, search and update your Currencycloud account and any associated sub-accounts. Also provides you with the ability to use your own reference IDs for easy reconciliation with your internal system
  name: Currencycloud Accounts API
  slug: currencycloud-accounts-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Authenticate to gain access to the API. Log in to your Currencycloud account using your API Key and log out to terminate your session.
  name: Currencycloud Authenticate API
  slug: currencycloud-authenticate-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Provides access to view balance information. View the balances that you currently hold in different currencies on your Currencycloud account.
  name: Currencycloud Balances API
  slug: currencycloud-balances-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create, search and manage the list of individuals or companies that you send payments to.
  name: Currencycloud Beneficiaries API
  slug: currencycloud-beneficiaries-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Business Information API from Currencycloud — 1 operation(s) for business information.
  name: Currencycloud Business Information API
  slug: currencycloud-business-information-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create, search and manage the list of users that have access in your Currencycloud account or associated sub-accounts.
  name: Currencycloud Contacts API
  slug: currencycloud-contacts-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Find, retrieve and create a live currency conversion. You can also create and manage the live conversion of funds between two currencies.
  name: Currencycloud Conversions API
  slug: currencycloud-conversions-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Country API from Currencycloud — 2 operation(s) for country.
  name: Currencycloud Country API
  slug: currencycloud-country-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Currency API from Currencycloud — 1 operation(s) for currency.
  name: Currencycloud Currency API
  slug: currencycloud-currency-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Requests that are only available in the Demo environment.
  name: Currencycloud Demo API
  slug: currencycloud-demo-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Document Images API from Currencycloud — 2 operation(s) for document images.
  name: Currencycloud Document Images API
  slug: currencycloud-document-images-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Documents API from Currencycloud — 2 operation(s) for documents.
  name: Currencycloud Documents API
  slug: currencycloud-documents-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Form API from Currencycloud — 3 operation(s) for form.
  name: Currencycloud Form API
  slug: currencycloud-form-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Find funding accounts that can be used to settle and collect funds in each available currency.
  name: Currencycloud Funding API
  slug: currencycloud-funding-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: View information relating to the 'payer' for a payment that has been initiated through the platform.
  name: Currencycloud Payers API
  slug: currencycloud-payers-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create, search, manage and action all of your domestic and international payments through this API.
  name: Currencycloud Payments API
  slug: currencycloud-payments-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The People API from Currencycloud — 2 operation(s) for people.
  name: Currencycloud People API
  slug: currencycloud-people-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create new quotes to use for held rates conversions.
  name: Currencycloud Quotes API
  slug: currencycloud-quotes-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Super fast real-time access to live foreign exchange rates through the Currencycloud platform.
  name: Currencycloud Rates API
  slug: currencycloud-rates-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Easy access to view important data relevant to your Currencycloud account including beneficiary details, conversion dates, available currencies, payer required details, payment dates and settlement de
  name: Currencycloud Reference API
  slug: currencycloud-reference-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Ability to create and retrieve reports.
  name: Currencycloud Reporting API
  slug: currencycloud-reporting-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Sender of funds.
  name: Currencycloud Sender API
  slug: currencycloud-sender-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Transaction Approval API from Currencycloud — 1 operation(s) for transaction approval.
  name: Currencycloud Transaction Approval API
  slug: currencycloud-transaction-approval-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: View balances and all pending and completed transactions in your Currencycloud account, as well as associated sub-account balances and transactions.
  name: Currencycloud Transactions API
  slug: currencycloud-transactions-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Search, retrieve and create a transfer of funds between your Currencycloud account and associated sub-accounts.
  name: Currencycloud Transfers API
  slug: currencycloud-transfers-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Manage withdrawal accounts
  name: Currencycloud Withdrawal Accounts API
  slug: currencycloud-withdrawal-accounts-api
artifact_total: 147
asyncapis:
- description: ''
  name: Currencycloud Webhooks
  slug: currencycloud-webhooks
collections:
- collection_type: postman
  name: api-onboarding Account Usage API
  slug: postman-currencycloud-account-usage-api
- collection_type: postman
  name: api-onboarding Account Usage Accounts API
  slug: postman-currencycloud-accounts-api
- collection_type: postman
  name: api-onboarding Account Usage Authenticate API
  slug: postman-currencycloud-authenticate-api
- collection_type: postman
  name: api-onboarding Account Usage Balances API
  slug: postman-currencycloud-balances-api
- collection_type: postman
  name: api-onboarding Account Usage Beneficiaries API
  slug: postman-currencycloud-beneficiaries-api
- collection_type: postman
  name: api-onboarding Account Usage Business Information API
  slug: postman-currencycloud-business-information-api
- collection_type: postman
  name: api-onboarding Account Usage Contacts API
  slug: postman-currencycloud-contacts-api
- collection_type: postman
  name: api-onboarding Account Usage Conversions API
  slug: postman-currencycloud-conversions-api
- collection_type: postman
  name: api-onboarding Account Usage Country API
  slug: postman-currencycloud-country-api
- collection_type: postman
  name: api-onboarding Account Usage Currency API
  slug: postman-currencycloud-currency-api
- collection_type: postman
  name: api-onboarding Account Usage Demo API
  slug: postman-currencycloud-demo-api
- collection_type: postman
  name: api-onboarding Account Usage Document Images API
  slug: postman-currencycloud-document-images-api
- collection_type: postman
  name: api-onboarding Account Usage Documents API
  slug: postman-currencycloud-documents-api
- collection_type: postman
  name: api-onboarding Account Usage Form API
  slug: postman-currencycloud-form-api
- collection_type: postman
  name: api-onboarding Account Usage Funding API
  slug: postman-currencycloud-funding-api
- collection_type: postman
  name: api-onboarding Account Usage Payers API
  slug: postman-currencycloud-payers-api
- collection_type: postman
  name: api-onboarding Account Usage Payments API
  slug: postman-currencycloud-payments-api
- collection_type: postman
  name: api-onboarding Account Usage People API
  slug: postman-currencycloud-people-api
- collection_type: postman
  name: api-onboarding Account Usage Quotes API
  slug: postman-currencycloud-quotes-api
- collection_type: postman
  name: api-onboarding Account Usage Rates API
  slug: postman-currencycloud-rates-api
- collection_type: postman
  name: api-onboarding Account Usage Reference API
  slug: postman-currencycloud-reference-api
- collection_type: postman
  name: api-onboarding Account Usage Reporting API
  slug: postman-currencycloud-reporting-api
- collection_type: postman
  name: api-onboarding Account Usage Sender API
  slug: postman-currencycloud-sender-api
- collection_type: postman
  name: api-onboarding Account Usage Transaction Approval API
  slug: postman-currencycloud-transaction-approval-api
- collection_type: postman
  name: api-onboarding Account Usage Transactions API
  slug: postman-currencycloud-transactions-api
- collection_type: postman
  name: api-onboarding Account Usage Transfers API
  slug: postman-currencycloud-transfers-api
- collection_type: postman
  name: api-onboarding Account Usage Withdrawal Accounts API
  slug: postman-currencycloud-withdrawal-accounts-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: api-onboarding Account Usage API
  slug: open-currencycloud-account-usage-api
- collection_type: open
  name: api-onboarding Account Usage Accounts API
  slug: open-currencycloud-accounts-api
- collection_type: open
  name: api-onboarding Account Usage Authenticate API
  slug: open-currencycloud-authenticate-api
- collection_type: open
  name: api-onboarding Account Usage Balances API
  slug: open-currencycloud-balances-api
- collection_type: open
  name: api-onboarding Account Usage Beneficiaries API
  slug: open-currencycloud-beneficiaries-api
- collection_type: open
  name: api-onboarding Account Usage Business Information API
  slug: open-currencycloud-business-information-api
- collection_type: open
  name: api-onboarding Account Usage Contacts API
  slug: open-currencycloud-contacts-api
- collection_type: open
  name: api-onboarding Account Usage Conversions API
  slug: open-currencycloud-conversions-api
- collection_type: open
  name: api-onboarding Account Usage Country API
  slug: open-currencycloud-country-api
- collection_type: open
  name: api-onboarding Account Usage Currency API
  slug: open-currencycloud-currency-api
- collection_type: open
  name: api-onboarding Account Usage Demo API
  slug: open-currencycloud-demo-api
- collection_type: open
  name: api-onboarding Account Usage Document Images API
  slug: open-currencycloud-document-images-api
- collection_type: open
  name: api-onboarding Account Usage Documents API
  slug: open-currencycloud-documents-api
- collection_type: open
  name: api-onboarding Account Usage Form API
  slug: open-currencycloud-form-api
- collection_type: open
  name: api-onboarding Account Usage Funding API
  slug: open-currencycloud-funding-api
- collection_type: open
  name: api-onboarding Account Usage Payers API
  slug: open-currencycloud-payers-api
- collection_type: open
  name: api-onboarding Account Usage Payments API
  slug: open-currencycloud-payments-api
- collection_type: open
  name: api-onboarding Account Usage People API
  slug: open-currencycloud-people-api
- collection_type: open
  name: api-onboarding Account Usage Quotes API
  slug: open-currencycloud-quotes-api
- collection_type: open
  name: api-onboarding Account Usage Rates API
  slug: open-currencycloud-rates-api
- collection_type: open
  name: api-onboarding Account Usage Reference API
  slug: open-currencycloud-reference-api
- collection_type: open
  name: api-onboarding Account Usage Reporting API
  slug: open-currencycloud-reporting-api
- collection_type: open
  name: api-onboarding Account Usage Sender API
  slug: open-currencycloud-sender-api
- collection_type: open
  name: api-onboarding Account Usage Transaction Approval API
  slug: open-currencycloud-transaction-approval-api
- collection_type: open
  name: api-onboarding Account Usage Transactions API
  slug: open-currencycloud-transactions-api
- collection_type: open
  name: api-onboarding Account Usage Transfers API
  slug: open-currencycloud-transfers-api
- collection_type: open
  name: api-onboarding Account Usage Withdrawal Accounts API
  slug: open-currencycloud-withdrawal-accounts-api
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/rules/currencycloud-rules.yml
  title: ''
  type: Spectral
  url: rules/currencycloud-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/json-ld/currencycloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/currencycloud-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/vocabulary/currencycloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/currencycloud-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/errors/currencycloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/currencycloud-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/hosts/currencycloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/currencycloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/vendors/currencycloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/currencycloud-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.currencycloud.com/legal/security
- group: company
  title: ''
  type: Blog
  url: https://blog.currencycloud.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/capabilities/currencycloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/currencycloud-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/overlays/currencycloud-reference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/currencycloud-reference-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/currencycloud/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.currencycloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.currencycloud.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.currencycloud.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.currencycloud.com/guides/getting-started/getting-started-with-the-api/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/authentication/currencycloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/currencycloud-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://developer.currencycloud.com/register-for-an-api-key/
- group: operate
  title: ''
  type: Support
  url: https://support.currencycloud.com/hc/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.currencycloud.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.visa.co.uk/legal/global-privacy-notice.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CurrencyCloud
- group: operate
  title: ''
  type: StatusPage
  url: https://status.currencycloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.currencycloud.com/guides/platform-specifics/deprecation-policy/
- group: build
  title: ''
  type: Postman
  url: https://github.com/CurrencyCloud/postman
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/packages/currencycloud-packages.yml
  title: ''
  type: SDKs
  url: packages/currencycloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/packages/currencycloud-packages.yml
  title: ''
  type: Packages
  url: packages/currencycloud-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/mcp/currencycloud-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/currencycloud-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/well-known/currencycloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/currencycloud-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/conformance/currencycloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/currencycloud-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/security/currencycloud-trust-center.yml
  title: ''
  type: Compliance
  url: security/currencycloud-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/security/currencycloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/currencycloud-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/errors/currencycloud-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/currencycloud-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/lifecycle/currencycloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/currencycloud-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/changelog/currencycloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/currencycloud-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/rate-limits/currencycloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/currencycloud-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/conventions/currencycloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/currencycloud-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/conventions/currencycloud-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/currencycloud-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/data-model/currencycloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/currencycloud-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/asyncapi/currencycloud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/currencycloud-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/sandbox/currencycloud-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/currencycloud-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/agentic-access/currencycloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/currencycloud-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/security/currencycloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/currencycloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.currencycloud.com
created: '2026-07-17'
description: 'Currencycloud is a cross-border payments and foreign-exchange platform, part of Visa, that provides a robust, predictable REST API for converting money between currencies, holding multi-currency balances, and making payments around the world. Its API v2 spans 18 domains — authentication, accounts and sub-accounts, balances, beneficiaries, contacts, conversions, funding, payers, payments, quotes, rates, reference data, reporting, transactions, transfers and withdrawal accounts — and lets businesses dynamically register sub-accounts to offer white-labelled money-transfer services to their own customers. Currencycloud is an FCA-authorised Electronic Money Institution (registration #900199) and a FinCEN-registered money transmitter, and publishes official SDKs for JavaScript, Python, Ruby, PHP, Java and .NET.'
image: https://raw.githubusercontent.com/CurrencyCloud/currencycloud-swagger/master/apps/website/public/images/introduction-header.png
json_schemas:
- name: AcceptTermsResponse
  property_count: 2
  slug: currencycloud-accept-terms-response
- name: AccountComplianceSettings
  property_count: 18
  slug: currencycloud-account-compliance-settings
- name: AccountPaymentChargesSetting
  property_count: 5
  slug: currencycloud-account-payment-charges-setting
- name: Account
  property_count: 28
  slug: currencycloud-account
- name: account_usage
  property_count: 16
  slug: currencycloud-account-usage
- name: AuthenticationToken
  property_count: 1
  slug: currencycloud-authentication-token
- name: Balance
  property_count: 6
  slug: currencycloud-balance
- name: BankDetails
  property_count: 13
  slug: currencycloud-bank-details
- name: BeneficiaryAccountVerificationResult
  property_count: 5
  slug: currencycloud-beneficiary-account-verification-result
- name: BeneficiaryRequirements
  property_count: 19
  slug: currencycloud-beneficiary-requirements
- name: Beneficiary
  property_count: 36
  slug: currencycloud-beneficiary
- name: business_information
  property_count: 17
  slug: currencycloud-business-information
- name: Contact
  property_count: 16
  slug: currencycloud-contact
- name: ConversionCancellationQuote
  property_count: 3
  slug: currencycloud-conversion-cancellation-quote
- name: ConversionDateChange
  property_count: 8
  slug: currencycloud-conversion-date-change
- name: ConversionDates
  property_count: 7
  slug: currencycloud-conversion-dates
- name: ConversionProfitAndLoss
  property_count: 2
  slug: currencycloud-conversion-profit-and-loss
- name: Conversion
  property_count: 29
  slug: currencycloud-conversion
- name: ConversionSplitHistory
  property_count: 3
  slug: currencycloud-conversion-split-history
- name: create_account_usage_request
  property_count: 12
  slug: currencycloud-create-account-usage-request
- name: create_business_information_request
  property_count: 13
  slug: currencycloud-create-business-information-request
- name: create_document_image_request
  property_count: 2
  slug: currencycloud-create-document-image-request
- name: create_document_request
  property_count: 2
  slug: currencycloud-create-document-request
- name: create_form_request
  property_count: 12
  slug: currencycloud-create-form-request
- name: create_person_request
  property_count: 14
  slug: currencycloud-create-person-request
- name: document_image
  property_count: 4
  slug: currencycloud-document-image
- name: document
  property_count: 5
  slug: currencycloud-document
- name: document_with_image_ids
  property_count: 8
  slug: currencycloud-document-with-image-ids
- name: form
  property_count: 18
  slug: currencycloud-form
- name: form_with_associations
  property_count: 21
  slug: currencycloud-form-with-associations
- name: FundingAccount
  property_count: 14
  slug: currencycloud-funding-account
- name: FundingTransaction
  property_count: 13
  slug: currencycloud-funding-transaction
- name: HeldRateQuote
  property_count: 19
  slug: currencycloud-held-rate-quote
- name: HMACKey
  property_count: 1
  slug: currencycloud-hmackey
- name: Pagination
  property_count: 8
  slug: currencycloud-pagination
- name: Payer
  property_count: 15
  slug: currencycloud-payer
- name: PaymentConfirmation
  property_count: 9
  slug: currencycloud-payment-confirmation
- name: PaymentDates
  property_count: 2
  slug: currencycloud-payment-dates
- name: PaymentDeliveryDate
  property_count: 6
  slug: currencycloud-payment-delivery-date
- name: PaymentFeeRule
  property_count: 6
  slug: currencycloud-payment-fee-rule
- name: PaymentFee
  property_count: 7
  slug: currencycloud-payment-fee
- name: Payment
  property_count: 31
  slug: currencycloud-payment
- name: PaymentTrackingInfo
  property_count: 6
  slug: currencycloud-payment-tracking-info
- name: person
  property_count: 18
  slug: currencycloud-person
- name: QuotePaymentFee
  property_count: 7
  slug: currencycloud-quote-payment-fee
- name: RateDetailed
  property_count: 14
  slug: currencycloud-rate-detailed
- name: RatesBasic
  property_count: 2
  slug: currencycloud-rates-basic
- name: ReportRequest
  property_count: 12
  slug: currencycloud-report-request
- name: Sender
  property_count: 10
  slug: currencycloud-sender
- name: SettlementAccount
  property_count: 14
  slug: currencycloud-settlement-account
- name: SimulateFunding
  property_count: 17
  slug: currencycloud-simulate-funding
- name: TopUpMarginBalance
  property_count: 3
  slug: currencycloud-top-up-margin-balance
- name: Transaction
  property_count: 17
  slug: currencycloud-transaction
- name: Transfer
  property_count: 14
  slug: currencycloud-transfer
- name: WithdrawalAccount
  property_count: 8
  slug: currencycloud-withdrawal-account
- name: WithdrawalPullFundsRequestDetails
  property_count: 5
  slug: currencycloud-withdrawal-pull-funds-request-details
jsonld:
- class_count: 120
  name: Currencycloud Context
  property_count: 314
  slug: currencycloud-context
layout: provider
modified: '2026-07-18'
name: Currencycloud
nav: Providers
network: true
overview: 'Currencycloud publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Usage API, Accounts API, Authenticate API, and 24 more. Tagged areas include Company, Fintech, Payments, Foreign Exchange, and Cross-Border Payments.


  The Currencycloud catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Currencycloud''s developer surface includes engineering blog, documentation, API reference, getting-started guide, authentication, signup flow, support, and 37 more developer resources.'
plans:
- name: Currencycloud Plans Pricing
  plan_count: 0
  slug: currencycloud-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 10
  name: Currencycloud Rate Limits
  slug: currencycloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Currencycloud API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 1
  slug: currencycloud-rules
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.6
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 69.0
    developer_ergonomics: 78.0
    discoverability: 66.1
    operational_transparency: 92.1
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 23.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/screenshots/currencycloud-2026-07-25T210947.png
security:
- kind: authentication
  name: Currencycloud Authentication
  slug: currencycloud-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Currencycloud Domain Security
  slug: currencycloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Currencycloud Trust Center
  slug: currencycloud-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27018, PCI DSS Level 1, SOC 1, SOC 2, SOC 3, FIPS, GDPR, UK DPA
slug: currencycloud
tags:
- Company
- Fintech
- Payments
- Foreign Exchange
- Cross-Border Payments
- Money Transfer
- Currency Conversion
- Banking
website: https://www.currencycloud.com
---
