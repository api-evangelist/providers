---
aid: high-mobility
name: High Mobility
description: High Mobility provides a connected car API platform that enables developers to build apps using real-time data from vehicles. The platform provides access to car data such as location, fuel level, door locks, diagnostics, and other vehicle telemetry data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automotive
  - Connected Cars
  - IoT
  - Vehicle Data
url: https://raw.githubusercontent.com/api-evangelist/high-mobility/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: high-mobility:high-mobility-api
    name: High Mobility Vehicle API
    description: The High Mobility Vehicle API provides access to real-time connected car data including vehicle telemetry, diagnostics, location, fuel levels, door state, and other vehicle capabilities.
    humanURL: https://high-mobility.com/developers/
    baseURL: https://api.high-mobility.com
    tags:
      - Automotive
      - Connected Cars
      - Vehicle Data
    properties:
      - type: Documentation
        url: https://docs.high-mobility.com/
      - type: Getting Started
        url: https://docs.high-mobility.com/docs/getting-started/quickstart.md
      - type: Authentication
        url: https://docs.high-mobility.com/docs/oauth-2.0.md
      - type: OpenAPI
        url: openapi/high-mobility-openapi.yml
      - type: GitHubRepository
        url: https://github.com/highmobility/open-api-specifications
common:
  - type: Portal
    url: https://high-mobility.com/developers/
  - type: Website
    url: https://high-mobility.com/
  - type: Documentation
    url: https://high-mobility.com/learn/documentation/
  - type: Sign Up
    url: https://high-mobility.com/developers/
  - type: GitHub Organization
    url: https://github.com/highmobility
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
