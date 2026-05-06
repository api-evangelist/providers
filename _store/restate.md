---
aid: restate
name: Restate
description: Restate is a low-latency durable execution engine for building resilient applications that tolerate all infrastructure faults. It provides durable execution for workflows, event-driven handlers, and stateful orchestration of microservices with exactly-once semantics, automatic retries, and built-in state management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Durable Execution
  - Workflows
  - Microservices
  - Orchestration
  - Distributed Systems
url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: restate:restate-admin
    name: Restate Admin API
    description: The Restate Admin API provides endpoints for managing service deployments, inspecting service metadata, managing in-flight invocations, and monitoring the health of the Restate server. It enables operators to register service deployments, purge completed invocations, and configure services programmatically.
    humanURL: https://restate.dev/
    baseURL: http://localhost:9070
    tags:
      - Deployments
      - Services
      - Invocations
      - Administration
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/openapi/restate-admin-api.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/json-schema/restate-deployment-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/json-schema/restate-invocation-schema.json
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/vocabulary/restate-vocabulary.yml
      - type: Documentation
        url: https://docs.restate.dev/
      - type: GitHub Repository
        url: https://github.com/restatedev/restate
      - type: KubernetesCRD
        url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/crd/restateclusters.yaml
      - type: KubernetesCRD
        url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/crd/restatedeployments.yaml
      - type: KubernetesCRD
        url: https://raw.githubusercontent.com/api-evangelist/restate/refs/heads/main/crd/restatecloudenvironments.yaml
common:
  - type: Website
    url: https://restate.dev/
  - type: Documentation
    url: https://docs.restate.dev/
  - type: GitHub Organization
    url: https://github.com/restatedev
  - type: TypeScript SDK
    url: https://github.com/restatedev/sdk-typescript
  - type: Python SDK
    url: https://github.com/restatedev/sdk-python
  - type: Java SDK
    url: https://github.com/restatedev/sdk-java
  - type: Go SDK
    url: https://github.com/restatedev/sdk-go
  - type: Rust SDK
    url: https://github.com/restatedev/sdk-rust
  - type: Examples
    url: https://github.com/restatedev/examples
  - type: Web UI
    url: https://github.com/restatedev/restate-web-ui
  - type: Discord
    url: https://discord.gg/skW3AZ6uGd
  - type: Blog
    url: https://restate.dev/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
