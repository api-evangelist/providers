---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 62.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 143
  human_in_the_loop: 0
  name: Apideck Agentic Access
  operation_count: 251
  slug: apideck-agentic-access
  summary_line: 251 operations · 143 acting
api_count: 54
apis:
- description: Apideck is the leading Unified API that doesn't store sensitive customer data. Build and maintain native integrations into your product with an exceptional Developer Experience.
  name: Apideck
  slug: apideck
- description: The Activity resource represents a logged event or task, such as a meeting, call, or email, including details like type, date, duration, and associations with contacts, companies, or opportunities.
  name: Apideck Activities API
  slug: apideck-activities-api
- description: Aged Creditors is a report showing amounts owed to suppliers, grouped by aging periods (current, 30, 60, 90+ days) with supplier details.
  name: Apideck Aged Creditors API
  slug: apideck-aged-creditors-api
- description: Aged Debtors is a report showing amounts owed by customers, grouped by aging periods (current, 30, 60, 90+ days) with customer details.
  name: Apideck Aged Debtors API
  slug: apideck-aged-debtors-api
- description: An Attachment represents a file linked to an accounting document, including file name, URL, content type, and the parent record reference.
  name: Apideck Attachments API
  slug: apideck-attachments-api
- description: A Balance Sheet report shows the financial position at a point in time, including totals for assets, liabilities, and equity accounts.
  name: Apideck Balance Sheet API
  slug: apideck-balance-sheet-api
- description: A Bank Account represents a financial account, including account name, number, type (checking, savings, credit card), currency, and balance.
  name: Apideck Bank Accounts API
  slug: apideck-bank-accounts-api
- description: A Bank Feed Account represents a connected financial institution account, including account details and connection status for transaction imports.
  name: Apideck Bank Feed Accounts API
  slug: apideck-bank-feed-accounts-api
- description: A Bank Feed Statement contains imported transaction data from a connected bank account, including statement period and transaction details.
  name: Apideck Bank Feed Statements API
  slug: apideck-bank-feed-statements-api
- description: A Bill Payment represents money paid to a supplier, including amount, date, payment method, and allocation to one or more bills.
  name: Apideck Bill Payments API
  slug: apideck-bill-payments-api
- description: A Bill represents an invoice from a supplier, including line items, amounts, due date, payment status, and linked supplier.
  name: Apideck Bills API
  slug: apideck-bills-api
- description: A Category represents a product or service grouping, including name and type for organizing invoice and bill line items.
  name: Apideck Categories API
  slug: apideck-categories-api
- description: List companies accessible through the current connection. Only available for multi-company connectors.
  name: Apideck Companies API
  slug: apideck-companies-api
- description: Company Info contains the organization's profile data including legal name, addresses, tax identifiers, currency, and fiscal year settings.
  name: Apideck Company Info API
  slug: apideck-company-info-api
- description: The Contact resource represents individuals, including details such as name, contact information, associated company, and activity history.
  name: Apideck Contacts API
  slug: apideck-contacts-api
- description: A Credit Note represents a reduction in the amount owed by a customer, including line items, amounts, and the linked customer or invoice.
  name: Apideck Credit Notes API
  slug: apideck-credit-notes-api
- description: The Custom Object Schema resource represents the schema of a custom object.
  name: Apideck Custom Object Schemas API
  slug: apideck-custom-object-schemas-api
- description: The Custom Object resource represents user-defined data structures in Salesforce, allowing storage of custom records with specific fields, relationships, and business logic tailored to unique organiza
  name: Apideck Custom Objects API
  slug: apideck-custom-objects-api
- description: A Customer represents a buyer or client, including contact details, billing and shipping addresses, tax information, and payment terms.
  name: Apideck Customers API
  slug: apideck-customers-api
- description: A Department represents an organizational unit, including name, code, and parent department for hierarchical structures.
  name: Apideck Departments API
  slug: apideck-departments-api
- description: Drive Groups resource represents the groups of drives in the cloud storage service. It provides methods for managing and accessing the drive groups, such as creating, deleting, and listing drive group
  name: Apideck Drive Groups API
  slug: apideck-drive-groups-api
- description: Drives resource represents logical containers for storing folders and files in the cloud storage service. It provides methods for managing and accessing the drives, such as creating, deleting, and lis
  name: Apideck Drives API
  slug: apideck-drives-api
- description: An Employee Payroll represents an individual's pay details for a period, including gross pay, deductions, taxes, and net pay.
  name: Apideck Employee Payrolls API
  slug: apideck-employee-payrolls-api
- description: An Employee Schedule represents work time assignments, including schedule entries with start time, end time, and work location.
  name: Apideck Employee Schedules API
  slug: apideck-employee-schedules-api
- description: An Employee represents an individual within the organization for accounting purposes, including name, department, hire date, and employment status.
  name: Apideck Employees API
  slug: apideck-employees-api
- description: An Expense Category classifies types of expenses within the organization, such as travel, meals, or office supplies. Used to categorize expense report line items.
  name: Apideck Expense Categories API
  slug: apideck-expense-categories-api
- description: An Expense Report is a collection of expense line items submitted by an employee for reimbursement, including amounts, categories, and approval status.
  name: Apideck Expense Reports API
  slug: apideck-expense-reports-api
- description: An Expense represents a business expenditure, including amount, date, category, payment method, merchant, and account allocation.
  name: Apideck Expenses API
  slug: apideck-expenses-api
- description: Files resource represents files stored in the cloud storage services. It provides methods for managing and accessing the files, such as uploading, downloading, and deleting files. For more information
  name: Apideck Files API
  slug: apideck-files-api
- description: Folders resource represents the folders within a drive in the cloud storage service. It provides methods for managing and accessing the folders, such as creating, deleting, and listing files & folders
  name: Apideck Folders API
  slug: apideck-folders-api
- description: An Invoice Item represents a reusable product or service that can be added to invoices, including name, description, price, and tax settings.
  name: Apideck Invoice Items API
  slug: apideck-invoice-items-api
- description: An Invoice represents a sales document sent to customers, including line items, taxes, discounts, totals, due date, and payment status.
  name: Apideck Invoices API
  slug: apideck-invoices-api
- description: A Journal Entry represents a manual accounting entry with debit and credit line items, memo, posting date, and status.
  name: Apideck Journal Entries API
  slug: apideck-journal-entries-api
- description: The Lead resource represents individuals or businesses that have shown interest in a company's products or services, including contact information and potential deal opportunities.
  name: Apideck Leads API
  slug: apideck-leads-api
- description: A Ledger Account represents an entry in the chart of accounts, including name, code, type (asset, liability, equity, revenue, expense), and balance.
  name: Apideck Ledger Accounts API
  slug: apideck-ledger-accounts-api
- description: A Location represents a physical business site, including name, address, and status for multi-location tracking.
  name: Apideck Locations API
  slug: apideck-locations-api
- description: The Note resource represents textual records, such as comments or messages, associated with various entities like contacts, opportunities, or activities.
  name: Apideck Notes API
  slug: apideck-notes-api
- description: The Opportunity resource represents potential business deals, including details such as title, value, status, close date, and associated contacts or companies.
  name: Apideck Opportunities API
  slug: apideck-opportunities-api
- description: A Payment represents money received from a customer, including amount, date, payment method, and allocation to one or more invoices.
  name: Apideck Payments API
  slug: apideck-payments-api
- description: A Payroll represents a pay run, including pay period dates, total amounts, status, and linked company.
  name: Apideck Payrolls API
  slug: apideck-payrolls-api
- description: The Pipeline resource represents a structured process for managing sales opportunities, including stages and associated activities.
  name: Apideck Pipelines API
  slug: apideck-pipelines-api
- description: A Profit and Loss report shows financial performance over a period, including revenue, cost of sales, expenses, and net income.
  name: Apideck Profit and Loss API
  slug: apideck-profit-and-loss-api
- description: A Project represents a job or engagement, including name, customer, budget amounts, budget hours, billing method, status, and profitability data.
  name: Apideck Projects API
  slug: apideck-projects-api
- description: A Purchase Order represents a request to buy goods or services from a supplier, including line items, amounts, delivery date, and status.
  name: Apideck Purchase Orders API
  slug: apideck-purchase-orders-api
- description: A Quote represents a sales estimate sent to customers, including line items, amounts, expiry date, and status before conversion to invoice.
  name: Apideck Quotes API
  slug: apideck-quotes-api
- description: A Refund represents money returned to a customer, supporting both itemized refunds (with line items) and allocation-based refunds (applied to invoices, credit notes, or overpayments).
  name: Apideck Refunds API
  slug: apideck-refunds-api
- description: Shared links resource represents the links to files and folders in the cloud storage service that have been shared with other users. It provides methods for managing and accessing the shared links, su
  name: Apideck Shared Links API
  slug: apideck-shared-links-api
- description: A Subsidiary represents a child company within an organization, including name, status, and parent company relationship.
  name: Apideck Subsidiaries API
  slug: apideck-subsidiaries-api
