---
aid: marketo
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/marketo.yml
apis:
  - aid: marketo:marketo-rest-api
    name: Marketo REST API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.marketo.com/rest-api/
    overlays: []
    properties:
      - url: https://developers.marketo.com/rest-api/
        type: Documentation
      - url: >-
          https://developers.marketo.com/rest-api/endpoint-reference/download-swagger-definition/
        type: Swagger
      - url: https://developers.marketo.com/rest-api/authentication/
        type: Authentication
      - url: https://developers.marketo.com/rest-api/error-codes/
        type: Errors
      - url: >-
          https://developers.marketo.com/rest-api/marketo-integration-best-practices/
        type: Best Practices
      - url: https://developers.marketo.com/performance/
        type: Performance
    description: >-
      Marketo exposes a REST API which allows for remote execution of many of
      the system's capabilities.  From creating programs to bulk lead import,
      there are a large number of options which allow fine-grained control of a
      Marketo instance.
name: Marketo
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://developers.marketo.com/
    type: Portal
  - url: https://developers.marketo.com/getting-started/
    type: Getting Started
  - url: https://developers.marketo.com/webhooks/
    type: Webhooks
  - url: https://github.com/Marketo/Community-Supported-Client-Libraries
    type: Libraries
  - url: http://www.marketo.com/company/contact/
    type: Contact
  - url: https://developers.marketo.com/blog/
    type: Blog
  - url: https://www.marketo.com/company/legal/
    type: Terms of Service
  - url: http://legal.marketo.com/privacy/
    type: Privacy
  - url: https://developers.marketo.com/api-license/
    type: License
created: 2023/11/23
modified: 2023/11/23
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
description: >-
  Marketo develops and sells marketing automation software for account-based
  marketing and other marketing services and products, including SEO and content
  creation.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
---