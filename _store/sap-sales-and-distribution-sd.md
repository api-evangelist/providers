---
aid: sap-sales-and-distribution-sd
url: https://raw.githubusercontent.com/api-evangelist/sap-sales-and-distribution-sd/refs/heads/main/apis.yml
apis:
- name: Sales Order API
  description: Create, read, update, and delete sales orders in SAP S/4HANA. This OData service supports full CRUD operations on sales order headers, items, partners, pricing elements, and schedule lines.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_SALES_ORDER_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_ORDER_SRV
  tags:
  - OData
  - Order Management
  - S/4HANA
  - Sales Orders
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_SALES_ORDER_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_SALES_ORDER_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-sales-order-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_SALES_ORDER_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_SALES_ORDER_SRV/resource
  - type: JSONSchema
    url: json-schema/sap-sd-sales-order-schema.json
  - type: JSONSchema
    url: json-schema/sap-sd-sales-order-item-schema.json
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Customer Master Data API
  description: Manage customer master data including addresses, contact information, and business partner details. This API provides access to business partner records used across SAP S/4HANA modules.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_BUSINESS_PARTNER/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_BUSINESS_PARTNER
  tags:
  - Business Partner
  - Customer Data
  - Master Data
  - OData
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_BUSINESS_PARTNER/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_BUSINESS_PARTNER/specification
  - type: OpenAPI
    url: openapi/sap-sd-customer-master-data-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_BUSINESS_PARTNER/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_BUSINESS_PARTNER/resource
  - type: JSONSchema
    url: json-schema/sap-sd-business-partner-schema.json
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Outbound Delivery API
  description: Create and manage outbound deliveries, goods issue, and shipping documents. This OData service supports delivery creation with reference to sales orders and subsequent logistics processing.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_OUTBOUND_DELIVERY_SRV
  tags:
  - Delivery
  - Logistics
  - OData
  - Shipping
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/specification
  - type: OpenAPI
    url: openapi/sap-sd-outbound-delivery-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_OUTBOUND_DELIVERY_SRV_0002/resource
  - type: JSONSchema
    url: json-schema/sap-sd-outbound-delivery-schema.json
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Billing Document API
  description: Create and manage billing documents, invoices, credit memos, and debit memos. This API enables billing document processing as part of the order-to-cash cycle in SAP S/4HANA.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/OP_API_BILLING_DOCUMENT_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_BILLING_DOCUMENT_SRV
  tags:
  - Billing
  - Credit Memo
  - Invoice
  - OData
  properties:
  - type: Documentation
    url: https://api.sap.com/api/OP_API_BILLING_DOCUMENT_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/OP_API_BILLING_DOCUMENT_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-billing-document-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/OP_API_BILLING_DOCUMENT_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/OP_API_BILLING_DOCUMENT_SRV/resource
  - type: JSONSchema
    url: json-schema/sap-sd-billing-document-schema.json
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Pricing API
  description: Calculate prices, discounts, and surcharges based on pricing conditions. This API manages sales pricing condition records used to determine prices in sales documents.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_SLSPRCGCONDITIONRECORD_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SLSPRCGCONDITIONRECORD_SRV
  tags:
  - Conditions
  - Discount
  - OData
  - Pricing
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_SLSPRCGCONDITIONRECORD_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_SLSPRCGCONDITIONRECORD_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-pricing-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_SLSPRCGCONDITIONRECORD_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_SLSPRCGCONDITIONRECORD_SRV/resource
  - type: JSONSchema
    url: json-schema/sap-sd-pricing-condition-schema.json
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Sales Quotation API
  description: Create and manage sales quotations and customer inquiries. This OData service supports the complete quotation lifecycle from creation through approval and conversion to sales orders.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_SALES_QUOTATION_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_QUOTATION_SRV
  tags:
  - OData
  - Pre-Sales
  - Quotation
  - Sales Document
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_SALES_QUOTATION_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_SALES_QUOTATION_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-sales-quotation-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_SALES_QUOTATION_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_SALES_QUOTATION_SRV/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Credit Management API
  description: Manage customer credit limits, credit exposure, and credit checks. This API enables automated credit risk assessment during sales order processing in SAP S/4HANA.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_CREDIT_MANAGEMENT/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CREDIT_MANAGEMENT
  tags:
  - Credit
  - Finance
  - OData
  - Risk Management
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_CREDIT_MANAGEMENT/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_CREDIT_MANAGEMENT/specification
  - type: OpenAPI
    url: openapi/sap-sd-credit-management-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_CREDIT_MANAGEMENT/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_CREDIT_MANAGEMENT/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Material Master API
  description: Access material master data including product information, availability, and pricing. This API provides read and write access to product records used across procurement, manufacturing, and sales processes.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_PRODUCT_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_PRODUCT_SRV
  tags:
  - Master Data
  - Material
  - OData
  - Product
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_PRODUCT_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_PRODUCT_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-material-master-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_PRODUCT_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_PRODUCT_SRV/resource
  - type: JSONSchema
    url: json-schema/sap-sd-product-schema.json
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Credit Memo Request API
  description: Create, read, update, and delete credit memo requests. This OData service also enables approval or denial of credit memo requests that require authorization before processing.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_CREDIT_MEMO_REQUEST_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CREDIT_MEMO_REQUEST_SRV
  tags:
  - Billing
  - Credit Memo
  - OData
  - Sales Document
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_CREDIT_MEMO_REQUEST_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_CREDIT_MEMO_REQUEST_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-credit-memo-request-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_CREDIT_MEMO_REQUEST_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_CREDIT_MEMO_REQUEST_SRV/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Debit Memo Request API
  description: Create, read, update, and delete debit memo requests. This OData service supports the full lifecycle of debit memo requests used to charge customers for additional amounts.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_DEBIT_MEMO_REQUEST_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_DEBIT_MEMO_REQUEST_SRV
  tags:
  - Billing
  - Debit Memo
  - OData
  - Sales Document
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_DEBIT_MEMO_REQUEST_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_DEBIT_MEMO_REQUEST_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-debit-memo-request-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_DEBIT_MEMO_REQUEST_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_DEBIT_MEMO_REQUEST_SRV/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Sales Contract API
  description: Create and manage sales contracts including quantity contracts and value contracts. This API supports contract lifecycle management from creation through fulfillment tracking.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_SALES_CONTRACT_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_CONTRACT_SRV
  tags:
  - Agreement
  - OData
  - S/4HANA
  - Sales Contract
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_SALES_CONTRACT_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_SALES_CONTRACT_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-sales-contract-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_SALES_CONTRACT_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_SALES_CONTRACT_SRV/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Sales Inquiry API
  description: Read sales inquiries from SAP S/4HANA. This OData service provides access to sales inquiry documents used in the pre-sales process to capture customer interest in products or services.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_SALES_INQUIRY_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_INQUIRY_SRV
  tags:
  - OData
  - Pre-Sales
  - S/4HANA
  - Sales Inquiry
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_SALES_INQUIRY_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_SALES_INQUIRY_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-sales-inquiry-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_SALES_INQUIRY_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_SALES_INQUIRY_SRV/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Sales Scheduling Agreement API
  description: Manage sales scheduling agreements in SAP S/4HANA. Scheduling agreements define delivery schedules for recurring deliveries of materials to customers over a specified period.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_SALES_SCHEDULING_AGREEMENT/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_SALES_SCHEDULING_AGREEMENT
  tags:
  - Logistics
  - OData
  - Sales Contract
  - Scheduling Agreement
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_SALES_SCHEDULING_AGREEMENT/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_SALES_SCHEDULING_AGREEMENT/specification
  - type: OpenAPI
    url: openapi/sap-sd-sales-scheduling-agreement-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_SALES_SCHEDULING_AGREEMENT/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_SALES_SCHEDULING_AGREEMENT/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Customer Return API
  description: Create, read, update, and delete customer returns in SAP S/4HANA. This API supports integration with customer return processing including SAP Advanced Returns Management using deep insert requests.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CUSTOMER_RETURN_SRV
  tags:
  - Customer Returns
  - OData
  - Reverse Logistics
  - S/4HANA
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-customer-return-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_CUSTOMER_RETURN_SRV/resource
  - type: JSONSchema
    url: json-schema/sap-sd-customer-return-schema.json
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Customer Returns Delivery API
  description: Manage customer returns deliveries in SAP S/4HANA. This API enables processing of inbound deliveries related to customer returns, including goods receipt and inspection.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/OP_API_CUSTOMER_RETURN_DELIVERY_SRV_0002/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CUSTOMER_RETURN_DELIVERY_SRV_0002
  tags:
  - OData
  - Returns Delivery
  - Reverse Logistics
  - Shipping
  properties:
  - type: Documentation
    url: https://api.sap.com/api/OP_API_CUSTOMER_RETURN_DELIVERY_SRV_0002/overview
  - type: OpenAPI
    url: https://api.sap.com/api/OP_API_CUSTOMER_RETURN_DELIVERY_SRV_0002/specification
  - type: OpenAPI
    url: openapi/sap-sd-customer-returns-delivery-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/OP_API_CUSTOMER_RETURN_DELIVERY_SRV_0002/tryout
  - type: API Reference
    url: https://api.sap.com/api/OP_API_CUSTOMER_RETURN_DELIVERY_SRV_0002/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Customer Material API
  description: Manage customer-material information records that link customer-specific material numbers and descriptions to internal material numbers. This API supports the sales process by mapping customer part numbers.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_CUSTOMER_MATERIAL_SRV/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_CUSTOMER_MATERIAL_SRV
  tags:
  - Customer Material
  - Master Data
  - OData
  - Sales
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_CUSTOMER_MATERIAL_SRV/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_CUSTOMER_MATERIAL_SRV/specification
  - type: OpenAPI
    url: openapi/sap-sd-customer-material-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_CUSTOMER_MATERIAL_SRV/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_CUSTOMER_MATERIAL_SRV/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
- name: Inbound Delivery API
  description: Create and manage inbound deliveries in SAP S/4HANA. This API supports creation of inbound deliveries with reference to sales documents and manages batch-split items for existing deliveries.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanUrl: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/overview
  baseUrl: https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap/API_INBOUND_DELIVERY_SRV_0002
  tags:
  - Inbound Delivery
  - Logistics
  - OData
  - Warehouse
  properties:
  - type: Documentation
    url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/overview
  - type: OpenAPI
    url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/specification
  - type: OpenAPI
    url: openapi/sap-sd-inbound-delivery-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/tryout
  - type: API Reference
    url: https://api.sap.com/api/API_INBOUND_DELIVERY_SRV_0002/resource
  - type: JSONLD
    url: json-ld/sap-sd-context.jsonld
  contact:
  - type: Support
    url: https://support.sap.com
name: SAP Sales and Distribution (SD)
tags:
- Distribution
- ERP
- OData
- S/4HANA
- Sales
- SAP
type: Contract
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for SAP Sales and Distribution module covering sales orders, pricing, delivery, billing, and customer management processes within SAP S/4HANA. These OData-based APIs enable integration with external applications for end-to-end order-to-cash operations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