- description: A Supplier represents a vendor or service provider, including contact information, addresses, tax details, and payment terms.
  name: Apideck Suppliers API
  slug: apideck-suppliers-api
- description: A Tax Rate defines a tax percentage applied to transactions, including name, rate, tax type, and applicable regions or conditions.
  name: Apideck Tax Rates API
  slug: apideck-tax-rates-api
- description: A Time Off Request represents an absence request, including type (vacation, sick), dates, status, and approval information.
  name: Apideck Time Off Requests API
  slug: apideck-time-off-requests-api
- description: A Tracking Category represents a classification dimension for reporting, including name, code, status, and parent category for hierarchies.
  name: Apideck Tracking Categories API
  slug: apideck-tracking-categories-api
- description: Upload sessions resource represents the sessions used for uploading files to the cloud storage service. It provides methods for managing and accessing the upload sessions, such as creating and resumin
  name: Apideck Upload Sessions API
  slug: apideck-upload-sessions-api
- description: A User represents a CRM team member, including name, email, role, status, and associated permissions within the system.
  name: Apideck Users API
  slug: apideck-users-api
artifact_total: 850
collections:
- collection_type: open
  name: Apideck Accounting API
  slug: open-apideck-accounting
- collection_type: open
  name: Apideck CRM API
  slug: open-apideck-crm
- collection_type: open
  name: Apideck File storage API
  slug: open-apideck-file-storage
- collection_type: open
  name: Apideck HRIS API
  slug: open-apideck-hris
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apideck-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apideck-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apideck-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apideck
- group: company
  title: ''
  type: Website
  url: https://www.apideck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.apideck.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.apideck.com/get-started
- group: build
  title: ''
  type: SDKs
  url: https://developers.apideck.com/sdks/node
- group: build
  title: ''
  type: SDKs
  url: https://developers.apideck.com/sdks/python
- group: build
  title: ''
  type: SDKs
  url: https://developers.apideck.com/sdks/go
- group: build
  title: ''
  type: SDKs
  url: https://developers.apideck.com/sdks/java
- group: build
  title: ''
  type: SDKs
  url: https://developers.apideck.com/sdks/php
- group: build
  title: ''
  type: SDKs
  url: https://developers.apideck.com/sdks/dot-net
- group: docs
  title: ''
  type: Guide
  url: https://developers.apideck.com/guides
- group: other
  title: ''
  type: Explorer
  url: https://developers.apideck.com/api-explorer
- group: start
  title: ''
  type: Login
  url: https://platform.apideck.com/login
- group: start
  title: ''
  type: Signup
  url: https://platform.apideck.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.apideck.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.apideck.com/changelog
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.apideck.com/errors
- group: build
  title: ''
  type: Examples
  url: https://developers.apideck.com/samples
- group: auth
  title: ''
  type: Security
  url: https://compliance.apideck.com/?_gl=1*1od5jy9*_gcl_au*MTUxOTE3MDcxMC4xNzUyNjE1MTc3
- group: auth
  title: ''
  type: Compliance
  url: https://compliance.apideck.com/?_gl=1*1od5jy9*_gcl_au*MTUxOTE3MDcxMC4xNzUyNjE1MTc3
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://compliance.apideck.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://compliance.apideck.com/terms
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://compliance.apideck.com/sla
- group: auth
  title: ''
  type: GDPR
  url: https://compliance.apideck.com/gdpr
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apideck.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apideck.com/
- group: company
  title: ''
  type: Blog
  url: https://www.apideck.com/blog
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/apideck-libraries/openapi-specs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apideck-libraries
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apideck-io
- group: auth
  title: ''
  type: Authentication
  url: https://www.apideck.com/products/vault
- group: other
  title: ''
  type: Products
  url: https://www.apideck.com/unified-apis
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.apideck.com/llms.txt
created: '2025-07-15'
description: Apideck is the leading Unified API that doesn't store sensitive customer data. Build and maintain native integrations into your product with an exceptional Developer Experience.
features:
- name: Unified APIs
- name: Data Sync
- name: Native Webhooks
- name: Virtualized Webhooks
- name: Authenticaiton
- name: Authorization
- name: Vault
- name: Secure environment
- name: Multi-factor authentication
- name: Restricted network access
- name: Data encryption
- name: Secure development practices
- name: Realtime monitoring
- name: SDKs
- name: Login With GitHub
- name: Login With Google
- name: API Testing
- name: Scalable Pricing
- name: Debugging
- name: Proxies
finops:
- name: Apideck Finops
  service_category: Integrations / Unified API
  slug: apideck-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apideck.png
integrations:
- name: Acerta
- name: Act
- name: ActiveCampaign
- name: Acumatica
- name: ADP iHCM
- name: ADP Workforce Now
- name: AFAS Software
- name: Albacross
- name: AlexisHR
- name: Amazon Seller Central
- name: Asana
- name: Attio
- name: auth-only
- name: Azure DevOps
- name: BambooHR
- name: banqUP
- name: Basecamp
- name: BigCommerce
- name: bol.com
- name: Box
- name: Breathe HR
- name: Bullhorn ATS
- name: Calendly
- name: CatalystOne
- name: Cegid Talentsoft
- name: Ceridian Dayforce
- name: Cezanne HR
- name: CharlieHR
- name: chatchat
- name: CIPHR
- name: Clear Books
- name: ClickUp
- name: Close.io
- name: Clover
- name: Copper
- name: Crisp
- name: Deel
- name: DigitalOcean
- name: Drift
- name: Dropbox
- name: early-access
- name: Employment Hero
- name: Etsy
- name: Exact Online
- name: Exact Online NL
- name: Exact Online UK
- name: Factorial
- name: Flexmail
- name: Folks HR
- name: Fourth
- name: FreeAgent
- name: FreshBooks
- name: Freshteam
- name: Freshworks CRM
- name: GeoDynamics
- name: GitHub
- name: GitLab
- name: GitLab server (on-prem)
- name: Gmail
- name: Google Analytics
- name: Google BigQuery
- name: Google Calendar
- name: Google Contacts
- name: Google Drive
- name: Google Sheets
- name: Google Tag Manager
- name: Google Workspace
- name: Greenhouse
- name: Group S
- name: Heap
- name: Hibob
- name: Holded
- name: Homerun HR
- name: HR Works
- name: HubSpot
- name: Humaans
- name: Intercom
- name: IRIS Cascade HR
- name: Iubenda
- name: JetBrains YouTrack
- name: Jira
- name: Jira Data Center
- name: Jira Service Desk
- name: journy.io
- name: JumpCloud
- name: Justworks
- name: Kashflow
- name: Keka HR
- name: Kenjo
- name: Kustomer
- name: Lever
- name: Lightspeed
- name: Lightspeed eCom (C-Series)
- name: Linear
- name: Loket.nl
- name: Lucca
- name: Magento
- name: MailChimp
- name: Mailgun
- name: MessageBird
- name: Metomic
- name: Microsoft Dynamics 365 Business Central
- name: Microsoft Dynamics 365 Human Resources
- name: Microsoft Dynamics CRM
- name: Microsoft Entra
- name: Microsoft Outlook
- name: Microsoft Teams
- name: Mollie
- name: monday.com
- name: MRI Software
- name: MYOB
- name: MYOB Acumatica
- name: Namely
- name: NetSuite
- name: Notion
- name: Odoo
- name: Officient
- name: Okta
- name: OneDrive
- name: OneLogin
- name: OneTrust
- name: Outlook Calendar
- name: Paychex
- name: PayFit
- name: Paylocity
- name: People HR
- name: Personio
- name: Picqer
- name: Pipedrive
- name: Planhat
- name: Plivo
- name: Portt
- name: Prestashop
- name: Procountor
- name: QuickBooks
- name: Recruitee
- name: RUN Powered by ADP
- name: Sage Business Cloud Accounting
- name: Sage HR
- name: Sage Intacct
- name: Salesflare
- name: Salesforce
- name: SAP SuccessFactors
- name: Sapling
- name: SD Worx
- name: SD Worx (Web service)
- name: Securex
- name: Segment
- name: Sendgrid
- name: ServiceNow
- name: Sesame HR
- name: SharePoint
- name: Shopify
- name: Shopware
- name: Shortcut
- name: Slack
- name: Square
- name: Sympa
- name: Teamleader
- name: Teamtailor
- name: Telnyx
- name: TikTok Shop
- name: Toast
- name: TriNet
- name: Twilio
- name: Typeform
- name: UKG Pro
- name: Visma Netvisor
- name: Visma Nmbrs
- name: Vonage
- name: Walmart
- name: Webexpenses
- name: Wix
- name: WooCommerce
- name: Workable
- name: Workday
- name: Xero
- name: Zendesk
- name: Zendesk Sell
- name: Zenefits
- name: Zoho Books
- name: Zoho CRM
- name: Zoho People
json_schemas:
- name: Account Code
  property_count: 0
  slug: apideck-accountcode
- name: Account Id
  property_count: 0
  slug: apideck-accountid
- name: AccountingBankAccount
  property_count: 27
  slug: apideck-accountingbankaccount
- name: Accounting by Row
  property_count: 0
  slug: apideck-accountingbyrow
