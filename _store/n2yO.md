---
aid: n2yo
name: N2YO
description: N2YO.com is a website that provides real-time tracking and information about satellites and space stations using space surveillance data from Space Track, operated by the US Air Force Space Command.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.n2yo.com/
created: '2024-03-30'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Satellites
  - Space
  - Tracking
apis:
  - aid: n2yo:n2yo-api
    name: N2YO.com API
    description: The purpose of the API is to provide data for software/web developers to build satellite tracking or prediction applications. The REST API v1 is free but it is transaction limited.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.n2yo.com/api/
    baseURL: https://api.n2yo.com/rest/v1/satellite
    tags:
      - Satellites
      - Space
      - Tracking
    properties:
      - type: Documentation
        url: https://www.n2yo.com/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/n2yo/main/openapi/n2yo-openapi.yml
      - type: SignUp
        url: https://www.n2yo.com/login/register/
      - type: Login
        url: https://www.n2yo.com/login/
    contact:
      - FN: N2YO Support
        url: https://www.n2yo.com/contact/
common:
  - type: Website
    url: https://www.n2yo.com/
  - type: SignUp
    url: https://www.n2yo.com/login/register/
  - type: Login
    url: https://www.n2yo.com/login/
  - type: Contact
    url: https://www.n2yo.com/contact/
  - type: Privacy Policy
    url: https://www.n2yo.com/privacy/
  - type: Terms of Service
    url: https://www.n2yo.com/terms/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
