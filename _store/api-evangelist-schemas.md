---
aid: api-evangelist-schemas
url: https://github.com/api-evangelist/schemas/blob/main/apis.yml
apis:
  - aid: api-evangelist-schemas:schemas
    name: API Evangelist Schemas API
    tags:
      - Schemas
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://schemas-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/schemas/
    properties:
      - url: https://github.com/api-evangelist/schemas
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/schemas/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/schemas/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API schema for the API Evangelist schemas API, inventorying
      all of the APIs managed through the platform.
name: API Evangelist Schemas
tags:
  - Schemas
type: Contract
image: >-
  https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
access: 1st-Party
common:
  - url: https://github.com/api-evangelist/
    type: GitHubOrganization
created: '2024-10-14'
modified: '2024-12-04'
position: Producing
description: >-
  This is the API schema for the API Evangelist schemas API, inventorying all of
  the schema which are applied across the APIs being profiled and reviewed.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'
slug: api-evangelist-schemas
---