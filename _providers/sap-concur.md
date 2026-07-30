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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Sap Concur Agentic Access
  operation_count: 27
  slug: sap-concur-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 32
apis:
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
- description: Operations for retrieving and updating expense allocations, which distribute expense amounts across cost centers or accounts.
  name: SAP Concur Allocations API
  slug: sap-concur-allocations-api
- description: Operations for creating, retrieving, updating, and deleting comments at the report header or individual expense level.
  name: SAP Concur Comments API
  slug: sap-concur-comments-api
- description: Operations for retrieving, updating, and deleting expense entries (line items) on a report, and retrieving itemizations.
  name: SAP Concur Expenses API
  slug: sap-concur-expenses-api
- description: Operations for creating, retrieving, updating, and deleting expense reports, as well as retrieving reports pending approval.
  name: SAP Concur Reports API
  slug: sap-concur-reports-api
- description: Operations for submitting, approving, recalling, and sending back expense reports through the approval workflow.
  name: SAP Concur Workflows API
  slug: sap-concur-workflows-api
artifact_total: 205
collections:
- collection_type: open
  name: SAP Concur Expense Report API
  slug: open-sap-concur-expense
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-concur-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-concur-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-concur-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-concur-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sapconcur
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.concur.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.concur.com/api-reference/authentication/getting-started.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.concur.com/api-reference/authentication/company-auth.html
- group: operate
  title: ''
  type: Support
  url: https://developer.concur.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.concur.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.concur.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://open.concur.com/
- group: company
  title: ''
  type: Blog
  url: https://www.concur.com/newsroom
- group: start
  title: ''
  type: Signup
  url: https://developer.concur.com/register
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/SAP-docs/preview.developer.concur.com
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.concur.com/tools-support/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.concur.com/tools-support/release-notes/
- group: other
  title: SAP Business Accelerator Hub
  type: Resources
  url: https://api.sap.com/products/SAPConcur/apis/REST
- group: learn
  title: ''
  type: Tutorials
  url: https://developers.sap.com/tutorials/data-to-value-conn-concur-part01..html
created: '2024'
description: SAP Concur is a leading provider of integrated travel, expense, and invoice management solutions. Their APIs enable developers to integrate Concur functionality into their applications, automate business processes, and access travel and expense data.
examples:
- key_count: 6
  name: Sap Concur Approvereport Example
  slug: sap-concur-approvereport-example
- key_count: 6
  name: Sap Concur Createexpensecomment Example
  slug: sap-concur-createexpensecomment-example
- key_count: 6
  name: Sap Concur Createreport Example
  slug: sap-concur-createreport-example
- key_count: 6
  name: Sap Concur Createreportcomment Example
  slug: sap-concur-createreportcomment-example
- key_count: 8
  name: Sap Concur Expense Allocation Example
  slug: sap-concur-expense-allocation-example
- key_count: 2
  name: Sap Concur Expense Amount Example
  slug: sap-concur-expense-amount-example
- key_count: 5
  name: Sap Concur Expense Comment Example
  slug: sap-concur-expense-comment-example
- key_count: 1
  name: Sap Concur Expense Comment Request Example
  slug: sap-concur-expense-comment-request-example
- key_count: 3
  name: Sap Concur Expense Cost Object For Approver Example
  slug: sap-concur-expense-cost-object-for-approver-example
- key_count: 3
  name: Sap Concur Expense Custom Data Example
  slug: sap-concur-expense-custom-data-example
- key_count: 6
  name: Sap Concur Expense Error Response Example
  slug: sap-concur-expense-error-response-example
- key_count: 2
  name: Sap Concur Expense Exchange Rate Example
  slug: sap-concur-expense-exchange-rate-example
- key_count: 12
  name: Sap Concur Expense Expense Detail Example
  slug: sap-concur-expense-expense-detail-example
- key_count: 5
  name: Sap Concur Expense Expense Itemization Example
  slug: sap-concur-expense-expense-itemization-example
- key_count: 4
  name: Sap Concur Expense Expense Summary Example
  slug: sap-concur-expense-expense-summary-example
- key_count: 0
  name: Sap Concur Expense Expense Tax Summary Example
  slug: sap-concur-expense-expense-tax-summary-example
- key_count: 4
  name: Sap Concur Expense Expense Type Example
  slug: sap-concur-expense-expense-type-example
