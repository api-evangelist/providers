---
aid: ms-office
url: https://raw.githubusercontent.com/api-evangelist/ms-office/refs/heads/main/apis.yml
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
name: Microsoft Office APIs
tags:
- Collaboration
- Documents
- Microsoft
- Office
- Productivity
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Microsoft Office products and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

