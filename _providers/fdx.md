---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fdx Agentic Access
  operation_count: 27
  slug: fdx-agentic-access
  summary_line: 27 operations
api_count: 12
apis:
- description: 'RESTful endpoints for retrieving consumer transaction histories including pending and posted transactions, transaction categorization, merchant data, and transaction amounts across deposit, loan, and '
  name: FDX Transactions API
  slug: fdx-transactions-api
- description: RESTful endpoints for retrieving investment account data including holdings, positions, investment transactions, cost basis, and portfolio composition. Covers brokerage, retirement, and managed invest
  name: FDX Investment API
  slug: fdx-investment-api
- description: RESTful endpoints for retrieving insurance policy information including policy coverage details, premium schedules, claims history, and beneficiary data under the FDX insurance data cluster.
  name: FDX Insurance API
  slug: fdx-insurance-api
- description: RESTful endpoints for retrieving consumer tax data including tax document metadata and structured tax form data (1099s, W-2s, and related forms) as defined by the FDX US Tax Data specification and the
  name: FDX Tax API
  slug: fdx-tax-api
- description: RESTful endpoints introduced in FDX API v6.0 for retrieving permissioned payroll data including employment records, pay stubs, income verification, and direct deposit details, supporting lending and p
  name: FDX Payroll API
  slug: fdx-payroll-api
- description: 'RESTful endpoints implementing the FDX Consent API Behavioral Specification for managing user permissions and consent events. Enables data recipients to initiate consent, query active consent grants, '
  name: FDX Consent API
  slug: fdx-consent-api
- description: Search and view customer accounts
  name: Financial Data Exchange (FDX) Account Information API
  slug: fdx-account-information-api
- description: Search and retrieve account statements
  name: Financial Data Exchange (FDX) Account Statements API
  slug: fdx-account-statements-api
- description: Search and view account transactions
  name: Financial Data Exchange (FDX) Account Transactions API
  slug: fdx-account-transactions-api
- description: Search and view asset transfer networks networks
  name: Financial Data Exchange (FDX) Asset Transfer Networks Information API
  slug: fdx-asset-transfer-networks-information-api
- description: Search and view account payment networks
  name: Financial Data Exchange (FDX) Payment Networks Information API
  slug: fdx-payment-networks-information-api
- description: Search and view customer or customers
  name: Financial Data Exchange (FDX) Personal Information API
  slug: fdx-personal-information-api
artifact_total: 105
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fdx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fdx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fdx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fdx-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://financialdataexchange.org
- group: docs
  title: ''
  type: Documentation
  url: https://financialdataexchange.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.financialdataexchange.org
- group: start
  title: ''
  type: OnboardingPortal
  url: https://onboarding.financialdataexchange.org
- group: start
  title: ''
  type: Registry
  url: https://registry.financialdataexchange.org
- group: company
  title: ''
  type: Blog
  url: https://financialdataexchange.org/fdx-feed/
- group: other
  title: ''
  type: Membership
  url: https://financialdataexchange.org/about-fdx/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/plaid/core-exchange
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/financialdataexchange
- group: other
  title: ''
  type: X
  url: https://x.com/fdxapi
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@financialdataexchange
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://financialdataexchange.org/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://financialdataexchange.org/terms-of-use/
- group: commercial
  title: ''
  type: LicenseAgreement
  url: https://financialdataexchange.org/fdx-api-license-agreement/
- group: auth
  title: ''
  type: Authentication
  url: https://financialdataexchange.org
- group: commercial
  title: ''
  type: Plans
  url: plans/fdx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fdx-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fdx-finops.yml
created: '2026-06-13'
description: Financial Data Exchange (FDX) is a non-profit industry standards body operating in the US and Canada that produces the FDX API, a royalty-free REST standard for consumer-permissioned financial data sharing. The FDX API defines interoperable endpoints covering deposit accounts, loan accounts, investment accounts, insurance policies, tax data, payroll data, reward programs, and consent management, enabling data providers (financial institutions), data access platforms (aggregators), and data recipients (fintechs) to exchange consumer financial data without exposing user credentials. As of early 2026 over 130 million consumer accounts are connected via the FDX API across 200+ member organizations including Bank of America, Chase, Citi, Wells Fargo, Plaid, and MX. FDX API v6.5 is the current stable release.
finops:
- name: Fdx Finops
  service_category: ''
  slug: fdx-finops
graphqls:
- description: 'name: FDX GraphQL Schema'
  name: FDX GraphQL Schema
  slug: fdx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fdx.png
