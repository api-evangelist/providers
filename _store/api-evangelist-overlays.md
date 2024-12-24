---
aid: api-evangelist-overlays
url: https://github.com/api-evangelist/overlays/blob/main/apis.yml
apis:
  - aid: api-evangelist-overlays:overlays
    name: API Evangelist Overlays API
    tags:
      - Overlays
    image: >-
      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    baseURL: https://overlays-api.api-evangelist.com/
    contact:
      - FN: APIs.io
        email: info@apievangelist.com
    humanURL: https://developer.apievangelist.com/overlays/
    properties:
      - url: https://github.com/api-evangelist/overlays
        type: GitHubRepository
      - url: >-
          https://github.com/api-evangelist/overlays/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apievangelist.com/documentation/
        type: Documentation
      - url: https://github.com/api-evangelist/overlays/blob/main/openapi.yml
        type: OpenAPI
    description: >-
      This is the API overlay for the API Evangelist overlays API, inventorying
      all of the APIs managed through the platform.
name: API Evangelist Overlays
tags:
  - Overlays
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
  This is the API overlay for the API Evangelist overlays API, documenting the
  overlays that are being applied as part of API operations.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'

---