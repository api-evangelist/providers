---
aid: tesla-motors
name: Tesla Motors
description: Tesla, Inc. (formerly Tesla Motors, Inc.) is an American electric vehicle and clean energy company that designs and manufactures electric cars, battery energy storage systems, solar panels, and related products. The Tesla Owner API provides programmatic access to Tesla vehicles for monitoring state, controlling climate, locking/unlocking doors, managing charging, and executing remote commands.
type: Index
image: https://www.tesla.com/favicon.ico
tags:
  - Automobiles
  - Electric Vehicles
  - Cars
  - Smart Vehicles
  - IoT
url: https://raw.githubusercontent.com/api-evangelist/tesla-motors/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tesla-motors:owner-api
    name: Tesla Owner API
    description: The Tesla Owner API (unofficial) provides access to Tesla vehicle telemetry, state data, and remote command capabilities for personal vehicles. Supports vehicle listing, state retrieval (charge, climate, drive, vehicle config), and commands including wake-up, door lock/unlock, climate control, charging, trunk control, and media playback.
    humanURL: https://tesla-api.timdorr.com/
    baseURL: https://owner-api.teslamotors.com
    tags:
      - Vehicles
      - Telemetry
      - Remote Commands
      - Charging
      - Climate Control
    properties:
      - url: https://tesla-api.timdorr.com/
        type: Documentation
      - url: https://github.com/timdorr/tesla-api
        type: Repository
      - url: https://raw.githubusercontent.com/api-evangelist/tesla-motors/refs/heads/main/openapi/tesla-motors-owner-openapi.yml
        type: OpenAPI
common:
  - name: Tesla Developer Portal
    url: https://developer.tesla.com
    type: Portal
  - name: Tesla Fleet API Documentation
    url: https://developer.tesla.com/docs/fleet-api
    type: Documentation
  - name: Tesla Owner API (Unofficial Documentation)
    url: https://tesla-api.timdorr.com/
    type: Documentation
  - name: Tesla Motors GitHub
    url: https://github.com/teslamotors
    type: Repository
  - name: Tesla Website
    url: https://www.tesla.com
    type: Website
  - name: Tesla Developer SDK (Python)
    url: https://github.com/tdorssers/TeslaPy
    type: SDK
  - name: Tesla API Ruby Gem
    url: https://github.com/timdorr/tesla-api
    type: SDK
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
