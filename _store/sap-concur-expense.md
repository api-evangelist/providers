---
aid: sap-concur-expense
url: https://raw.githubusercontent.com/api-evangelist/sap-concur-expense/refs/heads/main/apis.yml
apis:
- name: Expense Report API
  description: Allows developers to read and write expense report headers, entries, allocations, and manage the expense report lifecycle.
  image: https://www.concur.com/themes/custom/concur/logo.svg
  humanURL: https://developer.concur.com/api-reference/expense/
  baseURL: https://us.api.concursolutions.com/api/expense
  tags:
  - Expenses
  - Financial
  - Reports
  properties:
  - type: Documentation
    url: https://developer.concur.com/api-reference/expense/expense-report/
  - type: OpenAPI
    url: https://developer.concur.com/api-reference/expense/expense-report/v3.reports.html
  - type: Authentication
    url: https://developer.concur.com/api-reference/authentication/getting-started.html
- name: Quick Expense API
  description: Create and manage basic expenses quickly without creating a full expense report.
  image: https://www.concur.com/themes/custom/concur/logo.svg
  humanURL: https://developer.concur.com/api-reference/expense/quick-expense/
  baseURL: https://us.api.concursolutions.com/api/v3.0/expense/quickexpenses
  tags:
  - Expenses
  - Quick Expense
  properties:
  - type: Documentation
    url: https://developer.concur.com/api-reference/expense/quick-expense/v3.quick-expense.html
  - type: OpenAPI
    url: https://developer.concur.com/api-reference/expense/quick-expense/v3.quick-expense.html
- name: Expense Entry API
  description: Manage individual expense entries within expense reports including itemizations and custom fields.
  image: https://www.concur.com/themes/custom/concur/logo.svg
  humanURL: https://developer.concur.com/api-reference/expense/expense-report/expense-entry.html
  baseURL: https://us.api.concursolutions.com/api/v3.0/expense/entries
  tags:
  - Expense Entries
  - Line Items
  properties:
  - type: Documentation
    url: https://developer.concur.com/api-reference/expense/expense-report/expense-entry.html
- name: Digital Tax Invoice API
  description: Retrieve digital tax invoice data associated with expense entries for compliance and auditing.
  image: https://www.concur.com/themes/custom/concur/logo.svg
  humanURL: https://developer.concur.com/api-reference/expense/digital-tax-invoices/
  baseURL: https://us.api.concursolutions.com/api/v3.0/expense/digitaltaxinvoices
  tags:
  - Compliance
  - Invoice
  - Tax
  properties:
  - type: Documentation
    url: https://developer.concur.com/api-reference/expense/digital-tax-invoices/digital-tax-invoice.html
- name: Receipt Image API
  description: Upload, retrieve, and manage receipt images associated with expense entries.
  image: https://www.concur.com/themes/custom/concur/logo.svg
  humanURL: https://developer.concur.com/api-reference/image/
  baseURL: https://us.api.concursolutions.com/api/v3.0/expense/receiptimages
  tags:
  - Documents
  - Images
  - Receipts
  properties:
  - type: Documentation
    url: https://developer.concur.com/api-reference/image/v1.image.html
- name: Expense Group Configuration API
  description: Retrieve expense group configurations including expense types, policies, and workflow settings.
  image: https://www.concur.com/themes/custom/concur/logo.svg
  humanURL: https://developer.concur.com/api-reference/expense/expense-report/expense-group-configurations.html
  baseURL: https://us.api.concursolutions.com/api/v3.0/expense/expensegroupconfigurations
  tags:
  - Configuration
  - Policies
  - Settings
  properties:
  - type: Documentation
    url: https://developer.concur.com/api-reference/expense/expense-report/expense-group-configurations.html
- name: Expense Allocations API
  description: Manage allocation of expenses across multiple cost centers, projects, or departments.
  image: https://www.concur.com/themes/custom/concur/logo.svg
  humanURL: https://developer.concur.com/api-reference/expense/expense-report/expense-allocations.html
  baseURL: https://us.api.concursolutions.com/api/v3.0/expense/allocations
  tags:
  - Accounting
  - Allocations
  - Cost Centers
  properties:
  - type: Documentation
    url: https://developer.concur.com/api-reference/expense/expense-report/expense-allocations.html
- name: Payment Batch API
  description: Retrieve payment batches for processed expense reports ready for reimbursement.
  image: https://www.concur.com/themes/custom/concur/logo.svg
  humanURL: https://developer.concur.com/api-reference/expense/payment-batch/
  baseURL: https://us.api.concursolutions.com/api/v1.1/expense/paymentbatch
  tags:
  - Batch Processing
  - Payments
  - Reimbursement
  properties:
  - type: Documentation
    url: https://developer.concur.com/api-reference/expense/payment-batch/v1.payment-batches.html
name: SAP Concur Expense
tags:
- Expense Management
- Financial Management
- Receipts
- Reimbursement
- Reporting
- Travel
type: Contract
image: https://www.concur.com/themes/custom/concur/logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SAP Concur Expense is a travel and expense management solution that automates and streamlines expense reporting, approval workflows, and reimbursement processes for businesses.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

