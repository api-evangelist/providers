---
aid: coupa
url: https://raw.githubusercontent.com/api-evangelist/coupa/refs/heads/main/apis.yml
apis:
- name: Coupa Core API
  description: The primary RESTful API for accessing and managing core Coupa resources including suppliers, purchase orders, invoices, and requisitions.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/core-platform
  baseURL: https://instance.coupahost.com/api
  tags:
  - Invoices
  - Procurement
  - Purchase Orders
  - Requisitions
  - REST
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-api
  - type: OpenAPI
    url: https://compass.coupa.com/en-us/api_docs
  - type: Authentication
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-api/authentication
  - type: GettingStarted
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api
  - type: Errors
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/exception-handling-and-error-codes
  - type: APIReturnFormats
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/api-return-formats
  - type: XMLvsJSON
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/differences-between-xml-and-json-in-coupa
  - type: SampleRequests
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/sample-requestsresponses-xml-vs-json
  - type: SpecialActions
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/special-actions-and-api-notes
  - type: OpenAPISpec
    url: openapi/coupa-core-api-openapi.yml
  - type: JSONSchema
    url: json-schema/coupa-purchase-order-schema.json
  - type: JSONSchema
    url: json-schema/coupa-invoice-schema.json
  - type: JSONLD
    url: json-ld/coupa-context.jsonld
  contact:
  - type: Support
    url: https://compass.coupa.com/en-us/support
- name: Coupa Integration API
  description: API designed for enterprise integrations with ERP systems and other third-party applications.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/core-platform/integration
  baseURL: https://instance.coupahost.com/api
  tags:
  - Enterprise
  - ERP
  - Integration
  - Webhooks
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation
  - type: Webhooks
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/webhooks
  - type: Best Practices
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/integration-best-practices
  - type: IntegrationGuide
    url: https://compass.coupa.com/en-us/products/total-spend-management-platform/integration-playbooks-and-resources/other-integration-playbooks/erp-integration-adapters/build-your-integration
  - type: RESTAPIIntegration
    url: https://compass.coupa.com/en-us/products/total-spend-management-platform/integration-playbooks-and-resources/other-integration-playbooks/erp-integration-adapters/build-your-integration/integration-methods/coupa-rest-api-integration
- name: Coupa Supplier API
  description: API for supplier-specific operations including supplier information management, catalogs, and supplier collaboration.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/supplier-portal
  baseURL: https://instance.coupahost.com/api/suppliers
  tags:
  - Catalogs
  - Suppliers
  - Vendor Management
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/supplier-api
  - type: Getting Started
    url: https://compass.coupa.com/en-us/products/supplier-portal/getting-started
  - type: PunchoutDocumentation
    url: https://compass.coupa.com/en-us/products/product-documentation/supplier-resources/for-suppliers/integration-resources/purchase-orders-and-punchouts
  - type: cXMLDocumentation
    url: https://compass.coupa.com/en-us/products/product-documentation/suppliers/supplier-integration-resources/cxml-supplier-enablement
  - type: SuppliersReferenceAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)
- name: Coupa Analytics API
  description: API for accessing Coupa's analytics and reporting data for business intelligence and custom reporting needs.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/analytics
  baseURL: https://instance.coupahost.com/api/analytics
  tags:
  - Analytics
  - Business Intelligence
  - Data Export
  - Reporting
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/analytics-reporting
  - type: Data Dictionary
    url: https://compass.coupa.com/en-us/products/product-documentation/analytics-reporting/data-dictionary
- name: Coupa CCW API
  description: The Coupa Contingent Workforce (CCW) REST API enables customers and partners to build applications and integrate with CCW for managing contingent workforce operations including candidate lookup, worker management, and requisition handling.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api
  baseURL: https://instance.coupahost.com/api
  tags:
  - Candidates
  - Contingent Workforce
  - REST
  - Staffing
  - Workers
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api
  - type: Overview
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api/ccw-api-overview
  - type: APIExplorer
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api/api-explorer
  - type: Authentication
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api/managing-your-api-consumer-apps-and-credentials
- name: Coupa CSO API
  description: The Coupa Sourcing Optimization (CSO) API is a RESTful web service for importing and exporting fact sheet data, enabling integration between CSO and third-party systems for sourcing optimization workflows including markets, companies, users, and events.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api
  baseURL: https://instance.cso.coupahost.com/api
  tags:
  - Fact Sheets
  - Markets
  - Optimization
  - REST
  - Sourcing
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api
  - type: GettingStarted
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/get-started-with-cso-openapi
  - type: UserAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/user-api
  - type: CompanyAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/company-api
  - type: MarketAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/market-api
  - type: EventsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/events-api
