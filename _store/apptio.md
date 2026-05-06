---
aid: apptio
name: Apptio
description: Apptio is a technology business management platform that helps organizations understand the cost, value, and quality of their technology investments. It provides financial management, planning, and analytics capabilities for IT organizations, enabling data-driven decision-making around technology spending and resource allocation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Cost Management
  - IT Finance
  - Technology Business Management
url: https://raw.githubusercontent.com/api-evangelist/apptio/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apptio:apptio-api
    name: Apptio API
    tags:
      - Technology Business Management
      - IT Finance
      - Cost Management
      - Analytics
    humanURL: https://developer.apptio.com/
    properties:
      - url: https://developer.apptio.com/
        type: Documentation
      - url: openapi/apptio-openapi.yaml
        type: OpenAPI
      - url: json-schema/cost-allocation-schema.json
        type: JSONSchema
      - url: json-structure/cost-allocation-structure.json
        type: JSONStructure
      - url: examples/cost-allocation-example.json
        type: Example
      - url: json-ld/apptio-context.jsonld
        type: JSONLD
      - url: rules/apptio-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/apptio-api.yaml
        type: NaftikoCapability
      - url: capabilities/it-cost-management.yaml
        type: NaftikoCapability
      - url: vocabulary/apptio-vocabulary.yaml
        type: Vocabulary
    description: API for the Apptio technology business management platform providing programmatic access to cost allocations, IT budgets, and financial reporting for technology organizations.
common:
  - type: Website
    url: https://www.apptio.com/
  - type: Documentation
    url: https://developer.apptio.com/
  - type: Blog
    url: https://www.apptio.com/blog/
  - type: Sign Up
    url: https://www.apptio.com/request-demo/
  - type: GitHub Organization
    url: https://github.com/apptio
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
