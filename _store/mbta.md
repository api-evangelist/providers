---
aid: mbta
name: MBTA
description: The Massachusetts Bay Transportation Authority (MBTA) V3 API provides fast, easy access to MBTA schedules, alerts, and real-time information using the JSON:API format. Free API keys are available via the developer portal.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Boston
  - Massachusetts
  - Public Transportation
  - Real-Time
  - Transit
url: https://raw.githubusercontent.com/api-evangelist/mbta/refs/heads/main/apis.yml
created: '2025-02-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mbta:mbta-v3-api
    name: MBTA V3 API
    description: The MBTA V3 API provides access to MBTA schedules, alerts, and realtime information. It uses the JSON:API format and covers routes, stops, trips, schedules, predictions, vehicles, and alerts.
    humanURL: https://www.mbta.com/developers/v3-api
    baseURL: https://api-v3.mbta.com
    tags:
      - Real-Time
      - Schedules
      - Transit
    properties:
      - type: Documentation
        url: https://www.mbta.com/developers/v3-api
      - type: Reference
        url: https://api-v3.mbta.com/
      - type: Getting Started
        url: https://www.mbta.com/developers
      - type: OpenAPI
        url: openapi/mbta-mbta-v3-api-openapi.yml
common:
  - type: Portal
    url: https://www.mbta.com/developers
  - type: Sign Up
    url: https://api-v3.mbta.com/
  - type: GitHub Organization
    url: https://github.com/mbta
  - type: Terms of Service
    url: https://www.mass.gov/files/documents/2017/10/27/massdot-developers-license-agreement.pdf
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