- name: Coupa Treasury API
  description: REST API for retrieving and updating Coupa Treasury Management data such as cash flows and account balances. Treasury APIs follow the Coupa Core API structure but support JSON only.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-apis
  baseURL: https://instance.ctm.coupahost.com/v1
  tags:
  - Account Balances
  - Cash Management
  - Payments
  - REST
  - Treasury
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-apis
  - type: APIDocumentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-apis/view-treasury-api-documentation
  - type: Authentication
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc
- name: Coupa Open Buy API
  description: The Open Buy API provides a faster, standard, and secure interface for searching and purchasing items in real-time. It follows common eCommerce API patterns and supports authentication, search, detail, and checkout operations for all suppliers.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/supplier-resources/for-suppliers/integration-resources/open-buy-api-reference
  baseURL: https://instance.coupahost.com
  tags:
  - Catalog
  - eCommerce
  - Open Buy
  - REST
  - Search
  - Suppliers
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/supplier-resources/for-suppliers/integration-resources/open-buy-api-reference
  - type: SupplierIntegrationResources
    url: https://compass.coupa.com/en-us/products/product-documentation/supplier-resources/for-suppliers/integration-resources
  - type: Support
    url: mailto:openbuy-support@coupa.com
- name: Coupa Payments API
  description: API for managing Coupa Pay invoice payments and expense payments, including retrieval, export tracking, and payment status management. Accessed through the Coupa Pay payments endpoint.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payments-api-(coupa_paypayments-)
  baseURL: https://instance.coupahost.com/api/coupa_pay/payments
  tags:
  - Coupa Pay
  - Expense Payments
  - Invoice Payments
  - Payments
  - REST
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payments-api-(coupa_paypayments-)
  - type: SharedPaymentsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/payments-api
- name: Coupa Procurement API
  description: The Coupa Procurement API provides RESTful endpoints for managing the full procure-to-order lifecycle including requisitions, purchase orders, contracts, and sourcing (quote requests). It enables programmatic creation, querying, and updating of procurement transactions within the Coupa platform.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources
  baseURL: https://instance.coupahost.com/api
  tags:
  - Contracts
  - Procurement
  - Purchase Orders
  - Requisitions
  - REST
  - Sourcing
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources
  - type: RequisitionsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)
  - type: PurchaseOrdersAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)
  - type: ContractsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)
  - type: SourcingAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)
  - type: ApprovalsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)
- name: Coupa Invoicing API
  description: The Coupa Invoicing API provides RESTful endpoints for creating, updating, and querying invoices associated with purchase orders. It supports the full invoice lifecycle including invoice lines, charge allocations, and integration with invoicing platform workflows.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)
  baseURL: https://instance.coupahost.com/api/invoices
  tags:
  - Accounts Payable
  - Charge Allocations
  - Invoices
  - Invoicing
  - REST
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)
  - type: ExampleCalls
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoices-api-example-calls
  - type: InvoiceChargeAllocationAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-charge-allocation-api
  - type: InvoicingPlatformIntegration
    url: https://compass.coupa.com/en-us/products/total-spend-management-platform/integration-playbooks-and-resources/other-integration-playbooks/invoicing-platform-integration/build-your-integration/using-the-api
- name: Coupa Expenses API
  description: The Coupa Expenses API provides RESTful endpoints for managing expense reports, expense lines, expense categories, and related data. It supports creation, querying, and updating of expense transactions including itemized lines, per diem calculations, and tax details.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)
  baseURL: https://instance.coupahost.com/api/expense_reports
  tags:
  - Expense Lines
  - Expense Reports
  - Expenses
  - Per Diem
  - REST
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)
  - type: ExpenseReportsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-reports-api
  - type: ExpenseLinesAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api
  - type: ExampleCalls
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-api-example-calls
- name: Coupa Inventory and Receipts API
  description: The Coupa Inventory and Receipts API provides RESTful endpoints for managing receiving transactions, inventory adjustments, inventory consumptions, pick lists, fulfillment reservations, warehouse operations, and advance ship notices (ASN). It supports the full goods receipt and inventory management lifecycle.
  image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
  humanURL: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api
  baseURL: https://instance.coupahost.com/api
  tags:
  - Advance Ship Notices
  - Fulfillment
  - Inventory
  - Receipts
  - REST
  - Warehouse
  properties:
  - type: Documentation
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api
  - type: ReceivingTransactionsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/receiving-transactions-api-(receiving_transactions)
  - type: InventoryAdjustmentsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/inventory-adjustments-api-(inventory_adjustments)
  - type: InventoryConsumptionsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/inventory-consumptions-api-(inventory_consumptions)
  - type: PickListsAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)
  - type: WarehouseAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-api
  - type: AdvanceShipNoticesAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/advance-ship-notices-api-(asn)
  - type: InventoryBalanceAPI
    url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/inventory-balance-api
name: Coupa
tags:
- BSM
- Business Spend Management
- Cloud Platform
- Enterprise
- Financial Management
- Invoicing
- Procurement
- Supply Chain
type: Contract
image: https://www.coupa.com/wp-content/themes/coupa/images/coupa-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Coupa is a leading Business Spend Management (BSM) platform that provides cloud-based solutions for procurement, invoicing, expenses, payments, sourcing, contracts, and supply chain design & planning.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

