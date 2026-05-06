---
aid: dog-api
name: Dog API
description: The internet's biggest collection of open-source dog pictures. Fetching over 20,000 dog images accessible by more than 120 breeds via a free, no-auth REST API returning JSON.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Dogs
  - Images
  - Open Data
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/dog-api/refs/heads/main/apis.yml
created: '2024-11-14'
modified: '2026-04-28'
specificationVersion: '0.19'
access: 3rd-Party
position: Consuming
apis:
  - aid: dog-api:dog-api
    name: Dog API
    description: The Dog API (dog.ceo) is the internet's largest collection of open-source dog pictures, exposing over 20,000 images across 120+ breeds. The API requires no authentication and returns JSON.
    humanURL: https://dog.ceo/dog-api/
    baseURL: https://dog.ceo/api
    tags:
      - Dogs
      - Images
      - Open Data
    properties:
      - type: Documentation
        url: https://dog.ceo/dog-api/documentation
      - type: GitHub
        url: https://github.com/ElliottLandsborough/dog-ceo-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/dog-api/refs/heads/main/openapi/dog-api.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/dog-api/refs/heads/main/capabilities/dog-api.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/dog-api/refs/heads/main/rules/dog-api-rules.yml
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/dog-api/refs/heads/main/json-schema/breed-list-response.json
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/dog-api/refs/heads/main/json-ld/dog-api.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/dog-api/refs/heads/main/vocabulary/dog-api.yml
common:
  - type: Website
    url: https://dog.ceo
  - type: Documentation
    url: https://dog.ceo/dog-api/documentation
  - type: GitHub
    url: https://github.com/ElliottLandsborough/dog-ceo-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
