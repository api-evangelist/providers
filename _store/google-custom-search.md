---
aid: google-custom-search
name: Google Custom Search
description: The Google Custom Search JSON API allows programmatic searches over a website or collection of websites. It returns metadata about the search performed, metadata about the search engine used, and the search results including web pages and images.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-custom-search/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Custom Search
  - Google
  - Image Search
  - Search
  - Web Search
apis:
  - name: Google Custom Search JSON API
    description: Enables programmatic web and image searches over websites or collections of websites using Programmable Search Engines, returning structured search results with metadata.
    humanURL: https://developers.google.com/custom-search/v1/overview
    baseURL: https://customsearch.googleapis.com
    tags:
      - Images
      - Search
      - Web
    properties:
      - type: Documentation
        url: https://developers.google.com/custom-search/v1/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://developers.google.com/custom-search/v1/introduction
      - type: Getting Started
        url: https://developers.google.com/custom-search/v1/overview
      - type: JSONSchema
        url: json-schema/SearchResult.json
common:
  - type: Portal
    url: https://developers.google.com/custom-search
  - type: Getting Started
    url: https://developers.google.com/custom-search/v1/overview
  - type: Documentation
    url: https://developers.google.com/custom-search/v1/overview
  - type: Authentication
    url: https://developers.google.com/custom-search/v1/introduction
  - type: Pricing
    url: https://developers.google.com/custom-search/v1/overview#pricing
  - type: Terms of Service
    url: https://developers.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://developers.google.com/custom-search/v1/overview#support
  - type: JSON-LD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
