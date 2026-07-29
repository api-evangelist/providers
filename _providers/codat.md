---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Codat Agentic Access
  operation_count: 240
  slug: codat-agentic-access
  summary_line: 240 operations · 70 acting
api_count: 37
apis:
- description: 'The Codat Sync for Expenses API enables corporate card and expense management platforms to provide high-quality integrations with multiple accounting platforms, synchronizing categorized expense data '
  name: Codat Sync for Expenses API
  slug: sync-for-expenses-api
- description: The Codat Bill Pay API (Sync for Payables) enables neobanks, expense management providers, and B2B payment platforms to automate customers' accounts payable workflows, providing a standardized data mo
  name: Codat Bill Pay API
  slug: sync-for-payables-api
- description: The Codat Spend Insights API enables banks and commercial card issuers to access clients' accounts payable data from their ERP or accounting software within minutes, providing insights on spend and su
  name: Codat Spend Insights API
  slug: spend-insights-api
- description: The Codat Sync for Commerce API automatically replicates and reconciles sales data from merchant point-of-sale, payments, and eCommerce systems into their accounting software, transforming raw sales a
  name: Codat Sync for Commerce API
  slug: sync-for-commerce-api
- description: The Codat Sync for Payroll API enables HR, payroll, and vertical SaaS platforms to integrate their customers' payroll data into accounting software and support its reconciliation, providing a standard
  name: Codat Sync for Payroll API
  slug: sync-for-payroll-api
- description: Extra functionality for building an account management UI.
  name: Codat Account mapping API
  slug: codat-account-mapping-api
- description: Access bank transactions from an accounting software.
  name: Codat Accounting bank data API
  slug: codat-accounting-bank-data-api
- description: Data from a linked accounting software representing money the business owes money to its suppliers.
  name: Codat Accounts payable API
  slug: codat-accounts-payable-api
- description: Data from a linked accounting software representing money owed to the business for sold goods or services.
  name: Codat Accounts receivable API
  slug: codat-accounts-receivable-api
- description: Access bank accounts in an SMBs accounting software.
  name: Codat Bank accounts API
  slug: codat-bank-accounts-api
- description: Retrieve banking data from linked bank accounts.
  name: Codat Bank statements API
  slug: codat-bank-statements-api
- description: Create and manage your SMB users' companies.
  name: Codat Companies API
  slug: codat-companies-api
- description: View company information fetched from the source platform.
  name: Codat Company info API
  slug: codat-company-info-api
- description: Get detailed information about a company from the underlying accounting software.
  name: Codat Company information API
  slug: codat-company-information-api
- description: Configure UI and retrieve access tokens for authentication used by **Connections SDK**.
  name: Codat Connection management API
  slug: codat-connection-management-api
- description: Create new and manage existing data connections for a company.
  name: Codat Connections API
  slug: codat-connections-api
- description: Configure and pull additional data types that are not included in Codat's standardized data model.
  name: Codat Custom data type API
  slug: codat-custom-data-type-api
- description: Match mutable accounting data with immutable banking data to increase confidence in financial data.
  name: Codat Data integrity API
  slug: codat-data-integrity-api
- description: Download reports in Excel format.
  name: Codat Excel reports API
  slug: codat-excel-reports-api
- description: Endpoints to manage uploaded files.
  name: Codat File upload API
  slug: codat-file-upload-api
- description: Financial data and reports from a linked accounting software.
  name: Codat Financial statements API
  slug: codat-financial-statements-api
- description: View financial summary information for a company, including credit model reports and accounting score.
  name: Codat Financial summary API
  slug: codat-financial-summary-api
- description: Get a list of integrations supported by Codat and their logos.
  name: Codat Integrations API
  slug: codat-integrations-api
- description: Debt and other liabilities.
  name: Codat Liabilities API
  slug: codat-liabilities-api
- description: 'Implement the [loan writeback](https://docs.codat.io/lending/guides/loan-writeback/introduction) procedure in your lending process to maintain an accurate position of a loan during the entire lending '
  name: Codat Loan writeback API
  slug: codat-loan-writeback-api
- description: Control how data is retrieved from an integration.
  name: Codat Manage data API
  slug: codat-manage-data-api
- description: Generate and review generated reports for a company.
  name: Codat Manage reports API
  slug: codat-manage-reports-api
- description: Manage bank feed syncs for source accounts.
  name: Codat Managed bank feeds API
  slug: codat-managed-bank-feeds-api
- description: Initiate and monitor Create, Update, and Delete operations.
  name: Codat Push data API
  slug: codat-push-data-api
- description: View validation outcomes for completed read data operations.
  name: Codat Read data API
  slug: codat-read-data-api
- description: Initiate data refreshes, view pull status and history.
  name: Codat Refresh data API
  slug: codat-refresh-data-api
- description: Retrieve standardized sales data from a linked commerce software.
  name: Codat Sales API
  slug: codat-sales-api
