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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Sage Agentic Access
  operation_count: 25
  slug: sage-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 13
apis:
- description: Sage Intacct provides both REST and XML APIs for advanced financial management including multi-entity consolidations, project accounting, revenue recognition, and advanced reporting. The REST API uses
  name: Sage Intacct API
  slug: intacct
- description: Sage X3 provides a GraphQL API offering flexible data access for ERP operations including manufacturing, distribution, procurement, finance, and CRM. Supports SOAP API for legacy integrations. Targete
  name: Sage X3 API
  slug: sage-x3
- description: Sage 200 API provides REST access to Sage 200 Standard and Professional business management data including customers, suppliers, stock, sales orders, purchase orders, nominal ledger, bank reconciliati
  name: Sage 200 API
  slug: sage-200
- description: Sage 50 Accounts API enables desktop accounting integration for UK small businesses. Provides access to accounts, transactions, customers, suppliers, products, and financial data within Sage 50 Accoun
  name: Sage 50 Accounts API
  slug: sage-50
- description: Bank account and transaction management
  name: Sage Bank Accounts API
  slug: sage-bank-accounts-api
- description: Business settings and configuration
  name: Sage Business API
  slug: sage-business-api
- description: Customer and supplier contact management
  name: Sage Contacts API
  slug: sage-contacts-api
- description: Chart of accounts and ledger management
  name: Sage Ledger Accounts API
  slug: sage-ledger-accounts-api
- description: Customer and supplier payment recording
  name: Sage Payments API
  slug: sage-payments-api
- description: Product and service catalog management
  name: Sage Products API
  slug: sage-products-api
- description: Purchase invoice and supplier bill management
  name: Sage Purchase Invoices API
  slug: sage-purchase-invoices-api
- description: Sales invoice creation and management
  name: Sage Sales Invoices API
  slug: sage-sales-invoices-api
- description: Tax rate configuration
  name: Sage Tax Rates API
  slug: sage-tax-rates-api
artifact_total: 85
asyncapis:
- description: AsyncAPI 2.6 description of the documented webhook / event surface across Sage developer products. Sage's webhook story is fragmented across product lines and only a subset of products publish a webho
  name: Sage Webhooks
  slug: sage-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sage Accounting API
  slug: open-sage-accounting
- collection_type: open
  name: Sage Accounting Bank Accounts API
  slug: open-sage-bank-accounts-api
- collection_type: open
  name: Sage Accounting Bank Accounts Business API
  slug: open-sage-business-api
- collection_type: open
  name: Sage Accounting Bank Accounts Contacts API
  slug: open-sage-contacts-api
- collection_type: open
  name: Sage Accounting Bank Accounts Ledger Accounts API
  slug: open-sage-ledger-accounts-api
- collection_type: open
  name: Sage Accounting Bank Accounts Payments API
  slug: open-sage-payments-api
- collection_type: open
  name: Sage Accounting Bank Accounts Products API
  slug: open-sage-products-api
- collection_type: open
  name: Sage Accounting Bank Accounts Purchase Invoices API
  slug: open-sage-purchase-invoices-api
- collection_type: open
  name: Sage Accounting Bank Accounts Sales Invoices API
  slug: open-sage-sales-invoices-api
- collection_type: open
  name: Sage Accounting Bank Accounts Tax Rates API
  slug: open-sage-tax-rates-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sage-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sage-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sage-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sage-software
- group: start
  title: ''
  type: Portal
  url: https://developer.sage.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sage.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.sage.com/accounting/guides/concepts/authentication
- group: start
  title: ''
  type: Sandbox
  url: https://developer.sage.com/accounting/guides/test-drive/
- group: company
  title: ''
  type: Website
  url: https://www.sage.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.sage.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.sage.com/en-us/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sage
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sage-accounting-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sage-webhooks-asyncapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sage-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sage-contact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sage-invoice-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sage-contact-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sage-invoice-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sage-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sage-vocabulary.yml
created: '2025-03-01'
description: Sage provides cloud-based ERP, accounting, payroll, and HR software for businesses worldwide. The Sage Developer program provides APIs for integrating with Sage products including Sage Accounting (Business Cloud), Sage Intacct, Sage 200, Sage X3, and Sage 50. APIs support OAuth 2.0 authentication and cover contacts, invoices, payments, ledger accounts, bank accounts, products, and financial reporting. Sage Accounting API v3.1 is the current supported REST version with daily limits of 1,296,000 requests per app.
examples:
- key_count: 2
  name: Sage Create Contact Example
  slug: sage-create-contact-example
- key_count: 2
  name: Sage Create Sales Invoice Example
  slug: sage-create-sales-invoice-example
- key_count: 2
  name: Sage Record Payment Example
  slug: sage-record-payment-example
finops:
- name: Sage Finops
  service_category: Business Software / ERP / Accounting
  slug: sage-finops
graphqls:
- description: Sage X3 provides a GraphQL API offering flexible data access for ERP operations including manufacturing, distribution, procurement, finance, and CRM. Supports SOAP API for legacy integrations. Targete
  name: Sage GraphQL API
  slug: sage-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sage.png
