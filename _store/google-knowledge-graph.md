---
aid: google-knowledge-graph
name: Google Knowledge Graph Search
description: The Google Knowledge Graph Search API allows developers to search for entities (people, places, things) in the Google Knowledge Graph and retrieve structured data about them in JSON-LD format conforming to schema.org standards. Results include names, descriptions, images, and detailed descriptions with relevance scoring.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-knowledge-graph/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Entities
  - Google
  - Knowledge Graph
  - Linked Data
  - Schema.org
  - Semantic Search
apis:
  - name: Google Knowledge Graph Search API
    description: Search for entities in the Google Knowledge Graph and retrieve structured data in JSON-LD format, including names, descriptions, images, types, and relevance scores.
    humanURL: https://developers.google.com/knowledge-graph
    baseURL: https://kgsearch.googleapis.com/v1
    tags:
      - Entities
      - Knowledge Graph
      - Search
    properties:
      - type: Documentation
        url: https://developers.google.com/knowledge-graph/reference/rest/v1
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://developers.google.com/knowledge-graph/how-tos/authorizing
      - type: Getting Started
        url: https://developers.google.com/knowledge-graph/how-tos/search-widget
      - type: JSONSchema
        url: json-schema/Entity.json
      - type: Spectral Rules
        url: rules/google-knowledge-graph-spectral-rules.yml
common:
  - type: Portal
    url: https://developers.google.com/knowledge-graph
  - type: Getting Started
    url: https://developers.google.com/knowledge-graph/how-tos/search-widget
  - type: Documentation
    url: https://developers.google.com/knowledge-graph
  - type: Authentication
    url: https://developers.google.com/knowledge-graph/how-tos/authorizing
  - type: Terms of Service
    url: https://developers.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://developers.google.com/knowledge-graph/support
  - type: JSON-LD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
