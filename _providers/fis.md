---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 97
  human_in_the_loop: 57
  name: Fis Agentic Access
  operation_count: 241
  slug: fis-agentic-access
  summary_line: 241 operations · 97 acting · 57 human-in-the-loop
api_count: 2
apis:
- description: FIS (Fidelity National Information Services) provides core banking platforms including the Systematics suite. APIs bridge mainframe-based account processing, transaction management, and loan servicing
  name: FIS Core Banking API
  slug: fis-core-banking-api
- description: FIS wealth management APIs enable integration with portfolio management, account aggregation, trading, and advisory systems for wealth management platforms and financial advisors.
  name: FIS Wealth Management API
  slug: fis-wealth-management-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Account information and balance inquiries
  name: FIS Global Accounts API
  slug: fis-accounts-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: ACH (Automated Clearing House) payment operations
  name: FIS Global ACH API
  slug: fis-ach-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Initiate and manage payment transactions
  name: FIS Global Payments API
  slug: fis-payments-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Transaction history and status
  name: FIS Global Transactions API
  slug: fis-transactions-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Domestic and international wire transfer operations
  name: FIS Global Wire Transfers API
  slug: fis-wire-transfers-api
- description: FIS Code Connect is the developer marketplace exposing FIS APIs across payments, banking, capital markets, and wealth management products. Access to most APIs requires a partner agreement and authenti
  name: FIS Code Connect API Marketplace
  slug: code-connect
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Account API from FIS Global — 1 operation(s) for account.
  name: FIS Global Account API
  slug: fis-account-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The AccountControllerV2 API from FIS Global — 3 operation(s) for accountcontrollerv2.
  name: FIS Global Account Controller V2 API
  slug: fis-accountcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The AccountingTransaction API from FIS Global — 1 operation(s) for accountingtransaction.
  name: FIS Global Accounting Transaction API
  slug: fis-accountingtransaction-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The AccountingTransactionControllerV2 API from FIS Global — 1 operation(s) for accountingtransactioncontrollerv2.
  name: FIS Global Accounting Transaction Controller V2 API
  slug: fis-accountingtransactioncontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Aging API from FIS Global — 2 operation(s) for aging.
  name: FIS Global Aging API
  slug: fis-aging-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The AgingControllerV2 API from FIS Global — 2 operation(s) for agingcontrollerv2.
  name: FIS Global Aging Controller V2 API
  slug: fis-agingcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Attachment API from FIS Global — 1 operation(s) for attachment.
  name: FIS Global Attachment API
  slug: fis-attachment-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The AttachmentControllerV2 API from FIS Global — 1 operation(s) for attachmentcontrollerv2.
  name: FIS Global Attachment Controller V2 API
  slug: fis-attachmentcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Bank API from FIS Global — 4 operation(s) for bank.
  name: FIS Global Bank API
  slug: fis-bank-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The BankControllerV2 API from FIS Global — 9 operation(s) for bankcontrollerv2.
  name: FIS Global Bank Controller V2 API
  slug: fis-bankcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Bill API from FIS Global — 4 operation(s) for bill.
  name: FIS Global Bill API
  slug: fis-bill-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The BillControllerV2 API from FIS Global — 7 operation(s) for billcontrollerv2.
  name: FIS Global Bill Controller V2 API
  slug: fis-billcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Budget API from FIS Global — 1 operation(s) for budget.
  name: FIS Global Budget API
  slug: fis-budget-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Businesses API from FIS Global — 8 operation(s) for businesses.
  name: FIS Global Businesses API
  slug: fis-businesses-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The BusinessValuation API from FIS Global — 1 operation(s) for businessvaluation.
  name: FIS Global Business Valuation API
  slug: fis-businessvaluation-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The BusinessValuationControllerV2 API from FIS Global — 1 operation(s) for businessvaluationcontrollerv2.
  name: FIS Global Business Valuation Controller V2 API
  slug: fis-businessvaluationcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Connection API from FIS Global — 2 operation(s) for connection.
  name: FIS Global Connection API
  slug: fis-connection-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The ConnectionControllerV2 API from FIS Global — 2 operation(s) for connectioncontrollerv2.
  name: FIS Global Connection Controller V2 API
  slug: fis-connectioncontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The ContactControllerV2 API from FIS Global — 1 operation(s) for contactcontrollerv2.
  name: FIS Global Contact Controller V2 API
  slug: fis-contactcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Credit API from FIS Global — 2 operation(s) for credit.
  name: FIS Global Credit API
  slug: fis-credit-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The CreditControllerV2 API from FIS Global — 2 operation(s) for creditcontrollerv2.
  name: FIS Global Credit Controller V2 API
  slug: fis-creditcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Customer API from FIS Global — 2 operation(s) for customer.
  name: FIS Global Customer API
  slug: fis-customer-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The CustomerControllerV2 API from FIS Global — 4 operation(s) for customercontrollerv2.
  name: FIS Global Customer Controller V2 API
  slug: fis-customercontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Data API from FIS Global — 3 operation(s) for data.
  name: FIS Global Data API
  slug: fis-data-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The DataControllerV2 API from FIS Global — 6 operation(s) for datacontrollerv2.
  name: FIS Global Data Controller V2 API
  slug: fis-datacontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Deposit API from FIS Global — 1 operation(s) for deposit.
  name: FIS Global Deposit API
  slug: fis-deposit-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The DepositControllerV2 API from FIS Global — 1 operation(s) for depositcontrollerv2.
  name: FIS Global Deposit Controller V2 API
  slug: fis-depositcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Dispute API from FIS Global — 1 operation(s) for dispute.
  name: FIS Global Dispute API
  slug: fis-dispute-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The DisputeControllerV2 API from FIS Global — 1 operation(s) for disputecontrollerv2.
  name: FIS Global Dispute Controller V2 API
  slug: fis-disputecontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Estimate API from FIS Global — 1 operation(s) for estimate.
  name: FIS Global Estimate API
  slug: fis-estimate-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The EstimateControllerV2 API from FIS Global — 1 operation(s) for estimatecontrollerv2.
  name: FIS Global Estimate Controller V2 API
  slug: fis-estimatecontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The ExpenseControllerV2 API from FIS Global — 1 operation(s) for expensecontrollerv2.
  name: FIS Global Expense Controller V2 API
  slug: fis-expensecontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The File API from FIS Global — 1 operation(s) for file.
  name: FIS Global File API
  slug: fis-file-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialBenchmarking API from FIS Global — 1 operation(s) for financialbenchmarking.
  name: FIS Global Financial Benchmarking API
  slug: fis-financialbenchmarking-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialBenchmarkingControllerV2 API from FIS Global — 1 operation(s) for financialbenchmarkingcontrollerv2.
  name: FIS Global Financial Benchmarking Controller V2 API
  slug: fis-financialbenchmarkingcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialForecast API from FIS Global — 1 operation(s) for financialforecast.
  name: FIS Global Financial Forecast API
  slug: fis-financialforecast-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialForecastControllerV2 API from FIS Global — 1 operation(s) for financialforecastcontrollerv2.
  name: FIS Global Financial Forecast Controller V2 API
  slug: fis-financialforecastcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialFraudRisk API from FIS Global — 1 operation(s) for financialfraudrisk.
  name: FIS Global Financial Fraud Risk API
  slug: fis-financialfraudrisk-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialFraudRiskControllerV2 API from FIS Global — 1 operation(s) for financialfraudriskcontrollerv2.
  name: FIS Global Financial Fraud Risk Controller V2 API
  slug: fis-financialfraudriskcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialRatio API from FIS Global — 1 operation(s) for financialratio.
  name: FIS Global Financial Ratio API
  slug: fis-financialratio-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialRatioControllerV2 API from FIS Global — 1 operation(s) for financialratiocontrollerv2.
  name: FIS Global Financial Ratio Controller V2 API
  slug: fis-financialratiocontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialStatement API from FIS Global — 3 operation(s) for financialstatement.
  name: FIS Global Financial Statement API
  slug: fis-financialstatement-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The FinancialStatementControllerV2 API from FIS Global — 6 operation(s) for financialstatementcontrollerv2.
  name: FIS Global Financial Statement Controller V2 API
  slug: fis-financialstatementcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Inventory API from FIS Global — 2 operation(s) for inventory.
  name: FIS Global Inventory API
  slug: fis-inventory-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The InventoryControllerV2 API from FIS Global — 2 operation(s) for inventorycontrollerv2.
  name: FIS Global Inventory Controller V2 API
  slug: fis-inventorycontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Invoice API from FIS Global — 3 operation(s) for invoice.
  name: FIS Global Invoice API
  slug: fis-invoice-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The InvoiceControllerV2 API from FIS Global — 5 operation(s) for invoicecontrollerv2.
  name: FIS Global Invoice Controller V2 API
  slug: fis-invoicecontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Journal API from FIS Global — 2 operation(s) for journal.
  name: FIS Global Journal API
  slug: fis-journal-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The JournalControllerV2 API from FIS Global — 5 operation(s) for journalcontrollerv2.
  name: FIS Global Journal Controller V2 API
  slug: fis-journalcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Order API from FIS Global — 1 operation(s) for order.
  name: FIS Global Order API
  slug: fis-order-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The OrderControllerV2 API from FIS Global — 1 operation(s) for ordercontrollerv2.
  name: FIS Global Order Controller V2 API
  slug: fis-ordercontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The PaymentMethodControllerV2 API from FIS Global — 1 operation(s) for paymentmethodcontrollerv2.
  name: FIS Global Payment Method Controller V2 API
  slug: fis-paymentmethodcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The PayrollTransaction API from FIS Global — 1 operation(s) for payrolltransaction.
  name: FIS Global Payroll Transaction API
  slug: fis-payrolltransaction-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The PortfolioMetrics API from FIS Global — 1 operation(s) for portfoliometrics.
  name: FIS Global Portfolio Metrics API
  slug: fis-portfoliometrics-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The PortfolioMetricsControllerV2 API from FIS Global — 1 operation(s) for portfoliometricscontrollerv2.
  name: FIS Global Portfolio Metrics Controller V2 API
  slug: fis-portfoliometricscontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The ProbabilityOfDefault API from FIS Global — 1 operation(s) for probabilityofdefault.
  name: FIS Global Probability Of Default API
  slug: fis-probabilityofdefault-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The ProbabilityOfDefaultControllerV2 API from FIS Global — 1 operation(s) for probabilityofdefaultcontrollerv2.
  name: FIS Global Probability Of Default Controller V2 API
  slug: fis-probabilityofdefaultcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Product API from FIS Global — 1 operation(s) for product.
  name: FIS Global Product API
  slug: fis-product-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The ProductControllerV2 API from FIS Global — 1 operation(s) for productcontrollerv2.
  name: FIS Global Product Controller V2 API
  slug: fis-productcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The PurchaseOrderControllerV2 API from FIS Global — 1 operation(s) for purchaseordercontrollerv2.
  name: FIS Global Purchase Order Controller V2 API
  slug: fis-purchaseordercontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Refunds API from FIS Global — 2 operation(s) for refunds.
  name: FIS Global Refunds API
  slug: fis-refunds-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Reports API from FIS Global — 10 operation(s) for reports.
  name: FIS Global Reports API
  slug: fis-reports-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Sandbox API from FIS Global — 2 operation(s) for sandbox.
  name: FIS Global Sandbox API
  slug: fis-sandbox-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The TaxBenchmarking API from FIS Global — 1 operation(s) for taxbenchmarking.
  name: FIS Global Tax Benchmarking API
  slug: fis-taxbenchmarking-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The TaxBenchmarkingControllerV2 API from FIS Global — 1 operation(s) for taxbenchmarkingcontrollerv2.
  name: FIS Global Tax Benchmarking Controller V2 API
  slug: fis-taxbenchmarkingcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The TaxRateControllerV2 API from FIS Global — 2 operation(s) for taxratecontrollerv2.
  name: FIS Global Tax Rate Controller V2 API
  slug: fis-taxratecontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The TrackingCategory API from FIS Global — 1 operation(s) for trackingcategory.
  name: FIS Global Tracking Category API
  slug: fis-trackingcategory-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The TrackingCategoryControllerV2 API from FIS Global — 1 operation(s) for trackingcategorycontrollerv2.
  name: FIS Global Tracking Category Controller V2 API
  slug: fis-trackingcategorycontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Transaction API from FIS Global — 1 operation(s) for transaction.
  name: FIS Global Transaction API
  slug: fis-transaction-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The TransactionControllerV2 API from FIS Global — 1 operation(s) for transactioncontrollerv2.
  name: FIS Global Transaction Controller V2 API
  slug: fis-transactioncontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The TrialBalance API from FIS Global — 1 operation(s) for trialbalance.
  name: FIS Global Trial Balance API
  slug: fis-trialbalance-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The TrialBalanceControllerV2 API from FIS Global — 1 operation(s) for trialbalancecontrollerv2.
  name: FIS Global Trial Balance Controller V2 API
  slug: fis-trialbalancecontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Vendor API from FIS Global — 2 operation(s) for vendor.
  name: FIS Global Vendor API
  slug: fis-vendor-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The VendorControllerV2 API from FIS Global — 5 operation(s) for vendorcontrollerv2.
  name: FIS Global Vendor Controller V2 API
  slug: fis-vendorcontrollerv2-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Visualizations API from FIS Global — 16 operation(s) for visualizations.
  name: FIS Global Visualizations API
  slug: fis-visualizations-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Purchase Order API from FIS Global — 1 operation(s) for purchase order.
  name: FIS Global Purchase Order API
  slug: fis-purchase-order-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: The Tax Rate API from FIS Global — 1 operation(s) for tax rate.
  name: FIS Global Tax Rate API
  slug: fis-tax-rate-api
