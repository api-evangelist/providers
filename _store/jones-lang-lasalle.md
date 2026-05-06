---
aid: jones-lang-lasalle
name: Jones Lang LaSalle
url: https://raw.githubusercontent.com/api-evangelist/jones-lang-lasalle/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commercial Real Estate
  - Facility Management
  - Asset Management
  - Work Orders
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jones-lang-lasalle:corrigo-rest-api
    name: JLL Corrigo Enterprise REST API
    tags:
      - Asset Management
      - Commercial Real Estate
      - Facility Management
      - Work Orders
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://am-ce98c.corrigo.com/api/v1
    humanURL: https://developer.corrigo.com/
    properties:
      - url: https://developer.corrigo.com/
        type: Documentation
      - url: openapi/jones-lang-lasalle-corrigo-rest-api-openapi.yml
        type: OpenAPI
    description: The JLL Corrigo Enterprise REST API provides programmatic access to JLL Technologies' cloud-based facility management platform. The API enables integration with work order management, asset tracking, procurement, billing, and vendor management systems. It supports partner connectivity for data exchange with third-party systems using RESTful endpoints and JSON payloads.
common:
  - type: Website
    url: https://www.jll.com/
  - type: Developer
    url: https://developer.corrigo.com/
description: Jones Lang LaSalle Incorporated (JLL) is a global commercial real estate services company offering investment management, property management, and facility services. Through JLL Technologies (JLLT), the company delivers technology solutions including the Corrigo Enterprise platform for facility management with a REST API enabling integration with work order management, asset tracking, procurement, billing, and vendor management systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
