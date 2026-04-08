---
aid: sap-brim-billing-and-revenue-innovation-management
url: https://raw.githubusercontent.com/api-evangelist/sap-brim-billing-and-revenue-innovation-management/refs/heads/main/apis.yml
apis:
- name: SAP Convergent Charging API
  description: API for real-time charging and rating of usage-based services. Supports complex pricing models, prepaid and postpaid scenarios.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
  humanURL: https://help.sap.com/docs/SAP_CONVERGENT_CHARGING
  baseURL: https://api.sap.com/convergent-charging
  tags:
  - Charging
  - Rating
  - Real-Time
  - Usage-Based Pricing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_CONVERGENT_CHARGING
  - type: OpenAPI
    url: https://api.sap.com/api/convergent_charging/overview
  - type: OpenAPI
    url: openapi/sap-brim-convergent-charging-openapi.yml
  - type: Authentication
    url: https://help.sap.com/docs/SAP_CONVERGENT_CHARGING/authentication
  contact:
  - FN: SAP Support
    email: support@sap.com
    url: https://support.sap.com
- name: SAP Convergent Invoicing API
  description: API for creating, managing, and processing invoices from multiple sources. Supports complex billing scenarios, invoice consolidation, and flexible output formats.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
  humanURL: https://help.sap.com/docs/SAP_CONVERGENT_INVOICING
  baseURL: https://api.sap.com/convergent-invoicing
  tags:
  - Billing
  - Invoice Management
  - Invoicing
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_CONVERGENT_INVOICING
  - type: OpenAPI
    url: https://api.sap.com/api/convergent_invoicing/overview
  - type: Sandbox
    url: https://api.sap.com/api/convergent_invoicing/tryout
  contact:
  - FN: SAP Support
    email: support@sap.com
    url: https://support.sap.com
- name: SAP Subscription Billing API
  description: API for managing subscription lifecycle, including creation, modification, renewal, and cancellation. Supports various billing frequencies and subscription models.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
  humanURL: https://help.sap.com/docs/SAP_SUBSCRIPTION_BILLING
  baseURL: https://api.sap.com/subscription-billing
  tags:
  - Lifecycle Management
  - Recurring Billing
  - Subscriptions
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_SUBSCRIPTION_BILLING
  - type: OpenAPI
    url: https://api.sap.com/api/subscription_billing/overview
  - type: OpenAPI
    url: openapi/sap-brim-subscription-billing-openapi.yml
  - type: API Console
    url: https://api.sap.com/api/subscription_billing/console
  - type: Reference
    url: https://api.sap.com/package/SAPHybrisRevenueCloud/rest
  - type: Getting Started
    url: https://help.sap.com/doc/13f339973aee49e4a59f153b3c8299d8/2025-12-15/en-US/SAP_Subscription_Billing_API_Guide.pdf
  - type: JSONSchema
    url: json-schema/sap-brim-subscription-schema.json
  contact:
  - FN: SAP Support
    email: support@sap.com
    url: https://support.sap.com
- name: SAP Contract Accounts Receivable and Payable API
  description: API for managing customer accounts, payment processing, dunning, and dispute management. Core component for financial customer relationship management.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
  humanURL: https://help.sap.com/docs/SAP_CONTRACT_ACCOUNTS_RECEIVABLE_PAYABLE
  baseURL: https://api.sap.com/fica
  tags:
  - Accounts Receivable
  - Dunning
  - Financial Accounting
  - Payments
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_CONTRACT_ACCOUNTS_RECEIVABLE_PAYABLE
  - type: OpenAPI
    url: https://api.sap.com/api/fica/overview
  - type: Integration Guide
    url: https://help.sap.com/docs/SAP_FICA/integration
  contact:
  - FN: SAP Support
    email: support@sap.com
    url: https://support.sap.com
- name: SAP BRIM Usage Data Intake API
  description: API for ingesting high-volume usage data from various sources. Supports batch and real-time processing of usage events for rating and billing.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
  humanURL: https://help.sap.com/docs/SAP_BRIM_USAGE_DATA_INTAKE
  baseURL: https://api.sap.com/usage-data-intake
  tags:
  - Data Ingestion
  - Mediation
  - Usage Data
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_BRIM_USAGE_DATA_INTAKE
  - type: OpenAPI
    url: https://api.sap.com/api/usage_data_intake/overview
  - type: Technical Specifications
    url: https://help.sap.com/docs/SAP_BRIM_USAGE_DATA_INTAKE/specs
  contact:
  - FN: SAP Support
    email: support@sap.com
    url: https://support.sap.com
- name: SAP Revenue Accounting and Reporting API
  description: API for revenue recognition according to IFRS 15 and ASC 606 standards. Manages performance obligations, revenue allocation, and compliance reporting.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
  humanURL: https://help.sap.com/docs/SAP_REVENUE_ACCOUNTING_REPORTING
  baseURL: https://api.sap.com/revenue-accounting
  tags:
  - ASC 606
  - Compliance
  - IFRS 15
  - Revenue Recognition
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_REVENUE_ACCOUNTING_REPORTING
  - type: OpenAPI
    url: https://api.sap.com/api/revenue_accounting/overview
  - type: Compliance Guide
    url: https://help.sap.com/docs/SAP_REVENUE_ACCOUNTING_REPORTING/compliance
  contact:
  - FN: SAP Support
    email: support@sap.com
    url: https://support.sap.com
- name: SAP Subscription Order Management API
  description: API for managing subscription-based orders within the SAP BRIM suite, supporting complex offerings that combine physical products, services, and usage-based fees with full lifecycle management.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
  humanURL: https://help.sap.com/docs/BRIM
  baseURL: https://api.sap.com/subscription-order-management
  tags:
  - Lifecycle Management
  - Order Management
  - Subscription Orders
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/BRIM
  contact:
  - FN: SAP Support
    email: support@sap.com
    url: https://support.sap.com
name: SAP BRIM (Billing and Revenue Innovation Management)
tags:
- Billing
- Enterprise
- Order to Cash
- Revenue Management
- SAP
- Subscription Management
- Usage-Based Pricing
type: Contract
image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SAP BRIM (Billing and Revenue Innovation Management) is a comprehensive solution for order-to-cash processes, subscription management, usage-based pricing, and revenue management. It enables businesses to manage complex billing scenarios, subscription lifecycle, and revenue recognition.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

