---
aid: azure-functions
url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/apis.yml
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
name: Azure Functions
tags:
- Cloud
- Compute
- Event-Driven
- Functions
- Serverless
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure, supporting multiple programming languages and integration patterns.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

