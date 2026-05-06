---
aid: federal-railroad-administration
name: Federal Railroad Administration
description: The Federal Railroad Administration (FRA) is an agency within the Department of Transportation that is responsible for regulating and overseeing the safety of the nation's railroad systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-03-29'
modified: '2026-04-28'
position: Consumer
tags:
  - Federal Government
  - Railroads
  - Safety
  - Transportation
url: https://raw.githubusercontent.com/api-evangelist/federal-railroad-administration/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-railroad-administration:federal-railroad-administration
    name: Federal Railroad Administration Public API
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Railroads
      - Safety
    humanURL: https://safetydata.fra.dot.gov/MasterWebService/publicapi/
    baseURL: https://safetydata.fra.dot.gov/MasterWebService/publicapi
    description: The Federal Railroad Administration Public API provides safety data and access to railroad datasets including accidents, incidents, highway-rail grade crossings, inspections, and operational data.
    properties:
      - type: Documentation
        url: https://safetydata.fra.dot.gov/MasterWebService/publicapi/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/federal-railroad-administration/refs/heads/main/openapi/federal-railroad-administration-openapi.yml
common:
  - type: Website
    url: https://www.fra.dot.gov/
  - type: Documentation
    url: https://safetydata.fra.dot.gov/MasterWebService/publicapi/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
