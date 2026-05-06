---
aid: freedom-of-information-act
name: Freedom of Information Act
description: The Freedom of Information Act (FOIA) API provides access to FOIA request data and related information from federal agencies.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Federal Government
  - FOIA
  - Transparency
apis:
  - aid: freedom-of-information-act:freedom-of-information-act-foia-api
    name: Freedom of Information Act (FOIA) API
    description: The FOIA API provides access to public FOIA request data, agency components, and annual report XML, plus the agency submission specification used by participating agencies.
    humanURL: https://www.foia.gov/developer/
    baseURL: https://api.foia.gov
    tags:
      - Federal Government
      - FOIA
      - Transparency
    properties:
      - type: Documentation
        url: https://www.foia.gov/developer/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/openapi/freedom-of-information-act-openapi.yml
common:
  - type: Portal
    url: https://www.foia.gov/developer/
  - type: Website
    url: https://www.foia.gov/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