artifact_total: 228
asyncapis:
- description: ''
  name: Fis Webhooks
  slug: fis-webhooks
collections:
- collection_type: open
  name: FIS Payments Accounts API
  slug: open-fis-accounts-api
- collection_type: open
  name: FIS Payments Accounts ACH API
  slug: open-fis-ach-api
- collection_type: open
  name: FIS Accounts Payments API
  slug: open-fis-payments-api
- collection_type: open
  name: FIS Payments API
  slug: open-fis-payments
- collection_type: open
  name: FIS Payments Accounts Transactions API
  slug: open-fis-transactions-api
- collection_type: open
  name: FIS Payments Accounts Wire Transfers API
  slug: open-fis-wire-transfers-api
common:
- group: auth
  href: https://artifacts.apis.io/fis/scopes/fis-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fis-scopes.yml
- group: design
  href: https://artifacts.apis.io/fis/rules/fis-rules.yml
  title: ''
  type: Spectral
  url: rules/fis-rules.yml
- group: design
  href: https://artifacts.apis.io/fis/rules/fis-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/fis-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/fis/json-ld/fis-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fis-context.jsonld
- group: design
  href: https://artifacts.apis.io/fis/vocabulary/fis-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fis-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/fis/lifecycle/fis-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/fis-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/fis/hosts/fis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fis-hosts.yml
