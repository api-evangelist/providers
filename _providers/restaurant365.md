---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Restaurant365 Agentic Access
  operation_count: 20
  slug: restaurant365-agentic-access
  summary_line: 20 operations · 4 acting
api_count: 9
apis:
- description: Create accounts payable invoices in the customer database
  name: Restaurant365 AP Invoices API
  slug: restaurant365-ap-invoices-api
- description: Deleted entity tracking
  name: Restaurant365 Audit API
  slug: restaurant365-audit-api
- description: Obtain a bearer token for subsequent requests
  name: Restaurant365 Authentication API
  slug: restaurant365-authentication-api
- description: Create AP invoices by GL account and journal entries
  name: Restaurant365 General Ledger API
  slug: restaurant365-general-ledger-api
- description: Employees, labor detail, payroll, and POS employees
  name: Restaurant365 Labor API
  slug: restaurant365-labor-api
- description: OData service metadata
  name: Restaurant365 Metadata API
  slug: restaurant365-metadata-api
- description: Companies, locations, GL accounts, items, and job titles
  name: Restaurant365 Reference Data API
  slug: restaurant365-reference-data-api
- description: Sales ticket headers, detail, and payments
  name: Restaurant365 Sales API
  slug: restaurant365-sales-api
- description: Financial transactions and transaction detail
  name: Restaurant365 Transactions API
  slug: restaurant365-transactions-api
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices API
  slug: open-restaurant365-ap-invoices-api
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices Audit API
  slug: open-restaurant365-audit-api
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices Authentication API
  slug: open-restaurant365-authentication-api
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices General Ledger API
  slug: open-restaurant365-general-ledger-api
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices Labor API
  slug: open-restaurant365-labor-api
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices Metadata API
  slug: open-restaurant365-metadata-api
- collection_type: open
  name: Restaurant365 OData Connector
  slug: open-restaurant365-odata-connector
- collection_type: open
  name: R365 API
  slug: open-restaurant365-r365-api
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices Reference Data API
  slug: open-restaurant365-reference-data-api
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices Sales API
  slug: open-restaurant365-sales-api
- collection_type: open
  name: Restaurant365 OData Connector AP Invoices Transactions API
  slug: open-restaurant365-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/restaurant365-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restaurant365-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/restaurant365-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.restaurant365.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.restaurant365.com/docs/r365-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.restaurant365.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/restaurant365-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/restaurant365-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/restaurant365-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/restaurant365-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.restaurant365.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/restaurant365
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/restaurant365-cloud-erp-for-restaurants
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.restaurant365.com/llms.txt
created: '2026-06-02'
description: Restaurant365 is a cloud-based restaurant accounting, inventory, and operations platform serving thousands of restaurant locations across the United States. Its developer offering centers on the R365 API, which lets approved third-party vendors and partners connect to a customer's R365 database to retrieve data and create or push records such as AP invoices and general ledger entries. A complementary OData connector exposes sales, transaction, location, GL account, employee, and labor data for use in external reporting and business-intelligence tools. API access is provisioned per customer through R365 Support, with bearer-token authentication on the R365 API and Domain\Username basic authentication on the OData connector.
examples:
- key_count: 2
  name: Odata Connector List Sales Employee Example
  slug: odata-connector-list-sales-employee-example
- key_count: 2
  name: Odata Connector List Transactions Example
  slug: odata-connector-list-transactions-example
- key_count: 2
  name: R365 Api Authenticate Example
  slug: r365-api-authenticate-example
- key_count: 2
  name: R365 Api Create Ap Invoices Example
  slug: r365-api-create-ap-invoices-example
- key_count: 2
  name: R365 Api Create Ap Invoices Gl Example
  slug: r365-api-create-ap-invoices-gl-example
- key_count: 2
  name: R365 Api Create Journal Entries Example
  slug: r365-api-create-journal-entries-example
