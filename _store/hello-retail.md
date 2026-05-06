---
aid: hello-retail
name: Hello Retail
description: Hello Retail is a personalization and product recommendation platform for e-commerce. It provides a REST API and JavaScript SDK for integrating personalized product recommendations, search, and behavioral tracking into retail websites.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - E-Commerce
  - Personalization
  - Product Recommendations
  - Retail
url: https://raw.githubusercontent.com/api-evangelist/hello-retail/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hello-retail:hello-retail-api
    name: Hello Retail API
    description: Hello Retail provides a REST API for personalized product recommendations, on-site search, page-driven product listings, and customer bias retrieval. The helloretail.js script wraps the API as an easy-to-use JavaScript SDK for use directly on retail websites.
    humanURL: https://developer.helloretail.com/sdk/
    baseURL: https://core.helloretail.com
    tags:
      - E-Commerce
      - Personalization
      - REST
    properties:
      - type: Documentation
        url: https://developer.helloretail.com/sdk/
      - type: Getting Started
        url: https://developer.helloretail.com/getting-started/
      - type: Authentication
        url: https://developer.helloretail.com/authentication/
      - type: OpenAPI
        url: openapi/hello-retail-openapi.yml
common:
  - type: Portal
    url: https://developer.helloretail.com/
  - type: Website
    url: https://www.helloretail.com/
  - type: Sign Up
    url: https://app.helloretail.com/signup
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
