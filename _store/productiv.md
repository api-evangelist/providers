---
aid: productiv
url: https://raw.githubusercontent.com/api-evangelist/productiv/refs/heads/main/apis.yml
apis:
- aid: productiv:developer-api
  name: Productiv Developer API
  description: The Productiv Developer APIs support integrating custom applications into the Productiv platform, allowing external developers to define and publish new connected applications. Includes APIs for pushing usage events and user information, Data Export APIs for fetching app portfolio details, provisioning workflows, and audit events.
  humanURL: https://docs.app.productiv.com/developer-api/index.html
  baseURL: https://public-api.productiv.com
  tags:
  - Application Portfolio
  - Audit Events
  - Data Export
  - Provisioning
  - SaaS Management
  - Spend Data
  - Usage Analytics
  properties:
  - type: Documentation
    url: https://docs.app.productiv.com/developer-api/index.html
  - type: OpenAPI
    url: openapi/productiv-developer-openapi.yml
  - type: Authorization
    url: https://docs.app.productiv.com/developer-api/authorization.html
  - type: GettingStarted
    url: https://docs.app.productiv.com/developer-api/data-export-getting-started.html
  - type: JSONSchema
    url: json-schema/application.json
  - type: JSONSchema
    url: json-schema/app-summary.json
  - type: JSONSchema
    url: json-schema/app-details.json
  - type: JSONSchema
    url: json-schema/usage-event.json
  - type: JSONSchema
    url: json-schema/spend-data.json
  - type: JSONSchema
    url: json-schema/provisioned-user.json
  - type: JSONSchema
    url: json-schema/org-chart-user.json
  - type: JSONSchema
    url: json-schema/provisioning-workflow.json
  - type: JSONSchema
    url: json-schema/audit-event.json
  - type: JSONLD
    url: json-ld/productiv-context.jsonld
name: Productiv
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-07-11'
modified: '2026-04-07'
position: Consumer
description: The SaaS Management Platform that delivers the industrys most comprehensive view of your SaaS portfolio with deep usage analytics, spend data, and feature-level insights to power the technology decisions that support your business.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

