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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Sap Concur Expense Agentic Access
  operation_count: 23
  slug: sap-concur-expense-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 11
apis:
- description: Retrieve digital tax invoice data associated with expense entries for compliance and auditing in jurisdictions that require electronic invoicing (e-invoicing). Provides access to CFDI (Mexico), NF-e (
  name: Digital Tax Invoice API
  slug: digital-tax-invoice-api
- description: Retrieve expense group configurations including expense types, expense policies, payment types, and workflow settings. Used to dynamically configure expense capture UIs and enforce policy rules during
  name: Expense Group Configuration API
  slug: expense-group-configuration-api
- description: 'Manage allocation of expenses across multiple cost centers, projects, departments, or GL accounts. Supports percentage-based and amount-based allocation splits for corporate expense policy compliance '
  name: Expense Allocations API
  slug: expense-allocations-api
- description: Retrieve and manage payment batches for processed expense reports ready for reimbursement. Provides visibility into batch payment status, amounts, and payee information for integration with payroll an
  name: Payment Batch v1 API
  slug: payment-batch-v1-api
- description: Manage cost center, project, or GL account allocations for expense entries. Supports percentage-based and amount-based splits.
  name: SAP Concur Expense Allocations API
  slug: sap-concur-expense-allocations-api
- description: Manage individual expense line items within expense reports including itemizations, attendees, and custom fields.
  name: SAP Concur Expense Expense Entries API
  slug: sap-concur-expense-expense-entries-api
- description: Create, read, update, and submit expense reports. Manage the full report lifecycle from draft through approval and reimbursement.
  name: SAP Concur Expense Expense Reports API
  slug: sap-concur-expense-expense-reports-api
- description: Retrieve expense group policy configurations including expense types, payment types, and workflow settings.
  name: SAP Concur Expense Group Configurations API
  slug: sap-concur-expense-group-configurations-api
- description: Retrieve payment batch information for approved expense reports ready for reimbursement processing.
  name: SAP Concur Expense Payment Batches API
  slug: sap-concur-expense-payment-batches-api
- description: Create and manage quick expenses captured outside of a formal report. Quick expenses can be promoted to full expense report entries.
  name: SAP Concur Expense Quick Expenses API
  slug: sap-concur-expense-quick-expenses-api
- description: Upload and retrieve receipt images associated with expense entries. Supports PNG, JPG, PDF, and TIFF image formats.
  name: SAP Concur Expense Receipt Images API
  slug: sap-concur-expense-receipt-images-api
arazzos:
- description: Create an expense entry, upload a receipt image, and confirm the stored image.
  name: SAP Concur Attach Receipt to Entry
  slug: sap-concur-expense-attach-receipt-to-entry-workflow
- description: Capture a quick expense outside of a report and read it back to confirm.
  name: SAP Concur Create Quick Expense
  slug: sap-concur-expense-create-quick-expense-workflow
- description: Create a draft expense report, add an expense entry to it, then read the report back.
  name: SAP Concur Create Report and Add Entry
  slug: sap-concur-expense-create-report-add-entry-workflow
- description: Resolve the user's expense policy, then create a report under it and read it back.
  name: SAP Concur Create Report From Policy
  slug: sap-concur-expense-create-report-from-policy-workflow
- description: List reports pending approval, then read the first one in full detail.
  name: SAP Concur Find Pending Report Detail
  slug: sap-concur-expense-find-pending-report-detail-workflow
- description: Read an expense entry, then list how it is split across cost objects.
  name: SAP Concur Inspect Entry Allocations
  slug: sap-concur-expense-inspect-entry-allocations-workflow
- description: List the entries on a report and fetch the full detail of the first one.
  name: SAP Concur List Entries and Get Detail
  slug: sap-concur-expense-list-entries-get-detail-workflow
- description: Turn a captured quick expense into a report entry, then remove the quick expense.
  name: SAP Concur Promote Quick Expense to Report
  slug: sap-concur-expense-promote-quick-expense-workflow
- description: Retrieve a report and branch on whether it has been paid or is still pending.
  name: SAP Concur Report Status Check
  slug: sap-concur-expense-report-status-check-workflow
- description: Read a draft report, update its header fields, then read it back to confirm.
  name: SAP Concur Update Report and Verify
  slug: sap-concur-expense-update-report-verify-workflow
artifact_total: 75
collections:
- collection_type: postman
  name: SAP Concur Expense API
  slug: postman-sap-concur-expense-report
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAP Concur Expense Allocations API
  slug: open-sap-concur-expense-allocations-api
- collection_type: open
  name: SAP Concur Expense Allocations Expense Entries API
  slug: open-sap-concur-expense-expense-entries-api
- collection_type: open
  name: SAP Concur Expense Allocations Expense Reports API
  slug: open-sap-concur-expense-expense-reports-api
- collection_type: open
  name: SAP Concur Expense Allocations Group Configurations API
  slug: open-sap-concur-expense-group-configurations-api
- collection_type: open
  name: SAP Concur Expense Allocations Payment Batches API
  slug: open-sap-concur-expense-payment-batches-api
- collection_type: open
  name: SAP Concur Expense Allocations Quick Expenses API
  slug: open-sap-concur-expense-quick-expenses-api
- collection_type: open
  name: SAP Concur Expense Allocations Receipt Images API
  slug: open-sap-concur-expense-receipt-images-api
- collection_type: open
  name: SAP Concur Expense API
  slug: open-sap-concur-expense-report
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-concur-expense-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-concur-expense-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-concur-expense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-concur-expense-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-concur-expense-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-concur-expense/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-attach-receipt-to-entry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-create-quick-expense-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-create-report-add-entry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-create-report-from-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-find-pending-report-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-inspect-entry-allocations-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-list-entries-get-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-promote-quick-expense-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-report-status-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-concur-expense-update-report-verify-workflow.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.concur.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.concur.com/api-reference/expense/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.concur.com/api-reference/authentication/getting-started.html
- group: auth
  title: ''
  type: OAuth 2.0
  url: https://developer.concur.com/api-reference/authentication/apidoc.html
- group: other
  title: ''
  type: API Explorer
  url: https://developer.concur.com/api-explorer/
- group: operate
  title: ''
  type: Support
  url: https://developer.concur.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.concur.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://open.concur.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.concur.com/tools-support/release-notes/
- group: operate
  title: ''
  type: Community
  url: https://community.sap.com/topics/concur
- group: company
  title: ''
  type: Blog
  url: https://developer.concur.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/concur
- group: company
  title: ''
  type: Website
  url: https://www.concur.com/
- group: start
  title: ''
  type: Signup
  url: https://www.concur.com/en-us/try-concur.html
- group: build
  title: ''
  type: SDKs
  url: https://github.com/concur/concur-platform-sdk-java
- group: build
  title: ''
  type: PostmanCollection
  url: https://developer.concur.com/tools-support/postman.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sap-concur-expense-report-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sap-concur-expense-report-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sap-concur-expense-entry-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sap-concur-expense-receipt-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sap-concur-expense-report-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sap-concur-expense-entry-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sap-concur-expense-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/sap-concur-expense-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sap-concur-expense-vocabulary.yml
created: '2025-01-01'
description: SAP Concur Expense is a cloud-based travel and expense management solution that automates and streamlines expense reporting, approval workflows, and reimbursement processes for businesses. It integrates with corporate card programs, receipt capture, and ERP systems to provide end-to-end expense lifecycle management with audit controls and policy enforcement.
examples:
- key_count: 10
  name: Sap Concur Expense Create Entry Example
  slug: sap-concur-expense-create-entry-example
- key_count: 3
  name: Sap Concur Expense List Payment Batches Example
  slug: sap-concur-expense-list-payment-batches-example
- key_count: 3
  name: Sap Concur Expense List Reports Example
  slug: sap-concur-expense-list-reports-example
finops:
- name: Sap Concur Expense Finops
  service_category: Expense Management
  slug: sap-concur-expense-finops
image: https://www.concur.com/themes/custom/concur/logo.svg
json_schemas:
- name: Allocation
  property_count: 9
  slug: sap-concur-expense-allocation
- name: AllocationCollection
  property_count: 2
  slug: sap-concur-expense-allocationcollection
- name: SAP Concur Expense Entry
  property_count: 19
  slug: sap-concur-expense-entry
- name: ExpenseEntry
  property_count: 15
  slug: sap-concur-expense-expenseentry
- name: ExpenseEntryCollection
  property_count: 2
  slug: sap-concur-expense-expenseentrycollection
- name: ExpenseEntryCreate
  property_count: 9
  slug: sap-concur-expense-expenseentrycreate
- name: ExpenseEntryCreateResponse
  property_count: 2
  slug: sap-concur-expense-expenseentrycreateresponse
- name: ExpenseEntryUpdate
  property_count: 6
  slug: sap-concur-expense-expenseentryupdate
- name: ExpenseGroupConfig
  property_count: 7
  slug: sap-concur-expense-expensegroupconfig
- name: ExpenseGroupConfigCollection
  property_count: 2
  slug: sap-concur-expense-expensegroupconfigcollection
- name: ExpenseReport
  property_count: 17
  slug: sap-concur-expense-expensereport
- name: ExpenseReportCollection
  property_count: 2
  slug: sap-concur-expense-expensereportcollection
- name: ExpenseReportCreate
  property_count: 5
  slug: sap-concur-expense-expensereportcreate
- name: ExpenseReportCreateResponse
  property_count: 2
  slug: sap-concur-expense-expensereportcreateresponse
- name: ExpenseReportUpdate
  property_count: 3
  slug: sap-concur-expense-expensereportupdate
- name: PaymentBatch
  property_count: 8
  slug: sap-concur-expense-paymentbatch
- name: PaymentBatchCollection
  property_count: 2
  slug: sap-concur-expense-paymentbatchcollection
- name: QuickExpense
  property_count: 12
  slug: sap-concur-expense-quickexpense
- name: QuickExpenseCollection
  property_count: 2
  slug: sap-concur-expense-quickexpensecollection
- name: QuickExpenseCreate
  property_count: 7
  slug: sap-concur-expense-quickexpensecreate
- name: QuickExpenseCreateResponse
  property_count: 2
  slug: sap-concur-expense-quickexpensecreateresponse
- name: QuickExpenseUpdate
  property_count: 6
  slug: sap-concur-expense-quickexpenseupdate
- name: SAP Concur Receipt Image
  property_count: 9
  slug: sap-concur-expense-receipt
- name: ReceiptImage
  property_count: 5
  slug: sap-concur-expense-receiptimage
- name: ReceiptImageCollection
  property_count: 2
  slug: sap-concur-expense-receiptimagecollection
- name: ReceiptImageCreateResponse
  property_count: 2
  slug: sap-concur-expense-receiptimagecreateresponse
- name: SAP Concur Expense Report
  property_count: 18
  slug: sap-concur-expense-report
json_structures:
- name: Sap Concur Expense Entry Structure
  property_count: 0
  slug: sap-concur-expense-entry-structure
- name: Sap Concur Expense Report Structure
  property_count: 0
  slug: sap-concur-expense-report-structure
- name: Sap Concur Expense Structure
  property_count: 0
  slug: sap-concur-expense-structure
jsonld:
- class_count: 0
  name: Sap Concur Expense Context
  property_count: 34
  slug: sap-concur-expense-context
layout: provider
modified: '2026-05-19'
name: SAP Concur Expense
nav: Providers
network: true
overview: 'SAP Concur Expense publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Allocations API, Expense Entries API, Expense Reports API, and 4 more. Tagged areas include Expense Management, Financial Management, Receipts, Reimbursement, and Reporting.


  The SAP Concur Expense catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SAP Concur Expense''s developer surface includes authentication, getting-started guide, support, release notes, engineering blog, signup flow, and 36 more developer resources.'
plans:
- name: Sap Concur Expense Plans Pricing
  plan_count: 1
  slug: sap-concur-expense-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Sap Concur Expense Rate Limits
  slug: sap-concur-expense-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SAP Concur Expense API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sap-concur-expense-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: SAP Concur Expense API Rules
  rule_count: 16
  severity_counts:
    error: 2
    hint: 5
    info: 1
    warn: 8
  slug: sap-concur-expense-rules
scopes:
- name: Sap Concur Expense Scopes
  scope_count: 3
  slug: sap-concur-expense-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 47.8
  delta: 1.9
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 66.9
    developer_ergonomics: 45.2
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 23.7
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-concur-expense/refs/heads/main/screenshots/sap-concur-expense-2026-06-20T193425.png
security:
- kind: authentication
  name: Sap Concur Expense Authentication
  slug: sap-concur-expense-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sap Concur Expense Domain Security
  slug: sap-concur-expense-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sap Concur Expense Vulnerability Disclosure
  slug: sap-concur-expense-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-concur-expense
tags:
- Expense Management
- Financial Management
- Receipts
- Reimbursement
- Reporting
- SAP
- Travel
website: https://www.concur.com/
---
