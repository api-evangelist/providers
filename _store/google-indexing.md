---
aid: google-indexing
name: Google Indexing
description: The Google Indexing API allows site owners to directly notify Google when pages are added or removed. It enables requesting crawling for updated content and notifying of page removals, leading to fresher content in search results. Primarily intended for sites with job postings or livestream structured data.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-indexing/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Crawling
  - Google
  - Indexing
  - Search
  - SEO
  - URLs
apis:
  - name: Google Indexing API
    description: Allows site owners to notify Google directly when pages are updated or removed, enabling faster crawling and fresher search results for job postings and livestream content.
    humanURL: https://developers.google.com/search/apis/indexing-api/v3/quickstart
    baseURL: https://indexing.googleapis.com/v3
    tags:
      - Crawling
      - Indexing
      - URLs
    properties:
      - type: Documentation
        url: https://developers.google.com/search/apis/indexing-api/v3/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://developers.google.com/search/apis/indexing-api/v3/prereqs
      - type: Getting Started
        url: https://developers.google.com/search/apis/indexing-api/v3/quickstart
      - type: JSONSchema
        url: json-schema/UrlNotification.json
      - type: Spectral Rules
        url: rules/google-indexing-spectral-rules.yml
common:
  - type: Portal
    url: https://developers.google.com/search/apis/indexing-api
  - type: Getting Started
    url: https://developers.google.com/search/apis/indexing-api/v3/quickstart
  - type: Documentation
    url: https://developers.google.com/search/apis/indexing-api
  - type: Authentication
    url: https://developers.google.com/search/apis/indexing-api/v3/prereqs
  - type: Terms of Service
    url: https://developers.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://developers.google.com/search/apis/indexing-api/v3/support
  - type: JSON-LD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
