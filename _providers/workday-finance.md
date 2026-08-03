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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Workday Finance Agentic Access
  operation_count: 16
  slug: workday-finance-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 17
apis:
- description: SOAP API for managing revenue recognition, contracts, and billing processes. Supports revenue accounting workflows and contract analysis within Workday Financial Management.
  name: Workday Revenue Management API
  slug: workday-revenue-management-api
- description: SOAP API for expense management, including expense reports, approval workflows, and reimbursements. Part of Workday Spend Management for tracking and controlling employee and organizational expenses.
  name: Workday Expenses API
  slug: workday-expenses-api
- description: SOAP API for managing cash positions, bank transactions, and treasury operations. Supports cash flow forecasting, bank account management, and financial reconciliation processes.
  name: Workday Cash Management API
  slug: workday-cash-management-api
- description: SOAP API for budget planning, tracking, and analysis. Enables programmatic management of budgets, budget amendments, and budget structure data within Workday Financial Management.
  name: Workday Budgets API
  slug: workday-budgets-api
- description: SOAP API for project management, tracking project costs, billing, and resource allocation. Supports project-based accounting, cost capture, and resource planning workflows.
  name: Workday Projects API
  slug: workday-projects-api
- description: SOAP API for settlement management and payment services. Supports payment processing, bank routing, settlement runs, direct debit mandates, payment acknowledgements, cash balance checks, and escheatme
  name: Workday Settlement Services API
  slug: workday-settlement-services-api
- description: SOAP API exposing Workday Financials Inventory data. Supports goods delivery, stock tracking, inventory adjustments, cycle counting, par management, directed picks, put-away operations, recalls, and r
  name: Workday Inventory API
  slug: workday-inventory-api
- description: SOAP API for Professional Services Automation integrations. Exposes Workday Financials data for managing client-facing projects, services billing, resource staffing, and expense reporting within profe
  name: Workday Professional Services Automation API
  slug: workday-professional-services-automation-api
- description: General ledger accounts and account structures
  name: Workday Finance Accounts API
  slug: workday-finance-accounts-api
- description: Cost center management and reporting
  name: Workday Finance Cost Centers API
  slug: workday-finance-cost-centers-api
- description: Fiscal period and year management
  name: Workday Finance Financial Periods API
  slug: workday-finance-financial-periods-api
- description: Journal entry creation and retrieval
  name: Workday Finance Journal Entries API
  slug: workday-finance-journal-entries-api
- description: Purchase order creation and management
  name: Workday Finance Purchase Orders API
  slug: workday-finance-purchase-orders-api
- description: Purchase requisition management
  name: Workday Finance Requisitions API
  slug: workday-finance-requisitions-api
- description: Supplier invoice processing
  name: Workday Finance Supplier Invoices API
  slug: workday-finance-supplier-invoices-api
- description: Supplier account management
  name: Workday Finance Suppliers API
  slug: workday-finance-suppliers-api
- description: Worktag dimension management
  name: Workday Finance Worktags API
  slug: workday-finance-worktags-api
arazzos:
- description: Find an open financial period, then list and inspect its journal entries.
  name: Workday Finance Audit Open Period Journals
  slug: workday-finance-audit-open-period-journals-workflow
- description: Resolve a supplier, confirm it is active, then raise a purchase order against it.
  name: Workday Finance Onboard Supplier and Raise Purchase Order
  slug: workday-finance-onboard-supplier-purchase-order-workflow
- description: Confirm a supplier, list its outstanding invoices, then trace one back to its purchase order.
  name: Workday Finance Reconcile Supplier Invoices
  slug: workday-finance-reconcile-supplier-invoices-workflow
- description: Confirm the target period is open, post a journal entry, then read it back.
  name: Workday Finance Record Balanced Journal Entry
  slug: workday-finance-record-balanced-journal-entry-workflow
- description: Create a supplier invoice in procurement, then post the matching expense journal entry to the general ledger.
  name: Workday Finance Record Supplier Invoice Expense
  slug: workday-finance-record-supplier-invoice-expense-workflow
- description: Find an approved requisition, confirm the supplier, then raise a purchase order.
  name: Workday Finance Requisition to Purchase Order
  slug: workday-finance-requisition-to-purchase-order-workflow
- description: Read a purchase order, confirm its supplier, then create a matching supplier invoice.
  name: Workday Finance Supplier Invoice From Purchase Order
  slug: workday-finance-supplier-invoice-from-purchase-order-workflow
- description: Resolve a supplier from the directory, then list its purchase orders and invoices.
  name: Workday Finance Supplier Spend Overview
  slug: workday-finance-supplier-spend-overview-workflow
- description: Resolve cost center and worktag dimensions, then post a tagged journal entry.
  name: Workday Finance Tag Journal Entry With Worktags
  slug: workday-finance-tag-journal-entry-with-worktags-workflow
- description: Find a general ledger account by type, then read its full detail and balance.
  name: Workday Finance Verify Account Balance
  slug: workday-finance-verify-account-balance-workflow
artifact_total: 64
collections:
- collection_type: postman
  name: Workday Finance Financial Management API
  slug: postman-workday-finance-financial-management
- collection_type: postman
  name: Workday Finance Procurement API
  slug: postman-workday-finance-procurement
- collection_type: open
  name: Workday Finance Financial Management API
  slug: open-workday-finance-financial-management