- description: Manage company profile configuration, sync settings, and API keys.
  name: Codat Settings API
  slug: codat-settings-api
- description: Provide and manage lists of source bank accounts.
  name: Codat Source accounts API
  slug: codat-source-accounts-api
- description: Configure and pull additional data you can include in Codat's standard data types.
  name: Codat Supplemental data API
  slug: codat-supplemental-data-api
- description: Create new bank account transactions for a company's connections, and see previous operations.
  name: Codat Transactions API
  slug: codat-transactions-api
- description: Create and manage webhooks that listen to Codat's events.
  name: Codat Webhooks API
  slug: codat-webhooks-api
artifact_total: 351
collections:
- collection_type: open
  name: Bank Feeds
  slug: open-codat-bank-feeds
- collection_type: open
  name: Lending
  slug: open-codat-lending
- collection_type: open
  name: Platform API
  slug: open-codat-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codat-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codat-limited
- group: start
  title: ''
  type: Portal
  url: https://app.codat.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codat.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.codat.io/get-started/first-steps
- group: build
  title: ''
  type: SDKs
  url: https://docs.codat.io/get-started/libraries
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://github.com/codatio/oas
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codatio
- group: company
  title: ''
  type: Blog
  url: https://codat.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.codat.io/updates
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codat.io
- group: start
  title: ''
  type: Signup
  url: https://codat.io/start-building/
- group: company
  title: ''
  type: About
  url: https://codat.io/about/
- group: commercial
  title: ''
  type: Legal
  url: https://legal.codat.io/
- group: build
  title: ''
  type: TypeScript SDK
  url: https://github.com/codatio/client-sdk-typescript
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/codatio/client-sdk-python
- group: build
  title: ''
  type: C# SDK
  url: https://github.com/codatio/client-sdk-csharp
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/codatio/client-sdk-go
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/codatio/client-sdk-java
- group: agent
  title: ''
  type: LlmsText
  url: https://codat.io/llms.txt
created: '2026-03-03'
description: Codat is a unified API platform focused on SMB financial data, connecting to 30+ accounting, ERP, banking, and payment platforms.
examples:
- key_count: 6
  name: Codat Configure Custom Data Type Example
  slug: codat-configure-custom-data-type-example
- key_count: 6
  name: Codat Configure Supplemental Data Example
  slug: codat-configure-supplemental-data-example
- key_count: 6
  name: Codat Create Api Key Example
  slug: codat-create-api-key-example
- key_count: 6
  name: Codat Create Bank Account Mapping Example
  slug: codat-create-bank-account-mapping-example
- key_count: 6
  name: Codat Create Bank Transactions Example
  slug: codat-create-bank-transactions-example
- key_count: 6
  name: Codat Create Company Example
  slug: codat-create-company-example
- key_count: 6
  name: Codat Create Connection Example
  slug: codat-create-connection-example
- key_count: 6
  name: Codat Create Direct Cost Example
  slug: codat-create-direct-cost-example
- key_count: 6
  name: Codat Create Payment Example
  slug: codat-create-payment-example
- key_count: 6
  name: Codat Create Source Account Example
  slug: codat-create-source-account-example
- key_count: 6
  name: Codat Create Supplier Example
  slug: codat-create-supplier-example
- key_count: 6
  name: Codat Create Transfer Example
  slug: codat-create-transfer-example
- key_count: 6
  name: Codat Create Webhook Consumer Example
  slug: codat-create-webhook-consumer-example
- key_count: 6
  name: Codat Get Accounting Account Example
  slug: codat-get-accounting-account-example
- key_count: 6
  name: Codat Get Accounting Account Transaction Example
  slug: codat-get-accounting-account-transaction-example
- key_count: 6
  name: Codat Get Accounting Aged Creditors Report Example
  slug: codat-get-accounting-aged-creditors-report-example
- key_count: 6
  name: Codat Get Accounting Aged Debtors Report Example
  slug: codat-get-accounting-aged-debtors-report-example
- key_count: 6
  name: Codat Get Accounting Balance Sheet Example
  slug: codat-get-accounting-balance-sheet-example
- key_count: 6
  name: Codat Get Accounting Bank Account Example
  slug: codat-get-accounting-bank-account-example
- key_count: 6
  name: Codat Get Accounting Bill Credit Note Example
  slug: codat-get-accounting-bill-credit-note-example
- key_count: 6
  name: Codat Get Accounting Bill Example
  slug: codat-get-accounting-bill-example
- key_count: 6
  name: Codat Get Accounting Bill Payment Example
  slug: codat-get-accounting-bill-payment-example
- key_count: 6
  name: Codat Get Accounting Cash Flow Statement Example
  slug: codat-get-accounting-cash-flow-statement-example
- key_count: 6
  name: Codat Get Accounting Credit Note Example
  slug: codat-get-accounting-credit-note-example
