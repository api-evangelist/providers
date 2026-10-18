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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Concur Agentic Access
  operation_count: 55
  slug: concur-agentic-access
  summary_line: 55 operations · 28 acting
api_count: 12
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
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Manage expense reports
  name: SAP Concur Expense Reports API
  slug: concur-expense-reports-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Manage individual expense entries
  name: SAP Concur Expenses API
  slug: concur-expenses-api
- description: Manages user accounts and profiles, including creating, updating, and retrieving user information. Supports provisioning across Identity, Spend, and Travel services with bulk operations for managing m
  name: Concur User Provisioning API
  slug: concur-user-provisioning-api
- description: Allows for the submission and management of digital receipts within Concur Expense.
  name: Concur Receipt API
  slug: concur-receipt-api
- description: Exposes budget and fiscal year data, enabling partners and clients to read and manage fiscal years, budget categories, budget items, budget tracking fields, and budget adjustments through API endpoint
  name: Concur Budget API
  slug: concur-budget-api
- description: Provides an automated integration pathway for certified partner financial networks, issuing banks, and fin-tech partners to submit credit card account and transaction data to Concur Expense in near re
  name: Concur Cards API
  slug: concur-cards-api
- description: Enables the creation of expenses with minimal information such as date, amount, and expense type, with or without a receipt image. Supports attaching receipt files including PNG, PDF, TIFF, and JPEG f
  name: Concur Quick Expense API
  slug: concur-quick-expense-api
- description: Allows users to create custom exchange rates for a company, supporting bulk uploads of exchange rate data for specified currency pairs and effective dates with a maximum of 100 rates per request.
  name: Concur Exchange Rate API
  slug: concur-exchange-rate-api
- description: Allows an external system to interact with financial documents generated from SAP Concur for financial posting into an ERP, providing an automated solution to request approved expense reports, cash ad
  name: Concur Financial Integration API
  slug: concur-financial-integration-api
- description: Creates, updates, and reads user core identity profiles following the SCIM 2.0 standard. Enables looking up SAP Concur UUIDs for accessing other v4 APIs for individual users.
  name: Concur Identity API
  slug: concur-identity-api
- description: Implements the Publish/Subscribe pattern using principles of Event Driven Architecture, notifying clients and partners when specific business events occur such as expense report status changes and tra
  name: Concur Event Subscription Service API
  slug: concur-event-subscription-service-api
- description: Allows clients to add interactions with outside systems to their users SAP Concur experience through application connectors, supporting attendee data fetch, list item fetch, event notifications, and e
  name: Concur Callouts API
  slug: concur-callouts-api
- description: Provides a method for custom hotel source suppliers to provide hotel inventory, rates, and booking related functionality to SAP Concur Online Booking Tool, supporting search, rate retrieval, reservati
  name: Concur Direct Connect Hotel Service API
  slug: concur-direct-connect-hotel-service-api
- description: Enables travel users to access ground transportation inventory from service providers, supporting search, reservation, cancellation, and update operations for ground transportation bookings.
  name: Concur Direct Connect Ground Transportation API
  slug: concur-direct-connect-ground-transportation-api
- description: Facilitates ingestion and retrieval of receipt documents for use within Concur Expense, enabling users to create and retrieve simple receipts by uploading documents with associated metadata.
  name: Concur Spend Documents API
  slug: concur-spend-documents-api
- description: Provides an automated solution for retrieving, adding, updating, and deleting list items within SAP Concur, supporting hierarchical list structures with parent-child relationships across multiple leve
  name: Concur List Item API
  slug: concur-list-item-api
- description: Enables viewing configured lists within SAP Concur products and creating new lists, supporting shared lists across Expense, Invoice, and Request applications with managed list capabilities for partner
  name: Concur Lists API
  slug: concur-lists-api
- description: Enables retrieval of travel profile information for specified users and lists of travel profile summaries, available to developers, travel suppliers, and travel management companies.
  name: Concur Travel Profile API
  slug: concur-travel-profile-api
- description: Allows extraction of travel allowance information from the SAP Concur platform, providing the ability to read travel allowance itinerary data, calculation results, and configuration settings.
  name: Concur Travel Allowance API
  slug: concur-travel-allowance-api
- description: Enables users to create, view, and issue cash advances within Concur Expense. Supports single cash advance creation, retrieval, and issuance operations for both Professional and Standard editions. Req
  name: Concur Cash Advance API
  slug: concur-cash-advance-api
- description: Gives SAP Concur clients the ability to leverage external data to create and update approved purchase orders. Enables direct connections to manage purchase orders and resolve matching exceptions on in
  name: Concur Purchase Order API
  slug: concur-purchase-order-api
- description: 'Enables SAP Concur clients to leverage external data to create purchase requests for pre-authorization of purchase orders. Organizations can establish direct connections to automatically generate and '
  name: Concur Purchase Request API
  slug: concur-purchase-request-api
- description: Provides processes for managing vendor collections used in invoicing, including adding new vendors, updating, retrieving, and deleting information for existing vendors. Supports vendor banking informa
  name: Concur Vendor API
  slug: concur-vendor-api
