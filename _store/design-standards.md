---
aid: design-standards
name: Design Standards
description: Design Standards encompasses the frameworks, guidelines, and best practices used in product, interface, and system design to ensure consistency, usability, and accessibility. Includes API design guidelines, naming and format conventions, accessibility conformance, deprecation policy, and governance practices.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accessibility
  - Design Standards
  - Design Systems
  - UX
  - API Guidelines
  - Governance
url: https://raw.githubusercontent.com/api-evangelist/design-standards/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: design-standards:program
    name: Design Standards Program
    description: Rules, capabilities, vocabulary, and linked-data description for an organizational design standards program covering products, interfaces, and APIs.
    tags:
      - Standards
      - Governance
    properties:
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/design-standards/main/rules/design-standards-rules.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/design-standards/main/capabilities/design-standards-capabilities.md
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/design-standards/main/vocabulary/design-standards-vocabulary.json
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/design-standards/main/json-ld/design-standards.jsonld
common:
  - type: Reference
    url: https://opensource.zalando.com/restful-api-guidelines/
  - type: Reference
    url: https://www.w3.org/TR/WCAG21/
  - type: GitHub Organization
    url: https://github.com/api-evangelist
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
