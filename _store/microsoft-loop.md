---
aid: microsoft-loop
name: Microsoft Loop
description: Microsoft Loop is a collaborative productivity app that brings together teams, content, and tasks across Microsoft 365 tools. It provides API access through Microsoft Graph for managing Loop workspaces and components.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Collaboration
  - Microsoft
  - Microsoft 365
  - Productivity
url: https://raw.githubusercontent.com/api-evangelist/microsoft-loop/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-loop:graph-loop-api
    name: Microsoft Graph Loop API
    tags:
      - Collaboration
      - Loop Components
      - Microsoft Graph
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/graph/loop-api-concept-overview
    properties:
      - url: https://learn.microsoft.com/en-us/graph/loop-api-concept-overview
        type: Documentation
      - url: https://learn.microsoft.com/en-us/graph/auth/
        type: Authentication
    description: The Microsoft Graph Loop API enables developers to interact with Microsoft Loop workspaces and components. Loop components are portable, collaborative content blocks that sync across Microsoft 365 apps. The API provides access to Loop pages stored in SharePoint Embedded containers, enabling creation and management of collaborative content.
common:
  - type: Portal
    url: https://loop.microsoft.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-loop
  - type: Documentation
    url: https://support.microsoft.com/en-us/topic/get-started-with-microsoft-loop-9f4d8d4f-dfc6-4518-9ef6-069408c21f0c
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
