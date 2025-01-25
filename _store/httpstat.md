---
aid: httpstat
url: https://raw.githubusercontent.com/api-search/httpstat/refs/heads/main/apis.yml
apis:
  - aid: httpstat:httpstat
    name: httpstat.us API
    tags:
      - HTTP
      - Status Codes
      - Utilities
    humanURL: https://httpstat.us/
    properties:
      - url: https://httpstat.us/
        type: Documentation
      - url: openapi/httpstat.yml
        name: OpenAPI
        type: OpenAPI
      - url: httpstat/collection.bru
        name: Bruno Collection
        type: BrunoCollection
      - url: httpstat/environments/httpstat.bru
        name: Bruno Environment
        type: BrunoEnvironment
    description: |
      A simple service for generating various HTTP status codes.  
      Use this API to test how your scripts handle different HTTP responses.
name: httpstat
tags:
  - Utilities
  - Status Codes
  - HTTP
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-15'
modified: '2024-11-15'
position: Consumer
description: >-
  A super simple service for generating different HTTP codes. Its useful for
  testing how your own scripts deal with varying responses.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---