- name: CompanyId
  property_count: 0
  slug: apideck-accountingcompanyid
- name: AccountingConnectionCompany
  property_count: 2
  slug: apideck-accountingconnectioncompany
- name: AccountingCustomer
  property_count: 0
  slug: apideck-accountingcustomer
- name: AccountingDepartment
  property_count: 15
  slug: apideck-accountingdepartment
- name: AccountingDepartmentsFilter
  property_count: 1
  slug: apideck-accountingdepartmentsfilter
- name: AccountingEmployee
  property_count: 31
  slug: apideck-accountingemployee
- name: AccountingEmployeesFilter
  property_count: 2
  slug: apideck-accountingemployeesfilter
- name: AccountingEventType
  property_count: 0
  slug: apideck-accountingeventtype
- name: Invoice Id
  property_count: 0
  slug: apideck-accountinginvoiceid
- name: AccountingLocation
  property_count: 16
  slug: apideck-accountinglocation
- name: AccountingLocationsFilter
  property_count: 1
  slug: apideck-accountinglocationsfilter
- name: Accounting period
  property_count: 0
  slug: apideck-accountingperiod
- name: Project ID
  property_count: 0
  slug: apideck-accountingprojectid
- name: Sales Order ID
  property_count: 0
  slug: apideck-accountingsalesorderid
- name: AccountingWebhookEvent
  property_count: 0
  slug: apideck-accountingwebhookevent
- name: Account Name
  property_count: 0
  slug: apideck-accountname
- name: Is active
  property_count: 0
  slug: apideck-active
- name: ActivitiesFilter
  property_count: 5
  slug: apideck-activitiesfilter
- name: ActivitiesSort
  property_count: 2
  slug: apideck-activitiessort
- name: Activity
  property_count: 52
  slug: apideck-activity
- name: ActivityAttendee
  property_count: 14
  slug: apideck-activityattendee
- name: Address
  property_count: 25
  slug: apideck-address
- name: AgedCreditors
  property_count: 5
  slug: apideck-agedcreditors
- name: AgedDebtors
  property_count: 5
  slug: apideck-ageddebtors
- name: AgedReportFilter
  property_count: 5
  slug: apideck-agedreportfilter
- name: Allocation
  property_count: 5
  slug: apideck-allocation
- name: Amount
  property_count: 0
  slug: apideck-amount
- name: Attachment
  property_count: 13
  slug: apideck-attachment
- name: AttachmentReference
  property_count: 2
  slug: apideck-attachmentreference
- name: AttachmentReferenceType
  property_count: 0
  slug: apideck-attachmentreferencetype
- name: BadRequestResponse
  property_count: 7
  slug: apideck-badrequestresponse
- name: Balance by Period
  property_count: 4
  slug: apideck-balancebyperiod
- name: Balance by Transaction
  property_count: 7
  slug: apideck-balancebytransaction
- name: BalanceSheet
  property_count: 1
  slug: apideck-balancesheet
- name: Balance Sheet Account
  property_count: 5
  slug: apideck-balancesheetaccount
- name: Balance Sheet Account Record
  property_count: 4
  slug: apideck-balancesheetaccountrecord
- name: Balance Sheet Accounts
  property_count: 0
  slug: apideck-balancesheetaccounts
- name: BalanceSheetFilter
  property_count: 6
  slug: apideck-balancesheetfilter
- name: BankAccount
  property_count: 12
  slug: apideck-bankaccount
- name: BankAccountFilter
  property_count: 1
  slug: apideck-bankaccountfilter
- name: Account Name
  property_count: 0
  slug: apideck-bankaccountname
- name: Account Number
  property_count: 0
  slug: apideck-bankaccountnumber
- name: BankAccountsFilter
  property_count: 3
  slug: apideck-bankaccountsfilter
- name: BankAccountsSort
  property_count: 2
  slug: apideck-bankaccountssort
- name: Bank Code
  property_count: 0
  slug: apideck-bankcode
- name: BankFeedAccount
  property_count: 15
  slug: apideck-bankfeedaccount
- name: BankFeedStatement
  property_count: 14
  slug: apideck-bankfeedstatement
- name: Bank Name
  property_count: 0
  slug: apideck-bankname
- name: Benefit
  property_count: 3
  slug: apideck-benefit
- name: BIC/SWIFT Code
  property_count: 0
  slug: apideck-bic
- name: Bill
  property_count: 51
  slug: apideck-bill
- name: Bill Line Item
  property_count: 38
  slug: apideck-billlineitem
- name: BillPayment
  property_count: 29
  slug: apideck-billpayment
- name: BillsFilter
  property_count: 2
  slug: apideck-billsfilter
- name: BillsSort
  property_count: 2
  slug: apideck-billssort
- name: Birth Date
  property_count: 0
  slug: apideck-birthday
- name: Branch Identifier
  property_count: 0
  slug: apideck-branchidentifier
- name: BSB Number
  property_count: 0
  slug: apideck-bsbnumber
- name: CategoriesFilter
  property_count: 1
  slug: apideck-categoriesfilter
- name: Category
  property_count: 12
  slug: apideck-category
- name: Channel
  property_count: 0
  slug: apideck-channel
- name: CompaniesFilter
  property_count: 3
  slug: apideck-companiesfilter
- name: CompaniesSort
  property_count: 2
  slug: apideck-companiessort
- name: Company
  property_count: 42
  slug: apideck-company
- name: Company ID
  property_count: 0
  slug: apideck-companyid
- name: CompanyInfo
  property_count: 24
  slug: apideck-companyinfo
- name: Company name
  property_count: 0
  slug: apideck-companyname
- name: Compensation
  property_count: 6
  slug: apideck-compensation
- name: Contact
  property_count: 41
  slug: apideck-contact
- name: ContactsFilter
  property_count: 9
  slug: apideck-contactsfilter
- name: ContactsSort
  property_count: 2
  slug: apideck-contactssort
- name: CopyFolderRequest
  property_count: 4
  slug: apideck-copyfolderrequest
- name: Country Code
  property_count: 0
  slug: apideck-country
- name: CreateAccountingDepartmentResponse
  property_count: 7
  slug: apideck-createaccountingdepartmentresponse
- name: CreateAccountingEmployeeResponse
  property_count: 7
  slug: apideck-createaccountingemployeeresponse
- name: CreateAccountingLocationResponse
  property_count: 7
  slug: apideck-createaccountinglocationresponse
- name: CreateActivityResponse
  property_count: 7
  slug: apideck-createactivityresponse
- name: CreateAttachmentRequest
  property_count: 4
  slug: apideck-createattachmentrequest
- name: CreateAttachmentResponse
  property_count: 7
  slug: apideck-createattachmentresponse
- name: CreateBankAccountResponse
  property_count: 6
  slug: apideck-createbankaccountresponse
- name: CreateBankFeedAccountResponse
  property_count: 7
  slug: apideck-createbankfeedaccountresponse
- name: CreateBankFeedStatementResponse
  property_count: 7
  slug: apideck-createbankfeedstatementresponse
- name: CreateBillPaymentResponse
  property_count: 7
  slug: apideck-createbillpaymentresponse
- name: CreateBillResponse
  property_count: 7
  slug: apideck-createbillresponse
- name: CreateCompanyResponse
  property_count: 7
  slug: apideck-createcompanyresponse
- name: CreateContactResponse
  property_count: 7
  slug: apideck-createcontactresponse
- name: CreateCreditNoteResponse
  property_count: 7
  slug: apideck-createcreditnoteresponse
- name: CreateCustomerResponse
  property_count: 7
  slug: apideck-createcustomerresponse
- name: CreateCustomObjectResponse
  property_count: 7
  slug: apideck-createcustomobjectresponse
- name: CreateCustomObjectSchemaResponse
  property_count: 7
  slug: apideck-createcustomobjectschemaresponse
- name: Created at (timestamp)
  property_count: 0
  slug: apideck-createdat
- name: Created by
  property_count: 0
  slug: apideck-createdby
- name: CreateDepartmentResponse
  property_count: 7
  slug: apideck-createdepartmentresponse
- name: CreateDriveGroupResponse
  property_count: 7
  slug: apideck-createdrivegroupresponse
- name: CreateDriveResponse
  property_count: 7
  slug: apideck-createdriveresponse
- name: CreateEmployeeResponse
  property_count: 7
  slug: apideck-createemployeeresponse
- name: CreateExpenseCategoryResponse
  property_count: 7
  slug: apideck-createexpensecategoryresponse
- name: CreateExpenseReportResponse
  property_count: 7
  slug: apideck-createexpensereportresponse
- name: CreateExpenseResponse
  property_count: 7
  slug: apideck-createexpenseresponse
- name: CreateFileRequest
  property_count: 5
  slug: apideck-createfilerequest
- name: CreateFileResponse
  property_count: 7
  slug: apideck-createfileresponse
- name: CreateFolderRequest
  property_count: 6
  slug: apideck-createfolderrequest
- name: CreateFolderResponse
  property_count: 7
  slug: apideck-createfolderresponse
