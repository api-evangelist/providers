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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Peoplesoft Agentic Access
  operation_count: 60
  slug: peoplesoft-agentic-access
  summary_line: 60 operations · 15 acting
api_count: 48
apis:
- description: Framework for extracting and flattening PeopleSoft data for machine learning and analytics purposes. Uses PeopleSoft Search Framework technology with OpenSearch to build, index, and register data mode
  name: PeopleSoft Data Distribution Framework API
  slug: data-distribution-framework-api
- description: REST API for retrieving employee details by name or employee ID, and for looking up direct reports based on manager name or ID. Supports the Employee Directory chatbot skill and integration with exter
  name: PeopleSoft Employee Directory API
  slug: employee-directory-api
- description: REST API for creating, updating, and retrieving absence requests, viewing employee absence balances by type, and retrieving absence configuration rules. Supports Absence Management chatbot skill and s
  name: PeopleSoft Absence Management API
  slug: absence-management-api
- description: Delivered REST API endpoints for retrieving paycheck header details, earnings, deductions, taxes, direct deposits, employer paid benefits, garnishments, and year-end forms for North American payroll p
  name: PeopleSoft Payroll for North America API
  slug: payroll-for-north-america-api
- description: REST API endpoints for the Global Payroll skill, providing access to payroll data, product profile information, and chatbot framework resources for international payroll processing across multiple cou
  name: PeopleSoft Global Payroll API
  slug: global-payroll-api
- description: REST API for retrieving employee country and business partner contact details. Shared utility services used across all delivered HCM skills and integration scenarios.
  name: PeopleSoft HR Common Utility Services API
  slug: hr-common-utility-services-api
- description: 'Delivered REST API endpoints for expense report management including fetching expense reports by status, creation date, or sheet name, retrieving transaction details, managing wallet entries, expense '
  name: PeopleSoft Expenses API
  slug: expenses-api
- description: Delivered REST API endpoints for invoice and payment management including fetching disputed invoices, invoice status inquiries, payment status tracking, payment inquiries, and payment difference resol
  name: PeopleSoft eSettlements API
  slug: esettlements-api
- description: Delivered REST API endpoints for requisition management including retrieving requisitions for items, getting requester lists and names, and checking requisition status. Supports the full procure-to-pa
  name: PeopleSoft eProcurement API
  slug: eprocurement-api
- description: Comprehensive REST API for the Supplier Portal providing access to bid details, managed content such as announcements and events, overdue shipment tracking, purchase order acknowledgement, invoice and
  name: PeopleSoft Supplier Portal API
  slug: supplier-portal-api
- description: Accounts payable operations
  name: PeopleSoft Accounts Payable API
  slug: peoplesoft-accounts-payable-api
- description: Accounts receivable operations
  name: PeopleSoft Accounts Receivable API
  slug: peoplesoft-accounts-receivable-api
- description: Admissions operations
  name: PeopleSoft Admissions API
  slug: peoplesoft-admissions-api
- description: Analytics and reporting operations
  name: PeopleSoft Analytics API
  slug: peoplesoft-analytics-api
- description: Approval workflow operations
  name: PeopleSoft Approvals API
  slug: peoplesoft-approvals-api
- description: Benefits administration operations
  name: PeopleSoft Benefits API
  slug: peoplesoft-benefits-api
- description: Branding and theme operations
  name: PeopleSoft Branding API
  slug: peoplesoft-branding-api
- description: Budget management operations
  name: PeopleSoft Budgets API
  slug: peoplesoft-budgets-api
- description: Candidate and application operations
  name: PeopleSoft Candidates API
  slug: peoplesoft-candidates-api
- description: Case management operations
  name: PeopleSoft Cases API
  slug: peoplesoft-cases-api
- description: Chatbot integration operations
  name: PeopleSoft Chatbot API
  slug: peoplesoft-chatbot-api
- description: Component interface operations
  name: PeopleSoft Component Interfaces API
  slug: peoplesoft-component-interfaces-api
- description: Content management operations
  name: PeopleSoft Content API
  slug: peoplesoft-content-api
