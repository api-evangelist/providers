---
aid: conductor
url: https://raw.githubusercontent.com/api-evangelist/conductor/refs/heads/main/apis.yml
apis:
- aid: conductor:conductor
  name: Conductor
  tags:
  - Automation
  - Orchestration
  - State
  - Tasks
  humanURL: https://conductor-oss.github.io/conductor/documentation/api/workflow.html
  properties:
  - url: https://conductor-oss.github.io/conductor/documentation/api/workflow.html
    type: Documentation
  - url: openapi/conductor-conductor-openapi.yml
    type: OpenAPI
  - url: asyncapi/conductor-conductor-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/workflow-def.json
    type: JSONSchema
  - url: json-schema/task-def.json
    type: JSONSchema
  - url: json-schema/workflow-execution.json
    type: JSONSchema
  - url: json-schema/event-handler.json
    type: JSONSchema
  - url: json-ld/conductor-context.jsonld
    type: JSONLD
  description: Conductor allows you to build a complex application using simple and granular tasks that do not need to be aware of or keep track of the state of your application's execution flow. Conductor keeps track of the state, calls tasks in the right order (sequentially or in parallel, as defined by you), retry calls if needed, handle failure scenarios gracefully, and outputs the final result.
name: Conductor
tags:
- Automation
- Orchestration
- State
- Tasks
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consuming
description: Conductor allows you to build a complex application using simple and granular tasks that do not need to be aware of or keep track of the state of your application's execution flow. Conductor keeps track of the state, calls tasks in the right order (sequentially or in parallel, as defined by you), retry calls if needed, handle failure scenarios gracefully, and outputs the final result.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