- key_count: 8
  name: Sap Concur Expense Form Field Example
  slug: sap-concur-expense-form-field-example
- key_count: 3
  name: Sap Concur Expense Link Example
  slug: sap-concur-expense-link-example
- key_count: 5
  name: Sap Concur Expense Location Example
  slug: sap-concur-expense-location-example
- key_count: 9
  name: Sap Concur Expense Mileage Example
  slug: sap-concur-expense-mileage-example
- key_count: 10
  name: Sap Concur Expense New Report Example
  slug: sap-concur-expense-new-report-example
- key_count: 3
  name: Sap Concur Expense Payment Type Example
  slug: sap-concur-expense-payment-type-example
- key_count: 5
  name: Sap Concur Expense Report Approve Request Example
  slug: sap-concur-expense-report-approve-request-example
- key_count: 24
  name: Sap Concur Expense Report Details Example
  slug: sap-concur-expense-report-details-example
- key_count: 3
  name: Sap Concur Expense Report Send Back Request Example
  slug: sap-concur-expense-report-send-back-request-example
- key_count: 5
  name: Sap Concur Expense Report To Approve Example
  slug: sap-concur-expense-report-to-approve-example
- key_count: 1
  name: Sap Concur Expense Resource Created Response Example
  slug: sap-concur-expense-resource-created-response-example
- key_count: 3
  name: Sap Concur Expense Travel Allowance Example
  slug: sap-concur-expense-travel-allowance-example
- key_count: 8
  name: Sap Concur Expense Travel Example
  slug: sap-concur-expense-travel-example
- key_count: 2
  name: Sap Concur Expense Update Allocation Request Example
  slug: sap-concur-expense-update-allocation-request-example
- key_count: 9
  name: Sap Concur Expense Update Report Example
  slug: sap-concur-expense-update-report-example
- key_count: 5
  name: Sap Concur Expense Update Submitted Expense Example
  slug: sap-concur-expense-update-submitted-expense-example
- key_count: 5
  name: Sap Concur Expense Update Submitted Report Example
  slug: sap-concur-expense-update-submitted-report-example
- key_count: 3
  name: Sap Concur Expense Vendor Example
  slug: sap-concur-expense-vendor-example
- key_count: 6
  name: Sap Concur Getallocation Example
  slug: sap-concur-getallocation-example
- key_count: 6
  name: Sap Concur Getallocations Example
  slug: sap-concur-getallocations-example
- key_count: 6
  name: Sap Concur Getcostobjectsforapprover Example
  slug: sap-concur-getcostobjectsforapprover-example
- key_count: 6
  name: Sap Concur Getexpense Example
  slug: sap-concur-getexpense-example
- key_count: 6
  name: Sap Concur Getexpensecomments Example
  slug: sap-concur-getexpensecomments-example
- key_count: 6
  name: Sap Concur Getexpenseformfields Example
  slug: sap-concur-getexpenseformfields-example
- key_count: 6
  name: Sap Concur Getexpenseitemizations Example
  slug: sap-concur-getexpenseitemizations-example
- key_count: 6
  name: Sap Concur Getexpenses Example
  slug: sap-concur-getexpenses-example
- key_count: 6
  name: Sap Concur Getreport Example
  slug: sap-concur-getreport-example
- key_count: 6
  name: Sap Concur Getreportcomments Example
  slug: sap-concur-getreportcomments-example
- key_count: 6
  name: Sap Concur Getreportformfields Example
  slug: sap-concur-getreportformfields-example
- key_count: 6
  name: Sap Concur Getreportstoapprove Example
  slug: sap-concur-getreportstoapprove-example
- key_count: 6
  name: Sap Concur Recallreport Example
  slug: sap-concur-recallreport-example
- key_count: 6
  name: Sap Concur Sendbackreport Example
  slug: sap-concur-sendbackreport-example
- key_count: 6
  name: Sap Concur Updateallocation Example
  slug: sap-concur-updateallocation-example
- key_count: 6
  name: Sap Concur Updatereport Example
  slug: sap-concur-updatereport-example
- key_count: 6
  name: Sap Concur Updatereportcomment Example
  slug: sap-concur-updatereportcomment-example
- key_count: 6
  name: Sap Concur Updatesubmittedexpense Example
  slug: sap-concur-updatesubmittedexpense-example
- key_count: 6
  name: Sap Concur Updatesubmittedreport Example
  slug: sap-concur-updatesubmittedreport-example
