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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Quickbooks Agentic Access
  operation_count: 150
  slug: quickbooks-agentic-access
  summary_line: 150 operations · 58 acting
api_count: 2
apis:
- description: GraphQL API for QuickBooks Online served from a single endpoint, https://api.intuit.com/graphql, covering the premium Projects, Custom Fields, Sales Tax and Sales Order APIs and payroll compensation u
  name: QuickBooks Online GraphQL API
  slug: graphql
- description: 'GraphQL API for QuickBooks Online Payroll data exposed through QuickBooks Workforce: company information, employees, compensation, payslips, benefits, deductions and pensions, served from the single e'
  name: QuickBooks Workforce Payroll API
  slug: payroll
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Accounts are what businesses use to track transactions. Accounts can track money coming in (income or revenue) and going out (expenses). They can also track the value of things (assets), like vehicles
  name: QuickBooks Account API
  slug: quickbooks-account-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the account list detail report from the QuickBooks Online Report Service.
  name: QuickBooks Account List Detail API
  slug: quickbooks-accountlistdetail-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the AP Aging Detail report from the QuickBooks Online Report Service.
  name: QuickBooks AP Aging Detail API
  slug: quickbooks-apagingdetail-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the AP Aging summary report from the QuickBooks Online Report Service.
  name: QuickBooks AP Aging Summary API
  slug: quickbooks-apagingsummary-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the AR Aging Detail report from the QuickBooks Online Report Service.
  name: QuickBooks AR Aging Detail API
  slug: quickbooks-aragingdetail-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the AR Aging Summary report from the QuickBooks Online Report Service.
  name: QuickBooks AR Aging Summary API
  slug: quickbooks-aragingsummary-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: This page covers the Attachable, Upload, and Download resources used for attachment management. Attachments are supplemental information linked to a transaction or Item object. They can be files, note
  name: QuickBooks Attachable API
  slug: quickbooks-attachable-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to query the Balance Sheet report from the QuickBooks Online Report Service.
  name: QuickBooks Balance Sheet API
  slug: quickbooks-balancesheet-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: 'The batch operation enables an application to perform multiple operations in a single request. For example, in a single batch request an application can create a customer, update an invoice, and read '
  name: QuickBooks Batch API
  slug: quickbooks-batch-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A Bill object is an AP transaction representing a request-for-payment from a third party for goods/services rendered, received, or both.
  name: QuickBooks Bill API
  slug: quickbooks-bill-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A BillPayment object represents the payment transaction for a bill that the business owner receives from a vendor for goods or services purchased from the vendor. QuickBooks Online supports bill payme
  name: QuickBooks Bill Payment API
  slug: quickbooks-billpayment-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The Budget endpoint allows you to retrieve the current state of budgets already set up in the user's company file. A budget allows for an amount to be assigned on a monthly, quarterly, or annual basis
  name: QuickBooks Budget API
  slug: quickbooks-budget-api
- baseURL: https://api.intuit.com
  baseurl_source: declared
  description: The card entity lets you create and store credit and debit card objects. Apps can store and use credit cards as a payment method for payment processing via the charges entity. Keep in mind, the card e
  name: QuickBooks Cards API
  slug: quickbooks-cards-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The change data capture (cdc) operation returns a list of objects that have changed since a specified time. This operation is for an app that periodically polls data services in order to refresh its l
  name: QuickBooks Change Data Capture API
  slug: quickbooks-changedatacapture-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A change order represents a modification to the scope of work on an existing project estimate. It captures additions or deletions to the original contracted work, and rolls up into the project's total
  name: QuickBooks Change Order API
  slug: quickbooks-changeorder-api
