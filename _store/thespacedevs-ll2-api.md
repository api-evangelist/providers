---
aid: thespacedevs-ll2-api
url: https://raw.githubusercontent.com/api-evangelist/thespacedevs-ll2-api/refs/heads/main/apis.yml
apis:
  - aid: thespacedevs-ll2-api:thespacedevs-ll2-api
    name: TheSpaceDevs Launch Library 2 API
    tags:
      - Space
      - Launches
      - Rockets
      - Astronauts
      - Satellites
      - Spacecraft
      - Space Stations
    humanURL: https://thespacedevs.com/llapi
    baseURL: https://ll.thespacedevs.com
    properties:
      - url: https://thespacedevs.com/llapi
        type: Documentation
      - url: openapi/thespacedevs-ll2-api-openapi.yml
        type: OpenAPI
      - url: json-schema/thespacedevs-launch-schema.json
        type: JSONSchema
      - url: json-ld/thespacedevs-context.jsonld
        type: JSONLD
      - url: json-structure/thespacedevs-structure.json
        type: JSONStructure
      - url: rules/thespacedevs-rules.yml
        type: SpectralRules
      - url: capabilities/launch-tracking.yaml
        type: NaftikoCapabilities
      - url: vocabulary/thespacedevs-vocabulary.yml
        type: Vocabulary
    description: The Launch Library 2 API is the official successor of the popular Launch Library API. It provides comprehensive data on rocket launches, space events, crewed spaceflight, astronauts, spacecraft, space stations, and celestial bodies. The API is maintained by TheSpaceDevs community and delivers real-time and historical data on global space missions.
name: TheSpaceDevs LL2 API
tags:
  - Space
  - Satellites
  - Launches
  - Rockets
  - Astronauts
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-07T00:00:00.000Z'
modified: '2026-05-03'
position: Consuming
description: TheSpaceDevs LL2 API is the Launch Library 2, a comprehensive space launch and events database delivering data on rocket launches, space events, astronauts, spacecraft, space stations, and crewed spaceflight missions worldwide. Provides real-time updates on launch schedules, mission timelines, and spacecraft operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: TheSpaceDevs Website
    url: https://thespacedevs.com/
    type: Website
  - name: API Documentation
    url: https://ll.thespacedevs.com/docs/
    type: Documentation
  - name: GitHub Organization
    url: https://github.com/TheSpaceDevs
    type: GitHubOrganization
  - name: Discord Community
    url: https://discord.gg/p7ntkNA
    type: Community
  - name: Patreon
    url: https://www.patreon.com/TheSpaceDevs
    type: Support
---
