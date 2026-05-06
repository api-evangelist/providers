---
name: SAP S/4HANA
description: Collection of SAP S/4HANA Cloud and On-Premise APIs for enterprise resource planning.
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.18'
url: https://api.sap.com/apis.json
apis:
  - name: SAP S/4HANA Business Partner API
    description: API for creating, reading, updating, and deleting business partner master data.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_BUSINESS_PARTNER/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_BUSINESS_PARTNER
    tags:
      - Business Partner
      - Customer
      - ERP
      - Master Data
      - Supplier
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_BUSINESS_PARTNER/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/873c58e32fa642eea4ffb53d80819fa3.html
      - type: Console
        url: https://api.sap.com/api/API_BUSINESS_PARTNER/tryout
      - type: Authentication
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/26f2b5aa3f3a4019b7d08978095b9e6a.html
      - type: APIReference
        url: https://api.sap.com/api/API_BUSINESS_PARTNER/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_BUSINESS_PARTNER/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Sales Order API
    description: API for managing sales orders including creation, updates, and status changes.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_SALES_ORDER_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_ORDER_SRV
    tags:
      - ERP
      - Order Management
      - Sales
      - Sales Order
    properties:
      - type: OpenAPI
        url: openapi/sap-s4hana-sales-order-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-s4hana-sales-order-schema.json
      - type: JSONLD
        url: json-ld/sap-s4hana-context.jsonld
      - type: OpenAPI
        url: https://api.sap.com/api/API_SALES_ORDER_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/cd99a61e5e3f45789c954055c1e31de0/46e2b3e1e0d44419b86e4f0f6e90a0c9.html
      - type: Console
        url: https://api.sap.com/api/API_SALES_ORDER_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_SALES_ORDER_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_SALES_ORDER_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Purchase Order API
    description: API for creating and managing purchase orders in procurement processes.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_PURCHASEORDER_PROCESS_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV
    tags:
      - ERP
      - Procurement
      - Purchase Order
      - Purchasing
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_PURCHASEORDER_PROCESS_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/68bf513d4c6742ddb5c0268d46b48b7c/7e0da70d14b44e0cac79c2a29c21b695.html
      - type: Console
        url: https://api.sap.com/api/API_PURCHASEORDER_PROCESS_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_PURCHASEORDER_PROCESS_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_PURCHASEORDER_PROCESS_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Material Document API
    description: API for posting goods movements and managing inventory transactions.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_MATERIAL_DOCUMENT_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_MATERIAL_DOCUMENT_SRV
    tags:
      - ERP
      - Goods Movement
      - Inventory
      - Material Document
      - Warehouse
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_MATERIAL_DOCUMENT_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0dd0e7f348b04fc7b4e6e63bc9e1db9f/e5ced76872764cbbb8d78e81e21e7f35.html
      - type: Console
        url: https://api.sap.com/api/API_MATERIAL_DOCUMENT_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_MATERIAL_DOCUMENT_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_MATERIAL_DOCUMENT_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Product Master API
    description: API for managing product and material master data.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_PRODUCT_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_PRODUCT_SRV
    tags:
      - ERP
      - Master Data
      - Material
      - Product
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_PRODUCT_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/48a7b615c24444a9b3a6f2810f88db71.html
      - type: Console
        url: https://api.sap.com/api/API_PRODUCT_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_PRODUCT_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_PRODUCT_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Journal Entry API
    description: API for creating and managing financial journal entries.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_JOURNALENTRY_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_JOURNALENTRY_SRV
    tags:
      - Accounting
      - ERP
      - Finance
      - General Ledger
      - Journal Entry
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_JOURNALENTRY_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/b8c083f8f1614da6bf6f7a6e06c4f9be/e0f6c2e84e214c8c8d77a24b40a11ae8.html
      - type: Console
        url: https://api.sap.com/api/API_JOURNALENTRY_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_JOURNALENTRY_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_JOURNALENTRY_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Billing Document API
    description: API for reading, canceling, and retrieving PDFs of billing documents in sales and distribution.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_BILLING_DOCUMENT_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_BILLING_DOCUMENT_SRV
    tags:
      - Billing
      - ERP
      - Finance
      - Invoice
      - Sales
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_BILLING_DOCUMENT_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/65680dabb62546029175655482f85edc.html
      - type: Console
        url: https://api.sap.com/api/API_BILLING_DOCUMENT_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_BILLING_DOCUMENT_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_BILLING_DOCUMENT_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Supplier Invoice API
    description: API for creating and processing supplier invoices referenced to purchase orders.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_SUPPLIERINVOICE_PROCESS_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SUPPLIERINVOICE_PROCESS_SRV
    tags:
      - Accounts Payable
      - ERP
      - Finance
      - Procurement
      - Supplier Invoice
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_SUPPLIERINVOICE_PROCESS_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0864cb07010642b3bde45a20de4975bc/8ddf1d448ce74a799390a1706d90ca3d.html
      - type: Console
        url: https://api.sap.com/api/API_SUPPLIERINVOICE_PROCESS_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_SUPPLIERINVOICE_PROCESS_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_SUPPLIERINVOICE_PROCESS_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Customer Return API
    description: API for integrating external applications with customer return processing including advanced returns management.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CUSTOMER_RETURN_SRV
    tags:
      - Customer Return
      - ERP
      - Logistics
      - Returns Management
      - Sales
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/69bd2e81cb394eb0b3d8eae85d6b4517.html
      - type: Console
        url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Purchase Requisition API
    description: API for creating, updating, and managing purchase requisitions in procurement workflows.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_PURCHASEREQ_PROCESS_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_PURCHASEREQ_PROCESS_SRV
    tags:
      - ERP
      - Procurement
      - Purchase Requisition
      - Purchasing
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_PURCHASEREQ_PROCESS_SRV/overview
      - type: Console
        url: https://api.sap.com/api/API_PURCHASEREQ_PROCESS_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_PURCHASEREQ_PROCESS_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_PURCHASEREQ_PROCESS_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Outbound Delivery API
    description: API for creating, reading, updating, and deleting outbound deliveries including goods issue and picking operations.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_OUTBOUND_DELIVERY_SRV_0002
    tags:
      - ERP
      - Logistics
      - Outbound Delivery
      - Shipping
      - Warehouse
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/588780cab2774a7ab9fffca3a7f919fe/113abb06f3fe4e94987d35d5f86ba1ac.html
      - type: Console
        url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Inbound Delivery API
    description: API for creating, reading, updating, and deleting inbound deliveries for procurement and logistics.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_INBOUND_DELIVERY_SRV_0002
    tags:
      - ERP
      - Inbound Delivery
      - Logistics
      - Receiving
      - Warehouse
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/588780cab2774a7ab9fffca3a7f919fe/f3ff58c5e7ec43c7b55a503be6633567.html
      - type: Console
        url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Cost Center API
    description: API for reading cost center master data used in controlling and cost management.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_COSTCENTER_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_COSTCENTER_SRV
    tags:
      - Controlling
      - Cost Center
      - ERP
      - Finance
      - Master Data
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_COSTCENTER_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/6b39bd1d0e5e4099a5b65d835c29c696/5792333ddf3c47eaad4314b071dfd684.html
      - type: Console
        url: https://api.sap.com/api/API_COSTCENTER_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_COSTCENTER_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_COSTCENTER_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA GL Account API
    description: API for reading general ledger account master data in chart of accounts.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_GLACCOUNTINCHARTOFACCOUNTS_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_GLACCOUNTINCHARTOFACCOUNTS_SRV
    tags:
      - Accounting
      - ERP
      - Finance
      - General Ledger
      - GL Account
      - Master Data
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_GLACCOUNTINCHARTOFACCOUNTS_SRV/overview
      - type: Console
        url: https://api.sap.com/api/API_GLACCOUNTINCHARTOFACCOUNTS_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_GLACCOUNTINCHARTOFACCOUNTS_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_GLACCOUNTINCHARTOFACCOUNTS_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Bank Master API
    description: API for reading bank master data including bank keys, SWIFT codes, and bank details.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_BANKDETAIL_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_BANKDETAIL_SRV
    tags:
      - Bank
      - ERP
      - Finance
      - Master Data
      - Payment
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_BANKDETAIL_SRV/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e296651f454c4284ade361292c633d69/1de6770532554d43a1d026f57e7dd46e.html
      - type: Console
        url: https://api.sap.com/api/API_BANKDETAIL_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_BANKDETAIL_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_BANKDETAIL_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Production Order API
    description: API for reading production order data including components, operations, and status information.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_PRODUCTION_ORDER_2_SRV/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_PRODUCTION_ORDER_2_SRV
    tags:
      - ERP
      - Manufacturing
      - Production Order
      - Production Planning
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_PRODUCTION_ORDER_2_SRV/overview
      - type: Console
        url: https://api.sap.com/api/API_PRODUCTION_ORDER_2_SRV/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_PRODUCTION_ORDER_2_SRV/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_PRODUCTION_ORDER_2_SRV/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Maintenance Order API
    description: API for reading maintenance order data used in plant maintenance and enterprise asset management.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_MAINTENANCEORDER/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_MAINTENANCEORDER
    tags:
      - Asset Management
      - ERP
      - Maintenance Order
      - Plant Maintenance
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_MAINTENANCEORDER/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/2dfa044a255f49e89a3050daf3c61c11/ff951ebb44664d87b2a8db9290a41dc2.html
      - type: Console
        url: https://api.sap.com/api/API_MAINTENANCEORDER/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_MAINTENANCEORDER/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_MAINTENANCEORDER/schema
    contact:
      - type: Support
        url: https://support.sap.com
  - name: SAP S/4HANA Workforce Timesheet API
    description: API for creating, reading, updating, and deleting workforce timesheet entries with automatic posting to controlling.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/api/API_MANAGE_WORKFORCE_TIMESHEET/overview
    baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_MANAGE_WORKFORCE_TIMESHEET
    tags:
      - ERP
      - Human Resources
      - Time Management
      - Timesheet
      - Workforce
    properties:
      - type: OpenAPI
        url: https://api.sap.com/api/API_MANAGE_WORKFORCE_TIMESHEET/overview
      - type: Documentation
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/b08cb360201544ec803330fefa59b0f7/fa198e62c6d24788bd1f82082feb3096.html
      - type: Console
        url: https://api.sap.com/api/API_MANAGE_WORKFORCE_TIMESHEET/tryout
      - type: APIReference
        url: https://api.sap.com/api/API_MANAGE_WORKFORCE_TIMESHEET/resource
      - type: JSONSchema
        url: https://api.sap.com/api/API_MANAGE_WORKFORCE_TIMESHEET/schema
    contact:
      - type: Support
        url: https://support.sap.com
