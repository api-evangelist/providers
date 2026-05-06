---
aid: google-adsense
name: Google AdSense Management
description: The Google AdSense Management API allows publishers to access their inventory and run earnings and performance reports. Publishers can manage ad clients, ad units, custom channels, URL channels, and access payment and policy information programmatically.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-adsense/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Ad Units
  - AdSense
  - Advertising
  - Monetization
  - Publishers
  - Reports
  - Revenue
apis:
  - aid: google-adsense:google-adsense
    name: Google AdSense Management API
    description: The AdSense Management API enables publishers to programmatically manage their ad inventory, access earnings reports, configure ad clients and units, and retrieve payment and policy information.
    humanURL: https://developers.google.com/adsense/management
    baseURL: https://adsense.googleapis.com
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.yml
common:
  - type: Getting Started
    url: https://developers.google.com/adsense/management/getting_started
  - type: Pricing
    url: https://support.google.com/adsense/answer/180195
  - type: JSONLD
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
