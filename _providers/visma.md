---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-09-16'
api_count: 7
apis:
- description: 'GraphQL API for Business NXT, Visma''s ERP for mid-market Nordic customers. Two endpoints share one schema: /api/graphql for a Visma.net user context (authorization code with PKCE) and /api/graphql-ser'
  name: Visma Business NXT GraphQL API
  slug: visma-business-nxt-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Account API from Visma — 2 operation(s) for account.
  name: Visma Account API
  slug: visma-account-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'The bookkeeping accounts used to categorize financial transactions within your company. Overview of Accounts Functionality: [Accounts](https://support.spiris.se/bokforing-fakturering-plus/en-se/conten'
  name: Visma Accounts API
  slug: visma-accounts-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Creating or getting agreements for the company.
  name: Visma Agreements API
  slug: visma-agreements-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The periods used to distribute or allocate revenues and expenses across specific dates or accounting periods. Allocation periods help ensure accurate financial reporting and matching of income and cos
  name: Visma Allocation Periods API
  slug: visma-allocationperiods-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Handles approval operations for various document types including supplier invoice drafts and VAT reports. <br><br> ___ Available in any of the following variants: * Pro * Standard * Bookkeeping * Solo'
  name: Visma Approval API
  slug: visma-approval-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'App store activation status management for third-party integrations. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Bookkeeping * Solo'
  name: Visma App Store Activation Status API
  slug: visma-appstoreactivationstatus-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Article account codings define the accounting rules and VAT settings for articles (products/services) in the system. Overview of Article Account Codings Functionality: [Article Account Codings](https:'
  name: Visma Article Account Codings API
  slug: visma-articleaccountcodings-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Groups used to categorise and organise the articles. Overview of Article Labels Functionality: [Article labels](https://support.spiris.se/bokforing-fakturering-plus/en-se/content/online-help/settings-'
  name: Visma Article Labels API
  slug: visma-articlelabels-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'A product or service that the company offers to customers, used on quotes and invoices. Overview of Articles Functionality: [Articles](https://support.spiris.se/bokforing-fakturering/en-se/content/onl'
  name: Visma Articles API
  slug: visma-articles-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Attachment API from Visma — 1 operation(s) for attachment.
  name: Visma Attachment API
  slug: visma-attachment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Links that connect attachments, such as documents or images, to related records like invoices or vouchers. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Bookk'
  name: Visma Attachment Links API
  slug: visma-attachmentlinks-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Files or documents that can be linked to records such as supplier invoices and vouchers. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Bookkeeping * Solo'
  name: Visma Attachments API
  slug: visma-attachments-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Attribute API from Visma — 2 operation(s) for attribute.
  name: Visma Attribute API
  slug: visma-attribute-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Background API from Visma — 2 operation(s) for background.
  name: Visma Background API
  slug: visma-background-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Available banks in the system for banking operations and integrations. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Bookkeeping * Solo'
  name: Visma Bank API
  slug: visma-bank-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Blob API from Visma — 3 operation(s) for blob.
  name: Visma Blob API
  slug: visma-blob-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Branch API from Visma — 3 operation(s) for branch.
  name: Visma Branch API
  slug: visma-branch-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Creating or getting break rules of the company.
  name: Visma Break Rule API
  slug: visma-breakrule-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Budget API from Visma — 1 operation(s) for budget.
  name: Visma Budget API
  slug: visma-budget-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing care of sick child shortcuts for employees. Care of sick child shortcuts allow tracking of employee leaves related to caring for sick children.
  name: Visma Care Of Sick Child API
  slug: visma-careofsickchild-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing care of sick child shortcuts for employees. Care of sick child shortcuts allow tracking of employee leaves related to caring for sick children.
  name: Visma Care Of Sick Children API
  slug: visma-careofsickchildren-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Carrier API from Visma — 2 operation(s) for carrier.
  name: Visma Carrier API
  slug: visma-carrier-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CashAccount API from Visma — 2 operation(s) for cashaccount.
  name: Visma Cash Account API
  slug: visma-cashaccount-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CashSale API from Visma — 2 operation(s) for cashsale.
  name: Visma Cash Sale API
  slug: visma-cashsale-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CashTransaction API from Visma — 5 operation(s) for cashtransaction.
  name: Visma Cash Transaction API
  slug: visma-cashtransaction-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Contact API from Visma — 2 operation(s) for contact.
  name: Visma Contact API
  slug: visma-contact-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ContractTemplate API from Visma — 1 operation(s) for contracttemplate.
  name: Visma Contract Template API
  slug: visma-contracttemplate-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ContractUsage API from Visma — 2 operation(s) for contractusage.
  name: Visma Contract Usage API
  slug: visma-contractusage-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Items that belong to cost centers, used for project tracking and cost allocation. Overview of Cost Center Items Functionality: [Cost Centers](https://support.spiris.se/bokforing-fakturering-plus/en-se'
  name: Visma Cost Center Items API
  slug: visma-costcenteritems-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'The country information used for customers, suppliers, and addresses in the company. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Solo * Bookkeeping * Payrol'
  name: Visma Countries API
  slug: visma-countries-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Country API from Visma — 2 operation(s) for country.
  name: Visma Country API
  slug: visma-country-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CreditTerm API from Visma — 1 operation(s) for creditterm.
  name: Visma Credit Term API
  slug: visma-creditterm-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'The monetary unit for business transactions. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Bookkeeping * InvoicingCollaboration * Solo'
  name: Visma Currencies API
  slug: visma-currencies-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Currency API from Visma — 2 operation(s) for currency.
  name: Visma Currency API
  slug: visma-currency-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CurrencyRate API from Visma — 2 operation(s) for currencyrate.
  name: Visma Currency Rate API
  slug: visma-currencyrate-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CurrencyRateType API from Visma — 1 operation(s) for currencyratetype.
  name: Visma Currency Rate Type API
  slug: visma-currencyratetype-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Customer API from Visma — 18 operation(s) for customer.
  name: Visma Customer API
  slug: visma-customer-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerCreditNote API from Visma — 7 operation(s) for customercreditnote.
  name: Visma Customer Credit Note API
  slug: visma-customercreditnote-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerCreditNoteV2 API from Visma — 1 operation(s) for customercreditnotev2.
  name: Visma Customer Credit Note V2 API
  slug: visma-customercreditnotev2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerCreditWriteOff API from Visma — 2 operation(s) for customercreditwriteoff.
  name: Visma Customer Credit Write Off API
  slug: visma-customercreditwriteoff-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerDebitNote API from Visma — 7 operation(s) for customerdebitnote.
  name: Visma Customer Debit Note API
  slug: visma-customerdebitnote-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerDebitNoteV2 API from Visma — 1 operation(s) for customerdebitnotev2.
  name: Visma Customer Debit Note V2 API
  slug: visma-customerdebitnotev2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerDocument API from Visma — 1 operation(s) for customerdocument.
  name: Visma Customer Document API
  slug: visma-customerdocument-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerInvoice API from Visma — 12 operation(s) for customerinvoice.
  name: Visma Customer Invoice API
  slug: visma-customerinvoice-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Draft invoices sent to customers before they are finalized and posted to the accounting system. Overview of Customer Invoice Functionality: [Customer Invoices](https://support.spiris.se/bokforing-fakt'
  name: Visma Customer Invoice Drafts API
  slug: visma-customerinvoicedrafts-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerInvoiceV2 API from Visma — 1 operation(s) for customerinvoicev2.
  name: Visma Customer Invoice V2 API
  slug: visma-customerinvoicev2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Groups used to categorise and organise the customers. Overview of Customer Labels Functionality: [Customer Labels](https://support.spiris.se/bokforing-fakturering-plus/en-se/content/online-help/custom'
  name: Visma Customer Labels API
  slug: visma-customerlabels-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'A record of a financial transaction affecting a customer account, such as invoices, payments, or credit notes. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * S'
  name: Visma Customer Ledger Items API
  slug: visma-customerledgeritems-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerOverdueCharge API from Visma — 5 operation(s) for customeroverduecharge.
  name: Visma Customer Overdue Charge API
  slug: visma-customeroverduecharge-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerPayment API from Visma — 4 operation(s) for customerpayment.
  name: Visma Customer Payment API
  slug: visma-customerpayment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerPaymentMethod API from Visma — 3 operation(s) for customerpaymentmethod.
  name: Visma Customer Payment Method API
  slug: visma-customerpaymentmethod-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Organizations or individuals that purchase goods or services from your business. Overview of Customer Functionality: [Customers](https://support.spiris.se/bokforing-fakturering-plus/en-se/content/onli'
  name: Visma Customers API
  slug: visma-customers-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerSalesPrice API from Visma — 2 operation(s) for customersalesprice.
  name: Visma Customer Sales Price API
  slug: visma-customersalesprice-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The CustomerV2 API from Visma — 1 operation(s) for customerv2.
  name: Visma Customer V2 API
  slug: visma-customerv2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The DeferralCode API from Visma — 2 operation(s) for deferralcode.
  name: Visma Deferral Code API
  slug: visma-deferralcode-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Ways or means by which goods are delivered to the customer. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Solo'
  name: Visma Delivery Methods API
  slug: visma-deliverymethods-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Department API from Visma — 2 operation(s) for department.
  name: Visma Department API
  slug: visma-department-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Dimension API from Visma — 5 operation(s) for dimension.
  name: Visma Dimension API
  slug: visma-dimension-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Discount API from Visma — 4 operation(s) for discount.
  name: Visma Discount API
  slug: visma-discount-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Agreements that define specific discount terms and conditions for customers. Overview of Discount Agreement Functionality: [Discount Agreements](https://support.spiris.se/bokforing-fakturering-plus/en'
  name: Visma Discount Agreements API
  slug: visma-discountagreements-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The DiscountCodeV2 API from Visma — 1 operation(s) for discountcodev2.
  name: Visma Discount Code V2 API
  slug: visma-discountcodev2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The DiscountV2 API from Visma — 1 operation(s) for discountv2.
  name: Visma Discount V2 API
  slug: visma-discountv2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Documents represent uploaded or generated files, such as VAT reports PDF''s and backgrounds. <br><br> ___ Available in any of the following variants: * Pro * Standard * Bookkeeping * Invoicing * Solo'
  name: Visma Documents API
  slug: visma-documents-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The EarningType API from Visma — 2 operation(s) for earningtype.
  name: Visma Earning Type API
  slug: visma-earningtype-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Employee API from Visma — 6 operation(s) for employee.
  name: Visma Employee API
  slug: visma-employee-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Managing employees in your company's payroll system. You can retrieve employee information including personal details, contract status, employment agreements, work schedules, holiday balances, and tim
  name: Visma Employees API
  slug: visma-employees-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ExpenseClaim API from Visma — 5 operation(s) for expenseclaim.
  name: Visma Expense Claim API
  slug: visma-expenseclaim-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ExpenseReceipt API from Visma — 3 operation(s) for expensereceipt.
  name: Visma Expense Receipt API
  slug: visma-expensereceipt-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for reporting per-employee values for a deviation period from an external system. An external period carries a percentage-based project/cost-center distribution for the employee's worked ti
  name: Visma External Periods API
  slug: visma-externalperiods-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The FeaturesSet API from Visma — 1 operation(s) for featuresset.
  name: Visma Features Set API
  slug: visma-featuresset-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The FinancialPeriod API from Visma — 2 operation(s) for financialperiod.
  name: Visma Financial Period API
  slug: visma-financialperiod-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The FirstTimeStartup API from Visma — 1 operation(s) for firsttimestartup.
  name: Visma First Time Startup API
  slug: visma-firsttimestartup-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The FixedAsset API from Visma — 2 operation(s) for fixedasset.
  name: Visma Fixed Asset API
  slug: visma-fixedasset-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The FixedAssetClass API from Visma — 2 operation(s) for fixedassetclass.
  name: Visma Fixed Asset Class API
  slug: visma-fixedassetclass-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The FixedAssetPropertyTaxGroup API from Visma — 2 operation(s) for fixedassetpropertytaxgroup.
  name: Visma Fixed Asset Property Tax Group API
  slug: visma-fixedassetpropertytaxgroup-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The FixedAssetTransaction API from Visma — 2 operation(s) for fixedassettransaction.
  name: Visma Fixed Asset Transaction API
  slug: visma-fixedassettransaction-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Foreign payment codes used for international transactions with suppliers outside the company''s home country. <br><br> ___ Available in any of the following variants: * Pro * Standard * Bookkeeping * S'
  name: Visma Foreign Payment Codes API
  slug: visma-foreignpaymentcodes-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The GeneralLedgerBalanceV2 API from Visma — 1 operation(s) for generalledgerbalancev2.
  name: Visma General Ledger Balance V2 API
  slug: visma-generalledgerbalancev2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The GeneralLedgerTransactions API from Visma — 1 operation(s) for generalledgertransactions.
  name: Visma General Ledger Transactions API
  slug: visma-generalledgertransactions-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing holiday shortcuts for employees. Holiday shortcuts allow tracking of employee holiday/vacation periods.
  name: Visma Holiday API
  slug: visma-holiday-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing hours worked shortcuts for employees. Hours worked shortcuts allow tracking of employee worked time.
  name: Visma Hours Worked API
  slug: visma-hoursworked-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Inventory API from Visma — 16 operation(s) for inventory.
  name: Visma Inventory API
  slug: visma-inventory-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The InventoryAdjustment API from Visma — 3 operation(s) for inventoryadjustment.
  name: Visma Inventory Adjustment API
  slug: visma-inventoryadjustment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The InventoryIssue API from Visma — 3 operation(s) for inventoryissue.
  name: Visma Inventory Issue API
  slug: visma-inventoryissue-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The InventorySummary API from Visma — 1 operation(s) for inventorysummary.
  name: Visma Inventory Summary API
  slug: visma-inventorysummary-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The InventoryTransfer API from Visma — 3 operation(s) for inventorytransfer.
  name: Visma Inventory Transfer API
  slug: visma-inventorytransfer-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The JournalTransactionV2 API from Visma — 5 operation(s) for journaltransactionv2.
  name: Visma Journal Transaction V2 API
  slug: visma-journaltransactionv2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The KitAssembly API from Visma — 3 operation(s) for kitassembly.
  name: Visma Kit Assembly API
  slug: visma-kitassembly-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The KitSpecifications API from Visma — 3 operation(s) for kitspecifications.
  name: Visma Kit Specifications API
  slug: visma-kitspecifications-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The LandedCostCode API from Visma — 2 operation(s) for landedcostcode.
  name: Visma Landed Cost Code API
  slug: visma-landedcostcode-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Ledger API from Visma — 1 operation(s) for ledger.
  name: Visma Ledger API
  slug: visma-ledger-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Location API from Visma — 3 operation(s) for location.
  name: Visma Location API
  slug: visma-location-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The LotSerialClass API from Visma — 2 operation(s) for lotserialclass.
  name: Visma Lot Serial Class API
  slug: visma-lotserialclass-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Comments or observations that can be attached to various documents and entities in the system. Overview of Notes Functionality: [Notes](https://support.spiris.se/bokforing-fakturering-plus/en-se/conte'
  name: Visma Notes API
  slug: visma-notes-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The NumberSequence API from Visma — 2 operation(s) for numbersequence.
  name: Visma Number Sequence API
  slug: visma-numbersequence-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'A confirmed request for products or services to be delivered. Overview of Orders Functionality: [Orders](https://support.spiris.se/bokforing-fakturering-plus/en-se/content/online-help/sales-order.htm)'
  name: Visma Orders API
  slug: visma-orders-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Organization API from Visma — 3 operation(s) for organization.
  name: Visma Organization API
  slug: visma-organization-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing other absence shortcuts for employees. Other absence shortcuts allow tracking of employee other (non-specific) absence/leave periods with configurable registration methods (tim
  name: Visma Other Absence API
  slug: visma-otherabsence-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing other addition and deduction shortcuts for employees. Other addition and deduction shortcuts allow tracking of employee additions and/or deductions based on supplied pay code n
  name: Visma Other Addition Deduction API
  slug: visma-otheradditiondeduction-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing overtime shortcuts for employees. Overtime shortcuts allow tracking of employee overtime periods with configurable registration methods (time or hours).
  name: Visma Overtime API
  slug: visma-overtime-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The PackagingType API from Visma — 2 operation(s) for packagingtype.
  name: Visma Packaging Type API
  slug: visma-packagingtype-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing parental leave shortcuts for employees. Parental leave shortcuts allow tracking of employee leaves related to parental responsibilities.
  name: Visma Parental Leave API
  slug: visma-parentalleave-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Links or references related to a partner, such as external resources or connected documents. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Bookkeeping * Solo'
  name: Visma Partner Resource Links API
  slug: visma-partnerresourcelinks-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Managing paycodes in your company's payroll system. You can retrieve all paycodes, paycode by specified id and specific travel and expense paycodes, other additional deduction paycodes.
  name: Visma Paycodes API
  slug: visma-paycodes-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Payment API from Visma — 4 operation(s) for payment.
  name: Visma Payment API
  slug: visma-payment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'A record of a payment transaction used to register customer or supplier invoice payments. <br><br> ___ Available in any of the following variants: * Pro * Standard * Bookkeeping * Solo'
  name: Visma Payment Voucher API
  slug: visma-paymentvoucher-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing employee payslips. Use this to retrieve a single payslip or list payslips for a specific employee or wage run in your company's payroll system.
  name: Visma Payslips API
  slug: visma-payslips-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Project API from Visma — 7 operation(s) for project.
  name: Visma Project API
  slug: visma-project-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ProjectAccountGroup API from Visma — 2 operation(s) for projectaccountgroup.
  name: Visma Project Account Group API
  slug: visma-projectaccountgroup-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ProjectBasic API from Visma — 1 operation(s) for projectbasic.
  name: Visma Project Basic API
  slug: visma-projectbasic-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ProjectBudget API from Visma — 2 operation(s) for projectbudget.
  name: Visma Project Budget API
  slug: visma-projectbudget-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Projects that track work and expenses for specific customers or initiatives. Overview of Project Functionality: [Projects](https://support.spiris.se/bokforing-fakturering/en-se/content/online-help/acc'
  name: Visma Projects API
  slug: visma-projects-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ProjectTask API from Visma — 2 operation(s) for projecttask.
  name: Visma Project Task API
  slug: visma-projecttask-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The ProjectTransaction API from Visma — 2 operation(s) for projecttransaction.
  name: Visma Project Transaction API
  slug: visma-projecttransaction-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The PurchaseOrderBasic API from Visma — 2 operation(s) for purchaseorderbasic.
  name: Visma Purchase Order Basic API
  slug: visma-purchaseorderbasic-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The PurchaseReceipt API from Visma — 7 operation(s) for purchasereceipt.
  name: Visma Purchase Receipt API
  slug: visma-purchasereceipt-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The PurchaseReceiptBasic API from Visma — 3 operation(s) for purchasereceiptbasic.
  name: Visma Purchase Receipt Basic API
  slug: visma-purchasereceiptbasic-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The PurchaseReceiptV2 API from Visma — 2 operation(s) for purchasereceiptv2.
  name: Visma Purchase Receipt V2 API
  slug: visma-purchasereceiptv2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'A preliminary version of a quote that can be edited and finalized before becoming an official quote. Overview of Quotes Functionality: [Quotes](https://support.spiris.se/bokforing-fakturering-plus/en-'
  name: Visma Quote Drafts API
  slug: visma-quotedrafts-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'A proposed price for products or services before an order. Overview of Quotes Functionality: [Quotes](https://support.spiris.se/bokforing-fakturering-plus/en-se/content/online-help/sales-quotes.htm) <'
  name: Visma Quotes API
  slug: visma-quotes-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SalesCategory API from Visma — 3 operation(s) for salescategory.
  name: Visma Sales Category API
  slug: visma-salescategory-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Files or documents that can be linked to records such as customer invoices, quotes, and orders. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Solo'
  name: Visma Sales Document Attachments API
  slug: visma-salesdocumentattachments-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SalesOrderBasic API from Visma — 10 operation(s) for salesorderbasic.
  name: Visma Sales Order Basic API
  slug: visma-salesorderbasic-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SalesOrderBasicV2 API from Visma — 8 operation(s) for salesorderbasicv2.
  name: Visma Sales Order Basic V2 API
  slug: visma-salesorderbasicv2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SalesOrderType API from Visma — 2 operation(s) for salesordertype.
  name: Visma Sales Order Type API
  slug: visma-salesordertype-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SalesOrderV2 API from Visma — 12 operation(s) for salesorderv2.
  name: Visma Sales Order V2 API
  slug: visma-salesorderv2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SalesPerson API from Visma — 2 operation(s) for salesperson.
  name: Visma Sales Person API
  slug: visma-salesperson-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SalesPersonV2 API from Visma — 2 operation(s) for salespersonv2.
  name: Visma Sales Person V2 API
  slug: visma-salespersonv2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'A list of sales prices for products or services. Overview of Sales Price List Functionality: [Sales Price List](https://support.spiris.se/bokforing-fakturering-plus/en-se/content/online-help/settings-'
  name: Visma Sales Price Lists API
  slug: visma-salespricelists-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Shipment API from Visma — 11 operation(s) for shipment.
  name: Visma Shipment API
  slug: visma-shipment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing shortcut operations. Allows deleting shortcuts created by third-party integrations.
  name: Visma Shortcuts API
  slug: visma-shortcuts-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing sick leave shortcuts for employees. Sick leave shortcuts allow tracking of employee sick leave periods with configurable registration methods (time, hours, or percentage).
  name: Visma Sick Leave API
  slug: visma-sickleave-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: A Swedish standard file format used to import and export accounting data between different financial systems. This implementation supports verifications and documents. <br><br> ___ Available in any of
  name: Visma Sie File Import Export API
  slug: visma-siefileimportexport-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The StocktakeV2 API from Visma — 2 operation(s) for stocktakev2.
  name: Visma Stocktake V2 API
  slug: visma-stocktakev2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Supplier API from Visma — 12 operation(s) for supplier.
  name: Visma Supplier API
  slug: visma-supplier-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SupplierAccount API from Visma — 1 operation(s) for supplieraccount.
  name: Visma Supplier Account API
  slug: visma-supplieraccount-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SupplierDocument API from Visma — 1 operation(s) for supplierdocument.
  name: Visma Supplier Document API
  slug: visma-supplierdocument-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SupplierInvoice API from Visma — 16 operation(s) for supplierinvoice.
  name: Visma Supplier Invoice API
  slug: visma-supplierinvoice-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Draft invoices from suppliers before they are finalized and posted to the accounting system. Overview of Supplier Invoice Draft Functionality: [Supplier Invoices](https://support.spiris.se/bokforing-f'
  name: Visma Supplier Invoice Drafts API
  slug: visma-supplierinvoicedrafts-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SupplierLocation API from Visma — 3 operation(s) for supplierlocation.
  name: Visma Supplier Location API
  slug: visma-supplierlocation-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SupplierPayment API from Visma — 5 operation(s) for supplierpayment.
  name: Visma Supplier Payment API
  slug: visma-supplierpayment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Organizations or individuals that provide goods or services to your business. Overview of Supplier Functionality: [Suppliers](https://support.spiris.se/bokforing-fakturering-plus/en-se/content/online-'
  name: Visma Suppliers API
  slug: visma-suppliers-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The SupplierV2 API from Visma — 1 operation(s) for supplierv2.
  name: Visma Supplier V2 API
  slug: visma-supplierv2-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Agreed conditions for when and how a customer or supplier will pay. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Solo * Bookkeeping'
  name: Visma Terms Of Payment API
  slug: visma-termsofpayment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing timebank shortcuts for employees. Timebank shortcuts allow tracking of employee accumulated hours expenditure.
  name: Visma Timebank API
  slug: visma-timebank-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing time rule annual dates for company. Time rule annual dates are used to define specific dates that are relevant for time rules, such as holidays or special events.
  name: Visma Time Rule Annual Dates API
  slug: visma-timeruleannualdates-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing travel and expense shortcuts for employees. Travel and expense shortcuts allow tracking of employee travel and other expenses based on supplied pay code numbers.
  name: Visma Travel And Expense API
  slug: visma-travelandexpense-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The UiExtension API from Visma — 5 operation(s) for uiextension.
  name: Visma UI Extension API
  slug: visma-uiextension-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Measurement units for articles and invoicing. <br><br> ___ Available in any of the following variants: * Pro * Standard * Invoicing * Solo'
  name: Visma Units API
  slug: visma-units-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Users of Bookkeeping & Invoicing/eAccounting. <br><br> ___ Available in any of the following variants: * Pro * Invoicing * Standard * Bookkeeping * Solo * Payroll'
  name: Visma Users API
  slug: visma-users-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Vat API from Visma — 4 operation(s) for vat.
  name: Visma Vat API
  slug: visma-vat-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The VatCategory API from Visma — 2 operation(s) for vatcategory.
  name: Visma Vat Category API
  slug: visma-vatcategory-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'VAT codes define the tax rates and types applicable to different transactions. Overview of VAT Codes Functionality: [Vat Codes](https://support.spiris.se/bokforing-fakturering-plus/en-se/content/onlin'
  name: Visma Vat Code API
  slug: visma-vatcode-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'VAT reports for your company, including periodic VAT returns, approval status, and reporting details. Overview of VAT Report Functionality: [VAT Reports](https://support.spiris.se/bokforing-fakturerin'
  name: Visma Vat Report API
  slug: visma-vatreport-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The VatZone API from Visma — 2 operation(s) for vatzone.
  name: Visma Vat Zone API
  slug: visma-vatzone-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'A preliminary version of a voucher that can be edited and reviewed before being finalized. <br><br> ___ Available in any of the following variants: * Pro * Standard * Solo * Bookkeeping'
  name: Visma Voucher Drafts API
  slug: visma-voucherdrafts-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Transactions within your business organized by voucher entries with debit and credit rows. Overview of Voucher Functionality: [Vouchers](https://support.spiris.se/bokforing-fakturering-plus/en-se/cont'
  name: Visma Vouchers API
  slug: visma-vouchers-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Transactions within your business organized by voucher entries with debit and credit rows, for handling customer or supplier payment differences. This endpoint is not available for Swedish companies. '
  name: Visma Voucher With Overunder Payment API
  slug: visma-voucherwithoverunderpayment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for fetching wage runs created for Your company's employees.
  name: Visma Wageruns API
  slug: visma-wageruns-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Warehouse API from Visma — 4 operation(s) for warehouse.
  name: Visma Warehouse API
  slug: visma-warehouse-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The Warmup API from Visma — 1 operation(s) for warmup.
  name: Visma Warmup API
  slug: visma-warmup-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: The WebhookNotificationFeedback API from Visma — 1 operation(s) for webhooknotificationfeedback.
  name: Visma Webhook Notification Feedback API
  slug: visma-webhooknotificationfeedback-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: 'Customer orders placed through Spiris webshop. Overview of Webshop Order Functionality: [Webshop](https://support.spiris.se/webshop/sv-se/content/online-help/minitoc-startpage-online-help.htm) <br><br'
  name: Visma Webshop Orders API
  slug: visma-webshoporders-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing work day overrides for employees. Work day override allows to specify different working times/duration for specific days.
  name: Visma Work Day Override API
  slug: visma-workdayoverride-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing work day overrides for employees. Work day override allows to specify different working times/duration for specific days.
  name: Visma Work Day Overrides API
  slug: visma-workdayoverrides-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing work schedule time adjustments for a company. Work schedule time adjustments are used to define exceptions for specific dates which are repeating every year.
  name: Visma Work Schedule Time Adjustment API
  slug: visma-workscheduletimeadjustment-api
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: Operations for managing work schedule time adjustments for a company. Work schedule time adjustments are used to define exceptions for specific dates which are repeating every year.
  name: Visma Work Schedule Time Adjustments API
  slug: visma-workscheduletimeadjustments-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'The current financial balance of an account, showing the difference between its debits and credits. ___ Available in any of the following variants: * Pro * Standard * Bookkeeping * Solo'
  name: Visma Account Balance API
  slug: visma-account-balance-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Account types that can be used for categorizing accounts. This is applicable on all countries but most relevant for the Netherlands. ___ Available in any of the following variants: * Pro * Standard * '
  name: Visma Account Types API
  slug: visma-account-types-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Bank accounts associated with your company for handling financial transactions. Overview of Bank Account Functionality: Bank Accounts ___ Available in any of the following variants: * Pro * Standard *'
  name: Visma Bank Accounts API
  slug: visma-bank-accounts-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Bank transactions represent individual financial movements in and out of your company''s bank accounts. Overview of Bank Transaction Functionality: Bank Transactions ___ Available in any of the followi'
  name: Visma Bank Transactions API
  slug: visma-bank-transactions-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Configuration options of your company. Overview of Company Settings Functionality: Company settings ___'
  name: Visma Company Settings API
  slug: visma-company-settings-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Cost centers provide a way to organize and track expenses across different departments, projects, or business units within the company. Overview of Cost Center Functionality: Cost Centers ___ Availabl'
  name: Visma Cost Centers API
  slug: visma-cost-centers-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Credit Note API from Visma — 5 operation(s) for credit note.
  name: Visma Credit Note API
  slug: visma-credit-note-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Customer Contract API from Visma — 11 operation(s) for customer contract.
  name: Visma Customer Contract API
  slug: visma-customer-contract-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Invoices sent to customers for goods or services provided by your business. Overview of Customer Invoice Functionality: Customer Invoices ___ Available in any of the following variants: * Pro * Standa'
  name: Visma Customer Invoices API
  slug: visma-customer-invoices-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Conditions that define risks and responsibilities during delivery. ___ Available in any of the following variants: * Pro * Standard * Invoicing * Solo'
  name: Visma Delivery Terms API
  slug: visma-delivery-terms-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Discount Code API from Visma — 1 operation(s) for discount code.
  name: Visma Discount Code API
  slug: visma-discount-code-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The accounting periods that represent a complete financial year for your company. Fiscal years define the start and end dates used for financial reporting, accounting periods, and tax calculations. __
  name: Visma Fiscal Years API
  slug: visma-fiscal-years-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Fixed assets used to track long-term company resources such as equipment, vehicles, or machines. *(Note: Despite the endpoint name, this resource represents fixed assets rather than inventory items.)*'
  name: Visma Inventory Items API
  slug: visma-inventory-items-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Inventory Receipt API from Visma — 3 operation(s) for inventory receipt.
  name: Visma Inventory Receipt API
  slug: visma-inventory-receipt-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: Message threads allow users to communicate about specific documents or general topics within the system. Each thread can contain multiple messages and can be attached to various document types. Overvi
  name: Visma Message Threads API
  slug: visma-message-threads-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Multi language API from Visma — 4 operation(s) for multi language.
  name: Visma Multi language API
  slug: visma-multi-language-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Payment Method API from Visma — 2 operation(s) for payment method.
  name: Visma Payment Method API
  slug: visma-payment-method-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: Managing company payroll settings, including configuration of payroll periods, tax settings, and other payroll-related preferences.
  name: Visma Payroll Settings API
  slug: visma-payroll-settings-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Purchase Order API from Visma — 3 operation(s) for purchase order.
  name: Visma Purchase Order API
  slug: visma-purchase-order-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Sales Order API from Visma — 15 operation(s) for sales order.
  name: Visma Sales Order API
  slug: visma-sales-order-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Sub Account API from Visma — 2 operation(s) for sub account.
  name: Visma Sub Account API
  slug: visma-sub-account-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Invoices received from suppliers for goods or services provided to your business. Overview of Supplier Invoice Functionality: Supplier Invoices ___ Available in any of the following variants: * Pro * '
  name: Visma Supplier Invoices API
  slug: visma-supplier-invoices-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Time Card API from Visma — 5 operation(s) for time card.
  name: Visma Time Card API
  slug: visma-time-card-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: The Unit of Measure API from Visma — 1 operation(s) for unit of measure.
  name: Visma Unit of Measure API
  slug: visma-unit-of-measure-api
- baseURL: https://business.visma.net/api/graphql
  baseurl_source: declared
  description: 'Operations for managing work schedules for company. Work schedule allows to define working hours for employees, which can work in various schedule types: regular, irregular, full-time, part-time, etc.'
  name: Visma Work Schedules API
  slug: visma-work-schedules-api
artifact_total: 202
asyncapis:
- description: ''
  name: Visma Net Erp Webhooks
  slug: visma-net-erp-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/overlays/visma-net-erp-service-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/visma-net-erp-service-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/overlays/visma-eaccounting-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/visma-eaccounting-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/overlays/visma-payroll-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/visma-payroll-api-v2-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.visma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.visma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vismasoftware.no/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vismasoftware.no/vismanetapi/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vismasoftware.no/vismanetapi/introduction/getting-started-with-visma-net-api/
- group: start
  title: ''
  type: SignUp
  url: https://oauth.developers.visma.com/service-registry/
- group: operate
  title: ''
  type: Support
  url: https://docs.vismasoftware.no/vismanetapi/support/
- group: company
  title: ''
  type: Blog
  url: https://www.visma.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.visma.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.visma.com/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.visma.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.vismasoftware.no/vismanetapi/end-of-life-notices/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/visma-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-trust-center.yml
  title: ''
  type: Compliance
  url: security/visma-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/llms/visma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/visma-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/mcp/visma-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/visma-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/well-known/visma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/visma-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/well-known/visma-connect-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/visma-connect-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/packages/visma-packages.yml
  title: ''
  type: Packages
  url: packages/visma-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/components/visma-components.yml
  title: ''
  type: Components
  url: components/visma-components.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/authentication/visma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/visma-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/scopes/visma-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/visma-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/conventions/visma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/visma-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/conformance/visma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/visma-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/errors/visma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/visma-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/lifecycle/visma-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/visma-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/changelog/visma-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/visma-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/rate-limits/visma-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/visma-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/plans/visma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/visma-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/sandbox/visma-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/visma-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/data-model/visma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/visma-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/asyncapi/visma-net-erp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/visma-net-erp-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/visma-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/visma-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/visma-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/mcp/visma-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/visma-tool-crosswalk.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Visma-Software-AS-Product
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/visma-create-customer-and-sales-order.md
  title: ''
  type: AgentSkill
  url: skills/visma-create-customer-and-sales-order.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/visma-invoice-and-reverse.md
  title: ''
  type: AgentSkill
  url: skills/visma-invoice-and-reverse.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/visma-supplier-invoice-approval.md
  title: ''
  type: AgentSkill
  url: skills/visma-supplier-invoice-approval.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/visma-business-nxt-mcp-session.md
  title: ''
  type: AgentSkill
  url: skills/visma-business-nxt-mcp-session.md
created: '2026-09-13'
description: 'Visma is a Nordic business-software group headquartered in Oslo, Norway, supplying cloud ERP, accounting, invoicing, payroll, HR and public-sector software to more than a million customers across Europe and Latin America. Its developer surface is federated across product lines rather than centralised: Visma.net ERP publishes a 511-operation OpenAPI 3.0 contract at api.finance.visma.net in service (client-credentials) and interactive (authorization-code) flavours; Bookkeeping & Invoicing/eAccounting and Cloud Payroll (Spiris, formerly Visma Spcs) publish OpenAPI 3.0 contracts at eaccountingapi.vismaonline.com and vlsapi.vismaonline.com; and Business NXT exposes a GraphQL API at business.visma.net. Identity is centralised on Visma Connect (connect.visma.com), an OpenID Connect provider advertising 129 scopes, with a second IdentityServer at identity.vismaonline.com for the Spiris product line. Visma ships two first-party remote MCP servers — Business NXT at mcp.business.visma.net
  and Spiris at mcp.spiris.se — both OAuth-protected and discoverable via RFC 9728.'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Visma MCP Server
  slug: visma-mcp-server
modified: '2026-09-13'
name: Visma
nav: Providers
network: true
overview: 'Visma publishes 192 APIs on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Agreements API, and 189 more. Tagged areas include Accounting, Business Software, ERP, Enterprise, and Financial-Services.


  The Visma catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Visma''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 38 more developer resources.'
plans:
- name: Visma Plans Pricing
  plan_count: 1
  slug: visma-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Visma Rate Limits
  slug: visma-rate-limits
scopes:
- name: Visma Scopes
  scope_count: 5
  slug: visma-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 56.5
    discoverability: 75.9
    operational_transparency: 94.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 61.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 192
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Visma Authentication
  slug: visma-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Visma Domain Security
  slug: visma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Visma Vulnerability Disclosure
  slug: visma-vulnerability-disclosure
  summary_line: Intigriti · contact published
- kind: trust-center
  name: Visma Trust Center
  slug: visma-trust-center
  summary_line: trust center published
slug: visma
tags:
- Accounting
- Business Software
- ERP
- Enterprise
- Financial-Services
- Human Resources
- Invoicing
- Nordic
- Payroll
- Software-as-a-Service
website: https://www.visma.com/
---
