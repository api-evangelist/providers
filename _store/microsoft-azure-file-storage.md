---
aid: microsoft-azure-file-storage
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-file-storage/refs/heads/main/apis.yml
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
name: Microsoft Azure File Storage
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Azure Files FileREST protocol enables software vendors and regular Azure users to efficiently write applications and services that communicate with Azure file shares.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