- name: CreateHrisCompanyResponse
  property_count: 7
  slug: apideck-createhriscompanyresponse
- name: CreateInvoiceItemResponse
  property_count: 7
  slug: apideck-createinvoiceitemresponse
- name: CreateInvoiceResponse
  property_count: 7
  slug: apideck-createinvoiceresponse
- name: CreateJournalEntryResponse
  property_count: 7
  slug: apideck-createjournalentryresponse
- name: CreateLeadResponse
  property_count: 7
  slug: apideck-createleadresponse
- name: CreateLedgerAccountResponse
  property_count: 7
  slug: apideck-createledgeraccountresponse
- name: CreateNoteResponse
  property_count: 7
  slug: apideck-createnoteresponse
- name: CreateOpportunityResponse
  property_count: 7
  slug: apideck-createopportunityresponse
- name: CreatePaymentResponse
  property_count: 7
  slug: apideck-createpaymentresponse
- name: CreatePipelineResponse
  property_count: 7
  slug: apideck-createpipelineresponse
- name: CreateProjectResponse
  property_count: 6
  slug: apideck-createprojectresponse
- name: CreatePurchaseOrderResponse
  property_count: 7
  slug: apideck-createpurchaseorderresponse
- name: CreateQuoteResponse
  property_count: 6
  slug: apideck-createquoteresponse
- name: CreateRefundResponse
  property_count: 7
  slug: apideck-createrefundresponse
- name: CreateSharedLinkResponse
  property_count: 7
  slug: apideck-createsharedlinkresponse
- name: CreateSubsidiaryResponse
  property_count: 7
  slug: apideck-createsubsidiaryresponse
- name: CreateSupplierResponse
  property_count: 7
  slug: apideck-createsupplierresponse
- name: CreateTaxRateResponse
  property_count: 7
  slug: apideck-createtaxrateresponse
- name: CreateTimeOffRequestResponse
  property_count: 7
  slug: apideck-createtimeoffrequestresponse
- name: CreateTrackingCategoryResponse
  property_count: 7
  slug: apideck-createtrackingcategoryresponse
- name: CreateUploadSessionRequest
  property_count: 5
  slug: apideck-createuploadsessionrequest
- name: CreateUploadSessionResponse
  property_count: 7
  slug: apideck-createuploadsessionresponse
- name: CreateUserResponse
  property_count: 7
  slug: apideck-createuserresponse
- name: CreditNote
  property_count: 37
  slug: apideck-creditnote
- name: CreditNotesFilter
  property_count: 1
  slug: apideck-creditnotesfilter
- name: CreditNotesSort
  property_count: 2
  slug: apideck-creditnotessort
- name: Credit or Debit
  property_count: 0
  slug: apideck-creditordebit
- name: CrmEventType
  property_count: 0
  slug: apideck-crmeventtype
- name: CrmWebhookEvent
  property_count: 0
  slug: apideck-crmwebhookevent
- name: Currency
  property_count: 0
  slug: apideck-currency
- name: Currency Exchange Rate
  property_count: 0
  slug: apideck-currencyrate
- name: Customer
  property_count: 39
  slug: apideck-customer
- name: CustomersFilter
  property_count: 8
  slug: apideck-customersfilter
- name: CustomersSort
  property_count: 2
  slug: apideck-customerssort
- name: CustomField
  property_count: 4
  slug: apideck-customfield
- name: CustomMappings
  property_count: 0
  slug: apideck-custommappings
- name: CustomObject
  property_count: 9
  slug: apideck-customobject
- name: CustomObjectSchema
  property_count: 11
  slug: apideck-customobjectschema
- name: CustomObjectSchemasSort
  property_count: 2
  slug: apideck-customobjectschemassort
- name: CustomObjectsSort
  property_count: 2
  slug: apideck-customobjectssort
- name: Deceased Date
  property_count: 0
  slug: apideck-deceasedon
- name: Deduction
  property_count: 2
  slug: apideck-deduction
- name: DeleteAccountingDepartmentResponse
  property_count: 7
  slug: apideck-deleteaccountingdepartmentresponse
- name: DeleteAccountingEmployeeResponse
  property_count: 7
  slug: apideck-deleteaccountingemployeeresponse
- name: DeleteAccountingLocationResponse
  property_count: 7
  slug: apideck-deleteaccountinglocationresponse
- name: DeleteActivityResponse
  property_count: 7
  slug: apideck-deleteactivityresponse
- name: DeleteAttachmentResponse
  property_count: 7
  slug: apideck-deleteattachmentresponse
- name: DeleteBankAccountResponse
  property_count: 6
  slug: apideck-deletebankaccountresponse
- name: DeleteBankFeedAccountResponse
  property_count: 7
  slug: apideck-deletebankfeedaccountresponse
- name: DeleteBankFeedStatementResponse
  property_count: 7
  slug: apideck-deletebankfeedstatementresponse
- name: DeleteBillPaymentResponse
  property_count: 7
  slug: apideck-deletebillpaymentresponse
- name: DeleteBillResponse
  property_count: 7
  slug: apideck-deletebillresponse
- name: DeleteCompanyResponse
  property_count: 7
  slug: apideck-deletecompanyresponse
- name: DeleteContactResponse
  property_count: 7
  slug: apideck-deletecontactresponse
- name: DeleteCreditNoteResponse
  property_count: 7
  slug: apideck-deletecreditnoteresponse
- name: DeleteCustomerResponse
  property_count: 7
  slug: apideck-deletecustomerresponse
- name: DeleteCustomObjectResponse
  property_count: 7
  slug: apideck-deletecustomobjectresponse
- name: DeleteCustomObjectSchemaResponse
  property_count: 7
  slug: apideck-deletecustomobjectschemaresponse
- name: Deleted
  property_count: 0
  slug: apideck-deleted
- name: DeleteDepartmentResponse
  property_count: 7
  slug: apideck-deletedepartmentresponse
- name: DeleteDriveGroupResponse
  property_count: 7
  slug: apideck-deletedrivegroupresponse
- name: DeleteDriveResponse
  property_count: 7
  slug: apideck-deletedriveresponse
- name: DeleteEmployeeResponse
  property_count: 7
  slug: apideck-deleteemployeeresponse
- name: DeleteExpenseCategoryResponse
  property_count: 7
  slug: apideck-deleteexpensecategoryresponse
- name: DeleteExpenseReportResponse
  property_count: 7
  slug: apideck-deleteexpensereportresponse
- name: DeleteExpenseResponse
  property_count: 7
  slug: apideck-deleteexpenseresponse
- name: DeleteFileResponse
  property_count: 7
  slug: apideck-deletefileresponse
- name: DeleteFolderResponse
  property_count: 7
  slug: apideck-deletefolderresponse
- name: DeleteHrisCompanyResponse
  property_count: 7
  slug: apideck-deletehriscompanyresponse
- name: DeleteInvoiceItemResponse
  property_count: 0
  slug: apideck-deleteinvoiceitemresponse
- name: DeleteInvoiceResponse
  property_count: 7
  slug: apideck-deleteinvoiceresponse
- name: DeleteJournalEntryResponse
  property_count: 7
  slug: apideck-deletejournalentryresponse
- name: DeleteLeadResponse
  property_count: 7
  slug: apideck-deleteleadresponse
- name: DeleteLedgerAccountResponse
  property_count: 7
  slug: apideck-deleteledgeraccountresponse
- name: DeleteNoteResponse
  property_count: 7
  slug: apideck-deletenoteresponse
- name: DeleteOpportunityResponse
  property_count: 7
  slug: apideck-deleteopportunityresponse
- name: DeletePaymentResponse
  property_count: 7
  slug: apideck-deletepaymentresponse
- name: DeletePipelineResponse
  property_count: 7
  slug: apideck-deletepipelineresponse
- name: DeleteProjectResponse
  property_count: 6
  slug: apideck-deleteprojectresponse
- name: DeletePurchaseOrderResponse
  property_count: 7
  slug: apideck-deletepurchaseorderresponse
- name: DeleteQuoteResponse
  property_count: 6
  slug: apideck-deletequoteresponse
- name: DeleteRefundResponse
  property_count: 7
  slug: apideck-deleterefundresponse
- name: DeleteSharedLinkResponse
  property_count: 7
  slug: apideck-deletesharedlinkresponse
- name: DeleteSubsidiaryResponse
  property_count: 7
  slug: apideck-deletesubsidiaryresponse
- name: DeleteSupplierResponse
  property_count: 7
  slug: apideck-deletesupplierresponse
- name: DeleteTaxRateResponse
  property_count: 7
  slug: apideck-deletetaxrateresponse
- name: DeleteTimeOffRequestResponse
  property_count: 7
  slug: apideck-deletetimeoffrequestresponse
- name: DeleteTrackingCategoryResponse
  property_count: 7
  slug: apideck-deletetrackingcategoryresponse
- name: DeleteUploadSessionResponse
  property_count: 7
  slug: apideck-deleteuploadsessionresponse
- name: DeleteUserResponse
  property_count: 7
  slug: apideck-deleteuserresponse
