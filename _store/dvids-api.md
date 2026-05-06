---
aid: dvids-api
name: DVIDS API
description: The Defense Visual Information Distribution Service (DVIDS) API provides programmatic access to over 1.8 million U.S. military news, photos, video, audio, publications, and unit assets. The API is implemented as JSON over HTTP and integration is possible from any language that can make an HTTP request and parse JSON responses.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Media
  - Defense
  - Government
  - Search
created: '2025-05-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/dvids-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: dvids-api:dvids-api
    name: DVIDS API
    description: JSON-over-HTTP API for searching and retrieving DVIDS news, video, image, audio, publication, webcast, graphics, and unit records.
    humanURL: https://api.dvidshub.net/
    baseURL: https://api.dvidshub.net
    tags:
      - Media
      - Defense
      - Government
      - Search
    properties:
      - type: Documentation
        url: https://api.dvidshub.net/docs
      - type: Asset API
        url: https://api.dvidshub.net/docs/asset_api
      - type: Search API
        url: https://api.dvidshub.net/docs/search_api
      - type: Unit API
        url: https://api.dvidshub.net/docs/unit_api
      - type: OpenAPI
        url: openapi/dvids-api-openapi.yml
common:
  - type: Website
    url: https://www.dvidshub.net
  - type: Documentation
    url: https://api.dvidshub.net/docs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
