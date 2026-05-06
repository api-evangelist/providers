---
aid: sap-sales-and-distribution-sd
name: SAP Sales and Distribution (SD)
description: APIs for SAP Sales and Distribution module covering sales orders, pricing, delivery, billing, and customer management processes within SAP S/4HANA. These OData-based APIs enable integration with external applications for end-to-end order-to-cash operations including sales document management, logistics execution, billing, and credit management.
type: Index
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
url: https://raw.githubusercontent.com/api-evangelist/sap-sales-and-distribution-sd/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Distribution
  - ERP
  - OData
  - S/4HANA
  - Sales
  - SAP
apis:
  - aid: sap-sales-and-distribution-sd:sales-order
    name: Sales Order API
    description: Create, read, update, and delete sales orders in SAP S/4HANA. This OData service (API_SALES_ORDER_SRV) supports full CRUD operations on sales order headers, items, partners, pricing elements, and schedule lines. Sales orders are created using deep insert requests.
    humanURL: https://api.sap.com/api/API_SALES_ORDER_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_ORDER_SRV
    tags:
      - OData
      - Order Management
      - S/4HANA
      - Sales Orders
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_SALES_ORDER_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-sales-order-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-sd-sales-order-schema.json
      - type: JSONSchema
        url: json-schema/sap-sd-sales-order-item-schema.json
      - type: JSONStructure
        url: json-structure/sap-sd-sales-order-structure.json
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
      - type: Examples
        url: examples/sap-sd-list-sales-orders-example.json
      - type: Examples
        url: examples/sap-sd-create-sales-order-example.json
  - aid: sap-sales-and-distribution-sd:customer-master-data
    name: Customer Master Data API
    description: Manage customer master data including addresses, contact information, and business partner details in SAP S/4HANA. Provides access to business partner records used across SAP S/4HANA modules.
    humanURL: https://api.sap.com/api/API_BUSINESS_PARTNER/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_BUSINESS_PARTNER
    tags:
      - Business Partner
      - Customer Data
      - Master Data
      - OData
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_BUSINESS_PARTNER/overview
      - type: OpenAPI
        url: openapi/sap-sd-customer-master-data-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-sd-business-partner-schema.json
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:outbound-delivery
    name: Outbound Delivery API
    description: Create and manage outbound deliveries, goods issue, and shipping documents. Supports delivery creation with reference to sales orders and subsequent logistics processing including goods issue posting.
    humanURL: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_OUTBOUND_DELIVERY_SRV
    tags:
      - Delivery
      - Logistics
      - OData
      - Shipping
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/overview
      - type: OpenAPI
        url: openapi/sap-sd-outbound-delivery-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-sd-outbound-delivery-schema.json
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:billing-document
    name: Billing Document API
    description: Create and manage billing documents, invoices, credit memos, and debit memos. Enables billing document processing as part of the order-to-cash cycle in SAP S/4HANA including cancellation.
    humanURL: https://api.sap.com/api/OP_API_BILLING_DOCUMENT_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_BILLING_DOCUMENT_SRV
    tags:
      - Billing
      - Credit Memo
      - Invoice
      - OData
    properties:
      - type: Documentation
        url: https://api.sap.com/api/OP_API_BILLING_DOCUMENT_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-billing-document-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-sd-billing-document-schema.json
      - type: JSONStructure
        url: json-structure/sap-sd-billing-document-structure.json
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:pricing
    name: Pricing API
    description: Calculate prices, discounts, and surcharges based on pricing conditions. Manages sales pricing condition records used to determine prices in sales documents within SAP S/4HANA.
    humanURL: https://api.sap.com/api/API_SLSPRCGCONDITIONRECORD_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SLSPRCGCONDITIONRECORD_SRV
    tags:
      - Conditions
      - Discount
      - OData
      - Pricing
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_SLSPRCGCONDITIONRECORD_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-pricing-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-sd-pricing-condition-schema.json
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:sales-quotation
    name: Sales Quotation API
    description: Create and manage sales quotations and customer inquiries. Supports the complete quotation lifecycle from creation through approval and conversion to sales orders.
    humanURL: https://api.sap.com/api/API_SALES_QUOTATION_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_QUOTATION_SRV
    tags:
      - OData
      - Pre-Sales
      - Quotation
      - Sales Document
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_SALES_QUOTATION_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-sales-quotation-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:credit-management
    name: Credit Management API
    description: Manage customer credit limits, credit exposure, and credit checks in SAP S/4HANA. Enables automated credit risk assessment during sales order processing.
    humanURL: https://api.sap.com/api/API_CREDIT_MANAGEMENT/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CREDIT_MANAGEMENT
    tags:
      - Credit
      - Finance
      - OData
      - Risk Management
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_CREDIT_MANAGEMENT/overview
      - type: OpenAPI
        url: openapi/sap-sd-credit-management-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:material-master
    name: Material Master API
    description: Access material master data including product information, availability, and pricing. Provides read and write access to product records used across procurement, manufacturing, and sales processes.
    humanURL: https://api.sap.com/api/API_PRODUCT_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_PRODUCT_SRV
    tags:
      - Master Data
      - Material
      - OData
      - Product
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_PRODUCT_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-material-master-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-sd-product-schema.json
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:credit-memo-request
    name: Credit Memo Request API
    description: Create, read, update, and delete credit memo requests. Enables approval or denial of credit memo requests that require authorization before processing.
    humanURL: https://api.sap.com/api/API_CREDIT_MEMO_REQUEST_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CREDIT_MEMO_REQUEST_SRV
    tags:
      - Billing
      - Credit Memo
      - OData
      - Sales Document
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_CREDIT_MEMO_REQUEST_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-credit-memo-request-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:debit-memo-request
    name: Debit Memo Request API
    description: Create, read, update, and delete debit memo requests. Supports the full lifecycle of debit memo requests used to charge customers for additional amounts.
    humanURL: https://api.sap.com/api/API_DEBIT_MEMO_REQUEST_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_DEBIT_MEMO_REQUEST_SRV
    tags:
      - Billing
      - Debit Memo
      - OData
      - Sales Document
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_DEBIT_MEMO_REQUEST_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-debit-memo-request-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:sales-contract
    name: Sales Contract API
    description: Create and manage sales contracts including quantity contracts and value contracts. Supports contract lifecycle management from creation through fulfillment tracking.
    humanURL: https://api.sap.com/api/API_SALES_CONTRACT_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_CONTRACT_SRV
    tags:
      - Agreement
      - OData
      - S/4HANA
      - Sales Contract
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_SALES_CONTRACT_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-sales-contract-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:sales-inquiry
    name: Sales Inquiry API
    description: Read sales inquiries from SAP S/4HANA. Provides access to sales inquiry documents used in the pre-sales process to capture customer interest in products or services.
    humanURL: https://api.sap.com/api/API_SALES_INQUIRY_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_INQUIRY_SRV
    tags:
      - OData
      - Pre-Sales
      - S/4HANA
      - Sales Inquiry
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_SALES_INQUIRY_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-sales-inquiry-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:sales-scheduling-agreement
    name: Sales Scheduling Agreement API
    description: Manage sales scheduling agreements in SAP S/4HANA. Scheduling agreements define delivery schedules for recurring deliveries of materials to customers over a specified period.
    humanURL: https://api.sap.com/api/API_SALES_SCHEDULING_AGREEMENT/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_SCHEDULING_AGREEMENT
    tags:
      - Logistics
      - OData
      - Sales Contract
      - Scheduling Agreement
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_SALES_SCHEDULING_AGREEMENT/overview
      - type: OpenAPI
        url: openapi/sap-sd-sales-scheduling-agreement-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:customer-return
    name: Customer Return API
    description: Create, read, update, and delete customer returns in SAP S/4HANA. Supports integration with customer return processing including SAP Advanced Returns Management using deep insert requests.
    humanURL: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CUSTOMER_RETURN_SRV
    tags:
      - Customer Returns
      - OData
      - Reverse Logistics
      - S/4HANA
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-customer-return-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-sd-customer-return-schema.json
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:customer-returns-delivery
    name: Customer Returns Delivery API
    description: Manage customer returns deliveries in SAP S/4HANA. Enables processing of inbound deliveries related to customer returns, including goods receipt and inspection.
    humanURL: https://api.sap.com/api/OP_API_CUSTOMER_RETURN_DELIVERY_SRV_0002/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CUSTOMER_RETURN_DELIVERY_SRV_0002
    tags:
      - OData
      - Returns Delivery
      - Reverse Logistics
      - Shipping
    properties:
      - type: Documentation
        url: https://api.sap.com/api/OP_API_CUSTOMER_RETURN_DELIVERY_SRV_0002/overview
      - type: OpenAPI
        url: openapi/sap-sd-customer-returns-delivery-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:customer-material
    name: Customer Material API
    description: Manage customer-material information records that link customer-specific material numbers to internal material numbers. Supports the sales process by mapping customer part numbers to SAP materials.
    humanURL: https://api.sap.com/api/API_CUSTOMER_MATERIAL_SRV/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CUSTOMER_MATERIAL_SRV
    tags:
      - Customer Material
      - Master Data
      - OData
      - Sales
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_CUSTOMER_MATERIAL_SRV/overview
      - type: OpenAPI
        url: openapi/sap-sd-customer-material-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
  - aid: sap-sales-and-distribution-sd:inbound-delivery
    name: Inbound Delivery API
    description: Create and manage inbound deliveries in SAP S/4HANA. Supports creation of inbound deliveries with reference to sales documents and manages batch-split items for existing deliveries.
    humanURL: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/overview
    baseURL: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_INBOUND_DELIVERY_SRV_0002
    tags:
      - Inbound Delivery
      - Logistics
      - OData
      - Warehouse
    properties:
      - type: Documentation
        url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/overview
      - type: OpenAPI
        url: openapi/sap-sd-inbound-delivery-openapi.yml
      - type: JSONLD
        url: json-ld/sap-sd-context.jsonld
