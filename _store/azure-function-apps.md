---
aid: azure-function-apps
name: Azure Function Apps
description: Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure, with APIs for managing function apps, deployments, and runtime operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Compute
  - FaaS
  - Functions
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
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
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-functions/
  - type: Status
    url: https://status.azure.com
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/azure-functions/bg-p/AzureFunctionsBlog
  - type: GitHub Organization
    url: https://github.com/Azure/azure-functions
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/rules/azure-function-apps-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/vocabulary/azure-function-apps-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/json-ld/azure-function-apps-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/capabilities/azure-function-apps-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/capabilities/shared/azure-function-apps.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
