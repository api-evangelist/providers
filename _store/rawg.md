---
aid: rawg
name: RAWG
description: RAWG is the largest video game database and game discovery service, providing access to more than 350,000 games across 50+ platforms with rich metadata including tags, genres, developers, publishers, creators, release dates, Metacritic ratings, store links, ESRB ratings, average playtime, achievements, screenshots, trailers, and social media data. RAWG offers a free REST API for personal and small commercial use with API key authentication, enabling developers to search and filter games by platform, genre, developer, publisher, tag, release date, and rating. The API also provides endpoints for exploring game series, DLCs, development team members, and visually similar games (enterprise tier). RAWG is used by developers building game discovery apps, recommendation engines, gaming dashboards, and data warehouses.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/rawg/refs/heads/main/apis.yml
tags:
  - Database
  - Entertainment
  - Game Discovery
  - Games
  - Gaming
  - Metadata
  - Video Games
created: '2025-02-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rawg:rawg
    name: RAWG Video Games Database API
    description: The RAWG Video Games Database API provides programmatic access to a catalog of more than 350,000 games across 50+ platforms, including creator roles, individual creators, game developers, game publishers, genres, tags, storefronts, platforms, and detailed game metadata. The API supports pagination, search, and multi-dimensional filtering across dates, platforms, genres, tags, Metacritic scores, and more. All requests require an API key passed as a query parameter.
    humanURL: https://rawg.io/apidocs
    baseURL: https://api.rawg.io/api
    tags:
      - Database
      - Entertainment
      - Game Discovery
      - Games
      - Gaming
      - Metadata
      - Video Games
    properties:
      - type: Documentation
        url: https://rawg.io/apidocs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rawg/refs/heads/main/openapi/rawg-openapi.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/rawg/refs/heads/main/rules/rawg-rules.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/rawg/refs/heads/main/json-schema/rawg-game-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/rawg/refs/heads/main/json-structure/rawg-game-structure.json
      - type: JSONLd
        url: https://raw.githubusercontent.com/api-evangelist/rawg/refs/heads/main/json-ld/rawg-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/rawg/refs/heads/main/vocabulary/rawg-vocabulary.yml
common:
  - type: Website
    url: https://rawg.io
  - type: Documentation
    url: https://rawg.io/apidocs
  - type: SignUp
    url: https://rawg.io/login?forward=developer
  - type: TermsOfService
    url: https://rawg.io/terms
  - type: Blog
    url: https://rawg.io/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
