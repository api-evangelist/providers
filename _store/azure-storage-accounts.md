---
aid: azure-storage-accounts
name: Azure Storage Accounts
description: Azure Storage is Microsoft's cloud storage solution for modern data storage scenarios offering highly available, massively scalable, durable, and secure storage for blobs, files, queues, tables, and disks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Blob Storage
  - Cloud Storage
  - File Storage
  - Queue Storage
  - Storage
  - Table Storage
url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-storage-accounts:azure-storage-blob-service-api
    name: Azure Storage Blob Service API
    description: REST API for operations on blobs in Azure Storage.
    humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api
    baseURL: https://{accountName}.blob.core.windows.net
    tags:
      - Binary Data
      - Blob Storage
      - Object Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/storage/data-plane/Microsoft.BlobStorage/stable/2023-11-03/blob.json
  - aid: azure-storage-accounts:azure-storage-management-api
    name: Azure Storage Management API
    description: REST API for managing Azure Storage accounts and resources.
    humanURL: https://learn.microsoft.com/en-us/rest/api/storagerp/
    baseURL: https://management.azure.com
    tags:
      - Azure Resource Manager
      - Management
      - Resource Provider
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/storagerp/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/storage/resource-manager/Microsoft.Storage/stable/2023-01-01/storage.json
common:
  - type: Portal
    url: https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/storage/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create
  - type: Authentication
    url: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-requests-to-azure-storage
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/storage/common/storage-apis-and-sdks
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/rules/azure-storage-accounts-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/vocabulary/azure-storage-accounts-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/json-ld/azure-storage-accounts-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/capabilities/azure-storage-accounts-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/capabilities/shared/azure-storage-accounts.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