- key_count: 6
  name: Codat Get Accounting Customer Example
  slug: codat-get-accounting-customer-example
- key_count: 6
  name: Codat Get Accounting Direct Cost Example
  slug: codat-get-accounting-direct-cost-example
- key_count: 6
  name: Codat Get Accounting Direct Income Example
  slug: codat-get-accounting-direct-income-example
- key_count: 6
  name: Codat Get Accounting Invoice Example
  slug: codat-get-accounting-invoice-example
- key_count: 6
  name: Codat Get Accounting Journal Entry Example
  slug: codat-get-accounting-journal-entry-example
- key_count: 6
  name: Codat Get Accounting Journal Example
  slug: codat-get-accounting-journal-example
- key_count: 6
  name: Codat Get Accounting Payment Example
  slug: codat-get-accounting-payment-example
- key_count: 6
  name: Codat Get Accounting Profile Example
  slug: codat-get-accounting-profile-example
- key_count: 6
  name: Codat Get Accounting Profit And Loss Example
  slug: codat-get-accounting-profit-and-loss-example
- key_count: 6
  name: Codat Get Accounting Supplier Example
  slug: codat-get-accounting-supplier-example
- key_count: 6
  name: Codat Get Accounting Transfer Example
  slug: codat-get-accounting-transfer-example
- key_count: 6
  name: Codat Get Bank Account Mapping Example
  slug: codat-get-bank-account-mapping-example
- key_count: 6
  name: Codat Get Banking Account Example
  slug: codat-get-banking-account-example
- key_count: 6
  name: Codat Get Banking Transaction Category Example
  slug: codat-get-banking-transaction-category-example
- key_count: 6
  name: Codat Get Banking Transaction Example
  slug: codat-get-banking-transaction-example
- key_count: 6
  name: Codat Get Categorized Balance Sheet Statement Example
  slug: codat-get-categorized-balance-sheet-statement-example
- key_count: 6
  name: Codat Get Categorized Bank Statement Transactions Example
  slug: codat-get-categorized-bank-statement-transactions-example
- key_count: 6
  name: Codat Get Categorized Profit And Loss Statement Example
  slug: codat-get-categorized-profit-and-loss-statement-example
- key_count: 6
  name: Codat Get Commerce Customer Example
  slug: codat-get-commerce-customer-example
- key_count: 6
  name: Codat Get Commerce Customer Retention Metrics Example
  slug: codat-get-commerce-customer-retention-metrics-example
- key_count: 6
  name: Codat Get Commerce Dispute Example
  slug: codat-get-commerce-dispute-example
- key_count: 6
  name: Codat Get Commerce Lifetime Value Metrics Example
  slug: codat-get-commerce-lifetime-value-metrics-example
- key_count: 6
  name: Codat Get Commerce Location Example
  slug: codat-get-commerce-location-example
- key_count: 6
  name: Codat Get Commerce Order Example
  slug: codat-get-commerce-order-example
- key_count: 6
  name: Codat Get Commerce Orders Report Example
  slug: codat-get-commerce-orders-report-example
- key_count: 6
  name: Codat Get Commerce Payment Example
  slug: codat-get-commerce-payment-example
- key_count: 6
  name: Codat Get Commerce Payment Method Example
  slug: codat-get-commerce-payment-method-example
- key_count: 6
  name: Codat Get Commerce Product Category Example
  slug: codat-get-commerce-product-category-example
- key_count: 6
  name: Codat Get Commerce Product Example
  slug: codat-get-commerce-product-example
- key_count: 6
  name: Codat Get Commerce Profile Example
  slug: codat-get-commerce-profile-example
- key_count: 6
  name: Codat Get Commerce Refunds Report Example
  slug: codat-get-commerce-refunds-report-example
- key_count: 6
  name: Codat Get Commerce Revenue Metrics Example
  slug: codat-get-commerce-revenue-metrics-example
- key_count: 6
  name: Codat Get Commerce Transaction Example
  slug: codat-get-commerce-transaction-example
- key_count: 6
  name: Codat Get Company Access Token Example
  slug: codat-get-company-access-token-example
- key_count: 6
  name: Codat Get Company Data Status Example
  slug: codat-get-company-data-status-example
- key_count: 6
  name: Codat Get Company Example
  slug: codat-get-company-example
- key_count: 6
  name: Codat Get Company Syncsettings Example
  slug: codat-get-company-syncsettings-example
- key_count: 6
  name: Codat Get Connection Example
  slug: codat-get-connection-example
- key_count: 6
  name: Codat Get Connection Management Access Token Example
  slug: codat-get-connection-management-access-token-example
- key_count: 6
  name: Codat Get Create Bankaccounts Model Example
  slug: codat-get-create-bankaccounts-model-example
- key_count: 6
  name: Codat Get Create Chartofaccounts Model Example
  slug: codat-get-create-chartofaccounts-model-example
