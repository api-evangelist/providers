---
aid: durable-functions
name: Azure Durable Functions
description: Azure Durable Functions is a serverless extension for writing stateful workflows and orchestrations in code using Azure Functions. The extension exposes built-in HTTP APIs for managing orchestrations, durable entities, and task hubs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Composition
  - Durable Execution
  - Serverless Orchestration
  - Workflow
url: https://raw.githubusercontent.com/api-evangelist/durable-functions/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: durable-functions:durable-functions-http-api
    name: Azure Durable Functions HTTP API
    description: Built-in HTTP APIs exposed by the Durable Functions extension for starting orchestrations, querying instance status, raising events, terminating, suspending, resuming, rewinding, signaling entities, and purging history.
    humanURL: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-http-api
    baseURL: https://{appName}.azurewebsites.net
    tags:
      - Durable Execution
      - Serverless Orchestration
      - Workflow
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/azure-functions/durable/
      - type: HTTP API Reference
        url: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-http-api
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-create-first-csharp
      - type: OpenAPI
        url: openapi/durable-functions-http-api-openapi.yml
common:
  - type: Website
    url: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-functions/durable/
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Repository
    url: https://github.com/Azure/azure-functions-durable-extension
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