- baseURL: https://api.intuit.com
  baseurl_source: declared
  description: 'The charge entity lets you process, authorize, and capture payments for transactions (i.e. invoices and sales receipts) using credit cards and debit cards. Note: This entity can only be used for US-ba'
  name: QuickBooks Charges API
  slug: quickbooks-charges-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Class objects provide a way to track different segments of the business so they're not tied to a particular client or project. For example, you can define classes to break down the income and expenses
  name: QuickBooks Class API
  slug: quickbooks-class-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Applicable only for those companies that enable multicurrency, a companycurrency object defines a currency that is active in the QuickBooks Online company. One or more companycurrency objects are acti
  name: QuickBooks Company Currency API
  slug: quickbooks-companycurrency-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The CompanyInfo object contains basic company information. In QuickBooks, company info and preferences are displayed in the same place under preferences, so it may be confusing to figure out from user
  name: QuickBooks Company Info API
  slug: quickbooks-companyinfo-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Represents a financial transaction to record a Credit Card balance payment in QuickBooks Online. It provides an easy way for users to move money from a Bank account to a Credit Card account. It is ess
  name: QuickBooks Credit Card Payment API
  slug: quickbooks-creditcardpayment-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The CreditMemo object is a financial transaction representing a refund or credit of payment or part of a payment for goods or services that have been sold.
  name: QuickBooks Credit Memo API
  slug: quickbooks-creditmemo-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: 'A customer is a consumer of the service or product that your business offers. An individual customer can have an underlying nested structure, with a parent customer (the top-level object) having zero '
  name: QuickBooks Customer API
  slug: quickbooks-customer-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Customer Balance report from the QuickBooks Online Report Service.
  name: QuickBooks Customer Balance API
  slug: quickbooks-customerbalance-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Customer Balance Detail report from the QuickBooks Online Report Service.
  name: QuickBooks Customer Balance Detail API
  slug: quickbooks-customerbalancedetail-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Customer Income report from the QuickBooks Online Report Service.
  name: QuickBooks Customer Income API
  slug: quickbooks-customerincome-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Customer types allow categorizing customers in ways that are meaningful to the business. For example, one could set up customer types so that they indicate which industry a customer represents, a cust
  name: QuickBooks Customer Type API
  slug: quickbooks-customertype-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The Department resource provides a way to track transactions based on physical locations such as stores, sales regions, or countries. As you create sales and expense transactions, consistently designa
  name: QuickBooks Department API
  slug: quickbooks-department-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A deposit object is a transaction that records one or more deposits of the following types:A customer payment, originally held in the Undeposited Funds account, into the Asset Account specified by the
  name: QuickBooks Deposit API
  slug: quickbooks-deposit-api
- baseURL: https://api.intuit.com
  baseurl_source: declared
  description: 'The eCheck entity lets you create and store eCheck objects. Apps can store and use bank accounts as a payment method for payment processing via the charges entity. Note: This entity can only be used f'
  name: QuickBooks E Checks API
  slug: quickbooks-echecks-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: An Employee object represents a person working for the company. If you are looking to create a Contractor via API, refer how to create a Vendor object, with Vendor1099 field set to true.The DisplayNam
  name: QuickBooks Employee API
  slug: quickbooks-employee-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The Entitlements resource retrieves the features available to a company, identified by the company's realmID. The features available are determined by the type of company established during QuickBooks
  name: QuickBooks Entitlements API
  slug: quickbooks-entitlements-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The Estimate represents a proposal for a financial transaction from a business to a customer for goods or services proposed to be sold, including proposed pricing.
  name: QuickBooks Estimate API
  slug: quickbooks-estimate-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: 'The information below provides a reference on how to access the General Ledger Detail report from the QuickBooks Report Service. For each specified account, the report shows all the transactions that '
  name: QuickBooks General Ledger API
  slug: quickbooks-generalledger-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: InventoryAdjustment provides a way for customers to change the quantity of inventory items for various reasons, such as damage, stock write-off, shrinkage, or expiration. The change in quantity automa
  name: QuickBooks Inventory Adjustment API
  slug: quickbooks-inventoryadjustment-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Inventory Valuation Detail report from the QuickBooks Online Report Service.
  name: QuickBooks Inventory Valuation Detail API
  slug: quickbooks-inventoryvaluationdetail-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Inventory Valuation summary report from the QuickBooks Online Report Service.
  name: QuickBooks Inventory Valuation Summary API
  slug: quickbooks-inventoryvaluationsummary-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: An Invoice represents a sales form where the customer pays for a product or service later.
  name: QuickBooks Invoice API
  slug: quickbooks-invoice-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: An item is a thing that your company buys, sells, or re-sells, such as products and services. An item is shown as a line on an invoice or other sales form. The Item.Type attribute, which specifies how
  name: QuickBooks Item API
  slug: quickbooks-item-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the journal report from the QuickBooks Online Report Service. This report presents a summary of the journal code ledgers.
  name: QuickBooks Journal Report API
  slug: quickbooks-journalreport-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: 'A Payment object records a payment in QuickBooks. The payment can be applied for a particular customer against multiple Invoices and Credit Memos. It can also be created without any Invoice or Credit '
  name: QuickBooks Payment API
  slug: quickbooks-payment-api