- key_count: 6
  name: Codat Get Create Directcosts Model Example
  slug: codat-get-create-directcosts-model-example
- key_count: 6
  name: Codat Get Create Payment Model Example
  slug: codat-get-create-payment-model-example
- key_count: 6
  name: Codat Get Create Transfers Model Example
  slug: codat-get-create-transfers-model-example
- key_count: 6
  name: Codat Get Create Update Bankaccounts Model Example
  slug: codat-get-create-update-bankaccounts-model-example
- key_count: 6
  name: Codat Get Create Update Suppliers Model Example
  slug: codat-get-create-update-suppliers-model-example
- key_count: 6
  name: Codat Get Data Status Example
  slug: codat-get-data-status-example
- key_count: 6
  name: Codat Get Financial Summary Example
  slug: codat-get-financial-summary-example
- key_count: 6
  name: Codat Get Profile Syncsettings Example
  slug: codat-get-profile-syncsettings-example
- key_count: 6
  name: Codat Get Read Validation Results Example
  slug: codat-get-read-validation-results-example
- key_count: 6
  name: Codat List Accounting Account Transactions Example
  slug: codat-list-accounting-account-transactions-example
- key_count: 6
  name: Codat List Accounting Accounts Example
  slug: codat-list-accounting-accounts-example
- key_count: 6
  name: Codat List Accounting Bank Account Transactions Example
  slug: codat-list-accounting-bank-account-transactions-example
- key_count: 6
  name: Codat List Accounting Bank Accounts Example
  slug: codat-list-accounting-bank-accounts-example
- key_count: 6
  name: Codat List Accounting Bill Credit Notes Example
  slug: codat-list-accounting-bill-credit-notes-example
- key_count: 6
  name: Codat List Accounting Bill Payments Example
  slug: codat-list-accounting-bill-payments-example
- key_count: 6
  name: Codat List Accounting Bills Example
  slug: codat-list-accounting-bills-example
- key_count: 6
  name: Codat List Accounting Credit Notes Example
  slug: codat-list-accounting-credit-notes-example
- key_count: 6
  name: Codat List Accounting Customers Example
  slug: codat-list-accounting-customers-example
- key_count: 6
  name: Codat List Accounting Direct Costs Example
  slug: codat-list-accounting-direct-costs-example
- key_count: 6
  name: Codat List Accounting Direct Incomes Example
  slug: codat-list-accounting-direct-incomes-example
- key_count: 6
  name: Codat List Accounting Invoices Example
  slug: codat-list-accounting-invoices-example
- key_count: 6
  name: Codat List Accounting Journal Entries Example
  slug: codat-list-accounting-journal-entries-example
- key_count: 6
  name: Codat List Accounting Journals Example
  slug: codat-list-accounting-journals-example
- key_count: 6
  name: Codat List Accounting Payments Example
  slug: codat-list-accounting-payments-example
- key_count: 6
  name: Codat List Accounting Suppliers Example
  slug: codat-list-accounting-suppliers-example
- key_count: 6
  name: Codat List Accounting Transfers Example
  slug: codat-list-accounting-transfers-example
- key_count: 6
  name: Codat List Api Keys Example
  slug: codat-list-api-keys-example
- key_count: 6
  name: Codat List Bank Accounts Example
  slug: codat-list-bank-accounts-example
- key_count: 6
  name: Codat List Banking Account Balances Example
  slug: codat-list-banking-account-balances-example
- key_count: 6
  name: Codat List Banking Accounts Example
  slug: codat-list-banking-accounts-example
- key_count: 6
  name: Codat List Banking Transaction Categories Example
  slug: codat-list-banking-transaction-categories-example
- key_count: 6
  name: Codat List Banking Transactions Example
  slug: codat-list-banking-transactions-example
- key_count: 6
  name: Codat List Categorized Bank Statement Accounts Example
  slug: codat-list-categorized-bank-statement-accounts-example
- key_count: 6
  name: Codat List Commerce Customers Example
  slug: codat-list-commerce-customers-example
- key_count: 6
  name: Codat List Commerce Disputes Example
  slug: codat-list-commerce-disputes-example
- key_count: 6
  name: Codat List Commerce Locations Example
  slug: codat-list-commerce-locations-example
- key_count: 6
  name: Codat List Commerce Orders Example
  slug: codat-list-commerce-orders-example
- key_count: 6
  name: Codat List Commerce Payment Methods Example
  slug: codat-list-commerce-payment-methods-example
- key_count: 6
  name: Codat List Commerce Payments Example
  slug: codat-list-commerce-payments-example
- key_count: 6
  name: Codat List Commerce Product Categories Example
  slug: codat-list-commerce-product-categories-example
- key_count: 6
  name: Codat List Commerce Products Example
  slug: codat-list-commerce-products-example
