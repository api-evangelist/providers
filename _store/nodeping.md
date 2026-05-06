---
aid: nodeping
name: NodePing
description: NodePing provides uptime monitoring for websites and services with flat-rate plans that include unlimited international SMS notifications and unlimited users. The REST API exposes accounts, contacts, contact groups, schedules, checks, results, notifications, and probe info.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Monitoring
  - Uptime
  - Notifications
  - SaaS
created: '2025-02-12'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: nodeping:nodeping
    name: NodePing API
    description: Uptime monitoring API for managing checks, contacts, schedules, and retrieving uptime results.
    humanURL: https://nodeping.com/
    baseURL: https://api.nodeping.com/api/1
    tags:
      - Monitoring
      - Uptime
      - Notifications
    properties:
      - type: Documentation
        url: https://nodeping.com/docs-api.html
      - type: Website
        url: https://nodeping.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/openapi/nodeping-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/json-schema/nodeping-check-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/json-ld/nodeping-context.jsonld
common:
  - type: Website
    url: https://nodeping.com/
  - type: Documentation
    url: https://nodeping.com/docs-api.html
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/openapi/nodeping-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/json-schema/nodeping-check-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/json-ld/nodeping-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
