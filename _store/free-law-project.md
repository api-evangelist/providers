---
aid: free-law-project
name: Free Law Project
description: Free Law Project is a non-profit organization that seeks to increase access to justice and transparency in the legal system through the use of technology and open data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-07'
modified: '2026-04-28'
position: Consumer
tags:
  - Courts
  - Justice
  - Legal
  - Transparency
url: https://raw.githubusercontent.com/api-evangelist/free-law-project/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: free-law-project:free-law-project
    name: Free Law Project API
    tags:
      - Courts
      - Justice
      - Legal
      - Transparency
    humanURL: https://free.law/
    baseURL: https://www.courtlistener.com/api/rest/v4
    properties:
      - url: https://www.courtlistener.com/help/api/rest/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/free-law-project/refs/heads/main/openapi/free-law-project-openapi.yml
        type: OpenAPI
    description: The Free Law Project / CourtListener REST API provides access to case law, PACER data, the RECAP archive, oral arguments, judges, financial disclosures, citations, alerts, and tags.
common:
  - type: Website
    url: https://free.law/
  - type: Documentation
    url: https://www.courtlistener.com/help/api/rest/
  - type: GitHub Organization
    url: https://github.com/freelawproject
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
