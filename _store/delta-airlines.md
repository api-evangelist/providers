---
aid: delta-airlines
name: Delta Airlines
url: https://raw.githubusercontent.com/api-evangelist/delta-airlines/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Air Travel
  - Airlines
  - Aviation
  - Booking
  - Flights
  - NDC
  - Travel
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
description: Delta Airlines (alias of Delta Air Lines) is a major U.S. airline providing scheduled air transportation for passengers and cargo throughout the United States and across the world. This repository is an alias of the canonical delta-air-lines profile and points to the same partner developer portal at apiportal.delta.com.
apis:
  - aid: delta-airlines:delta-api-suite
    name: Delta API Suite
    description: The Delta API Suite is a partner-facing collection of APIs covering flight search, flight offers and order management, customer journey events, and operational data. Access is restricted to approved partners through Delta's developer portal.
    humanURL: https://apiportal.delta.com
    tags:
      - Flights
      - NDC
      - Offers
      - Orders
      - Travel
    properties:
      - type: Documentation
        url: https://apiportal.delta.com
      - type: SignUp
        url: https://apiportal.delta.com/publish
      - type: Alias
        url: https://github.com/api-evangelist/delta-air-lines
common:
  - type: Website
    url: https://www.delta.com
  - type: Developer Portal
    url: https://apiportal.delta.com
  - type: Canonical
    url: https://github.com/api-evangelist/delta-air-lines
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
