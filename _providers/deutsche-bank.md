---
access_model:
  confidence: high
  label: Free self-service sandbox; production access by reviewed go-live request and separate agreement
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://developer.db.com/faq
  - plans/deutsche-bank-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.2
  scored_at: '2026-09-16'
api_count: 36
apis:
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The alias API contains endpoints to add, update or delete aliases for means of payment.
  name: Deutsche Bank Alias API
  slug: deutsche-bank-alias-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Apple Pay™ API contains endpoints to initiate a payment session to perform credit card payment transactions based on Apple Pay™ payment information.
  name: Deutsche Bank Apple Pay API
  slug: deutsche-bank-apple-pay-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Authorization API from Deutsche Bank — 3 operation(s) for authorization.
  name: Deutsche Bank Authorization API
  slug: deutsche-bank-authorization-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The merchant's system has to implement this endpoint to receive callback requests.
  name: Deutsche Bank Callback API
  slug: deutsche-bank-callback-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to cancel existing SEPA Credit Transfers.
  name: Deutsche Bank Cancel SEPA Credit Transfers API
  slug: deutsche-bank-cancel-sepa-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to cancel existing SEPA Instant Credit Transfers.
  name: Deutsche Bank Cancel SEPA Instant Credit Transfers API
  slug: deutsche-bank-cancel-sepa-instant-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Cash account opening status API from Deutsche Bank — 1 operation(s) for cash account opening status.
  name: Deutsche Bank Cash account opening status API
  slug: deutsche-bank-cash-account-opening-status-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Lets you easily open cash accounts with Deutsche Bank, Postbank or norisbank on your customer's behalf.
  name: Deutsche Bank Cash Account Openings API
  slug: deutsche-bank-cash-account-openings-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Gives you an overview of all savings and current accounts of your customers. With this api, you can retrieve details such as IBAN, BIC or account type which you can then use for further inquiries on t
  name: Deutsche Bank Cash Accounts API
  slug: deutsche-bank-cash-accounts-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to create SEPA Credit Transfers. Both single and bulk payments are supported.
  name: Deutsche Bank Create SEPA Credit Transfers API
  slug: deutsche-bank-create-sepa-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to create SEPA Instant Credit Transfers. Both single and bulk payments are supported.
  name: Deutsche Bank Create SEPA Instant Credit Transfers API
  slug: deutsche-bank-create-sepa-instant-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Employee Share Plan Securities Account Opening API from Deutsche Bank — 2 operation(s) for employee share plan securities account opening.
  name: Deutsche Bank Employee Share Plan Securities Account Opening API
  slug: deutsche-bank-employee-share-plan-securities-account-opening-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The eScore API contains endpoints to minimize non-payment risk.
  name: Deutsche Bank E Score API
  slug: deutsche-bank-escore-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The ForgeRock Auth Tree API from Deutsche Bank — 1 operation(s) for forgerock auth tree.
  name: Deutsche Bank ForgeRock Auth Tree API
  slug: deutsche-bank-forgerock-auth-tree-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The ForgeRock OAuth API from Deutsche Bank — 2 operation(s) for forgerock oauth.
  name: Deutsche Bank ForgeRock OAuth API
  slug: deutsche-bank-forgerock-oauth-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The ForgeRock Session API from Deutsche Bank — 1 operation(s) for forgerock session.
  name: Deutsche Bank ForgeRock Session API
  slug: deutsche-bank-forgerock-session-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Forms API contains endpoints to initialize a form service interaction. It allows the merchant to redirect the customer to a customizable frontend page where the customer may enter sensitive paymen
  name: Deutsche Bank Forms API
  slug: deutsche-bank-forms-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to retrieve the details of SEPA Credit Transfers, both for single and bulk payments.
  name: Deutsche Bank Get details for SEPA Credit Transfers API
  slug: deutsche-bank-get-details-for-sepa-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to retrieve the details of SEPA Instant Credit Transfers, both for single and bulk payments.
  name: Deutsche Bank Get details for SEPA Instant Credit Transfers API
  slug: deutsche-bank-get-details-for-sepa-instant-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to retrieve the processing status of SEPA Credit Transfers, both for single and bulk payments.
  name: Deutsche Bank Get status for SEPA Credit Transfers API
  slug: deutsche-bank-get-status-for-sepa-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to retrieve the processing status of SEPA Instant Credit Transfers, both for single and bulk payments.
  name: Deutsche Bank Get status for SEPA Instant Credit Transfers API
  slug: deutsche-bank-get-status-for-sepa-instant-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to check the Verification of Payee (VoP) details for your SEPA Credit Transfers, whether you're making a single payment or a bulk transfer.
  name: Deutsche Bank Get VoP details for SEPA Credit Transfers API
  slug: deutsche-bank-get-vop-details-for-sepa-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints to check the Verification of Payee (VoP) details for your SEPA Instant Credit Transfers, whether you're making a single payment or a bulk transfer.
  name: Deutsche Bank Get VoP details for SEPA Instant Credit Transfers API
  slug: deutsche-bank-get-vop-details-for-sepa-instant-credit-transfers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Google Pay™ API contains endpoints to perform credit card payment transactions based on Google Pay™ payment information.
  name: Deutsche Bank Google Pay API
  slug: deutsche-bank-google-pay-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Headless 3-D Secure API contains endpoints to conduct headless 3-D Secure transactions.
  name: Deutsche Bank Headless 3-D Secure API
  slug: deutsche-bank-headless-3-d-secure-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The iFrame API contains an endpoint to initialize an iFrame interaction. It allows the merchant to embed specific elements of a frontend page into their own web page. Entry of sensitive data is done i
  name: Deutsche Bank I Frame API
  slug: deutsche-bank-iframe-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Information related operations.
  name: Deutsche Bank Info API
  slug: deutsche-bank-info-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Investment Order Subscription Api
  name: Deutsche Bank Investments Order Subscription API
  slug: deutsche-bank-investments-order-subscription-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Loan Offers API from Deutsche Bank — 5 operation(s) for loan offers.
  name: Deutsche Bank Loan Offers API
  slug: deutsche-bank-loan-offers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Managed Mandate API contains endpoints to work with managed mandates.
  name: Deutsche Bank Managed Mandate API
  slug: deutsche-bank-managed-mandate-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Change an existing order or preview a change of an existing order
  name: Deutsche Bank Order Change API
  slug: deutsche-bank-order-change-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Delete an existing order
  name: Deutsche Bank Order Delete API
  slug: deutsche-bank-order-delete-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Retrieve details on existing orders
  name: Deutsche Bank Order Details API
  slug: deutsche-bank-order-details-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Create an order or preview an order creation
  name: Deutsche Bank Order Entry API
  slug: deutsche-bank-order-entry-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Produce a PDF with the estimated expenses for an order execution or modification.
  name: Deutsche Bank Order Expense Report API
  slug: deutsche-bank-order-expense-report-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Password Encryption API from Deutsche Bank — 1 operation(s) for password encryption.
  name: Deutsche Bank Password Encryption API
  slug: deutsche-bank-password-encryption-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Payment API contains endpoints to add or modify payment transactions. When using the API, the merchant is only integrated to the API at the backend. All use cases are triggered via an API call. It
  name: Deutsche Bank Payment API
  slug: deutsche-bank-payment-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Payment Link API contains endpoints to prepare payments your customers can carry out later by using the provided link.
  name: Deutsche Bank Payment Link API
  slug: deutsche-bank-payment-link-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Processing Orders API from Deutsche Bank — 2 operation(s) for processing orders.
  name: Deutsche Bank Processing Orders API
  slug: deutsche-bank-processing-orders-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Verifies if the provided IBAN is reachable for an SEPA Instant Credit Transfer
  name: Deutsche Bank Reachability Status API
  slug: deutsche-bank-reachability-status-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Risk Management API contains endpoints to add and remove risk list entries and to calculate a risk score.
  name: Deutsche Bank Risk Management API
  slug: deutsche-bank-risk-management-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Use these endpoints for Second Factory Retry of existing SEPA Instant Credit Transfers.
  name: Deutsche Bank Second Factor Retry API
  slug: deutsche-bank-second-factor-retry-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Get static data on Securities
  name: Deutsche Bank Security Statics API
  slug: deutsche-bank-security-statics-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Get price information for a given security
  name: Deutsche Bank Support API
  slug: deutsche-bank-support-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Swaggers/OpenAPI repository
  name: Deutsche Bank Swaggers API
  slug: deutsche-bank-swaggers-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Tenants
  name: Deutsche Bank Tenants API
  slug: deutsche-bank-tenants-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Provides an easy and accurate way to prove recent income and rent payments to describe the financial situation of a customer.
  name: Deutsche Bank Transaction Analysis API
  slug: deutsche-bank-transaction-analysis-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Transaction Authorization API from Deutsche Bank — 4 operation(s) for transaction authorization.
  name: Deutsche Bank Transaction Authorization API
  slug: deutsche-bank-transaction-authorization-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Transactions Subscription Api
  name: Deutsche Bank Transaction Subscription API
  slug: deutsche-bank-transaction-subscription-api
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: Provides all transactions information from your customers' savings and current accounts for the last 13 months.
  name: Deutsche Bank Transactions API
  slug: deutsche-bank-transactions-api