features:
- description: Push vendor AP invoices into the customer database with item or GL-account detail.
  name: AP Invoice Automation
- description: Create balanced journal entries and GL-coded AP invoices via the R365 API.
  name: General Ledger Posting
- description: Read-only OData views for transactions, sales, labor, and reference data.
  name: OData Reporting Views
- description: rowVersion property supports pulling only records changed since the last sync.
  name: Incremental Sync
- description: EntityDeleted view exposes records removed from the system for audit reconciliation.
  name: Audit Tracking
finops:
- name: Restaurant365 Finops
  service_category: Restaurant Management Software
  slug: restaurant365-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restaurant365.png
integrations:
- description: Connect to OData views through the Excel OData feed and R365 Excel plug-in.
  name: Excel
- description: Any OData-compatible BI/reporting tool can consume the OData connector views.
  name: Business Intelligence Tools
- description: POSEmployee and sales views map R365 records to point-of-sale data.
  name: POS Systems
json_schemas:
- name: Employee
  property_count: 22
  slug: odata-connector-employee
- name: GLAccount
  property_count: 17
  slug: odata-connector-gl-account
- name: SalesEmployee
  property_count: 25
  slug: odata-connector-sales-employee
- name: Transaction
  property_count: 15
  slug: odata-connector-transaction
- name: APInvoice
  property_count: 16
  slug: r365-api-ap-invoice
- name: JournalEntry
  property_count: 13
  slug: r365-api-journal-entry
json_structures:
- name: Odata Connector Sales Employee Structure
  property_count: 25
  slug: odata-connector-sales-employee-structure
- name: Odata Connector Transaction Structure
  property_count: 15
  slug: odata-connector-transaction-structure
- name: R365 Api Ap Invoice Structure
  property_count: 16
  slug: r365-api-ap-invoice-structure
- name: R365 Api Journal Entry Structure
  property_count: 13
  slug: r365-api-journal-entry-structure
jsonld:
- class_count: 11
  name: Restaurant365 Odata Connector Context
  property_count: 23
  slug: restaurant365-odata-connector-context
- class_count: 3
  name: Restaurant365 R365 Api Context
  property_count: 24
  slug: restaurant365-r365-api-context
layout: provider
modified: '2026-06-03'
name: Restaurant365
nav: Providers
network: true
overview: 'Restaurant365 publishes 9 APIs on the [APIs.io](https://apis.io/) network, including AP Invoices API, Audit API, Authentication API, and 6 more. Tagged areas include Restaurant, Accounting, Inventory, Invoices, and Reporting.


  The Restaurant365 catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Restaurant365''s developer surface includes authentication, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Restaurant365 Plans Pricing
  plan_count: 4
  slug: restaurant365-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Restaurant365 Rate Limits
  slug: restaurant365-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Restaurant365 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restaurant365-jsonschema-spectral-rules
- effective_rule_count: 25
  extends: []
  name: Restaurant365 API Rules
  rule_count: 25
  severity_counts:
    error: 6
    hint: 0
    info: 4
    warn: 15
  slug: restaurant365-rules
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.8
    contract_quality: 74.4
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restaurant365/refs/heads/main/screenshots/restaurant365-2026-06-20T193014.png
security:
- kind: authentication
  name: Restaurant365 Authentication
  slug: restaurant365-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Restaurant365 Domain Security
  slug: restaurant365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: restaurant365
tags:
- Restaurant
- Accounting
- Inventory
- Invoices
- Reporting
- OData
use_cases:
- description: Suppliers push electronic invoices directly into a restaurant's R365 ledger.
  name: Vendor Invoice Integration
- description: Pull sales, labor, and financial data into external BI and reporting tools via OData.
  name: BI And Reporting
- description: Extract labor detail and payroll summary data for downstream payroll processing.
  name: Payroll Export
- description: Replicate transactions and sales into a warehouse using date-range chunked pulls.
  name: Data Warehouse Replication
website: https://www.restaurant365.com
---
