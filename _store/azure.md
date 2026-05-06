---
aid: azure
name: Microsoft Azure
description: Microsoft Azure is a comprehensive cloud computing platform offering IaaS, PaaS, and SaaS solutions for building, deploying, and managing applications through Microsoft's global network of datacenters.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Computing
  - Databases
  - Infrastructure
  - Machine Learning
  - Networking
  - Platform as a Service
  - Storage
url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure:azure-compute-api
    name: Azure Compute API
    description: Manage virtual machines, containers, and serverless computing resources.
    humanURL: https://azure.microsoft.com/en-us/products/category/compute
    baseURL: https://management.azure.com
    tags:
      - Containers
      - Functions
      - Kubernetes
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/openapi/azure-management-openapi.yaml
  - aid: azure:azure-storage-api
    name: Azure Storage API
    description: Scalable cloud storage for data objects, files, messages, and more.
    humanURL: https://azure.microsoft.com/en-us/products/category/storage
    baseURL: https://management.azure.com
    tags:
      - Blob Storage
      - File Storage
      - Queue Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/openapi/azure-management-openapi.yaml
  - aid: azure:azure-cognitive-services-api
    name: Azure Cognitive Services API
    description: Add AI capabilities including vision, speech, language, and decision-making.
    humanURL: https://azure.microsoft.com/en-us/products/cognitive-services
    baseURL: https://{region}.api.cognitive.microsoft.com
    tags:
      - Artificial Intelligence
      - Computer Vision
      - Natural Language
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/cognitive-services/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/openapi/azure-management-openapi.yaml
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/rules/azure-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/vocabulary/azure-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/json-ld/azure-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/capabilities/azure-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/capabilities/shared/azure.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
