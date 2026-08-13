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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Temenos Transact Agentic Access
  operation_count: 30
  slug: temenos-transact-agentic-access
  summary_line: 30 operations · 8 acting
api_count: 13
apis:
- description: APIs for Temenos Transact microservices including callback registry, configuration management, user entitlements, and service orchestration for building event-driven and composable banking application
  name: Temenos Transact Microservices APIs
  slug: temenos-transact-microservices-apis
- description: High-performance APIs built on the near real-time Analytics Data Store and Operational Data Store from Temenos Transact Data Hub, providing banking-specific analytical and operational data for reporti
  name: Temenos Transact Data Hub APIs
  slug: temenos-transact-data-hub-apis
- description: APIs built on the near real-time Operational Data Store from Temenos Transact Data Hub, presenting data in specific formats for operational and API use cases utilizing real-time data streams and ETL t
  name: Temenos Operational Data Store APIs
  slug: temenos-operational-data-store-apis
- description: Manage customer accounts created using the Arrangement Architecture including current accounts, savings accounts, corporate accounts, Islamic accounts, non-resident and minor accounts.
  name: Temenos Transact Accounts API
  slug: temenos-transact-accounts-api
- description: Manage payment beneficiaries including domestic and international beneficiary registration, validation, and maintenance.
  name: Temenos Transact Beneficiaries API
  slug: temenos-transact-beneficiaries-api
- description: Manage debit and credit card operations including card issuance, activation, blocking, and limit management.
  name: Temenos Transact Cards API
  slug: temenos-transact-cards-api
- description: Create, update, and manage customer profiles, contact details, KYC documentation, compliance records, communication preferences, and party relationships.
  name: Temenos Transact Customers API
  slug: temenos-transact-customers-api
- description: Manage deposit arrangements including term deposits, savings deposits, and fixed deposit products with maturity tracking and renewal capabilities.
  name: Temenos Transact Deposits API
  slug: temenos-transact-deposits-api
- description: Create and manage loan arrangements, credit facilities, repayment schedules, drawdowns, and loan lifecycle operations.
  name: Temenos Transact Loans API
  slug: temenos-transact-loans-api
- description: Process fund transfers, standing orders, direct debits, payment orders, sweeps, and cross-border payments. Includes payment validation, cost calculation, status tracking, and cancellation.
  name: Temenos Transact Payments API
  slug: temenos-transact-payments-api
- description: Browse the product catalog and retrieve product conditions, eligibility criteria, and arrangement details.
  name: Temenos Transact Products API
  slug: temenos-transact-products-api
- description: Access system-wide lookup and configuration data including currencies, countries, IBAN/BIC validation, interest rate tables, and balance type definitions.
  name: Temenos Transact Reference Data API
  slug: temenos-transact-reference-data-api
- description: Retrieve transaction history, statement details, and account activity records for all account types and arrangements.
  name: Temenos Transact Transactions API
  slug: temenos-transact-transactions-api
artifact_total: 178
collections:
- collection_type: open
  name: Temenos Transact Core Banking API
  slug: open-temenos-transact-core-banking
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/temenos-transact-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/temenos-transact-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/temenos-transact-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/temenos
- group: start
  title: ''
  type: Portal
  url: https://developer.temenos.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.temenos.com/article/sandbox-quick-guide
- group: docs
  title: ''
  type: Documentation
  url: https://developer.temenos.com/guides
- group: company
  title: ''
  type: Blog
  url: https://www.temenos.com/blog/the-modern-developer-portal/
- group: operate
  title: ''
  type: Community
  url: https://basecamp.temenos.com/s/
- group: start
  title: ''
  type: Signup
  url: https://tcsp-signup.temenos.com/signup/communityregistration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/temenostech
- group: company
  title: ''
  type: Website
  url: https://www.temenos.com/
