---
aid: race-entry
name: Race Entry
description: This API was designed specifically for the Director software to allow certain timers and directors integration into our Race Entry data with the Director. It provides programmatic access to events, registrations, participants, teams, results, check-in PINs, and club memberships, with temporary key/secret authentication issued via a login endpoint.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Race Timing
  - Race Registration
  - Event Management
  - Race Results
  - Sports
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/race-entry/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: race-entry:race-entry
    name: Race Entry
    description: This API was designed specifically for the Director software to allow certain timers and directors integration into our Race Entry data with the Director.
    humanURL: https://www.raceentry.com/documentation/softwareapi/index
    baseURL: https://www.raceentry.com/softwareapi
    tags:
      - Race Timing
      - Race Registration
      - Event Management
      - Race Results
    properties:
      - type: Documentation
        url: https://www.raceentry.com/documentation/softwareapi/index
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/race-entry/refs/heads/main/openapi/race-entry-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
