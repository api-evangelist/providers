---
aid: tesla
name: Tesla
description: Tesla, Inc. is an American electric vehicle and clean energy company founded in 2003. Tesla offers the Fleet API for partners to access Tesla vehicles and energy devices with owner-granted permissions, covering vehicle telemetry, remote commands, charging management, energy site management, and fleet management capabilities.
type: Index
image: https://www.tesla.com/favicon.ico
tags:
  - Automobiles
  - Cars
  - Vehicles
  - Electric Vehicles
  - Energy
  - Clean Energy
  - IoT
url: https://developer.tesla.com/
created: '2025-02-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tesla:fleet-api
    name: Tesla Fleet API
    description: The Tesla Fleet API is the official partner API providing access to Tesla vehicles and energy devices with owner-granted OAuth permissions. Supports vehicle telemetry, remote vehicle commands, charging management, energy site control, and fleet management for third-party applications.
    humanURL: https://developer.tesla.com/docs/fleet-api
    baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
    tags:
      - Vehicles
      - Telemetry
      - Remote Commands
      - Charging
      - Energy
      - Fleet Management
    properties:
      - url: https://developer.tesla.com/docs/fleet-api
        type: Documentation
      - url: https://developer.tesla.com/docs/fleet-api/endpoints/vehicle-endpoints
        type: Documentation
      - url: https://developer.tesla.com/docs/fleet-api/endpoints/vehicle-commands
        type: Documentation
      - url: https://developer.tesla.com/docs/fleet-api/endpoints/charging-endpoints
        type: Documentation
      - url: https://developer.tesla.com/docs/fleet-api/endpoints/energy
        type: Documentation
      - url: https://developer.tesla.com/docs/fleet-api/authentication/overview
        type: Authentication
      - url: https://developer.tesla.com/docs/fleet-api/billing-and-limits
        type: Billing
      - url: https://raw.githubusercontent.com/api-evangelist/tesla/refs/heads/main/openapi/tesla-openapi-original.yml
        type: OpenAPI
  - aid: tesla:owner-api
    name: Tesla Owner API
    description: The Tesla Owner API (community-documented) provides access to Tesla vehicles via the owner-api.teslamotors.com endpoint. Supports vehicle state retrieval, remote commands, and vehicle management for personal vehicle owners.
    humanURL: https://tesla-api.timdorr.com/
    baseURL: https://owner-api.teslamotors.com/api/1
    tags:
      - Vehicles
      - Owner API
      - Remote Commands
      - Telemetry
    properties:
      - url: https://tesla-api.timdorr.com/
        type: Documentation
      - url: https://github.com/timdorr/tesla-api
        type: Repository
      - url: https://raw.githubusercontent.com/api-evangelist/tesla/refs/heads/main/openapi/tesla-openapi-original.yml
        type: OpenAPI
common:
  - name: Tesla Developer Portal
    url: https://developer.tesla.com/
    type: Portal
  - name: Tesla Fleet API Announcements
    url: https://developer.tesla.com/docs/fleet-api/announcements
    type: Announcements
  - name: Tesla Fleet API FAQ
    url: https://developer.tesla.com/docs/fleet-api/support/faq
    type: FAQ
  - name: Tesla Developer Support
    url: https://developer.tesla.com/docs/fleet-api/support/contact
    type: Contact
  - name: Tesla GitHub Organization
    url: https://github.com/teslamotors
    type: Repository
  - name: Tesla Website
    url: https://www.tesla.com
    type: Website
  - name: TeslaPy SDK
    url: https://github.com/tdorssers/TeslaPy
    type: SDK
  - name: Tesla API Ruby Gem
    url: https://github.com/timdorr/tesla-api
    type: SDK
  - name: Tesla Postman Collection
    url: https://documenter.getpostman.com/view/781424/2s9YRCWB4f
    type: Postman
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