- key_count: 6
  name: Codat List Commerce Transactions Example
  slug: codat-list-commerce-transactions-example
- key_count: 6
  name: Codat List Companies Example
  slug: codat-list-companies-example
- key_count: 6
  name: Codat List Connections Example
  slug: codat-list-connections-example
- key_count: 6
  name: Codat List Pull Operations Example
  slug: codat-list-pull-operations-example
- key_count: 6
  name: Codat List Reconciled Invoices Example
  slug: codat-list-reconciled-invoices-example
- key_count: 6
  name: Codat List Reports Example
  slug: codat-list-reports-example
- key_count: 6
  name: Codat List Webhook Consumers Example
  slug: codat-list-webhook-consumers-example
- key_count: 6
  name: Codat Refresh Product Data Example
  slug: codat-refresh-product-data-example
- key_count: 6
  name: Codat Replace Company Example
  slug: codat-replace-company-example
- key_count: 6
  name: Codat Rotate Zapier Key Example
  slug: codat-rotate-zapier-key-example
- key_count: 6
  name: Codat Unlink Connection Example
  slug: codat-unlink-connection-example
- key_count: 6
  name: Codat Update Company Example
  slug: codat-update-company-example
finops:
- name: Codat Finops
  service_category: Unified API
  slug: codat-finops
graphqls:
- description: Codat is a unified API platform providing standardized access to SMB financial data from 30+ accounting, banking, commerce, and ERP systems. This conceptual GraphQL schema represents the Codat data mo
  name: Codat GraphQL Schema
  slug: codat-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codat.png
json_schemas:
- name: Account categories updated webhook
  property_count: 9
  slug: codat-accountcategoriesupdatedwebhook
- name: 'Accounting: Account'
  property_count: 0
  slug: codat-accountingaccount
- name: 'Accounting: Accounts'
  property_count: 0
  slug: codat-accountingaccounts
- name: 'Accounting: Account transaction'
  property_count: 0
  slug: codat-accountingaccounttransaction
- name: 'Accounting: Account transactions'
  property_count: 0
  slug: codat-accountingaccounttransactions
- name: 'Accounting: Address'
  property_count: 7
  slug: codat-accountingaddress
- name: 'Accounting: Aged creditors report'
  property_count: 3
  slug: codat-accountingagedcreditorreport
- name: 'Accounting: Aged debtors report'
  property_count: 3
  slug: codat-accountingageddebtorreport
- name: 'Accounting: Attachment'
  property_count: 0
  slug: codat-accountingattachment
- name: 'Accounting: Balance sheet'
  property_count: 4
  slug: codat-accountingbalancesheet
- name: 'Accounting: Bank account'
  property_count: 0
  slug: codat-accountingbankaccount
- name: 'Accounting: Bank accounts'
  property_count: 0
  slug: codat-accountingbankaccounts
- name: Bank Account Type
  property_count: 0
  slug: codat-accountingbankaccounttype
- name: 'Accounting: Bank account transaction'
  property_count: 0
  slug: codat-accountingbanktransaction
- name: 'Accounting: Accounting bank transactions'
  property_count: 0
  slug: codat-accountingbanktransactions
- name: 'Accounting: Bill'
  property_count: 0
  slug: codat-accountingbill
- name: 'Accounting: Bill credit note'
  property_count: 0
  slug: codat-accountingbillcreditnote
- name: 'Accounting: Bill credit notes'
  property_count: 0
  slug: codat-accountingbillcreditnotes
- name: 'Accounting: Bill payment'
  property_count: 0
  slug: codat-accountingbillpayment
- name: 'Accounting: Bill payments'
  property_count: 0
  slug: codat-accountingbillpayments
- name: 'Accounting: Bills'
  property_count: 0
  slug: codat-accountingbills
- name: 'Accounting: Cash flow statement'
  property_count: 6
  slug: codat-accountingcashflowstatement
- name: 'Accounting: Company information'
  property_count: 14
  slug: codat-accountingcompanyinfo
- name: 'Accounting: Create account response'
  property_count: 0
  slug: codat-accountingcreateaccountresponse
- name: 'Accounting: Create bank account response'
  property_count: 0
  slug: codat-accountingcreatebankaccountresponse
- name: 'Accounting: Create bank account transactions'
  property_count: 2
  slug: codat-accountingcreatebanktransactions
- name: 'Accounting: Create/update bank transaction response'
  property_count: 0
  slug: codat-accountingcreatebanktransactionsresponse
- name: 'Accounting: Create direct cost response'
  property_count: 0
  slug: codat-accountingcreatedirectcostresponse
- name: 'Accounting: Create payment response'
  property_count: 0
  slug: codat-accountingcreatepaymentresponse
- name: 'Accounting: Create supplier response'
  property_count: 0
  slug: codat-accountingcreatesupplierresponse
- name: 'Accounting: Create transfer response'
  property_count: 0
  slug: codat-accountingcreatetransferresponse
