---
aid: google-knowledge-graph
url: https://raw.githubusercontent.com/api-evangelist/google-knowledge-graph/refs/heads/main/apis.yml
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
name: Google Knowledge Graph Search
tags:
- Entities
- Google
- Knowledge Graph
- Linked Data
- Schema.org
- Semantic Search
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google Knowledge Graph Search API allows developers to search for entities (people, places, things) in the Google Knowledge Graph and retrieve structured data about them in JSON-LD format conforming to schema.org standards. Results include names, descriptions, images, and detailed descriptions with relevance scoring.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

