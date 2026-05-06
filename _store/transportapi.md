---
aid: transportapi
name: TransportAPI
description: TransportAPI is a managed data service provider for UK public transport, offering real-time and scheduled bus, rail, and multimodal transport data via REST and WebSocket APIs to power apps, websites, analytics, and data-mining workflows.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Public Transit
  - Transport
  - UK
  - Real-Time
  - Journey Planning
  - Bus
  - Rail
created: '2025-05-02'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/transportapi/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: transportapi:transportapi
    name: TransportAPI
    description: UK public transport data API providing real-time bus and rail departures, multimodal journey planning, bus and rail performance analytics, and transport places lookup across Great Britain.
    humanURL: https://developer.transportapi.com/
    baseURL: https://transportapi.com/v3/uk
    tags:
      - Public Transit
      - Transport
      - UK
      - Real-Time
      - Journey Planning
      - Bus
      - Rail
    properties:
      - type: Documentation
        url: https://developer.transportapi.com/docs/
      - type: OpenAPI
        url: openapi/transportapi-openapi.yml
      - type: JSONStructure
        url: json-structure/transportapi-departure-structure.json
      - type: JSONLD
        url: json-ld/transportapi-context.jsonld
      - type: SpectralRules
        url: rules/transportapi-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/uk-transport-information.yaml
      - type: Vocabulary
        url: vocabulary/transportapi-vocabulary.yml
      - type: Sign Up
        url: https://developer.transportapi.com/
    x-services:
      - TAPI Journey Planner
      - TAPI Bus Information
      - TAPI Bus Performance
      - TAPI Rail Information
      - TAPI Rail Performance
      - TAPI Places
    x-authentication:
      type: API Key
      description: app_id and app_key query parameters or X-App-Id and X-App-Key HTTP headers
    x-pricing:
      free: 30 hits per day forever
      paid: Higher allowance tiers via subscription
common:
  - type: Website
    url: https://www.transportapi.com/
  - type: Documentation
    url: https://developer.transportapi.com/
  - type: Sign Up
    url: https://developer.transportapi.com/
  - type: GitHub
    url: https://github.com/transportapi
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
