---
aid: api-evangelist-apis
url: https://github.com/api-evangelist/apis/blob/main/apis.yml
apis:
  - aid: api-evangelist-apis:apis
    name: API Evangelist APIs API
    tags:
      - APIs
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://apis-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/apis/
    properties:
      - url: https://github.com/api-evangelist/apis
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/apis/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/apis/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API contract for the API Evangelist apis API, inventorying all
      of the APIs managed through the platform.
name: API Evangelist APIs
tags:
  - APIs
type: Contract
image: >-
  https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
access: 1st-Party
common:
  - url: https://github.com/api-evangelist/
    type: GitHubOrganization
created: '2024-10-14'
modified: '2024-12-14'
position: Producing
description: The APIs for managing API Evangelist.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'
---