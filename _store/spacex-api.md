---
aid: spacex-api
url: https://raw.githubusercontent.com/api-evangelist/spacex-api/refs/heads/main/apis.yml
name: SpaceX API
description: The SpaceX API is an open-source REST API providing comprehensive data about SpaceX missions, rockets, capsules, cores, crew, launchpads, landing pads, payloads, and the Starlink satellite constellation. It offers endpoints for all past and upcoming launches, real-time mission data, and vehicle telemetry. No authentication is required.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Space
  - Aerospace
  - Launches
  - SpaceX
created: '2024-11-07'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: spacex-api:spacex-api
    name: SpaceX API
    description: Open-source REST API providing data on SpaceX launches, rockets, capsules, cores, crew, launchpads, landing pads, payloads, ships, and Starlink satellites. Supports query, pagination, and population of linked entity IDs. No authentication required.
    humanURL: https://github.com/r-spacex/SpaceX-API
    baseURL: https://api.spacexdata.com/v5
    tags:
      - Space
      - Aerospace
      - Launches
      - SpaceX
    properties:
      - url: https://github.com/r-spacex/SpaceX-API
        type: GitHubRepository
      - url: https://raw.githubusercontent.com/api-evangelist/spacex-api/refs/heads/main/openapi/spacex-api-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/spacex-api/refs/heads/main/rules/spacex-api-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/spacex-api/refs/heads/main/json-schema/spacex-api-launch-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/spacex-api/refs/heads/main/json-structure/spacex-api-launch-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/spacex-api/refs/heads/main/json-ld/spacex-api-context.jsonld
        type: JSONLDContext
      - url: https://raw.githubusercontent.com/api-evangelist/spacex-api/refs/heads/main/vocabulary/spacex-api-vocabulary.yml
        type: Vocabulary
common:
  - type: Website
    url: https://www.spacex.com
  - type: GitHub
    url: https://github.com/r-spacex/SpaceX-API
  - type: Documentation
    url: https://github.com/r-spacex/SpaceX-API/blob/master/docs/v5/README.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
