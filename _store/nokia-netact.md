---
aid: nokia-netact
name: Nokia NetAct
description: Nokia NetAct is a network management system that enables operators to monitor, configure, and optimize multi-vendor mobile networks across radio, transport, and core domains. The northbound interface exposes REST APIs for OSS/BSS integration including topology, performance, fault, and configuration management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Network Management
  - OSS
  - SNMP
  - Telecom
url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nokia-netact:nokia-netact-api
    name: Nokia NetAct / Ericsson OSS API
    description: Nokia NetAct and Ericsson OSS provide network element management APIs for telecom operators. APIs enable network topology discovery, performance monitoring, fault management, and configuration management across RAN, transport, and core network infrastructure.
    humanURL: https://www.nokia.com/
    baseURL: https://api.nokia-netact.example.com
    tags:
      - Network Management
      - OSS
      - SNMP
      - Telecom
    properties:
      - type: Documentation
        url: https://www.nokia.com/networks/products/netact/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/openapi/nokia-netact-nbi-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/json-schema/nokia-netact-network-element-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/json-ld/nokia-netact-context.jsonld
common:
  - type: Portal
    url: https://www.nokia.com/
  - type: Website
    url: https://www.nokia.com/
  - type: Documentation
    url: https://www.nokia.com/networks/products/netact/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/openapi/nokia-netact-nbi-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/json-schema/nokia-netact-network-element-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/json-ld/nokia-netact-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
