---
aid: james-webb-space-telescope-api
name: James Webb Space Telescope API
description: A free, third-party API for accessing James Webb Space Telescope data sourced from the Mikulski Archive for Space Telescopes (MAST). The API provides access to JWST images, observations, and data filterable by program, type, and other parameters. It is built by an independent engineer (not an official NASA, ESA, or CSA service) and data is available under CC-BY 4.0. Authentication is via API key obtained at signup.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Astronomy
  - JWST
  - NASA
  - Science
  - Space
url: https://raw.githubusercontent.com/api-evangelist/james-webb-space-telescope-api/refs/heads/main/apis.yml
created: '2024-11-07'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: james-webb-space-telescope-api:james-webb-space-telescope-api
    name: James Webb Space Telescope API
    description: Programmatic access to JWST images and observations sourced from the MAST archive. Filter and query by program, observation type, and other attributes. Requires an API key obtained via signup at jwstapi.com.
    humanURL: https://jwstapi.com
    baseURL: https://api.jwstapi.com
    tags:
      - Astronomy
      - JWST
      - Science
      - Space
    properties:
      - type: Documentation
        url: https://jwstapi.com
      - type: SignUp
        url: https://jwstapi.com
common:
  - type: Website
    url: https://jwstapi.com
  - type: TermsOfService
    name: License
    description: Data available under CC-BY 4.0.
    url: https://creativecommons.org/licenses/by/4.0/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
