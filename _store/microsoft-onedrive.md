---
aid: microsoft-onedrive
name: Microsoft OneDrive
description: Microsoft OneDrive is a cloud-based file storage and synchronization service. It provides APIs through Microsoft Graph for accessing, managing, and sharing files and folders stored in OneDrive personal and OneDrive for Business.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Storage
  - File Storage
  - Files
  - Microsoft
  - Microsoft 365
url: https://raw.githubusercontent.com/api-evangelist/microsoft-onedrive/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-onedrive:graph-drive-api
    name: Microsoft Graph OneDrive API
    tags:
      - Cloud Storage
      - File Storage
      - Files
      - Microsoft Graph
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/
    properties:
      - url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/graph/api/resources/onedrive
        type: Reference
    description: The Microsoft Graph OneDrive API provides programmatic access to OneDrive personal and OneDrive for Business file storage. Developers can upload, download, search, and share files and folders, manage permissions, track changes with delta queries, and create sharing links. The API supports large file uploads with resumable sessions and real-time notifications via webhooks.
  - aid: microsoft-onedrive:file-picker
    name: OneDrive File Picker
    tags:
      - File Picker
      - Files
      - UI Component
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/onedrive/developer/controls/file-pickers/
    properties:
      - url: https://learn.microsoft.com/en-us/onedrive/developer/controls/file-pickers/
        type: Documentation
    description: The OneDrive File Picker is a JavaScript SDK that provides a pre-built UI component for selecting files from OneDrive within web applications. It handles authentication, file browsing, and selection, returning file metadata and download URLs to the calling application without requiring direct API integration.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage
  - type: Documentation
    url: https://learn.microsoft.com/en-us/onedrive/developer/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
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