- description: Customer data operations
  name: PeopleSoft Customers API
  slug: peoplesoft-customers-api
- description: Employee data operations
  name: PeopleSoft Employees API
  slug: peoplesoft-employees-api
- description: Enrollment operations
  name: PeopleSoft Enrollment API
  slug: peoplesoft-enrollment-api
- description: Environment provisioning and management
  name: PeopleSoft Environments API
  slug: peoplesoft-environments-api
- description: Expense management operations
  name: PeopleSoft Expenses API
  slug: peoplesoft-expenses-api
- description: Financial aid operations
  name: PeopleSoft Financial Aid API
  slug: peoplesoft-financial-aid-api
- description: Forecasting operations
  name: PeopleSoft Forecasts API
  slug: peoplesoft-forecasts-api
- description: General ledger operations
  name: PeopleSoft General Ledger API
  slug: peoplesoft-general-ledger-api
- description: Inventory management operations
  name: PeopleSoft Inventory API
  slug: peoplesoft-inventory-api
- description: Job posting and search operations
  name: PeopleSoft Jobs API
  slug: peoplesoft-jobs-api
- description: Notification management operations
  name: PeopleSoft Notifications API
  slug: peoplesoft-notifications-api
- description: Order fulfillment operations
  name: PeopleSoft Orders API
  slug: peoplesoft-orders-api
- description: Payroll operations
  name: PeopleSoft Payroll API
  slug: peoplesoft-payroll-api
- description: Pivot grid and dashboard operations
  name: PeopleSoft Pivot Grids API
  slug: peoplesoft-pivot-grids-api
- description: Process scheduling and monitoring operations
  name: PeopleSoft Processes API
  slug: peoplesoft-processes-api
- description: Procurement and purchasing operations
  name: PeopleSoft Procurement API
  slug: peoplesoft-procurement-api
- description: Query execution and management operations
  name: PeopleSoft Queries API
  slug: peoplesoft-queries-api
- description: PeopleSoft REST resource operations
  name: PeopleSoft Resources API
  slug: peoplesoft-resources-api
- description: Sales operations
  name: PeopleSoft Sales API
  slug: peoplesoft-sales-api
- description: Search and indexing operations
  name: PeopleSoft Search API
  slug: peoplesoft-search-api
- description: Integration Broker service operations
  name: PeopleSoft Service Operations API
  slug: peoplesoft-service-operations-api
- description: ASF service operations
  name: PeopleSoft Services API
  slug: peoplesoft-services-api
- description: Student record operations
  name: PeopleSoft Students API
  slug: peoplesoft-students-api
- description: Provisioning template operations
  name: PeopleSoft Templates API
  slug: peoplesoft-templates-api
- description: Update and patch management operations
  name: PeopleSoft Updates API
  slug: peoplesoft-updates-api
arazzos:
- description: List the user's pending approvals and approve, deny, or push back the first one when present.
  name: PeopleSoft Process a Pending Approval
  slug: peoplesoft-approval-process-workflow
- description: Read a Component Interface record and branch to update it if it exists, otherwise create it.
  name: PeopleSoft Component Interface Upsert
  slug: peoplesoft-component-upsert-workflow
- description: Search CRM customers, pull the matched customer record, then create a service case for them.
  name: PeopleSoft Find a Customer and Open a Case
  slug: peoplesoft-customer-case-workflow
- description: Find an employee in a department, pull their full record, then review payroll runs and benefit enrollments.
  name: PeopleSoft Employee Payroll and Benefits Review
  slug: peoplesoft-employee-payroll-review-workflow
- description: Pick a provisioning template, provision a Cloud Manager environment, poll until ready, then notify recipients.
  name: PeopleSoft Provision Environment and Notify
  slug: peoplesoft-env-provision-notify-workflow
- description: Pull general ledger journals for a date range, then gather AP vouchers and AR items for the same period.
  name: PeopleSoft Financial Period Review
  slug: peoplesoft-financial-period-review-workflow
