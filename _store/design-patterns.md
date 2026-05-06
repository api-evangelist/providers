---
aid: design-patterns
name: Design Patterns
description: Reusable solutions to commonly occurring problems in software design, including the Gang of Four catalog (creational, structural, behavioral) and core API design patterns such as HATEOAS, idempotency keys, webhooks, and sagas.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Best Practices
  - Object-Oriented Programming
  - Software Architecture
  - Software Engineering
  - API Design
url: https://raw.githubusercontent.com/api-evangelist/design-patterns/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: design-patterns:catalog
    name: Design Patterns Catalog
    description: Rules, capabilities, vocabulary, and linked-data description covering classic Gang of Four patterns and key API design patterns.
    tags:
      - Patterns
      - Architecture
    properties:
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/design-patterns/main/rules/design-patterns-rules.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/design-patterns/main/capabilities/design-patterns-capabilities.md
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/design-patterns/main/vocabulary/design-patterns-vocabulary.json
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/design-patterns/main/json-ld/design-patterns.jsonld
common:
  - type: Reference
    url: https://refactoring.guru/design-patterns
  - type: Reference
    url: https://en.wikipedia.org/wiki/Software_design_pattern
  - type: GitHub Organization
    url: https://github.com/api-evangelist
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
