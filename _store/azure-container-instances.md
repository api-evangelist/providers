---
aid: azure-container-instances
name: Azure Container Instances
description: Azure Container Instances (ACI) is the fastest and simplest way to run containers in Azure without having to manage virtual machines or adopt a higher-level orchestration service. It offers serverless containers with per-second billing, custom sizes, and seamless integration with the Azure ecosystem for burst and event-driven workloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Cloud
  - Container Instances
  - Containers
  - Microsoft
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-container-instances:azure-container-instances
    name: Azure Container Instances
    description: Azure Container Instances is a service that enables you to run containers directly on the Microsoft Azure cloud without managing virtual machines or adopting orchestration services. It provides fast startup times, per-second billing, custom CPU and memory sizing, and persistent storage with Azure Files integration for both Linux and Windows containers.
    humanURL: https://azure.microsoft.com/en-us/products/container-instances
    tags:
      - Azure
      - Cloud
      - Container Instances
      - Containers
      - Microsoft
      - Serverless
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/container-instances/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/openapi/azure-container-instances-openapi.yaml
common:
  - type: Website
    url: https://azure.microsoft.com/en-us/products/container-instances
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/container-instances/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/container-instances/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free/
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/rules/azure-container-instances-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/vocabulary/azure-container-instances-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/json-ld/azure-container-instances-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/capabilities/azure-container-instances-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/capabilities/shared/azure-container-instances.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
