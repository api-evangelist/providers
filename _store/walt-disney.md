---
aid: walt-disney
url: https://raw.githubusercontent.com/api-evangelist/walt-disney/refs/heads/main/apis.yml
modified: '2026-05-03'
created: '2026-03-21'
name: Walt Disney
tags:
  - Entertainment
  - Media
  - Streaming
  - Parks
  - Content
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
description: The Walt Disney Company is a leading diversified international family entertainment and media enterprise with operations across media networks, parks and resorts, studio entertainment, and direct-to-consumer streaming. Disney's developer APIs and open source projects enable partners and developers to integrate Disney content, characters, and experiences into their applications.
apis:
  - aid: walt-disney:disney-characters-api
    name: Disney Characters API
    tags:
      - Characters
      - Content
      - Entertainment
      - Films
      - Parks
      - Television
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.disneyapi.dev
    humanURL: https://disneyapi.dev/
    properties:
      - url: https://disneyapi.dev/docs/
        type: Documentation
      - url: openapi/walt-disney-disney-api-openapi.yml
        type: OpenAPI
      - url: rules/walt-disney-rules.yml
        type: SpectralRules
      - url: capabilities/disney-content-discovery.yaml
        type: NaftikoCapabilities
      - url: json-schema/walt-disney-character-schema.json
        type: JSONSchema
      - url: json-ld/walt-disney-context.jsonld
        type: JSONLDContext
      - url: vocabulary/walt-disney-vocabulary.yml
        type: Vocabulary
    description: The Disney Characters API provides REST and GraphQL interfaces to a comprehensive database of 9,820+ Disney characters across all Disney brands including Walt Disney Animation, Pixar, Marvel, Star Wars, and National Geographic. Each character includes associated films, short films, TV shows, video games, park attractions, and character relationships. The API requires no authentication and is freely accessible.
common:
  - url: https://www.disney.com/
    name: Walt Disney Company
    type: Website
  - url: https://disneyapi.dev/
    name: Disney Characters API
    type: Portal
  - url: https://disneyapi.dev/docs/
    name: Disney API Documentation
    type: Documentation
  - url: https://disney.github.io/
    name: Disney Open Source
    type: GitHubOrganization
  - url: https://github.com/disney
    name: Disney GitHub Organization
    type: GitHubOrganization
  - url: https://github.com/disneystreaming
    name: Disney Streaming GitHub Organization
    type: GitHubOrganization
  - url: https://medium.com/disney-streaming
    name: Disney Streaming Engineering Blog
    type: Blog
  - url: https://developer.disney.com/
    name: Disney Developer Portal
    type: Portal
features:
  - Disney Character Database (9,820+ characters)
  - REST API (no authentication required)
  - GraphQL API
  - Character-to-media cross-references (films, TV, games, parks)
  - Character relationship mapping (allies, enemies)
  - Pagination support
  - Disney Parks Attraction Data
openSource:
  - name: Quanta
    description: Roaring bitmap-based HTAP database engine
    url: https://github.com/disney/quanta
  - name: Automated Cloud Advisor
    description: AWS cost optimization tool
    url: https://github.com/disneystreaming/automated-cloud-advisor
  - name: Groovity
    description: Modular scripting language for REST APIs
    url: https://github.com/disney/groovity
  - name: MaterialX
    description: Open standard for material and look-development content
    url: https://github.com/materialx/MaterialX
  - name: Universal Scene Description (USD)
    description: Software for robust 3D scene interchange
    url: https://github.com/PixarAnimationStudios/USD
  - name: OpenSubdiv
    description: High-performance subdivision surface evaluation
    url: https://github.com/PixarAnimationStudios/OpenSubdiv
  - name: OpenEXR
    description: High dynamic-range image file format
    url: https://github.com/openexr/openexr
  - name: weaver-test
    description: Scala test framework for Cats-Effect
    url: https://github.com/disneystreaming/weaver-test
solutions:
  - Entertainment Content APIs
  - Character Data
  - Media Metadata
  - Open Source Graphics Standards
  - Cloud Infrastructure Tools
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
