---
aid: api-evangelist-policies

specificationVersion: '0.18'

type: Contract

name: API Evangelist policies

description: >-

  This is the API policy for the API Evangelist policies API, inventorying all

  of the APIs managed through the platform.

image: >-

  https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png

tags:

  - policies

created: '2024-10-14'

modified: '2024-10-14'

url: https://github.com/api-evangelist/policies/blob/main/apis.yml

apis:

  - aid: api-evangelist-policies:policies

    name: API Evangelist policies API

    description: >-

      This is the API policy for the API Evangelist policies API, inventorying

      all of the APIs managed through the platform.

    image: >-

      https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png

    humanURL: https://developer.apievangelist.com/policies/

    baseURL: https://policies-api.api-evangelist.com/

    tags:

      - policies

    properties:

      - type: GitHubRepository

        url: https://github.com/api-evangelist/policies

      - type: GitHubActions

        url: >-

          https://github.com/api-evangelist/policies/blob/main/.github/workflows/pipeline.yml

      - type: Documentation

        url: https://developer.apievangelist.com/documentation/

      - type: OpenAPI

        url: https://github.com/api-evangelist/policies/blob/main/openapi.yml

    contact:

      - FN: APIs.io

        email: info@apievangelist.com

common:

  - type: GitHubOrganization

    url: https://github.com/api-evangelist/

maintainers:

  - FN: Kin Lane

    email: info@apievangelist.com

    X-github: kinlane

---