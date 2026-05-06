---
aid: azure-container-registry
name: Azure Container Registry
description: Azure Container Registry is a managed Docker registry service based on the open-source Docker Registry for storing and managing private container images and artifacts. It supports automated container image builds, geo-replication, and integrates with Azure Kubernetes Service and other Azure deployment targets.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Container Images
  - Containers
  - Docker
  - Registry
url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-container-registry:azure-container-registry
    name: Azure Container Registry
    description: Azure Container Registry is a managed Docker registry service for storing and managing private container images and artifacts with support for automated builds, geo-replication, and integration with Azure deployment targets.
    humanURL: https://azure.microsoft.com/en-us/products/container-registry
    tags:
      - Container Images
      - Containers
      - Docker
      - Registry
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/container-registry/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/container-registry/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/openapi/azure-container-registry-openapi.yaml
common:
  - type: Website
    url: https://azure.microsoft.com/en-us/products/container-registry
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/container-registry/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/container-registry/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Status
    url: https://status.azure.com/
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/rules/azure-container-registry-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/vocabulary/azure-container-registry-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/json-ld/azure-container-registry-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/capabilities/azure-container-registry-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/capabilities/shared/azure-container-registry.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
