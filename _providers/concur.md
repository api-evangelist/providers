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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Concur Agentic Access
  operation_count: 5
  slug: concur-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 10
apis:
- description: REST API for managing expense reports, entries, allocations, and attendees. Supports creating, updating, and submitting expense reports with receipt images, policy validation, and approval workflows.
  name: SAP Concur Expense API
  slug: expense-api
- description: REST API for managing travel itineraries, bookings, and travel profiles. Supports searching for travel options, creating bookings, and managing travel policies and preferences.
  name: SAP Concur Travel API
  slug: travel-api
- description: REST API for accounts payable invoice processing including purchase requests, vendor management, payment batches, and invoice approval workflows.
  name: SAP Concur Invoice API
  slug: invoice-api
- description: REST API for submitting and managing digital receipts from e-commerce providers, ground transportation, hotels, and other merchants directly to Concur expense.
  name: SAP Concur Receipts API
  slug: receipts-api
- description: REST API for managing pre-trip travel requests and approvals, enabling employees to submit travel requests for authorization before booking.
  name: SAP Concur Request API
  slug: request-api
- description: SCIM 2.0-compliant API for provisioning and managing Concur user accounts, roles, and profile information with support for bulk operations.
  name: SAP Concur User Provisioning API
  slug: user-provisioning-api
- description: Event subscription API enabling applications to receive real-time notifications when events occur in Concur such as expense report submissions, approvals, and status changes.
  name: SAP Concur Events API
  slug: events-api
- description: REST API for managing custom lists and list items used in expense forms, travel policies, and invoice configurations for dropdown and lookup fields.
  name: SAP Concur Lists API
  slug: lists-api
- description: Manage expense reports
  name: SAP Concur Expense Reports API
  slug: concur-expense-reports-api
- description: Manage individual expense entries
  name: SAP Concur Expenses API
  slug: concur-expenses-api
artifact_total: 53
collections:
- collection_type: postman
  name: SAP Concur Expense Expense Reports API
  slug: postman-concur-expense-reports-api
- collection_type: postman
  name: SAP Concur Expense Expense Reports Expenses API
  slug: postman-concur-expenses-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-concur/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/concur-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/concur-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/concur-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/concur-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sapconcur
- group: start
  title: ''
  type: Portal
  url: https://developer.concur.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.concur.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.concur.com/api-reference/getting-started.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.concur.com/api-reference/authentication/apidoc.html
- group: company
  title: ''
  type: Blog
  url: https://www.concur.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP/concur-platform
- group: operate
  title: ''
  type: Support
  url: https://developer.concur.com/tools-support/support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.concur.com/en-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.concur.com/en-us/privacy-policy
- group: start
  title: ''
  type: Sandbox
  url: https://developer.concur.com/manage-apps/register.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.concur.com/tools-support/release-notes/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.concur.com/en-us/pricing
created: '2024-01-01'
description: SAP Concur provides a comprehensive suite of REST APIs for travel, expense, and invoice management. The Concur API platform enables integration with expense reporting, travel booking, invoice processing, receipt capture, and user management services used by enterprises worldwide for spend management automation.
examples:
- key_count: 6
  name: Concur Createexpensereport Example
  slug: concur-createexpensereport-example
- key_count: 8
  name: Concur Expense Api Expense Example
  slug: concur-expense-api-expense-example
- key_count: 10
  name: Concur Expense Api Expense Report Example
  slug: concur-expense-api-expense-report-example
- key_count: 6
  name: Concur Getexpensereports Example
  slug: concur-getexpensereports-example
features:
- description: Create, submit, and manage expense reports with policy validation and multi-level approval workflows.
  name: Expense Report Management
- description: Capture and process digital receipts from merchants for automatic expense matching.
  name: Receipt Digitization
- description: Search and book travel through API-connected travel management companies and booking tools.
  name: Travel Booking Integration
- description: Automate accounts payable workflows with purchase requests, vendor management, and payment processing.
  name: Invoice Processing
- description: Real-time event subscriptions for expense, travel, and invoice status changes.
  name: Event Notifications
- description: Standards-based user provisioning and management with SCIM 2.0 protocol support.
  name: SCIM User Provisioning
finops:
- name: Concur Finops
  service_category: Travel & Expense Management
  slug: concur-finops
image: /assets/icons/concur.png
integrations:
- description: Financial posting integration for automated expense and invoice data transfer to SAP ERP.
  name: SAP S/4HANA
- description: HR integration for employee data synchronization and travel policy assignment.
  name: SAP SuccessFactors
- description: Automated ride receipt submission from Uber business accounts to Concur expense.
  name: Uber for Business
- description: Ground transportation receipt integration for business ride expense automation.
  name: Lyft
- description: Approval and notification integration for expense workflows within Teams.
  name: Microsoft Teams
json_schemas:
- name: ExpenseReport
  property_count: 10
  slug: concur-expense-api-expense-report
- name: Expense
  property_count: 8
  slug: concur-expense-api-expense
- name: Expense
  property_count: 8
  slug: concur-expense
- name: ExpenseCollection
  property_count: 1
  slug: concur-expensecollection
- name: ExpenseCreate
  property_count: 6
  slug: concur-expensecreate
- name: ExpenseReport
  property_count: 10
  slug: concur-expensereport
- name: ExpenseReportCollection
  property_count: 1
  slug: concur-expensereportcollection
- name: ExpenseReportCreate
  property_count: 5
  slug: concur-expensereportcreate
json_structures:
- name: Concur Expense Api Expense Report Structure
  property_count: 10
  slug: concur-expense-api-expense-report-structure
- name: Concur Expense Api Expense Structure
  property_count: 8
  slug: concur-expense-api-expense-structure
- name: Concur Structure
  property_count: 0
  slug: concur-structure
jsonld:
- class_count: 2
  name: Concur Context
  property_count: 15
  slug: concur-context
layout: provider
modified: '2026-05-19'
name: SAP Concur
nav: Providers
network: true
overview: 'SAP Concur publishes 2 APIs on the [APIs.io](https://apis.io/) network: Expense Reports API and Expenses API. Tagged areas include Expense Management, Finance, Invoice, SAP, and Travel.


  The SAP Concur catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SAP Concur''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, sandbox, and 11 more developer resources.'
plans:
- name: Concur Plans Pricing
  plan_count: 1
  slug: concur-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 2
  name: Concur Rate Limits
  slug: concur-rate-limits
rules:
- name: SAP Concur API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: concur-jsonschema-spectral-rules
- name: SAP Concur API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 9
  slug: concur-spectral-rules
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.0
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/screenshots/concur-2026-06-20T174842.png
security:
- kind: authentication
  name: Concur Authentication
  slug: concur-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Concur Domain Security
  slug: concur-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Concur Vulnerability Disclosure
  slug: concur-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: concur
tags:
- Expense Management
- Finance
- Invoice
- SAP
- Travel
use_cases:
- description: Integrate Concur expense and invoice data with ERP systems for automated financial posting.
  name: ERP Integration
- description: Build travel booking integrations connecting corporate travel policies with booking engines.
  name: Travel Management
- description: Automatically capture and match digital receipts from e-commerce and travel merchants.
  name: Receipt Automation
- description: Extract expense and travel data for spend analytics, compliance reporting, and budget tracking.
  name: Spend Analytics
- description: Automate Concur user provisioning as part of employee onboarding workflows.
  name: Employee Onboarding
website: https://developer.concur.com/
---
