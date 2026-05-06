---
aid: workday-finance
specificationVersion: '0.19'
name: Workday Finance
description: APIs for Workday's cloud-based financial management system, enabling enterprise resource planning, accounting, financial analytics, procurement, grants management, inventory, and settlement services.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-finance/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
tags:
  - Accounting
  - Cloud
  - Enterprise
  - ERP
  - Finance
  - Financial Management
apis:
  - name: Workday Financial Management API
    description: Core SOAP API for financial management operations including general ledger, accounts payable, accounts receivable, financial reporting, tax, financial organizations, and worktag management. Exposes data relative to accounts, accounting, business plans, and related financial structures.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/overview.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Accounting
      - Banking
      - Finance
      - General Ledger
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v41.2/index.html
      - type: Reference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v41.2/Financial_Management.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v41.2/Financial_Management.wsdl
      - type: OpenAPI
        url: openapi/workday-finance-financial-management-openapi.yml
    contact:
      - FN: Workday API Support
        email: api-support@workday.com
        X-twitter: workday
  - name: Workday Revenue Management API
    description: SOAP API for managing revenue recognition, contracts, and billing processes. Supports revenue accounting workflows and contract analysis within Workday Financial Management.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/revenue-management.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Billing
      - Contracts
      - Revenue
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Revenue_Management/v41.2/index.html
      - type: Reference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Revenue_Management/v41.2/Revenue_Management.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Revenue_Management/v41.2/Revenue_Management.wsdl
  - name: Workday Expenses API
    description: SOAP API for expense management, including expense reports, approval workflows, and reimbursements. Part of Workday Spend Management for tracking and controlling employee and organizational expenses.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/spend-management/expenses.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Expenses
      - Reimbursement
      - Spend Management
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Expenses/v41.2/index.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Expenses/v41.2/Expenses.wsdl
  - name: Workday Cash Management API
    description: SOAP API for managing cash positions, bank transactions, and treasury operations. Supports cash flow forecasting, bank account management, and financial reconciliation processes.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/cash-management.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Banking
      - Cash Management
      - Treasury
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Cash_Management/v41.2/index.html
      - type: Reference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Cash_Management/v41.2/Cash_Management.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Cash_Management/v41.2/Cash_Management.wsdl
  - name: Workday Budgets API
    description: SOAP API for budget planning, tracking, and analysis. Enables programmatic management of budgets, budget amendments, and budget structure data within Workday Financial Management.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/budget-management.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Budgets
      - Financial Planning
      - Planning
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Budgets/v41.2/index.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Budgets/v41.2/Budgets.wsdl
  - name: Workday Projects API
    description: SOAP API for project management, tracking project costs, billing, and resource allocation. Supports project-based accounting, cost capture, and resource planning workflows.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/projects.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Cost Tracking
      - Project Management
      - Projects
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Projects/v41.2/index.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Projects/v41.2/Projects.wsdl
  - name: Workday Resource Management API
    description: SOAP API exposing Workday Financials Resource Management data, including suppliers, supplier accounts, procurement, purchase orders, invoicing, business assets, asset depreciation, and travel and entertainment operations. Supports the full procure-to-pay lifecycle and asset management workflows.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/spend-management/procure-to-pay.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Business Assets
      - Invoicing
      - Procurement
      - Resource Management
      - Suppliers
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Resource_Management/v45.2/index.html
      - type: Reference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Resource_Management/v45.2/Resource_Management.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Resource_Management/v45.2/Resource_Management.wsdl
      - type: OpenAPI
        url: openapi/workday-finance-procurement-openapi.yml
  - name: Workday Settlement Services API
    description: SOAP API for settlement management and payment services. Supports payment processing, bank routing, settlement runs, direct debit mandates, payment acknowledgements, cash balance checks, and escheatment management across supplier payments, employee reimbursements, and customer payments.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/accounting-finance.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Banking
      - Direct Debit
      - Payments
      - Settlements
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Settlement_Services/v45.2/index.html
      - type: Reference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Settlement_Services/v45.2/Settlement_Services.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Settlement_Services/v45.2/Settlement_Services.wsdl
  - name: Workday Inventory API
    description: SOAP API exposing Workday Financials Inventory data. Supports goods delivery, stock tracking, inventory adjustments, cycle counting, par management, directed picks, put-away operations, recalls, and replenishment across storage locations and distribution networks.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/spend-management/inventory.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Goods Delivery
      - Inventory
      - Stock Management
      - Supply Chain
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Inventory/v45.2/index.html
      - type: Reference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Inventory/v45.2/Inventory.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Inventory/v45.2/Inventory.wsdl
  - name: Workday Professional Services Automation API
    description: SOAP API for Professional Services Automation integrations. Exposes Workday Financials data for managing client-facing projects, services billing, resource staffing, and expense reporting within professional services organizations.
    image: https://www.workday.com/content/dam/web/images/logo/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/professional-services-automation/overview.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Professional Services
      - PSA
      - Resource Staffing
      - Services Billing
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Professional_Services_Automation/v45.2/index.html
      - type: Reference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Professional_Services_Automation/v45.2/Professional_Services_Automation.html
      - type: X-wsdl
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Professional_Services_Automation/v45.2/Professional_Services_Automation.wsdl
common:
  - type: Portal
    url: https://community.workday.com/api
  - type: Documentation
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: Getting Started
    url: https://doc.workday.com/r/Enterprise_Interface_API_Concepts_and_Resources/Getting_Started_with_Workday_Web_Services
  - type: Authentication
    url: https://doc.workday.com/r/Enterprise_Interface_API_Concepts_and_Resources/Authentication
  - type: Rate Limits
    url: https://doc.workday.com/r/Enterprise_Interface_API_Concepts_and_Resources/Rate_Limiting
  - type: Console
    url: https://developer.workday.com/about
  - type: Website
    url: https://www.workday.com/en-us/products/financial-management/overview.html
  - type: Sign Up
    url: https://resourcecenter.workday.com/
  - type: Blog
    url: https://blog.workday.com/
  - type: Support
    url: https://www.workday.com/en-us/services/support.html
  - type: Community
    url: https://www.workday.com/en-us/services/community.html
  - type: Status
    url: https://status.workday.com/
  - type: Terms of Service
    url: https://www.workday.com/en-us/legal.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: GitHub Organization
    url: https://github.com/Workday
  - type: Marketplace
    url: https://marketplace.workday.com/en-US/home
  - type: Change Log
    url: https://community.workday.com/articles/16827
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: Spectral Rules
    url: rules/workday-finance-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/financial-operations.yaml
  - type: JSON-LD
    url: json-ld/workday-finance-context.jsonld
  - type: JSONSchema
    url: json-schema/workday-finance-journal-entry-schema.json
  - type: JSONSchema
    url: json-schema/workday-finance-supplier-invoice-schema.json
  - type: JSONSchema
    url: json-schema/workday-finance-purchase-order-schema.json
  - type: Vocabulary
    url: vocabulary/workday-finance-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