- name: 'Accounting: Credit note'
  property_count: 0
  slug: codat-accountingcreditnote
- name: 'Accounting: Credit notes'
  property_count: 0
  slug: codat-accountingcreditnotes
- name: 'Accounting: Customer'
  property_count: 0
  slug: codat-accountingcustomer
- name: 'Accounting: Customers'
  property_count: 0
  slug: codat-accountingcustomers
- name: 'Accounting: Direct cost'
  property_count: 0
  slug: codat-accountingdirectcost
- name: 'Accounting: Direct costs'
  property_count: 0
  slug: codat-accountingdirectcosts
- name: 'Accounting: Direct income'
  property_count: 0
  slug: codat-accountingdirectincome
- name: 'Accounting: Direct incomes'
  property_count: 0
  slug: codat-accountingdirectincomes
- name: 'Accounting: Invoice'
  property_count: 0
  slug: codat-accountinginvoice
- name: 'Accounting: Invoices'
  property_count: 0
  slug: codat-accountinginvoices
- name: 'Accounting: Journal'
  property_count: 0
  slug: codat-accountingjournal
- name: 'Accounting: Journal entries'
  property_count: 0
  slug: codat-accountingjournalentries
- name: 'Accounting: Journal entry'
  property_count: 0
  slug: codat-accountingjournalentry
- name: 'Accounting: Journals'
  property_count: 0
  slug: codat-accountingjournals
- name: 'Accounting: Payment'
  property_count: 0
  slug: codat-accountingpayment
- name: 'Accounting: Payment allocation'
  property_count: 2
  slug: codat-accountingpaymentallocation
- name: 'Accounting: Payment method'
  property_count: 0
  slug: codat-accountingpaymentmethod
- name: 'Accounting: Payments'
  property_count: 0
  slug: codat-accountingpayments
- name: 'Accounting: Profit and loss report'
  property_count: 5
  slug: codat-accountingprofitandlossreport
- name: Record reference
  property_count: 2
  slug: codat-accountingrecordref
- name: 'Accounting: Supplier'
  property_count: 0
  slug: codat-accountingsupplier
- name: Suppliers
  property_count: 0
  slug: codat-accountingsuppliers
- name: 'Accounting: Tracking category'
  property_count: 0
  slug: codat-accountingtrackingcategory
- name: 'Accounting: Transfer'
  property_count: 0
  slug: codat-accountingtransfer
- name: 'Accounting: Transfers'
  property_count: 0
  slug: codat-accountingtransfers
- name: Tracking
  property_count: 5
  slug: codat-accountspayabletracking
- name: Tracking
  property_count: 6
  slug: codat-accountsreceivabletracking
- name: 'Accounting: Aged currency outstanding'
  property_count: 2
  slug: codat-agedcurrencyoutstanding
- name: API key details
  property_count: 0
  slug: codat-apikeydetails
- name: API keys
  property_count: 1
  slug: codat-apikeys
- name: Attachments
  property_count: 1
  slug: codat-attachments
- name: Bank Account Credentials
  property_count: 2
  slug: codat-bankaccountcredentials
- name: 'Accounting: Bank accounts'
  property_count: 0
  slug: codat-bankaccounts
- name: Bank feed account mapping
  property_count: 3
  slug: codat-bankfeedaccountmapping
- name: Bank feed account mapping response
  property_count: 4
  slug: codat-bankfeedaccountmappingresponse
- name: Bank feed account mapping
  property_count: 3
  slug: codat-bankfeedbankaccountmapping
- name: Bank feed account mapping response
  property_count: 4
  slug: codat-bankfeedbankaccountmappingresponse
- name: Bank feed mapping
  property_count: 10
  slug: codat-bankfeedmapping
- name: 'Banking: Bank account'
  property_count: 0
  slug: codat-bankingaccount
- name: 'Banking: Account balance'
  property_count: 0
  slug: codat-bankingaccountbalance
- name: 'Banking: Account balances'
  property_count: 0
  slug: codat-bankingaccountbalances
- name: 'Banking: Bank accounts'
  property_count: 0
  slug: codat-bankingaccounts
- name: 'Banking: Transaction'
  property_count: 0
  slug: codat-bankingtransaction
- name: 'Banking: Transaction categories'
  property_count: 0
  slug: codat-bankingtransactioncategories
- name: 'Banking: Transaction category'
  property_count: 0
  slug: codat-bankingtransactioncategory
- name: 'Banking: Transactions'
  property_count: 0
  slug: codat-bankingtransactions
- name: Banking data upload settings
  property_count: 3
  slug: codat-bankstatementuploadconfiguration
- name: Bank transactions
  property_count: 0
  slug: codat-banktransactions
- name: Branding
  property_count: 3
  slug: codat-branding
- name: Categorized bank statement accounts
  property_count: 0
  slug: codat-categorizedbankstatementaccounts
