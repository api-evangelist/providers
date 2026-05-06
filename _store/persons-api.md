---
aid: api-evangelist-persons
name: Persons
type: Template
description: This is a template APIs.json for a persons API, to be used in storytelling, training, and knowledge bases.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Programming Interface
  - Persons
created: '2024-12-29'
modified: '2026-04-28'
url: http://example.com/apis.json
specificationVersion: '0.19'
apis:
  - aid: api-evangelist-persons:persons-api
    name: Persons API.
    description: A demo persons API.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://example.com/apis.yml
    baseURL: http://apis.example.com
    tags:
      - Application Programming Interface
      - Persons
    properties:
      - type: Documentation
        url: http://example.com/documentation
      - type: OpenAPI
        url: openapi/persons-api-openapi.yml
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
    email: info@apievangelist.com
---
