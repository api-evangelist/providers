---
aid: google-ad-manager
name: Google Ad Manager
description: The Google Ad Manager API provides programmatic access to manage Ad Manager data including ad units, companies, orders, placements, line items, creatives, reports, and targeting. It enables publishers to automate their ad operations and integrate Ad Manager with other systems.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-ad-manager/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Ad Manager
  - Ad Operations
  - Ad Serving
  - Creatives
  - Line Items
  - Orders
  - Publishers
  - Targeting
apis:
  - aid: google-ad-manager:google-ad-manager
    name: Google Ad Manager API
    description: The Ad Manager API enables programmatic management of ad inventory, orders, line items, creatives, reports, and targeting for publisher ad operations and revenue management.
    humanURL: https://developers.google.com/ad-manager/api/start
    baseURL: https://admanager.googleapis.com
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.yml
common:
  - type: Getting Started
    url: https://developers.google.com/ad-manager/api/beta/getting-started
  - type: Pricing
    url: https://admanager.google.com/home/
  - type: JSONLD
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
