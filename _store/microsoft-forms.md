---
aid: microsoft-forms
name: Microsoft Forms
description: Microsoft Forms is a web-based application for creating surveys, quizzes, and polls. It provides API access through Microsoft Graph for managing forms, retrieving responses, and integrating form functionality into custom applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Forms
  - Microsoft
  - Microsoft 365
  - Quizzes
  - Surveys
url: https://raw.githubusercontent.com/api-evangelist/microsoft-forms/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-forms:graph-forms-api
    name: Microsoft Graph Forms API
    description: The Microsoft Graph Forms API provides programmatic access to Microsoft Forms for creating and managing forms, surveys, and quizzes. Developers can retrieve form definitions, access response data, and integrate form functionality into custom applications through the Microsoft Graph endpoint.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/forms-overview
    baseURL: https://graph.microsoft.com/v1.0/
    tags:
      - Forms
      - Microsoft Graph
      - Quizzes
      - Surveys
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/forms-overview
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/graph/use-the-api
common:
  - type: Portal
    url: https://forms.office.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/online-surveys-polls-quizzes
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