- baseURL: https://api.intuit.com
  baseurl_source: declared
  description: Payments receipts are created for each invoice once the payment is received.
  name: QuickBooks Payment Receipt API
  slug: quickbooks-paymentreceipt-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The Preferences resource represents a set of company preferences that control application behavior in QuickBooks Online. They are mostly exposed as read-only through the Preferences endpoint with only
  name: QuickBooks Preferences API
  slug: quickbooks-preferences-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Profit and Loss Summary report from the QuickBooks Online Report Service.
  name: QuickBooks Profit And Loss API
  slug: quickbooks-profitandloss-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Profit and Loss Detail report from the QuickBooks Online Report Service.
  name: QuickBooks Profit And Loss Detail API
  slug: quickbooks-profitandlossdetail-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A Purchase object represents an expense, such as a purchase made from a vendor. Of note, You must specify an AccountRef for all purchases. The TotalAmtattribute must add up to sum of Line.Amount attri
  name: QuickBooks Purchase API
  slug: quickbooks-purchase-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: 'A RecurringTransaction object refers to scheduling the creation of transactions, setting up reminders, and creating transaction templates for later use. This feature is available in QuickBooks Online '
  name: QuickBooks Recurring Transaction API
  slug: quickbooks-recurringtransaction-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A RefundReceipt object represents a refund to the customer for a product or service that was provided.
  name: QuickBooks Refund Receipt API
  slug: quickbooks-refundreceipt-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A Reimburse Charge is a billable Expense. This happens when you mark your Expense/Bill lines as Billable to some customer to be invoiced later.
  name: QuickBooks Reimburse Charge API
  slug: quickbooks-reimbursecharge-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the sales by class summary report from the QuickBooks Online Report Service.
  name: QuickBooks Sales By Class Summary API
  slug: quickbooks-salesbyclasssummary-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Sales by Customer report from the QuickBooks Online Report Service.
  name: QuickBooks Sales By Customer API
  slug: quickbooks-salesbycustomer-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Sales by Department report from the QuickBooks Online Report Service.
  name: QuickBooks Sales By Department API
  slug: quickbooks-salesbydepartment-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Sales by Product report from the QuickBooks Online Report Service.
  name: QuickBooks Sales By Product API
  slug: quickbooks-salesbyproduct-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A SalesReceipt object represents the sales receipt that is given to a customer. A sales receipt is similar to an invoice. However, for a sales receipt, payment is received as part of the sale of goods
  name: QuickBooks Sales Receipt API
  slug: quickbooks-salesreceipt-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A TaxAgency object is associated with a tax rate and identifies the agency to which that tax rate applies, that is, the entity that collects those taxes. QuickBooks companies based in the US will only
  name: QuickBooks Tax Agency API
  slug: quickbooks-taxagency-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Tax classification segregates different items into different classifications and the tax classification is one of the key parameters to determine appropriate tax on transactions involving items. Tax c
  name: QuickBooks Tax Classification API
  slug: quickbooks-taxclassification-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A TaxCode object is used to track the taxable or non-taxable status of products, services, and customers. You can assign a sales tax code to each of your products, services, and customers based on the
  name: QuickBooks Tax Code API
  slug: quickbooks-taxcode-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Tax Payment/Refund made against filed taxReturn. Applicable for AU, CA and UK locales only.
  name: QuickBooks Tax Payment API
  slug: quickbooks-taxpayment-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: 'The TaxService resource allows you to perform the following actions: Create a new TaxCode object and specify a list of existing tax rates to be associated to that tax code. To retrieve a list of exist'
  name: QuickBooks Tax Service API
  slug: quickbooks-taxservice-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Applicable for non-US locale companies only. The information below provides a reference on how to access the Tax Summary report from the QuickBooks Online Report Service.
  name: QuickBooks Tax Summary API
  slug: quickbooks-taxsummary-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A Term object represents the terms under which a sale is made, typically expressed in the form of days due after the goods are received. Optionally, a discount of the total amount may be applied if pa
  name: QuickBooks Term API
  slug: quickbooks-term-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The TimeActivity object represents a record of time worked by a vendor or employee.
  name: QuickBooks Time Activity API
  slug: quickbooks-timeactivity-api
