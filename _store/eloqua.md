---
aid: eloqua
url: https://raw.githubusercontent.com/api-evangelist/eloqua/refs/heads/main/apis.yml
apis:
- aid: eloqua:eloqua-rest-api
  name: Eloqua REST API
  description: The primary REST API for Oracle Eloqua, providing access to marketing automation, contact management, campaign operations, and analytics.
  humanURL: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/
  baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  tags:
  - Campaigns
  - Contacts
  - Marketing
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/
  - type: OpenAPI
    url: openapi/eloqua-rest-openapi.yml
- aid: eloqua:eloqua-bulk-api
  name: Eloqua Bulk API
  description: Bulk API for high-volume data operations including imports, exports, and synchronization of large datasets.
  humanURL: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/BulkAPI.html
  baseURL: https://secure.p01.eloqua.com/API/Bulk/2.0/
  tags:
  - Bulk Operations
  - Data Export
  - Data Import
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/BulkAPI.html
  - type: OpenAPI
    url: openapi/eloqua-bulk-openapi.yml
name: Oracle Eloqua
tags:
- CRM
- Email Marketing
- Lead Management
- Marketing Automation
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle Eloqua is a marketing automation platform that provides tools for lead management, email marketing, and marketing campaign management through comprehensive REST APIs. It enables marketing teams to create, execute, and measure the effectiveness of marketing programs and campaigns.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