- group: operate
  title: ''
  type: Support
  url: https://support.temenos.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.temenos.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.temenos.com/privacy-policy/
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/temenos-devex/temenos-essential-apis/documentation/sd6uv6m/temenos-essential-apis
created: '2024'
description: Core banking APIs from Temenos Transact, providing comprehensive banking functionality including accounts, transactions, payments, loans, and customer management.
examples:
- key_count: 10
  name: Temenos Transact Core Banking Account Balances Example
  slug: temenos-transact-core-banking-account-balances-example
- key_count: 0
  name: Temenos Transact Core Banking Account Balances Response Example
  slug: temenos-transact-core-banking-account-balances-response-example
- key_count: 0
  name: Temenos Transact Core Banking Account Details Response Example
  slug: temenos-transact-core-banking-account-details-response-example
- key_count: 16
  name: Temenos Transact Core Banking Account Example
  slug: temenos-transact-core-banking-account-example
- key_count: 2
  name: Temenos Transact Core Banking Account Update Request Example
  slug: temenos-transact-core-banking-account-update-request-example
- key_count: 1
  name: Temenos Transact Core Banking Accounts Response Example
  slug: temenos-transact-core-banking-accounts-response-example
- key_count: 7
  name: Temenos Transact Core Banking Address Example
  slug: temenos-transact-core-banking-address-example
- key_count: 1
  name: Temenos Transact Core Banking Beneficiaries Response Example
  slug: temenos-transact-core-banking-beneficiaries-response-example
- key_count: 2
  name: Temenos Transact Core Banking Beneficiary Create Request Example
  slug: temenos-transact-core-banking-beneficiary-create-request-example
- key_count: 12
  name: Temenos Transact Core Banking Beneficiary Example
  slug: temenos-transact-core-banking-beneficiary-example
- key_count: 0
  name: Temenos Transact Core Banking Beneficiary Response Example
  slug: temenos-transact-core-banking-beneficiary-response-example
- key_count: 0
  name: Temenos Transact Core Banking Card Details Response Example
  slug: temenos-transact-core-banking-card-details-response-example
- key_count: 10
  name: Temenos Transact Core Banking Card Example
  slug: temenos-transact-core-banking-card-example
- key_count: 1
  name: Temenos Transact Core Banking Cards Response Example
  slug: temenos-transact-core-banking-cards-response-example
- key_count: 1
  name: Temenos Transact Core Banking Countries Response Example
  slug: temenos-transact-core-banking-countries-response-example
- key_count: 5
  name: Temenos Transact Core Banking Country Example
  slug: temenos-transact-core-banking-country-example
- key_count: 1
  name: Temenos Transact Core Banking Currencies Response Example
  slug: temenos-transact-core-banking-currencies-response-example
- key_count: 7
  name: Temenos Transact Core Banking Currency Example
  slug: temenos-transact-core-banking-currency-example
- key_count: 2
  name: Temenos Transact Core Banking Customer Create Request Example
  slug: temenos-transact-core-banking-customer-create-request-example
- key_count: 0
  name: Temenos Transact Core Banking Customer Details Response Example
  slug: temenos-transact-core-banking-customer-details-response-example
- key_count: 22
  name: Temenos Transact Core Banking Customer Example
  slug: temenos-transact-core-banking-customer-example
- key_count: 2
  name: Temenos Transact Core Banking Customer Update Request Example
  slug: temenos-transact-core-banking-customer-update-request-example
- key_count: 1
  name: Temenos Transact Core Banking Customers Response Example
  slug: temenos-transact-core-banking-customers-response-example
- key_count: 0
  name: Temenos Transact Core Banking Deposit Details Response Example
  slug: temenos-transact-core-banking-deposit-details-response-example
- key_count: 14
  name: Temenos Transact Core Banking Deposit Example
  slug: temenos-transact-core-banking-deposit-example
- key_count: 1
  name: Temenos Transact Core Banking Deposits Response Example
  slug: temenos-transact-core-banking-deposits-response-example
- key_count: 2
  name: Temenos Transact Core Banking Error Response Example
  slug: temenos-transact-core-banking-error-response-example
- key_count: 16
  name: Temenos Transact Core Banking Fund Transfer Example
  slug: temenos-transact-core-banking-fund-transfer-example