features:
- description: Secure token-based authentication supporting both company-level and user-level access tokens with automatic refresh.
  name: OAuth 2.0 Authentication
- description: Separate API endpoints for US, US2, EMEA, and China datacenters ensuring data residency compliance.
  name: Multi-Datacenter Support
- description: Publish/Subscribe event-driven architecture for real-time notifications on business events like report submissions.
  name: Event Subscription Service
- description: Standards-based user identity management following SCIM protocol for automated user lifecycle operations.
  name: SCIM 2.0 User Provisioning
- description: Integration framework allowing travel suppliers to provide inventory directly to the Concur booking tool.
  name: Direct Connect Framework
- description: Custom exchange rate management supporting bulk uploads for currency conversion across global operations.
  name: Multi-Currency Exchange Rates
finops:
- name: Sap Concur Finops
  service_category: Travel & Expense Management
  slug: sap-concur-finops
graphqls:
- description: This is a conceptual GraphQL schema for the SAP Concur platform, the leading provider of integrated travel, expense, and invoice management solutions. The schema unifies SAP Concur's multiple REST API
  name: SAP Concur GraphQL Schema
  slug: sap-concur-graphql
image: https://www.concur.com/themes/custom/concur/logo.svg
json_schemas:
- name: Allocation
  property_count: 11
  slug: sap-concur-allocation
- name: Amount
  property_count: 2
  slug: sap-concur-amount
- name: Comment
  property_count: 5
  slug: sap-concur-comment
- name: CommentRequest
  property_count: 1
  slug: sap-concur-commentrequest
- name: CostObjectForApprover
  property_count: 3
  slug: sap-concur-costobjectforapprover
- name: CustomData
  property_count: 3
  slug: sap-concur-customdata
- name: ErrorResponse
  property_count: 6
  slug: sap-concur-errorresponse
- name: ExchangeRate
  property_count: 2
  slug: sap-concur-exchangerate
- name: Allocation
  property_count: 8
  slug: sap-concur-expense-allocation
- name: Amount
  property_count: 2
  slug: sap-concur-expense-amount
- name: CommentRequest
  property_count: 1
  slug: sap-concur-expense-comment-request
- name: Comment
  property_count: 5
  slug: sap-concur-expense-comment
- name: CostObjectForApprover
  property_count: 3
  slug: sap-concur-expense-cost-object-for-approver
- name: CustomData
  property_count: 3
  slug: sap-concur-expense-custom-data
- name: ErrorResponse
  property_count: 6
  slug: sap-concur-expense-error-response
- name: ExchangeRate
  property_count: 2
  slug: sap-concur-expense-exchange-rate
- name: ExpenseDetail
  property_count: 12
  slug: sap-concur-expense-expense-detail
- name: ExpenseItemization
  property_count: 5
  slug: sap-concur-expense-expense-itemization
- name: ExpenseSummary
  property_count: 4
  slug: sap-concur-expense-expense-summary
- name: ExpenseTaxSummary
  property_count: 0
  slug: sap-concur-expense-expense-tax-summary
- name: ExpenseType
  property_count: 4
  slug: sap-concur-expense-expense-type
- name: FormField
  property_count: 8
  slug: sap-concur-expense-form-field
- name: Link
  property_count: 3
  slug: sap-concur-expense-link
- name: Location
  property_count: 5
  slug: sap-concur-expense-location
- name: Mileage
  property_count: 9
  slug: sap-concur-expense-mileage
- name: NewReport
  property_count: 10
  slug: sap-concur-expense-new-report
- name: PaymentType
  property_count: 3
  slug: sap-concur-expense-payment-type
- name: ReportApproveRequest
  property_count: 5
  slug: sap-concur-expense-report-approve-request
- name: ReportDetails
  property_count: 24
  slug: sap-concur-expense-report-details
- name: SAP Concur Expense Report Schema
  property_count: 0
  slug: sap-concur-expense-report
- name: ReportSendBackRequest
  property_count: 3
  slug: sap-concur-expense-report-send-back-request
- name: ReportToApprove
  property_count: 5
  slug: sap-concur-expense-report-to-approve
- name: ResourceCreatedResponse
  property_count: 1
  slug: sap-concur-expense-resource-created-response
- name: TravelAllowance
  property_count: 3
  slug: sap-concur-expense-travel-allowance
- name: Travel
  property_count: 8
  slug: sap-concur-expense-travel