- group: other
  href: https://artifacts.apis.io/fis/vendors/fis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fis-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/fis/finops/fis-finops.yml
  title: ''
  type: FinOps
  url: finops/fis-finops.yml
- group: other
  href: https://artifacts.apis.io/fis/capabilities/fis-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fis-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/fis/overlays/fis-accounting-data-as-a-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fis-accounting-data-as-a-service-overlay.yaml
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.fisglobal.com/
- group: agent
  href: https://artifacts.apis.io/fis/agentic-access/fis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fis-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fis/security/fis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fis-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fis/authentication/fis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fis-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FISGlobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fis
- group: company
  title: ''
  type: Website
  url: https://www.fisglobal.com/
- group: agent
  href: https://artifacts.apis.io/fis/well-known/fis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fis-well-known.yml
- group: auth
  href: https://artifacts.apis.io/fis/well-known/fis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fis-security.txt
- group: auth
  href: https://artifacts.apis.io/fis/security/fis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fisglobal.com/en/responsible-disclosure
- group: auth
  href: https://artifacts.apis.io/fis/security/fis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fis-trust-center.yml
- group: build
  href: https://artifacts.apis.io/fis/packages/fis-packages.yml
  title: ''
  type: Packages
  url: packages/fis-packages.yml
- group: build
  href: https://artifacts.apis.io/fis/packages/fis-packages.yml
  title: ''
  type: SDKs
  url: packages/fis-packages.yml