artifact_total: 59
asyncapis:
- description: ''
  name: Deutsche Bank Webhooks
  slug: deutsche-bank-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.db.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.db.com/apidocumentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.db.com/apiexplorer
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.db.com/apidocumentation/apigettingstartedguide/introduction
- group: start
  title: ''
  type: SignUp
  url: https://developer.db.com/registration
- group: operate
  title: ''
  type: Support
  url: https://developer.db.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.db.com/faq
- group: company
  title: ''
  type: Blog
  url: https://developer.db.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.db.com/releasenotes
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/changelog/deutsche-bank-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/deutsche-bank-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.db.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.db.com/privacynotice
- group: company
  title: ''
  type: Partners
  url: https://developer.db.com/partnernetwork
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deutschebank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deutsche-bank
- group: company
  title: ''
  type: Website
  url: https://www.db.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/authentication/deutsche-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deutsche-bank-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/scopes/deutsche-bank-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/deutsche-bank-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/conventions/deutsche-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deutsche-bank-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/conventions/deutsche-bank-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/deutsche-bank-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/errors/deutsche-bank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deutsche-bank-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/errors/deutsche-bank-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/deutsche-bank-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/conformance/deutsche-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deutsche-bank-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/conformance/deutsche-bank-conformance.yml
  title: ''
  type: Compliance
  url: conformance/deutsche-bank-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/lifecycle/deutsche-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/deutsche-bank-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/sandbox/deutsche-bank-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/deutsche-bank-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/asyncapi/deutsche-bank-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/deutsche-bank-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/data-model/deutsche-bank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deutsche-bank-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/packages/deutsche-bank-packages.yml
  title: ''
  type: Packages
  url: packages/deutsche-bank-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/components/deutsche-bank-components.yml
  title: ''
  type: Components
  url: components/deutsche-bank-components.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/plans/deutsche-bank-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deutsche-bank-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/rate-limits/deutsche-bank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deutsche-bank-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/mcp/deutsche-bank-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deutsche-bank-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/llms/deutsche-bank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deutsche-bank-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/well-known/deutsche-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deutsche-bank-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/well-known/deutsche-bank-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deutsche-bank-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/security/deutsche-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deutsche-bank-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/security/deutsche-bank-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/deutsche-bank-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/security/deutsche-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deutsche-bank-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/finops/deutsche-bank-finops.yml
  title: ''
  type: FinOps
  url: finops/deutsche-bank-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-addresses-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-addresses-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-ageCertificate-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-ageCertificate-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-banking-cashAccountOpenings-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-banking-cashAccountOpenings-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-cashAccounts-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-cashAccounts-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-creditCardTransactions-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-creditCardTransactions-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-creditCards-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-creditCards-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-customerSolvency-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-customerSolvency-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-investments-assets-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-assets-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-investments-earningTransactions-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-earningTransactions-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-investments-espSecuritiesAccounts-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-espSecuritiesAccounts-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-investments-orders-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-orders-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-investments-performances-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-performances-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-investments-reports-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-reports-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-investments-securityAccounts-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-securityAccounts-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-investments-securityTransactions-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-securityTransactions-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-loanOffers-privatebanking-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-loanOffers-privatebanking-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-loanOffers-privatebanking-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-loanOffers-privatebanking-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-partners-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-partners-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-payments-sepaInstantCreditTransfer-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-payments-sepaInstantCreditTransfer-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-processingOrders-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-processingOrders-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-processingOrders-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-processingOrders-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-sepaCreditTransfer-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-sepaCreditTransfer-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-sepaDirectDebit-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-sepaDirectDebit-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-subscriptions-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-subscriptions-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-swaggers-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-swaggers-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-transactionAnalysis-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-transactionAnalysis-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-transactionAuthorization-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-transactionAuthorization-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-transactions-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-transactions-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-dbapi-verifyCustomer-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-verifyCustomer-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-merchant-solution-callback-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-callback-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-merchant-solution-callback-v2_1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-callback-v2_1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-merchant-solution-security-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-security-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-merchant-solution-security-v2_1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-security-v2_1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-merchant-solution-services-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-services-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-merchant-solution-services-v2.1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-services-v2.1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/overlays/deutsche-bank-oneid-fakerock-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-oneid-fakerock-v1-overlay.yaml
