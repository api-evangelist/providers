---
aid: azure-functions
name: Azure Functions
description: Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure, supporting multiple programming languages and integration patterns.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - Compute
  - Event-Driven
  - Functions
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-functions:azure-functions-management-api
    name: Azure Functions Management API
    description: REST API for managing Azure Functions apps, function deployments, and configuration.
    humanURL: https://docs.microsoft.com/en-us/azure/azure-functions/
    baseURL: https://management.azure.com
    tags:
      - Deployment
      - Functions
      - Management
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/rest/api/appservice/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/web/resource-manager/Microsoft.Web/stable/2022-03-01/WebApps.json
      - type: Getting Started
        url: https://docs.microsoft.com/en-us/azure/azure-functions/functions-get-started
  - aid: azure-functions:azure-functions-runtime-api
    name: Azure Functions Runtime API
    description: API for invoking and interacting with deployed Azure Functions.
    humanURL: https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference
    baseURL: https://{function-app-name}.azurewebsites.net
    tags:
      - HTTP Triggers
      - Invocation
      - Runtime
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/openapi/azure-functions-openapi.yaml
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-functions/
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/azure-functions/bg-p/AzureFunctionsBlog
  - type: Status
    url: https://status.azure.com
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHub Organization
    url: https://github.com/Azure/Azure-Functions
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/rules/azure-functions-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/vocabulary/azure-functions-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/json-ld/azure-functions-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/capabilities/azure-functions-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/capabilities/shared/azure-functions.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
