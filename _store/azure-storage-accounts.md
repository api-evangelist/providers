---
aid: azure-storage-accounts
url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/apis.yml
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
name: Azure Storage Accounts
tags:
- Azure
- Blob Storage
- Cloud Storage
- File Storage
- Queue Storage
- Storage
- Table Storage
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Storage is Microsoft's cloud storage solution for modern data storage scenarios offering highly available, massively scalable, durable, and secure storage for blobs, files, queues, tables, and disks.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

