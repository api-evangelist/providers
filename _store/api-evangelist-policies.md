---
aid: api-evangelist-policies
url: https://github.com/api-evangelist/policies/blob/main/apis.yml
apis:
  - aid: api-evangelist-policies:policies
    name: API Evangelist policies API
    tags:
      - policies
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://policies-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/policies/
    properties:
      - url: https://github.com/api-evangelist/policies
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/policies/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/policies/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API policy for the API Evangelist policies API, inventorying
      all of the APIs managed through the platform.
name: API Evangelist policies
tags:
  - policies
type: Contract
image: >-
  https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
common:
  - url: https://github.com/api-evangelist/
    type: GitHubOrganization
created: '2024-10-14'
modified: '2024-10-14'
description: >-
  This is the API policy for the API Evangelist policies API, inventorying all
  of the APIs managed through the platform.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'

---