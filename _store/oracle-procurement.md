---
aid: oracle-procurement
url: https://raw.githubusercontent.com/api-evangelist/oracle-procurement/refs/heads/main/apis.yml
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
name: Oracle Procurement
tags:
- ERP
- Procurement
- Purchasing
- Spend Management
- Suppliers
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs for Oracle Procurement Cloud services, enabling procurement processes, supplier management, purchasing, and spend analysis.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

