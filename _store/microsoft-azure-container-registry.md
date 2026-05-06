---
aid: microsoft-azure-container-registry
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-container-registry/refs/heads/main/apis.yml
apis:
  - aid: microsoft-azure-container-registry:azure-container-registry-api
    name: Azure Container Registry API
    tags:
      - Containers
      - Docker
      - Registry
      - Container Images
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{registry}.azurecr.io/
    humanURL: https://learn.microsoft.com/en-us/rest/api/containerregistry/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/containerregistry/
        type: Documentation
    description: Azure Container Registry provides REST APIs for managing container images, Helm charts, and OCI artifacts. It supports geo-replication, image scanning, task-based builds, webhook notifications, and integration with Azure Kubernetes Service and other container platforms.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/
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
description: Azure Container Registry is a managed, private Docker registry service for storing and managing container images, Helm charts, and OCI artifacts. This collection documents the REST APIs for repository management, image distribution, geo-replication, task-based builds, and webhook notifications used across cloud-native workloads.
---
