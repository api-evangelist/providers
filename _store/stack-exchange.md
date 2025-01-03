---
aid: stack-exchange
url: >-
  https://raw.githubusercontent.com/api-search/code/main/_apis/stack-exchange/apis.md
apis:
  - aid: stack-exchange:stack-exchange-api
    name: Stack Exchange API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    contact:
      - FN: Stack Exchange
        url: http://stackapps.com/
        email: team+api@stackexchange.com
    humanURL: https://api.stackexchange.com/
    properties:
      - url: https://api.stackexchange.com/docs
        type: Documentation
      - url: openapi/stack-exchange-openapi-original.yml
        type: OpenAPI
    description: >-
      This is the documentation for the v2.3 Stack Exchange API (with both
      authentication and write support). If you have additional questions, or
      believe you have encountered a bug, don't hesitate to post a question on
      Stack Apps.
name: Stack Exchange
tags:
  - Code
  - Questions
  - Answers
  - Q&A
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://api.stackexchange.com/docs/authentication
    type: Authentication
  - url: https://stackoverflow.blog/
    type: Blog
  - url: https://stackexchange.com/legal/api-terms-of-use
    type: Terms of Service
  - url: https://api.stackexchange.com/docs/throttle
    type: Rate Limits
  - url: http://stackapps.com/apps/oauth/register
    type: Sign UP
  - url: http://stackapps.com/apps/oauth
    type: Applications
created: 2023/11/15
modified: '2024-12-13'
position: Consuming
description: >-
  Stack Exchange is a network of question-and-answer websites on topics in
  diverse fields, each site covering a specific topic, where questions, answers,
  and users are subject to a reputation award process. The reputation system
  allows the sites to be self-moderating
maintainers:
  - FN: Name
    url: http://example.com
    email: info@example.com
specificationVersion: '0.16'

---