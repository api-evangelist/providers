---
aid: genius-sports
name: Genius Sports
description: Genius Sports provides APIs to query information regarding matches, players, statistics etc. both past and future across multiple sports including basketball, football (soccer), volleyball, American football, and ice hockey.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports
  - Statistics
  - Live Data
  - Fixtures
created: '2025-03-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/genius-sports/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: genius-sports:rest-api
    name: Genius Sports REST API
    description: Query information regarding matches, players, statistics etc. both past and future. Covers basketball, 3x3, football (soccer), volleyball, American football, and ice hockey.
    humanURL: https://developer.geniussports.com/
    tags:
      - Sports
      - Statistics
    properties:
      - type: Documentation
        url: https://developer.geniussports.com/
  - aid: genius-sports:streaming-api
    name: Genius Sports Streaming API
    description: Delivers event-by-event data and aggregated statistics for matches in progress, supporting live consumption of sporting event data.
    humanURL: https://developer.geniussports.com/
    tags:
      - Sports
      - Statistics
      - Live Data
    properties:
      - type: Documentation
        url: https://developer.geniussports.com/
  - aid: genius-sports:publish-api
    name: Genius Sports Publish API
    description: Enables publishing of real-time event data from sporting events into the Genius Sports warehouse and statistics engine.
    humanURL: https://developer.geniussports.com/
    tags:
      - Sports
      - Live Data
    properties:
      - type: Documentation
        url: https://developer.geniussports.com/
  - aid: genius-sports:livestats-in-arena-feed
    name: Genius Sports LiveStats In-Arena Feed
    description: Live venue data delivered for TV production and consumers covering basketball, football (soccer), and volleyball.
    humanURL: https://developer.geniussports.com/
    tags:
      - Sports
      - Live Data
    properties:
      - type: Documentation
        url: https://developer.geniussports.com/
  - aid: genius-sports:licensing-api
    name: Genius Sports Licensing API
    description: Retrieves matches and options from the Genius Sports licensing server.
    humanURL: https://developer.geniussports.com/
    tags:
      - Sports
      - Licensing
    properties:
      - type: Documentation
        url: https://developer.geniussports.com/
  - aid: genius-sports:fixtures-api-v2
    name: Genius Sports Fixtures API v2
    description: The authoritative data source for pre-match fixtures data. Swagger specifications are available for CI, UAT, and Production environments.
    humanURL: https://developer.geniussports.com/
    tags:
      - Sports
      - Fixtures
    properties:
      - type: Documentation
        url: https://developer.geniussports.com/
  - aid: genius-sports:matching-api-v2
    name: Genius Sports Matching API v2
    description: Enables clients to match their internal data to the existing data in the Genius Sports platform. Swagger specifications are available for CI, UAT, and Production environments.
    humanURL: https://developer.geniussports.com/
    tags:
      - Sports
      - Data Matching
    properties:
      - type: Documentation
        url: https://developer.geniussports.com/
common:
  - type: Website
    url: https://geniussports.com/
  - type: Documentation
    url: https://developer.geniussports.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
