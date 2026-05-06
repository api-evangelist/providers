---
name: Azure Blob Storage
description: Microsoft Azure Blob Storage is a service for storing large amounts of unstructured object data, such as text or binary data, that can be accessed from anywhere in the world via HTTP or HTTPS.
image: https://azure.microsoft.com/svghandler/storage-blobs/
tags:
  - Azure
  - Blobs
  - Cloud Storage
  - Microsoft
  - Object Storage
  - Storage
created: '2024'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/storage/blobs/
apis:
  - name: Azure Blob Storage REST API
    description: The REST API for Azure Blob Storage provides operations for working with blobs and containers, including create, read, update, and delete operations.
    image: https://azure.microsoft.com/svghandler/storage-blobs/
    humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api
    baseURL: https://{accountName}.blob.core.windows.net
    tags:
      - Blobs
      - Containers
      - REST API
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/storage/data-plane/Microsoft.BlobStorage/stable/2021-12-02/blob.json
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-requests-to-azure-storage
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction#client-libraries
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview
      - type: Code Samples
        url: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-samples-blobs-cli
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/operations-on-blobs
      - type: Change Log
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/versioning-for-the-azure-storage-services
      - type: Quotas
        url: https://learn.microsoft.com/en-us/azure/storage/blobs/scalability-targets
      - type: GitHubRepository
        url: https://github.com/Azure/azure-rest-api-specs
  - name: Azure Data Lake Storage Gen2 REST API
    description: The Azure Data Lake Storage Gen2 REST APIs allow interaction with Azure Blob Storage through a file system interface. They enable creation and management of file systems, directories, and files on storage accounts with hierarchical namespace enabled, supporting big data analytics workloads.
    image: https://azure.microsoft.com/svghandler/storage-blobs/
    humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/data-lake-storage-gen2
    baseURL: https://{accountName}.dfs.core.windows.net
    tags:
      - Big Data
      - Data Lake
      - File System
      - Hierarchical Namespace
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/data-lake-storage-gen2
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/datalakestoragegen2/filesystem
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-requests-to-azure-storage
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction#client-libraries
  - name: Azure Storage Resource Provider REST API
    description: The Azure Storage Resource Provider REST API enables programmatic management of storage accounts and related resources through Azure Resource Manager. It supports operations such as creating, updating, listing, and deleting storage accounts, managing access keys, and configuring storage account properties.
    image: https://azure.microsoft.com/svghandler/storage-blobs/
    humanURL: https://learn.microsoft.com/en-us/rest/api/storagerp/
    baseURL: https://management.azure.com
    tags:
      - Administration
      - Management
      - Resource Provider
      - Storage Accounts
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/storagerp/
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/storagerp/storage-accounts
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/storage/common/authorization-resource-provider
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/storage/resource-manager/Microsoft.Storage/stable/2023-05-01/storage.json
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/topics/storage/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
  - type: Change Log
    url: https://learn.microsoft.com/en-us/rest/api/storageservices/previous-azure-storage-service-versions
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/storage/blobs/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-requests-to-azure-storage
  - type: Quotas
    url: https://learn.microsoft.com/en-us/azure/storage/blobs/scalability-targets
  - type: Website
    url: https://azure.microsoft.com/en-us/products/storage/blobs/
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free/
  - type: Console
    url: https://portal.azure.com/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/storage/common/storage-srp-overview
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-blob-storage
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Developer Tools
    url: https://azure.microsoft.com/en-us/products/storage/storage-explorer
  - type: Security
    url: https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/storage-security-baseline
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