- description: Enables retrieval and updating of invoices for tax calculation purposes, allowing external tax systems to fetch invoices requiring tax assessment and submit calculated tax amounts and rates back to Co
  name: Concur Sales Tax Validation API
  slug: concur-sales-tax-validation-api
- description: Manages transmission of compliance documents between SAP Concur and validating vendors, enabling vendors to exchange compliance documents, validate them against relevant authoritative or regulatory so
  name: Concur Document Compliance Gateway API
  slug: concur-document-compliance-gateway-api
- description: Enables clients to manage receipt images attached to expense reports and images associated with invoices. Users can retrieve existing images by report ID, image ID, or invoice ID, and upload new image
  name: Concur Image API
  slug: concur-image-api
- description: 'Exposes receipt requests to inform E-Receipt partners which E-Receipts to send to SAP Concur and for which user. Partners receive paginated responses and can filter results using optional timestamps, '
  name: Concur Travel Receipts API
  slug: concur-travel-receipts-api
- description: Retrieves details about locations used by Concur that are valid at a user's company. Supports filtering by name, city, country, and other geographic parameters, and returns location data including IAT
  name: Concur Locations API
  slug: concur-locations-api
- description: Provides access to the configured attendee types within SAP Concur, allowing retrieval and management of attendee type resources used for categorizing attendees in expense reports.
  name: Concur Expense Attendee Types API
  slug: concur-expense-attendee-types-api
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
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Operations for retrieving and updating expense allocations, which distribute expense amounts across cost centers or accounts.
  name: SAP Concur Allocations API
  slug: concur-allocations-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting comments at the report header or individual expense level.
  name: SAP Concur Comments API
  slug: concur-comments-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Manage individual expense line items within expense reports including itemizations, attendees, and custom fields.
  name: SAP Concur Expense Entries API
  slug: concur-expense-entries-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Retrieve expense group policy configurations including expense types, payment types, and workflow settings.
  name: SAP Concur Group Configurations API
  slug: concur-group-configurations-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Retrieve payment batch information for approved expense reports ready for reimbursement processing.
  name: SAP Concur Payment Batches API
  slug: concur-payment-batches-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Create and manage quick expenses captured outside of a formal report. Quick expenses can be promoted to full expense report entries.
  name: SAP Concur Quick Expenses API
  slug: concur-quick-expenses-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Upload and retrieve receipt images associated with expense entries. Supports PNG, JPG, PDF, and TIFF image formats.
  name: SAP Concur Receipt Images API
  slug: concur-receipt-images-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting expense reports, as well as retrieving reports pending approval.
  name: SAP Concur Reports API
  slug: concur-reports-api
- baseURL: https://us.api.concursolutions.com/expensereports/v4/
  baseurl_source: declared
  description: Operations for submitting, approving, recalling, and sending back expense reports through the approval workflow.
  name: SAP Concur Workflows API
  slug: concur-workflows-api
artifact_total: 98
collections:
- collection_type: postman
  name: SAP Concur Expense Expense Reports API
  slug: postman-concur-expense-reports-api
- collection_type: postman
  name: SAP Concur Expense Expense Reports Expenses API
  slug: postman-concur-expenses-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAP Concur Expense Expense Reports API
  slug: open-concur-expense-reports-api
- collection_type: open
  name: SAP Concur Expense Expense Reports Expenses API
  slug: open-concur-expenses-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/plans/concur-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/concur-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/rate-limits/concur-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/concur-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/finops/concur-finops.yml
  title: ''
  type: FinOps
  url: finops/concur-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.concur.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-concur/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/agentic-access/concur-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/concur-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/security/concur-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/concur-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/security/concur-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/concur-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/authentication/concur-authentication.yml
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
- group: company
  title: ''
  type: Blog
  url: https://www.concur.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://developer.concur.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/concur
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
- has_sources: true
  method: generated
  name: Concur Finops
  primary_unit: ''
  service_category: Travel & Expense Management
  slug: concur-finops
  template: false
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
- name: SAP Concur Expense Report Schema
  property_count: 0
  slug: sap-concur-expense-report
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
- class_count: 0
  name: Sap Concur Context
  property_count: 15
  slug: sap-concur-context
layout: provider
modified: '2026-05-19'
name: SAP Concur
nav: Providers
network: true
overview: 'SAP Concur publishes 50 API contracts indexed on the [APIs.io](https://apis.io/) network, including Expense Reports API, Expenses API, Allocations API, and 47 more. Tagged areas include Expense Management, Finance, Invoices, SAP, and Travel.


  The SAP Concur catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  SAP Concur''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, sandbox, and 18 more developer resources.'
plans:
- name: Concur Plans Pricing
  plan_count: 1
  slug: concur-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Concur Rate Limits
  slug: concur-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: SAP Concur — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: concur-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: SAP Concur API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 9
  slug: concur-spectral-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.9
    catalog_earned_first_party: 0.0
    catalog_gap: 53.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.1
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 62.1
    developer_ergonomics: 46.4
    discoverability: 71.4
    operational_transparency: 23.7
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 8.3
      total: 12
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
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
- Invoices
- SAP
- Travel
- Business Travel
- Financial Services
- Invoice Management
- Travel Management
- Financial Management
- Receipts
- Reimbursement
- Reporting
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
website: https://www.concur.com/
---
