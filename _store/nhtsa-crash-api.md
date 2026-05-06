---
aid: nhtsa-crash-api
name: NHTSA Crash API
description: The NHTSA Crash Data API provides access to the National Highway Traffic Safety Administration's crash data including crash reports, vehicle information, and safety statistics collected through the Fatality Analysis Reporting System (FARS) and Crash Report Sampling System (CRSS).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Crash Data
  - Government
  - NHTSA
  - Traffic Safety
  - Transportation
url: https://raw.githubusercontent.com/api-evangelist/nhtsa-crash-api/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nhtsa-crash-api:nhtsa-crash-data-api
    name: NHTSA Crash Data API
    description: Access crash data from the National Highway Traffic Safety Administration including FARS and CRSS datasets via REST API.
    humanURL: https://crashviewer.nhtsa.dot.gov/CrashAPI
    tags:
      - Crash Data
      - CRSS
      - FARS
      - Traffic Safety
    properties:
      - type: Documentation
        url: https://crashviewer.nhtsa.dot.gov/CrashAPI
      - type: OpenAPI
        url: openapi/nhtsa-crash-api-nhtsa-crash-data-api-openapi.yml
common:
  - type: Website
    url: https://www.nhtsa.gov/
  - type: Documentation
    url: https://crashviewer.nhtsa.dot.gov/CrashAPI
  - type: Support
    url: https://www.nhtsa.gov/contact
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
