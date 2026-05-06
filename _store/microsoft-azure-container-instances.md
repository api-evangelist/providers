---
aid: microsoft-azure-container-instances
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-container-instances/refs/heads/main/apis.yml
apis:
  - aid: microsoft-azure-container-instances:rest-api
    name: Azure Container Instances REST API
    tags:
      - Container Groups
      - Containers
      - Docker
      - Serverless Containers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/container-instances/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/container-instances/
        type: Documentation
    description: Azure Container Instances REST API enables running Docker containers on-demand without managing infrastructure. It supports creating container groups, configuring networking, mounting volumes, setting resource limits, and retrieving container logs.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
modified: '2026-04-28'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
description: Azure Container Instances offers the fastest and simplest way to run containers in Azure without managing virtual machines or higher-level orchestrators. This collection captures the REST API surface for creating container groups, configuring networking and storage, and operating serverless containers on demand.
---