- name: Categorized bank statement transactions
  property_count: 0
  slug: codat-categorizedbankstatementtransactions
- name: Client ID
  property_count: 0
  slug: codat-clientid
- name: Client rate limit webhook
  property_count: 4
  slug: codat-clientratelimitwebhook
- name: 'Commerce: Address'
  property_count: 7
  slug: codat-commerceaddress
- name: 'Commerce: Company profile'
  property_count: 0
  slug: codat-commercecompanyinfo
- name: 'Commerce: Customer'
  property_count: 0
  slug: codat-commercecustomer
- name: 'Commerce: Customers'
  property_count: 0
  slug: codat-commercecustomers
- name: 'Commerce: Dispute'
  property_count: 0
  slug: codat-commercedispute
- name: 'Commerce: Disputes'
  property_count: 0
  slug: codat-commercedisputes
- name: 'Commerce: Location'
  property_count: 0
  slug: codat-commercelocation
- name: 'Commerce: Locations'
  property_count: 0
  slug: codat-commercelocations
- name: 'Commerce: Order'
  property_count: 0
  slug: codat-commerceorder
- name: 'Commerce: Orders'
  property_count: 0
  slug: codat-commerceorders
- name: 'Commerce: Payment'
  property_count: 0
  slug: codat-commercepayment
- name: 'Commerce: Payment method'
  property_count: 0
  slug: codat-commercepaymentmethod
- name: 'Commerce: Payment methods'
  property_count: 0
  slug: codat-commercepaymentmethods
- name: 'Commerce: Payments'
  property_count: 0
  slug: codat-commercepayments
- name: 'Commerce: Product'
  property_count: 0
  slug: codat-commerceproduct
- name: 'Commerce: Product categories'
  property_count: 0
  slug: codat-commerceproductcategories
- name: 'Commerce: Product category'
  property_count: 0
  slug: codat-commerceproductcategory
- name: 'Commerce: Products'
  property_count: 0
  slug: codat-commerceproducts
- name: Record Ref
  property_count: 2
  slug: codat-commercerecordref
- name: Commerce report
  property_count: 5
  slug: codat-commercereport
- name: 'Commerce: Tax component'
  property_count: 0
  slug: codat-commercetaxcomponent
- name: 'Commerce: Transaction'
  property_count: 0
  slug: codat-commercetransaction
- name: 'Commerce: Transactions'
  property_count: 0
  slug: codat-commercetransactions
- name: Companies
  property_count: 0
  slug: codat-companies
- name: Company
  property_count: 0
  slug: codat-company
- name: Company access token
  property_count: 0
  slug: codat-companyaccesstoken
- name: Company information
  property_count: 5
  slug: codat-companyinformation
- name: Create company request
  property_count: 3
  slug: codat-companyrequestbody
- name: Company sync settings
  property_count: 3
  slug: codat-companysyncsettings
- name: Update company request
  property_count: 3
  slug: codat-companyupdaterequest
- name: Company webhook
  property_count: 4
  slug: codat-companywebhook
- name: Connection
  property_count: 12
  slug: codat-connection
- name: Access token
  property_count: 1
  slug: codat-connectionmanagementaccesstoken
- name: Allowed origins
  property_count: 1
  slug: codat-connectionmanagementallowedorigins
- name: Connections
  property_count: 0
  slug: codat-connections
- name: Connection webhook
  property_count: 4
  slug: codat-connectionwebhook
- name: Create API key
  property_count: 1
  slug: codat-createapikey
- name: Create bank transactions
  property_count: 2
  slug: codat-createbanktransactions
- name: Create bank transaction response
  property_count: 0
  slug: codat-createbanktransactionsresponse
- name: Custom data type configuration
  property_count: 4
  slug: codat-customdatatypeconfiguration
- name: Custom data type records
  property_count: 4
  slug: codat-customdatatyperecords
- name: Data integrity detail
  property_count: 8
  slug: codat-dataintegritydetail
- name: Data integrity details
  property_count: 0
  slug: codat-dataintegritydetails
- name: Data integrity status
  property_count: 0
  slug: codat-dataintegritystatus
- name: Data integrity statuses
  property_count: 1
  slug: codat-dataintegritystatuses
- name: Data integrity summaries
  property_count: 1
  slug: codat-dataintegritysummaries
- name: Data integrity summary
  property_count: 0
  slug: codat-dataintegritysummary
- name: Data status
  property_count: 5
  slug: codat-datastatus
- name: Data statuses
  property_count: 43
  slug: codat-datastatuses
- name: Data status response
  property_count: 0
  slug: codat-datastatusresponse
- name: Data types
  property_count: 0
  slug: codat-datatype
- name: Write data type webhook
  property_count: 4
  slug: codat-datatypewritewebhook
- name: Date time
  property_count: 0
  slug: codat-datetime
