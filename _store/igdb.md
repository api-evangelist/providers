---
aid: igdb
name: IGDB
description: IGDB (Internet Game Database) is the world's most comprehensive video game database. The IGDB API provides access to a complete, holistic, accurate, and up-to-date data representation of the video game market, including game products, consumer opinions, and gaming industry information.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Entertainment
  - Game Database
  - Gaming
  - Video Games
created: '2025-02-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/igdb/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: igdb:igdb-api
    name: IGDB API
    description: The IGDB API provides programmatic access to the Internet Game Database, offering data on video games, platforms, companies, genres, release dates, covers, screenshots, and user reviews for thousands of games. Requests are authenticated via Twitch OAuth Client Credentials and use the Apicalypse query language for filtering and field selection.
    humanURL: https://www.igdb.com/api
    baseURL: https://api.igdb.com/v4
    tags:
      - Game Database
      - Gaming
      - Video Games
    properties:
      - type: Documentation
        url: https://api-docs.igdb.com/
      - type: Getting Started
        url: https://api-docs.igdb.com/#getting-started
      - type: Authentication
        url: https://api-docs.igdb.com/#authentication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/igdb/refs/heads/main/openapi/igdb-openapi.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/igdb/refs/heads/main/rules/igdb-rules.yml
    contact:
      - FN: IGDB Support
        url: https://www.igdb.com/contact
common:
  - type: Website
    url: https://www.igdb.com/
  - type: Portal
    url: https://www.igdb.com/api
  - type: Documentation
    url: https://api-docs.igdb.com/
  - type: Support
    url: https://www.igdb.com/contact
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
