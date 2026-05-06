---
aid: norfolk-southern
name: Norfolk Southern
description: Norfolk Southern Corporation is one of the nation's premier transportation companies, operating approximately 19,300 route miles in 22 states and the District of Columbia. Norfolk Southern offers an API Resource Platform (ApiHub) providing real-time visibility into shipment status, trip plans, and gate receipts.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/norfolk-southern/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Freight
  - Logistics
  - Railroad
  - Shipping
  - Transportation
apis:
  - aid: norfolk-southern:shipment-status
    name: Norfolk Southern Shipment Status API
    description: Pinpoint the current location and ETA for shipments and access details such as commodity, origin, and destination to proactively plan and staff delivery.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nscorp.com/
    baseURL: https://api.nscorp.com
    tags:
      - Freight
      - Railroad
      - Shipment
      - Tracking
    properties:
      - type: Documentation
        url: https://developer.nscorp.com/
      - type: OpenAPI
        url: openapi/norfolk-southern-shipment-status-api.yml
  - aid: norfolk-southern:trip-plan
    name: Norfolk Southern Trip Plan API
    description: Track a shipment's progress on its planned route with its current ETA, future movements, and completed movements.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nscorp.com/
    baseURL: https://api.nscorp.com
    tags:
      - ETA
      - Railroad
      - Route
      - Trip Plan
    properties:
      - type: Documentation
        url: https://developer.nscorp.com/
  - aid: norfolk-southern:gate-receipts
    name: Norfolk Southern Gate Receipts API
    description: Access gate receipt data, terminal, and driver information, as well as the pickup numbers for equipment.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nscorp.com/
    baseURL: https://api.nscorp.com
    tags:
      - Gate Receipts
      - Intermodal
      - Terminal
    properties:
      - type: Documentation
        url: https://developer.nscorp.com/
common:
  - type: Portal
    url: https://developer.nscorp.com/
  - type: Website
    url: https://www.norfolksouthern.com/
  - type: Innovation
    url: https://www.norfolksouthern.com/en/innovation
  - type: Support
    url: mailto:CSHelpDesk@NSCORP.COM
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
---