- name: UpdateAllocationRequest
  property_count: 2
  slug: sap-concur-expense-update-allocation-request
- name: UpdateReport
  property_count: 9
  slug: sap-concur-expense-update-report
- name: UpdateSubmittedExpense
  property_count: 5
  slug: sap-concur-expense-update-submitted-expense
- name: UpdateSubmittedReport
  property_count: 5
  slug: sap-concur-expense-update-submitted-report
- name: Vendor
  property_count: 3
  slug: sap-concur-expense-vendor
- name: ExpenseDetail
  property_count: 25
  slug: sap-concur-expensedetail
- name: ExpenseItemization
  property_count: 7
  slug: sap-concur-expenseitemization
- name: ExpenseSummary
  property_count: 9
  slug: sap-concur-expensesummary
- name: ExpenseTaxSummary
  property_count: 8
  slug: sap-concur-expensetaxsummary
- name: ExpenseType
  property_count: 4
  slug: sap-concur-expensetype
- name: FormField
  property_count: 8
  slug: sap-concur-formfield
- name: Link
  property_count: 3
  slug: sap-concur-link
- name: Location
  property_count: 5
  slug: sap-concur-location
- name: Mileage
  property_count: 9
  slug: sap-concur-mileage
- name: NewReport
  property_count: 10
  slug: sap-concur-newreport
- name: PaymentType
  property_count: 3
  slug: sap-concur-paymenttype
- name: ReportApproveRequest
  property_count: 5
  slug: sap-concur-reportapproverequest
- name: ReportDetails
  property_count: 28
  slug: sap-concur-reportdetails
- name: ReportSendBackRequest
  property_count: 3
  slug: sap-concur-reportsendbackrequest
- name: ReportToApprove
  property_count: 6
  slug: sap-concur-reporttoapprove
- name: ResourceCreatedResponse
  property_count: 1
  slug: sap-concur-resourcecreatedresponse
- name: Travel
  property_count: 8
  slug: sap-concur-travel
- name: TravelAllowance
  property_count: 3
  slug: sap-concur-travelallowance
- name: UpdateAllocationRequest
  property_count: 2
  slug: sap-concur-updateallocationrequest
- name: UpdateReport
  property_count: 9
  slug: sap-concur-updatereport
- name: UpdateSubmittedExpense
  property_count: 5
  slug: sap-concur-updatesubmittedexpense
- name: UpdateSubmittedReport
  property_count: 5
  slug: sap-concur-updatesubmittedreport
- name: Vendor
  property_count: 3
  slug: sap-concur-vendor
json_structures:
- name: Sap Concur Expense Allocation Structure
  property_count: 8
  slug: sap-concur-expense-allocation-structure
- name: Sap Concur Expense Amount Structure
  property_count: 2
  slug: sap-concur-expense-amount-structure
- name: Sap Concur Expense Comment Request Structure
  property_count: 1
  slug: sap-concur-expense-comment-request-structure
- name: Sap Concur Expense Comment Structure
  property_count: 5
  slug: sap-concur-expense-comment-structure
- name: Sap Concur Expense Cost Object For Approver Structure
  property_count: 3
  slug: sap-concur-expense-cost-object-for-approver-structure
- name: Sap Concur Expense Custom Data Structure
  property_count: 3
  slug: sap-concur-expense-custom-data-structure
- name: Sap Concur Expense Error Response Structure
  property_count: 6
  slug: sap-concur-expense-error-response-structure
- name: Sap Concur Expense Exchange Rate Structure
  property_count: 2
  slug: sap-concur-expense-exchange-rate-structure
- name: Sap Concur Expense Expense Detail Structure
  property_count: 12
  slug: sap-concur-expense-expense-detail-structure
- name: Sap Concur Expense Expense Itemization Structure
  property_count: 5
  slug: sap-concur-expense-expense-itemization-structure
- name: Sap Concur Expense Expense Summary Structure
  property_count: 4
  slug: sap-concur-expense-expense-summary-structure
- name: Sap Concur Expense Expense Tax Summary Structure
  property_count: 0
  slug: sap-concur-expense-expense-tax-summary-structure
- name: Sap Concur Expense Expense Type Structure
  property_count: 4
  slug: sap-concur-expense-expense-type-structure
- name: Sap Concur Expense Form Field Structure
  property_count: 8
  slug: sap-concur-expense-form-field-structure
