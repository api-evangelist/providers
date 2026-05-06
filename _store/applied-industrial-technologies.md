---
aid: applied-industrial-technologies
url: https://raw.githubusercontent.com/api-evangelist/applied-industrial-technologies/refs/heads/main/apis.yml
modified: '2026-04-19'
apis:
  - aid: applied-industrial-technologies:applied-industrial-technologies-api
    name: Applied Industrial Technologies API
    tags:
      - Industrial Distribution
      - Bearings
      - Power Transmission
      - Products
      - Orders
    humanURL: https://www.applied-industrial-technologies.com
    properties:
      - url: https://www.applied-industrial-technologies.com
        type: Website
      - url: openapi/applied-industrial-technologies-openapi.yaml
        type: OpenAPI
      - url: json-schema/product-schema.json
        type: JSONSchema
      - url: json-structure/product-structure.json
        type: JSONStructure
      - url: examples/product-example.json
        type: Example
      - url: json-ld/applied-industrial-technologies-context.jsonld
        type: JSONLD
      - url: rules/applied-industrial-technologies-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/applied-industrial-technologies-api.yaml
        type: NaftikoCapability
      - url: capabilities/industrial-procurement.yaml
        type: NaftikoCapability
      - url: vocabulary/applied-industrial-technologies-vocabulary.yaml
        type: Vocabulary
    description: API for browsing the Applied Industrial Technologies product catalog of bearings, power transmission, fluid power, and industrial rubber products, and managing purchase orders.
common:
  - type: Website
    url: https://www.applied-industrial-technologies.com
description: Applied Industrial Technologies is an industrial distributor of bearings, power transmission products, fluid power components, industrial rubber products, linear motion components, tools, and related supplies.
name: Applied Industrial Technologies
tags:
  - Industrial Distribution
  - Bearings
  - Power Transmission
  - Fluid Power
  - Supply Chain
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
---
