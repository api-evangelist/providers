---
aid: api-evangelist-lifecycles
url: https://github.com/api-evangelist/lifecycles/blob/main/apis.yml
apis:
  - aid: api-evangelist-lifecycles:lifecycles
    name: API Evangelist Lifecycles API
    tags:
      - Lifecycles
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://lifecycles-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/lifecycles/
    properties:
      - url: https://github.com/api-evangelist/lifecycles
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/lifecycles/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/lifecycles/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API lifecycle for the API Evangelist lifecycles API,
      inventorying all of the APIs managed through the platform.
name: API Evangelist Lifecycles
tags:
  - Lifecycles
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
  This is the API lifecycle for the API Evangelist lifecycles API, breaking API
  operations down into stages that can be applied at different times.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'
---