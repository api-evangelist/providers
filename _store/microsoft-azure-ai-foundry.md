---
aid: microsoft-azure-ai-foundry
name: Microsoft Azure AI Foundry
description: Microsoft Azure AI Foundry is a unified platform for building, evaluating, and deploying generative AI applications. It provides a model catalog, prompt engineering tools, fine-tuning capabilities, retrieval augmented generation (RAG) patterns, and responsible AI evaluation across a comprehensive set of management and data plane APIs.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - AI Services
  - Generative AI
  - Microsoft Azure
  - Model Catalog
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-ai-foundry/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-ai-foundry:rest-api
    name: Azure AI Foundry REST API
    description: Azure AI Foundry REST API provides a unified platform for building generative AI applications. It supports model catalog access, prompt engineering, fine-tuning, RAG patterns, and responsible AI evaluation through a comprehensive set of management and data plane APIs.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/azureml/
    baseURL: https://management.azure.com/
    tags:
      - AI
      - AI Services
      - Generative AI
      - Model Catalog
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azureml/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/azure/ai-foundry/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry
      - type: SDK
        url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/ai-foundry/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: StatusPage
    url: https://status.azure.com/
  - type: GitHubOrganization
    url: https://github.com/Azure
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
