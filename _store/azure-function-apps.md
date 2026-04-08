---
aid: azure-function-apps
url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/apis.yml
apis:
- aid: azure-function-apps:azure-function-apps-rest-api
  name: Azure Function Apps REST API
  description: REST API for managing Azure Function Apps, including creating, updating, and deleting function apps, as well as managing settings and deployments.
  humanURL: https://learn.microsoft.com/en-us/azure/azure-functions/
  baseURL: https://management.azure.com
  tags:
  - Functions
  - Management
  - Serverless
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/appservice/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/web/resource-manager/Microsoft.Web/stable/2022-09-01/WebApps.json
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-get-started
name: Azure Function Apps
tags:
- Azure
- Compute
- FaaS
- Functions
- Serverless
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure, with APIs for managing function apps, deployments, and runtime operations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

