---

name: Pinterest
description: >-
  Pinterest is an American image sharing and social media service designed to
  enable saving and discovery of information like recipes, home, style,
  motivation, and inspiration on the internet using images and, on a smaller
  scale, animated GIFs and videos, in the form of pinboards.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-search/images/main/_apis/pinterest/apis.md
created: 2023/11/23
modified: '2024-07-03'
specificationVersion: '0.18'
tags: []
apis:
  - name: Pinterest API
    description: This is the description of your API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.pinterest.com/
    baseURL: https://api.example.com
    tags: []
    properties:
      - type: Documentation
        url: https://developers.pinterest.com/docs/api/v5/
      - type: OpenAPI
        url: properties/pinterest-openapi-original.yml
    overlays:
      - type: APIs.io Search
        url: >-
          overlays/https://raw.githubusercontent.com/pinterest/api-description/main/v5/openapi.yaml-openapi-search.yml
    aid: pinterest:pinterest-api
common:
  - type: Guidelines
    url: https://www.pinterest.com/_/_/policy/developer-guidelines
  - type: News
    url: https://www.pinterest.com/_/_/newsroom/
  - type: Blog
    url: https://medium.com/pinterest-engineering
  - type: Support
    url: https://help.pinterest.com/contact
  - type: Terms of Service
    url: https://developers.pinterest.com/terms/
  - type: OpenAPI
    url: https://github.com/pinterest/api-description
  - type: GitHub Org
    url: https://github.com/pinterest
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
overlays:
  - type: APIs.io Search
    url: overlays/apis-io-search.yml
  - type: API Evangelist Ratings
    url: overlays/apis-io-search.yml
aid: pinterest

---