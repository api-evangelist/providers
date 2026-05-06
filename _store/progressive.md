---
aid: progressive
name: Progressive
description: The Progressive Corporation is one of the largest providers of car insurance in the United States, also offering personal and commercial auto, home, renters, boat, motorcycle, and other insurance products. Progressive operates a developer portal at developer.progressive.com offering APIs for auto insurance quoting, certificate of insurance generation, and agent portal integrations.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Auto Insurance
  - Commercial Insurance
  - Embedded Insurance
  - Insurance
  - Quoting
url: https://raw.githubusercontent.com/api-evangelist/progressive/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: progressive:auto-quote-api
    name: Progressive Auto Quote API
    tags:
      - Auto Insurance
      - Embedded Insurance
      - Insurance
      - Quoting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.progressive.com
    humanURL: https://developer.progressive.com/s/clautoquoteapidoc
    properties:
      - url: https://developer.progressive.com/s/clautoquoteapidoc
        type: Documentation
      - url: openapi/progressive-auto-quote-api-openapi.yml
        type: OpenAPI
    description: The Progressive Auto Quote API enables partners to embed auto insurance quoting capabilities directly into their applications and platforms. Through the Progressive Developer Portal, partners can access APIs to return estimated auto insurance rates with customizable options including SDK and headless API integration. The API supports both non-production and production environments for testing and live deployments.
  - aid: progressive:certificate-of-insurance-api
    name: Progressive Certificate of Insurance API
    tags:
      - Certificates
      - Commercial Insurance
      - Insurance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.progressive.com
    humanURL: https://developer.progressive.com/s/
    properties:
      - url: https://developer.progressive.com/s/
        type: Documentation
      - url: openapi/progressive-certificate-of-insurance-api-openapi.yml
        type: OpenAPI
    description: The Progressive Certificate of Insurance API provides programmatic access to generate and manage certificates of insurance for commercial policyholders. This API enables partners and agents to automate the certificate issuance process, reducing manual effort and improving turnaround times for proof of insurance documentation.
common:
  - type: Portal
    url: https://developer.progressive.com/s/
  - type: Website
    url: https://www.progressive.com/
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