json_schemas:
- name: Account Category type
  property_count: 0
  slug: fdx-accountcategory
- name: Account Contact entity
  property_count: 4
  slug: fdx-accountcontact
- name: Account Descriptor entity
  property_count: 7
  slug: fdx-accountdescriptor
- name: Account Holder entity
  property_count: 0
  slug: fdx-accountholder
- name: Account Holder Relationship
  property_count: 0
  slug: fdx-accountholderrelationship
- name: Payment Networks entity
  property_count: 0
  slug: fdx-accountpaymentnetworklist
- name: Accounts entity
  property_count: 0
  slug: fdx-accounts
- name: Account Status
  property_count: 0
  slug: fdx-accountstatus
- name: Account entity
  property_count: 0
  slug: fdx-accountwithdescriptor
- name: Account With Details entity
  property_count: 0
  slug: fdx-accountwithdetails
- name: Address
  property_count: 7
  slug: fdx-address
- name: AnnuityAccountDescriptor
  property_count: 0
  slug: fdx-annuityaccountdescriptor
- name: AnnuityAccountType
  property_count: 0
  slug: fdx-annuityaccounttype
- name: Asset Transfer Network
  property_count: 6
  slug: fdx-assettransfernetwork
- name: Asset Transfer Networks
  property_count: 1
  slug: fdx-assettransfernetworklist
- name: Asset Transfer Type
  property_count: 0
  slug: fdx-assettransfertype
- name: CommercialAccountDescriptor
  property_count: 0
  slug: fdx-commercialaccountdescriptor
- name: CommercialAccountType
  property_count: 0
  slug: fdx-commercialaccounttype
- name: Content Types
  property_count: 0
  slug: fdx-contenttypes
- name: Currency entity
  property_count: 1
  slug: fdx-currency
- name: Customer entity.
  property_count: 1
  slug: fdx-customer
- name: Customer Name entity
  property_count: 0
  slug: fdx-customername
- name: Customer entity
  property_count: 1
  slug: fdx-customerwithname
- name: Date String
  property_count: 0
  slug: fdx-datestring
- name: DebitCreditMemo
  property_count: 0
  slug: fdx-debitcreditmemo
- name: Delivery Address
  property_count: 0
  slug: fdx-deliveryaddress
- name: Delivery Address Type
  property_count: 0
  slug: fdx-deliveryaddresstype
- name: Deposit Account Details entity
  property_count: 0
  slug: fdx-depositaccount
- name: DepositAccountDescriptor
  property_count: 0
  slug: fdx-depositaccountdescriptor
- name: DepositAccountType
  property_count: 0
  slug: fdx-depositaccounttype
- name: Deposit Transaction entity
  property_count: 0
  slug: fdx-deposittransaction
- name: DigitalWalletDescriptor
  property_count: 0
  slug: fdx-digitalwalletdescriptor
- name: DigitalWalletType
  property_count: 0
  slug: fdx-digitalwallettype
- name: FI Attribute entity
  property_count: 2
  slug: fdx-fiattribute
- name: HATEOAS Link
  property_count: 4
  slug: fdx-hateoaslink
- name: HATEOAS links array
  property_count: 0
  slug: fdx-hateoaslinks
- name: Holding entity
  property_count: 0
  slug: fdx-holding
- name: Holding SubType
  property_count: 0
  slug: fdx-holdingsubtype
- name: Holding Type
  property_count: 0
  slug: fdx-holdingtype
- name: HTTP action type
  property_count: 0
  slug: fdx-httpaction
- name: Identifier
  property_count: 0
  slug: fdx-identifier
- name: Individual name
  property_count: 4
  slug: fdx-individualname
- name: InsuranceAccountDescriptor
  property_count: 0
  slug: fdx-insuranceaccountdescriptor
- name: InsuranceAccountType
  property_count: 0
  slug: fdx-insuranceaccounttype
- name: Interest Rate Type
  property_count: 0
  slug: fdx-interestratetype
- name: InvestmentAccount
  property_count: 0
  slug: fdx-investmentaccount
- name: InvestmentAccountDescriptor
  property_count: 0
  slug: fdx-investmentaccountdescriptor
- name: InvestmentAccountType
  property_count: 0
  slug: fdx-investmentaccounttype
- name: Investment Transaction entity
  property_count: 0
  slug: fdx-investmenttransaction
- name: Investment Transaction Type
  property_count: 0
  slug: fdx-investmenttransactiontype
