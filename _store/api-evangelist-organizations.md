---
aid: api-evangelist-organizations
url: https://github.com/api-evangelist/organizations/blob/main/apis.yml
apis:
  - aid: api-evangelist-organizations:organizations
    name: API Evangelist Organizations API
    tags:
      - Organizations
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://organizations-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/organizations/
    properties:
      - url: https://github.com/api-evangelist/organizations
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/organizations/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/organizations/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API organization for the API Evangelist organizations API,
      inventorying all of the APIs managed through the platform.
name: API Evangelist Organizations
tags:
  - Organizations
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
  This is the API organization for the API Evangelist organizations API,
  breaking down all of the GitHub organizations being managed via API
  Evangelist.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'
slug: api-evangelist-organizations
---