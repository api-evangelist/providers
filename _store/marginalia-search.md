---
aid: marginalia-search
name: Marginalia Search
description: Marginalia Search is an independent search engine focused on non-commercial content. Its API is accessible through api2.marginalia-search.com (current) and the legacy api.marginalia.nu / api.marginalia-search.com endpoints, and allows developers to perform web searches against the Marginalia index.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Open Source
  - Search
  - Web Search
url: https://raw.githubusercontent.com/api-evangelist/marginalia-search/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: marginalia-search:marginalia-search-api
    name: Marginalia Search API
    description: The Marginalia Search API provides access to the Marginalia search engine index. The current API is hosted at api2.marginalia-search.com; legacy api.marginalia.nu and api.marginalia-search.com endpoints remain available but are deprecated. All requests authenticate via the API-Key header.
    humanURL: https://about.marginalia-search.com/article/api/
    baseURL: https://api2.marginalia-search.com
    tags:
      - Search
      - Web Search
    properties:
      - type: Documentation
        url: https://about.marginalia-search.com/article/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/marginalia-search/refs/heads/main/openapi/marginalia-search-openapi.yml
common:
  - type: Website
    url: https://marginalia-search.com/
  - type: GitHub Organization
    url: https://github.com/MarginaliaSearch
  - type: Contact
    url: mailto:contact@marginalia-search.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
