---
aid: api-evangelist-blueprints
url: https://github.com/api-evangelist/blueprints/blob/main/apis.yml
apis:
  - aid: api-evangelist-blueprints:blueprints
    name: API Evangelist blueprints API
    tags:
      - blueprints
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://blueprints-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/blueprints/
    properties:
      - url: https://github.com/api-evangelist/blueprints
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/blueprints/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/blueprints/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API blueprint for the API Evangelist blueprints API,
      inventorying all of the APIs managed through the platform.
name: API Evangelist Blueprints
tags:
  - Blueprints
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
description: The API for managing blueprints.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'

---