- description: List available pivot grid definitions, then retrieve the data for the first grid with optional filters.
  name: PeopleSoft Pivot Grid Dashboard Pull
  slug: peoplesoft-pivot-grid-dashboard-workflow
- description: List available PS Query definitions, confirm the requested query exists, then execute it with paging.
  name: PeopleSoft List and Execute a Query
  slug: peoplesoft-query-export-workflow
- description: Search recruiting postings by keyword, pull the matched job details, then submit a candidate application.
  name: PeopleSoft Search Jobs and Submit Application
  slug: peoplesoft-recruiting-apply-workflow
- description: Submit a Process Scheduler request, poll its instance until it finishes, then list the recent process queue.
  name: PeopleSoft Submit Process and Poll to Completion
  slug: peoplesoft-scheduled-process-poll-workflow
- description: Trigger a Search Framework index build, then run a full-text search to verify content is searchable.
  name: PeopleSoft Rebuild Search Index and Verify
  slug: peoplesoft-search-reindex-workflow
- description: Find a student in a term, pull their record, then review class enrollment and financial aid awards.
  name: PeopleSoft Student Enrollment and Aid Review
  slug: peoplesoft-student-enrollment-review-workflow
artifact_total: 169
collections:
- collection_type: postman
  name: PeopleSoft Application Services Framework API
  slug: postman-application-services-framework
- collection_type: postman
  name: PeopleSoft Approval Workflow Engine API
  slug: postman-approval-workflow-engine
- collection_type: postman
  name: PeopleSoft Campus Solutions API
  slug: postman-campus-solutions
- collection_type: postman
  name: PeopleSoft Chatbot Integration Framework API
  slug: postman-chatbot-integration
- collection_type: postman
  name: PeopleSoft Cloud Manager API
  slug: postman-cloud-manager
- collection_type: postman
  name: PeopleSoft Component Interface API
  slug: postman-component-interface
- collection_type: postman
  name: PeopleSoft CRM API
  slug: postman-crm
- collection_type: postman
  name: PeopleSoft Enterprise Performance Management API
  slug: postman-enterprise-performance-management
- collection_type: postman
  name: PeopleSoft Financials API
  slug: postman-financials
- collection_type: postman
  name: PeopleSoft HCM API
  slug: postman-hcm
- collection_type: postman
  name: PeopleSoft Integration Broker
  slug: postman-integration-broker
- collection_type: postman
  name: PeopleSoft Interaction Hub API
  slug: postman-interaction-hub
- collection_type: postman
  name: PeopleSoft Notification Framework API
  slug: postman-notification-framework
- collection_type: postman
  name: PeopleSoft Pivot Grid API
  slug: postman-pivot-grid
- collection_type: postman
  name: PeopleSoft Process Scheduler API
  slug: postman-process-scheduler
- collection_type: postman
  name: PeopleSoft Query API
  slug: postman-query
- collection_type: postman
  name: PeopleSoft Recruiting and Talent Management API
  slug: postman-recruiting-talent-management
- collection_type: postman
  name: PeopleSoft REST API
  slug: postman-rest-api
- collection_type: postman
  name: PeopleSoft Search Framework API
  slug: postman-search-framework
- collection_type: postman
  name: PeopleSoft Supply Chain Management API
  slug: postman-supply-chain-management
- collection_type: postman
  name: PeopleSoft Update Manager API
  slug: postman-update-manager
- collection_type: open
  name: PeopleSoft Application Services Framework API
  slug: open-application-services-framework
- collection_type: open
  name: PeopleSoft Approval Workflow Engine API
  slug: open-approval-workflow-engine
- collection_type: open
  name: PeopleSoft Campus Solutions API
  slug: open-campus-solutions
- collection_type: open
  name: PeopleSoft Chatbot Integration Framework API
  slug: open-chatbot-integration
- collection_type: open
  name: PeopleSoft Cloud Manager API
  slug: open-cloud-manager
- collection_type: open
  name: PeopleSoft Component Interface API
  slug: open-component-interface
- collection_type: open
  name: PeopleSoft CRM API
  slug: open-crm
- collection_type: open
  name: PeopleSoft Enterprise Performance Management API
  slug: open-enterprise-performance-management
