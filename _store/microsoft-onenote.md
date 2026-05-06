---
aid: microsoft-onenote
name: Microsoft OneNote
description: Microsoft OneNote is a digital note-taking application. It provides API access through Microsoft Graph for managing notebooks, sections, section groups, and pages stored in OneDrive or SharePoint.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Microsoft
  - Microsoft 365
  - Notebooks
  - Notes
  - Productivity
url: https://raw.githubusercontent.com/api-evangelist/microsoft-onenote/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-onenote:graph-onenote-api
    name: Microsoft Graph OneNote API
    tags:
      - Microsoft Graph
      - Notebooks
      - Notes
      - Office 365
      - Pages
      - Productivity
      - Sections
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/graph/integrate-with-onenote
    properties:
      - url: https://learn.microsoft.com/en-us/graph/integrate-with-onenote
        type: Documentation
      - url: https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview
        type: Reference
      - url: https://learn.microsoft.com/en-us/graph/onenote-get-started
        type: Getting Started
    description: The Microsoft Graph OneNote API provides programmatic access to OneNote notebooks, sections, section groups, and pages stored in OneDrive or SharePoint. Developers can create, read, update, and delete notebook content, extract text from images using OCR, perform full-text search, and sync changes across devices.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/onenote/digital-note-taking-app
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/integrate-with-onenote
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Change Log
    url: https://developer.microsoft.com/en-us/graph/changelog
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/graph/throttling
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
