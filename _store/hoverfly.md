---
aid: hoverfly
name: Hoverfly
description: Hoverfly is an open source API simulation tool for creating realistic mock services and capturing-replaying HTTP traffic for testing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Mocking
  - Testing
url: https://raw.githubusercontent.com/api-evangelist/hoverfly/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hoverfly:hoverfly-admin-api
    name: Hoverfly Admin API
    description: The Hoverfly Admin API provides programmatic control of a Hoverfly instance, including simulation management, mode and middleware configuration, journal and diff inspection, state management, caching, logging, templating data sources, and post-serve actions.
    humanURL: https://docs.hoverfly.io/en/latest/pages/reference/api/api.html
    baseURL: http://localhost:8888
    tags:
      - Mocking
      - Simulation
      - Testing
    properties:
      - type: Documentation
        url: https://docs.hoverfly.io
      - type: APIReference
        url: https://docs.hoverfly.io/en/latest/pages/reference/api/api.html
      - type: SourceCode
        url: https://github.com/SpectoLabs/hoverfly
      - type: OpenAPI
        url: openapi/hoverfly-openapi.yml
common:
  - type: Website
    url: https://hoverfly.io
  - type: Documentation
    url: https://docs.hoverfly.io
  - type: SourceCode
    url: https://github.com/SpectoLabs/hoverfly
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
