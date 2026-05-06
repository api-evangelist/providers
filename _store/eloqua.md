---
aid: eloqua
name: Oracle Eloqua
description: Oracle Eloqua is a marketing automation platform that provides tools for lead management, email marketing, and marketing campaign management through comprehensive REST APIs. It enables marketing teams to create, execute, and measure the effectiveness of marketing programs and campaigns.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CRM
  - Email Marketing
  - Lead Management
  - Marketing Automation
url: https://www.oracle.com/marketingcloud/products/marketing-automation/
created: '2025-01-01'
modified: '2026-03-16'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
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
common:
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/GettingStarted.html
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/Authentication.html
  - type: Support
    url: https://support.oracle.com/
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: SDKs
    url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/SDKs.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