- collection_type: open
  name: PeopleSoft Financials API
  slug: open-financials
- collection_type: open
  name: PeopleSoft HCM API
  slug: open-hcm
- collection_type: open
  name: PeopleSoft Integration Broker
  slug: open-integration-broker
- collection_type: open
  name: PeopleSoft Interaction Hub API
  slug: open-interaction-hub
- collection_type: open
  name: PeopleSoft Notification Framework API
  slug: open-notification-framework
- collection_type: open
  name: PeopleSoft Pivot Grid API
  slug: open-pivot-grid
- collection_type: open
  name: PeopleSoft Process Scheduler API
  slug: open-process-scheduler
- collection_type: open
  name: PeopleSoft Query API
  slug: open-query
- collection_type: open
  name: PeopleSoft Recruiting and Talent Management API
  slug: open-recruiting-talent-management
- collection_type: open
  name: PeopleSoft REST API
  slug: open-rest-api
- collection_type: open
  name: PeopleSoft Search Framework API
  slug: open-search-framework
- collection_type: open
  name: PeopleSoft Supply Chain Management API
  slug: open-supply-chain-management
- collection_type: open
  name: PeopleSoft Update Manager API
  slug: open-update-manager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/peoplesoft-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peoplesoft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/peoplesoft-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/peoplesoft-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/peoplesoft/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-approval-process-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-component-upsert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-customer-case-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-employee-payroll-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-env-provision-notify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-financial-period-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-pivot-grid-dashboard-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-query-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-recruiting-apply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-scheduled-process-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-search-reindex-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/peoplesoft-student-enrollment-review-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peoplesoft-inc
- group: start
  title: ''
  type: Portal
  url: https://www.oracle.com/applications/peoplesoft/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/applications/peoplesoft/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/applications/peoplesoft/peopletools/index.html
- group: start
  title: ''
  type: Information Portal
  url: https://docs.oracle.com/cd/E52319_01/infoportal/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/cd/F30998_01/pt858pbr2/eng/pt/tsec/concept_UnderstandingOAuth2_0.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/peoplesoft/
- group: operate
  title: ''
  type: ChangeLog
  url: https://blogs.oracle.com/peoplesoft/category/ps-image-and-release-updates
- group: docs
  title: ''
  type: PeopleCode API Reference
  url: https://docs.oracle.com/cd/E25688_01/pt852pbr0/eng/psbooks/tpcr/book.htm
- group: auth
  title: ''
  type: Security
  url: https://www.oracle.com/security-alerts/
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com/
- group: other
  title: ''
  type: Knowledge Base
  url: https://docs.oracle.com/en/applications/peoplesoft/
- group: operate
  title: ''
  type: Community
  url: https://community.oracle.com/customerconnect/categories/peoplesoft
- group: operate
  title: ''
  type: Forums
  url: https://forums.oracle.com/ords/apexds/domain/dev-community/category/peoplesoft_enterprise
- group: other
  title: ''
  type: PeopleSoft on OCI
  url: https://docs.oracle.com/cd/E52319_01/infoportal/opc.html
- group: learn
  title: ''
  type: Training
  url: https://education.oracle.com/peoplesoft
- group: learn
  title: ''
  type: Videos
  url: https://docs.oracle.com/cd/E52319_01/infoportal/videos.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/corporate/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/contracts/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/services-privacy-policy/
- group: company
  title: ''
  type: News
  url: https://docs.oracle.com/cd/E52319_01/infoportal/news.html
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/applications/peoplesoft/
- group: start
  title: ''
  type: Login
  url: https://cloud.oracle.com/
- group: start
  title: ''
  type: Signup
  url: https://cloud.oracle.com/
- group: other
  title: ''
  type: REST API Endpoints
  url: https://docs.oracle.com/cd/G36917_01/ps91pbr20/eng/ps/eccp/UnderstandingRestApiEndpointsForPeoplesoft.html
