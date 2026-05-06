---
aid: microsoft-whiteboard
name: Microsoft Whiteboard
description: Microsoft Whiteboard is a digital canvas for visual collaboration. It provides API access through Microsoft Graph for managing whiteboard resources, participants, and content programmatically.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Collaboration
  - Microsoft
  - Microsoft 365
  - Visual Collaboration
  - Whiteboard
url: https://raw.githubusercontent.com/api-evangelist/microsoft-whiteboard/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-whiteboard:graph-whiteboard-api
    name: Microsoft Graph Whiteboard API
    tags:
      - Collaboration
      - Microsoft Graph
      - Visual Collaboration
      - Whiteboard
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/whiteboard
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/whiteboard
        type: Documentation
      - url: https://learn.microsoft.com/en-us/graph/auth/
        type: Authentication
    description: The Microsoft Graph Whiteboard API enables developers to manage Microsoft Whiteboard resources programmatically. Applications can create whiteboards, manage participants, and export whiteboard content. The API integrates with Microsoft Teams meetings and supports collaborative digital canvas scenarios.
common:
  - type: Portal
    url: https://whiteboard.microsoft.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/microsoft-whiteboard/digital-whiteboard-app
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/whiteboard
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
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
