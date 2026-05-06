---
aid: navis
url: https://raw.githubusercontent.com/api-evangelist/navis/refs/heads/main/apis.yml
name: Navis (Kaleris)
tags:
  - Maritime
  - Port
  - Terminal
  - Container
  - Logistics
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-18'
modified: '2026-04-28'
position: Consuming
description: Navis (now operated by Kaleris) provides terminal operating systems and supply chain software for the maritime and intermodal industries. The flagship N4 product offers APIs for container tracking, vessel planning, berth scheduling, yard management, and gate operations, serving 650+ organizations across 95+ countries.
specificationVersion: '0.19'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
apis:
  - aid: navis:n4
    name: NAVIS N4 Terminal Operating System API
    description: NAVIS N4 provides terminal operating system APIs for container port operations. APIs enable container tracking, vessel planning, berth scheduling, yard management, and gate operations for port terminals and intermodal facilities. Now operated by Kaleris, serving 650+ organizations across 95+ countries.
    humanURL: https://www.navis.com/
    tags:
      - Maritime
      - Port
      - Terminal
      - Container
      - Logistics
    properties:
      - type: Documentation
        url: https://kaleris.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/navis/refs/heads/main/openapi/navis-n4-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/navis/refs/heads/main/json-schema/navis-unit-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/navis/refs/heads/main/json-ld/navis-context.jsonld
common:
  - type: Portal
    url: https://kaleris.com/
  - type: Website
    url: https://kaleris.com/
  - type: Support
    url: https://kaleris.com/support/
  - type: Support
    url: https://kaleriscommunity.force.com/
  - type: Blog
    url: https://kaleris.com/resources/
  - type: PrivacyPolicy
    url: https://kaleris.com/privacy-policy/
  - type: TermsOfService
    url: https://kaleris.com/terms-and-conditions/
  - type: Status
    url: https://trust.kaleris.com/
---