- group: design
  href: https://artifacts.apis.io/fis/components/fis-components.yml
  title: ''
  type: Components
  url: components/fis-components.yml
- group: start
  href: https://artifacts.apis.io/fis/sandbox/fis-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fis-sandbox.yml
- group: design
  href: https://artifacts.apis.io/fis/lifecycle/fis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fis-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.railz.ai
- group: operate
  href: https://artifacts.apis.io/fis/changelog/fis-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fis-changelog.yml
- group: operate
  href: https://artifacts.apis.io/fis/rate-limits/fis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fis-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fis/plans/fis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fis-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fis/errors/fis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fis-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fis/conventions/fis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fis-conventions.yml
- group: design
  href: https://artifacts.apis.io/fis/data-model/fis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fis-data-model.yml
- group: design
  href: https://artifacts.apis.io/fis/conformance/fis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fis-conformance.yml
- group: design
  href: https://artifacts.apis.io/fis/asyncapi/fis-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fis-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/fis/mcp/fis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fis-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fis/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/fis/llms/fis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fis-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://codeconnect.fisglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.railz.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.railz.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://codeconnect.fisglobal.com/app/guides/gettingstarted
- group: start
  title: ''
  type: SignUp
  url: https://codeconnect.fisglobal.com/app/userregister
