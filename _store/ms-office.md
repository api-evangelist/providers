---
aid: ms-office
name: Microsoft Office APIs
description: Collection of APIs for Microsoft Office products and services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.microsoft.com/en-us/microsoft-365
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Collaboration
  - Documents
  - Microsoft
  - Office
  - Productivity
apis:
  - name: Microsoft Graph API
    description: Unified API endpoint for accessing Microsoft 365 services including Office applications.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.microsoft.com/en-us/graph
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Graph
      - Integration
      - Microsoft 365
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://docs.microsoft.com/en-us/graph/auth/
  - name: Office Add-ins API
    description: JavaScript API for building add-ins for Word, Excel, PowerPoint, and Outlook.
    humanURL: https://docs.microsoft.com/en-us/office/dev/add-ins/
    baseURL: https://appsforoffice.microsoft.com
    tags:
      - Add-Ins
      - Extensions
      - JavaScript
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/office/dev/add-ins/overview/office-add-ins
      - type: Reference
        url: https://docs.microsoft.com/en-us/javascript/api/overview
common:
  - type: Portal
    url: https://developer.microsoft.com/
  - type: Authentication
    url: https://docs.microsoft.com/en-us/azure/active-directory/develop/
  - type: Status
    url: https://status.office.com/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