- name: Department
  property_count: 11
  slug: apideck-department
- name: Department ID
  property_count: 0
  slug: apideck-departmentid
- name: Department
  property_count: 0
  slug: apideck-deprecateddepartment
- name: Linked Supplier
  property_count: 5
  slug: apideck-deprecatedlinkedsupplier
- name: DeprecatedLinkedTrackingCategory
  property_count: 2
  slug: apideck-deprecatedlinkedtrackingcategory
- name: Description
  property_count: 0
  slug: apideck-description
- name: Discount Percentage
  property_count: 0
  slug: apideck-discountpercentage
- name: Display id
  property_count: 0
  slug: apideck-displayid
- name: Division
  property_count: 0
  slug: apideck-division
- name: DownstreamId
  property_count: 0
  slug: apideck-downstreamid
- name: Drive
  property_count: 9
  slug: apideck-drive
- name: DriveGroup
  property_count: 10
  slug: apideck-drivegroup
- name: DriveGroupsFilter
  property_count: 1
  slug: apideck-drivegroupsfilter
- name: DrivesFilter
  property_count: 1
  slug: apideck-drivesfilter
- name: Due date
  property_count: 0
  slug: apideck-duedate
- name: Email
  property_count: 3
  slug: apideck-email
- name: Employee
  property_count: 67
  slug: apideck-employee
- name: compensation
  property_count: 8
  slug: apideck-employeecompensation
- name: Employee ID
  property_count: 0
  slug: apideck-employeeid
- name: job
  property_count: 14
  slug: apideck-employeejob
- name: EmployeeList
  property_count: 5
  slug: apideck-employeelist
- name: Employee number
  property_count: 0
  slug: apideck-employeenumber
- name: EmployeePayroll
  property_count: 10
  slug: apideck-employeepayroll
- name: EmployeeSchedules
  property_count: 2
  slug: apideck-employeeschedules
- name: EmployeesFilter
  property_count: 11
  slug: apideck-employeesfilter
- name: EmployeesOneFilter
  property_count: 1
  slug: apideck-employeesonefilter
- name: EmployeesSort
  property_count: 2
  slug: apideck-employeessort
- name: Employment status
  property_count: 0
  slug: apideck-employmentstatus
- name: Expense
  property_count: 35
  slug: apideck-expense
- name: ExpenseCategoriesFilter
  property_count: 2
  slug: apideck-expensecategoriesfilter
- name: ExpenseCategory
  property_count: 19
  slug: apideck-expensecategory
- name: ExpenseLineItem
  property_count: 20
  slug: apideck-expenselineitem
- name: ExpenseReport
  property_count: 33
  slug: apideck-expensereport
- name: ExpenseReportLineItem
  property_count: 24
  slug: apideck-expensereportlineitem
- name: ExpenseReportsFilter
  property_count: 3
  slug: apideck-expensereportsfilter
- name: ExpensesFilter
  property_count: 3
  slug: apideck-expensesfilter
- name: ExpiresAt
  property_count: 0
  slug: apideck-expiresat
- name: FilesFilter
  property_count: 3
  slug: apideck-filesfilter
- name: FileSize
  property_count: 0
  slug: apideck-filesize
- name: FilesSearch
  property_count: 3
  slug: apideck-filessearch
- name: FilesSort
  property_count: 2
  slug: apideck-filessort
- name: FileStorageEventType
  property_count: 0
  slug: apideck-filestorageeventtype
- name: FileStorageWebhookEvent
  property_count: 0
  slug: apideck-filestoragewebhookevent
- name: FileType
  property_count: 0
  slug: apideck-filetype
- name: First name
  property_count: 0
  slug: apideck-firstname
- name: Folder
  property_count: 15
  slug: apideck-folder
- name: Gender
  property_count: 0
  slug: apideck-gender
- name: GetAccountingDepartmentResponse
  property_count: 7
  slug: apideck-getaccountingdepartmentresponse
- name: GetAccountingDepartmentsResponse
  property_count: 9
  slug: apideck-getaccountingdepartmentsresponse
- name: GetAccountingEmployeeResponse
  property_count: 7
  slug: apideck-getaccountingemployeeresponse
- name: GetAccountingEmployeesResponse
  property_count: 9
  slug: apideck-getaccountingemployeesresponse
- name: GetAccountingLocationResponse
  property_count: 7
  slug: apideck-getaccountinglocationresponse
- name: GetAccountingLocationsResponse
  property_count: 9
  slug: apideck-getaccountinglocationsresponse
- name: GetActivitiesResponse
  property_count: 9
  slug: apideck-getactivitiesresponse
- name: GetActivityResponse
  property_count: 7
  slug: apideck-getactivityresponse
- name: GetAgedCreditorsResponse
  property_count: 7
  slug: apideck-getagedcreditorsresponse
- name: GetAgedDebtorsResponse
  property_count: 7
  slug: apideck-getageddebtorsresponse
- name: GetAttachmentResponse
  property_count: 7
  slug: apideck-getattachmentresponse
- name: GetAttachmentsResponse
  property_count: 9
  slug: apideck-getattachmentsresponse
- name: GetBalanceSheetResponse
  property_count: 7
  slug: apideck-getbalancesheetresponse
- name: GetBankAccountResponse
  property_count: 6
  slug: apideck-getbankaccountresponse
- name: GetBankAccountsResponse
  property_count: 8
  slug: apideck-getbankaccountsresponse
- name: GetBankFeedAccountResponse
  property_count: 7
  slug: apideck-getbankfeedaccountresponse
- name: GetBankFeedAccountsResponse
  property_count: 9
  slug: apideck-getbankfeedaccountsresponse
- name: GetBankFeedStatementResponse
  property_count: 7
  slug: apideck-getbankfeedstatementresponse
- name: GetBankFeedStatementsResponse
  property_count: 9
  slug: apideck-getbankfeedstatementsresponse
- name: GetBillPaymentResponse
  property_count: 7
  slug: apideck-getbillpaymentresponse
- name: GetBillPaymentsResponse
  property_count: 9
  slug: apideck-getbillpaymentsresponse
- name: GetBillResponse
  property_count: 7
  slug: apideck-getbillresponse
- name: GetBillsResponse
  property_count: 9
  slug: apideck-getbillsresponse
- name: GetCategoriesResponse
  property_count: 9
  slug: apideck-getcategoriesresponse
- name: GetCategoryResponse
  property_count: 7
  slug: apideck-getcategoryresponse
- name: GetCompaniesResponse
  property_count: 8
  slug: apideck-getcompaniesresponse
- name: GetCompanyInfoResponse
  property_count: 7
  slug: apideck-getcompanyinforesponse
- name: GetCompanyResponse
  property_count: 7
  slug: apideck-getcompanyresponse
- name: GetContactResponse
  property_count: 7
  slug: apideck-getcontactresponse
- name: GetContactsResponse
  property_count: 9
  slug: apideck-getcontactsresponse
- name: GetCreditNoteResponse
  property_count: 7
  slug: apideck-getcreditnoteresponse
- name: GetCreditNotesResponse
  property_count: 9
  slug: apideck-getcreditnotesresponse
- name: GetCustomerResponse
  property_count: 7
  slug: apideck-getcustomerresponse
- name: GetCustomersResponse
  property_count: 9
  slug: apideck-getcustomersresponse
- name: GetCustomObjectResponse
  property_count: 7
  slug: apideck-getcustomobjectresponse
- name: GetCustomObjectSchemaResponse
  property_count: 7
  slug: apideck-getcustomobjectschemaresponse
- name: GetCustomObjectSchemasResponse
  property_count: 9
  slug: apideck-getcustomobjectschemasresponse
- name: GetCustomObjectsResponse
  property_count: 9
  slug: apideck-getcustomobjectsresponse
- name: GetDepartmentResponse
  property_count: 7
  slug: apideck-getdepartmentresponse
- name: GetDepartmentsResponse
  property_count: 9
  slug: apideck-getdepartmentsresponse
- name: GetDriveGroupResponse
  property_count: 7
  slug: apideck-getdrivegroupresponse
- name: GetDriveGroupsResponse
  property_count: 9
  slug: apideck-getdrivegroupsresponse
- name: GetDriveResponse
  property_count: 7
  slug: apideck-getdriveresponse
- name: GetDrivesResponse
  property_count: 9
  slug: apideck-getdrivesresponse
- name: GetEmployeePayrollResponse
  property_count: 7
  slug: apideck-getemployeepayrollresponse
- name: GetEmployeePayrollsResponse
  property_count: 7
  slug: apideck-getemployeepayrollsresponse
- name: GetEmployeeResponse
  property_count: 7
  slug: apideck-getemployeeresponse
- name: GetEmployeeSchedulesResponse
  property_count: 7
  slug: apideck-getemployeeschedulesresponse
- name: GetEmployeesResponse
  property_count: 9
  slug: apideck-getemployeesresponse
- name: GetExpenseCategoriesResponse
  property_count: 9
  slug: apideck-getexpensecategoriesresponse
- name: GetExpenseCategoryResponse
  property_count: 7
  slug: apideck-getexpensecategoryresponse