- key_count: 2
  name: Temenos Transact Core Banking Fund Transfer Request Example
  slug: temenos-transact-core-banking-fund-transfer-request-example
- key_count: 0
  name: Temenos Transact Core Banking Fund Transfer Response Example
  slug: temenos-transact-core-banking-fund-transfer-response-example
- key_count: 1
  name: Temenos Transact Core Banking Iban Validation Response Example
  slug: temenos-transact-core-banking-iban-validation-response-example
- key_count: 0
  name: Temenos Transact Core Banking Loan Details Response Example
  slug: temenos-transact-core-banking-loan-details-response-example
- key_count: 17
  name: Temenos Transact Core Banking Loan Example
  slug: temenos-transact-core-banking-loan-example
- key_count: 1
  name: Temenos Transact Core Banking Loans Response Example
  slug: temenos-transact-core-banking-loans-response-example
- key_count: 3
  name: Temenos Transact Core Banking Pagination Info Example
  slug: temenos-transact-core-banking-pagination-info-example
- key_count: 19
  name: Temenos Transact Core Banking Payment Order Example
  slug: temenos-transact-core-banking-payment-order-example
- key_count: 2
  name: Temenos Transact Core Banking Payment Order Request Example
  slug: temenos-transact-core-banking-payment-order-request-example
- key_count: 0
  name: Temenos Transact Core Banking Payment Order Response Example
  slug: temenos-transact-core-banking-payment-order-response-example
- key_count: 1
  name: Temenos Transact Core Banking Payment Orders Response Example
  slug: temenos-transact-core-banking-payment-orders-response-example
- key_count: 9
  name: Temenos Transact Core Banking Product Example
  slug: temenos-transact-core-banking-product-example
- key_count: 1
  name: Temenos Transact Core Banking Products Response Example
  slug: temenos-transact-core-banking-products-response-example
- key_count: 4
  name: Temenos Transact Core Banking Response Header Example
  slug: temenos-transact-core-banking-response-header-example
- key_count: 13
  name: Temenos Transact Core Banking Standing Order Example
  slug: temenos-transact-core-banking-standing-order-example
- key_count: 2
  name: Temenos Transact Core Banking Standing Order Request Example
  slug: temenos-transact-core-banking-standing-order-request-example
- key_count: 0
  name: Temenos Transact Core Banking Standing Order Response Example
  slug: temenos-transact-core-banking-standing-order-response-example
- key_count: 1
  name: Temenos Transact Core Banking Standing Orders Response Example
  slug: temenos-transact-core-banking-standing-orders-response-example
- key_count: 18
  name: Temenos Transact Core Banking Transaction Example
  slug: temenos-transact-core-banking-transaction-example
- key_count: 1
  name: Temenos Transact Core Banking Transactions Response Example
  slug: temenos-transact-core-banking-transactions-response-example
features:
- description: Modular, component-based framework enabling reusable product components across retail, corporate, treasury, wealth, and Islamic banking.
  name: Arrangement Architecture
- description: Full support for multi-currency accounts, payments, and exchange rate management with ISO 4217 compliance.
  name: Multi-Currency Support
- description: Built-in customer verification, AML checks, and compliance tracking for regulatory requirements.
  name: KYC and AML Compliance
- description: Support for SEPA, SWIFT, ACH, RTGS, and domestic clearing payment types with real-time processing.
  name: Real-Time Payments
- description: Configurable product catalog with conditions, eligibility criteria, and arrangement details for banking products.
  name: Product Catalog
finops:
- name: Temenos Transact Finops
  service_category: Banking Software
  slug: temenos-transact-finops
image: https://www.temenos.com/wp-content/uploads/2023/01/temenos-logo.svg
json_schemas:
- name: AccountBalancesResponse
  property_count: 0
  slug: temenos-transact-core-banking-account-balances-response
- name: AccountBalances
  property_count: 10
  slug: temenos-transact-core-banking-account-balances
- name: AccountDetailsResponse
  property_count: 0
  slug: temenos-transact-core-banking-account-details-response
