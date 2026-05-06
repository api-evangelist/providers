---
aid: restack
name: Restack
description: Restack is an enterprise AI agent platform and backend framework for building accurate, reliable, and scalable AI products. It provides durable workflow orchestration, long-running agent execution, and infrastructure for deploying AI agents at enterprise scale using Python and Kubernetes.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - Workflows
  - Orchestration
  - Enterprise
  - Python
url: https://raw.githubusercontent.com/api-evangelist/restack/refs/heads/main/apis.yml
created: '2025-02-17'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: restack:restack
    name: Restack
    description: Restack is an enterprise AI agent platform that provides long-running workflow orchestration, durable execution, and infrastructure for building and deploying AI agents. It generates REST API endpoints for each agent and workflow, enabling programmatic triggering, scheduling, and management of AI agents from any client application.
    humanURL: https://www.restack.io/
    baseURL: https://api.restack.io
    tags:
      - AI Agents
      - Workflows
      - Orchestration
      - Enterprise
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/restack/refs/heads/main/openapi/restack-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/restack/refs/heads/main/json-schema/restack-agent-run-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/restack/refs/heads/main/json-schema/restack-workflow-run-schema.json
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/restack/refs/heads/main/vocabulary/restack-vocabulary.yml
      - type: Documentation
        url: https://docs.restack.io/
      - type: Getting Started
        url: https://docs.restack.io/
      - type: GitHub Organization
        url: https://github.com/restackio
      - type: Python SDK
        url: https://github.com/restackio/examples-python
      - type: TypeScript SDK
        url: https://github.com/restackio/examples-typescript
      - type: Kubernetes Helm
        url: https://github.com/restackio/helm
      - type: Boilerplate
        url: https://github.com/restackio/boilerplate
common:
  - type: Website
    url: https://www.restack.io/
  - type: Documentation
    url: https://docs.restack.io/
  - type: GitHub Organization
    url: https://github.com/restackio
  - type: LinkedIn
    url: https://www.linkedin.com/company/restackio/
  - type: Python SDK
    url: https://github.com/restackio/examples-python
  - type: TypeScript SDK
    url: https://github.com/restackio/examples-typescript
  - type: Kubernetes Helm
    url: https://github.com/restackio/helm
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
