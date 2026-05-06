---
aid: wiremock
name: WireMock
description: WireMock is an open source tool for mocking HTTP services and APIs. It enables developers to build stable, predictable development environments by creating mock APIs that simulate the behavior of real services. WireMock provides a comprehensive admin API for managing stub mappings, recording real traffic, verifying requests, and modeling stateful behavior through scenarios. The project is governed by the WireMock community on GitHub and supports Java, Python, JavaScript, .NET, Go, PHP, and Kotlin clients.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Mocking
  - Mock Server
  - Mocking
  - Platform
  - Stubs
  - Testing
url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/apis.yml
access: 3rd-Party
created: '2025-01-08'
modified: '2026-05-03'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: wiremock:wiremock-admin-api
    name: WireMock Admin API
    description: The WireMock Admin REST API provides programmatic control over a running WireMock server instance. It supports creating, updating, and deleting stub mappings; querying the request journal; recording and replaying real API traffic; managing stateful scenarios; and performing system operations such as reset and shutdown. The API is described in OpenAPI 3.0 and available under the /__admin/ path prefix on any running WireMock instance.
    humanURL: https://wiremock.org/docs/standalone/admin-api-reference/
    baseURL: http://localhost:8080
    tags:
      - Admin API
      - API Mocking
      - Mock Server
      - Stub Management
      - Testing
    properties:
      - type: Documentation
        url: https://wiremock.org/docs/standalone/admin-api-reference/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/openapi/wiremock-admin-api-openapi.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/rules/wiremock-rules.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/capabilities/api-mocking-and-testing.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/json-schema/wiremock-stub-mapping-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/json-structure/wiremock-stub-mapping-structure.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/examples/wiremock-create-stub-mapping-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/examples/wiremock-scenario-stub-example.json
common:
  - url: https://wiremock.org/
    name: WireMock
    type: Website
    description: Official WireMock project website.
  - url: https://wiremock.org/docs/
    name: WireMock Documentation
    type: Documentation
    description: Official WireMock documentation.
  - url: https://wiremock.org/docs/standalone/admin-api-reference/
    name: WireMock Admin API Reference
    type: Reference
    description: Reference documentation for the WireMock Admin REST API.
  - url: https://github.com/wiremock/wiremock
    name: WireMock GitHub Repository
    type: GitHubRepository
    description: Main WireMock Java repository on GitHub.
  - url: https://github.com/wiremock
    name: WireMock GitHub Organization
    type: GitHubOrganization
    description: WireMock GitHub organization with SDKs for Java, Python, JS, .NET, Go, PHP, and Kotlin.
  - url: https://github.com/wiremock/python-wiremock
    name: WireMock Python Client
    type: SDK
    description: Official WireMock Python client library.
  - url: https://github.com/wiremock/wiremock-js
    name: WireMock JavaScript Client
    type: SDK
    description: Official WireMock JavaScript/Node.js client library.
  - url: https://github.com/wiremock/WireMock.Net
    name: WireMock.Net
    type: SDK
    description: Official WireMock .NET client library.
  - url: https://github.com/wiremock/go-wiremock
    name: WireMock Go Client
    type: SDK
    description: Official WireMock Go client library.
  - url: https://github.com/wiremock/wiremock-php
    name: WireMock PHP Client
    type: SDK
    description: Official WireMock PHP client library.
  - url: https://github.com/wiremock/kotlin-wiremock
    name: WireMock Kotlin Client
    type: SDK
    description: Official WireMock Kotlin client library.
  - url: https://github.com/wiremock/wiremock-docker
    name: WireMock Docker
    type: Docker
    description: Official WireMock Docker images.
  - url: https://github.com/wiremock/helm-charts
    name: WireMock Helm Charts
    type: HelmChart
    description: Official WireMock Helm charts for Kubernetes deployment.
  - url: https://github.com/wiremock/wiremock-npm
    name: WireMock npm Package
    type: SDK
    description: WireMock npm package for Node.js.
  - url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/json-ld/wiremock-context.jsonld
    name: WireMock JSON-LD Context
    type: JSONLDContext
    description: JSON-LD context for WireMock domain vocabulary.
  - url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/vocabulary/wiremock-vocabulary.yml
    name: WireMock Vocabulary
    type: Vocabulary
    description: Domain vocabulary for WireMock API mocking concepts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
