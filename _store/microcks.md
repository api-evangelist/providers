---
aid: microcks
name: Microcks
description: Microcks is an open source, cloud-native tool for API mocking and testing. It provides a platform for importing API contracts (OpenAPI, AsyncAPI, Postman Collections), generating mock responses, and running test suites. It shortens the feedback loop for API development teams.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/microcks/refs/heads/main/apis.yml
tags:
  - API Testing
  - Cloud Native
  - DevOps
  - Mocking
  - Open Source
created: '2025-01-08'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microcks:microcks-api
    name: Microcks API
    description: The Microcks platform API provides endpoints for managing services, test suites, and mock configurations programmatically. It supports integration into CI/CD pipelines for automated API testing and mocking.
    humanURL: https://microcks.io/
    tags:
      - API Testing
      - Mocking
    properties:
      - type: Documentation
        url: https://microcks.io/documentation/
      - type: Getting Started
        url: https://microcks.io/documentation/getting-started/
      - type: OpenAPI
        url: openapi/microcks-openapi.yml
common:
  - type: Portal
    url: https://microcks.io/
  - type: Documentation
    url: https://microcks.io/documentation/
  - type: GitHub Organization
    url: https://github.com/microcks
  - type: Community
    url: https://microcks.io/community/
  - type: Blog
    url: https://microcks.io/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
