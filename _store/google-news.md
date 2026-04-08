---
aid: google-news
url: https://raw.githubusercontent.com/api-evangelist/google-news/refs/heads/main/apis.yml
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
name: Google News RSS
tags:
- Aggregation
- Google News
- Headlines
- Media
- News
- RSS
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google News provides RSS feeds that deliver news headlines organized by topic, location, and search query. The feeds expose structured XML data that can be consumed programmatically to retrieve top stories, topic-based headlines (World, Business, Technology, Sports, etc.), location-specific news, and keyword search results across multiple languages and regions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

