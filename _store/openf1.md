---
aid: openf1
name: OpenF1
description: OpenF1 is a free and open-source API providing real-time and historical Formula 1 data including car telemetry, lap timings, race control messages, weather, pit stops, team radio, and championship standings.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Formula 1
  - Motorsport
  - Telemetry
  - Real-Time
  - Sports
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openf1/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openf1:openf1
    name: OpenF1 API
    description: OpenF1 is a free and open-source REST API that provides real-time and historical Formula 1 data, including car telemetry at 3.7 Hz, sector and lap timing, race control flags, pit stops, tyre stints, weather, and team radio recordings.
    humanURL: https://openf1.org/
    baseURL: https://api.openf1.org/v1
    tags:
      - Formula 1
      - Telemetry
      - Real-Time
    properties:
      - type: Documentation
        url: https://openf1.org/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openf1/refs/heads/main/openapi/openf1-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/openf1/refs/heads/main/json-schema/openf1-session-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/openf1/refs/heads/main/json-schema/openf1-driver-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/openf1/refs/heads/main/json-schema/openf1-lap-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/openf1/refs/heads/main/json-schema/openf1-cardata-schema.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/openf1/refs/heads/main/json-ld/openf1-context.jsonld
common:
  - type: Documentation
    url: https://openf1.org/
  - type: GitHubRepository
    url: https://github.com/br-g/openf1
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