common:
  - type: Portal
    url: https://api.sap.com
  - type: GettingStarted
    url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/1e45cfd73e814aa6b1a1118e2c1d3cec.html
  - type: Authentication
    url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/26f2b5aa3f3a4019b7d08978095b9e6a.html
  - type: ChangeLog
    url: https://api.sap.com/releasenotes
  - type: Support
    url: https://support.sap.com
  - type: TermsOfService
    url: https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html
  - type: PrivacyPolicy
    url: https://www.sap.com/about/legal/privacy.html
  - type: API Catalog
    url: https://api.sap.com/products/SAPS4HANACloud/apis/all
  - type: API Packages
    url: https://api.sap.com/products/SAPS4HANACloud/apis/packages
  - type: OData V4 APIs
    url: https://api.sap.com/products/SAPS4HANACloud/apis/ODATAV4
  - type: REST APIs
    url: https://api.sap.com/products/SAPS4HANACloud/apis/REST
  - type: On-Premise API Catalog
    url: https://api.sap.com/products/SAPS4HANA/apis/all
  - type: On-Premise API Packages
    url: https://api.sap.com/products/SAPS4HANA/apis/packages
  - type: Private Edition APIs
    url: https://api.sap.com/products/SAPS4HANACloudPrivateEdition/apis/packages
  - type: Community
    url: https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-apis-and-where-to-find-them/ba-p/13723939
  - type: StatusPage
    url: https://www.sap.com/about/cloud-trust-center/cloud-service-status.html
  - type: Features
    data:
      - name: OData V2 and V4 APIs
        description: RESTful APIs following OData protocol for standardized CRUD operations and query capabilities.
      - name: Deep Insert
        description: Create complex documents with header and dependent entities in a single API request.
      - name: Optimistic Concurrency
        description: ETag-based concurrency control to prevent conflicting updates to business documents.
      - name: Real-Time Integration
        description: Synchronous API access to live ERP data for real-time business process integration.
      - name: Multi-Module Coverage
        description: APIs spanning finance, sales, procurement, logistics, manufacturing, and HR modules.
  - type: UseCases
    data:
      - name: Order-to-Cash
        description: Automate the sales process from sales order creation through delivery and billing.
      - name: Procure-to-Pay
        description: Streamline procurement from purchase requisition through purchase order, receipt, and invoice.
      - name: Financial Close
        description: Automate journal entries, cost center reporting, and GL account management for period close.
      - name: Supply Chain Visibility
        description: Track inbound and outbound deliveries, inventory movements, and material documents in real time.
  - type: Integrations
    data:
      - name: SAP Business Technology Platform
        description: Native integration with SAP BTP for extensions, analytics, and AI/ML capabilities.
      - name: SAP Integration Suite
        description: Pre-built integration flows for connecting S/4HANA with third-party applications.
      - name: Microsoft Office
        description: Integration with Excel and Outlook for business data analysis and communication workflows.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Business Applications
  - Cloud
  - Enterprise Resource Planning
  - ERP
  - Finance
  - Human Resources
  - Inventory
  - Logistics
  - Manufacturing
  - Plant Maintenance
  - Procurement
  - S/4HANA
  - Sales
  - SAP
---
