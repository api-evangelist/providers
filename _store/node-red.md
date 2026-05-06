---
aid: node-red
name: Node-RED
description: Node-RED is an open source flow-based programming tool for wiring together hardware devices, APIs, and online services. The runtime exposes an Admin HTTP API used by the Node-RED Editor and the command-line admin tool to manage flows, nodes, settings, diagnostics, and authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Self-Hosted
  - Workflow Automation
  - Flow-Based Programming
  - IoT
url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: node-red:node-red
    name: Node-RED Admin API
    description: Node-RED's Admin HTTP API for remote administration of the runtime, including flows, nodes, settings, diagnostics, and authentication.
    humanURL: https://nodered.org
    baseURL: http://localhost:1880
    tags:
      - Workflow Automation
      - Flow-Based Programming
    properties:
      - type: Documentation
        url: https://nodered.org/docs/
      - type: API Documentation
        url: https://nodered.org/docs/api/admin/methods/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/openapi/node-red-admin-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/json-schema/node-red-flow-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/json-ld/node-red-context.jsonld
      - type: Repository
        url: https://github.com/node-red/node-red
common:
  - type: Website
    url: https://nodered.org
  - type: Documentation
    url: https://nodered.org/docs/
  - type: API Documentation
    url: https://nodered.org/docs/api/admin/methods/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/openapi/node-red-admin-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/json-schema/node-red-flow-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/json-ld/node-red-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
