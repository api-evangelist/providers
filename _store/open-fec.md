---
aid: open-fec
name: OpenFEC
description: The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. Bulk downloads are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data are updated nightly.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Campaign Finance
  - Elections
  - FEC
  - Federal
  - Government
url: https://raw.githubusercontent.com/api-evangelist/open-fec/refs/heads/main/apis.yml
created: '2024-03-30'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: open-fec:openfec-api
    name: OpenFEC API
    description: RESTful web service supporting full-text and field-specific searches on Federal Election Commission data including candidates, committees, and financial data.
    humanURL: https://api.open.fec.gov/developers/
    baseURL: https://api.open.fec.gov/v1
    tags:
      - Campaign Finance
      - Elections
      - FEC
    properties:
      - type: Documentation
        url: https://api.open.fec.gov/developers/
      - type: OpenAPI
        url: openapi/open-fec-openapi.yml
common:
  - type: Website
    url: https://www.fec.gov/
  - type: Documentation
    url: https://api.open.fec.gov/developers/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