- collection_type: open
  name: Workday Finance Procurement API
  slug: open-workday-finance-procurement
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-finance-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-finance-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-finance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-finance-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-finance/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-audit-open-period-journals-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-onboard-supplier-purchase-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-reconcile-supplier-invoices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-record-balanced-journal-entry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-record-supplier-invoice-expense-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-requisition-to-purchase-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-supplier-invoice-from-purchase-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-supplier-spend-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-tag-journal-entry-with-worktags-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-finance-verify-account-balance-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://community.workday.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.workday.com/r/Enterprise_Interface_API_Concepts_and_Resources/Getting_Started_with_Workday_Web_Services
- group: auth
  title: ''
  type: Authentication
  url: https://doc.workday.com/r/Enterprise_Interface_API_Concepts_and_Resources/Authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://doc.workday.com/r/Enterprise_Interface_API_Concepts_and_Resources/Rate_Limiting
- group: start
  title: ''
  type: Console
  url: https://developer.workday.com/about
- group: company
  title: ''
  type: Website
  url: https://www.workday.com/en-us/products/financial-management/overview.html
- group: start
  title: ''
  type: Signup
  url: https://resourcecenter.workday.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/services/support.html
- group: operate
  title: ''
  type: Community
  url: https://www.workday.com/en-us/services/community.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workday.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.workday.com/en-US/home
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.workday.com/articles/16827
- group: docs
  title: ''
  type: Reference
  url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-finance-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/workday-finance-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-finance-journal-entry-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-finance-supplier-invoice-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-finance-purchase-order-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-finance-vocabulary.yml
created: '2024-01-01'
description: APIs for Workday's cloud-based financial management system, enabling enterprise resource planning, accounting, financial analytics, procurement, grants management, inventory, and settlement services.
examples:
- key_count: 2
  name: Workday Finance Create Supplier Invoice Example
  slug: workday-finance-create-supplier-invoice-example
- key_count: 2
  name: Workday Finance List Journal Entries Example
  slug: workday-finance-list-journal-entries-example
finops:
- name: Workday Finance Finops
  service_category: Financial Management SaaS
  slug: workday-finance-finops
graphqls:
- description: This GraphQL schema represents the Workday Financial Management ERP domain, covering the full spectrum of enterprise financial operations. Workday Financial Management is a cloud-native ERP platform p
  name: Workday Financial Management GraphQL Schema
  slug: workday-finance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-finance.png
json_schemas:
- name: Account
  property_count: 8
  slug: workday-finance-account
- name: CostCenter
  property_count: 7
  slug: workday-finance-costcenter
- name: ErrorResponse
  property_count: 2
  slug: workday-finance-errorresponse
- name: FinancialPeriod
  property_count: 8
  slug: workday-finance-financialperiod
- name: Workday Finance Journal Entry
  property_count: 10
  slug: workday-finance-journal-entry
- name: JournalEntry
  property_count: 9
  slug: workday-finance-journalentry
- name: JournalEntryCreate
  property_count: 4
  slug: workday-finance-journalentrycreate
- name: JournalEntryLine
  property_count: 7
  slug: workday-finance-journalentryline
- name: Workday Finance Purchase Order
  property_count: 10
  slug: workday-finance-purchase-order
- name: PurchaseOrder
  property_count: 10
  slug: workday-finance-purchaseorder
- name: PurchaseOrderCreate
  property_count: 3
  slug: workday-finance-purchaseordercreate
- name: Requisition
  property_count: 9
  slug: workday-finance-requisition
- name: ResourceReference
  property_count: 3
  slug: workday-finance-resourcereference
- name: Workday Finance Supplier Invoice
  property_count: 11
  slug: workday-finance-supplier-invoice
- name: Supplier
  property_count: 8
  slug: workday-finance-supplier
- name: SupplierInvoice
  property_count: 11
  slug: workday-finance-supplierinvoice
- name: SupplierInvoiceCreate
  property_count: 6
  slug: workday-finance-supplierinvoicecreate
- name: Worktag
  property_count: 6
  slug: workday-finance-worktag
json_structures:
- name: Workday Finance Journal Entry Structure
  property_count: 0
  slug: workday-finance-journal-entry-structure
- name: Workday Finance Structure
  property_count: 0
  slug: workday-finance-structure
jsonld:
- class_count: 35
  name: Workday Finance Context
  property_count: 6
  slug: workday-finance-context
layout: provider
modified: '2026-05-19'
name: Workday Finance
nav: Providers
network: true
overview: 'Workday Finance publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Cost Centers API, Financial Periods API, and 6 more. Tagged areas include Accounting, Cloud, Enterprise, ERP, and Finance.


  The Workday Finance catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Finance''s developer surface includes authentication, developer portal, documentation, getting-started guide, developer console, signup flow, engineering blog, and 32 more developer resources.'
plans:
- name: Workday Finance Plans Pricing
  plan_count: 1
  slug: workday-finance-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Workday Finance Rate Limits
  slug: workday-finance-rate-limits
rules:
- name: Workday Finance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-finance-jsonschema-spectral-rules
- name: Workday Finance API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 7
  slug: workday-finance-rules
score:
  band: strong
  composite: 64.5
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 72.3
    developer_ergonomics: 63.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-finance/refs/heads/main/screenshots/workday-finance-2026-06-20T201558.png
security:
- kind: authentication
  name: Workday Finance Authentication
  slug: workday-finance-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Workday Finance Domain Security
  slug: workday-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Finance Trust Center
  slug: workday-finance-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-finance
tags:
- Accounting
- Cloud
- Enterprise
- ERP
- Finance
- Financial Management
website: https://www.workday.com/en-us/products/financial-management/overview.html
---
