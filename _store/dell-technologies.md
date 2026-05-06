---
aid: dell-technologies
name: Dell Technologies
url: https://raw.githubusercontent.com/api-evangelist/dell-technologies/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise IT
  - Infrastructure
  - Servers
  - Storage
  - Cloud
  - Automation
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
description: Dell Technologies is a global Fortune 500 technology company that designs, develops, manufactures, and supports a wide range of computing products, including PCs, servers, storage, networking equipment, and software services. Dell publishes a developer platform exposing APIs and SDKs for managing PowerEdge servers, PowerStore storage, PowerScale, OpenManage, APEX, and related infrastructure products, enabling automation of IT operations and integration into enterprise tooling.
apis:
  - aid: dell-technologies:dell-api
    name: Dell Technologies API
    description: The Dell Technologies API provides programmatic access to Dell developer platform capabilities for managing infrastructure, configuring servers, monitoring systems, and automating IT operations across PowerEdge, PowerStore, PowerScale, and OpenManage product lines.
    humanURL: https://developer.dell.com/
    baseURL: https://developer.dell.com/apis
    tags:
      - Enterprise IT
      - Infrastructure
      - Servers
      - Storage
      - PowerEdge
      - PowerStore
      - OpenManage
    properties:
      - type: Documentation
        url: https://developer.dell.com/
      - type: OpenAPI
        url: openapi/dell-technologies-dell-api-openapi.yml
      - type: Rules
        url: rules/dell-technologies-dell-api-rules.yml
      - type: Capabilities
        url: capabilities/dell-technologies-dell-api-capabilities.yml
      - type: JSONSchema
        url: json-schema/dell-server-schema.json
common:
  - type: Website
    url: https://www.dell.com/
  - type: Developer Portal
    url: https://developer.dell.com/
  - type: GitHub
    url: https://github.com/dell
  - type: Support
    url: https://www.dell.com/support
  - type: Blog
    url: https://www.dell.com/en-us/blog/
  - type: JSON-LD
    url: json-ld/dell-context.jsonld
  - type: Vocabulary
    url: vocabulary/dell-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
