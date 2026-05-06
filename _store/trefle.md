---
aid: trefle
name: Trefle
description: An open, freely accessible botanical data source and REST API for plant information covering over 400,000 plant species with taxonomy, morphology, growth requirements, and geographic distributions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agriculture
  - Botany
  - Open Data
  - Plants
  - Science
created: '2025-02-24'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/trefle/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: trefle:trefle
    name: Trefle API
    description: An open, freely accessible botanical data source and REST API for plant information with taxonomy, species, distributions, and growth data.
    humanURL: https://trefle.io/
    baseURL: https://trefle.io/api/v1
    tags:
      - Botany
      - Open Data
      - Plants
      - Science
    properties:
      - type: Documentation
        url: https://docs.trefle.io/
      - type: Getting Started
        url: https://docs.trefle.io/docs/guides/getting-started
      - type: OpenAPI
        url: openapi/trefle-openapi.yml
      - type: JSONSchema
        url: json-schema/trefle-plant-schema.json
      - type: JSONSchema
        url: json-schema/trefle-species-schema.json
      - type: JSONLD
        url: json-ld/trefle-context.jsonld
      - type: JSONStructure
        url: json-structure/trefle-species-structure.json
      - type: Example
        url: examples/trefle-search-plants-example.json
      - type: Example
        url: examples/trefle-get-species-example.json
      - type: SpectralRuleset
        url: rules/trefle-rules.yml
      - type: NaftikoCapability
        url: capabilities/shared/trefle-api.yaml
common:
  - type: Website
    url: https://trefle.io/
  - type: Documentation
    url: https://docs.trefle.io/
  - type: Sign Up
    url: https://trefle.io/users/sign_in
  - type: GitHub
    url: https://github.com/treflehq
  - type: NaftikoCapability
    url: capabilities/botanical-data.yaml
  - type: Vocabulary
    url: vocabulary/trefle-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
