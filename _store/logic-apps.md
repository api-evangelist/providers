---
aid: logic-apps
name: Azure Logic Apps
description: Azure Logic Apps is a cloud-based workflow automation service for integrating apps, data, and services across organizations. It provides a managed iPaaS platform with hundreds of connectors, a visual workflow designer, and a fully documented Azure Resource Manager REST API for managing workflows, runs, triggers and versions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Enterprise
  - iPaaS
  - Integration
  - Microsoft
  - Workflow Automation
url: https://raw.githubusercontent.com/api-evangelist/logic-apps/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: logic-apps:management-api
    name: Azure Logic Apps Management API
    description: The Azure Logic Apps Management REST API exposes operations for managing workflows, runs, triggers, versions and integration accounts in the multitenant (Consumption) Logic Apps service via Azure Resource Manager.
    humanURL: https://learn.microsoft.com/en-us/rest/api/logic/
    baseURL: https://management.azure.com
    tags:
      - Azure
      - Management
      - REST
      - Workflow Automation
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/logic/
      - type: OpenAPI
        url: openapi/logic-apps-management-api-openapi.yml
common:
  - type: Website
    url: https://azure.microsoft.com/en-us/products/logic-apps
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/logic-apps/
  - type: Reference
    url: https://learn.microsoft.com/en-us/rest/api/logic/
  - type: Connectors
    url: https://learn.microsoft.com/en-us/connectors/connector-reference/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/logic-apps/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
