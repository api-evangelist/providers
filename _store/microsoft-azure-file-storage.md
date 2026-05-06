---
aid: microsoft-azure-file-storage
name: Azure File Storage
description: The Azure Files FileREST protocol enables software vendors and regular Azure users to efficiently write applications and services that communicate with Azure file shares. It provides fully managed cloud file shares accessible via SMB and NFS protocols, with support for snapshots and Azure File Sync.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Storage
  - File Shares
  - File Storage
  - NFS
  - SMB
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-file-storage/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-file-storage:rest-api
    name: Azure File Storage REST API
    tags:
      - Cloud Storage
      - File Shares
      - File Storage
      - NFS
      - SMB
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{account}.file.core.windows.net/
    humanURL: https://learn.microsoft.com/en-us/rest/api/storageservices/file-service-rest-api
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/storageservices/file-service-rest-api
        type: Documentation
    description: Azure File Storage REST API provides fully managed cloud file shares accessible via SMB and NFS protocols. It supports creating file shares, managing directories and files, configuring snapshots, and setting up Azure File Sync for hybrid cloud file storage.
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
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
