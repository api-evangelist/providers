---
aid: google-news
name: Google News RSS
description: Google News provides RSS feeds that deliver news headlines organized by topic, location, and search query. The feeds expose structured XML data that can be consumed programmatically to retrieve top stories, topic-based headlines (World, Business, Technology, Sports, etc.), location-specific news, and keyword search results across multiple languages and regions.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-news/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Aggregation
  - Google News
  - Headlines
  - Media
  - News
  - RSS
apis:
  - name: Google News RSS API
    description: RSS feed endpoints for retrieving Google News headlines by topic, location, and search query across multiple languages and regions.
    humanURL: https://news.google.com
    baseURL: https://news.google.com/rss
    properties:
      - type: Documentation
        url: https://news.google.com/rss/help
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/google-news/refs/heads/main/openapi/openapi.yml
      - type: Getting Started
        url: https://news.google.com
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/google-news/refs/heads/main/json-schema/google-news.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/google-news/refs/heads/main/json-ld/google-news.jsonld
common:
  - type: Portal
    url: https://news.google.com
  - type: Getting Started
    url: https://news.google.com
  - type: Terms of Service
    url: https://policies.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Support
    url: https://support.google.com/news
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/google-news/refs/heads/main/json-ld/google-news.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
