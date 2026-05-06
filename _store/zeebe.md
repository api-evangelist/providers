---
aid: zeebe
name: Zeebe
description: Zeebe is the cloud-native workflow engine that powers Camunda 8, providing scalable, resilient workflow automation and microservices orchestration without relying on a central database, enabling high throughput with horizontal scaling. It implements BPMN 2.0 process execution and provides a REST API for process deployment, instance management, job handling, message correlation, and cluster topology queries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - BPMN
  - Camunda
  - Cloud Native
  - Distributed Systems
  - Java
  - Microservices
  - Process Automation
  - Workflow Orchestration
url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: zeebe:zeebe
    name: Zeebe REST API
    description: The Zeebe REST API provides programmatic access to the Zeebe workflow engine powering Camunda 8. It enables process deployment, process instance creation and management, job activation and completion, message and signal publishing, incident resolution, user task management, and cluster topology queries.
    humanURL: https://docs.camunda.io/docs/apis-tools/zeebe-api-rest/zeebe-api-rest-overview/
    baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
    tags:
      - BPMN
      - Camunda
      - Cloud Native
      - Microservices
      - Process Automation
      - Workflow Orchestration
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/openapi/zeebe-api.yml
      - type: Documentation
        url: https://docs.camunda.io/docs/apis-tools/zeebe-api-rest/zeebe-api-rest-overview/
      - type: Postman
        url: https://www.postman.com/camundateam/camunda-8-postman/collection/j0knqwp/zeebe-api-rest
      - type: Spectral Rules
        url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/rules/zeebe-rules.yml
      - type: Examples
        url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/examples/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/json-schema/
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/json-structure/
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/json-ld/zeebe-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/vocabulary/zeebe-vocabulary.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/capabilities/
common:
  - type: Website
    url: https://camunda.com/platform/zeebe/
    name: Zeebe Platform Page
  - type: Documentation
    url: https://docs.camunda.io/docs/components/zeebe/zeebe-overview/
    name: Zeebe Documentation Overview
  - type: Documentation
    url: https://docs.camunda.io/docs/apis-tools/zeebe-api-rest/zeebe-api-rest-overview/
    name: Zeebe REST API Documentation
  - type: Getting Started
    url: https://docs.camunda.io/docs/guides/
    name: Getting Started with Camunda 8
  - type: GitHub
    url: https://github.com/camunda/camunda
    name: Camunda GitHub Repository
  - type: GitHubOrg
    url: https://github.com/camunda
    name: Camunda GitHub Organization
  - type: GitHubOrg
    url: https://github.com/camunda-community-hub
    name: Camunda Community Hub
  - type: Pricing
    url: https://camunda.com/pricing/
    name: Camunda Pricing
  - type: Blog
    url: https://camunda.com/blog/
    name: Camunda Blog
  - type: Issues
    url: https://github.com/camunda/camunda/issues
    name: GitHub Issues
  - type: SDK
    url: https://github.com/camunda/camunda-bpm-spring-boot-starter
    name: Spring Boot Starter
  - type: SDK
    url: https://github.com/camunda-community-hub/zeebe-client-csharp
    name: C# Client
  - type: SDK
    url: https://github.com/camunda-community-hub/micronaut-zeebe-client
    name: Micronaut Client
  - type: ChangeLog
    url: https://github.com/camunda/camunda/releases
    name: Release Notes
  - type: Forum
    url: https://forum.camunda.io/
    name: Camunda Forum
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
