---
aid: deprecation
name: Deprecation
description: API deprecation, sunset headers, end-of-life management, and API retirement practices, including RFC 8594 Sunset, the Deprecation header, OpenAPI deprecation flags, and consumer migration patterns.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Retirement
  - Deprecation
  - End of Life
  - Sunset
  - Lifecycle
  - Migration
url: https://raw.githubusercontent.com/api-evangelist/deprecation/refs/heads/main/apis.yml
created: '2026-03-29'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: deprecation:practice
    name: API Deprecation Practice
    description: Rules, capabilities, vocabulary, and linked-data description for managing API deprecation and retirement.
    tags:
      - Deprecation
      - Sunset
    properties:
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/deprecation/main/rules/deprecation-rules.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/deprecation/main/capabilities/deprecation-capabilities.md
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/deprecation/main/vocabulary/deprecation-vocabulary.json
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/deprecation/main/json-ld/deprecation.jsonld
common:
  - type: Reference
    url: https://www.rfc-editor.org/rfc/rfc8594.html
  - type: Reference
    url: https://datatracker.ietf.org/doc/draft-ietf-httpapi-deprecation-header/
  - type: GitHub Organization
    url: https://github.com/api-evangelist
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
