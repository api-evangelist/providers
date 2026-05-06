---
aid: ups
url: https://raw.githubusercontent.com/api-evangelist/ups/refs/heads/main/apis.yml
apis:
  - aid: ups:ups-shipping
    name: UPS Shipping API
    description: The UPS Shipping API enables developers to create and manage shipments, generate shipping labels, validate addresses, retrieve rates, track packages, schedule pickups, and access time-in-transit information via OAuth 2.0 authenticated REST API calls.
    humanURL: https://developer.ups.com/
    baseURL: https://onlinetools.ups.com/api
    tags:
      - Shipping
      - Logistics
      - Tracking
      - Rating
      - Address Validation
    properties:
      - type: Documentation
        url: https://developer.ups.com/
      - type: Getting Started
        url: https://developer.ups.com/get-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ups/refs/heads/main/openapi/ups-shipping-openapi.yml
name: UPS
tags:
  - Logistics
  - Shipping
  - Fortune 500
  - Supply Chain
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-05-04'
position: Consumer
description: UPS, or United Parcel Service, is a Fortune 500 global logistics company that specializes in package delivery and supply chain management services. UPS provides a comprehensive REST API platform with OAuth 2.0 authentication covering shipping, tracking, rating, address validation, pickup scheduling, paperless international documents, and time-in-transit estimation.
common:
  - type: Website
    url: https://www.ups.com
  - type: Developer Portal
    url: https://developer.ups.com
  - type: API Catalog
    url: https://developer.ups.com/catalog
  - type: Getting Started
    url: https://developer.ups.com/get-started
  - type: Features
    data:
      - 'UPS: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - UPS Developer Kit APIs (Shipping, Tracking, Rating, Address Validation) require account; shipping rates per package/zone.
    sources:
      - https://developer.ups.com/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
