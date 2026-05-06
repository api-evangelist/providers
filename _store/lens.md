---
aid: lens
name: Lens
description: Lens is an open knowledge platform from Cambia that aggregates global scholarly works and patent records and exposes them through a REST API. The versioned API supports rich Elasticsearch-style queries, cursor pagination, and field projection across the full Lens scholarly and patent corpora, enabling research, science policy, technology landscape, and patent intelligence applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Scholarly
  - Patents
  - Research
  - Science
  - Open Data
url: https://raw.githubusercontent.com/api-evangelist/lens/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: lens:lens-api
    name: Lens API
    description: The Lens API exposes the full corpus of Lens scholarly works and patents via a REST interface. Search endpoints accept Elasticsearch-style query DSL via POST or simple Lucene query strings via GET, with cursor-based pagination, field projection, sorting, stemming controls, and patent family grouping. Authentication is via a bearer token issued from the Lens user profile.
    humanURL: https://docs.api.lens.org/
    baseURL: https://api.lens.org
    tags:
      - Scholarly
      - Patents
      - Search
      - Research
    properties:
      - url: https://docs.api.lens.org/
        type: Documentation
      - url: https://api.lens.org/swagger-ui.html
        type: SwaggerUI
      - url: openapi/lens-openapi.yml
        type: OpenAPI
common:
  - url: https://www.lens.org/
    type: Website
  - url: https://docs.api.lens.org/
    type: Documentation
  - url: https://www.lens.org/lens/user/subscriptions
    type: Plans
  - url: https://www.lens.org/lens/about
    type: About
  - url: https://www.lens.org/lens/terms-and-conditions
    type: TermsOfService
  - url: https://www.lens.org/lens/privacy-policy
    type: PrivacyPolicy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
