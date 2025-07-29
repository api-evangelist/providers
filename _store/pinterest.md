---
aid: pinterest
url: >-
  https://raw.githubusercontent.com/api-search/images/main/_apis/pinterest/apis.md
apis:
  - aid: pinterest:pinterest-api
    name: Pinterest API
    tags:
      - Images
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.pinterest.com/
    overlays:
      - url: >-

          overlays/https://raw.githubusercontent.com/pinterest/api-description/main/v5/openapi.yaml-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.pinterest.com/docs/api/v5/
        type: Documentation
      - url: properties/pinterest-api-openapi.yml
        type: OpenAPI
    description: This is the description of your API.
name: Pinterest
tags:
  - Images
  - Social Media
  - Videos
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.pinterest.com/_/_/policy/developer-guidelines
    type: Guidelines
  - url: https://www.pinterest.com/_/_/newsroom/
    type: News
  - url: https://medium.com/pinterest-engineering
    type: Blog
  - url: https://help.pinterest.com/contact
    type: Support
  - url: https://developers.pinterest.com/terms/
    type: Terms of Service
  - url: https://github.com/pinterest/api-description
    type: OpenAPI
  - url: https://github.com/pinterest
    type: GitHub Org
  - url: properties/api-description
    name: OpenAPI
    type: OpenAPI
created: 2023/11/23
modified: '2025-07-29'
position: Consuming
description: |-

  Pinterest is an American image sharing and social media service designed to
  enable saving and discovery of information like recipes, home, style,
  motivation, and inspiration on the internet using images and, on a smaller
  scale, animated GIFs and videos, in the form of pinboards.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---