- name: ISO 3166 Country Code
  property_count: 0
  slug: fdx-iso3166countrycode
- name: ISO 4217 Code
  property_count: 0
  slug: fdx-iso4217code
- name: LineOfCreditAccount
  property_count: 0
  slug: fdx-lineofcreditaccount
- name: LineOfCreditAccountDescriptor
  property_count: 0
  slug: fdx-lineofcreditaccountdescriptor
- name: LineOfCreditAccountType
  property_count: 0
  slug: fdx-lineofcreditaccounttype
- name: Line-Of-Credit Transaction entity
  property_count: 0
  slug: fdx-lineofcredittransaction
- name: Line-Of-Credit Transaction Type
  property_count: 0
  slug: fdx-lineofcredittransactiontype
- name: Loan Account entity
  property_count: 0
  slug: fdx-loanaccount
- name: LoanAccountDescriptor
  property_count: 0
  slug: fdx-loanaccountdescriptor
- name: LoanAccountType
  property_count: 0
  slug: fdx-loanaccounttype
- name: Loan Transaction entity
  property_count: 0
  slug: fdx-loantransaction
- name: Loan Transaction Type
  property_count: 0
  slug: fdx-loantransactiontype
- name: Page Metadata
  property_count: 3
  slug: fdx-pagemetadata
- name: Paginated Array
  property_count: 1
  slug: fdx-paginatedarray
- name: Payment Network Supported by Account
  property_count: 5
  slug: fdx-paymentnetwork
- name: Payment Network Identifier Type
  property_count: 0
  slug: fdx-paymentnetworkidentifiertype
- name: Payment Network Type
  property_count: 0
  slug: fdx-paymentnetworktype
- name: Security ID entity
  property_count: 2
  slug: fdx-securityid
- name: Security ID Type
  property_count: 0
  slug: fdx-securityidtype
- name: Security Type
  property_count: 0
  slug: fdx-securitytype
- name: Statement entity
  property_count: 6
  slug: fdx-statement
- name: Statement PDF
  property_count: 0
  slug: fdx-statementpdf
- name: Statements entity
  property_count: 0
  slug: fdx-statements
- name: String 255
  property_count: 0
  slug: fdx-string255
- name: String 64
  property_count: 0
  slug: fdx-string64
- name: Telephone Network
  property_count: 0
  slug: fdx-telephonenetwork
- name: Telephone Number
  property_count: 5
  slug: fdx-telephonenumber
- name: Telephone Number Purpose
  property_count: 0
  slug: fdx-telephonenumberpurpose
- name: Timestamp
  property_count: 0
  slug: fdx-timestamp
- name: Transaction
  property_count: 14
  slug: fdx-transaction
- name: Transactions entity
  property_count: 0
  slug: fdx-transactions
- name: Transaction Status
  property_count: 0
  slug: fdx-transactionstatus
- name: Unit Type
  property_count: 0
  slug: fdx-unittype
jsonld:
- class_count: 28
  name: Fdx Context
  property_count: 4
  slug: fdx-context
layout: provider
modified: '2026-06-13'
name: Financial Data Exchange (FDX)
nav: Providers
network: true
overview: 'Financial Data Exchange (FDX) publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account Information API, Account Statements API, Account Transactions API, and 3 more. Tagged areas include Financial Data, Open Banking, Open Finance, Financial Data Exchange, and Consumer Permissioned.


  The Financial Data Exchange (FDX) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Financial Data Exchange (FDX)''s developer surface includes authentication, documentation, engineering blog, YouTube channel, and 18 more developer resources.'
plans:
- name: Fdx Plans Pricing
  plan_count: 4
  slug: fdx-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 0
  name: Fdx Rate Limits
  slug: fdx-rate-limits
rules:
- name: Financial Data Exchange (FDX) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fdx-jsonschema-spectral-rules
scopes:
- name: Fdx Scopes
  scope_count: 3
  slug: fdx-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  delta: -6.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.9
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fdx/refs/heads/main/screenshots/fdx-2026-06-20T181106.png
security:
- kind: authentication
  name: Fdx Authentication
  slug: fdx-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Fdx Domain Security
  slug: fdx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fdx
tags:
- Financial Data
- Open Banking
- Open Finance
- Financial Data Exchange
- Consumer Permissioned
- Account Data
- Transactions
- Investments
- Insurance
- Tax Data
- Payroll
- REST
- OAuth2
- FAPI
- CFPB 1033
website: https://financialdataexchange.org
---
