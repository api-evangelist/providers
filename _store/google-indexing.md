---
aid: google-indexing
url: https://raw.githubusercontent.com/api-evangelist/google-indexing/refs/heads/main/apis.yml
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
name: Google Indexing
tags:
- Crawling
- Google
- Indexing
- Search
- SEO
- URLs
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google Indexing API allows site owners to directly notify Google when pages are added or removed. It enables requesting crawling for updated content and notifying of page removals, leading to fresher content in search results. Primarily intended for sites with job postings or livestream structured data.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