created: '2025-02-08'
description: 'Deutsche Bank is a global financial institution headquartered in Frankfurt, providing retail, corporate and investment banking, asset management and wealth management. Its developer programme - dbAPI, published at developer.db.com - goes well beyond the PSD2 regulatory minimum: 36 first-party OpenAPI 3.0.x contracts covering 195 operations across banking, cards, payments, investments, lending, onboarding, reference data and merchant acquiring, all retrievable from Deutsche Bank''s own public swagger catalogue. The same contracts serve three tenants - Deutsche Bank, norisbank and Postbank. Access is OAuth 2.0 / OpenID Connect with 42 published scopes, PSD2 strong customer authentication exposed as its own API, a free self-service simulation gateway with persona-based test users, and a reviewed go-live process for production data.'
finops:
- name: Deutsche Bank Finops
  service_category: API
  slug: deutsche-bank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deutsche-bank.png
layout: provider
mcp_servers:
- description: Deutsche Bank ships NO Model Context Protocol server. This is a DERIVED candidate tool surface, computed from the read-safe operations in Deutsche Bank's own published OpenAPI contracts so the shape o
  name: Derived candidate tool surface (no server ships)
  slug: derived-candidate-tool-surface-no-server-ships
modified: '2026-09-06'
name: Deutsche Bank
nav: Providers
network: true
overview: 'Deutsche Bank publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Alias API, Apple Pay API, Authorization API, and 47 more. Tagged areas include Banking, Financial, Wealth Management, Open Banking, and PSD2.


  The Deutsche Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Deutsche Bank''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 70 more developer resources.'
plans:
- name: Deutsche Bank Plans Pricing
  plan_count: 0
  slug: deutsche-bank-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Deutsche Bank Rate Limits
  slug: deutsche-bank-rate-limits
scopes:
- name: Deutsche Bank Scopes
  scope_count: 0
  slug: deutsche-bank-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 65.0
    developer_ergonomics: 37.5
    discoverability: 63.0
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 51.8
  provenance:
    conformance: derived
    contracts:
      callable: 26.5
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 84.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/screenshots/deutsche-bank-2026-06-20T175943.png
security:
- kind: authentication
  name: Deutsche Bank Authentication
  slug: deutsche-bank-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Deutsche Bank Domain Security
  slug: deutsche-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deutsche Bank Vulnerability Disclosure
  slug: deutsche-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deutsche-bank
tags:
- Banking
- Financial
- Wealth Management
- Open Banking
- PSD2
- Payments
- SEPA
- Investment
- Credit Cards
- Merchant Solutions
- Germany
- Financial-Services
website: https://www.db.com/
---