- name: Sap Concur Expense Link Structure
  property_count: 3
  slug: sap-concur-expense-link-structure
- name: Sap Concur Expense Location Structure
  property_count: 5
  slug: sap-concur-expense-location-structure
- name: Sap Concur Expense Mileage Structure
  property_count: 9
  slug: sap-concur-expense-mileage-structure
- name: Sap Concur Expense New Report Structure
  property_count: 10
  slug: sap-concur-expense-new-report-structure
- name: Sap Concur Expense Payment Type Structure
  property_count: 3
  slug: sap-concur-expense-payment-type-structure
- name: Sap Concur Expense Report Approve Request Structure
  property_count: 5
  slug: sap-concur-expense-report-approve-request-structure
- name: Sap Concur Expense Report Details Structure
  property_count: 24
  slug: sap-concur-expense-report-details-structure
- name: Sap Concur Expense Report Send Back Request Structure
  property_count: 3
  slug: sap-concur-expense-report-send-back-request-structure
- name: Sap Concur Expense Report To Approve Structure
  property_count: 5
  slug: sap-concur-expense-report-to-approve-structure
- name: Sap Concur Expense Resource Created Response Structure
  property_count: 1
  slug: sap-concur-expense-resource-created-response-structure
- name: Sap Concur Expense Travel Allowance Structure
  property_count: 3
  slug: sap-concur-expense-travel-allowance-structure
- name: Sap Concur Expense Travel Structure
  property_count: 8
  slug: sap-concur-expense-travel-structure
- name: Sap Concur Expense Update Allocation Request Structure
  property_count: 2
  slug: sap-concur-expense-update-allocation-request-structure
- name: Sap Concur Expense Update Report Structure
  property_count: 9
  slug: sap-concur-expense-update-report-structure
- name: Sap Concur Expense Update Submitted Expense Structure
  property_count: 5
  slug: sap-concur-expense-update-submitted-expense-structure
- name: Sap Concur Expense Update Submitted Report Structure
  property_count: 5
  slug: sap-concur-expense-update-submitted-report-structure
- name: Sap Concur Expense Vendor Structure
  property_count: 3
  slug: sap-concur-expense-vendor-structure
- name: Sap Concur Structure
  property_count: 0
  slug: sap-concur-structure
jsonld:
- class_count: 0
  name: Sap Concur Context
  property_count: 15
  slug: sap-concur-context
- class_count: 0
  name: Sap Concur Expense Context
  property_count: 0
  slug: sap-concur-expense-context
layout: provider
modified: '2026-05-19'
name: SAP Concur
nav: Providers
network: true
overview: 'SAP Concur publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Allocations API, Comments API, Expenses API, and 2 more. Tagged areas include Business Travel, Expense Management, Financial Services, Invoice Management, and Travel Management.


  The SAP Concur catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  SAP Concur''s developer surface includes authentication, support, engineering blog, signup flow, release notes, changelog, and 13 more developer resources.'
plans:
- name: Sap Concur Plans Pricing
  plan_count: 1
  slug: sap-concur-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 1
  name: Sap Concur Rate Limits
  slug: sap-concur-rate-limits
rules:
- name: SAP Concur API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: sap-concur-jsonschema-spectral-rules
- name: SAP Concur API Rules
  rule_count: 21
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 12
  slug: sap-concur-spectral-rules
score:
  band: strong
  composite: 56.7
  delta: -2.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 80.1
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-concur/refs/heads/main/screenshots/sap-concur-2026-06-20T193423.png
security:
- kind: authentication
  name: Sap Concur Authentication
  slug: sap-concur-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sap Concur Domain Security
  slug: sap-concur-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sap Concur Vulnerability Disclosure
  slug: sap-concur-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-concur
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
use_cases:
- description: Automate expense report creation, submission, and approval workflows by integrating with ERP and financial systems.
  name: Expense Report Automation
- description: Connect travel management companies and suppliers to provide booking, itinerary, and receipt data within Concur Travel.
  name: Travel Booking Integration
- description: Streamline accounts payable by automating invoice creation, purchase order matching, and vendor management.
  name: Invoice Processing
- description: Extract approved expense reports and invoices for automated posting into ERP systems like SAP, Oracle, and NetSuite.
  name: Financial Posting
- description: Submit and manage digital receipts from e-receipt partners and mobile capture for paperless expense management.
  name: Receipt Digitization
website: https://developer.concur.com/
---
