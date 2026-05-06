---
aid: spaceflight-news-api
url: https://raw.githubusercontent.com/api-evangelist/spaceflight-news-api/refs/heads/main/apis.yml
name: Spaceflight News API
description: The Spaceflight News API (SNAPI) is a free, open REST API that aggregates space-related news, blogs, and reports from over 43 sources including NASA, SpaceX, Reuters, NASASpaceflight, and Spaceflight Now. It provides paginated access to articles, blogs, and reports with integration to Launch Library 2 for linking news to specific launches and events.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - News
  - Space
  - Spaceflight
  - Media
created: '2024-11-07'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: spaceflight-news-api:spaceflight-news-api
    name: Spaceflight News API
    description: REST API providing access to spaceflight news, blogs, and reports aggregated from over 43 sources. Supports pagination, filtering by news site, and linking articles to Launch Library 2 launches and events. No authentication required.
    humanURL: https://www.spaceflightnewsapi.net
    baseURL: https://api.spaceflightnewsapi.net/v4
    tags:
      - News
      - Space
      - Spaceflight
      - Media
    properties:
      - url: https://www.spaceflightnewsapi.net
        type: Documentation
      - url: https://api.spaceflightnewsapi.net/v4/docs/
        type: SwaggerUI
      - url: https://github.com/thespacedevs/spaceflightnewsapi
        type: GitHubRepository
      - url: https://raw.githubusercontent.com/api-evangelist/spaceflight-news-api/refs/heads/main/openapi/spaceflight-news-api-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/spaceflight-news-api/refs/heads/main/rules/spaceflight-news-api-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/spaceflight-news-api/refs/heads/main/json-schema/spaceflight-news-api-article-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/spaceflight-news-api/refs/heads/main/json-structure/spaceflight-news-api-article-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/spaceflight-news-api/refs/heads/main/json-ld/spaceflight-news-api-context.jsonld
        type: JSONLDContext
      - url: https://raw.githubusercontent.com/api-evangelist/spaceflight-news-api/refs/heads/main/vocabulary/spaceflight-news-api-vocabulary.yml
        type: Vocabulary
common:
  - type: Website
    url: https://www.spaceflightnewsapi.net
  - type: Documentation
    url: https://api.spaceflightnewsapi.net/v4/docs/
  - type: GitHub
    url: https://github.com/thespacedevs/spaceflightnewsapi
  - type: Support
    url: https://discord.gg/thespacedevs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
