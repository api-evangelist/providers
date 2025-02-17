---
---
aid: api-evangelist-state
name: State of APIs
type: Contract
description: |-
  This is the APIs.json for the API Evangelist State of APis.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
- Application Programming Interface
- API
- State
- Report

created: '2025-02-10'
modified: '2025-02-10'

url: http://example.com/apis.json
specificationVersion: '0.19'
apis:

  - aid: api-evangelist-products:products-api
    name: Products API.
    description: A demo products API.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://example.com/apis.yml
    baseURL: http://apis.example.com
    tags:
      - API
      - Application Programming Interface
      - Products
    properties:
      - type: Documentation
        url: http://example.com/documentation
      - type: OpenAPI
        url: openapi/products-api-openapi.yml
      - type: Authentication
        url: http://example.com/authentication
      - type: GettingStarted
        url: http://example.com/getting-started
      - type: ChangeLog
        url: http://example.com/change-log 
    contact:
      - FN: API Evangelist
        email: info@apievangelist.com

common:

  - type: Website
    url: http://apievangelist.com

maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com---