- group: operate
  title: ''
  type: Support
  url: https://codeconnect.fisglobal.com/app/guides/faqs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fisglobal.com/products/accounting-data-as-a-service
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fisglobal.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fisglobal.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.fisglobal.com/insights
created: '2026-04-28'
description: FIS (Fidelity National Information Services) is a global leader in financial technology providing APIs for core banking, payments, wealth management, and capital markets through the CodeConnect API marketplace. APIs connect financial institutions, fintechs, and enterprises to FIS banking and payment infrastructure.
finops:
- has_sources: true
  method: derived
  name: Fis Finops
  primary_unit: ''
  service_category: ''
  slug: fis-finops
  template: true
image: https://codeconnect.fisglobal.com/assets/FIS_codeConnect_logo_white.svg
json_schemas:
- name: AccountBalance
  property_count: 5
  slug: fis-account-balance
- name: AccountingTransactionsResponseDto
  property_count: 4
  slug: fis-accounting-transactions-response-dto
- name: AccountingTransactionsResponseV2Dto
  property_count: 3
  slug: fis-accounting-transactions-response-v2-dto
- name: AchBatchRequest
  property_count: 6
  slug: fis-ach-batch-request
- name: AchBatch
  property_count: 6
  slug: fis-ach-batch
- name: AchTransferRequest
  property_count: 8
  slug: fis-ach-transfer-request
- name: AchTransfer
  property_count: 12
  slug: fis-ach-transfer
- name: ApAgingResponseDto
  property_count: 3
  slug: fis-ap-aging-response-dto
- name: ApAgingResponseV2Dto
  property_count: 2
  slug: fis-ap-aging-response-v2-dto
- name: ArAgingResponseDto
  property_count: 3
  slug: fis-ar-aging-response-dto
- name: ArAgingResponseV2Dto
  property_count: 2
  slug: fis-ar-aging-response-v2-dto
- name: BankReconciliationResponseDto
  property_count: 3
  slug: fis-bank-reconciliation-response-dto
- name: BatchPushBankTransactionResponseV2Dto
  property_count: 5
  slug: fis-batch-push-bank-transaction-response-v2-dto
- name: BatchPushChartOfAccountV2Dto
  property_count: 2
  slug: fis-batch-push-chart-of-account-v2-dto
- name: BatchPushChartOfAccountV2ResponseDto
  property_count: 5
  slug: fis-batch-push-chart-of-account-v2-response-dto
- name: BatchPushCustomerResponseV2Dto
  property_count: 5
  slug: fis-batch-push-customer-response-v2-dto
- name: BatchUpdateBankTransactionResponseV2Dto
  property_count: 5
  slug: fis-batch-update-bank-transaction-response-v2-dto
- name: BatchUpdateChartOfAccountV2Dto
  property_count: 2
  slug: fis-batch-update-chart-of-account-v2-dto
- name: BatchUpdateChartOfAccountV2ResponseDto
  property_count: 5
  slug: fis-batch-update-chart-of-account-v2-response-dto
- name: BatchUpdateCustomerResponseDto
  property_count: 5
  slug: fis-batch-update-customer-response-dto
- name: BusinessValuationResponseDto
  property_count: 2
  slug: fis-business-valuation-response-dto
- name: BusinessValuationResponseV2Dto
  property_count: 2
  slug: fis-business-valuation-response-v2-dto
