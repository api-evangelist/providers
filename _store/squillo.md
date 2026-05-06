---
aid: squillo
name: Squillo
description: Squillo is a Software as a Utility (SaaU) platform that enables integration and automation of entire IT systems and human processes in minutes, not months. It provides a low-code/no-code approach to connecting enterprise applications, automating workflows, and orchestrating complex IT processes without traditional development overhead.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Integration Platform
  - Automation
  - Workflow
  - No-Code
  - IT Process Automation
  - Software As A Utility
url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/apis.yml
created: '2025-08-19'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: squillo:squillo-platform
    name: Squillo Platform API
    description: The Squillo Platform API provides programmatic access to Squillo's integration and automation capabilities. Enables developers to manage workflows, connectors, integrations, and automation tasks programmatically. The API supports creating and managing integration flows, monitoring execution status, and configuring system connections.
    humanURL: https://squillo.io/
    baseURL: https://api.squillo.io/v1
    tags:
      - Integration Platform
      - Workflow Automation
      - IT Process Automation
      - No-Code
      - Connectors
    properties:
      - type: Documentation
        url: https://squillo.io/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/openapi/squillo-platform-openapi.yml
common:
  - type: Website
    url: https://squillo.io/
  - type: Documentation
    url: https://squillo.io/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/openapi/squillo-platform-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/json-schema/squillo-workflow-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/json-structure/squillo-workflow-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/json-ld/squillo-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/rules/squillo-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/capabilities/workflow-automation.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/squillo/refs/heads/main/vocabulary/squillo-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
