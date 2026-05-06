---
aid: spaceapi
url: https://raw.githubusercontent.com/api-evangelist/spaceapi/refs/heads/main/apis.yml
name: SpaceAPI
description: SpaceAPI is an open standard for hackerspaces, makerspaces, fablabs, and similar community spaces to publish real-time information about their spaces in a machine-readable JSON format. It provides a central directory (collector) that aggregates endpoints from participating spaces around the world, enabling applications to discover and display space status, location, contact, and operational information.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Co-Working
  - Event Spaces
  - Maker Spaces
  - Hackerspaces
  - Community
  - Open Standard
created: '2024-11-07'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: spaceapi:spaceapi-collector
    name: SpaceAPI Collector
    description: The SpaceAPI Collector is a central directory API that aggregates endpoints from hackerspaces and makerspaces around the world that implement the SpaceAPI standard. It returns a list of all registered spaces with their status endpoint URLs, validity, names, and last-seen timestamps.
    humanURL: https://spaceapi.io
    baseURL: https://collector.spaceapi.io
    tags:
      - Co-Working
      - Maker Spaces
      - Hackerspaces
      - Directory
    properties:
      - url: https://spaceapi.io
        type: Documentation
      - url: https://spaceapi.io/how-to-use/
        type: Getting Started
      - url: https://api.spaceapi.io/openapi.json
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/spaceapi/refs/heads/main/openapi/spaceapi-collector-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/spaceapi/refs/heads/main/rules/spaceapi-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/spaceapi/refs/heads/main/json-schema/spaceapi-directory-entry-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/spaceapi/refs/heads/main/json-structure/spaceapi-directory-entry-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/spaceapi/refs/heads/main/json-ld/spaceapi-context.jsonld
        type: JSONLDContext
      - url: https://raw.githubusercontent.com/api-evangelist/spaceapi/refs/heads/main/vocabulary/spaceapi-vocabulary.yml
        type: Vocabulary
common:
  - type: Website
    url: https://spaceapi.io
  - type: Documentation
    url: https://spaceapi.io/how-to-use/
  - type: GitHub
    url: https://github.com/SpaceApi
  - type: Directory
    url: https://directory.spaceapi.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