- name: CashflowStatementsResponseDto
  property_count: 3
  slug: fis-cashflow-statements-response-dto
- name: ConnectionsResponseDto
  property_count: 2
  slug: fis-connections-response-dto
- name: ConnectionsResponseDtoV2
  property_count: 2
  slug: fis-connections-response-dto-v2
- name: CreditRatingsResponseDto
  property_count: 2
  slug: fis-credit-ratings-response-dto
- name: CreditRatingsResponseV2Dto
  property_count: 2
  slug: fis-credit-ratings-response-v2-dto
- name: CreditScoresResponseDto
  property_count: 2
  slug: fis-credit-scores-response-dto
- name: CreditScoresResponseV2Dto
  property_count: 2
  slug: fis-credit-scores-response-v2-dto
- name: DataStatusResponseDto
  property_count: 2
  slug: fis-data-status-response-dto
- name: DataStatusResponseV2Dto
  property_count: 3
  slug: fis-data-status-response-v2-dto
- name: DataSyncDto
  property_count: 4
  slug: fis-data-sync-dto
- name: DataSyncResponseDto
  property_count: 5
  slug: fis-data-sync-response-dto
- name: DataSyncResponseV2Dto
  property_count: 7
  slug: fis-data-sync-response-v2-dto
- name: DataSyncV2Dto
  property_count: 4
  slug: fis-data-sync-v2-dto
- name: DeleteStatusResponseV2Dto
  property_count: 2
  slug: fis-delete-status-response-v2-dto
- name: DisableConnectionDto
  property_count: 1
  slug: fis-disable-connection-dto
- name: DisconnectResponseDto
  property_count: 6
  slug: fis-disconnect-response-dto
- name: FinancialBenchmarkingsResponseDto
  property_count: 2
  slug: fis-financial-benchmarkings-response-dto
- name: FinancialForecastResponseV1Dto
  property_count: 2
  slug: fis-financial-forecast-response-v1-dto
- name: FinancialForecastResponseV2Dto
  property_count: 2
  slug: fis-financial-forecast-response-v2-dto
- name: FinancialFraudRiskResponseDto
  property_count: 2
  slug: fis-financial-fraud-risk-response-dto
- name: FinancialFraudRiskResponseV2Dto
  property_count: 2
  slug: fis-financial-fraud-risk-response-v2-dto
- name: FinancialRatiosResponseDto
  property_count: 3
  slug: fis-financial-ratios-response-dto
- name: FinancialRatiosResponseV2Dto
  property_count: 3
  slug: fis-financial-ratios-response-v2-dto
- name: GetAttachmentResponseV1Dto
  property_count: 2
  slug: fis-get-attachment-response-v1-dto
- name: GetAttachmentV2ResponseDto
  property_count: 3
  slug: fis-get-attachment-v2-response-dto
- name: GetBankAccountResponseDto
  property_count: 4
  slug: fis-get-bank-account-response-dto
- name: GetBankTransactionsResponseDto
  property_count: 3
  slug: fis-get-bank-transactions-response-dto
- name: GetBankTransfersResponseDto
  property_count: 4
  slug: fis-get-bank-transfers-response-dto
- name: GetBillCreditNoteResponseDto
  property_count: 4
  slug: fis-get-bill-credit-note-response-dto
- name: GetBillPaymentResponseDto
  property_count: 4
  slug: fis-get-bill-payment-response-dto
- name: GetBudgetResponseV2Dto
  property_count: 3
  slug: fis-get-budget-response-v2-dto
- name: GetChartOfAccountsResponseV1Dto
  property_count: 4
  slug: fis-get-chart-of-accounts-response-v1-dto
- name: GetContactResponseDto
  property_count: 3
  slug: fis-get-contact-response-dto
- name: GetCustomerBankAccountResponseV2Dto
  property_count: 3
  slug: fis-get-customer-bank-account-response-v2-dto
- name: GetCustomerResponseDto
  property_count: 4
  slug: fis-get-customer-response-dto
- name: GetDepositResponseDto
  property_count: 4
  slug: fis-get-deposit-response-dto
- name: GetDepositResponseV2Dto
  property_count: 3
  slug: fis-get-deposit-response-v2-dto
- name: GetDisputeResponseDto
  property_count: 4
  slug: fis-get-dispute-response-dto
