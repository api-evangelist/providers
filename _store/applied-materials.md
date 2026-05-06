---
aid: applied-materials
url: https://raw.githubusercontent.com/api-evangelist/applied-materials/refs/heads/main/apis.yml
modified: '2026-04-19'
apis:
  - aid: applied-materials:applied-materials-api
    name: Applied Materials API
    tags:
      - Semiconductor
      - Manufacturing
      - Equipment
      - Maintenance
    humanURL: https://www.applied-materials.com
    properties:
      - url: https://www.applied-materials.com
        type: Website
      - url: openapi/applied-materials-openapi.yaml
        type: OpenAPI
      - url: json-schema/equipment-schema.json
        type: JSONSchema
      - url: json-structure/equipment-structure.json
        type: JSONStructure
      - url: examples/equipment-example.json
        type: Example
      - url: json-ld/applied-materials-context.jsonld
        type: JSONLD
      - url: rules/applied-materials-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/applied-materials-api.yaml
        type: NaftikoCapability
      - url: capabilities/equipment-monitoring.yaml
        type: NaftikoCapability
      - url: vocabulary/applied-materials-vocabulary.yaml
        type: Vocabulary
    description: API for managing semiconductor manufacturing equipment from Applied Materials, supporting equipment status monitoring and maintenance scheduling in fab environments.
common:
  - type: Website
    url: https://www.applied-materials.com
description: Applied Materials is a global leader in materials engineering solutions used to produce virtually every new chip and advanced display in the world.
name: Applied Materials
tags:
  - Semiconductor
  - Manufacturing
  - Equipment
  - Fab Operations
  - Materials Engineering
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
---