- name: GetExpenseReportResponse
  property_count: 7
  slug: apideck-getexpensereportresponse
- name: GetExpenseReportsResponse
  property_count: 9
  slug: apideck-getexpensereportsresponse
- name: GetExpenseResponse
  property_count: 7
  slug: apideck-getexpenseresponse
- name: GetExpensesResponse
  property_count: 9
  slug: apideck-getexpensesresponse
- name: GetFileResponse
  property_count: 7
  slug: apideck-getfileresponse
- name: GetFilesResponse
  property_count: 9
  slug: apideck-getfilesresponse
- name: GetFolderResponse
  property_count: 7
  slug: apideck-getfolderresponse
- name: GetFoldersResponse
  property_count: 9
  slug: apideck-getfoldersresponse
- name: GetHrisCompaniesResponse
  property_count: 9
  slug: apideck-gethriscompaniesresponse
- name: GetHrisCompanyResponse
  property_count: 7
  slug: apideck-gethriscompanyresponse
- name: GetHrisJobResponse
  property_count: 7
  slug: apideck-gethrisjobresponse
- name: GetHrisJobsResponse
  property_count: 7
  slug: apideck-gethrisjobsresponse
- name: GetInvoiceItemResponse
  property_count: 7
  slug: apideck-getinvoiceitemresponse
- name: GetInvoiceItemsResponse
  property_count: 9
  slug: apideck-getinvoiceitemsresponse
- name: GetInvoiceResponse
  property_count: 7
  slug: apideck-getinvoiceresponse
- name: GetInvoicesResponse
  property_count: 9
  slug: apideck-getinvoicesresponse
- name: GetJournalEntriesResponse
  property_count: 9
  slug: apideck-getjournalentriesresponse
- name: GetJournalEntryResponse
  property_count: 7
  slug: apideck-getjournalentryresponse
- name: GetLeadResponse
  property_count: 7
  slug: apideck-getleadresponse
- name: GetLeadsResponse
  property_count: 9
  slug: apideck-getleadsresponse
- name: GetLedgerAccountResponse
  property_count: 7
  slug: apideck-getledgeraccountresponse
- name: GetLedgerAccountsResponse
  property_count: 9
  slug: apideck-getledgeraccountsresponse
- name: GetNoteResponse
  property_count: 7
  slug: apideck-getnoteresponse
- name: GetNotesResponse
  property_count: 9
  slug: apideck-getnotesresponse
- name: GetOpportunitiesResponse
  property_count: 9
  slug: apideck-getopportunitiesresponse
- name: GetOpportunityResponse
  property_count: 7
  slug: apideck-getopportunityresponse
- name: GetPaymentResponse
  property_count: 7
  slug: apideck-getpaymentresponse
- name: GetPaymentsResponse
  property_count: 9
  slug: apideck-getpaymentsresponse
- name: GetPayrollResponse
  property_count: 7
  slug: apideck-getpayrollresponse
- name: GetPayrollsResponse
  property_count: 7
  slug: apideck-getpayrollsresponse
- name: GetPipelineResponse
  property_count: 7
  slug: apideck-getpipelineresponse
- name: GetPipelinesResponse
  property_count: 9
  slug: apideck-getpipelinesresponse
- name: GetProfitAndLossResponse
  property_count: 7
  slug: apideck-getprofitandlossresponse
- name: GetProjectResponse
  property_count: 6
  slug: apideck-getprojectresponse
- name: GetProjectsResponse
  property_count: 8
  slug: apideck-getprojectsresponse
- name: GetPurchaseOrderResponse
  property_count: 7
  slug: apideck-getpurchaseorderresponse
- name: GetPurchaseOrdersResponse
  property_count: 9
  slug: apideck-getpurchaseordersresponse
- name: GetQuoteResponse
  property_count: 6
  slug: apideck-getquoteresponse
- name: GetQuotesResponse
  property_count: 8
  slug: apideck-getquotesresponse
- name: GetRefundResponse
  property_count: 7
  slug: apideck-getrefundresponse
- name: GetRefundsResponse
  property_count: 9
  slug: apideck-getrefundsresponse
- name: GetSharedLinkResponse
  property_count: 7
  slug: apideck-getsharedlinkresponse
- name: GetSharedLinksResponse
  property_count: 9
  slug: apideck-getsharedlinksresponse
- name: GetSubsidiariesResponse
  property_count: 9
  slug: apideck-getsubsidiariesresponse
- name: GetSubsidiaryResponse
  property_count: 7
  slug: apideck-getsubsidiaryresponse
- name: GetSupplierResponse
  property_count: 7
  slug: apideck-getsupplierresponse
- name: GetSuppliersResponse
  property_count: 9
  slug: apideck-getsuppliersresponse
- name: GetTaxRateResponse
  property_count: 7
  slug: apideck-gettaxrateresponse
- name: GetTaxRatesResponse
  property_count: 9
  slug: apideck-gettaxratesresponse
- name: GetTimeOffRequestResponse
  property_count: 7
  slug: apideck-gettimeoffrequestresponse
- name: GetTimeOffRequestsResponse
  property_count: 9
  slug: apideck-gettimeoffrequestsresponse
- name: GetTrackingCategoriesResponse
  property_count: 9
  slug: apideck-gettrackingcategoriesresponse
- name: GetTrackingCategoryResponse
  property_count: 7
  slug: apideck-gettrackingcategoryresponse
- name: GetUploadSessionResponse
  property_count: 7
  slug: apideck-getuploadsessionresponse
- name: GetUserResponse
  property_count: 7
  slug: apideck-getuserresponse
- name: GetUsersResponse
  property_count: 9
  slug: apideck-getusersresponse
- name: HrisCompany
  property_count: 19
  slug: apideck-hriscompany
- name: HrisEventType
  property_count: 0
  slug: apideck-hriseventtype
- name: HrisJob
  property_count: 10
  slug: apideck-hrisjob
- name: HrisJobs
  property_count: 2
  slug: apideck-hrisjobs
- name: HrisWebhookEvent
  property_count: 0
  slug: apideck-hriswebhookevent
- name: IBAN
  property_count: 0
  slug: apideck-iban
- name: ID
  property_count: 0
  slug: apideck-id
- name: ID
  property_count: 0
  slug: apideck-idornull
- name: Initials
  property_count: 0
  slug: apideck-initials
- name: Invoice
  property_count: 51
  slug: apideck-invoice
- name: InvoiceItem
  property_count: 34
  slug: apideck-invoiceitem
- name: InvoiceItemAssetAccount
  property_count: 0
  slug: apideck-invoiceitemassetaccount
- name: InvoiceItemExpenseAccount
  property_count: 0
  slug: apideck-invoiceitemexpenseaccount
- name: InvoiceItemFilter
  property_count: 2
  slug: apideck-invoiceitemfilter
- name: InvoiceItemIncomeAccount
  property_count: 0
  slug: apideck-invoiceitemincomeaccount
- name: InvoiceItemsFilter
  property_count: 4
  slug: apideck-invoiceitemsfilter
- name: InvoiceItemsSort
  property_count: 2
  slug: apideck-invoiceitemssort
- name: Invoice Line Item
  property_count: 35
  slug: apideck-invoicelineitem
- name: InvoiceResponse
  property_count: 2
  slug: apideck-invoiceresponse
- name: InvoicesFilter
  property_count: 4
  slug: apideck-invoicesfilter
- name: InvoicesSort
  property_count: 2
  slug: apideck-invoicessort
- name: Is Reconciled
  property_count: 0
  slug: apideck-isreconciled
- name: Job role
  property_count: 0
  slug: apideck-jobrole
- name: JournalEntriesFilter
  property_count: 2
  slug: apideck-journalentriesfilter
- name: JournalEntriesSort
  property_count: 2
  slug: apideck-journalentriessort
- name: JournalEntry
  property_count: 28
  slug: apideck-journalentry
- name: JournalEntryLineItem
  property_count: 18
  slug: apideck-journalentrylineitem
- name: Language
  property_count: 0
  slug: apideck-language
- name: Last name
  property_count: 0
  slug: apideck-lastname
- name: Lead
  property_count: 30
  slug: apideck-lead
- name: LeadsFilter
  property_count: 5
  slug: apideck-leadsfilter
- name: LeadsSort
  property_count: 2
  slug: apideck-leadssort
- name: LedgerAccount
  property_count: 34
  slug: apideck-ledgeraccount
- name: LedgerAccounts
  property_count: 0
  slug: apideck-ledgeraccounts
- name: LedgerAccountsFilter
  property_count: 3
  slug: apideck-ledgeraccountsfilter
- name: LedgerAccountsSort
  property_count: 2
  slug: apideck-ledgeraccountssort
- name: Type
  property_count: 0
  slug: apideck-lineitemtype
- name: Line number
  property_count: 0
  slug: apideck-linenumber
- name: LinkedAttachment
  property_count: 6
  slug: apideck-linkedattachment
- name: LinkedBankAccount
  property_count: 4
  slug: apideck-linkedbankaccount
