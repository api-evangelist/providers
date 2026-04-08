---
aid: azure-storage-account
url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/apis.yml
apis:
- aid: azure-storage-account:azure-blob-storage-api
  name: Azure Blob Storage API
  description: REST API for storing and managing unstructured data as blobs.
  humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api
  baseURL: https://{account}.blob.core.windows.net
  tags:
  - Blob Storage
  - Object Storage
  - Unstructured Data
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/storage/blobs/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/storage/data-plane/Microsoft.BlobStorage/stable/2021-12-02/blob.json
  - type: Authentication
    url: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-requests-to-azure-storage
- aid: azure-storage-account:azure-queue-storage-api
  name: Azure Queue Storage API
  description: REST API for storing and retrieving messages in queues.
  humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/queue-service-rest-api
  baseURL: https://{account}.queue.core.windows.net
  tags:
  - Asynchronous Processing
  - Message Queue
  - Queue Storage
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/storage/queues/
- aid: azure-storage-account:azure-table-storage-api
  name: Azure Table Storage API
  description: REST API for storing structured NoSQL data in the cloud.
  humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/table-service-rest-api
  baseURL: https://{account}.table.core.windows.net
  tags:
  - NoSQL
  - Structured Data
  - Table Storage
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/storage/tables/
- aid: azure-storage-account:azure-file-storage-api
  name: Azure File Storage API
  description: REST API for managed file shares using SMB and NFS protocols.
  humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/file-service-rest-api
  baseURL: https://{account}.file.core.windows.net
  tags:
  - File Shares
  - File Storage
  - SMB
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/storage/files/
name: Azure Storage Account
tags:
- Azure
- Blob Storage
- Cloud Storage
- File Storage
- Microsoft
- Storage
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Azure Storage Account services including Blob, Queue, Table, and File storage, providing highly available, massively scalable, durable, and secure storage for a variety of data objects.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

