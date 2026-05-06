---
aid: nomad
name: HashiCorp Nomad
description: HashiCorp Nomad is a flexible workload orchestrator that enables organizations to deploy and manage containers, legacy applications, and batch jobs across any infrastructure. The Nomad developer platform provides a comprehensive HTTP API, official SDKs, and tooling for automating job scheduling, cluster management, and service orchestration at scale.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/nomad/refs/heads/main/apis.yml
created: '2026-03-20'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Workload Orchestration
  - Container Orchestration
  - Scheduling
  - Infrastructure
  - DevOps
apis:
  - aid: nomad:http-api
    name: HashiCorp Nomad HTTP API
    description: The HashiCorp Nomad HTTP API provides programmatic access to all Nomad functionality including job scheduling, allocation management, node operations, deployments, services, evaluations, namespaces, ACL policies, and cluster status. All API routes are prefixed with /v1/ and the default port is 4646. The API is RESTful, responds to standard HTTP verbs, and supports ACL token authentication via the X-Nomad-Token header or Bearer scheme. Developers can use this API to submit and manage workloads, monitor cluster health, query allocation status, and integrate Nomad orchestration into their infrastructure automation workflows.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.hashicorp.com/nomad/api-docs
    baseURL: http://localhost:4646
    tags:
      - Workload Orchestration
      - Container Orchestration
      - Scheduling
      - Infrastructure
      - DevOps
      - Cloud
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/nomad/api-docs
      - type: OpenAPI
        url: openapi/nomad-http-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/nomad-event-stream-asyncapi.yml
      - type: JSONSchema
        url: json-schema/nomad-job-schema.json
  - aid: nomad:go-sdk
    name: HashiCorp Nomad Go SDK
    description: The HashiCorp Nomad Go SDK is the official Go client library for interacting with the Nomad HTTP API. It provides a high-level, idiomatic Go interface for managing jobs, allocations, nodes, deployments, evaluations, and other Nomad resources. The SDK is maintained by HashiCorp as part of the main Nomad repository and is used internally by the Nomad CLI itself, making it the most comprehensive and up-to-date client available.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://pkg.go.dev/github.com/hashicorp/nomad/api
    tags:
      - Workload Orchestration
      - Go
      - SDK
      - DevOps
    properties:
      - type: Documentation
        url: https://pkg.go.dev/github.com/hashicorp/nomad/api
  - aid: nomad:python-sdk
    name: HashiCorp Nomad Python SDK
    description: The python-nomad library is a Python client for the HashiCorp Nomad HTTP API. It provides Pythonic access to Nomad resources including jobs, nodes, allocations, deployments, evaluations, namespaces, and ACL management. The library supports configuration via environment variables such as NOMAD_ADDR, NOMAD_TOKEN, and NOMAD_NAMESPACE for consistency with the Nomad CLI and other ecosystem tools.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/jrxFive/python-nomad
    tags:
      - Workload Orchestration
      - Python
      - SDK
      - DevOps
    properties:
      - type: Documentation
        url: https://github.com/jrxFive/python-nomad
  - aid: nomad:java-sdk
    name: HashiCorp Nomad Java SDK
    description: The Nomad Java SDK is an official Java client library for the HashiCorp Nomad HTTP API. It enables Java and JVM-based applications to interact with Nomad clusters for submitting jobs, querying allocations, managing nodes, and performing other orchestration operations. The SDK provides a typed Java interface over the Nomad REST API, making it suitable for enterprise applications and microservice architectures running on the JVM.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.hashicorp.com/nomad/api-docs/libraries-and-sdks
    tags:
      - Workload Orchestration
      - Java
      - SDK
      - DevOps
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/nomad/api-docs/libraries-and-sdks
common:
  - type: Portal
    url: https://developer.hashicorp.com/nomad
  - type: Documentation
    url: https://developer.hashicorp.com/nomad/docs
  - type: Website
    url: https://www.nomadproject.io/
  - type: PrivacyPolicy
    url: https://www.hashicorp.com/privacy
  - type: TermsOfService
    url: https://www.hashicorp.com/terms-of-service
  - type: Support
    url: https://support.hashicorp.com/
  - type: Blog
    url: https://www.hashicorp.com/blog
  - type: Login
    url: https://portal.cloud.hashicorp.com/sign-in
  - type: JSON-LD
    url: json-ld/nomad-context.jsonld
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
---