- name: Account
  property_count: 16
  slug: temenos-transact-core-banking-account
- name: AccountUpdateRequest
  property_count: 2
  slug: temenos-transact-core-banking-account-update-request
- name: AccountsResponse
  property_count: 1
  slug: temenos-transact-core-banking-accounts-response
- name: Address
  property_count: 7
  slug: temenos-transact-core-banking-address
- name: BeneficiariesResponse
  property_count: 1
  slug: temenos-transact-core-banking-beneficiaries-response
- name: BeneficiaryCreateRequest
  property_count: 2
  slug: temenos-transact-core-banking-beneficiary-create-request
- name: BeneficiaryResponse
  property_count: 0
  slug: temenos-transact-core-banking-beneficiary-response
- name: Beneficiary
  property_count: 12
  slug: temenos-transact-core-banking-beneficiary
- name: CardDetailsResponse
  property_count: 0
  slug: temenos-transact-core-banking-card-details-response
- name: Card
  property_count: 10
  slug: temenos-transact-core-banking-card
- name: CardsResponse
  property_count: 1
  slug: temenos-transact-core-banking-cards-response
- name: CountriesResponse
  property_count: 1
  slug: temenos-transact-core-banking-countries-response
- name: Country
  property_count: 5
  slug: temenos-transact-core-banking-country
- name: CurrenciesResponse
  property_count: 1
  slug: temenos-transact-core-banking-currencies-response
- name: Currency
  property_count: 7
  slug: temenos-transact-core-banking-currency
- name: CustomerCreateRequest
  property_count: 2
  slug: temenos-transact-core-banking-customer-create-request
- name: CustomerDetailsResponse
  property_count: 0
  slug: temenos-transact-core-banking-customer-details-response
- name: Customer
  property_count: 22
  slug: temenos-transact-core-banking-customer
- name: CustomerUpdateRequest
  property_count: 2
  slug: temenos-transact-core-banking-customer-update-request
- name: CustomersResponse
  property_count: 1
  slug: temenos-transact-core-banking-customers-response
- name: DepositDetailsResponse
  property_count: 0
  slug: temenos-transact-core-banking-deposit-details-response
- name: Deposit
  property_count: 14
  slug: temenos-transact-core-banking-deposit
- name: DepositsResponse
  property_count: 1
  slug: temenos-transact-core-banking-deposits-response
- name: ErrorResponse
  property_count: 2
  slug: temenos-transact-core-banking-error-response
- name: FundTransferRequest
  property_count: 2
  slug: temenos-transact-core-banking-fund-transfer-request
- name: FundTransferResponse
  property_count: 0
  slug: temenos-transact-core-banking-fund-transfer-response
- name: FundTransfer
  property_count: 16
  slug: temenos-transact-core-banking-fund-transfer
- name: IbanValidationResponse
  property_count: 1
  slug: temenos-transact-core-banking-iban-validation-response
- name: LoanDetailsResponse
  property_count: 0
  slug: temenos-transact-core-banking-loan-details-response
- name: Loan
  property_count: 17
  slug: temenos-transact-core-banking-loan
- name: LoansResponse
  property_count: 1
  slug: temenos-transact-core-banking-loans-response
- name: PaginationInfo
  property_count: 3
  slug: temenos-transact-core-banking-pagination-info
- name: PaymentOrderRequest
  property_count: 2
  slug: temenos-transact-core-banking-payment-order-request
- name: PaymentOrderResponse
  property_count: 0
  slug: temenos-transact-core-banking-payment-order-response
- name: PaymentOrder
  property_count: 19
  slug: temenos-transact-core-banking-payment-order
- name: PaymentOrdersResponse
  property_count: 1
  slug: temenos-transact-core-banking-payment-orders-response
- name: Product
  property_count: 9
  slug: temenos-transact-core-banking-product
- name: ProductsResponse
  property_count: 1
  slug: temenos-transact-core-banking-products-response
- name: ResponseHeader
  property_count: 4
  slug: temenos-transact-core-banking-response-header
