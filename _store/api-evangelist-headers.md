---
aid: api-evangelist-headers
url: https://github.com/api-evangelist/headers/blob/main/apis.yml
apis:
  - aid: api-evangelist-headers:headers
    name: API Evangelist Headers API
    tags:
      - Headers
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://headers-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/headers/
    properties:
      - url: https://github.com/api-evangelist/headers
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/headers/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/headers/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API header for the API Evangelist headers API, inventorying
      all of the APIs managed through the platform.
name: API Evangelist Headers
tags:
  - Headers
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
  This is the API header for the API Evangelist headers API, inventorying all of
  the HTTP headers that are used as part of the HTTP transport.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'
---