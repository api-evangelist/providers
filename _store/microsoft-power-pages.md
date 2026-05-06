---
aid: microsoft-power-pages
name: Microsoft Power Pages
description: Microsoft Power Pages is a secure, enterprise-grade, low-code platform for creating, hosting, and administering modern external-facing business websites. It provides APIs for CRUD operations on Dataverse tables from portal pages.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Dataverse
  - Low-Code
  - Microsoft
  - Web Portals
url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-pages/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-power-pages:web-api
    name: Power Pages Web API
    tags:
      - CRUD
      - Dataverse
      - Web Portals
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{site}.powerappsportals.com/_api/
    humanURL: https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview
    properties:
      - url: https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview
        type: Documentation
      - url: https://learn.microsoft.com/en-us/power-pages/configure/read-operations
        type: Getting Started
    description: The Power Pages Web API provides CRUD operations on Dataverse tables from Power Pages websites. It enables authenticated and anonymous users to interact with business data through portal pages using standard REST conventions with table permissions for security.
common:
  - type: Portal
    url: https://make.powerpages.microsoft.com/
  - type: Website
    url: https://powerpages.microsoft.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-pages/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-pages/getting-started/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Community
    url: https://community.powerplatform.com/forums/thread/?threadid=4f8c3d6b-df78-ef11-a317-7c1e522703d5
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
