---
aid: upkeep
name: UpKeep
description: UpKeep is an asset operations management and CMMS (Computerized Maintenance Management System) platform for maintenance teams and facility managers. The UpKeep API provides programmatic access to work orders, assets, locations, preventive maintenance schedules, parts inventory, purchase orders, meters, requests, and webhooks.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CMMS
  - Maintenance Management
  - Asset Management
  - Facility Management
  - Work Orders
created: '2025-02-12'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/upkeep/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: upkeep:upkeep
    name: UpKeep API
    description: The UpKeep API provides programmatic access to the UpKeep CMMS platform, enabling management of work orders, assets, locations, preventive maintenance schedules, parts inventory, purchase orders, meters, and maintenance requests. Uses session token authentication with version 2022-09-14.
    humanURL: https://developers.onupkeep.com/
    baseURL: https://api.onupkeep.com/api/v2
    tags:
      - CMMS
      - Maintenance Management
      - Asset Management
      - Work Orders
      - Preventive Maintenance
    properties:
      - type: Documentation
        url: https://developers.onupkeep.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/upkeep/refs/heads/main/openapi/upkeep-openapi.yml
common:
  - type: Website
    url: https://upkeep.com
  - type: Developer Documentation
    url: https://developers.onupkeep.com/
  - type: REST API Integration
    url: https://upkeep.com/integrations/rest-api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
