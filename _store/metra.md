---
aid: metra
name: Metra
description: Metra provides GTFS API data for the Metra commuter rail system in the Chicago metropolitan area. The API is hosted at gtfsapi.metrarail.com and provides both RAW data and JSON for schedules, trips, stops, and real-time updates.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Chicago
  - Commuter Rail
  - GTFS
  - Public Transportation
  - Transit
url: https://raw.githubusercontent.com/api-evangelist/metra/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: metra:metra-gtfs-api
    name: Metra GTFS API
    description: The Metra GTFS API provides both raw data and JSON for Metra commuter rail schedules, trips, stops, and real-time transit information. Developers must redistribute data through their own host and not direct users to access data directly from Metra's servers.
    humanURL: https://metra.com/metra-gtfs-api
    baseURL: https://gtfsapi.metrarail.com
    tags:
      - Commuter Rail
      - GTFS
      - Transit
    properties:
      - type: Documentation
        url: https://metra.com/metra-gtfs-api
common:
  - type: Portal
    url: https://metra.com/metra-gtfs-api
  - type: Website
    url: https://www.metrarail.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
