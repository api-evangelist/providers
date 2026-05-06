---
aid: appsmith
name: Appsmith
description: Appsmith is an open source low-code platform for building internal tools and workflow applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Low-Code
  - Open Source
  - Internal Tools
  - Workflow Automation
  - Developer Tools
url: https://raw.githubusercontent.com/api-evangelist/appsmith/refs/heads/main/apis.yml
created: 2026-03-27T00:00:00.000Z
modified: '2026-04-19'
specificationVersion: 0.19
apis:
  - aid: appsmith:appsmith-api
    name: Appsmith API
    tags:
      - Low-Code
      - Applications
      - Workspaces
      - Datasources
    humanURL: https://docs.appsmith.com
    properties:
      - url: https://www.appsmith.com
        type: Website
      - url: https://docs.appsmith.com
        type: Documentation
      - url: https://github.com/appsmithorg/appsmith
        type: GitHubRepository
      - url: openapi/appsmith-openapi.yaml
        type: OpenAPI
      - url: json-schema/application-schema.json
        type: JSONSchema
      - url: json-structure/application-structure.json
        type: JSONStructure
      - url: examples/application-example.json
        type: Example
      - url: json-ld/appsmith-context.jsonld
        type: JSONLD
      - url: rules/appsmith-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/appsmith-api.yaml
        type: NaftikoCapability
      - url: capabilities/internal-tool-builder.yaml
        type: NaftikoCapability
      - url: vocabulary/appsmith-vocabulary.yaml
        type: Vocabulary
    description: API for the Appsmith open source low-code platform, enabling programmatic management of applications, workspaces, and datasources for building internal tools.
common:
  - type: Website
    url: https://www.appsmith.com
  - type: Documentation
    url: https://docs.appsmith.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
