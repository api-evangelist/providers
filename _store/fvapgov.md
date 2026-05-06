---
aid: fvapgov
name: FVAP.gov
description: Federal Voting Assistance Program (FVAP) publishes XML feeds of voter information by U.S. state and territory, including important info, deadline dates, ballot rules, and election offices, plus a combined electronic Voting Assistance Guide (eVAG).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-03-30'
modified: '2026-04-28'
position: Consumer
tags:
  - Government
  - Voting
url: https://raw.githubusercontent.com/api-evangelist/fvapgov/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: fvapgov:fvapgov-xml-api
    name: FVAP.gov XML API
    description: 'Published XML feeds providing voter information by U.S. state and territory: important info, deadline dates, ballot rules, election offices, and a combined eVAG document.'
    humanURL: https://www.fvap.gov/xml-api
    baseURL: https://www.fvap.gov
    tags:
      - Elections
      - Government
      - Voting
    properties:
      - type: Documentation
        url: https://www.fvap.gov/xml-api
      - type: XSD
        url: https://www.fvap.gov/xml-api/api-schema.xsd
      - type: OpenAPI
        url: openapi/fvapgov-xml-api-openapi.yml
common:
  - type: Website
    url: https://www.fvap.gov/
  - type: Documentation
    url: https://www.fvap.gov/xml-api
  - type: JSONSchema
    url: json-schema/fvapgov-evag-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