- baseURL: https://api.intuit.com
  baseurl_source: declared
  description: 'The token entity lets you create opaque containers to mask cardholder''s credit card or bank account info. Your app can use the token to make API calls and process payments without reading or exposing '
  name: QuickBooks Tokens API
  slug: quickbooks-tokens-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Transaction List report from the QuickBooks Online Report Service.
  name: QuickBooks Transaction List API
  slug: quickbooks-transactionlist-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Transaction List By Customer report from the QuickBooks Online Report Service.
  name: QuickBooks Transaction List By Customer API
  slug: quickbooks-transactionlistbycustomer-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Transaction List By Vendor report from the QuickBooks Online Report Service.
  name: QuickBooks Transaction List By Vendor API
  slug: quickbooks-transactionlistbyvendor-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Transaction List With Splits report from the QuickBooks Online Report Service.
  name: QuickBooks Transaction List With Splits API
  slug: quickbooks-transactionlistwithsplits-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A Transfer represents a transaction where funds are moved between two accounts from the company's QuickBooks chart of accounts.
  name: QuickBooks Transfer API
  slug: quickbooks-transfer-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Trial Balance report from the QuickBooks Online Report Service. For France-based companies, use TrialBalanceFR as the endpoint.
  name: QuickBooks Trial Balance API
  slug: quickbooks-trialbalance-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The Vendor object represents the seller from whom your company purchases any service or product.
  name: QuickBooks Vendor API
  slug: quickbooks-vendor-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Vendor Balance report from the QuickBooks Online Report Service.
  name: QuickBooks Vendor Balance API
  slug: quickbooks-vendorbalance-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Vendor Balance Detail report from the QuickBooks Online Report Service.
  name: QuickBooks Vendor Balance Detail API
  slug: quickbooks-vendorbalancedetail-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The VendorCredit object is an accounts payable transaction that represents a refund or credit of payment for goods or services. It is a credit that a vendor owes you for various reasons such as overpa
  name: QuickBooks Vendor Credit API
  slug: quickbooks-vendorcredit-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the Expenses by Vendor report from the QuickBooks Online Report Service.
  name: QuickBooks Vendor Expenses API
  slug: quickbooks-vendorexpenses-api
- baseURL: https://api.intuit.com
  baseurl_source: declared
  description: 'The bankAccount entity lets you create and update bank account objects. Apps can store and use bank accounts as a payment method for payment processing via the charges entity. Note: This entity can on'
  name: QuickBooks Bank Accounts API
  slug: quickbooks-bank-accounts-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The information below provides a reference on how to access the cash flow report from the QuickBooks Online Report Service.
  name: QuickBooks Cash Flow API
  slug: quickbooks-cash-flow-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: Applicable only for those companies that enable multicurrency, the exchangerate resource provides the ability to query and set exchange rates available to the QuickBooks Online company. This entity wo
  name: QuickBooks Exchange Rate API
  slug: quickbooks-exchange-rate-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: JournalEntry is a transaction in which:There are at least one pair of lines, a debit and a credit, called distribution lines. Each distribution line has an account from the Chart of Accounts. Query th
  name: QuickBooks Journal Entry API
  slug: quickbooks-journal-entry-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The PaymentMethod resource provides the method of payment for received goods. Delete is achieved by setting the Active attribute to false in an object update request; thus, making it inactive. In this
  name: QuickBooks Payment Method API
  slug: quickbooks-payment-method-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: The PurchaseOrder object is a non-posting transaction representing a request to purchase goods or services from a third party.
  name: QuickBooks Purchase Order API
  slug: quickbooks-purchase-order-api
