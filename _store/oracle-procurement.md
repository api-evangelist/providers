---
aid: oracle-procurement
name: Oracle Procurement
description: A collection of APIs for Oracle Procurement Cloud services, enabling procurement processes, supplier management, purchasing, and spend analysis.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ERP
  - Procurement
  - Purchasing
  - Spend Management
  - Suppliers
created: '2024-01-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/oracle-procurement/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - name: Oracle Procurement REST API
    description: REST API for managing procurement operations including requisitions, purchase orders, and supplier information.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanUrl: https://docs.oracle.com/en/cloud/saas/procurement/
    baseUrl: https://your-instance.oraclecloud.com/fscmRestApi/resources/latest
    tags:
      - Procurement
      - Purchase Orders
      - Requisitions
      - REST
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/api-procurement.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/Authentication.html
  - name: Purchase Orders API
    description: Create, update, and manage purchase orders.
    humanUrl: https://docs.oracle.com/en/cloud/saas/procurement/
    baseUrl: https://your-instance.oraclecloud.com/fscmRestApi/resources/latest/purchaseOrders
    tags:
      - Buying
      - Purchase Orders
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/op-purchaseorders-get.html
  - name: Requisitions API
    description: Manage purchase requisitions and approval workflows.
    humanUrl: https://docs.oracle.com/en/cloud/saas/procurement/
    baseUrl: https://your-instance.oraclecloud.com/fscmRestApi/resources/latest/requisitions
    tags:
      - Approvals
      - Requisitions
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/op-requisitions-get.html
  - name: Suppliers API
    description: Access and manage supplier information, sites, and contacts.
    humanUrl: https://docs.oracle.com/en/cloud/saas/procurement/
    baseUrl: https://your-instance.oraclecloud.com/fscmRestApi/resources/latest/suppliers
    tags:
      - Suppliers
      - Vendor Management
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/op-suppliers-get.html
  - name: Purchase Agreements API
    description: Manage blanket purchase agreements and contract terms.
    humanUrl: https://docs.oracle.com/en/cloud/saas/procurement/
    baseUrl: https://your-instance.oraclecloud.com/fscmRestApi/resources/latest/purchaseAgreements
    tags:
      - Agreements
      - Contracts
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/
  - name: Receipts API
    description: Record and manage receipt transactions for purchased goods and services.
    humanUrl: https://docs.oracle.com/en/cloud/saas/procurement/
    baseUrl: https://your-instance.oraclecloud.com/fscmRestApi/resources/latest/receipts
    tags:
      - Receipts
      - Receiving
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/
common:
  - type: Getting Started
    url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/QuickStart.html
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/
  - type: Portal
    url: https://cloud.oracle.com/
  - type: Support
    url: https://www.oracle.com/support/
  - type: Status
    url: https://ocistatus.oraclecloud.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
