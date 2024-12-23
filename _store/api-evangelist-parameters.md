---
aid: api-evangelist-parameters
url: https://github.com/api-evangelist/parameters/blob/main/apis.yml
apis:
  - aid: api-evangelist-parameters:parameters
    name: API Evangelist Parameters API
    tags:
      - Parameters
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://parameters-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/parameters/
    properties:
      - url: https://github.com/api-evangelist/parameters
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/parameters/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/parameters/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API parameter for the API Evangelist parameters API,
      inventorying all of the APIs managed through the platform.
name: API Evangelist Parameters
tags:
  - Parameters
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
  This is the API parameter for the API Evangelist parameters API, documenting
  all of the parameters in use across different public APIs.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'
---