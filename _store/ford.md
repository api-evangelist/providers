---
aid: ford
name: Ford
description: Ford is a multinational automotive company that designs, manufactures, and sells a wide range of vehicles, including cars, trucks, and SUVs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-25'
modified: '2026-04-28'
position: Consumer
tags:
  - Automobiles
  - Cars
  - Vehicles
url: https://raw.githubusercontent.com/api-evangelist/ford/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: ford:fordconnect
    name: FordConnect
    tags: []
    humanURL: https://developer.ford.com/apis/fordconnect
    properties:
      - url: https://developer.ford.com/apis/fordconnect
        type: Documentation
    description: FordConnect allows to send vehicle commands (e.g., lock, unlock, etc.) and request vehicle information (e.g., fuel range, tire pressure, etc.) to Ford and Lincoln vehicles.
  - aid: ford:ford-wltp-emissions
    name: Ford WLTP Emissions
    tags: []
    humanURL: https://developer.ford.com/emissions
    properties:
      - url: https://developer.ford.com/emissions
        type: Documentation
    description: With this API, authorized external parties can retrieve WLTP values based on a specific vehicle configuration.
common:
  - type: Portal
    url: https://developer.ford.com/
  - type: Terms of Service
    url: https://www.ford.com/help/terms/
  - type: Privacy Policy
    url: https://www.ford.com/help/privacy/
  - type: Website
    url: https://www.ford.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
