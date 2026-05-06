---
aid: apyhub
name: ApyHub
description: ApyHub is an API platform that provides a collection of utility APIs for common development tasks such as document conversion, data processing, image manipulation, currency exchange, and more. It simplifies API development by offering pre-built, ready-to-use API utilities that developers can integrate into their applications quickly.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Platform
  - Data Processing
  - Document Conversion
  - Utility APIs
url: https://raw.githubusercontent.com/api-evangelist/apyhub/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apyhub:apyhub-api
    name: ApyHub API
    tags:
      - Document Conversion
      - PDF Generation
      - Data Processing
      - Utility APIs
      - Currency
    humanURL: https://apyhub.com/
    properties:
      - url: https://apyhub.com/docs
        type: Documentation
      - url: openapi/apyhub-openapi.yaml
        type: OpenAPI
      - url: json-schema/conversion-request-schema.json
        type: JSONSchema
      - url: json-structure/conversion-request-structure.json
        type: JSONStructure
      - url: examples/conversion-request-example.json
        type: Example
      - url: json-ld/apyhub-context.jsonld
        type: JSONLD
      - url: rules/apyhub-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/apyhub-api.yaml
        type: NaftikoCapability
      - url: capabilities/document-utilities.yaml
        type: NaftikoCapability
      - url: vocabulary/apyhub-vocabulary.yaml
        type: Vocabulary
    description: The ApyHub API provides utility APIs for document conversion, PDF generation, data extraction, image processing, and currency exchange that developers can integrate quickly into their applications.
common:
  - type: Website
    url: https://apyhub.com/
  - type: Documentation
    url: https://apyhub.com/docs
  - type: Blog
    url: https://apyhub.com/blog
  - type: Sign Up
    url: https://apyhub.com/register
  - type: Login
    url: https://apyhub.com/login
  - type: GitHub Organization
    url: https://github.com/apyhub
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