- name: End upload session request
  property_count: 1
  slug: codat-enduploadsessionrequest
- name: Enhanced cash flow transactions
  property_count: 3
  slug: codat-enhancedcashflowtransactions
- name: Enhanced report
  property_count: 2
  slug: codat-enhancedfinancialreport
- name: Enhanced invoices report
  property_count: 2
  slug: codat-enhancedinvoicesreport
- name: Error message
  property_count: 7
  slug: codat-errormessage
- name: Excel status
  property_count: 8
  slug: codat-excelstatus
- name: File
  property_count: 4
  slug: codat-file
- name: Files
  property_count: 0
  slug: codat-files
- name: Attachment upload
  property_count: 1
  slug: codat-fileupload
- name: Closed Books Indicator
  property_count: 2
  slug: codat-financialsummary
- name: Integration
  property_count: 11
  slug: codat-integration
- name: Integrations
  property_count: 0
  slug: codat-integrations
- name: Loan summary
  property_count: 2
  slug: codat-loansummary
- name: Loan transactions
  property_count: 2
  slug: codat-loantransactions
- name: Metadata
  property_count: 1
  slug: codat-metadata
- name: Pagination information
  property_count: 4
  slug: codat-paginginfo
- name: Payment method reference
  property_count: 2
  slug: codat-paymentmethodref
- name: Phone
  property_count: 2
  slug: codat-phonenumber
- name: Profile
  property_count: 7
  slug: codat-profile
- name: 'Accounting: Project reference'
  property_count: 2
  slug: codat-projectref
- name: Pull operation
  property_count: 12
  slug: codat-pulloperation
- name: Pull operations
  property_count: 0
  slug: codat-pulloperations
- name: Push operation
  property_count: 13
  slug: codat-pushoperation
- name: Push operations
  property_count: 0
  slug: codat-pushoperations
- name: Push option
  property_count: 7
  slug: codat-pushoption
- name: Read completed webhook
  property_count: 4
  slug: codat-readcompletedwebhook
- name: 'Accounting: Report line'
  property_count: 4
  slug: codat-reportline
- name: Report
  property_count: 6
  slug: codat-reportoperation
- name: Source account (v1)
  property_count: 10
  slug: codat-sourceaccount
- name: Batch source account request creation response
  property_count: 2
  slug: codat-sourceaccountbatchcreateresponse
- name: Batch source account creation error
  property_count: 2
  slug: codat-sourceaccountbatcherrorresponse
- name: Source account (v2)
  property_count: 12
  slug: codat-sourceaccountv2
- name: Batch source account (v2) creation response
  property_count: 2
  slug: codat-sourceaccountv2batchcreateresponse
- name: Source account status changed webhook
  property_count: 4
  slug: codat-sourceaccountwebhook
- name: Start scheduled sync result
  property_count: 1
  slug: codat-startscheduledsyncresult
- name: Upload session start request
  property_count: 1
  slug: codat-startuploadsessionrequest
- name: Supplemental data
  property_count: 1
  slug: codat-supplementaldata
- name: Supplemental data configuration
  property_count: 1
  slug: codat-supplementaldataconfiguration
- name: SyncSetting
  property_count: 8
  slug: codat-syncsetting
- name: Sync settings
  property_count: 3
  slug: codat-syncsettings
- name: Sync status
  property_count: 14
  slug: codat-syncstatusresult
- name: Third-party schema
  property_count: 0
  slug: codat-thirdpartyschema
- name: Update connection
  property_count: 1
  slug: codat-updateconnectionstatus
- name: Validation result
  property_count: 2
  slug: codat-validationresult
- name: Webhook consumer
  property_count: 5
  slug: codat-webhookconsumer
- name: Zapier integration key
  property_count: 1
  slug: codat-webhookzapierkey
- name: Weblink
  property_count: 2
  slug: codat-weblink
json_structures:
- name: Codat Structure
  property_count: 0
  slug: codat-structure
layout: provider
modified: '2026-05-19'
name: Codat
nav: Providers
network: true
overview: 'Codat publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Account mapping API, Accounting bank data API, Accounts payable API, and 29 more. Tagged areas include Unified_API.


  The Codat catalog on APIs.io includes 1 Spectral governance ruleset.


  Codat''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, signup flow, and 15 more developer resources.'
plans:
- name: Codat Plans Pricing
  plan_count: 1
  slug: codat-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Codat Rate Limits
  slug: codat-rate-limits
rules:
- name: Codat API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: codat-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.8
  delta: -1.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 67.0
    developer_ergonomics: 56.5
    discoverability: 40.7
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codat/refs/heads/main/screenshots/codat-2026-06-20T174652.png
security:
- kind: authentication
  name: Codat Authentication
  slug: codat-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Codat Domain Security
  slug: codat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: codat
tags:
- Unified_API
website: https://app.codat.io/
---
