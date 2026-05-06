---
aid: hatchet
name: Hatchet
description: Hatchet is a distributed task queue and workflow engine for building resilient backend applications with durable execution.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Composition
  - Task Queue
  - Workflow Engine
url: https://raw.githubusercontent.com/api-evangelist/hatchet/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hatchet:hatchet-api
    name: Hatchet API
    description: Hatchet is a distributed task queue and workflow engine for building resilient backend applications with durable execution. The REST API exposes operations for tasks, workflow runs, events, filters, webhooks, tenants, workers, scheduled and cron workflows, alerting, and metadata.
    humanURL: https://docs.hatchet.run/
    tags:
      - API Composition
      - Background Tasks
      - Workflow Engine
      - Task Queue
      - Durable Execution
    properties:
      - type: Documentation
        url: https://docs.hatchet.run/
      - type: Getting Started
        url: https://docs.hatchet.run/home/quickstart
      - type: OpenAPI
        url: https://raw.githubusercontent.com/hatchet-dev/hatchet/main/api-contracts/openapi/openapi.yaml
      - type: SourceCode
        url: https://github.com/hatchet-dev/hatchet
      - type: SelfHosting
        url: https://docs.hatchet.run/self-hosting
common:
  - type: Website
    url: https://hatchet.run/
  - type: Documentation
    url: https://docs.hatchet.run/
  - type: GitHub Organization
    url: https://github.com/hatchet-dev
  - type: SourceCode
    url: https://github.com/hatchet-dev/hatchet
  - type: Pricing
    url: https://hatchet.run/pricing
  - type: Blog
    url: https://hatchet.run/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
