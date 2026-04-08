---
aid: chaos-mesh
url: https://raw.githubusercontent.com/api-evangelist/chaos-mesh/refs/heads/main/apis.yml
apis:
- aid: chaos-mesh:chaos-mesh-api
  name: Chaos Mesh API
  tags:
  - Chaos Engineering
  - Fault Injection
  - Kubernetes
  humanURL: https://chaos-mesh.org/docs/
  properties:
  - url: https://chaos-mesh.org/docs/
    type: Documentation
  - type: Getting Started
    url: https://chaos-mesh.org/docs/quick-start/
  - type: GitHubRepository
    url: https://github.com/chaos-mesh/chaos-mesh
  - type: OpenAPI
    url: openapi/chaos-mesh-dashboard-api-openapi.yml
  - type: JSONSchema
    url: json-schema/chaos-mesh-experiment-schema.json
  description: Chaos Mesh provides Kubernetes custom resources and a REST API for orchestrating chaos experiments including network faults, pod failures, IO chaos, stress testing, and HTTP request injection. The Chaos Dashboard provides a web UI backed by a REST API for creating, managing, and monitoring chaos experiments and workflows.
name: Chaos Mesh
tags:
- Chaos Engineering
- Cloud Native
- Kubernetes
- Resilience
- Testing
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Chaos Mesh is a cloud-native chaos engineering platform that orchestrates chaos experiments on Kubernetes environments to test system resilience and reliability.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

