---
aid: the-news-api
name: The News API
description: The News API provides free access to search worldwide news and top stories from over 40,000 sources in 50 countries. Access live and historical news articles with advanced filtering by keyword, category, language, country, domain, and date. The API supports boolean search operators, pagination, and returns structured article data including headlines, descriptions, images, and category classifications.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Articles
  - Headlines
  - News
  - Media
  - Search
  - International
created: '2025-02-09'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/the-news-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: the-news-api:the-news-api
    name: The News API
    description: Get free access to search worldwide news and top stories from over 40,000 sources in 50 countries. Access live and historical articles with filters for keyword, category, language, locale, domain, and publication date.
    humanURL: https://www.thenewsapi.com/
    baseURL: https://api.thenewsapi.com/v1
    tags:
      - Articles
      - Headlines
      - News
      - Search
      - International
    properties:
      - type: Documentation
        url: https://www.thenewsapi.com/documentation
      - type: Sign Up
        url: https://www.thenewsapi.com/register
      - type: Authentication
        url: https://www.thenewsapi.com/documentation#auth
      - type: OpenAPI
        url: openapi/the-news-api-openapi.yml
common:
  - type: Website
    url: https://www.thenewsapi.com/
  - type: Documentation
    url: https://www.thenewsapi.com/documentation
  - type: Sign Up
    url: https://www.thenewsapi.com/register
  - type: Pricing
    url: https://www.thenewsapi.com/pricing
  - type: SpectralRuleset
    url: rules/the-news-api-rules.yml
  - type: NaftikoCapability
    url: capabilities/news-monitoring.yaml
  - type: JSONSchema
    url: json-schema/the-news-api-article-schema.json
  - type: JSONLDContext
    url: json-ld/the-news-api-context.jsonld
  - type: Vocabulary
    url: vocabulary/the-news-api-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