json_schemas:
- name: Address
  property_count: 6
  slug: sage-address
- name: AddressInput
  property_count: 6
  slug: sage-addressinput
- name: BankAccount
  property_count: 7
  slug: sage-bankaccount
- name: BankAccountList
  property_count: 1
  slug: sage-bankaccountlist
- name: BankAccountRef
  property_count: 2
  slug: sage-bankaccountref
- name: Business
  property_count: 7
  slug: sage-business
- name: Sage Contact
  property_count: 14
  slug: sage-contact
- name: ContactList
  property_count: 5
  slug: sage-contactlist
- name: ContactRef
  property_count: 2
  slug: sage-contactref
- name: CountryRef
  property_count: 2
  slug: sage-countryref
- name: CreateBankAccountRequest
  property_count: 1
  slug: sage-createbankaccountrequest
- name: CreateContactRequest
  property_count: 1
  slug: sage-createcontactrequest
- name: CreateProductRequest
  property_count: 1
  slug: sage-createproductrequest
- name: CreatePurchaseInvoiceRequest
  property_count: 1
  slug: sage-createpurchaseinvoicerequest
- name: CreateSalesInvoiceRequest
  property_count: 1
  slug: sage-createsalesinvoicerequest
- name: CurrencyRef
  property_count: 2
  slug: sage-currencyref
- name: ErrorResponse
  property_count: 1
  slug: sage-errorresponse
- name: Sage Sales Invoice
  property_count: 13
  slug: sage-invoice
- name: LedgerAccount
  property_count: 6
  slug: sage-ledgeraccount
- name: LedgerAccountList
  property_count: 2
  slug: sage-ledgeraccountlist
- name: LedgerAccountRef
  property_count: 2
  slug: sage-ledgeraccountref
- name: LineItem
  property_count: 9
  slug: sage-lineitem
- name: LineItemInput
  property_count: 5
  slug: sage-lineiteminput
- name: Payment
  property_count: 5
  slug: sage-payment
- name: PaymentRequest
  property_count: 1
  slug: sage-paymentrequest
- name: Price
  property_count: 2
  slug: sage-price
- name: PriceInput
  property_count: 2
  slug: sage-priceinput
- name: Product
  property_count: 9
  slug: sage-product
- name: ProductList
  property_count: 2
  slug: sage-productlist
- name: PurchaseInvoice
  property_count: 12
  slug: sage-purchaseinvoice
- name: PurchaseInvoiceList
  property_count: 2
  slug: sage-purchaseinvoicelist
- name: SalesInvoice
  property_count: 13
  slug: sage-salesinvoice
- name: SalesInvoiceList
  property_count: 3
  slug: sage-salesinvoicelist
- name: StatusRef
  property_count: 2
  slug: sage-statusref
- name: TaxRate
  property_count: 5
  slug: sage-taxrate
- name: TaxRateList
  property_count: 1
  slug: sage-taxratelist
- name: TaxRateRef
  property_count: 2
  slug: sage-taxrateref
- name: TypeRef
  property_count: 2
  slug: sage-typeref
- name: UpdateContactRequest
  property_count: 1
  slug: sage-updatecontactrequest
- name: UpdateProductRequest
  property_count: 1
  slug: sage-updateproductrequest
- name: UpdateSalesInvoiceRequest
  property_count: 1
  slug: sage-updatesalesinvoicerequest
json_structures:
- name: Sage Contact Structure
  property_count: 0
  slug: sage-contact-structure
- name: Sage Invoice Structure
  property_count: 0
  slug: sage-invoice-structure
- name: Sage Structure
  property_count: 0
  slug: sage-structure
jsonld:
- class_count: 40
  name: Sage Context
  property_count: 1
  slug: sage-context
layout: provider
modified: '2026-05-30'
name: Sage
nav: Providers
network: true
overview: 'Sage publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bank Accounts API, Business API, Contacts API, and 6 more. Tagged areas include Accounting, Business Management, Cloud Software, ERP, and Payroll.


  The Sage catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Sage''s developer surface includes authentication, developer portal, documentation, sandbox, support, engineering blog, and 17 more developer resources.'
plans:
- name: Sage Plans Pricing
  plan_count: 1
  slug: sage-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Sage Rate Limits
  slug: sage-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Sage API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: sage-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Sage API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sage-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Sage API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 5
    warn: 4
  slug: sage-rules
scopes:
- name: Sage Scopes
  scope_count: 2
  slug: sage-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 41.1
  delta: -2.6
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 26.5
    contract_quality: 74.9
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 26.5
    operational_transparency: 7.9
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sage/refs/heads/main/screenshots/sage-2026-06-20T193330.png
security:
- kind: authentication
  name: Sage Authentication
  slug: sage-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sage Domain Security
  slug: sage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sage Vulnerability Disclosure
  slug: sage-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sage
tags:
- Accounting
- Business Management
- Cloud Software
- ERP
- Payroll
- HR
website: https://www.sage.com/
---
