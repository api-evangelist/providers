---
aid: open-policy-agent
url: '

  https://raw.githubusercontent.com/api-search/open-policy-agent/refs/heads/main/apis.yml'
apis:
- aid: open-policy-agent:open-policy-agent-policy-api
  name: Open Policy Agent Policy API
  tags:
  - Management
  - Policies
  - Rego
  humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#policy-api
  properties:
  - url: https://www.openpolicyagent.org/docs/latest/rest-api/#policy-api
    type: Documentation
  - url: openapi/policy-api.yml
    type: OpenAPI
  - url: json-schema/opa-policy-schema.json
    type: JSONSchema
  - url: policy/bruno.json
    type: BrunoCollection
  - url: '

      https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-19ce2c88-97b8-4f58-a101-b8be70794a85'
    type: PostmanCollection
  description: API for managing policy modules, allowing CRUD operations on Rego policy files stored in OPA.
- aid: open-policy-agent:open-policy-agent-data-api
  name: Open Policy Agent Data API
  tags:
  - Data
  - Documents
  - Storage
  humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#data-api
  properties:
  - url: https://www.openpolicyagent.org/docs/latest/rest-api/#data-api
    type: Documentation
  - url: openapi/data-api.yml
    type: OpenAPI
  - url: data/bruno.json
    type: BrunoCollection
  - url: '

      https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-96c58dc4-3514-48ee-a35f-a9c2aeb14fa0'
    type: PostmanCollection
  description: API for reading and writing documents in OPA (Open Policy Agent).
- aid: open-policy-agent:open-policy-agent-query-api
  name: Open Policy Agent Query API
  tags:
  - Evaluation
  - Queries
  - Rego
  humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#query-api
  properties:
  - url: https://www.openpolicyagent.org/docs/latest/rest-api/#query-api
    type: Documentation
  - url: openapi/query-api.yml
    type: OpenAPI
  - url: query/bruno.json
    type: BrunoCollection
  - url: '

      https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-9170dd84-c3d5-45a4-9efc-9ef6ab30744e'
    type: PostmanCollection
  description: API for executing simple and ad-hoc queries in OPA (Open Policy Agent).
- aid: open-policy-agent:open-policy-agent-compile-api
  name: Open Policy Agent Compile API
  tags:
  - Compile
  - Evaluation
  - Partial Evaluation
  humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api
  properties:
  - url: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api
    type: Documentation
  - url: openapi/compile-api.yml
    type: OpenAPI
  - url: compile/bruno.json
    type: BrunoCollection
  - url: '

      https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-1e1d8e0e-7157-4b7f-99cf-611fa56a0c3c'
    type: PostmanCollection
  description: API for partially evaluating Rego queries in OPA (Open Policy Agent).
- aid: open-policy-agent:open-policy-agent-health-api
  name: Open Policy Agent Health API
  tags:
  - Availability
  - Health
  - Monitoring
  humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#health-api
  properties:
  - url: https://www.openpolicyagent.org/docs/latest/rest-api/#health-api
    type: Documentation
  - url: openapi/health-api.yml
    type: OpenAPI
  - url: health/bruno.json
    type: BrunoCollection
  - url: '

      https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-198cdb4f-e1d1-44c4-aa1f-ef8f66760d1a'
    type: PostmanCollection
  description: API for checking the health and readiness of an OPA (Open Policy Agent) server.
- aid: open-policy-agent:open-policy-agent-config-api
  name: Open Policy Agent Config API
  tags:
  - Configurations
  - Discovery
  - Management
  humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#config-api
  properties:
  - url: https://www.openpolicyagent.org/docs/latest/rest-api/#config-api
    type: Documentation
  - url: openapi/config-api.yml
    type: OpenAPI
  - url: config/bruno.json
    type: BrunoCollection
  - url: '

      https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-979cbaf7-8515-4fd2-8035-134685590967'
    type: PostmanCollection
  description: API for retrieving OPA's active configuration, including discovered configurations.
- aid: open-policy-agent:open-policy-agent-status-api
  name: Open Policy Agent Status API
  tags:
  - Monitoring
  - Observability
  - Status
  humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#status-api
  properties:
  - url: https://www.openpolicyagent.org/docs/latest/rest-api/#status-api
    type: Documentation
  - url: openapi/status-api.yml
    type: OpenAPI
  - url: status/bruno.json
    type: BrunoCollection
  - url: '

      https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-b4943ca3-d651-4c68-a003-e6ca7feace03'
    type: PostmanCollection
  description: API for accessing OPA (Open Policy Agent) status information via a pull-based mechanism.
name: Open Policy Agent
tags:
- Policies
- Standards
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://www.openpolicyagent.org/docs/latest/rest-api/
  name: Documentation
  type: Documentation
- url: https://www.openpolicyagent.org/docs/latest/rest-api/#authentication
  name: Authentication
  type: Authentication
- url: https://www.openpolicyagent.org/docs/latest/rest-api/#errors
  name: Errors
  type: Errors
- url: https://www.postman.com/api-evangelist/open-policy-agent/overview
  name: Postman Workspace
  type: PostmanWorkspace
- url: https://github.com/api-search/open-policy-agent
  name: GitHub Repository
  type: GitHubRepository
created: '2024-11-18'
modified: '2026-04-07'
position: Consuming
description: Open Policy Agent (OPA) is an open-source project that provides a flexible and powerful policy engine for cloud-native environments. OPA enables users to define and enforce policies across their infrastructure, applications, and services through a declarative language called Rego. OPA integrates seamlessly with popular tools and frameworks like Kubernetes, Istio, and Envoy, making it easy to implement fine-grained access control, security, and compliance policies.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

