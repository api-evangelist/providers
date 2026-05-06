---
name: SAP Concur
description: SAP Concur is a leading provider of integrated travel, expense, and invoice management solutions. Their APIs enable developers to integrate Concur functionality into their applications, automate business processes, and access travel and expense data.
image: https://www.concur.com/themes/custom/concur/logo.svg
url: https://www.concur.com
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
tags:
  - Business Travel
  - Expense Management
  - Financial Services
  - Invoice Management
  - Travel Management
apis:
  - name: Concur Expense API
    description: Enables integration with Concur Expense for creating, retrieving, and managing expense reports, entries, and related data.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/expense/
    tags:
      - Expenses
      - Receipts
      - Reports
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/
      - type: OpenAPI
        url: https://developer.concur.com/api-reference/expense/expense-report/expense-report.json
      - type: OpenAPI
        url: openapi/sap-concur-expense-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-concur-expense-report-schema.json
      - type: JSONLD
        url: json-ld/sap-concur-context.jsonld
      - type: Authentication
        url: https://developer.concur.com/api-reference/authentication/getting-started.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/v4.reports.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/v4.allocations.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/v4.workflows.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/v4.comments.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/v4.expense-attendee-associations.html
      - type: Resources
        url: https://api.sap.com/package/ConcurExpense
        title: SAP Business Accelerator Hub
  - name: Concur Travel API
    description: Provides access to travel booking data, profiles, and itinerary information within Concur Travel.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/travel/
    tags:
      - Bookings
      - Itineraries
      - Travel
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/travel/
      - type: OpenAPI
        url: https://developer.concur.com/api-reference/travel/itinerary/itinerary.json
      - type: Authentication
        url: https://developer.concur.com/api-reference/authentication/getting-started.html
  - name: Concur Invoice API
    description: Allows integration with Concur Invoice for managing purchase requests, invoices, and payment requests.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/invoice/
    tags:
      - Invoices
      - Payments
      - Purchase Requests
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/invoice/
      - type: OpenAPI
        url: https://developer.concur.com/api-reference/invoice/v3.invoice.json
      - type: Authentication
        url: https://developer.concur.com/api-reference/authentication/getting-started.html
      - type: Resources
        url: https://api.sap.com/package/ConcurInvoice
        title: SAP Business Accelerator Hub
  - name: Concur Request API
    description: Enables management of travel requests and approvals within the Concur system.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/request/
    tags:
      - Approvals
      - Travel Requests
      - Workflows
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/request/
      - type: OpenAPI
        url: https://developer.concur.com/api-reference/request/v4.request.json
      - type: Authentication
        url: https://developer.concur.com/api-reference/authentication/getting-started.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/request/v4.get-started.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/request/v4.endpoints.cashadvance-resources.html
      - type: Resources
        url: https://api.sap.com/package/ConcurRequest
        title: SAP Business Accelerator Hub
  - name: Concur User Provisioning API
    description: Manages user accounts and profiles, including creating, updating, and retrieving user information. Supports provisioning across Identity, Spend, and Travel services with bulk operations for managing multiple user records.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/user/v1.0
    humanURL: https://developer.concur.com/api-reference/user/
    tags:
      - Identity Management
      - Provisioning
      - Users
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/user/
      - type: Documentation
        url: https://developer.concur.com/api-reference/user-provisioning/v4.user-provisioning.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/user-provisioning/spend/v4.spend-role-code-definition.html
  - name: Concur Receipt API
    description: Allows for the submission and management of digital receipts within Concur Expense.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/receipts/
    tags:
      - Documents
      - Images
      - Receipts
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/receipts/
      - type: Documentation
        url: https://developer.concur.com/api-reference/receipts/endpoints.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/receipts/sample-receipts.html
  - name: Concur Budget API
    description: Exposes budget and fiscal year data, enabling partners and clients to read and manage fiscal years, budget categories, budget items, budget tracking fields, and budget adjustments through API endpoints.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/budget/getting-started.html
    tags:
      - Budgets
      - Financial Planning
      - Fiscal Years
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/budget/getting-started.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/budget/v4.fiscal-year.html
  - name: Concur Cards API
    description: Provides an automated integration pathway for certified partner financial networks, issuing banks, and fin-tech partners to submit credit card account and transaction data to Concur Expense in near real time.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/cards/v4.cards-get-started.html
    tags:
      - Credit Cards
      - Financial Data
      - Transactions
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/cards/v4.cards-get-started.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/cards/v4.cards-endpoints.schemas.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/cards/v4.cards-endpoints.account.html
  - name: Concur Quick Expense API
    description: Enables the creation of expenses with minimal information such as date, amount, and expense type, with or without a receipt image. Supports attaching receipt files including PNG, PDF, TIFF, and JPEG formats up to 50 MB.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/expense/quick-expense/v4.quick-expense.html
    tags:
      - Expenses
      - Quick Entry
      - Receipts
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/quick-expense/v4.quick-expense.html
  - name: Concur Exchange Rate API
    description: Allows users to create custom exchange rates for a company, supporting bulk uploads of exchange rate data for specified currency pairs and effective dates with a maximum of 100 rates per request.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/expense/exchange-rate/v4.exchange-rate.html
    tags:
      - Currency
      - Exchange Rates
      - Financial Data
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/exchange-rate/v4.exchange-rate.html
  - name: Concur Financial Integration API
    description: Allows an external system to interact with financial documents generated from SAP Concur for financial posting into an ERP, providing an automated solution to request approved expense reports, cash advances, and invoices for import into client internal systems.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/financial-integration/v4.financial-integration.html
    tags:
      - ERP
      - Financial Integration
      - Posting
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/financial-integration/v4.financial-integration.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/financial-integration/v4.financial-integration-use-cases-extract-information.html
  - name: Concur Identity API
    description: Creates, updates, and reads user core identity profiles following the SCIM 2.0 standard. Enables looking up SAP Concur UUIDs for accessing other v4 APIs for individual users.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/profile/v4.identity.html
    tags:
      - Identity
      - SCIM
      - User Profiles
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/profile/v4.identity.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/profile/v1.getting-started.html
  - name: Concur Event Subscription Service API
    description: Implements the Publish/Subscribe pattern using principles of Event Driven Architecture, notifying clients and partners when specific business events occur such as expense report status changes and travel request updates.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/ess/v4.event-subscription.html
    tags:
      - Events
      - Subscriptions
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/ess/v4.event-subscription.html
  - name: Concur Callouts API
    description: Allows clients to add interactions with outside systems to their users SAP Concur experience through application connectors, supporting attendee data fetch, list item fetch, event notifications, and external URL launches.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v1.0
    humanURL: https://developer.concur.com/api-reference/callouts/callouts-application-connectors.html
    tags:
      - Callouts
      - Connectors
      - Integrations
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/callouts/callouts-application-connectors.html
  - name: Concur Direct Connect Hotel Service API
    description: Provides a method for custom hotel source suppliers to provide hotel inventory, rates, and booking related functionality to SAP Concur Online Booking Tool, supporting search, rate retrieval, reservation management, and cancellation handling.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/direct-connects/hotel-service-4/v4.getting-started.html
    tags:
      - Booking
      - Direct Connect
      - Hotels
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/direct-connects/hotel-service-4/v4.getting-started.html
  - name: Concur Direct Connect Ground Transportation API
    description: Enables travel users to access ground transportation inventory from service providers, supporting search, reservation, cancellation, and update operations for ground transportation bookings.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v1.0
    humanURL: https://developer.concur.com/api-reference/direct-connects/ground-transportation.html
    tags:
      - Booking
      - Direct Connect
      - Ground Transportation
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/direct-connects/ground-transportation.html
  - name: Concur Spend Documents API
    description: Facilitates ingestion and retrieval of receipt documents for use within Concur Expense, enabling users to create and retrieve simple receipts by uploading documents with associated metadata.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/spend-documents/v4.spend-documents.html
    tags:
      - Documents
      - Receipts
      - Spend Management
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/spend-documents/v4.spend-documents.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/spend-documents/get-receipt.html
  - name: Concur List Item API
    description: Provides an automated solution for retrieving, adding, updating, and deleting list items within SAP Concur, supporting hierarchical list structures with parent-child relationships across multiple levels.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/common/list-item/v4.list-item.html
    tags:
      - Configuration
      - List Items
      - Lists
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/common/list-item/v4.list-item.html
  - name: Concur Lists API
    description: Enables viewing configured lists within SAP Concur products and creating new lists, supporting shared lists across Expense, Invoice, and Request applications with managed list capabilities for partner applications.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/common/lists/v4.list.html
    tags:
      - Configuration
      - Lists
      - Shared Resources
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/common/lists/v4.list.html
  - name: Concur Travel Profile API
    description: Enables retrieval of travel profile information for specified users and lists of travel profile summaries, available to developers, travel suppliers, and travel management companies.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v2.0
    humanURL: https://developer.concur.com/api-reference/travel-profile/v2.profile-service.html
    tags:
      - Loyalty Programs
      - Travel Profiles
      - User Profiles
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/travel-profile/v2.profile-service.html
  - name: Concur Travel Allowance API
    description: Allows extraction of travel allowance information from the SAP Concur platform, providing the ability to read travel allowance itinerary data, calculation results, and configuration settings.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/travelallowance/v4.travelallowance-get-started.html
    tags:
      - Expenses
      - Per Diem
      - Travel Allowance
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/travelallowance/v4.travelallowance-get-started.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/travelallowance/v4.travel-allowance-days-endpoints.html
  - name: Concur Cash Advance API
    description: Enables users to create, view, and issue cash advances within Concur Expense. Supports single cash advance creation, retrieval, and issuance operations for both Professional and Standard editions. Requires the Identity v4 API to obtain user IDs.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/cash-advance/v4-1.cash-advance.html
    tags:
      - Cash Advances
      - Expenses
      - Reimbursements
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/cash-advance/v4-1.cash-advance.html
  - name: Concur Purchase Order API
    description: Gives SAP Concur clients the ability to leverage external data to create and update approved purchase orders. Enables direct connections to manage purchase orders and resolve matching exceptions on invoices through create, update, and retrieve operations.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/invoice/v3.purchase-order.html
    tags:
      - Invoices
      - Procurement
      - Purchase Orders
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/invoice/v3.purchase-order.html
  - name: Concur Purchase Request API
    description: Enables SAP Concur clients to leverage external data to create purchase requests for pre-authorization of purchase orders. Organizations can establish direct connections to automatically generate and submit purchase requests into approval workflows, with approved requests resulting in purchase orders for vendor transmission.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/invoice/v4.purchase-request-get-started.html
    tags:
      - Approvals
      - Procurement
      - Purchase Requests
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/invoice/v4.purchase-request-get-started.html
      - type: Documentation
        url: https://developer.concur.com/api-reference/invoice/v4.purchase-request-endpoints.html
  - name: Concur Vendor API
    description: Provides processes for managing vendor collections used in invoicing, including adding new vendors, updating, retrieving, and deleting information for existing vendors. Supports vendor banking information, grouping, and extensive search filtering with up to 20 custom fields.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/invoice/v3.vendor.html
    tags:
      - Invoices
      - Supplier Management
      - Vendors
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/invoice/v3.vendor.html
  - name: Concur Sales Tax Validation API
    description: Enables retrieval and updating of invoices for tax calculation purposes, allowing external tax systems to fetch invoices requiring tax assessment and submit calculated tax amounts and rates back to Concur. Handles comprehensive invoice data including vendor information, billing and shipping addresses, and line items.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/invoice/v3.sales-tax-validation.html
    tags:
      - Invoices
      - Tax Compliance
      - Tax Validation
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/invoice/v3.sales-tax-validation.html
  - name: Concur Document Compliance Gateway API
    description: Manages transmission of compliance documents between SAP Concur and validating vendors, enabling vendors to exchange compliance documents, validate them against relevant authoritative or regulatory sources, and return the validation results. Streamlines compliance document validation and tax data extraction for expense creation.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v4.0
    humanURL: https://developer.concur.com/api-reference/document-compliance-gateway/V4.document-compliance-gateway.html
    tags:
      - Compliance
      - Document Validation
      - Tax Documents
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/document-compliance-gateway/V4.document-compliance-gateway.html
  - name: Concur Image API
    description: Enables clients to manage receipt images attached to expense reports and images associated with invoices. Users can retrieve existing images by report ID, image ID, or invoice ID, and upload new images in PDF, JPEG, JPG, and PNG formats up to 10 MB to users, expense entries, reports, or invoices.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/image/v1.0
    humanURL: https://developer.concur.com/api-reference/image/v1.image.html
    tags:
      - Documents
      - Images
      - Receipts
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/image/v1.image.html
  - name: Concur Travel Receipts API
    description: Exposes receipt requests to inform E-Receipt partners which E-Receipts to send to SAP Concur and for which user. Partners receive paginated responses and can filter results using optional timestamps, with support for separate US and EMEA datacenter endpoints.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://us.api.concursolutions.com/travelreceipts/v1
    humanURL: https://developer.concur.com/api-reference/travel-receipts/getting-started.html
    tags:
      - E-Receipts
      - Travel
      - Travel Receipts
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/travel-receipts/getting-started.html
  - name: Concur Locations API
    description: Retrieves details about locations used by Concur that are valid at a user's company. Supports filtering by name, city, country, and other geographic parameters, and returns location data including IATA codes, geographic coordinates, airport status, and booking tool availability.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/common/locations/v3.locations.html
    tags:
      - Common Resources
      - Geography
      - Locations
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/common/locations/v3.locations.html
  - name: Concur Expense Attendee Types API
    description: Provides access to the configured attendee types within SAP Concur, allowing retrieval and management of attendee type resources used for categorizing attendees in expense reports.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    baseURL: https://www.concursolutions.com/api/v3.0
    humanURL: https://developer.concur.com/api-reference/expense/attendee-types/v3.attendee-types.html
    tags:
      - Attendees
      - Configuration
      - Expenses
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/attendee-types/v3.attendee-types.html
common:
  - type: DeveloperPortal
    url: https://developer.concur.com/
  - type: Authentication
    url: https://developer.concur.com/api-reference/authentication/getting-started.html
  - type: Authentication
    url: https://developer.concur.com/api-reference/authentication/company-auth.html
  - type: Support
    url: https://developer.concur.com/support/
  - type: TermsOfService
    url: https://www.concur.com/terms-of-use
  - type: PrivacyPolicy
    url: https://www.concur.com/privacy-policy
  - type: StatusPage
    url: https://open.concur.com/
  - type: Blog
    url: https://www.concur.com/newsroom
  - type: SignUp
    url: https://developer.concur.com/register
  - type: GitHubRepository
    url: https://github.com/SAP-docs/preview.developer.concur.com
  - type: ReleaseNotes
    url: https://developer.concur.com/tools-support/release-notes/
  - type: ChangeLog
    url: https://developer.concur.com/tools-support/release-notes/
  - type: Resources
    url: https://api.sap.com/products/SAPConcur/apis/REST
    title: SAP Business Accelerator Hub
  - type: Tutorials
    url: https://developers.sap.com/tutorials/data-to-value-conn-concur-part01..html
  - type: Features
    data:
      - name: OAuth 2.0 Authentication
        description: Secure token-based authentication supporting both company-level and user-level access tokens with automatic refresh.
      - name: Multi-Datacenter Support
        description: Separate API endpoints for US, US2, EMEA, and China datacenters ensuring data residency compliance.
      - name: Event Subscription Service
        description: Publish/Subscribe event-driven architecture for real-time notifications on business events like report submissions.
      - name: SCIM 2.0 User Provisioning
        description: Standards-based user identity management following SCIM protocol for automated user lifecycle operations.
      - name: Direct Connect Framework
        description: Integration framework allowing travel suppliers to provide inventory directly to the Concur booking tool.
      - name: Multi-Currency Exchange Rates
        description: Custom exchange rate management supporting bulk uploads for currency conversion across global operations.
  - type: UseCases
    data:
      - name: Expense Report Automation
        description: Automate expense report creation, submission, and approval workflows by integrating with ERP and financial systems.
      - name: Travel Booking Integration
        description: Connect travel management companies and suppliers to provide booking, itinerary, and receipt data within Concur Travel.
      - name: Invoice Processing
        description: Streamline accounts payable by automating invoice creation, purchase order matching, and vendor management.
      - name: Financial Posting
        description: Extract approved expense reports and invoices for automated posting into ERP systems like SAP, Oracle, and NetSuite.
      - name: Receipt Digitization
        description: Submit and manage digital receipts from e-receipt partners and mobile capture for paperless expense management.
  - type: Integrations
    data:
      - name: SAP ERP
        description: Native integration with SAP S/4HANA and SAP ERP for financial posting, cost center sync, and master data management.
      - name: Microsoft Teams
        description: Approve expense reports and travel requests directly from Microsoft Teams notifications.
      - name: Uber for Business
        description: Automatic e-receipt submission for Uber business rides directly into Concur Expense.
      - name: Salesforce
        description: Sync customer and opportunity data to pre-populate expense reports and travel requests.
      - name: Oracle NetSuite
        description: Automated financial posting of approved expense reports and invoices into Oracle NetSuite.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://developer.concur.com/
---
