---
aid: unsplash
name: Unsplash
description: Unsplash is a platform providing the world's largest collection of high-quality, freely usable photographs. The Unsplash API gives developers programmatic access to search, browse, and retrieve photos, collections, topics, and user profiles. Photos are provided under the Unsplash License. Authentication uses Client-ID for public access or OAuth 2.0 for user-delegated operations.
url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/apis.yml
created: '2024-11-13'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
tags:
  - Photos
  - Images
  - Photography
  - Stock Photos
  - Creative
  - Open Source
  - Media
apis:
  - aid: unsplash:unsplash
    name: Unsplash API
    description: 'REST API providing access to Unsplash''s full photo library with endpoints for photo search, random photos, editorial feed browsing, photo detail and statistics, collection management, topic browsing, and user profiles. Returns JSON responses with multiple photo size URLs (raw, full, regular, small, thumb) via imgix CDN. Rate limit: 50 req/hr (demo), 1000 req/hr (production). Download tracking via /photos/{id}/download is required per Unsplash API guidelines.'
    humanURL: https://unsplash.com/developers
    baseURL: https://api.unsplash.com
    tags:
      - Photos
      - Search
      - Collections
      - Topics
      - Statistics
    properties:
      - type: Documentation
        url: https://unsplash.com/documentation
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/openapi/unsplash-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/rules/unsplash-rules.yml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/capabilities/photo-discovery.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/json-schema/unsplash-photo-schema.json
common:
  - type: Website
    url: https://unsplash.com
  - type: Documentation
    url: https://unsplash.com/documentation
  - type: Developers
    url: https://unsplash.com/developers
  - type: Guidelines
    url: https://help.unsplash.com/en/articles/2511245-unsplash-api-guidelines
  - type: GitHub
    url: https://github.com/unsplash
  - type: Changelog
    url: https://unsplash.com/documentation/changelog
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/vocabulary/unsplash-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/json-ld/unsplash-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