created: '2024-01-15'
description: Collection of Oracle PeopleSoft Enterprise application APIs for Human Capital Management, Financial Management, Supply Chain Management, CRM, Campus Solutions, and engineering intelligence across PeopleTools platform services.
examples:
- key_count: 10
  name: Peoplesoft Campus Solutions Class Enrollment Example
  slug: peoplesoft-campus-solutions-class-enrollment-example
- key_count: 13
  name: Peoplesoft Campus Solutions Student Example
  slug: peoplesoft-campus-solutions-student-example
- key_count: 10
  name: Peoplesoft Crm Case Example
  slug: peoplesoft-crm-case-example
- key_count: 10
  name: Peoplesoft Financials Journal Entry Example
  slug: peoplesoft-financials-journal-entry-example
- key_count: 9
  name: Peoplesoft Financials Voucher Example
  slug: peoplesoft-financials-voucher-example
- key_count: 15
  name: Peoplesoft Hcm Employee Example
  slug: peoplesoft-hcm-employee-example
- key_count: 9
  name: Peoplesoft Hcm Position Example
  slug: peoplesoft-hcm-position-example
- key_count: 9
  name: Peoplesoft Supply Chain Management Purchase Order Example
  slug: peoplesoft-supply-chain-management-purchase-order-example
features:
- description: RESTful APIs via PeopleTools Integration Broker for JSON-based integration with external systems.
  name: REST Web Services
- description: Modern REST API layer with OpenAPI spec generation, proper HTTP status codes, and JSON payloads.
  name: Application Services Framework
- description: Enterprise messaging and integration platform supporting SOAP, REST, and asynchronous messaging.
  name: Integration Broker
- description: Programmatic access to PeopleSoft component business logic for data entry and validation.
  name: Component Interface API
- description: Execute PeopleSoft queries and retrieve results via REST for reporting and analytics.
  name: Query API
- description: Human Capital Management APIs for workforce administration, benefits, payroll, and talent management.
  name: HCM APIs
- description: APIs for general ledger, accounts payable/receivable, asset management, and procurement.
  name: Financial Management APIs
- description: APIs for inventory, purchasing, order management, and supplier collaboration.
  name: Supply Chain Management APIs
- description: APIs for student records, admissions, financial aid, and academic advisement.
  name: Campus Solutions APIs
- description: Standards-based OAuth 2.0 authentication for secure API access.
  name: OAuth 2.0 Authentication
- description: APIs for integrating with PeopleSoft Fluid user interface framework.
  name: Fluid UI Integration
- description: Digital assistant and chatbot framework APIs for conversational PeopleSoft interactions.
  name: Chatbot Integration
finops:
- name: Peoplesoft Finops
  service_category: Enterprise Software
  slug: peoplesoft-finops
image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
json_schemas:
- name: ClassEnrollment
  property_count: 10
  slug: peoplesoft-campus-solutions-class-enrollment
- name: Student
  property_count: 13
  slug: peoplesoft-campus-solutions-student
- name: Case
  property_count: 10
  slug: peoplesoft-case
- name: ClassEnrollment
  property_count: 10
  slug: peoplesoft-classenrollment
- name: Case
  property_count: 10
  slug: peoplesoft-crm-case
- name: Employee
  property_count: 26
  slug: peoplesoft-employee
- name: JournalEntry
  property_count: 10
  slug: peoplesoft-financials-journal-entry
- name: Voucher
  property_count: 9
  slug: peoplesoft-financials-voucher
- name: Employee
  property_count: 26
  slug: peoplesoft-hcm-employee
- name: Position
  property_count: 9
  slug: peoplesoft-hcm-position
- name: JournalEntry
  property_count: 10
  slug: peoplesoft-journalentry
- name: Position
  property_count: 9
  slug: peoplesoft-position
- name: PurchaseOrder
  property_count: 9
  slug: peoplesoft-purchaseorder
- name: Student
  property_count: 13
  slug: peoplesoft-student
- name: PurchaseOrder
  property_count: 9
  slug: peoplesoft-supply-chain-management-purchase-order
- name: Voucher
  property_count: 9
  slug: peoplesoft-voucher