- name: StandingOrderRequest
  property_count: 2
  slug: temenos-transact-core-banking-standing-order-request
- name: StandingOrderResponse
  property_count: 0
  slug: temenos-transact-core-banking-standing-order-response
- name: StandingOrder
  property_count: 13
  slug: temenos-transact-core-banking-standing-order
- name: StandingOrdersResponse
  property_count: 1
  slug: temenos-transact-core-banking-standing-orders-response
- name: Transaction
  property_count: 18
  slug: temenos-transact-core-banking-transaction
- name: TransactionsResponse
  property_count: 1
  slug: temenos-transact-core-banking-transactions-response
- name: Temenos Transact Banking Transaction
  property_count: 24
  slug: temenos-transaction
json_structures:
- name: Temenos Transact Core Banking Account Balances Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-account-balances-response-structure
- name: Temenos Transact Core Banking Account Balances Structure
  property_count: 10
  slug: temenos-transact-core-banking-account-balances-structure
- name: Temenos Transact Core Banking Account Details Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-account-details-response-structure
- name: Temenos Transact Core Banking Account Structure
  property_count: 16
  slug: temenos-transact-core-banking-account-structure
- name: Temenos Transact Core Banking Account Update Request Structure
  property_count: 2
  slug: temenos-transact-core-banking-account-update-request-structure
- name: Temenos Transact Core Banking Accounts Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-accounts-response-structure
- name: Temenos Transact Core Banking Address Structure
  property_count: 7
  slug: temenos-transact-core-banking-address-structure
- name: Temenos Transact Core Banking Beneficiaries Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-beneficiaries-response-structure
- name: Temenos Transact Core Banking Beneficiary Create Request Structure
  property_count: 2
  slug: temenos-transact-core-banking-beneficiary-create-request-structure
- name: Temenos Transact Core Banking Beneficiary Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-beneficiary-response-structure
- name: Temenos Transact Core Banking Beneficiary Structure
  property_count: 12
  slug: temenos-transact-core-banking-beneficiary-structure
- name: Temenos Transact Core Banking Card Details Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-card-details-response-structure
- name: Temenos Transact Core Banking Card Structure
  property_count: 10
  slug: temenos-transact-core-banking-card-structure
- name: Temenos Transact Core Banking Cards Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-cards-response-structure
- name: Temenos Transact Core Banking Countries Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-countries-response-structure
- name: Temenos Transact Core Banking Country Structure
  property_count: 5
  slug: temenos-transact-core-banking-country-structure
- name: Temenos Transact Core Banking Currencies Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-currencies-response-structure
- name: Temenos Transact Core Banking Currency Structure
  property_count: 7
  slug: temenos-transact-core-banking-currency-structure
- name: Temenos Transact Core Banking Customer Create Request Structure
  property_count: 2
  slug: temenos-transact-core-banking-customer-create-request-structure
- name: Temenos Transact Core Banking Customer Details Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-customer-details-response-structure
- name: Temenos Transact Core Banking Customer Structure
  property_count: 22
  slug: temenos-transact-core-banking-customer-structure
- name: Temenos Transact Core Banking Customer Update Request Structure
  property_count: 2
  slug: temenos-transact-core-banking-customer-update-request-structure
- name: Temenos Transact Core Banking Customers Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-customers-response-structure
- name: Temenos Transact Core Banking Deposit Details Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-deposit-details-response-structure
- name: Temenos Transact Core Banking Deposit Structure
  property_count: 14
  slug: temenos-transact-core-banking-deposit-structure
- name: Temenos Transact Core Banking Deposits Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-deposits-response-structure
- name: Temenos Transact Core Banking Error Response Structure
  property_count: 2
  slug: temenos-transact-core-banking-error-response-structure
- name: Temenos Transact Core Banking Fund Transfer Request Structure
  property_count: 2
  slug: temenos-transact-core-banking-fund-transfer-request-structure
- name: Temenos Transact Core Banking Fund Transfer Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-fund-transfer-response-structure
- name: Temenos Transact Core Banking Fund Transfer Structure
  property_count: 16
  slug: temenos-transact-core-banking-fund-transfer-structure
