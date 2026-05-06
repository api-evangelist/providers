---
aid: taddy-api
name: Taddy API
description: Taddy provides a GraphQL-based podcast API giving developers access to over 4 million podcasts and 200 million episodes with real-time search, episode transcripts, webhooks, top charts, and comic book data. Taddy simplifies building podcast applications by aggregating and standardizing RSS feed data at scale with daily updates of 1,000 new podcasts and 50,000 new episodes.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Audio
  - Comics
  - GraphQL
  - Media
  - Podcasts
  - Transcripts
  - Webhooks
created: '2025-05-02'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: taddy-api:taddy-podcast-api
    name: Taddy Podcast API
    description: GraphQL API providing access to over 4 million podcasts and 200 million episodes. Supports podcast and episode search, transcript retrieval with speaker and timecode data, top charts by country, webhooks for real-time updates and brand monitoring, and detailed metadata including genres, persons, chapters, and transcription status.
    humanURL: https://taddy.org/developers/podcast-api
    baseURL: https://api.taddy.org
    tags:
      - Audio
      - Episodes
      - GraphQL
      - Podcasts
      - Search
      - Transcripts
      - Webhooks
    properties:
      - type: Documentation
        url: https://taddy.org/developers/podcast-api
      - type: Getting Started
        url: https://taddy.org/developers/intro-to-taddy-graphql-api
      - type: GraphQL Schema
        url: https://ax0.taddy.org/docs/schema.graphql
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/openapi/taddy-podcast-openapi.yml
  - aid: taddy-api:taddy-comics-api
    name: Taddy Comics API
    description: GraphQL API for accessing comic book series, issues, and creator data from the Taddy comic book database.
    humanURL: https://taddy.org/developers/comics-api
    baseURL: https://api.taddy.org
    tags:
      - Comics
      - GraphQL
      - Media
    properties:
      - type: Documentation
        url: https://taddy.org/developers/comics-api
common:
  - type: Portal
    url: https://taddy.org/developers
  - type: Documentation
    url: https://taddy.org/developers/podcast-api
  - type: Getting Started
    url: https://taddy.org/developers/intro-to-taddy-graphql-api
  - type: Sign Up
    url: https://taddy.org/register
  - type: Website
    url: https://taddy.org/
  - type: Pricing
    url: https://taddy.org/developers#pricing
  - type: GitHub Org
    url: https://github.com/taddyorg
  - type: Example Project
    url: https://github.com/taddyorg/taddy-api-example-project
  - type: Dataset Export
    url: https://github.com/taddyorg/podcast-dataset-export
  - type: Webhooks
    url: https://github.com/taddyorg/webhook-example-taddy
  - type: n8n Integration
    url: https://github.com/taddyorg/podcast-data-n8n-integration
  - type: Zapier Integration
    url: https://github.com/taddyorg/podcast-data-zapier-integration
  - type: JSON Schema
    url: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/json-schema/taddy-podcast-series-schema.json
  - type: JSON Schema
    url: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/json-schema/taddy-podcast-episode-schema.json
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/vocabulary/taddy-api-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
