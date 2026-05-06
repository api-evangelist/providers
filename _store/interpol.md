---
aid: interpol
name: Interpol
description: INTERPOL (International Criminal Police Organization) is an inter-governmental organization with 196 member countries that helps police worldwide work together to make the world a safer place. INTERPOL exposes a public Notices web service that returns Red, Yellow, and UN Notices data. An OpenAPI description of that service is published by the bundesAPI community and mirrored in this repository.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - International
  - Law Enforcement
  - Notices
  - Police
url: https://raw.githubusercontent.com/api-evangelist/interpol/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: interpol:interpol-notices-api
    name: Interpol Notices API
    description: The INTERPOL Notices API provides public, unauthenticated access to Red, Yellow, and UN Notices, including notice metadata and associated images. The API is queryable by name, nationality, age range, sex, and issuing country.
    humanURL: https://interpol.api.bund.dev
    baseURL: https://ws-public.interpol.int/notices/v1/
    tags:
      - Law Enforcement
      - Notices
      - International
    properties:
      - type: Documentation
        url: https://interpol.api.bund.dev
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/interpol/refs/heads/main/openapi/interpol-openapi.yml
common:
  - type: Website
    url: https://www.interpol.int/
  - type: Source
    url: https://github.com/bundesAPI/interpol-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
