---
aid: thesportsdb
name: TheSportsDB
description: An open, crowd-sourced sports database of artwork and metadata with a free sports API in JSON format. TheSportsDB provides data on sports leagues, teams, players, events, venues, and season standings across a wide range of sports worldwide including soccer, basketball, baseball, American football, hockey, tennis, and more.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports
  - Database
  - Free
  - Open Data
  - Teams
  - Players
  - Events
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/thesportsdb/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: thesportsdb:thesportsdb
    name: TheSportsDB API
    description: An open, crowd-sourced sports database of artwork and metadata with a free sports API in JSON format. Provides data on leagues, teams, players, events, venues, and season standings across hundreds of sports worldwide.
    humanURL: https://www.thesportsdb.com/
    baseURL: https://www.thesportsdb.com/api/v1/json/3
    tags:
      - Sports
      - Database
      - Free
      - Teams
      - Players
      - Events
      - Leagues
    properties:
      - type: Documentation
        url: https://www.thesportsdb.com/documentation
      - type: Website
        url: https://www.thesportsdb.com/
      - url: openapi/thesportsdb-openapi.yml
        type: OpenAPI
      - url: json-schema/thesportsdb-team-schema.json
        type: JSONSchema
      - url: json-ld/thesportsdb-context.jsonld
        type: JSONLD
      - url: json-structure/thesportsdb-structure.json
        type: JSONStructure
      - url: rules/thesportsdb-rules.yml
        type: SpectralRules
      - url: capabilities/sports-data.yaml
        type: NaftikoCapabilities
      - url: vocabulary/thesportsdb-vocabulary.yml
        type: Vocabulary
common:
  - type: Website
    url: https://www.thesportsdb.com/
  - type: Documentation
    url: https://www.thesportsdb.com/documentation
  - type: Sign Up
    url: https://www.thesportsdb.com/register
  - type: Pricing
    url: https://www.thesportsdb.com/patreon
  - type: Examples
    url: https://www.thesportsdb.com/docs_api_examples
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