- name: GetDisputeResponseV2Dto
  property_count: 4
  slug: fis-get-dispute-response-v2-dto
- name: GetEstimateResponseDto
  property_count: 4
  slug: fis-get-estimate-response-dto
- name: GetEstimateResponseV2Dto
  property_count: 3
  slug: fis-get-estimate-response-v2-dto
- name: GetExpenseResponseV2Dto
  property_count: 3
  slug: fis-get-expense-response-v2-dto
- name: IncomeStatementsResponseDto
  property_count: 3
  slug: fis-income-statements-response-dto
- name: PaymentRequest
  property_count: 8
  slug: fis-payment-request
- name: FIS Payment
  property_count: 15
  slug: fis-payment
- name: PostBillPaymentRequestResponseV2Dto
  property_count: 7
  slug: fis-post-bill-payment-request-response-v2-dto
- name: PostBusinessesResponseDto
  property_count: 6
  slug: fis-post-businesses-response-dto
- name: PostBusinessesResponseDtoV2
  property_count: 6
  slug: fis-post-businesses-response-dto-v2
- name: PushAttachmentResponseV1Dto
  property_count: 6
  slug: fis-push-attachment-response-v1-dto
- name: PushAttachmentV1Dto
  property_count: 3
  slug: fis-push-attachment-v1-dto
- name: PushAttachmentV2Dto
  property_count: 3
  slug: fis-push-attachment-v2-dto
- name: PushAttachmentV2ResponseDto
  property_count: 7
  slug: fis-push-attachment-v2-response-dto
- name: PushBankAccountResponseV2Dto
  property_count: 7
  slug: fis-push-bank-account-response-v2-dto
- name: PushBankTransactionResponseDto
  property_count: 3
  slug: fis-push-bank-transaction-response-dto
- name: PushBankTransactionResponseV2Dto
  property_count: 7
  slug: fis-push-bank-transaction-response-v2-dto
- name: PushBankTransfersResponseDto
  property_count: 6
  slug: fis-push-bank-transfers-response-dto
- name: PushBankTransfersResponseV2Dto
  property_count: 7
  slug: fis-push-bank-transfers-response-v2-dto
- name: PushBillCreditNoteResponseDto
  property_count: 6
  slug: fis-push-bill-credit-note-response-dto
- name: PushBillCreditNoteResponseV2Dto
  property_count: 7
  slug: fis-push-bill-credit-note-response-v2-dto
- name: PushBillPaymentResponseDto
  property_count: 6
  slug: fis-push-bill-payment-response-dto
- name: PushBillPaymentResponseV2Dto
  property_count: 7
  slug: fis-push-bill-payment-response-v2-dto
- name: PushBillResponseDto
  property_count: 6
  slug: fis-push-bill-response-dto
- name: PushBillResponseV2Dto
  property_count: 7
  slug: fis-push-bill-response-v2-dto
- name: PushChartOfAccountV1Dto
  property_count: 2
  slug: fis-push-chart-of-account-v1-dto
- name: PushChartOfAccountV1ResponseDto
  property_count: 6
  slug: fis-push-chart-of-account-v1-response-dto
- name: PushChartOfAccountV2ResponseDto
  property_count: 7
  slug: fis-push-chart-of-account-v2-response-dto
- name: PushCustomerBankAccountResponseDto
  property_count: 7
  slug: fis-push-customer-bank-account-response-dto
- name: PushCustomerV1Dto
  property_count: 2
  slug: fis-push-customer-v1-dto
- name: PushCustomerV1ResponseDto
  property_count: 6
  slug: fis-push-customer-v1-response-dto
- name: PushCustomerV2ResponseDto
  property_count: 7
  slug: fis-push-customer-v2-response-dto
- name: PushDepositV1Dto
  property_count: 2
  slug: fis-push-deposit-v1-dto
- name: PushDepositV1ResponseDto
  property_count: 6
  slug: fis-push-deposit-v1-response-dto
- name: PushDepositV2Dto
  property_count: 2
  slug: fis-push-deposit-v2-dto
- name: PushDepositV2ResponseDto
  property_count: 7
  slug: fis-push-deposit-v2-response-dto
- name: PushEstimateV1Dto
  property_count: 2
  slug: fis-push-estimate-v1-dto