- baseURL: https://quickbooks.api.intuit.com
  baseurl_source: declared
  description: A TaxRate object represents rate applied to calculate tax liability. Use the TaxService entity to create a taxrate. See Global tax model for more information about using TaxRate objects and the tax mo
  name: QuickBooks Tax Rate API
  slug: quickbooks-tax-rate-api
artifact_total: 110
asyncapis:
- description: AsyncAPI 2.6 description of the QuickBooks Online (QBO) Data Services webhook surface. QuickBooks Online delivers asynchronous notifications of data-change events on the configured Intuit App by issui
  name: QuickBooks Online Webhooks
  slug: quickbooks-online-webhooks-asyncapi
common:
- group: other
  href: https://artifacts.apis.io/quickbooks/capabilities/quickbooks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/quickbooks-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/quickbooks/rate-limits/quickbooks-payments-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quickbooks-payments-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/quickbooks/well-known/quickbooks-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quickbooks-status-security.txt
- group: agent
  href: https://artifacts.apis.io/quickbooks/agentic-access/quickbooks-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quickbooks-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/quickbooks/rate-limits/quickbooks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quickbooks-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/quickbooks/plans/quickbooks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quickbooks-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/rules/quickbooks-rules.yml
  title: ''
  type: Spectral
  url: rules/quickbooks-rules.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/rules/quickbooks-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/quickbooks-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/json-ld/quickbooks-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/quickbooks-context.jsonld
- group: design
  href: https://artifacts.apis.io/quickbooks/vocabulary/quickbooks-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/quickbooks-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/quickbooks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/asyncapi/quickbooks-online-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/quickbooks-online-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/data-model/quickbooks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quickbooks-data-model.yml
- group: operate
  href: https://artifacts.apis.io/quickbooks/changelog/quickbooks-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/quickbooks-changelog.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/conventions/quickbooks-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/quickbooks-conventions.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/conventions/quickbooks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/quickbooks-conventions.yml
- group: start
  href: https://artifacts.apis.io/quickbooks/sandbox/quickbooks-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/quickbooks-sandbox.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.developer.intuit.com/
- group: design
  href: https://artifacts.apis.io/quickbooks/lifecycle/quickbooks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/quickbooks-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/quickbooks/errors/quickbooks-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/quickbooks-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/errors/quickbooks-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/quickbooks-problem-types.yml
- group: design
  href: https://artifacts.apis.io/quickbooks/conformance/quickbooks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quickbooks-conformance.yml
- group: agent
  href: https://artifacts.apis.io/quickbooks/llms/quickbooks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quickbooks-llms.txt
- group: build
  href: https://artifacts.apis.io/quickbooks/mcp/quickbooks-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/quickbooks-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/quickbooks/well-known/quickbooks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quickbooks-well-known.yml
- group: other
  href: https://artifacts.apis.io/quickbooks/hosts/quickbooks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quickbooks-hosts.yml
- group: build
  href: https://artifacts.apis.io/quickbooks/integrations/quickbooks-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/quickbooks-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/quickbooks/vendors/quickbooks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quickbooks-vendors.yml
- group: build
  href: https://artifacts.apis.io/quickbooks/packages/quickbooks-packages.yml
  title: ''
  type: SDKs
  url: packages/quickbooks-packages.yml
- group: build
  href: https://artifacts.apis.io/quickbooks/packages/quickbooks-packages.yml
  title: ''
  type: Packages
  url: packages/quickbooks-packages.yml
- group: auth
  href: https://artifacts.apis.io/quickbooks/authentication/quickbooks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quickbooks-authentication.yml
- group: auth
  href: https://artifacts.apis.io/quickbooks/scopes/quickbooks-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/quickbooks-scopes.yml
- group: auth
  href: https://artifacts.apis.io/quickbooks/security/quickbooks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quickbooks-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/quickbooks
- group: company
  title: ''
  type: Website
  url: https://quickbooks.intuit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.intuit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.intuit.com/app/developer/qbo/docs/develop
- group: docs
  title: ''
  type: APIReference
  url: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/account
- group: start
  title: ''
  type: SignUp
  url: https://developer.intuit.com/app/developer/homepage
