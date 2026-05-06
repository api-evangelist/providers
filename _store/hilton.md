---
aid: hilton
name: Hilton
description: Hilton is one of the largest and fastest-growing hospitality companies in the world, with a portfolio of hotel brands across luxury, full-service, focused-service, and timeshare segments. Hilton operates a developer program that exposes APIs for hotel search, availability, reservations, loyalty program integration, and partner distribution. Most Hilton APIs are partner-gated and require credentials issued through the Hilton developer program.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Hospitality
  - Hotels
  - Travel
  - Reservations
  - Loyalty
url: https://raw.githubusercontent.com/api-evangelist/hilton/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hilton:hilton-api
    name: Hilton Developer API
    description: Hilton provides developer APIs for hotel search, availability, reservations, and loyalty program integration. The APIs enable travel partners and corporate clients to integrate Hilton booking capabilities. Access is gated through the Hilton developer program.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.hilton.com/
    baseURL: https://api.hilton.com
    tags:
      - Hospitality
      - Hotels
      - Loyalty
      - Reservations
      - Travel
    properties:
      - type: Documentation
        url: https://developer.hilton.com/
      - type: OpenAPI
        url: openapi/hilton-hilton-api-openapi.yml
common:
  - type: Website
    url: https://www.hilton.com
  - type: Developer Portal
    url: https://developer.hilton.com/
  - type: Honors Program
    url: https://www.hilton.com/en/hilton-honors/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
