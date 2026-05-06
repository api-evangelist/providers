---
aid: grapes-knowledge-base
name: Grapes Knowledge Base
description: Grapes is a knowledge management platform with administrative, configuration, and project management capabilities. The Grapes API allows automation of recurring operations including project administration, agent configuration, and dataset import/export. Documentation is available in English and French.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Knowledge Management
  - Knowledge Base
  - Data Management
  - Automation
  - HATEOAS
created: '2025-02-24'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/grapes-knowledge-base/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: grapes-knowledge-base:grapes-api
    name: Grapes API
    description: The Grapes API allows you to automate recurring operations on the Grapes knowledge management platform, including project administration, agent configuration, and dataset import/export. The API follows HATEOAS principles for link management between resources.
    humanURL: https://docs.data-grapes.com/en/docs/developer-docs/api/api-reference/
    tags:
      - Knowledge Management
      - Automation
      - HATEOAS
    properties:
      - type: Documentation
        url: https://docs.data-grapes.com/en/docs/developer-docs/api/api-reference/
      - type: Security
        url: https://docs.data-grapes.com/en/docs/developer-docs/api/api-security/
      - type: OpenAPI
        url: openapi/grapes-knowledge-base-openapi.yml
common:
  - type: Documentation
    url: https://docs.data-grapes.com/en/
  - type: DeveloperDocs
    url: https://docs.data-grapes.com/en/docs/developer-docs/
  - type: UserGuide
    url: https://docs.data-grapes.com/en/docs/user-guide/
  - type: OpenAPI
    url: openapi/grapes-knowledge-base-openapi.yml
  - type: JSONSchema
    url: json-schema/grapes-knowledge-base-project-schema.json
  - type: JSONLDContext
    url: json-ld/grapes-knowledge-base-context.jsonld
  - type: Rules
    url: grapes-knowledge-base-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