json_structures:
- name: Peoplesoft Campus Solutions Class Enrollment Structure
  property_count: 10
  slug: peoplesoft-campus-solutions-class-enrollment-structure
- name: Peoplesoft Campus Solutions Student Structure
  property_count: 13
  slug: peoplesoft-campus-solutions-student-structure
- name: Peoplesoft Crm Case Structure
  property_count: 10
  slug: peoplesoft-crm-case-structure
- name: Peoplesoft Financials Journal Entry Structure
  property_count: 10
  slug: peoplesoft-financials-journal-entry-structure
- name: Peoplesoft Financials Voucher Structure
  property_count: 9
  slug: peoplesoft-financials-voucher-structure
- name: Peoplesoft Hcm Employee Structure
  property_count: 26
  slug: peoplesoft-hcm-employee-structure
- name: Peoplesoft Hcm Position Structure
  property_count: 9
  slug: peoplesoft-hcm-position-structure
- name: Peoplesoft Structure
  property_count: 0
  slug: peoplesoft-structure
- name: Peoplesoft Supply Chain Management Purchase Order Structure
  property_count: 9
  slug: peoplesoft-supply-chain-management-purchase-order-structure
jsonld:
- class_count: 8
  name: Peoplesoft Context
  property_count: 77
  slug: peoplesoft-context
layout: provider
modified: '2026-04-17'
name: PeopleSoft
nav: Providers
network: true
overview: 'PeopleSoft publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Accounts Payable API, Accounts Receivable API, Admissions API, and 35 more. Tagged areas include Campus Solutions, CRM, Enterprise Software, ERP, and Financial Management.


  The PeopleSoft catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  PeopleSoft''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, support, and 36 more developer resources.'
plans:
- name: Peoplesoft Plans Pricing
  plan_count: 1
  slug: peoplesoft-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Peoplesoft Rate Limits
  slug: peoplesoft-rate-limits
rules:
- name: PeopleSoft API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: peoplesoft-jsonschema-spectral-rules
- name: PeopleSoft API Rules
  rule_count: 24
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 9
  slug: peoplesoft-spectral-rules
scopes:
- name: Peoplesoft Scopes
  scope_count: 0
  slug: peoplesoft-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.9
  delta: -5.1
  facets:
    commercial_clarity: 73.7
    contract_quality: 68.3
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 38
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/peoplesoft/refs/heads/main/screenshots/peoplesoft-2026-06-20T191552.png
security:
- kind: authentication
  name: Peoplesoft Authentication
  slug: peoplesoft-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Peoplesoft Domain Security
  slug: peoplesoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peoplesoft
solutions:
- description: Human Capital Management for workforce administration, benefits, payroll, talent, and workforce planning.
  name: PeopleSoft HCM
- description: Financial and Supply Chain Management for general ledger, AP/AR, procurement, and inventory.
  name: PeopleSoft FSCM
- description: Higher education platform for student records, admissions, financial aid, and academic management.
  name: PeopleSoft Campus Solutions
- description: Customer Relationship Management for sales, marketing, and service automation.
  name: PeopleSoft CRM
tags:
- Campus Solutions
- CRM
- Enterprise Software
- ERP
- Financial Management
- HCM
- Supply Chain Management
use_cases:
- description: Integrate HCM data with payroll, benefits, and talent management platforms.
  name: HR System Integration
- description: Exchange financial transactions and reporting data with external ERP and accounting systems.
  name: Financial Data Exchange
- description: Integrate campus solutions with learning management and student portal systems.
  name: Student Information System
- description: Automate procurement, inventory, and supplier management workflows.
  name: Supply Chain Automation
- description: Build employee and student self-service applications using PeopleSoft APIs.
  name: Self-Service Portals
- description: Power mobile apps for employee self-service, approvals, and time entry.
  name: Mobile Applications
- description: Connect PeopleSoft with Oracle Integration Cloud and other cloud platforms.
  name: Cloud Integration
- description: Extract data via Query API for business intelligence and analytics platforms.
  name: Reporting and Analytics
website: https://www.oracle.com/applications/peoplesoft/
---
