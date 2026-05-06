---
aid: reuters
name: Reuters
description: Global news organization providing breaking news, business, financial, and multimedia content through wire services, digital platforms, and content APIs serving media organizations worldwide. Reuters Connect Web Services provides a professional REST API for searching and retrieving editorial content including text, images, video, and graphics.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Business
  - Finance
  - Journalism
  - Media
  - News
  - Wire Service
url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: reuters:reuters-connect-api
    name: Reuters Connect API
    description: Professional content delivery platform providing access to news, images, video, and data from Reuters and partner content sources via REST API, powering over 100 customer applications and internal systems. Content is organized into channels by category (TXT, PIX, VID, GFX) and items can be retrieved individually or searched by keyword.
    humanURL: https://www.reutersconnect.com
    tags:
      - Content Delivery
      - Images
      - Media
      - News
      - Search
      - Video
    properties:
      - type: Documentation
        url: https://developers.reutersconnect.com/docs
      - type: Authentication
        url: https://developers.reutersconnect.com/authentication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/openapi/reuters-connect-api-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/json-schema/reuters-channel-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/json-schema/reuters-item-schema.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/json-ld/reuters-context.jsonld
common:
  - type: Documentation
    url: https://developers.reutersconnect.com/docs
  - type: Authentication
    url: https://developers.reutersconnect.com/authentication
  - type: Blog
    url: https://medium.com/tr-labs-ml-engineering-blog
  - type: Support
    url: https://www.reuters.com/info-pages/contact-us/
  - type: TermsOfService
    url: https://www.reuters.com/info-pages/terms-of-use/
  - type: PrivacyPolicy
    url: https://www.thomsonreuters.com/en/privacy-statement.html
  - type: GitHubOrganization
    url: https://github.com/ReutersMedia
  - type: Website
    url: https://www.reuters.com
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/openapi/reuters-connect-api-openapi.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/vocabulary/reuters-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