- name: LinkedCustomer
  property_count: 6
  slug: apideck-linkedcustomer
- name: LinkedDepartment
  property_count: 4
  slug: apideck-linkeddepartment
- name: LinkedEmployee
  property_count: 3
  slug: apideck-linkedemployee
- name: LinkedExpenseCategory
  property_count: 4
  slug: apideck-linkedexpensecategory
- name: LinkedFinancialAccount
  property_count: 7
  slug: apideck-linkedfinancialaccount
- name: LinkedFolder
  property_count: 2
  slug: apideck-linkedfolder
- name: LinkedInvoiceItem
  property_count: 3
  slug: apideck-linkedinvoiceitem
- name: LinkedLedgerAccount
  property_count: 6
  slug: apideck-linkedledgeraccount
- name: LinkedLocation
  property_count: 4
  slug: apideck-linkedlocation
- name: LinkedParentCustomer
  property_count: 2
  slug: apideck-linkedparentcustomer
- name: LinkedPurchaseOrder
  property_count: 3
  slug: apideck-linkedpurchaseorder
- name: LinkedSubsidiary
  property_count: 3
  slug: apideck-linkedsubsidiary
- name: LinkedSupplier
  property_count: 5
  slug: apideck-linkedsupplier
- name: LinkedTaxDetail
  property_count: 4
  slug: apideck-linkedtaxdetail
- name: LinkedTaxRate
  property_count: 4
  slug: apideck-linkedtaxrate
- name: LinkedTaxStatusDetail
  property_count: 2
  slug: apideck-linkedtaxstatusdetail
- name: Linked tracking categories
  property_count: 0
  slug: apideck-linkedtrackingcategories
- name: LinkedTrackingCategory
  property_count: 5
  slug: apideck-linkedtrackingcategory
- name: LinkedWorktag
  property_count: 2
  slug: apideck-linkedworktag
- name: Links
  property_count: 3
  slug: apideck-links
- name: Location ID
  property_count: 0
  slug: apideck-locationid
- name: Meta
  property_count: 2
  slug: apideck-meta
- name: Middle name
  property_count: 0
  slug: apideck-middlename
- name: Name
  property_count: 0
  slug: apideck-name
- name: Nationality
  property_count: 0
  slug: apideck-nationality
- name: Note
  property_count: 16
  slug: apideck-note
- name: NotFoundResponse
  property_count: 6
  slug: apideck-notfoundresponse
- name: NotImplementedResponse
  property_count: 6
  slug: apideck-notimplementedresponse
- name: OpportunitiesFilter
  property_count: 7
  slug: apideck-opportunitiesfilter
- name: OpportunitiesSort
  property_count: 2
  slug: apideck-opportunitiessort
- name: Opportunity
  property_count: 42
  slug: apideck-opportunity
- name: Outstanding Balance by Currency
  property_count: 3
  slug: apideck-outstandingbalancebycurrency
- name: Outstanding Balance
  property_count: 3
  slug: apideck-outstandingbalancebycustomer
- name: Outstanding Balance
  property_count: 3
  slug: apideck-outstandingbalancebysupplier
- name: Owner
  property_count: 3
  slug: apideck-owner
- name: ParentFolderId
  property_count: 0
  slug: apideck-parentfolderid
- name: PassThroughBody
  property_count: 0
  slug: apideck-passthroughbody
- name: PassThroughQuery
  property_count: 1
  slug: apideck-passthroughquery
- name: Payment
  property_count: 32
  slug: apideck-payment
- name: Payment Frequency
  property_count: 0
  slug: apideck-paymentfrequency
- name: Payment method
  property_count: 0
  slug: apideck-paymentmethod
- name: Payment method reference
  property_count: 0
  slug: apideck-paymentmethodreference
- name: PaymentRequiredResponse
  property_count: 6
  slug: apideck-paymentrequiredresponse
- name: PaymentsFilter
  property_count: 5
  slug: apideck-paymentsfilter
- name: PaymentsSort
  property_count: 2
  slug: apideck-paymentssort
- name: Payment status
  property_count: 0
  slug: apideck-paymentstatus
- name: Payment Type
  property_count: 0
  slug: apideck-paymenttype
- name: Payment Unit
  property_count: 0
  slug: apideck-paymentunit
- name: Payroll
  property_count: 10
  slug: apideck-payroll
- name: PayrollsFilter
  property_count: 2
  slug: apideck-payrollsfilter
- name: PayrollTotals
  property_count: 9
  slug: apideck-payrolltotals
- name: Period Count
  property_count: 0
  slug: apideck-periodcount
- name: Period Length
  property_count: 0
  slug: apideck-periodlength
- name: Person
  property_count: 9
  slug: apideck-person
- name: PhoneNumber
  property_count: 6
  slug: apideck-phonenumber
- name: Photo URL
  property_count: 0
  slug: apideck-photourl
- name: Pipeline
  property_count: 11
  slug: apideck-pipeline
- name: PolicyType
  property_count: 0
  slug: apideck-policytype
- name: ProfitAndLoss
  property_count: 16
  slug: apideck-profitandloss
- name: ProfitAndLossFilter
  property_count: 5
  slug: apideck-profitandlossfilter
- name: ProfitAndLossIndicator
  property_count: 1
  slug: apideck-profitandlossindicator
- name: ProfitAndLossRecord
  property_count: 6
  slug: apideck-profitandlossrecord
- name: ProfitAndLossRecords
  property_count: 0
  slug: apideck-profitandlossrecords
- name: ProfitAndLossSection
  property_count: 6
  slug: apideck-profitandlosssection
- name: Profit and Loss Type
  property_count: 0
  slug: apideck-profitandlosstype
- name: Project
  property_count: 44
  slug: apideck-project
- name: ProjectsFilter
  property_count: 4
  slug: apideck-projectsfilter
- name: ProjectsSort
  property_count: 2
  slug: apideck-projectssort
- name: Pronouns
  property_count: 0
  slug: apideck-pronouns
- name: PurchaseOrder
  property_count: 49
  slug: apideck-purchaseorder
- name: PurchaseOrdersFilter
  property_count: 2
  slug: apideck-purchaseordersfilter
- name: PurchaseOrdersSort
  property_count: 2
  slug: apideck-purchaseorderssort
- name: Quantity
  property_count: 0
  slug: apideck-quantity
- name: Quote
  property_count: 38
  slug: apideck-quote
- name: Quote Line Item
  property_count: 27
  slug: apideck-quotelineitem
- name: raw
  property_count: 0
  slug: apideck-raw
- name: Rebilling
  property_count: 4
  slug: apideck-rebilling
- name: Record URL
  property_count: 0
  slug: apideck-recordurl
- name: Reference
  property_count: 0
  slug: apideck-reference
- name: Refund
  property_count: 38
  slug: apideck-refund
- name: RefundsFilter
  property_count: 2
  slug: apideck-refundsfilter
- name: RefundsSort
  property_count: 2
  slug: apideck-refundssort
- name: Refund status
  property_count: 0
  slug: apideck-refundstatus
- name: Refund Type
  property_count: 0
  slug: apideck-refundtype
- name: Report As Of Date
  property_count: 0
  slug: apideck-reportasofdate
- name: Report Generated At
  property_count: 0
  slug: apideck-reportgeneratedat
- name: Routing Number
  property_count: 0
  slug: apideck-routingnumber
- name: Row version
  property_count: 0
  slug: apideck-rowversion
- name: Sales Tax Number
  property_count: 0
  slug: apideck-salestaxnumber
- name: Salutation
  property_count: 0
  slug: apideck-salutation
- name: Schedule
  property_count: 4
  slug: apideck-schedule
- name: SharedLink
  property_count: 11
  slug: apideck-sharedlink
- name: SharedLinkTarget
  property_count: 3
  slug: apideck-sharedlinktarget
- name: SocialLink
  property_count: 3
  slug: apideck-sociallink
- name: Social Security Number
  property_count: 0
  slug: apideck-socialsecuritynumber
- name: SortDirection
  property_count: 0
  slug: apideck-sortdirection
- name: Subsidiary
  property_count: 15
  slug: apideck-subsidiary
- name: Subsidiary ID
  property_count: 0
  slug: apideck-subsidiaryid
- name: SubsidiaryReference
  property_count: 2
  slug: apideck-subsidiaryreference
- name: Subtotal amount
  property_count: 0
  slug: apideck-subtotal
- name: Suffix
  property_count: 0
  slug: apideck-suffix
- name: Supplier
  property_count: 43
  slug: apideck-supplier
- name: SuppliersFilter
  property_count: 6
  slug: apideck-suppliersfilter
- name: SuppliersSort
  property_count: 2
  slug: apideck-supplierssort
- name: Tags
  property_count: 0
  slug: apideck-tags
- name: Tax
  property_count: 3
  slug: apideck-tax
- name: Taxable
  property_count: 0
  slug: apideck-taxable
- name: Tax amount
  property_count: 0
  slug: apideck-taxamount
- name: Tax Code
  property_count: 0
  slug: apideck-taxcode
