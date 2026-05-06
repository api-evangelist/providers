---
aid: pantry
name: Pantry
description: Pantry is a free data storage service for developers that focuses on your development time, letting you build awesome things fast. It provides a simple cloud-based JSON data storage API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Storage
  - Developer Tools
  - JSON
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/pantry/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: pantry:pantry
    name: Pantry API
    description: Free cloud-based JSON data storage API for developers. Create a pantry, then store, retrieve, update, and delete JSON baskets within it.
    humanURL: https://getpantry.cloud/
    tags:
      - Data Storage
      - JSON
    properties:
      - type: Documentation
        url: https://getpantry.cloud/
      - type: Getting Started
        url: https://getpantry.cloud/
      - type: OpenAPI
        url: openapi/pantry-openapi.yml
      - type: JSONSchema
        url: json-schema/pantry.json
      - type: JSONSchema
        url: json-schema/basket.json
      - type: JSONLD
        url: json-ld/pantry-context.jsonld
common:
  - type: Website
    url: https://getpantry.cloud/
  - type: Documentation
    url: https://getpantry.cloud/
  - type: SourceCode
    url: https://github.com/imRohan/Pantry
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