- name: Temenos Transact Core Banking Iban Validation Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-iban-validation-response-structure
- name: Temenos Transact Core Banking Loan Details Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-loan-details-response-structure
- name: Temenos Transact Core Banking Loan Structure
  property_count: 17
  slug: temenos-transact-core-banking-loan-structure
- name: Temenos Transact Core Banking Loans Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-loans-response-structure
- name: Temenos Transact Core Banking Pagination Info Structure
  property_count: 3
  slug: temenos-transact-core-banking-pagination-info-structure
- name: Temenos Transact Core Banking Payment Order Request Structure
  property_count: 2
  slug: temenos-transact-core-banking-payment-order-request-structure
- name: Temenos Transact Core Banking Payment Order Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-payment-order-response-structure
- name: Temenos Transact Core Banking Payment Order Structure
  property_count: 19
  slug: temenos-transact-core-banking-payment-order-structure
- name: Temenos Transact Core Banking Payment Orders Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-payment-orders-response-structure
- name: Temenos Transact Core Banking Product Structure
  property_count: 9
  slug: temenos-transact-core-banking-product-structure
- name: Temenos Transact Core Banking Products Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-products-response-structure
- name: Temenos Transact Core Banking Response Header Structure
  property_count: 4
  slug: temenos-transact-core-banking-response-header-structure
- name: Temenos Transact Core Banking Standing Order Request Structure
  property_count: 2
  slug: temenos-transact-core-banking-standing-order-request-structure
- name: Temenos Transact Core Banking Standing Order Response Structure
  property_count: 0
  slug: temenos-transact-core-banking-standing-order-response-structure
- name: Temenos Transact Core Banking Standing Order Structure
  property_count: 13
  slug: temenos-transact-core-banking-standing-order-structure
- name: Temenos Transact Core Banking Standing Orders Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-standing-orders-response-structure
- name: Temenos Transact Core Banking Transaction Structure
  property_count: 18
  slug: temenos-transact-core-banking-transaction-structure
- name: Temenos Transact Core Banking Transactions Response Structure
  property_count: 1
  slug: temenos-transact-core-banking-transactions-response-structure
jsonld:
- class_count: 31
  name: Temenos Transact Context
  property_count: 121
  slug: temenos-transact-context
- class_count: 0
  name: Temenos Transact Core Banking Context
  property_count: 0
  slug: temenos-transact-core-banking-context
layout: provider
modified: '2026-05-19'
name: Temenos Transact
nav: Providers
network: true
overview: 'Temenos Transact publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Beneficiaries API, Cards API, and 7 more. Tagged areas include Banking, Core Banking, Digital Banking, Enterprise, and Financial Services.


  The Temenos Transact catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Temenos Transact''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, signup flow, support, and 9 more developer resources.'
plans:
- name: Temenos Transact Plans Pricing
  plan_count: 1
  slug: temenos-transact-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 1
  name: Temenos Transact Rate Limits
  slug: temenos-transact-rate-limits
rules:
- name: Temenos Transact API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: temenos-transact-jsonschema-spectral-rules
- name: Temenos Transact API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: temenos-transact-spectral-rules
score:
  band: developing
  composite: 50.6
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 75.4
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/temenos-transact/refs/heads/main/screenshots/temenos-transact-2026-06-20T195053.png
security:
- kind: authentication
  name: Temenos Transact Authentication
  slug: temenos-transact-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Temenos Transact Domain Security
  slug: temenos-transact-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: temenos-transact
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
use_cases:
- description: Build digital banking apps with account management, transaction history, and payment initiation APIs.
  name: Digital Banking
- description: Enable third-party access to banking data and payment services through standardized APIs.
  name: Open Banking
- description: Automate loan application, credit assessment, and disbursement workflows through API integration.
  name: Loan Origination
- description: Streamline customer registration with KYC verification, account opening, and beneficiary setup.
  name: Customer Onboarding
website: https://www.temenos.com/
---
