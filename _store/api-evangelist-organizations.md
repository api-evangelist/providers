---
---
aid: api-evangelist-organizations
name: Organizations
type: Template
description: |-
  This is a template APIs.json for a organizations API, to be used in storytelling, training, and knowledge bases.

image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
- Application Programming Interface
- API
- Organizations

created: '2024-12-29'
modified: '2024-12-29'

url: http://example.com/apis.json
specificationVersion: '0.19'
apis:

  - aid: api-evangelist-organizations:organizations-api
    name: Organizations API.
    description: A demo organizations API.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://example.com/apis.yml
    baseURL: http://apis.example.com
    tags:
      - API
      - Application Programming Interface
      - Organizations
    properties:
      - type: Documentation
        url: http://example.com/documentation
      - type: OpenAPI
        url: openapi/organizations-api-openapi.yml
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