- name: Tax inclusive
  property_count: 0
  slug: apideck-taxinclusive
- name: Tax number
  property_count: 0
  slug: apideck-taxnumber
- name: TaxRate
  property_count: 24
  slug: apideck-taxrate
- name: TaxRatesFilter
  property_count: 5
  slug: apideck-taxratesfilter
- name: Team
  property_count: 2
  slug: apideck-team
- name: Payment Terms ID
  property_count: 0
  slug: apideck-termsid
- name: TimeOffRequest
  property_count: 21
  slug: apideck-timeoffrequest
- name: TimeOffRequestsFilter
  property_count: 6
  slug: apideck-timeoffrequestsfilter
- name: Timezone
  property_count: 0
  slug: apideck-timezone
- name: Job title
  property_count: 0
  slug: apideck-title
- name: TooManyRequestsResponse
  property_count: 6
  slug: apideck-toomanyrequestsresponse
- name: Total Amount
  property_count: 0
  slug: apideck-totalamount
- name: Total Amount
  property_count: 0
  slug: apideck-totalplamount
- name: Total tax amount
  property_count: 0
  slug: apideck-totaltax
- name: TrackingCategory
  property_count: 14
  slug: apideck-trackingcategory
- name: Transaction Date
  property_count: 0
  slug: apideck-transactiondate
- name: Transaction note
  property_count: 0
  slug: apideck-transactionnote
- name: Transaction number
  property_count: 0
  slug: apideck-transactionnumber
- name: Transaction Reference
  property_count: 0
  slug: apideck-transactionreference
- name: UnauthorizedResponse
  property_count: 6
  slug: apideck-unauthorizedresponse
- name: UnexpectedErrorResponse
  property_count: 6
  slug: apideck-unexpectederrorresponse
- name: UnifiedFile
  property_count: 20
  slug: apideck-unifiedfile
- name: UnifiedId
  property_count: 1
  slug: apideck-unifiedid
- name: Unit of measure
  property_count: 0
  slug: apideck-unitofmeasure
- name: Unit price
  property_count: 0
  slug: apideck-unitprice
- name: UnprocessableResponse
  property_count: 6
  slug: apideck-unprocessableresponse
- name: UpdateAccountingDepartmentResponse
  property_count: 7
  slug: apideck-updateaccountingdepartmentresponse
- name: UpdateAccountingEmployeeResponse
  property_count: 7
  slug: apideck-updateaccountingemployeeresponse
- name: UpdateAccountingLocationResponse
  property_count: 7
  slug: apideck-updateaccountinglocationresponse
- name: UpdateActivityResponse
  property_count: 7
  slug: apideck-updateactivityresponse
- name: UpdateBankAccountResponse
  property_count: 6
  slug: apideck-updatebankaccountresponse
- name: UpdateBankFeedAccountResponse
  property_count: 7
  slug: apideck-updatebankfeedaccountresponse
- name: UpdateBankFeedStatementResponse
  property_count: 7
  slug: apideck-updatebankfeedstatementresponse
- name: UpdateBillPaymentResponse
  property_count: 7
  slug: apideck-updatebillpaymentresponse
- name: UpdateBillResponse
  property_count: 7
  slug: apideck-updatebillresponse
- name: UpdateCompanyResponse
  property_count: 7
  slug: apideck-updatecompanyresponse
- name: UpdateContactResponse
  property_count: 7
  slug: apideck-updatecontactresponse
- name: UpdateCreditNoteResponse
  property_count: 7
  slug: apideck-updatecreditnoteresponse
- name: UpdateCustomerResponse
  property_count: 7
  slug: apideck-updatecustomerresponse
- name: UpdateCustomObjectResponse
  property_count: 7
  slug: apideck-updatecustomobjectresponse
- name: UpdateCustomObjectSchemaResponse
  property_count: 7
  slug: apideck-updatecustomobjectschemaresponse
- name: Updated at (timestamp)
  property_count: 0
  slug: apideck-updatedat
- name: Updated by
  property_count: 0
  slug: apideck-updatedby
- name: UpdateDepartmentResponse
  property_count: 7
  slug: apideck-updatedepartmentresponse
- name: UpdateDriveGroupResponse
  property_count: 7
  slug: apideck-updatedrivegroupresponse
- name: UpdateDriveResponse
  property_count: 7
  slug: apideck-updatedriveresponse
- name: UpdateEmployeeResponse
  property_count: 7
  slug: apideck-updateemployeeresponse
- name: UpdateExpenseCategoryResponse
  property_count: 7
  slug: apideck-updateexpensecategoryresponse
- name: UpdateExpenseReportResponse
  property_count: 7
  slug: apideck-updateexpensereportresponse
- name: UpdateExpenseResponse
  property_count: 7
  slug: apideck-updateexpenseresponse
- name: UpdateFileRequest
  property_count: 4
  slug: apideck-updatefilerequest
- name: UpdateFileResponse
  property_count: 7
  slug: apideck-updatefileresponse
- name: UpdateFolderRequest
  property_count: 5
  slug: apideck-updatefolderrequest
- name: UpdateFolderResponse
  property_count: 7
  slug: apideck-updatefolderresponse
- name: UpdateHrisCompanyResponse
  property_count: 7
  slug: apideck-updatehriscompanyresponse
- name: UpdateInvoiceItemsResponse
  property_count: 7
  slug: apideck-updateinvoiceitemsresponse
- name: UpdateInvoiceResponse
  property_count: 7
  slug: apideck-updateinvoiceresponse
- name: UpdateJournalEntryResponse
  property_count: 7
  slug: apideck-updatejournalentryresponse
- name: UpdateLeadResponse
  property_count: 7
  slug: apideck-updateleadresponse
- name: UpdateLedgerAccountResponse
  property_count: 7
  slug: apideck-updateledgeraccountresponse
- name: UpdateNoteResponse
  property_count: 7
  slug: apideck-updatenoteresponse
- name: UpdateOpportunityResponse
  property_count: 7
  slug: apideck-updateopportunityresponse
- name: UpdatePaymentResponse
  property_count: 7
  slug: apideck-updatepaymentresponse
- name: UpdatePipelineResponse
  property_count: 7
  slug: apideck-updatepipelineresponse
- name: UpdateProjectResponse
  property_count: 6
  slug: apideck-updateprojectresponse
- name: UpdatePurchaseOrderResponse
  property_count: 7
  slug: apideck-updatepurchaseorderresponse
- name: UpdateQuoteResponse
  property_count: 6
  slug: apideck-updatequoteresponse
- name: UpdateRefundResponse
  property_count: 7
  slug: apideck-updaterefundresponse
- name: UpdateSharedLinkResponse
  property_count: 7
  slug: apideck-updatesharedlinkresponse
- name: UpdateSubsidiaryResponse
  property_count: 7
  slug: apideck-updatesubsidiaryresponse
- name: UpdateSupplierResponse
  property_count: 7
  slug: apideck-updatesupplierresponse
- name: UpdateTaxRateResponse
  property_count: 7
  slug: apideck-updatetaxrateresponse
- name: UpdateTimeOffRequestResponse
  property_count: 7
  slug: apideck-updatetimeoffrequestresponse
- name: UpdateTrackingCategoryResponse
  property_count: 7
  slug: apideck-updatetrackingcategoryresponse
- name: UpdateUploadSessionResponse
  property_count: 7
  slug: apideck-updateuploadsessionresponse
- name: UpdateUserResponse
  property_count: 7
  slug: apideck-updateuserresponse
- name: UploadSession
  property_count: 6
  slug: apideck-uploadsession
- name: User
  property_count: 22
  slug: apideck-user
- name: WebhookEvent
  property_count: 0
  slug: apideck-webhookevent
- name: Website
  property_count: 3
  slug: apideck-website
- name: ID
  property_count: 0
  slug: apideck-writableid
json_structures:
- name: Apideck Structure
  property_count: 0
  slug: apideck-structure
layout: provider
modified: '2026-05-19'
name: Apideck
nav: Providers
network: true
overview: 'Apideck publishes 53 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Aged Creditors API, Aged Debtors API, and 50 more. Tagged areas include Integrations and Unified API.


  The Apideck catalog on APIs.io includes 1 Spectral governance ruleset.


  Apideck''s developer surface includes authentication, documentation, getting-started guide, signup flow, support, changelog, code examples, and 29 more developer resources.'
plans:
- name: Apideck Plans Pricing
  plan_count: 3
  slug: apideck-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 2
  name: Apideck Rate Limits
  slug: apideck-rate-limits
rules:
- name: Apideck API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apideck-jsonschema-spectral-rules
score:
  band: strong
  composite: 67.4
  delta: 2.5
  facets:
    commercial_clarity: 92.1
    contract_quality: 56.4
    developer_ergonomics: 52.2
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 68.4
  previous_composite: 64.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apideck/refs/heads/main/screenshots/apideck-2026-06-20T172302.png
security:
- kind: authentication
  name: Apideck Authentication
  slug: apideck-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Apideck Domain Security
  slug: apideck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apideck
tags:
- Integrations
- Unified API
website: https://www.apideck.com/
---
