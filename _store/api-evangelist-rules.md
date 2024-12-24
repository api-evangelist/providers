---
aid: api-evangelist-rules
url: https://github.com/api-evangelist/rules/blob/main/apis.yml
apis:
  - aid: api-evangelist-rules:rules
    name: API Evangelist Rules API
    tags:
      - Rules
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://rules-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/rules/
    properties:
      - url: https://github.com/api-evangelist/rules
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/rules/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/rules/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API rule for the API Evangelist rules API, inventorying all of
      the APIs managed through the platform.
name: API Evangelist Rules
tags:
  - Rules
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
  This is the API rule for the API Evangelist rules API, defining the
  machine-readable rules that are applied to identify patterns and anti-patterns
  in use across APis.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'

---