common:
  - type: Portal
    url: https://api.sap.com
  - type: Documentation
    url: https://help.sap.com/docs/SAP_S4HANA_CLOUD
  - type: Website
    url: https://www.sap.com
  - type: Getting Started
    url: https://developers.sap.com/tutorials.html
  - type: Authentication
    url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/
  - type: Blog
    url: https://community.sap.com/t5/c-khhcw49343/SD+%28Sales+and+Distribution%29/pd-p/209057551571413566377230676804921
  - type: Status
    url: https://www.sap.com/about/trust-center/cloud-service-status.html
  - type: Support
    url: https://support.sap.com
  - type: Terms of Service
    url: https://www.sap.com/about/agreements/product-use-and-support-terms.html
  - type: Privacy Policy
    url: https://www.sap.com/about/legal/privacy.html
  - type: GitHub Organization
    url: https://github.com/SAP
  - type: Community
    url: https://community.sap.com
  - type: Login
    url: https://accounts.sap.com
  - type: Sign Up
    url: https://developers.sap.com
  - type: SDK
    url: https://sap.github.io/cloud-sdk/
  - type: SDK
    url: https://github.com/SAP/cloud-sdk-js
  - type: SpectralRules
    url: rules/sap-sd-rules.yml
  - type: Capabilities
    url: capabilities/order-to-cash.yaml
  - type: Capabilities
    url: capabilities/customer-management.yaml
  - type: Vocabulary
    url: vocabulary/sap-sd-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
