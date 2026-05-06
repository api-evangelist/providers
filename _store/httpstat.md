---
aid: httpstat
name: Httpstat.us
description: httpstat.us is a super simple service for generating different HTTP status codes. It is useful for testing how your own scripts and applications deal with varying HTTP responses, allowing developers to simulate different server response scenarios.
url: https://raw.githubusercontent.com/api-evangelist/httpstat/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - HTTP
  - Status Codes
  - Testing
  - Utilities
created: '2024-11-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: httpstat:httpstat-api
    name: Httpstat.us API
    description: A simple service for generating various HTTP status codes. Use this API to test how your scripts handle different HTTP responses. Returns the specified HTTP status code on every request.
    humanURL: https://httpstat.us/
    baseURL: https://httpstat.us
    tags:
      - HTTP
      - Status Codes
      - Utilities
    properties:
      - type: Documentation
        url: https://httpstat.us/
      - type: OpenAPI
        url: openapi/httpstat-openapi.yml
      - type: Rules
        url: rules/httpstat-rules.yml
common:
  - type: Website
    url: https://httpstat.us/
  - type: Repository
    url: https://github.com/Readify/httpstatus
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
