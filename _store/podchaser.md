---
aid: podchaser
name: Podchaser
description: Podchaser provides one of the most comprehensive podcast databases, exposed through a GraphQL API designed to drive podcast discovery for listeners, podcasters, brands, and platform partners. The API surface is GraphQL-only and is therefore not represented as an OpenAPI specification in this index.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Podcasting
  - Discovery
  - GraphQL
  - Database
created: '2025-05-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/podchaser/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: podchaser:podchaser
    name: Podchaser GraphQL API
    description: Podchaser's GraphQL API provides programmatic access to podcasts, episodes, creators, credits, reviews, and lists across the Podchaser database. Authentication is handled via OAuth-style API tokens and the single endpoint is queried with GraphQL operations.
    humanURL: https://www.podchaser.com/api
    baseURL: https://api.podchaser.com/graphql
    tags:
      - Podcasting
      - GraphQL
      - Discovery
      - Metadata
    properties:
      - type: Documentation
        url: https://api-docs.podchaser.com/
      - type: GraphQLSchema
        url: https://api-docs.podchaser.com/docs/reference/schema
common:
  - type: Website
    url: https://www.podchaser.com/
  - type: Documentation
    url: https://api-docs.podchaser.com/
  - type: APIPortal
    url: https://www.podchaser.com/api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
