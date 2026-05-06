---
aid: concur
name: SAP Concur
description: SAP Concur provides a comprehensive suite of REST APIs for travel, expense, and invoice management. The Concur API platform enables integration with expense reporting, travel booking, invoice processing, receipt capture, and user management services used by enterprises worldwide for spend management automation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Expense Management
  - Finance
  - Invoice
  - SAP
  - Travel
apis:
  - aid: concur:expense-api
    name: SAP Concur Expense API
    description: REST API for managing expense reports, entries, allocations, and attendees. Supports creating, updating, and submitting expense reports with receipt images, policy validation, and approval workflows.
    humanURL: https://developer.concur.com/api-reference/expense/expense-report/v4.expenses.html
    baseURL: https://us.api.concursolutions.com/expensereports/v4/
    tags:
      - Expense Reports
      - Expense Tracking
      - REST
      - Spend Management
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/v4.expenses.html
      - type: APIReference
        url: https://developer.concur.com/api-reference/expense/expense-report/v4.expenses.html
      - type: GettingStarted
        url: https://developer.concur.com/api-reference/expense/expense-report/v4.expenses-get-started.html
  - aid: concur:travel-api
    name: SAP Concur Travel API
    description: REST API for managing travel itineraries, bookings, and travel profiles. Supports searching for travel options, creating bookings, and managing travel policies and preferences.
    humanURL: https://developer.concur.com/api-reference/travel/
    baseURL: https://us.api.concursolutions.com/travel/
    tags:
      - Bookings
      - Itineraries
      - REST
      - Travel
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/travel/
  - aid: concur:invoice-api
    name: SAP Concur Invoice API
    description: REST API for accounts payable invoice processing including purchase requests, vendor management, payment batches, and invoice approval workflows.
    humanURL: https://developer.concur.com/api-reference/invoice/v3.invoice.html
    baseURL: https://us.api.concursolutions.com/invoice/
    tags:
      - Accounts Payable
      - Invoices
      - Payments
      - REST
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/invoice/v3.invoice.html
  - aid: concur:receipts-api
    name: SAP Concur Receipts API
    description: REST API for submitting and managing digital receipts from e-commerce providers, ground transportation, hotels, and other merchants directly to Concur expense.
    humanURL: https://developer.concur.com/api-reference/receipts/
    baseURL: https://us.api.concursolutions.com/receipts/v4/
    tags:
      - Digital Receipts
      - E-Receipts
      - REST
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/receipts/
  - aid: concur:request-api
    name: SAP Concur Request API
    description: REST API for managing pre-trip travel requests and approvals, enabling employees to submit travel requests for authorization before booking.
    humanURL: https://developer.concur.com/api-reference/request/v4.get-started.html
    baseURL: https://us.api.concursolutions.com/travelrequest/v4/
    tags:
      - Approvals
      - REST
      - Travel Requests
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/request/v4.get-started.html
  - aid: concur:user-provisioning-api
    name: SAP Concur User Provisioning API
    description: SCIM 2.0-compliant API for provisioning and managing Concur user accounts, roles, and profile information with support for bulk operations.
    humanURL: https://developer.concur.com/api-reference/user-provisioning/v4.user-provisioning.html
    baseURL: https://us.api.concursolutions.com/provisioning/v4/
    tags:
      - Provisioning
      - REST
      - SCIM
      - Users
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/user-provisioning/v4.user-provisioning.html
  - aid: concur:events-api
    name: SAP Concur Events API
    description: Event subscription API enabling applications to receive real-time notifications when events occur in Concur such as expense report submissions, approvals, and status changes.
    humanURL: https://developer.concur.com/api-reference/ess/v4.event-subscription.html
    baseURL: https://us.api.concursolutions.com/events/v4/
    tags:
      - Events
      - REST
      - Subscriptions
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/ess/v4.event-subscription.html
  - aid: concur:lists-api
    name: SAP Concur Lists API
    description: REST API for managing custom lists and list items used in expense forms, travel policies, and invoice configurations for dropdown and lookup fields.
    humanURL: https://developer.concur.com/api-reference/common/lists/v4.list.html
    baseURL: https://us.api.concursolutions.com/list/v4/
    tags:
      - Configuration
      - Lists
      - REST
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/common/lists/v4.list.html
common:
  - type: Portal
    url: https://developer.concur.com/
  - type: Documentation
    url: https://developer.concur.com/api-reference/
  - type: GettingStarted
    url: https://developer.concur.com/api-reference/getting-started.html
  - type: Authentication
    url: https://developer.concur.com/api-reference/authentication/apidoc.html
  - type: Blog
    url: https://www.concur.com/blog
  - type: GitHubOrganization
    url: https://github.com/SAP/concur-platform
  - type: Support
    url: https://developer.concur.com/tools-support/support.html
  - type: TermsOfService
    url: https://www.concur.com/en-us/terms-of-use
  - type: PrivacyPolicy
    url: https://www.concur.com/en-us/privacy-policy
  - type: Sandbox
    url: https://developer.concur.com/manage-apps/register.html
  - type: ChangeLog
    url: https://developer.concur.com/tools-support/release-notes/
  - type: Pricing
    url: https://www.concur.com/en-us/pricing
  - type: Features
    data:
      - name: Expense Report Management
        description: Create, submit, and manage expense reports with policy validation and multi-level approval workflows.
      - name: Receipt Digitization
        description: Capture and process digital receipts from merchants for automatic expense matching.
      - name: Travel Booking Integration
        description: Search and book travel through API-connected travel management companies and booking tools.
      - name: Invoice Processing
        description: Automate accounts payable workflows with purchase requests, vendor management, and payment processing.
      - name: Event Notifications
        description: Real-time event subscriptions for expense, travel, and invoice status changes.
      - name: SCIM User Provisioning
        description: Standards-based user provisioning and management with SCIM 2.0 protocol support.
  - type: UseCases
    data:
      - name: ERP Integration
        description: Integrate Concur expense and invoice data with ERP systems for automated financial posting.
      - name: Travel Management
        description: Build travel booking integrations connecting corporate travel policies with booking engines.
      - name: Receipt Automation
        description: Automatically capture and match digital receipts from e-commerce and travel merchants.
      - name: Spend Analytics
        description: Extract expense and travel data for spend analytics, compliance reporting, and budget tracking.
      - name: Employee Onboarding
        description: Automate Concur user provisioning as part of employee onboarding workflows.
  - type: Integrations
    data:
      - name: SAP S/4HANA
        description: Financial posting integration for automated expense and invoice data transfer to SAP ERP.
      - name: SAP SuccessFactors
        description: HR integration for employee data synchronization and travel policy assignment.
      - name: Uber for Business
        description: Automated ride receipt submission from Uber business accounts to Concur expense.
      - name: Lyft
        description: Ground transportation receipt integration for business ride expense automation.
      - name: Microsoft Teams
        description: Approval and notification integration for expense workflows within Teams.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
