---
aid: netlify
url: >-

  https://raw.githubusercontent.com/api-search/infrastructure/main/_apis/netlify/apis.md
apis:
  - aid: netlify:netlify-api
    name: Netlify API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.netlify.com/
    overlays:
      - url: >-

          overlays/https://open-api.netlify.com/6dac5474-6daf-41e6-8a14-6d9bcb8aca52-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://open-api.netlify.com/
        type: Documentation
      - url: openapi/netlify-openapi-original.yml
        type: OpenAPI
    description: |-

      Netlify is a hosting service for the programmable web. It understands your
      documents and provides an API to handle atomic deploys of websites, manage
      form submissions, inject JavaScript snippets, and much more. This is a
      REST-style API that uses JSON for serialization and OAuth 2 for
      authentication.
name: Netlify
tags:
  - Cloud
  - Serverless
  - Websites
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.netlify.com/legal/terms-of-use/
    type: Terms of Service
  - url: https://netlify.com/blog/
    type: Blog
  - url: https://netlify.com/changelog/
    type: Change Log
  - url: https://answers.netlify.com/
    type: Forum
  - url: https://www.netlify.com/support/
    type: Support
  - url: https://www.netlify.com/support/
    type: CLI
  - url: https://www.netlify.com/privacy/
    type: Privacy Policy
  - url: https://app.netlify.com/signup
    type: Sign Up
created: 2023/11/14
modified: '2024-12-15'
position: Consuming
description: |-

  Netlify is a remote-first cloud computing company that offers a development
  platform that includes build, deploy, and serverless backend services for web
  applications and dynamic websites.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---