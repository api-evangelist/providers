---
aid: netflix-conductor
name: Netflix Conductor
description: Conductor is a microservices orchestration platform originally created by Netflix, providing a workflow engine for coordinating and managing complex distributed processes across multiple services with built-in retries, error handling, and observability.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Event-Driven
  - Microservices
  - Netflix
  - Open Source
  - Orchestration
  - Workflows
url: https://raw.githubusercontent.com/api-evangelist/netflix-conductor/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-03-26'
specificationVersion: '0.19'
apis:
  - aid: netflix-conductor:netflix-conductor
    name: Netflix Conductor
    description: Conductor is a microservices orchestration engine originally built at Netflix for running workflows that span across multiple services, providing task management, workflow definitions, and a REST API for managing distributed process execution.
    humanURL: https://conductor-oss.org/
    tags:
      - Event-Driven
      - Microservices
      - Netflix
      - Open Source
      - Orchestration
      - Workflows
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/netflix-conductor/refs/heads/main/openapi/conductor-api.yml
common:
  - type: Website
    url: https://conductor-oss.org/
  - type: Documentation
    url: https://docs.conductor-oss.org/
  - type: Getting Started
    url: https://docs.conductor-oss.org/getting-started
  - type: GitHub
    url: https://github.com/conductor-oss/conductor
  - type: Blog
    url: https://conductor-oss.org/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
