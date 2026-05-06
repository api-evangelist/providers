---
aid: ourpeople
name: OurPeople
description: The OurPeople API uses common standards to allow easy read and write access to your data. OurPeople is a frontline communications platform that helps organizations communicate with deskless workers.
url: https://raw.githubusercontent.com/api-evangelist/ourpeople/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
position: Consuming
access: 3rd-Party
tags:
  - Communications
  - Workforce
  - Frontline
created: '2025-02-08'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ourpeople:ourpeople-api
    name: OurPeople API
    description: The OurPeople API uses common standards to allow easy read and write access to your data, with JWT authentication and broadcast delivery tracking endpoints.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.ourpeople.com/
    baseURL: https://example-api.ourpeople.co
    tags:
      - Communications
      - Workforce
      - Broadcasts
      - Authentication
    properties:
      - type: Documentation
        url: https://developer.ourpeople.com/
      - type: Authentication
        url: https://developer.ourpeople.com/docs/api/authentication
      - type: Rate Limits
        url: https://developer.ourpeople.com/docs/api/rate-limits
      - type: OpenAPI
        url: openapi/ourpeople-openapi.yml
    contact:
      - FN: OurPeople Support
        email: support@ourpeople.com
common:
  - type: Portal
    url: https://developer.ourpeople.com/
  - type: Documentation
    url: https://developer.ourpeople.com/
  - type: Website
    url: https://ourpeople.com/
  - type: Support
    url: https://ourpeople.com/support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