- group: commercial
  title: ''
  type: Pricing
  url: https://quickbooks.intuit.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intuit
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/intuit/quickbooks-online-mcp-server
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/intuit-developer/intuit-developer-quickbooks-online-accounting-api/overview
- group: operate
  title: ''
  type: Support
  url: https://help.developer.intuit.com/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.intuit.com/app/developer/qbo/docs/legal-agreements/intuit-terms-of-service-for-intuit-developer-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intuit.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/intuitdev
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.intuit.com/app/developer/qbo/docs/release-notes
created: '2026-05-11'
description: QuickBooks is Intuit's accounting software platform for small businesses, self-employed, and accountants, available as QuickBooks Online (cloud) and QuickBooks Desktop. The QuickBooks Online Accounting REST API provides programmatic access to a company's financial data, allowing developers to read, create, update, and delete accounting objects including invoices, customers, payments, bills, vendors, items, and tax data using OAuth 2.0 and JSON over HTTPS.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quickbooks.png
json_schemas:
- name: bankaccount
  property_count: 14
  slug: quickbooks-bankaccount
- name: bankaccountrequest
  property_count: 9
  slug: quickbooks-bankaccountrequest
- name: card
  property_count: 17
  slug: quickbooks-card
- name: chargerequest
  property_count: 8
  slug: quickbooks-chargerequest
- name: chargeresponse
  property_count: 16
  slug: quickbooks-chargeresponse
- name: creditmemoresponse
  property_count: 32
  slug: quickbooks-creditmemoresponse
- name: customerresponse
  property_count: 42
  slug: quickbooks-customerresponse
- name: echeckresponse
  property_count: 12
  slug: quickbooks-echeckresponse
- name: estimateresponse
  property_count: 38
  slug: quickbooks-estimateresponse
- name: invoiceresponse
  property_count: 51
  slug: quickbooks-invoiceresponse
- name: refundreceiptresponse
  property_count: 35
  slug: quickbooks-refundreceiptresponse
- name: salesreceiptresponse
  property_count: 40
  slug: quickbooks-salesreceiptresponse
jsonld:
- class_count: 120
  name: Quickbooks Context
  property_count: 370
  slug: quickbooks-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-11-05'
name: QuickBooks
nav: Providers
network: true
overview: 'QuickBooks publishes 82 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account List Detail API, AP Aging Detail API, and 79 more. Tagged areas include Accounting, Bookkeeping, Small Business, Finance, and Invoicing.


  The QuickBooks catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  QuickBooks'' developer surface includes changelog, sandbox, authentication, documentation, API reference, signup flow, pricing, and 42 more developer resources.'
plans:
- name: Quickbooks Plans Pricing
  plan_count: 4
  slug: quickbooks-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Quickbooks Payments Rate Limits
  slug: quickbooks-payments-rate-limits
- limit_count: 12
  name: Quickbooks Rate Limits
  slug: quickbooks-rate-limits
rules:
- authorship: generated
  effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: QuickBooks — asyncapi rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: quickbooks-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: QuickBooks API Rules
  rule_count: 71
  severity_counts:
    error: 60
    hint: 0
    info: 2
    warn: 9
  slug: quickbooks-rules
scopes:
- name: Quickbooks Scopes
  scope_count: 19
  slug: quickbooks-scopes
  summary_line: 19 scopes · authorizationCode
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 26.9
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 35.7
    developer_ergonomics: 74.4
    discoverability: 65.0
    operational_transparency: 81.6
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 80
      marker_coverage: 100.0
      total: 80
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/quickbooks/quickbooks-2026-06-20T192434.png
security:
- kind: authentication
  name: Quickbooks Authentication
  slug: quickbooks-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Quickbooks Domain Security
  slug: quickbooks-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: quickbooks-invoice-to-cash
  slug: quickbooks-invoice-to-cash
- name: quickbooks-payments-charge-and-refund
  slug: quickbooks-payments-charge-and-refund
- name: quickbooks-record-and-pay-bill
  slug: quickbooks-record-and-pay-bill
- name: quickbooks-sync-changes
  slug: quickbooks-sync-changes
slug: quickbooks
tags:
- Accounting
- Bookkeeping
- Small Business
- Finance
- Invoicing
- Payroll
- Tax
website: https://quickbooks.intuit.com/
---