- name: PushEstimateV1ResponseDto
  property_count: 6
  slug: fis-push-estimate-v1-response-dto
- name: PushEstimateV2Dto
  property_count: 2
  slug: fis-push-estimate-v2-dto
- name: PushEstimateV2ResponseDto
  property_count: 7
  slug: fis-push-estimate-v2-response-dto
- name: PushExpenseDto
  property_count: 2
  slug: fis-push-expense-dto
- name: PushExpenseeResponseDto
  property_count: 7
  slug: fis-push-expensee-response-dto
- name: PushFileUploadDto
  property_count: 2
  slug: fis-push-file-upload-dto
- name: PushFileUploadResponseDto
  property_count: 6
  slug: fis-push-file-upload-response-dto
- name: PushStatusResponseDto
  property_count: 3
  slug: fis-push-status-response-dto
- name: PushStatusResponseV2Dto
  property_count: 3
  slug: fis-push-status-response-v2-dto
- name: PushUpdateCustomerV1Dto
  property_count: 2
  slug: fis-push-update-customer-v1-dto
- name: PutBusinessesResponseDto
  property_count: 7
  slug: fis-put-businesses-response-dto
- name: PutBusinessesResponseDtoV2
  property_count: 7
  slug: fis-put-businesses-response-dto-v2
- name: PutCustomerV1ResponseDto
  property_count: 6
  slug: fis-put-customer-v1-response-dto
- name: PutCustomerV2ResponseDto
  property_count: 7
  slug: fis-put-customer-v2-response-dto
- name: SyncInfoResponseV2Dto
  property_count: 2
  slug: fis-sync-info-response-v2-dto
- name: TransactionList
  property_count: 3
  slug: fis-transaction-list
- name: UpdateBankTransactionResponseDto
  property_count: 7
  slug: fis-update-bank-transaction-response-dto
- name: UpdateBillPaymentResponseV2Dto
  property_count: 7
  slug: fis-update-bill-payment-response-v2-dto
- name: UpdateBillsResponseV1Dto
  property_count: 6
  slug: fis-update-bills-response-v1-dto
- name: UpdateBillsResponseV2Dto
  property_count: 7
  slug: fis-update-bills-response-v2-dto
- name: UpdateChartOfAccountV2ResponseDto
  property_count: 7
  slug: fis-update-chart-of-account-v2-response-dto
- name: WireTransferRequest
  property_count: 7
  slug: fis-wire-transfer-request
- name: WireTransfer
  property_count: 12
  slug: fis-wire-transfer
jsonld:
- class_count: 12
  name: Fis Context
  property_count: 10
  slug: fis-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.railz.ai over HTTP requiring OAuth.
  name: FIS Global MCP Server
  slug: fis-accounting-data-as-a-service-docs
modified: '2026-09-10'
name: FIS Global
nav: Providers
network: true
overview: 'FIS Global publishes 85 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, ACH API, Payments API, and 82 more. Tagged areas include Banking, Core Banking, Financial Services, Payments, and Fintech.


  The FIS Global catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  FIS Global''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, signup flow, and 43 more developer resources.'
plans:
- name: Fis Plans Pricing
  plan_count: 2
  slug: fis-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Fis Rate Limits
  slug: fis-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: FIS Global — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fis-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: FIS Global API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 5
  slug: fis-rules
scopes:
- name: Fis Scopes
  scope_count: 3
  slug: fis-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 37
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 79.4
    developer_ergonomics: 47.0
    discoverability: 66.7
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 60.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 93.9
      derived: 0
      marker_coverage: 93.9
      total: 82
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fis/fis-2026-06-20T181251.png
security:
- kind: authentication
  name: Fis Authentication
  slug: fis-authentication
  summary_line: http/basic · 2 schemes
- kind: domain-security
  name: Fis Domain Security
  slug: fis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fis Vulnerability Disclosure
  slug: fis-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Fis Trust Center
  slug: fis-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: fis-onboard-a-business-connection
  slug: fis-onboard-a-business-connection
- name: fis-push-a-record-into-the-ledger
  slug: fis-push-a-record-into-the-ledger
- name: fis-read-a-customers-financials
  slug: fis-read-a-customers-financials
slug: fis
tags:
- Banking
- Core Banking
- Financial Services
- Payments
- Fintech
website: https://www.fisglobal.com/
---
